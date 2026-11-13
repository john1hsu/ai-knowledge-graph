---
id: kt:reranking
type: Technique
title: Reranking
aliases: [re-ranking, neural reranking, second-stage ranking, cross-encoder reranking, passage re-ranking]
domain: retrieval-and-knowledge
summary: >-
  A second retrieval stage in which a slower, more accurate model rescores and reorders the top candidates
  returned by a fast first-stage retriever, so that the most relevant results rise to the top of the list.
maturity: established
broader: [kt:information-retrieval]
related: [kt:semantic-search, kt:hybrid-search, kt:learning-to-rank, kt:colbert, kt:large-language-model]
relations:
  - {predicate: dependsOn, object: kt:bm25}
  - {predicate: basedOn, object: kt:bert}
  - {predicate: usedIn, object: kt:retrieval-augmented-generation}
  - {predicate: evaluatedOn, object: kt:beir}
  - {predicate: evaluatedOn, object: kt:ms-marco}
  - {predicate: trainedWith, object: kt:knowledge-distillation}
sources:
  - id: s1
    title: "Passage Re-ranking with BERT"
    publisher: arXiv:1901.04085 (Nogueira and Cho), v5, April 2020
    url: https://arxiv.org/pdf/1901.04085
    type: primary
    accessed: 2026-11-13
  - id: s2
    title: "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT"
    publisher: SIGIR 2020 (Khattab and Zaharia); author copy hosted at UC Berkeley
    url: https://people.eecs.berkeley.edu/~matei/papers/2020/sigir_colbert.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "Is ChatGPT Good at Search? Investigating Large Language Models as Re-Ranking Agents"
    publisher: EMNLP 2023, pages 14918-14937 (Sun, Yan, Ma, Wang, Ren, Chen, Yin and Ren)
    url: https://aclanthology.org/2023.emnlp-main.923
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "Is ChatGPT Good at Search? (full text, v3)"
    publisher: arXiv:2304.09542 (Sun et al.), authors' version
    url: https://arxiv.org/html/2304.09542v3
    type: primary
    accessed: 2026-11-13
  - id: s5
    title: "Retrieve & Re-Rank"
    publisher: Sentence Transformers documentation (sbert.net)
    url: https://sbert.net/examples/applications/retrieve_rerank
    type: official-docs
    accessed: 2026-11-13
  - id: s6
    title: "CS276 Lecture 15: Learning to Rank"
    publisher: Stanford University, CS276 Information Retrieval and Web Search (Manning and Nayak)
    url: https://web.stanford.edu/class/cs276/handouts/lecture15-learning-ranking-handouts-6-per.pdf
    type: academic
    accessed: 2026-11-13
created: 2026-11-13
---

# Reranking

**Reranking** (or re-ranking) is the second stage of a multi-stage retrieval pipeline. A cheap first-stage retriever, such as BM25 or a dense bi-encoder, pulls a shortlist of candidates from a large collection; a more expensive model then scores each candidate against the query and reorders the list. The split exists because the most accurate relevance models are far too slow to run over millions of documents, but are affordable over a few dozen to a thousand.[^s5][^s1] Reranking is now a standard component of search engines and of retrieval-augmented generation (RAG) systems, where the ordering of the top few passages decides what the language model gets to read.

## Origin

Learning a ranking function from data predates neural networks. Stanford's information retrieval course describes the learning-to-rank family: pointwise methods that score each document independently, pairwise methods such as the ranking SVM that learn which of two results should be ranked higher, and methods that optimise whole-list measures like NDCG directly. The course notes that machine-learned rankers often beat hand-tuned scoring functions, sometimes by using those functions as input features.[^s6]

The neural reranker in its modern form came from Rodrigo Nogueira and Kyunghyun Cho's 2019 report *Passage Re-ranking with BERT*. They fine-tuned BERT-Large as a binary relevance classifier and applied it to the top 1,000 passages BM25 returned for each MS MARCO query. Mean reciprocal rank at 10 (MRR@10) rose from about 16.5 for untuned BM25 to 35.8 on the evaluation set. The model took the top spot on the MS MARCO passage leaderboard, beating the previous best by 27% relative.[^s1] The authors framed it as the middle step of a three-stage question-answering system: retrieve, rerank, then generate an answer from the top passages. That shape is the template for today's RAG pipelines.[^s1]

## How it works

**Cross-encoders.** The query and one candidate are joined into a single input, with the query as segment A (truncated to 64 tokens in the original paper) and the passage as segment B, together capped at 512 tokens. The final [CLS] vector feeds a small classification layer that outputs a probability of relevance. Training uses cross-entropy over relevant and non-relevant pairs, and candidates are sorted by that probability.[^s1] Because every layer attends jointly over query and passage tokens, cross-encoders capture fine-grained matches that separately computed embeddings miss. The cost is one full transformer pass per query–document pair, which is why the Sentence Transformers documentation recommends retrieving a shortlist (for example about 100 passages) with a bi-encoder or lexical search and running the cross-encoder only over that shortlist.[^s5]

**Late interaction.** ColBERT, presented at SIGIR 2020, encodes the query and document separately into per-token embeddings. For each query token it finds the most similar document token (the "MaxSim" operator), then sums those maxima into a score; the interaction step has no trainable parameters. Document embeddings can be computed offline. Reranking BM25's top 1,000 results on MS MARCO took 61 ms per query on a V100 GPU, compared with 10,700 ms for a BERT-base cross-encoder, a speedup of over 170×, and about 13,900× fewer FLOPs. Effectiveness was competitive with the cross-encoder.[^s2] The same paper showed that ColBERT can also retrieve end to end from a vector index, which raised Recall@1000 on MS MARCO from 81.4 when reranking BM25 candidates to 96.8.[^s2] That result shows the main ceiling on any reranker: it cannot recover a relevant document the first stage never returned.

**LLM rerankers.** Sun et al. (EMNLP 2023) prompted instruction-following LLMs to output a permutation of passage identifiers, such as [2] > [3] > [1], rather than scores. Context limits meant they could not see every candidate at once, so they used a sliding window of 20 passages, stepping 10 at a time from the back of BM25's top 100 to the front.[^s4] They reported that GPT-4 used this way was competitive with, and sometimes better than, supervised rerankers on standard benchmarks. They also built a new test set, NovelEval, to check for training-data contamination.[^s3] Because GPT-4 reranking was too slow and expensive for commercial search, they distilled its rankings into a 440M-parameter model that, by their report, outperformed a 3B-parameter supervised model on BEIR.[^s3][^s4]

## Limitations and trade-offs

- **Recall ceiling.** The first stage caps quality. Sun et al. note that results also depend on the order of the initial candidates.[^s4][^s2]
- **Latency and cost.** Cost scales with the number of candidates times model size. Choosing *k* trades recall against response time.[^s5][^s2]
- **Instability of generative rankers.** LLM permutations can vary from run to run, and long passages in low-resource languages use up the context budget.[^s4]
- **Domain shift.** Rerankers fine-tuned on MS MARCO web queries may transfer unevenly to specialised corpora, which is why zero-shot suites such as BEIR are used to evaluate them.[^s3]

## In practice

A common pattern, described in the Sentence Transformers documentation, is dense or lexical retrieval of on the order of a hundred candidates, a cross-encoder or late-interaction reranker over them, and then the top handful of passages passed to the generator in a RAG system. Pretrained MS MARCO cross-encoders are distributed through libraries such as Sentence Transformers, which also supports in-document search: with only a few paragraphs, the retrieval stage can be skipped and every paragraph scored directly.[^s5]

## Connections

Reranking is a stage of **information retrieval** and the learned descendant of **learning to rank**.[^s6] It **depends on** a first-stage retriever, classically **BM25**, and it complements **semantic search** and **hybrid search**, which supply its candidates.[^s1][^s5] The cross-encoder design is **based on BERT**. **ColBERT** offers a cheaper late-interaction alternative.[^s1][^s2] LLM rerankers bring **large language models** into the loop and are compressed back into small models through **knowledge distillation**.[^s3] Rerankers are **evaluated on** MS MARCO and **BEIR**, and are **used in retrieval-augmented generation** to choose the context a model reads.[^s1][^s3]

## Sources
[^s1]: Nogueira and Cho, "Passage Re-ranking with BERT", arXiv:1901.04085, 2019. https://arxiv.org/pdf/1901.04085 (accessed 2026-11-13)
[^s2]: Khattab and Zaharia, "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT", SIGIR 2020. https://people.eecs.berkeley.edu/~matei/papers/2020/sigir_colbert.pdf (accessed 2026-11-13)
[^s3]: Sun et al., "Is ChatGPT Good at Search? Investigating Large Language Models as Re-Ranking Agents", EMNLP 2023. https://aclanthology.org/2023.emnlp-main.923 (accessed 2026-11-13)
[^s4]: Sun et al., "Is ChatGPT Good at Search?", arXiv:2304.09542v3. https://arxiv.org/html/2304.09542v3 (accessed 2026-11-13)
[^s5]: Sentence Transformers, "Retrieve & Re-Rank". https://sbert.net/examples/applications/retrieve_rerank (accessed 2026-11-13)
[^s6]: Manning and Nayak, CS276 Lecture 15 "Learning to Rank", Stanford University. https://web.stanford.edu/class/cs276/handouts/lecture15-learning-ranking-handouts-6-per.pdf (accessed 2026-11-13)
