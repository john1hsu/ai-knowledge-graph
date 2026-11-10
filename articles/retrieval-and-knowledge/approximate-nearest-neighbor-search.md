---
id: kt:approximate-nearest-neighbor-search
type: Technique
title: Approximate nearest neighbor search
aliases: [ANN search, approximate k-nearest neighbor search, approximate similarity search, vector similarity search]
domain: retrieval-and-knowledge
summary: >-
  A family of indexing and search methods that return points that are close to, but not guaranteed to be exactly,
  the nearest neighbours of a query vector, trading a small loss in recall for search that is far faster and
  cheaper than exhaustive comparison in high-dimensional spaces.
maturity: established
broader: [kt:information-retrieval]
related: [kt:embeddings, kt:vector-database]
relations:
  - {predicate: enables, object: kt:semantic-search}
  - {predicate: usedIn, object: kt:retrieval-augmented-generation}
  - {predicate: implementedIn, object: kt:faiss}
  - {predicate: evaluatedOn, object: kt:ann-benchmarks}
sources:
  - id: s1
    title: "Near-Optimal Hashing Algorithms for Approximate Nearest Neighbor in High Dimensions"
    publisher: Communications of the ACM 51(1), January 2008 (Andoni and Indyk)
    url: https://pike.psu.edu/classes/cre515/2010-spring/CACM.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s2
    title: "Approximate Nearest Neighbor: Towards Removing the Curse of Dimensionality"
    publisher: Theory of Computing 8, article 14, pp. 321-350, 2012 (Har-Peled, Indyk and Motwani); journal version of STOC'98 and FOCS'01 papers
    url: https://mirror.theoryofcomputing.org/articles/v008a014/
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s3
    title: "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs"
    publisher: arXiv:1603.09320v2 (Malkov and Yashunin), 2016
    url: https://arxiv.org/abs/1603.09320v2
    type: primary
    accessed: 2026-11-10
  - id: s4
    title: "Billion-scale similarity search with GPUs"
    publisher: arXiv:1702.08734 (Johnson, Douze and Jégou; Facebook AI Research), 2017
    url: https://arxiv.org/pdf/1702.08734
    type: primary
    accessed: 2026-11-10
  - id: s5
    title: "The Faiss Library"
    publisher: arXiv:2401.08281v3 (Douze, Guzhva, Deng, Johnson, Szilvasy, Mazaré, Lomeli, Hosseini and Jégou)
    url: https://arxiv.org/html/2401.08281v3
    type: primary
    accessed: 2026-11-10
  - id: s6
    title: "ANN-Benchmarks: A Benchmarking Tool for Approximate Nearest Neighbor Algorithms"
    publisher: arXiv:1807.05614 (Aumüller, Bernhardsson and Faithfull), 2018; conference version at SISAP 2017
    url: https://arxiv.org/pdf/1807.05614
    type: primary
    accessed: 2026-11-10
created: 2026-11-10
---

# Approximate nearest neighbor search

**Approximate nearest neighbor (ANN) search** is the problem, and the family of algorithms that solve it, of finding database vectors that are close to a query vector without guaranteeing that they are the exact closest ones. Relaxing exactness is what makes similarity search practical over millions or billions of high-dimensional embeddings, and ANN indexes sit underneath most modern vector search, recommendation and retrieval-augmented generation systems.[^s1][^s5]

## Why approximate?

Exact nearest-neighbor methods such as kd-trees need space or query time that grows exponentially with the dimension d, so in high dimensions they often do little better than comparing the query to every point, a problem known as the curse of dimensionality.[^s1] The ANN-Benchmarks authors summarize the consequence: for large, high-dimensional datasets, exact answers require either linear scans or costs exponential in d, which rules out efficient exact search.[^s6] Formally, the *c-approximate R-near neighbor* problem asks a data structure to return, with high probability, any point within distance cR of the query whenever some point lies within R, for an approximation factor c > 1.[^s1]

## Origin

Indyk and Motwani introduced locality-sensitive hashing (LSH) for this problem in a 1998 STOC paper, later unified with follow-up FOCS 2001 results in a 2012 *Theory of Computing* article by Har-Peled, Indyk and Motwani. That article gives algorithms whose space is polynomial in n and d and whose query time is sub-linear in n.[^s2] For Hamming distance, the Indyk–Motwani hash family gives a query-time exponent of ρ = 1/c, meaning roughly n^ρ work per query.[^s1] Andoni and Indyk later gave a Euclidean family with ρ approaching 1/c², close to a known lower bound for hashing-based methods.[^s1]

## How the main families work

**Hashing (LSH).** A hash family is useful when nearby points collide with higher probability than distant ones. LSH concatenates k such hash functions into one key, to make collisions selective, and builds L tables with independent keys, so that a true neighbour collides with the query in at least one table; the query then checks only the points in its buckets.[^s1]

**Quantization and inverted files.** Faiss-style indexes cluster the database with a coarse quantizer and, at query time, visit only a few clusters (the *nprobe* parameter). Residual vectors are compressed with **product quantization**, which splits each vector into sub-vectors and stores a short code for each, so distances can be estimated from small lookup tables. Johnson, Douze and Jégou implemented this IVFADC scheme on GPUs. In 2017 they reported 8.5× faster billion-scale search than the prior GPU state of the art, and a k-NN graph over the 1-billion-vector Deep1B set built on four GPUs in under 12 hours.[^s4]

**Proximity graphs.** Graph indexes link each vector to nearby vectors and answer queries by greedy walks through the graph. Malkov and Yashunin's **HNSW** builds a hierarchy of such graphs incrementally: each element's top layer is drawn from an exponentially decaying distribution, so upper layers are sparse and carry long-range links. Search starts at the top and descends, and the authors report logarithmic scaling with dataset size.[^s3]

## Trade-offs and evaluation

ANN methods trade four quantities: accuracy, search speed, memory and index build time.[^s5] Accuracy is usually reported as recall, for example the fraction of the true k nearest neighbours that appear in the returned list.[^s5] ANN-Benchmarks, introduced by Aumüller, Bernhardsson and Faithfull, plots recall against queries per second on datasets such as SIFT, GIST and GloVe. In its 2018 results, graph methods such as HNSW and KGraph generally gave the best trade-offs at high recall. FAISS's inverted-file index built in seconds with a small footprint, while some graph indexes took hours to build.[^s6] The Faiss authors similarly advise graph indexes when memory is not tight and the collection is modest, and compressed IVF indexes for very large collections.[^s5] Most fast methods expose several tuning parameters and do not self-tune to a target recall, so practitioners must benchmark on their own data.[^s6]

## In practice

The Faiss authors describe their library as a search engine embedded in other systems rather than a database. They report that vector databases such as Milvus use Faiss as a core engine and that Zilliz and Pinecone use it or reimplement its algorithms. Applications include text retrieval for knowledge-intensive NLP, deduplication and content moderation, and the authors cite an index of 1.5 trillion vectors.[^s5]

## Connections

- **Broader:** ANN search is a core technique of **information retrieval**, applied whenever documents are represented as vectors.[^s5]
- **Related:** it operates over **embeddings** produced by neural encoders, and **vector databases** wrap ANN indexes with storage, sharding and query services.[^s5]
- **Enables:** dense **semantic search**, which ranks by vector proximity and needs fast neighbour lookup at scale.[^s3][^s5]
- **Used in:** the retrieval step of **retrieval-augmented generation**, among other knowledge-intensive NLP tasks.[^s5]
- **Implemented in:** **Faiss**, Meta's open-source similarity-search library, among others.[^s4][^s5]
- **Evaluated on:** **ANN-Benchmarks**, the standard recall-versus-throughput comparison.[^s6]

## Sources

[^s1]: Andoni and Indyk, "Near-Optimal Hashing Algorithms for Approximate Nearest Neighbor in High Dimensions", Communications of the ACM 51(1), 2008. https://pike.psu.edu/classes/cre515/2010-spring/CACM.pdf (accessed 2026-11-10)
[^s2]: Har-Peled, Indyk and Motwani, "Approximate Nearest Neighbor: Towards Removing the Curse of Dimensionality", Theory of Computing 8:321-350, 2012. https://mirror.theoryofcomputing.org/articles/v008a014/ (accessed 2026-11-10)
[^s3]: Malkov and Yashunin, "Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs", arXiv:1603.09320v2, 2016. https://arxiv.org/abs/1603.09320v2 (accessed 2026-11-10)
[^s4]: Johnson, Douze and Jégou, "Billion-scale similarity search with GPUs", arXiv:1702.08734, 2017. https://arxiv.org/pdf/1702.08734 (accessed 2026-11-10)
[^s5]: Douze et al., "The Faiss Library", arXiv:2401.08281v3. https://arxiv.org/html/2401.08281v3 (accessed 2026-11-10)
[^s6]: Aumüller, Bernhardsson and Faithfull, "ANN-Benchmarks: A Benchmarking Tool for Approximate Nearest Neighbor Algorithms", arXiv:1807.05614, 2018. https://arxiv.org/pdf/1807.05614 (accessed 2026-11-10)
