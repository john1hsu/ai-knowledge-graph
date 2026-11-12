#!/usr/bin/env python3
"""AI Knowledge Graph builder and validator.

Usage:
  python3 scripts/kg.py check            # validate only (exit 1 on errors)
  python3 scripts/kg.py build            # validate, then regenerate graph/
  python3 scripts/kg.py similar "Title" [--about "one-sentence definition"]
                                         # find existing articles close to a candidate topic

Articles live in articles/<domain>/<slug>.md with YAML frontmatter (see SCHEMA.md).
Generated outputs (never hand-edit): graph/graph.jsonld, graph/triples.nt,
graph/index.json, graph/frontier.md, graph/stats.md.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML missing: pip install pyyaml --break-system-packages")

ROOT = Path(__file__).resolve().parent.parent
ARTICLES = ROOT / "articles"
GRAPH = ROOT / "graph"
ONTOLOGY = ROOT / "ontology" / "ontology.ttl"

BASE = "https://github.com/john1hsu/ai-knowledge-graph/id/"
KTO = "https://github.com/john1hsu/ai-knowledge-graph/ontology#"
SKOS = "http://www.w3.org/2004/02/skos/core#"
PROV = "http://www.w3.org/ns/prov#"
RDF_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
RDFS_LABEL = "http://www.w3.org/2000/01/rdf-schema#label"
DCT = "http://purl.org/dc/terms/"

ID_RE = re.compile(r"^kt:[a-z0-9]+(?:-[a-z0-9]+)*$")
SOURCE_TYPES = {
    "peer-reviewed",     # conference/journal papers: NeurIPS, ICML, ICLR, ACL, CVPR, JMLR, Nature, Science
    "primary",           # the original paper (incl. the authors' arXiv version), technical reports, model/system cards
    "lab-research",      # research pages and blogs of AI labs: Anthropic, Google DeepMind, OpenAI, Meta AI, NVIDIA Research
    "official-docs",     # framework/product docs: PyTorch, Hugging Face, NVIDIA, Anthropic/OpenAI API docs, MCP spec
    "academic",          # university course notes and research centres: Stanford CS224N/CS231n, Stanford HAI AI Index, CMU, MIT
    "textbook",          # Russell & Norvig, Goodfellow et al. Deep Learning, Dive into Deep Learning (d2l.ai), Sutton & Barto
    "government",        # NIST (AI RMF), OMB memos, executive orders, EU AI Act text, UK AISI, CISA
    "intergovernmental", # OECD.AI, UNESCO
    "standards-body",    # ISO/IEC (42001, 22989), IEEE, W3C
    "encyclopedia",      # Britannica
    "preprint",          # arXiv preprints by third parties, not yet peer reviewed (weak)
    "news",              # reputable press, for announcements and events only (weak)
    "community",         # practitioner blogs, Medium, forums (weak)
}
STRONG_SOURCE_TYPES = SOURCE_TYPES - {"preprint", "news", "community"}
EVIDENCE_SOURCE_TYPES = {"peer-reviewed", "primary", "academic", "textbook", "government",
                         "intergovernmental", "standards-body"}
MATURITY = {"historical", "foundational", "established", "emerging", "frontier"}
REQUIRED = ["id", "type", "title", "domain", "summary", "sources", "created", "maturity"]
NEAR_DUP_THRESHOLD = 0.45   # shingle Jaccard on body text
TITLE_DUP_THRESHOLD = 0.85  # token Jaccard on normalized titles/aliases


# ---------------------------------------------------------------- helpers ---
def ontology_terms() -> tuple[set[str], set[str]]:
    text = ONTOLOGY.read_text()
    classes = set(re.findall(r"^kto:(\w+)\s+a owl:Class", text, re.M))
    props = set(re.findall(r"^kto:(\w+)\s+a owl:ObjectProperty", text, re.M))
    return classes, props


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    stop = {"the", "a", "an", "of", "and", "in", "on", "to", "for"}
    return " ".join(w for w in s.split() if w not in stop)


def tokens(s: str) -> set[str]:
    # crude stemming so "superconductors" ~ "superconductivity"
    return {w[:6] if len(w) > 6 else w.rstrip("s") for w in norm(s).split()}


def shingles(text: str, k: int = 5) -> set[int]:
    words = norm(re.sub(r"\[\^s\d+\]", " ", text)).split()
    return {hash(" ".join(words[i:i + k])) for i in range(max(0, len(words) - k + 1))}


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a and b else 0.0


def iri(node_id: str) -> str:
    return BASE + node_id.split(":", 1)[1]


def load_articles() -> tuple[list[dict], list[str]]:
    arts, errors = [], []
    for path in sorted(ARTICLES.rglob("*.md")):
        rel = path.relative_to(ROOT)
        raw = path.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
        if not m:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            errors.append(f"{rel}: bad YAML: {e}")
            continue
        fm["_path"], fm["_body"] = str(rel), m.group(2)
        arts.append(fm)
    return arts, errors


# ------------------------------------------------------------- validation ---
def validate(arts: list[dict]) -> list[str]:
    classes, props = ontology_terms()
    errs: list[str] = []
    ids: dict[str, str] = {}
    names: list[tuple[str, str, set]] = []

    for a in arts:
        p = a["_path"]
        for f in REQUIRED:
            if not a.get(f):
                errs.append(f"{p}: missing required field '{f}'")
        aid = a.get("id", "")
        if aid and not ID_RE.match(aid):
            errs.append(f"{p}: id '{aid}' must look like kt:lowercase-slug")
        if aid:
            if aid in ids:
                errs.append(f"{p}: duplicate id {aid} (also {ids[aid]})")
            ids[aid] = p
            slug = aid.split(":", 1)[1]
            if Path(p).stem != slug:
                errs.append(f"{p}: filename must be {slug}.md")
            dom = a.get("domain", "")
            if Path(p).parent.name != dom:
                errs.append(f"{p}: must live in articles/{dom}/")
        if a.get("type") and a["type"] not in classes:
            errs.append(f"{p}: type '{a['type']}' not in ontology classes {sorted(classes)}")

        for key in ("broader", "related"):
            for ref in a.get(key) or []:
                if not ID_RE.match(str(ref)):
                    errs.append(f"{p}: {key} ref '{ref}' is not a kt: id")
        for r in a.get("relations") or []:
            if not isinstance(r, dict) or set(r) != {"predicate", "object"}:
                errs.append(f"{p}: each relation needs exactly predicate + object")
                continue
            if r["predicate"] not in props:
                errs.append(f"{p}: predicate '{r['predicate']}' not in ontology (add it to ontology.ttl first)")
            if not ID_RE.match(str(r["object"])):
                errs.append(f"{p}: relation object '{r['object']}' is not a kt: id")

        if a.get("maturity") and a["maturity"] not in MATURITY:
            errs.append(f"{p}: maturity '{a['maturity']}' not in {sorted(MATURITY)}")

        # --- citations
        srcs = a.get("sources") or []
        sids = set()
        strong = 0
        urls = set()
        for s in srcs:
            if not isinstance(s, dict):
                errs.append(f"{p}: malformed source entry")
                continue
            for f in ("id", "title", "publisher", "url", "type", "accessed"):
                if not s.get(f):
                    errs.append(f"{p}: source {s.get('id', '?')} missing '{f}'")
            if s.get("id"):
                sids.add(s["id"])
            if s.get("url") and not str(s["url"]).startswith("https://"):
                errs.append(f"{p}: source {s.get('id')} url must be https")
            if s.get("url") in urls:
                errs.append(f"{p}: duplicate source url {s.get('url')}")
            urls.add(s.get("url"))
            if s.get("type") not in SOURCE_TYPES:
                errs.append(f"{p}: source {s.get('id')} type '{s.get('type')}' not in {sorted(SOURCE_TYPES)}")
            elif s["type"] in STRONG_SOURCE_TYPES:
                strong += 1
        if len(srcs) < 3:
            errs.append(f"{p}: needs at least 3 sources (has {len(srcs)})")
        if not any(isinstance(x, dict) and x.get("type") in EVIDENCE_SOURCE_TYPES for x in srcs):
            errs.append(f"{p}: needs at least 1 scholarly/primary/official source {sorted(EVIDENCE_SOURCE_TYPES)}")
        if strong < 2:
            errs.append(f"{p}: needs at least 2 sources of a strong type {sorted(STRONG_SOURCE_TYPES)}")
        body = a["_body"]
        cited = set(re.findall(r"\[\^(s\d+)\](?!:)", body))
        defined = set(re.findall(r"^\[\^(s\d+)\]:", body, re.M))
        for sid in sids - cited:
            errs.append(f"{p}: source {sid} is never cited in the body")
        for sid in cited - sids:
            errs.append(f"{p}: body cites [^{sid}] but it is not in frontmatter sources")
        for sid in sids - defined:
            errs.append(f"{p}: missing footnote definition [^{sid}]: in the Sources section")
        # every substantive paragraph must carry a citation
        prose = body.split("\n## Sources", 1)[0]
        for para in re.split(r"\n\s*\n", prose):
            t = para.strip()
            if not t or t.startswith("#") or t.startswith(">") or len(t) < 120:
                continue
            if "[^s" not in t:
                errs.append(f"{p}: uncited paragraph: '{t[:70]}...'")
        if len(re.findall(r"\w+", prose)) < 350:
            errs.append(f"{p}: body is under 350 words")

        names.append((p, a.get("title", ""), {norm(x) for x in [a.get("title", "")] + list(a.get("aliases") or [])}))

    # --- uniqueness: titles / aliases
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            pi, ti, ni = names[i]
            pj, tj, nj = names[j]
            if ni & nj:
                errs.append(f"{pi}: title/alias collides with {pj}: {sorted(ni & nj)}")
            elif jaccard(tokens(ti), tokens(tj)) >= TITLE_DUP_THRESHOLD:
                errs.append(f"{pi}: title too similar to {pj} ('{ti}' vs '{tj}')")
    # --- uniqueness: content
    sh = [(a["_path"], shingles(a["_body"])) for a in arts]
    for i in range(len(sh)):
        for j in range(i + 1, len(sh)):
            s = jaccard(sh[i][1], sh[j][1])
            if s >= NEAR_DUP_THRESHOLD:
                errs.append(f"{sh[i][0]}: near-duplicate of {sh[j][0]} (similarity {s:.2f})")
    return errs


# ------------------------------------------------------------------ build ---
def edges(a: dict):
    for b in a.get("broader") or []:
        yield SKOS + "broader", b
    for r in a.get("related") or []:
        yield SKOS + "related", r
    for r in a.get("relations") or []:
        yield KTO + r["predicate"], r["object"]


def lit(s: str) -> str:
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def build(arts: list[dict]) -> None:
    GRAPH.mkdir(exist_ok=True)
    known = {a["id"] for a in arts}
    triples, nodes, index = [], [], []
    inbound: Counter = Counter()
    frontier: dict[str, list[str]] = defaultdict(list)

    for a in arts:
        s = f"<{iri(a['id'])}>"
        triples += [
            f"{s} <{RDF_TYPE}> <{KTO}{a['type']}> .",
            f"{s} <{RDFS_LABEL}> {lit(a['title'])} .",
            f"{s} <{SKOS}prefLabel> {lit(a['title'])} .",
            f"{s} <{SKOS}definition> {lit(a['summary'])} .",
            f"{s} <{DCT}created> {lit(a['created'])} .",
            f"{s} <{KTO}maturity> {lit(a['maturity'])} .",
            f"{s} <{KTO}domain> {lit(a['domain'])} .",
        ]
        for al in a.get("aliases") or []:
            triples.append(f"{s} <{SKOS}altLabel> {lit(al)} .")
        node = {
            "@id": a["id"], "@type": f"kto:{a['type']}", "skos:prefLabel": a["title"],
            "skos:definition": a["summary"], "kto:domain": a["domain"], "dcterms:created": str(a["created"]),
            "kto:maturity": a["maturity"],
            "prov:wasDerivedFrom": [], "kto:file": a["_path"],
        }
        if a.get("aliases"):
            node["skos:altLabel"] = a["aliases"]
        for pred, obj in edges(a):
            triples.append(f"{s} <{pred}> <{iri(obj)}> .")
            key = pred.replace(SKOS, "skos:").replace(KTO, "kto:")
            node.setdefault(key, []).append({"@id": obj})
            inbound[obj] += 1
            if obj not in known:
                frontier[obj].append(a["id"])
        for src in a["sources"]:
            sid = f"<{BASE}source/{a['id'].split(':', 1)[1]}/{src['id']}>"
            triples += [
                f"{s} <{PROV}wasDerivedFrom> {sid} .",
                f"{sid} <{RDF_TYPE}> <{KTO}Source> .",
                f"{sid} <{DCT}title> {lit(src['title'])} .",
                f"{sid} <{DCT}publisher> {lit(src['publisher'])} .",
                f"{sid} <https://schema.org/url> {lit(src['url'])} .",
                f"{sid} <{KTO}sourceType> {lit(src['type'])} .",
            ]
            node["prov:wasDerivedFrom"].append({"dcterms:title": src["title"], "dcterms:publisher": src["publisher"],
                                                 "schema:url": src["url"], "kto:sourceType": src["type"]})
        nodes.append(node)
        index.append({"id": a["id"], "title": a["title"], "aliases": a.get("aliases") or [], "type": a["type"],
                      "domain": a["domain"], "file": a["_path"], "created": str(a["created"]),
                      "maturity": a["maturity"], "source_urls": [x["url"] for x in a["sources"]]})

    (GRAPH / "triples.nt").write_text("\n".join(sorted(set(triples))) + "\n")
    ctx = {"kt": BASE, "kto": KTO, "skos": SKOS, "prov": PROV, "dcterms": DCT, "schema": "https://schema.org/",
           "@base": BASE}
    (GRAPH / "graph.jsonld").write_text(json.dumps({"@context": ctx, "@graph": nodes}, indent=2, ensure_ascii=False) + "\n")
    (GRAPH / "index.json").write_text(json.dumps(sorted(index, key=lambda x: x["id"]), indent=2, ensure_ascii=False) + "\n")

    # frontier: referenced-but-unwritten nodes, best candidates for the next article
    fl = sorted(frontier.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    lines = ["# Frontier", "", "Nodes referenced by existing articles but not yet written, ranked by how many "
             "articles point to them. Generated by `scripts/kg.py build`.", ""]
    if fl:
        lines += ["| Node | Referenced by |", "|---|---|"]
        lines += [f"| `{k}` | {', '.join(f'`{x}`' for x in v)} |" for k, v in fl]
    else:
        lines.append("_Empty._")
    (GRAPH / "frontier.md").write_text("\n".join(lines) + "\n")

    # stats + centrality
    by_type = Counter(a["type"] for a in arts)
    by_dom = Counter(a["domain"] for a in arts)
    out = ["# Graph statistics", "", f"- Articles (nodes written): **{len(arts)}**",
           f"- Frontier nodes (referenced, unwritten): **{len(frontier)}**",
           f"- Edges: **{sum(1 for a in arts for _ in edges(a))}**",
           f"- Citations: **{sum(len(a['sources']) for a in arts)}**", ""]
    try:
        import networkx as nx
        g = nx.DiGraph()
        g.add_nodes_from(a["id"] for a in arts)
        for a in arts:
            for _, o in edges(a):
                g.add_edge(a["id"], o)
        if g.number_of_nodes():
            pr = nx.pagerank(g)
            comps = list(nx.weakly_connected_components(g))
            iso = [n for n in known if g.degree(n) == 0]
            out += [f"- Weakly connected components: **{len(comps)}**",
                    f"- Isolated articles (no edges): **{len(iso)}**", "",
                    "## Most central nodes (PageRank)", "", "| Node | PageRank | Written |", "|---|---|---|"]
            out += [f"| `{n}` | {v:.4f} | {'yes' if n in known else 'no'} |"
                    for n, v in sorted(pr.items(), key=lambda kv: -kv[1])[:15]]
            try:
                comms = nx.algorithms.community.louvain_communities(g.to_undirected(), seed=42)
                out += ["", f"## Communities (Louvain): {len(comms)}", ""]
                for i, c in enumerate(sorted(comms, key=len, reverse=True)[:10], 1):
                    out.append(f"{i}. " + ", ".join(f"`{x}`" for x in sorted(c)[:12]) + (" …" if len(c) > 12 else ""))
            except Exception:
                pass
            out.append("")
    except ImportError:
        out += ["_(install networkx for centrality and community metrics)_", ""]
    out += ["## By type", ""] + [f"- {k}: {v}" for k, v in sorted(by_type.items())]
    out += ["", "## By domain", ""] + [f"- {k}: {v}" for k, v in sorted(by_dom.items())]
    out += ["", "## By maturity (emerging/frontier nodes go stale fastest)", ""]
    out += [f"- {k}: {v}" for k, v in sorted(Counter(a["maturity"] for a in arts).items())]
    (GRAPH / "stats.md").write_text("\n".join(out) + "\n")


# ------------------------------------------------------------ similarity ---
# `similar` scores a candidate topic against every article on two signals:
#   name  - IDF-weighted token overlap with the article's title and aliases
#           (common words such as "model" or "learning" count for little; an
#           acronym that spells out a title, e.g. RLHF, counts as a match), and
#   about - TF-IDF cosine between the candidate's description (--about) and the
#           article's title, aliases and summary, i.e. what the article is about.
# With --about, score = 0.4 * name + 0.6 * about, so two topics that merely
# share words ("Deep reinforcement learning" vs "Deep learning") stay below the
# review threshold while a reworded duplicate of an existing article rises above
# it. An exact title, alias or acronym match always scores 1.0. Without --about
# only the name signal is available. Plain character overlap is no longer used:
# it made unrelated short titles ("LLM-as-a-judge" vs "AI agent") score >= 0.5.
SIM_REVIEW_THRESHOLD = 0.5
NAME_WEIGHT = 0.4


def _idf(docs: list[set[str]]) -> dict[str, float]:
    import math
    df = Counter(t for d in docs for t in d)
    n = len(docs)
    return defaultdict(lambda: math.log(n + 1) + 1, {t: math.log((n + 1) / (c + 1)) + 1 for t, c in df.items()})


def _tok_eq(a: str, b: str) -> bool:
    if a == b:
        return True
    if min(len(a), len(b)) < 5:
        return False
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, b).ratio() >= 0.85


def _acronym(s: str) -> str:
    return "".join(w[0] for w in norm(s).split() if w)


def name_sim(query: str, label: str, idf: dict[str, float]) -> float:
    q, l = norm(query).replace(" ", ""), norm(label).replace(" ", "")
    if not q or not l:
        return 0.0
    if q == l:
        return 1.0
    # acronym <-> expansion ("RLHF" vs "reinforcement learning from human feedback")
    if (len(norm(query).split()) == 1 and len(q) >= 2 and q == _acronym(label)) or \
       (len(norm(label).split()) == 1 and len(l) >= 2 and l == _acronym(query)):
        return 1.0
    qt, lt = tokens(query), tokens(label)
    if not qt or not lt:
        return 0.0
    wq = sum(idf[t] for t in qt)
    wl = sum(idf[t] for t in lt)
    mq = sum(idf[t] for t in qt if any(_tok_eq(t, u) for u in lt))
    ml = sum(idf[u] for u in lt if any(_tok_eq(u, t) for t in qt))
    return (mq + ml) / (wq + wl)  # IDF-weighted Dice overlap


def _vec(text: str, idf: dict[str, float]) -> dict[str, float]:
    import math
    tf = Counter(tokens_list(text))
    v = {t: (1 + math.log(c)) * idf[t] for t, c in tf.items()}
    n = math.sqrt(sum(x * x for x in v.values())) or 1.0
    return {t: x / n for t, x in v.items()}


def tokens_list(s: str) -> list[str]:
    return [w[:6] if len(w) > 6 else w.rstrip("s") for w in norm(s).split()]


def _profile(a: dict) -> str:
    labels = " ".join([a.get("title", "")] + list(a.get("aliases") or []))
    return f"{labels} {a.get('summary', '')}"


def similar(query: str, arts: list[dict], about: str = "") -> None:
    # IDF over title + aliases + summary, so generic words ("model", "network",
    # "evaluation") that appear across many articles carry little weight.
    text_idf = label_idf = _idf([set(tokens_list(_profile(a))) for a in arts])
    qv = _vec(f"{query} {about}", text_idf) if about else None
    phrase = norm(query)
    scored = []
    for a in arts:
        labels = [a.get("title", "")] + list(a.get("aliases") or [])
        name = max(name_sim(query, x, label_idf) for x in labels)
        content = 0.0
        if qv is not None:
            av = _vec(_profile(a), text_idf)
            content = sum(x * av.get(t, 0.0) for t, x in qv.items())
        mentions = len(re.findall(r"\b" + re.escape(phrase) + r"\b", norm(a["_body"]))) if phrase else 0
        if qv is None or name >= 0.95:   # exact title/alias/acronym match always counts in full
            score = name
        else:                             # otherwise meaning outweighs shared words
            score = NAME_WEIGHT * name + (1 - NAME_WEIGHT) * content
        scored.append((score, name, content, mentions, a.get("id"), a.get("title")))
    scored.sort(key=lambda x: (x[0], x[3]), reverse=True)
    hits = [x for x in scored if x[0] >= 0.2][:10]
    if not hits:
        print("No similar articles. Topic looks unique.")
    else:
        print("score  name  about  mentions  node")
    for s, n, c, m, i, t in hits:
        flag = "  <- review" if s >= SIM_REVIEW_THRESHOLD else ""
        about_col = f"{c:.2f}" if qv is not None else "  - "
        print(f"{s:.2f}   {n:.2f}  {about_col}  {m:>8}  {i}  {t}{flag}")
    mentioned = sorted((x for x in scored if x[3] and x not in hits), key=lambda x: -x[3])[:5]
    if mentioned:
        print("Also mention the phrase in their body: " + ", ".join(f"{x[4]} ({x[3]}x)" for x in mentioned))
    if qv is None:
        print('Name-only check. Add --about "<one-sentence definition>" to also compare against what each '
              'article is about; shared words alone are weak evidence of a duplicate.')


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    arts, errs = load_articles()
    if cmd == "similar":
        args, about = sys.argv[2:], ""
        if "--about" in args:
            k = args.index("--about")
            about = " ".join(args[k + 1:])
            args = args[:k]
        similar(" ".join(args), arts, about)
        return 0
    errs += validate(arts) if not errs else []
    if errs:
        print(f"{len(errs)} problem(s):")
        for e in errs:
            print("  -", e)
        return 1
    print(f"OK: {len(arts)} article(s) valid.")
    if cmd == "build":
        build(arts)
        print("Graph regenerated in graph/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
