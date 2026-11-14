---
id: kt:vector-database
type: Tool
title: Vector database
aliases: [vector database management system, VDBMS, vector store, vector DB]
domain: retrieval-and-knowledge
summary: >-
  A data management system that stores high-dimensional embedding vectors together with their metadata and
  answers similarity queries over them, typically through approximate nearest neighbor indexes, while adding
  database features such as updates, filtering on attributes, persistence and distributed scale-out.
maturity: established
broader: [kt:information-retrieval]
related: [kt:embeddings, kt:semantic-search, kt:hybrid-search]
relations:
  - {predicate: dependsOn, object: kt:approximate-nearest-neighbor-search}
  - {predicate: usedIn, object: kt:retrieval-augmented-generation}
  - {predicate: contrastsWith, object: kt:faiss}
sources:
  - id: s1
    title: "Survey of vector database management systems"
    publisher: The VLDB Journal 33, pp. 1591-1615, 2024 (Pan, Wang and Li)
    url: https://dbgroup.cs.tsinghua.edu.cn/ligl/papers/vldbj2024-vectordb.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s2
    title: "Milvus: A Purpose-Built Vector Data Management System"
    publisher: ACM SIGMOD 2021 (Wang et al., Zilliz and Purdue University)
    url: https://www.cs.purdue.edu/homes/csjgwang/pubs/SIGMOD21_Milvus.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node"
    publisher: NeurIPS 2019 (Jayaram Subramanya et al., Microsoft Research)
    url: https://papers.nips.cc/paper/2019/hash/09853c7fb1d3f8ee67a61b6bf4a7f8e6-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "pgvector: Open-source vector similarity search for Postgres (vector extension documentation)"
    publisher: PGXN, pgvector project
    url: https://pgxn.org/dist/vector
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# Vector database

A vector database, or vector database management system (VDBMS), stores embedding vectors produced by machine-learning models alongside ordinary attributes and answers queries of the form "find the k items most similar to this vector". Pan, Wang and Li's 2024 survey in *The VLDB Journal* counts more than 20 commercial systems of this kind that appeared within roughly five years, a wave it attributes largely to large language model applications that need fast, reliable retrieval over large stores of unstructured data.[^s1] Similarity search itself is much older; what is new is wrapping it in a full data system.[^s1]

## Why vectors need their own data management

The survey names five obstacles that keep conventional databases from handling vectors well: similarity is a vague criterion that may not match user intent; each comparison costs time proportional to the dimensionality; vectors are large enough to span multiple pages; they have no natural sort order to index on; and vector indexes that stop after k neighbours combine awkwardly with attribute predicates.[^s1] The Milvus paper (SIGMOD 2021) makes the complementary argument from the library side: tools such as Faiss and SPTAG keep data and indexes in the memory of one machine, assume static data, and offer no attribute filtering or multi-vector queries, so production users had to build the surrounding system themselves.[^s2]

## How it works

**Indexing.** Exhaustive search is exact but scales linearly, so vector databases build approximate nearest neighbour indexes. The survey groups them into table- and hash-based methods (locality-sensitive hashing, clustering-based inverted files such as IVF), tree-based methods (k-d trees, ANNOY), graph-based methods (HNSW, NSG, Vamana), and quantization schemes (scalar and product quantization) that compress vectors to save memory.[^s1] Milvus, for example, exposes IVF_FLAT, IVF_SQ8, IVF_PQ, HNSW, RNSG and ANNOY behind one extensible interface.[^s2]

**Disk-resident search.** Purely in-memory indexes cap dataset size. DiskANN (NeurIPS 2019) keeps compressed vectors in RAM and its Vamana graph on SSD; the authors reported serving a one-billion-point SIFT1B index from a workstation with 64 GB RAM at more than 5,000 queries per second, under 3 ms mean latency and over 95% 1-recall@1, while memory-matched Faiss baselines plateaued near 50% recall.[^s3]

**Hybrid queries.** Real queries usually combine a vector with filters (price, tenant, date). Systems use pre-filtering (block non-matching vectors before the scan, e.g. with bitmasks), post-filtering (search first, then filter, which can return fewer than k results unless extra candidates are fetched), or single-stage "visit-first" scans that check predicates during traversal; some, such as Qdrant and Vespa, choose a strategy by selectivity rules, while Milvus and AnalyticDB-V use cost models.[^s1] Pre-filtering a graph index can disconnect it, a problem that variants such as Filtered-DiskANN address by adding edges.[^s1]

**Data system features.** Milvus handles inserts and deletes with an LSM-tree-style design of in-memory buffers flushed to immutable segments, uses snapshot isolation so reads are not blocked by writes, and separates compute from shared storage for distributed scale-out.[^s2] Distributed systems shard data by hashing, attributes or clusters, then scatter a query to shards and merge the partial top-k results.[^s1]

## Native versus extended systems

The survey distinguishes native systems built around vectors (for example Pinecone, Chroma, Milvus, Qdrant and Weaviate) from extended systems that add vector types to an existing engine, including NoSQL stores (MongoDB, Redis, Cassandra) and relational databases (pgvector, SingleStore, ClickHouse); it notes that extended systems offer the broadest capabilities and reuse existing infrastructure, possibly at some cost in performance.[^s1] pgvector illustrates the extended approach: vectors live in ordinary PostgreSQL tables with ACID transactions and joins; search is exact by default, and adding an HNSW or IVFFlat index switches to approximate results.[^s4] Its documentation (version 0.8.7, accessed November 2026) describes HNSW as giving a better speed-recall trade-off at the cost of slower builds and more memory, limits indexed `vector` columns to 2,000 dimensions, and warns that filters applied after an approximate index scan can return fewer rows than requested unless iterative index scans are enabled.[^s4]

## Limitations and open questions

Benchmark claims in this space are mostly vendor- or author-run: the Milvus paper's reported speed-ups of up to two orders of magnitude were measured by its own authors against anonymised competitors.[^s2] Open research problems include estimating the cost of hybrid filter operators, partitioning vectors across machines, GPU-friendly graph indexes, indexes that update without rebuilding, and similarity measures that better reflect what users actually mean.[^s1]

## Connections

A vector database is an information retrieval system whose core operation is approximate nearest neighbour search, on which it depends.[^s1] It stores the outputs of embedding models and serves semantic search and hybrid search pipelines; its most visible use today is as the retrieval store in retrieval-augmented generation.[^s1] It contrasts with Faiss, a similarity-search library that supplies index algorithms but not the storage, update, filtering and distribution layers a database adds.[^s2]

## Sources

[^s1]: Pan, Wang and Li, "Survey of vector database management systems", The VLDB Journal 33, 2024. https://dbgroup.cs.tsinghua.edu.cn/ligl/papers/vldbj2024-vectordb.pdf (accessed 2026-11-14)
[^s2]: Wang et al., "Milvus: A Purpose-Built Vector Data Management System", SIGMOD 2021. https://www.cs.purdue.edu/homes/csjgwang/pubs/SIGMOD21_Milvus.pdf (accessed 2026-11-14)
[^s3]: Jayaram Subramanya et al., "DiskANN: Fast Accurate Billion-point Nearest Neighbor Search on a Single Node", NeurIPS 2019. https://papers.nips.cc/paper/2019/hash/09853c7fb1d3f8ee67a61b6bf4a7f8e6-Abstract.html (accessed 2026-11-14)
[^s4]: pgvector project, "vector" extension documentation on PGXN. https://pgxn.org/dist/vector (accessed 2026-11-14)
