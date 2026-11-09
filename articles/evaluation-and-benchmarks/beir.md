---
id: kt:beir
type: Benchmark
title: BEIR
aliases: [Benchmarking IR, BEIR zero-shot retrieval benchmark]
domain: evaluation-and-benchmarks
summary: >-
  A heterogeneous benchmark, introduced by Thakur and colleagues in 2021, that tests how well information retrieval
  models generalize zero-shot across 18 datasets spanning nine retrieval tasks, scored mainly with nDCG@10.
maturity: established
broader: [kt:ai-evaluation, kt:information-retrieval]
related: [kt:bm25, kt:semantic-search, kt:embeddings, kt:reranking, kt:retrieval-augmented-generation]
relations:
  - {predicate: introducedIn, object: kt:beir-a-heterogeneous-benchmark-for-zero-shot-evaluation-of-information-retrieval-models}
  - {predicate: usedIn, object: kt:mteb}
sources:
  - id: s1
    title: "BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models"
    publisher: arXiv:2104.08663v4 (Thakur, Reimers, Rücklé, Srivastava, Gurevych), October 2021
    url: https://arxiv.org/abs/2104.08663v4
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models (poster)"
    publisher: NeurIPS 2021 Datasets and Benchmarks Track
    url: https://neurips.cc/virtual/2021/29903
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s3
    title: "beir-cellar/beir: A Heterogeneous Benchmark for Information Retrieval"
    publisher: BEIR maintainers on GitHub (UKP Lab, University of Waterloo, Hugging Face)
    url: https://github.com/beir-cellar/beir
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "MTEB: Massive Text Embedding Benchmark"
    publisher: arXiv:2210.07316 (Muennighoff, Tazi, Magne, Reimers), 2022–2023
    url: https://arxiv.org/pdf/2210.07316v2
    type: primary
    accessed: 2026-11-09
  - id: s5
    title: "Resources for Brewing BEIR: Reproducible Reference Models and an Official Leaderboard"
    publisher: arXiv:2306.07471 (Kamalloo, Thakur, Lassance, Ma, Yang, Lin), June 2023
    url: https://arxiv.org/abs/2306.07471
    type: primary
    accessed: 2026-11-09
created: 2026-11-09
---

# BEIR

**BEIR** is a benchmark for measuring whether information retrieval (IR) models still work when moved to data unlike what they were trained on. It was introduced by Nandan Thakur, Nils Reimers, Andreas Rücklé, Abhishek Srivastava and Iryna Gurevych in an arXiv paper first submitted in April 2021, and presented as a poster in the NeurIPS 2021 Datasets and Benchmarks Track.[^s1][^s2] The authors' motivation was that neural retrievers had mostly been tested in narrow, homogeneous settings, which said little about out-of-distribution behaviour.[^s1]

## How it works

BEIR bundles 18 publicly available datasets that cover nine task types: fact checking, citation prediction, duplicate-question retrieval, argument retrieval, news retrieval, open-domain question answering, tweet retrieval, biomedical IR and entity retrieval.[^s1] Models are typically trained on MS MARCO and then evaluated **zero-shot** on the other datasets; MS MARCO results are reported separately and kept out of the zero-shot comparison.[^s1] The datasets differ sharply in size and density of judgments: as listed in the official repository, TREC-COVID has 50 queries over about 171K documents with roughly 494 relevant documents per query, while Quora has 10,000 queries with fewer than two relevant documents each.[^s3] Four collections (BioASQ, Signal-1M, TREC-NEWS and Robust04) cannot be redistributed, so the repository gives reproduction instructions instead of downloads.[^s3]

The headline metric is **nDCG@10**, chosen because it handles both binary and graded relevance labels, which BEIR's mixed datasets require.[^s1] The `beir` Python package (Apache-2.0) loads each dataset as a corpus, a query set and relevance judgments (qrels), and reports nDCG, MAP, recall and precision at cut-offs from 1 to 1,000, with MRR available as a custom metric.[^s3]

## Key findings

The original study compared ten systems across lexical, sparse, dense, late-interaction and re-ranking families.[^s1] Its central result was that **BM25 is a hard baseline to beat out of domain**: relative to BM25's average nDCG@10, DPR scored 47.7% lower, ANCE 7.4% lower and TAS-B 2.8% lower, while late-interaction ColBERT was 2.5% higher and BM25 followed by a cross-encoder re-ranker was 11% higher.[^s1] The better models paid for it in compute. On DBPedia (1M documents) the paper reports about 20 ms per query on CPU with a 0.4 GB index for BM25, versus about 350 ms on GPU and a 20 GB index for ColBERT.[^s1]

## Limitations and critiques

BEIR's authors flagged a **lexical annotation bias**. Many datasets were judged by pooling results from keyword systems, so documents found only by neural retrievers were often never labelled. On TREC-COVID, 30.6% of DPR's and 31.8% of TAS-B's top-10 hits were unjudged, against 6.4% for BM25; after the authors labelled 980 missing pairs, DPR's nDCG@10 rose from 0.332 to 0.445 while BM25 barely moved.[^s1] Scores therefore partly reflect how a dataset was built, not only retrieval quality. A 2023 follow-up by Kamalloo, Thakur and others added that complex neural tooling made results hard to reproduce and that there was no authoritative place to compare models, and responded with reference implementations for dense and sparse models and an official self-service leaderboard.[^s5]

## In practice

BEIR became the default yardstick for zero-shot retrieval and embedding models. The Massive Text Embedding Benchmark (MTEB) describes BEIR as the standard for evaluating embeddings on zero-shot IR, and its retrieval task reuses BEIR's datasets and evaluation, including all of the publicly available collections, with nDCG@10 as the main metric.[^s4] In that 2022–2023 study, SGPT-5.8B-msmarco was the strongest model on the BEIR subset, with an average retrieval score of 50.25 as reported by its authors.[^s4] The `beir` package also lets users plug in their own models or preprocess their own IR datasets into the same format, so teams can compare lexical, dense, sparse and re-ranking retrievers on data close to their application.[^s3]

## Connections

BEIR is an instance of **AI evaluation** applied to **information retrieval**, and it is **introduced in** the Thakur et al. paper.[^s1] Its best-known result concerns **BM25**, which it showed to be a robust zero-shot baseline, and it is the usual test for **semantic search** over dense **embeddings**, whose generalization gaps it exposed.[^s1] The strong showing of cross-encoder **reranking** on BEIR supports the common two-stage design of cheap retrieval followed by re-ranking.[^s1] BEIR's datasets are **used in MTEB**'s retrieval track, and retriever choices for **retrieval-augmented generation** are frequently justified with BEIR or MTEB retrieval scores.[^s4]

## Sources
[^s1]: Thakur, Reimers, Rücklé, Srivastava and Gurevych, "BEIR: A Heterogenous Benchmark for Zero-shot Evaluation of Information Retrieval Models", arXiv:2104.08663v4 (2021). https://arxiv.org/abs/2104.08663v4 (accessed 2026-11-09)
[^s2]: NeurIPS 2021 Datasets and Benchmarks Track, "BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models" (poster). https://neurips.cc/virtual/2021/29903 (accessed 2026-11-09)
[^s3]: beir-cellar/beir repository, GitHub. https://github.com/beir-cellar/beir (accessed 2026-11-09)
[^s4]: Muennighoff, Tazi, Magne and Reimers, "MTEB: Massive Text Embedding Benchmark", arXiv:2210.07316v2. https://arxiv.org/pdf/2210.07316v2 (accessed 2026-11-09)
[^s5]: Kamalloo, Thakur, Lassance, Ma, Yang and Lin, "Resources for Brewing BEIR: Reproducible Reference Models and an Official Leaderboard", arXiv:2306.07471 (2023). https://arxiv.org/abs/2306.07471 (accessed 2026-11-09)
