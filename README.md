# AI Knowledge Graph

A growing, citation-backed knowledge graph of artificial intelligence, from ML foundations and AI history to transformers, LLMs, agents, safety, governance and infrastructure. An hourly scheduled run researches one new topic, writes it as a node with typed edges to the rest of the graph, validates it, and commits it.

## How it's organized

| Layer | What | Where |
|---|---|---|
| Ontology | AI classes (Architecture, Algorithm, Technique, Paradigm, Model, Dataset, Benchmark, Tool, Hardware, Risk, Policy, Work, Event, …) and typed relations (introducedIn, basedOn, extends, supersededBy, trainedWith, evaluatedOn, implementedIn, runsOn, mitigates, exploits, regulatedBy, …) on RDFS/OWL, SKOS and PROV-O | `ontology/ontology.ttl` |
| Nodes | One Markdown article per entity, with YAML frontmatter holding its id, class, hierarchy, typed edges, maturity and per-article provenance | `articles/<domain>/` |
| Graph exports | Linked-data exports regenerated on every commit: JSON-LD, N-Triples, an index | `graph/graph.jsonld`, `graph/triples.nt`, `graph/index.json` |
| Analytics | PageRank centrality, Louvain communities, connected components, coverage by type, domain and maturity | `graph/stats.md` |
| Frontier | Nodes existing articles point to but nobody has written yet; the hourly run alternates between expanding this (depth) and the least-covered domain (breadth) | `graph/frontier.md` |

## Guarantees enforced by `scripts/kg.py`

- **Cited:** at least 3 sources per article, at least 2 strong and at least 1 scholarly, primary or official (original papers, peer-reviewed proceedings, textbooks, NIST/ISO/government texts); every source is cited and every substantive paragraph carries a citation.
- **Dated:** every node records its maturity (historical → frontier), so fast-moving topics are easy to find and refresh.
- **Unique:** no duplicate ids, titles or aliases (acronyms count); near-paraphrase titles and overlapping text are rejected.
- **Well-formed:** classes and predicates must exist in the ontology.

```bash
pip install pyyaml networkx
python3 scripts/kg.py check              # validate
python3 scripts/kg.py build              # validate + regenerate graph/
python3 scripts/kg.py similar "Topic"    # check a candidate for duplicates
```

Steer what gets written by editing `topics/seeds.yaml`. The run playbook is `CLAUDE.md`; the article format is `SCHEMA.md`. The `.nt` and `.jsonld` exports load into RDF tools (Apache Jena, GraphDB, rdflib) or Neo4j via n10s.
