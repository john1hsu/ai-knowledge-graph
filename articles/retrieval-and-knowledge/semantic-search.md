---
id: kt:semantic-search
type: Technique
title: Semantic search
aliases: [meaning-based search, neural search, vector search, dense semantic search]
domain: retrieval-and-knowledge
summary: >-
  An information retrieval approach that ranks documents by how closely their meaning matches a query's,
  rather than by exact keyword overlap, typically by mapping queries and documents into a shared vector space
  and returning the nearest items.
maturity: established
broader: [kt:information-retrieval]
related: [kt:embeddings, kt:vector-database, kt:bm25, kt:reranking, kt:hybrid-search, kt:retrieval-augmented-generation]
relations:
  - {predicate: dependsOn, object: kt:embeddings}
  - {predicate: basedOn, object: kt:latent-semantic-analysis}
  - {predicate: dependsOn, object: kt:approximate-nearest-neighbor-search}
  - {predicate: alternativeTo, object: kt:bm25}
  - {predicate: evaluatedOn, object: kt:beir}
  - {predicate: usedIn, object: kt:retrieval-augmented-generation}
sources:
  - id: s1
    title: "Indexing by Latent Semantic Analysis"
    publisher: Journal of the American Society for Information Science 41(6), 391-407, 1990 (Deerwester, Dumais, Furnas, Landauer and Harshman); author copy hosted by Microsoft Research
    url: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/08/JASIS90.pdf
    type: primary
    accessed: 2026-11-08
  - id: s2
    title: "Introduction to Information Retrieval, Chapter 18: Matrix decompositions and latent semantic indexing"
    publisher: Cambridge University Press, 2008 (Manning, Raghavan and Schütze); Stanford NLP Group online edition
    url: https://nlp.stanford.edu/IR-book/pdf/18lsi.pdf
    type: textbook
    accessed: 2026-11-08
  - id: s3
    title: "Semantic Search"
    publisher: Sentence Transformers documentation (sbert.net)
    url: https://sbert.net/examples/sentence_transformer/applications/semantic-search
    type: official-docs
    accessed: 2026-11-08
  - id: s4
    title: "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs"
    publisher: Malkov and Yashunin, arXiv 1603.09320
    url: https://arxiv.org/pdf/1603.09320
    type: primary
    accessed: 2026-11-08
  - id: s5
    title: "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT"
    publisher: Khattab and Zaharia, arXiv 2004.12832
    url: https://arxiv.org/abs/2004.12832v2
    type: primary
    accessed: 2026-11-08
  - id: s6
    title: "BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models"
    publisher: Thakur, Reimers, Rücklé, Srivastava and Gurevych, arXiv 2104.08663 (NeurIPS 2021 Datasets and Benchmarks Track)
    url: https://arxiv.org/abs/2104.08663
    type: primary
    accessed: 2026-11-08
created: 2026-11-08
---

# Semantic search

**Semantic search** retrieves information by meaning rather than by literal string matching. The Sentence Transformers documentation describes its goal as improving search accuracy by understanding the content of both the query and the corpus, so that synonyms, abbreviations and misspellings can still find the right results; in its modern form, every corpus entry is embedded into a vector space, the query is embedded into the same space, and the closest entries are returned.[^s3] It is contrasted with lexical (keyword) retrieval, which scores documents only on the terms they share with the query.

## Origin: the vocabulary problem

Classic vector space retrieval gives every term its own dimension, so it cannot see relationships between words. Manning, Raghavan and Schütze illustrate the two resulting failures: **synonymy** (a query for "car" undervalues a document that says "automobile") and **polysemy** (a word like "charge" inflates similarity between texts that use it in different senses).[^s2]

The first widely cited fix was **latent semantic indexing (LSI)**, also called latent semantic analysis, introduced by Deerwester, Dumais, Furnas, Landauer and Harshman in 1990. They applied singular value decomposition to a large term-by-document matrix, keeping roughly 100 orthogonal factors, so that each document became a short vector of factor weights. A query was treated as a pseudo-document built from its term vectors, and documents whose cosine similarity to it exceeded a threshold were returned.[^s1] The authors called this fully automatic method promising; in their experiments it beat raw term matching on one test collection and roughly tied on another.[^s1]

LSI had lasting limits. The textbook notes that the SVD is costly, that it had no reported successful experiment beyond about a million documents, that newly added documents can only be approximately folded in until the decomposition is recomputed, and that it never became a major force in ranking.[^s2]

## How modern semantic search works

Today's systems replace the SVD with learned neural encoders but keep the same shape: encode the corpus once offline, encode each query at search time, and rank by vector similarity, usually cosine similarity or dot product on normalized vectors.[^s3] Practitioners distinguish two settings. In **symmetric** search, query and documents are similar in length and kind (one question matched to paraphrased questions), so their roles could be swapped. In **asymmetric** search, a short query such as a question must match a longer passage that answers it, and the documentation stresses choosing a model trained for the right setting, encoding queries and documents with their respective methods.[^s3]

**Scaling the nearest-neighbour step.** Exhaustive comparison is practical up to roughly a million entries, according to the Sentence Transformers guide.[^s3] Beyond that, systems use approximate nearest neighbour (ANN) indexes such as FAISS, Annoy or hnswlib, which return results in milliseconds but may miss some true nearest vectors; each exposes parameters that trade recall against speed.[^s3] A popular ANN design is **HNSW** (Hierarchical Navigable Small World), proposed by Malkov and Yashunin: it stacks proximity graphs over nested subsets of the data, like a probabilistic skip list, and starts each search on the sparse top layer before descending, which gives logarithmic complexity scaling.[^s4]

**Retrieve and re-rank.** Single-vector bi-encoders are fast but coarse, so many pipelines first retrieve candidates and then re-rank them with a more expensive model.[^s3] Khattab and Zaharia's **ColBERT** sits between the two: it encodes queries and documents independently with BERT, keeps per-token vectors, and applies a cheap "late interaction" step to compare them. They reported it was competitive with BERT re-rankers while running about two orders of magnitude faster and using about four orders of magnitude fewer FLOPs per query.[^s5]

## Limitations and evidence

Semantic search does not uniformly beat keyword search. The BEIR benchmark (Thakur and colleagues, NeurIPS 2021 Datasets and Benchmarks Track) tested ten retrieval systems zero-shot on 18 public datasets and found BM25 a robust baseline, while dense and sparse neural retrievers, though efficient, often underperformed out of their training distribution; re-ranking and late-interaction models scored best on average but at high computational cost.[^s6] Vector representations also share LSI's inability to express negation or enforce Boolean constraints, a weakness the IR textbook notes for vector space retrieval generally.[^s2] Results depend heavily on the encoder chosen and on whether the task is symmetric or asymmetric.[^s3]

## In practice

Semantic search powers question answering, site and enterprise search, duplicate detection and the retrieval step of retrieval-augmented generation. Production systems commonly store vectors in ANN-backed indexes; the Sentence Transformers guide notes that Elasticsearch and OpenSearch support dense vector indexing, and that OpenSearch can combine vector search with BM25 keyword scoring, a pattern known as hybrid search.[^s3]

## Connections

Semantic search is a technique within **information retrieval** and **depends on embeddings** to represent meaning as vectors.[^s3] It is **based on** the earlier **latent semantic analysis**, which first moved retrieval into a reduced "concept" space.[^s1][^s2] At scale it **depends on approximate nearest neighbour search** such as HNSW, typically served from a **vector database**.[^s3][^s4] It is an **alternative to** lexical ranking with **BM25** and is often combined with it as **hybrid search** or followed by **reranking**, as with ColBERT-style late interaction.[^s3][^s5] Its generalization is **evaluated on BEIR**, and it is **used in retrieval-augmented generation** to supply relevant context to language models.[^s6][^s3]

## Sources

[^s1]: Deerwester, Dumais, Furnas, Landauer and Harshman, "Indexing by Latent Semantic Analysis", Journal of the American Society for Information Science 41(6), 391-407 (1990). https://www.microsoft.com/en-us/research/wp-content/uploads/2016/08/JASIS90.pdf (accessed 2026-11-08)
[^s2]: Manning, Raghavan and Schütze, "Matrix decompositions and latent semantic indexing", Introduction to Information Retrieval, Cambridge University Press (2008), ch. 18. https://nlp.stanford.edu/IR-book/pdf/18lsi.pdf (accessed 2026-11-08)
[^s3]: Sentence Transformers documentation, "Semantic Search". https://sbert.net/examples/sentence_transformer/applications/semantic-search (accessed 2026-11-08)
[^s4]: Malkov and Yashunin, "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs", arXiv 1603.09320. https://arxiv.org/pdf/1603.09320 (accessed 2026-11-08)
[^s5]: Khattab and Zaharia, "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT", arXiv 2004.12832. https://arxiv.org/abs/2004.12832v2 (accessed 2026-11-08)
[^s6]: Thakur, Reimers, Rücklé, Srivastava and Gurevych, "BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models", arXiv 2104.08663 (NeurIPS 2021 Datasets and Benchmarks). https://arxiv.org/abs/2104.08663 (accessed 2026-11-08)
