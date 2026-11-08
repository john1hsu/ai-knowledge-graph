# AI Knowledge Graph — run playbook

This repo is a citation-backed knowledge graph of artificial intelligence: ML foundations, deep learning, transformers and LLMs, training and inference, retrieval, agents, prompting, evaluation, safety and security, governance and policy, vision and multimodal, reinforcement learning, infrastructure, and AI history. An hourly scheduled run adds **exactly one new, unique article** per run. Follow these steps in order. Read `SCHEMA.md` before writing.

## 1. Sync and orient
```bash
git pull --rebase origin main
python3 scripts/kg.py build      # must print OK; fix the repo first if it doesn't
```
Read `graph/stats.md`, `graph/frontier.md` and `topics/seeds.yaml`. `graph/index.json` lists every existing node (ids, titles, aliases, maturity, source URLs).

## 2. Pick the topic (graph-driven)
Use the current UTC hour:
- **Even hour → depth.** Take the highest-ranked node in `graph/frontier.md` (referenced by the most articles but not yet written) that fits a domain in `topics/seeds.yaml`, **skipping any node that would belong to the domain with the most articles** (see `graph/stats.md`; on a tie for most, skip all tied domains). This turns dangling edges into real nodes without letting one domain's dense cross-links snowball into a lopsided graph.
- **Odd hour → breadth.** Take the domain in `topics/seeds.yaml` with the fewest articles (ties: alphabetical, skipping the domain of the most recent commit) and pick an unwritten seed topic, or another important topic in that domain.
- If no frontier node fits, do a breadth run.
- Write every new article under one of the domains in `topics/seeds.yaml`.

Then prove it is unique:
```bash
python3 scripts/kg.py similar "<candidate title>"
```
If any score ≥ 0.5, or an existing title/alias names the same thing, pick a different topic. Never write a second article on a subject that already has a node — not a rename, a sub-angle that restates it, an acronym (e.g. "RLHF" vs "reinforcement learning from human feedback"), or a synonym. Record alternate names and acronyms as `aliases`.

## 3. Research
- Run several web searches; read the actual pages (WebFetch), don't rely on snippets or memory.
- Collect 3–6 credible sources: at least 1 scholarly, primary or official source and at least 2 of a strong type (see `SCHEMA.md`). Prefer the original paper that introduced the idea (proceedings page or the authors' arXiv version), peer-reviewed surveys, textbooks, official framework docs, and government/standards texts for policy topics. **Never cite Wikipedia**, content farms, SEO listicles, or AI-generated pages.
- Every URL you cite must be one you actually opened this run. Never invent or guess a URL or an arXiv ID.
- Date every time-sensitive figure (benchmark scores, model sizes, adoption numbers, rankings): "as of 2026", "reported in the 2025 AI Index". Don't present one lab's marketing claims as settled fact; attribute them.
- Set `maturity` honestly; use `frontier` for anything announced in roughly the last year.
- Paraphrase. No quotation longer than 15 words; at most one quote per source.

## 4. Write the node
- Path `articles/<domain>/<slug>.md`, id `kt:<slug>`. Pick the most specific `type` from the ontology.
- 350–900 words, practitioner level: definition, origin (who introduced it, in which paper, when), how it works (a formula or small example where it helps), limitations and open questions, how it's used in practice, and a **Connections** section explaining the edges.
- Every factual paragraph carries footnote citations `[^sN]`; list all sources in `## Sources`.
- Edges: 1–3 `broader`, 2–6 `related` or typed `relations`. Use typed predicates where they fit (`introducedIn`, `createdBy`, `basedOn`, `extends`, `supersededBy`, `trainedWith`, `evaluatedOn`, `implementedIn`, `runsOn`, `mitigates`, `exploits`, `regulatedBy`, …). **Link to existing node ids wherever they fit** (check `graph/index.json`); new target ids are fine and join the frontier.
- If a needed predicate or class is missing, add it to `ontology/ontology.ttl` (with a label and, if applicable, inverse) in the same commit. Keep the ontology small; reuse before adding.
- Back-links: if the new node is a natural child or relative of an existing article, you may add its id to that article's `related` list. Don't otherwise rewrite existing articles.

## 5. Validate, build, commit, push
```bash
python3 scripts/kg.py build    # fix every reported problem, then re-run until OK
git add -A
git commit -m "Add <Title> (<domain>)"
git pull --rebase origin main && git push origin main
```
If the push is rejected, pull --rebase, rebuild, and push again (once). Commit generated `graph/` files with the article.

## Don'ts
- Don't add more than one article per run, delete articles, or rewrite history.
- Don't commit if validation fails; leave the repo clean.
- Don't cite a source you didn't open.
- Don't write operational instructions for attacks (working jailbreak prompts, exploit code, weaponization details). Security and safety topics are covered at the level of concepts, impacts and mitigations.
