---
id: kt:apache-lucene
type: Tool
title: Apache Lucene
aliases: [Lucene, Lucene Core, Apache Lucene Core]
domain: retrieval-and-knowledge
summary: >-
  An open-source Java search library from the Apache Software Foundation that builds inverted indexes over text and
  structured fields, ranks results with pluggable scoring models such as BM25, and since version 9.0 also supports
  approximate nearest-neighbour vector search with HNSW graphs; it is the engine inside Solr, Elasticsearch and OpenSearch.
maturity: established
broader: [kt:information-retrieval]
related: [kt:bm25, kt:tf-idf, kt:approximate-nearest-neighbor-search, kt:hybrid-search, kt:semantic-search, kt:vector-database]
relations:
  - {predicate: createdBy, object: kt:doug-cutting}
  - {predicate: basedOn, object: kt:inverted-index}
  - {predicate: alternativeTo, object: kt:faiss}
  - {predicate: enables, object: kt:hybrid-search}
  - {predicate: usedIn, object: kt:retrieval-augmented-generation}
  - {predicate: hasPart, object: kt:hnsw}
sources:
  - id: s1
    title: "Apache Lucene Core"
    publisher: Apache Software Foundation (lucene.apache.org)
    url: https://lucene.apache.org/core/
    type: official-docs
    accessed: 2026-11-18
  - id: s2
    title: "Lucene 9.11.0 core API (package overview)"
    publisher: Apache Software Foundation, Lucene Javadoc
    url: https://lucene.apache.org/core/9_11_0/core
    type: official-docs
    accessed: 2026-11-18
  - id: s3
    title: "07 December 2021, Apache Lucene 9.0 available"
    publisher: Apache Lucene PMC release announcement (Apache Confluence)
    url: https://cwiki-test.apache.org/confluence/x/xZBnCw
    type: official-docs
    accessed: 2026-11-18
  - id: s4
    title: "Anserini: Enabling the Use of Lucene for Information Retrieval Research"
    publisher: Yang, Fang and Lin, SIGIR 2017 (authors' copy)
    url: https://peilin-yang.github.io/files/pub/Yang_etal_SIGIR2017.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s5
    title: "Vector Search with OpenAI Embeddings: Lucene Is All You Need"
    publisher: Lin, Pradeep, Teofili and Xian, arXiv 2308.14963 (2023)
    url: https://arxiv.org/pdf/2308.14963
    type: primary
    accessed: 2026-11-18
  - id: s6
    title: "Happy birthday, Lucene"
    publisher: Elastic (company history page)
    url: https://www.elastic.co/celebrating-lucene
    type: community
    accessed: 2026-11-18
  - id: s7
    title: "Apache Solr 10.0.0 released"
    publisher: Apache Solr PMC announcement (announce@apache.org archive), 4 March 2026
    url: https://mail-archive.com/announce@apache.org/msg10780.html
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# Apache Lucene

**Apache Lucene** is an open-source, Java search library maintained by the Apache Software Foundation under the Apache License 2.0. It provides full-text and structured (fielded) search, faceting, spell correction, query suggestions and nearest-neighbour search over high-dimensional vectors, with a pluggable ranking layer that includes the vector space model and Okapi **BM25**.[^s1] Lucene is a library rather than a server: products such as Apache Solr and Elasticsearch wrap it with networking, distribution and administration, which is why it sits underneath much of the world's production keyword search.[^s4][^s6]

## Origin

Doug Cutting wrote the first version while learning Java, his fifth search engine, and released it as open source on SourceForge in April 2000.[^s6] Lucene joined the Apache Jakarta project in September 2001, and version 1.2 in 2002 was its first release under the Apache licence. Elastic's history of the project lists later milestones: a codecs API and BM25 among other similarity models in 4.0 (2012), BM25 becoming the default similarity in 6.0 (2016), and Block-Max WAND for faster top-hit retrieval in 8.0 (2019).[^s6] Elasticsearch, first released in 2010, was built on top of Lucene from the start.[^s6]

## How it works

An application indexes **documents**, each a set of named **fields**. An **Analyzer** turns field text into a stream of tokens through a chain of tokenizers and filters; an **IndexWriter** adds the documents, and a **codec** controls how the resulting inverted index (the map from each term to the documents that contain it) is encoded on disk, stored behind a `Directory` abstraction.[^s2] At query time, classes such as `TermQuery`, `PhraseQuery` and `BooleanQuery`, or a parsed query string, are run by an **IndexSearcher** over an **IndexReader**, which returns the top-scoring hits.[^s2]

Since **Lucene 9.0**, released on 7 December 2021, the library can also index dense numeric vectors and answer nearest-neighbour queries using Hierarchical Navigable Small World (HNSW) graphs; that release required JDK 11 or newer.[^s3] In the 9.x line the vector code lives in dedicated KNN and HNSW packages, alongside a quantization package that scales vectors down to smaller data types to save memory.[^s2] Because keyword and vector indexes live in the same engine, a single Lucene index can serve both lexical and embedding-based retrieval.

## Strengths, limitations and debate

Information-retrieval researchers long preferred academic toolkits such as Indri and Terrier. Yang, Fang and Lin (SIGIR 2017) attributed this to Lucene's production orientation: sparse documentation of its internals, APIs unfamiliar to researchers, and late adoption of modern ranking functions (BM25 arrived only in 2011).[^s4] Their **Anserini** toolkit wraps Lucene for reproducible experiments. On Gov2, single-threaded, it answered efficiency queries in about 382 ms on average versus 2,403 ms for Indri, with comparable BM25 and query-likelihood effectiveness across five TREC collections.[^s4]

For neural search, Lin and colleagues (2023) argued that a dedicated vector store is not required when an organisation already runs Lucene. Indexing OpenAI ada2 embeddings of MS MARCO with Lucene 9.5's HNSW, they reported RR@10 of 0.343 on the dev set.[^s5] They were open about the costs: Lucene then capped vectors at 1,024 dimensions, so they had to patch it for 1,536-dimensional embeddings; its query throughput was roughly half that of Faiss under comparable settings; and HNSW indexing is non-deterministic.[^s5] Whether general-purpose search engines or specialised vector databases are the better home for embeddings remains a live engineering trade-off.

## In practice

As of November 2026 the Lucene Core site lists version 10.6.0 as the latest release.[^s1] Downstream projects track it closely: Apache Solr 10.0, announced on 4 March 2026, is built on Lucene 10.3. The Solr 10.0 announcement also lists scalar and binary quantized dense vectors and GPU-accelerated vector operations through cuVS-Lucene.[^s7] In LLM applications Lucene-based engines commonly serve as the retriever in retrieval-augmented generation, supplying BM25 candidates, vector candidates or both for **hybrid search**.[^s5][^s1]

## Connections

Lucene is a tool of **information retrieval**, **created by** Doug Cutting and **based on** the **inverted index**.[^s6][^s2] It is the reference implementation of **BM25** and of the older **TF-IDF** vector-space scoring, both shipped as pluggable models.[^s1] Its HNSW component makes it an engine for **approximate nearest-neighbour search** and **semantic search**, which puts it in direct comparison with **Faiss** and dedicated **vector databases**.[^s3][^s5] Holding lexical and vector indexes together **enables hybrid search**, and that pairing is how Lucene is **used in retrieval-augmented generation** pipelines.[^s5]

## Sources

[^s1]: Apache Software Foundation, "Apache Lucene Core". https://lucene.apache.org/core/ (accessed 2026-11-18)
[^s2]: Apache Software Foundation, "Lucene 9.11.0 core API" package overview. https://lucene.apache.org/core/9_11_0/core (accessed 2026-11-18)
[^s3]: Apache Lucene PMC, "07 December 2021, Apache Lucene 9.0 available". https://cwiki-test.apache.org/confluence/x/xZBnCw (accessed 2026-11-18)
[^s4]: Yang, Fang and Lin, "Anserini: Enabling the Use of Lucene for Information Retrieval Research", SIGIR 2017. https://peilin-yang.github.io/files/pub/Yang_etal_SIGIR2017.pdf (accessed 2026-11-18)
[^s5]: Lin, Pradeep, Teofili and Xian, "Vector Search with OpenAI Embeddings: Lucene Is All You Need", arXiv 2308.14963 (2023). https://arxiv.org/pdf/2308.14963 (accessed 2026-11-18)
[^s6]: Elastic, "Happy birthday, Lucene". https://www.elastic.co/celebrating-lucene (accessed 2026-11-18)
[^s7]: Apache Solr PMC, "Apache Solr 10.0.0 released" announcement, 4 March 2026. https://mail-archive.com/announce@apache.org/msg10780.html (accessed 2026-11-18)
