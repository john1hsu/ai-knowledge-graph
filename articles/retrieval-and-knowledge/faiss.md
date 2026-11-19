---
id: kt:faiss
type: Tool
title: Faiss
aliases: [FAISS, Facebook AI Similarity Search]
domain: retrieval-and-knowledge
summary: >-
  An open-source C++ library with Python wrappers, developed by Meta's FAIR group, for efficient similarity search,
  clustering and compression of dense vectors, offering exact and approximate nearest-neighbour indexes on CPU and GPU.
maturity: established
broader: [kt:approximate-nearest-neighbor-search]
related: [kt:vector-database, kt:embeddings, kt:semantic-search]
relations:
  - {predicate: createdBy, object: kt:meta-ai}
  - {predicate: introducedIn, object: kt:billion-scale-similarity-search-with-gpus}
  - {predicate: basedOn, object: kt:product-quantization}
  - {predicate: runsOn, object: kt:gpu-computing}
  - {predicate: usedIn, object: kt:retrieval-augmented-generation}
  - {predicate: alternativeTo, object: kt:apache-lucene}
sources:
  - id: s1
    title: "The Faiss library"
    publisher: arXiv:2401.08281v3 (Douze, Guzhva, Deng, Johnson, Szilvasy, Mazaré, Lomeli, Hosseini and Jégou; Meta FAIR), February 2025
    url: https://arxiv.org/abs/2401.08281v3
    type: primary
    accessed: 2026-11-19
  - id: s2
    title: "Billion-scale similarity search with GPUs"
    publisher: arXiv:1702.08734 (Johnson, Douze and Jégou; Facebook AI Research), February 2017
    url: https://arxiv.org/pdf/1702.08734
    type: primary
    accessed: 2026-11-19
  - id: s3
    title: "Faiss: A library for efficient similarity search"
    publisher: Engineering at Meta (Jégou, Douze and Johnson), 29 March 2017
    url: https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/
    type: lab-research
    accessed: 2026-11-19
  - id: s4
    title: "facebookresearch/faiss — README and LICENSE"
    publisher: GitHub (Meta FAIR)
    url: https://github.com/facebookresearch/faiss
    type: official-docs
    accessed: 2026-11-19
created: 2026-11-19
---

# Faiss

**Faiss** (originally "Facebook AI Similarity Search") is an open-source library for searching, clustering, compressing and transforming large collections of dense vectors such as embeddings.[^s1] Given a query vector, it returns the database vectors with the smallest Euclidean distance or the largest inner product, either exactly or approximately.[^s3] Its core is written in C++ with full Python/numpy wrappers, it is released under the MIT licence, and development is led by Meta's Fundamental AI Research (FAIR) group.[^s4]

## Origin

Meta (then Facebook) announced Faiss in March 2017, in a post by Hervé Jégou, Matthijs Douze and Jeff Johnson.[^s3] The accompanying paper, *Billion-scale similarity search with GPUs* (Johnson, Douze and Jégou, 2017), introduced a GPU k-selection algorithm, WarpSelect, that the authors report reaches up to 55% of theoretical peak performance, and applied it to brute-force, product-quantization-based and compressed-domain search.[^s2] The paper reported building a k-nearest-neighbour graph over one billion vectors in under 12 hours on four GPUs, and a SIFT1B comparison in which its single-GPU search was about 8.5 times faster than a previously published GPU method at similar accuracy.[^s2] Much of the library's compression machinery builds on earlier product-quantization research by the same group.[^s1]

## How it works

Faiss frames vector search as a trade-off among speed, memory use and accuracy, with index build time as a further cost.[^s1] Its building blocks combine freely:[^s1]

- **Exact search.** `IndexFlat` compares the query with every vector, using BLAS matrix multiplication; it is the accuracy baseline for everything else.[^s1]
- **Inverted files (IVF).** A coarse quantizer, usually trained with k-means, splits the data into `nlist` cells, and a query visits only the `nprobe` nearest cells. Raising `nprobe` buys recall with time.[^s1]
- **Graph indexes.** HNSW and NSG navigate a proximity graph. The 2024 Faiss paper recommends them when memory is not tight, typically for collections under about a million vectors.[^s1]
- **Compression.** Scalar quantizers (8, 6 or 4 bits, fp16, bf16), product quantization (PQ), additive quantizers such as residual and local-search quantization, plus transforms such as PCA and OPQ, shrink vectors to compact codes. For very large collections that must be compressed, the authors describe IVF with compressed codes as the only practical option.[^s1]

An `index_factory` string assembles these parts. For example, "PCA160,IVF20000_HNSW,PQ20x10,RFlat" reduces dimensions with PCA, routes queries through IVF with an HNSW coarse quantizer, stores PQ codes and re-ranks candidates with exact distances.[^s1] Cosine similarity is handled by normalizing vectors and using inner product.[^s1]

On GPUs, indexes such as `GpuIndexFlatL2` are drop-in replacements for their CPU counterparts and can be sharded or replicated across several GPUs.[^s4] As of late 2026 the README lists CUDA and AMD ROCm backends and NVIDIA cuVS as an optional GPU backend, with prebuilt packages named faiss-cpu, faiss-gpu and faiss-gpu-cuvs.[^s4]

## Limitations

Faiss is deliberately a library, not a service or a database. The authors note that it does not extract features and offers no concurrent writes, sharding, load balancing, transactions or query optimization; systems that need those build them around Faiss.[^s1] Approximate indexes also need tuning: IVF and quantizers must be trained on representative data, and parameter choices move recall, latency and memory in opposite directions, so results should be checked against an exact baseline.[^s1] The 2017 speed figures were measured on hardware of that era and against particular baselines, so they illustrate the design rather than current rankings.[^s2]

## In practice

The 2024 paper (revised February 2025) reported about 30,000 GitHub stars, over 4,000 citations of the GPU paper and around 3 million package downloads; the repository showed about 41,600 stars when checked in November 2026.[^s1][^s4] The authors describe uses including a 1.5-trillion-vector index, text retrieval for knowledge-intensive NLP, de-duplication of 1.3 billion images, and content moderation with range queries.[^s1] They also state that commercial vector databases have either built on Faiss or reimplemented its algorithms; Milvus, for instance, uses Faiss as one of the core engines in its Knowhere library.[^s1]

## Connections

Faiss is a concrete implementation of approximate nearest neighbor search, its broader node, and offers several ANN families (IVF, HNSW, NSG) behind one interface.[^s1] It is **created by** Meta's research group and **introduced in** the 2017 GPU similarity-search paper.[^s2][^s3] It is **based on** product quantization and related vector-compression research, and it **runs on** GPU computing through CUDA, ROCm and cuVS backends.[^s1][^s4] Because it lacks storage, updates and query planning, it contrasts with a full **vector database**, many of which embed Faiss or its algorithms.[^s1] It indexes **embeddings** for **semantic search** and is a common retriever component in **retrieval-augmented generation**, where knowledge-intensive text retrieval is one of its documented applications.[^s1] Lucene-based engines are an **alternative** when lexical search, filtering and document storage are needed in the same system.

## Sources
[^s1]: Douze et al., "The Faiss library", arXiv:2401.08281v3, Feb 2025. https://arxiv.org/abs/2401.08281v3 (accessed 2026-11-19)
[^s2]: Johnson, Douze and Jégou, "Billion-scale similarity search with GPUs", arXiv:1702.08734, 2017. https://arxiv.org/pdf/1702.08734 (accessed 2026-11-19)
[^s3]: Jégou, Douze and Johnson, "Faiss: A library for efficient similarity search", Engineering at Meta, 29 Mar 2017. https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/ (accessed 2026-11-19)
[^s4]: Meta FAIR, facebookresearch/faiss README and LICENSE, GitHub. https://github.com/facebookresearch/faiss (accessed 2026-11-19)
