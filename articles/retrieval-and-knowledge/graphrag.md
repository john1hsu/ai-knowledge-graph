---
id: kt:graphrag
type: Technique
title: GraphRAG
aliases: [Graph RAG, graph-based retrieval-augmented generation, Microsoft GraphRAG]
domain: retrieval-and-knowledge
summary: >-
  A retrieval-augmented generation approach from Microsoft Research that uses an LLM to extract an entity
  knowledge graph from a corpus, partitions it into a hierarchy of communities with pre-written summaries,
  and answers corpus-wide "sensemaking" questions by map-reducing over those summaries.
maturity: emerging
broader: [kt:retrieval-augmented-generation]
related: [kt:knowledge-graph, kt:semantic-search, kt:vector-database, kt:context-window, kt:hallucination, kt:llm-as-a-judge]
relations:
  - {predicate: createdBy, object: kt:microsoft-research}
  - {predicate: introducedIn, object: kt:from-local-to-global-a-graphrag-approach-to-query-focused-summarization}
  - {predicate: dependsOn, object: kt:leiden-algorithm}
  - {predicate: basedOn, object: kt:large-language-model}
  - {predicate: alternativeTo, object: kt:lazygraphrag}
sources:
  - id: s1
    title: "From Local to Global: A GraphRAG Approach to Query-Focused Summarization"
    publisher: arXiv:2404.16130 v2 (Edge, Trinh, Cheng, Bradley, Chao, Mody, Truitt, Metropolitansky, Ness and Larson; Microsoft)
    url: https://arxiv.org/html/2404.16130v2
    type: primary
    accessed: 2026-11-16
  - id: s2
    title: "Query Engine"
    publisher: Microsoft GraphRAG official documentation
    url: https://microsoft.github.io/graphrag/query/overview
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "LazyGraphRAG: Setting a new standard for quality and cost"
    publisher: Microsoft Research Blog (Edge, Trinh and Larson), 25 November 2024, updated 6 June 2025
    url: https://microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost
    type: lab-research
    accessed: 2026-11-16
  - id: s4
    title: "From Louvain to Leiden: guaranteeing well-connected communities"
    publisher: Scientific Reports 9, 5233 (2019) (Traag, Waltman and van Eck); PubMed Central
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC6435756
    type: peer-reviewed
    accessed: 2026-11-16
created: 2026-11-16
---

# GraphRAG

**GraphRAG** is a graph-based variant of retrieval-augmented generation developed at Microsoft and described in the 2024 paper "From Local to Global" by Darren Edge, Jonathan Larson and colleagues.[^s1] Its motivation is a blind spot of ordinary vector RAG: retrieving the few chunks nearest to a query works for pointed factual questions, but fails on global questions such as "what are the main themes of this corpus?", whose answer is spread across the whole collection rather than sitting in any single passage.[^s1] The authors frame those as query-focused summarization (or "sensemaking") tasks and note that earlier summarization methods did not scale to the corpus sizes RAG systems index.[^s1]

## How it works

Indexing happens in stages, all ahead of query time.[^s1]

1. **Chunking.** Documents are cut into overlapping text chunks; the paper's experiments used 600-token chunks with 100-token overlap, noting that larger chunks save LLM calls but lose recall.[^s1]
2. **Graph extraction.** An LLM reads each chunk and emits entities, relationships between them, short descriptions and factual claims. A "gleaning" loop re-prompts the model to check whether it missed entities. Nodes are merged by exact string match, and edge weights count how often a relationship recurs.[^s1]
3. **Community detection.** The resulting graph is partitioned hierarchically with the Leiden algorithm, recursing into sub-communities until they cannot be split further.[^s1] Leiden, published by Traag, Waltman and van Eck in 2019, fixes a flaw in the older Louvain method, which can return badly connected or even disconnected communities; Leiden guarantees connected communities and was reported to run faster.[^s4]
4. **Community summaries.** The LLM writes a report for every community, bottom-up: leaf reports prioritise high-degree entities, while higher levels substitute their children's shorter summaries when the context limit is reached.[^s1]

To answer a global question, the system shuffles and batches community summaries at a chosen level of the hierarchy. In a **map** step each batch yields a partial answer with a 0–100 helpfulness score, zero-scored answers are dropped, and a **reduce** step merges the remaining answers, highest-scored first, into the final response.[^s1]

The open-source implementation exposes several query modes. Global search is the map-reduce method above; local search combines graph entities with raw text chunks for questions about specific entities; DRIFT search extends local search with community context and generated follow-up questions; and basic search is a plain vector-RAG baseline for comparison.[^s2]

## Evidence and limitations

The paper evaluated two corpora of roughly 1 million tokens (podcast transcripts) and 1.7 million tokens (news articles), with 125 LLM-generated sensemaking questions per dataset and an LLM judge comparing answers pairwise.[^s1] Against vector RAG, the global methods won 72–83% of comprehensiveness comparisons on podcasts and 72–80% on news, and also won most diversity comparisons, though vector RAG gave the most direct answers.[^s1] Root-level community summaries needed about 97% fewer context tokens per query than map-reducing over the raw source text.[^s1]

The authors list clear limits: only two corpora were tested, fabrication rates were not measured, the evaluation relies on LLM judges, and entity matching is exact-string only.[^s1] Cost is the main practical objection. Building the podcast index took 281 minutes with GPT-4 Turbo, because every chunk passes through an LLM.[^s1] Microsoft's own follow-up described the up-front indexing cost of full GraphRAG as potentially prohibitive for some uses, and its global search as expensive per query.[^s3]

## In practice

Microsoft released GraphRAG as open source, and the paper notes integrations with LangChain, LlamaIndex, NebulaGraph and Neo4j.[^s1] In November 2024 Microsoft Research announced **LazyGraphRAG**, which replaces LLM extraction with cheaper noun-phrase extraction and skips index-time summarization, deferring LLM work to query time.[^s3] Microsoft claims its indexing cost matches vector RAG and is 0.1% of full GraphRAG's, and that it matches GraphRAG global-search quality at more than 700 times lower query cost; these are the lab's own results, judged by an LLM on a news-article benchmark.[^s3] The same post argues that a fully summarised index still has value, for example for generating reports.[^s3]

## Connections

GraphRAG is a specialisation of **retrieval-augmented generation**, and its graph is a form of **knowledge graph** built automatically by a **large language model** rather than curated by hand.[^s1] It contrasts with **semantic search** over a **vector database**, which the paper uses as its baseline, and it works around the limited **context window** by summarising communities instead of stuffing raw text into the prompt.[^s1] It **depends on** the **Leiden algorithm** for its community hierarchy,[^s4] was **created by Microsoft Research** and **introduced in** the "From Local to Global" paper, and was evaluated with **LLM-as-a-judge** comparisons.[^s1] The authors flag unmeasured **hallucination** as an open question,[^s1] and **LazyGraphRAG** is Microsoft's cheaper alternative design, which the lab presents as complementary rather than a full replacement.[^s3]

## Sources

[^s1]: Edge et al., "From Local to Global: A GraphRAG Approach to Query-Focused Summarization", arXiv:2404.16130v2. https://arxiv.org/html/2404.16130v2 (accessed 2026-11-16)
[^s2]: Microsoft, "Query Engine", GraphRAG documentation. https://microsoft.github.io/graphrag/query/overview (accessed 2026-11-16)
[^s3]: Edge, Trinh and Larson, "LazyGraphRAG: Setting a new standard for quality and cost", Microsoft Research Blog, 25 Nov 2024. https://microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost (accessed 2026-11-16)
[^s4]: Traag, Waltman and van Eck, "From Louvain to Leiden: guaranteeing well-connected communities", Scientific Reports 9, 5233 (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6435756 (accessed 2026-11-16)
