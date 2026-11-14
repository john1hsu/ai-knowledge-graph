---
id: kt:hybrid-search
type: Technique
title: Hybrid search
aliases: [hybrid retrieval, sparse-dense retrieval, hybrid sparse-dense search, lexical-semantic hybrid search]
domain: retrieval-and-knowledge
summary: >-
  A retrieval approach that runs a lexical (sparse, keyword) search such as BM25 and a dense vector
  similarity search over the same collection, then fuses the two ranked lists into a single ranking,
  typically by weighted score combination or reciprocal rank fusion.
maturity: established
broader: [kt:information-retrieval]
related: [kt:semantic-search, kt:reranking, kt:vector-database]
relations:
  - {predicate: basedOn, object: kt:bm25}
  - {predicate: basedOn, object: kt:reciprocal-rank-fusion}
  - {predicate: dependsOn, object: kt:embeddings}
  - {predicate: usedIn, object: kt:retrieval-augmented-generation}
  - {predicate: evaluatedOn, object: kt:beir}
  - {predicate: influencedBy, object: kt:dense-passage-retrieval}
sources:
  - id: s1
    title: "Dense Passage Retrieval for Open-Domain Question Answering"
    publisher: arXiv:2004.04906 (Karpukhin, Oguz, Min, Lewis, Wu, Edunov, Chen and Yih); EMNLP 2020
    url: https://arxiv.org/pdf/2004.04906.pdf
    type: primary
    accessed: 2026-11-14
  - id: s2
    title: "A Replication Study of Dense Passage Retriever"
    publisher: arXiv:2104.05740 (Ma, Sun, Pradeep and Lin, University of Waterloo)
    url: https://arxiv.org/pdf/2104.05740
    type: preprint
    accessed: 2026-11-14
  - id: s3
    title: "BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models"
    publisher: NeurIPS 2021 Datasets and Benchmarks Track (Thakur, Reimers, Rücklé, Srivastava and Gurevych)
    url: https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/65b9eea6e1cc6bb9f0cd2a47751a186f-Paper-round2.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "Reciprocal rank fusion outperforms condorcet and individual rank learning methods"
    publisher: SIGIR 2009, pages 758-759 (Cormack, Clarke and Buettcher); Google Research publication page
    url: https://research.google/pubs/pub36196/
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "Reciprocal rank fusion (Elasticsearch Reference 8.19)"
    publisher: Elastic
    url: https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rrf.html
    type: official-docs
    accessed: 2026-11-14
  - id: s6
    title: "Hybrid search (concepts)"
    publisher: Weaviate documentation
    url: https://docs.weaviate.io/weaviate/concepts/search/hybrid-search
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# Hybrid search

**Hybrid search** combines two kinds of first-stage retrieval over the same corpus: a sparse lexical retriever that scores exact term overlap (classically BM25) and a dense retriever that scores the similarity of learned query and document embeddings. The two candidate lists are merged into one ranking. The motivation is that the two signals fail in different places. Lexical matching is precise on rare names, codes and exact phrases, while dense matching captures paraphrase and synonymy that share no words.[^s1][^s2] Hybrid search is now a standard first stage for search engines and for retrieval-augmented generation pipelines, and it is exposed as a built-in query mode in systems such as Elasticsearch and Weaviate.[^s5][^s6]

## Origin and evidence

The modern sparse-dense pattern was popularised by work on neural passage retrieval for question answering. The Dense Passage Retrieval (DPR) paper of 2020 took the top 2,000 passages from BM25 and the top 2,000 from DPR and reranked their union by a linear combination of BM25 score and λ times the dense dot-product score, with λ set to 1.1 on development data.[^s1] In that paper the hybrid did not clearly beat dense retrieval alone on Natural Questions (76.6% versus 78.4% top-20 accuracy, against 59.1% for BM25), but BM25 beat DPR on SQuAD, where questions were written while looking at the passage and therefore share much of its vocabulary.[^s1]

A University of Waterloo replication (Ma, Sun, Pradeep and Lin, 2021) reached a different conclusion: with a stronger BM25 baseline and tuned fusion weights, hybrid retrieval gave statistically significant gains over DPR on nearly every dataset tested, for example raising top-20 accuracy on Natural Questions from 79.5 to 82.6. The authors observed that the top results of the sparse and dense retrievers overlap little, suggesting the two exploit different relevance signals.[^s2] The BEIR benchmark (NeurIPS 2021, 18 datasets) added a generalisation argument: BM25 stayed a strong zero-shot baseline, and many dense models that beat it on in-domain MS MARCO data fell below it under domain shift.[^s3] Combining the two hedges against that failure mode.

## How it works

Both retrievers run in parallel, each returning its own top-k list, and a fusion step produces the final order.[^s2][^s6] There are two main families of fusion.

- **Score fusion.** Each list's scores are put on a common scale and summed with a weight. Weaviate, for instance, min-max normalises each list so the best score becomes 1 and the worst 0, then sums the scaled scores. Its `alpha` parameter runs from 0 (keyword only) to 1 (vector only), with 0.75 as the server default.[^s6] The replication study tested both raw and normalised score sums and found no significant difference between them.[^s2]
- **Rank fusion.** Only positions are used, which sidesteps the fact that BM25 scores and cosine similarities live on unrelated scales. Reciprocal rank fusion (RRF), introduced by Cormack, Clarke and Buettcher at SIGIR 2009, scores each document by summing 1/(k + rank) over the lists that contain it.[^s4][^s5] Elasticsearch implements RRF with a default rank constant k of 60; a larger k gives lower-ranked documents more influence. Its documentation describes RRF as needing no tuning and as able to combine relevance indicators that are unrelated to each other.[^s5]

Weaviate used rank-based fusion as its default up to version 1.23 and switched to relative score fusion from 1.24, arguing that normalised scores retain more information than ranks alone.[^s6]

## Limitations and practical notes

Hybrid search roughly doubles first-stage work and adds parameters (the weight, the rank constant, the per-list depth) that must be validated on in-domain queries. Gains are not uniform: even in the replication study, the hybrid improved end-to-end answer accuracy on TriviaQA but left Natural Questions essentially unchanged.[^s2] Fusion also cannot rescue a document that neither retriever surfaced, so the candidate depth per list matters; the DPR experiments fused the top 2,000 results from each retriever and the replication the top 1,000.[^s1][^s2] For the highest precision, practitioners usually follow hybrid retrieval with a cross-encoder reranker, which BEIR found to be the most accurate configuration but also among the slowest, at over 350 ms per query in its 2021 measurements.[^s3]

## Connections

Hybrid search is a technique within **information retrieval** that is **based on** **BM25** for its lexical half and on **reciprocal rank fusion** or score fusion to merge results.[^s4][^s5] Its dense half **depends on** **embeddings**, typically stored and searched in a **vector database**, and it extends plain **semantic search** with a keyword signal.[^s6] The approach was shaped by experiments around **dense passage retrieval**, and its value is commonly argued from zero-shot results on **BEIR**.[^s1][^s3] It is **used in** **retrieval-augmented generation** to choose which passages an LLM reads, and its output is often passed to a **reranking** stage.[^s2][^s3]

## Sources
[^s1]: Karpukhin et al., "Dense Passage Retrieval for Open-Domain Question Answering", arXiv:2004.04906 (EMNLP 2020). https://arxiv.org/pdf/2004.04906.pdf (accessed 2026-11-14)
[^s2]: Ma, Sun, Pradeep and Lin, "A Replication Study of Dense Passage Retriever", arXiv:2104.05740, 2021. https://arxiv.org/pdf/2104.05740 (accessed 2026-11-14)
[^s3]: Thakur et al., "BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models", NeurIPS 2021 Datasets and Benchmarks. https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/65b9eea6e1cc6bb9f0cd2a47751a186f-Paper-round2.pdf (accessed 2026-11-14)
[^s4]: Cormack, Clarke and Buettcher, "Reciprocal rank fusion outperforms condorcet and individual rank learning methods", SIGIR 2009. https://research.google/pubs/pub36196/ (accessed 2026-11-14)
[^s5]: Elastic, "Reciprocal rank fusion", Elasticsearch Reference 8.19. https://www.elastic.co/guide/en/elasticsearch/reference/8.19/rrf.html (accessed 2026-11-14)
[^s6]: Weaviate, "Hybrid search" (concepts documentation). https://docs.weaviate.io/weaviate/concepts/search/hybrid-search (accessed 2026-11-14)
