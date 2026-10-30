# Article schema

Each article is one **node** in the graph: `articles/<domain>/<slug>.md`, where the filename equals the id's slug and `<domain>` is a key in `topics/seeds.yaml`.

```markdown
---
id: kt:self-attention                  # stable node id: kt: + lowercase-hyphen slug
type: Architecture                     # a class from ontology/ontology.ttl
title: Self-attention
aliases: [intra-attention, scaled dot-product attention]
domain: transformers-and-llms          # a domain key from topics/seeds.yaml
summary: >-                            # 1–2 sentence definition (becomes skos:definition)
  A mechanism that lets each position in a sequence weigh every other position when computing its representation.
maturity: established                  # historical | foundational | established | emerging | frontier
broader: [kt:attention-mechanism]
related: [kt:positional-encoding]
relations:                             # typed edges; predicates must exist in the ontology
  - {predicate: introducedIn, object: kt:attention-is-all-you-need}
  - {predicate: partOf, object: kt:transformer-architecture}
  - {predicate: alternativeTo, object: kt:recurrent-neural-network}
sources:                               # >= 3 total, >= 2 strong, >= 1 scholarly/primary/official
  - id: s1
    title: "Attention Is All You Need"
    publisher: NeurIPS 2017 (Vaswani et al.)
    url: https://papers.nips.cc/paper/7181-attention-is-all-you-need
    type: peer-reviewed
    accessed: 2026-10-30
created: 2026-10-30
---

# Self-attention

Prose with inline footnote citations after each claim.[^s1]

## How it works
Mechanism, with a formula or small worked example where it helps.[^s1]

## Why it matters / limitations
Evidence, trade-offs, known failure modes, open questions.[^s2]

## In practice
Where it's used today, tools that implement it, dated figures.[^s3]

## Connections
How this node relates to its neighbours, in prose, with citations.

## Sources
[^s1]: Vaswani et al., "Attention Is All You Need", NeurIPS 2017. https://papers.nips.cc/... (accessed 2026-10-30)
```

## Maturity

| value | meaning |
|---|---|
| historical | mainly of historical interest (expert systems, AI winters) |
| foundational | bedrock theory unlikely to change (gradient descent, MDPs) |
| established | widely adopted, settled practice (transformers, LoRA, RAG) |
| emerging | in active adoption, practice still shifting (agent protocols, reasoning models) |
| frontier | recent research or announcements; most likely to go stale |

## Rules enforced by `scripts/kg.py check`

- Required fields: `id, type, title, domain, summary, sources, created, maturity`.
- `type` must be a class, and every `relations.predicate` a property, in `ontology/ontology.ttl`.
- Every edge target is a `kt:` id. Targets with no article yet become **frontier** nodes (`graph/frontier.md`).
- Citations: at least 3 sources; at least 2 of a strong type; at least 1 scholarly, primary or official source (`peer-reviewed, primary, academic, textbook, government, intergovernmental, standards-body`); https only; no duplicate URLs; every source cited in the body and defined in `## Sources`; every substantive paragraph cited.
- Body of at least 350 words.
- Uniqueness: no duplicate ids, titles or aliases; no near-paraphrase titles; no bodies that overlap another article above the similarity threshold.

## Source types

| type | strong? | examples |
|---|---|---|
| peer-reviewed | yes | NeurIPS, ICML, ICLR, ACL, EMNLP, CVPR proceedings; JMLR, Nature, Science (prefer the proceedings or DOI page) |
| primary | yes | the original paper (including the authors' own arXiv version), technical reports, model cards and system cards |
| lab-research | yes | research pages and blogs of Anthropic, Google DeepMind, OpenAI, Meta AI, Microsoft Research, NVIDIA Research |
| official-docs | yes | PyTorch, Hugging Face, NVIDIA developer docs, Anthropic/OpenAI API docs, the MCP specification |
| academic | yes | Stanford CS224N/CS231n notes, Stanford HAI AI Index, university research centres |
| textbook | yes | Russell & Norvig *AIMA*, Goodfellow et al. *Deep Learning*, *Dive into Deep Learning* (d2l.ai), Sutton & Barto |
| government | yes | NIST (AI RMF), OMB memoranda, executive orders, EU AI Act official text, UK AISI, CISA |
| intergovernmental | yes | OECD.AI, UNESCO |
| standards-body | yes | ISO/IEC 42001 and 22989, IEEE |
| encyclopedia | yes | Britannica |
| preprint | no | third-party arXiv preprints not yet peer reviewed |
| news | no | reputable press, for announcements and events only |
| community | no | practitioner blogs, Medium, forums |

Never cite Wikipedia, content farms, SEO listicles, or AI-generated pages.
