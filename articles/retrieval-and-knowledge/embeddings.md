---
id: kt:embeddings
type: Concept
title: Embeddings
aliases: [embedding, vector embeddings, word embeddings, dense vector representations, distributed representations]
domain: retrieval-and-knowledge
summary: >-
  Learned, dense, fixed-length vectors of real numbers that represent discrete items such as words, sentences,
  documents or images, arranged so that geometric closeness (for example, high cosine similarity) reflects
  semantic or functional similarity.
maturity: established
broader: [kt:representation-learning, kt:machine-learning]
related: [kt:word2vec, kt:vector-database, kt:semantic-search, kt:retrieval-augmented-generation, kt:large-language-model, kt:artificial-neural-network]
relations:
  - {predicate: introducedIn, object: kt:a-neural-probabilistic-language-model}
  - {predicate: enables, object: kt:semantic-search}
  - {predicate: usedIn, object: kt:retrieval-augmented-generation}
  - {predicate: alternativeTo, object: kt:bm25}
sources:
  - id: s1
    title: "A Neural Probabilistic Language Model"
    publisher: Journal of Machine Learning Research 3 (2003), 1137-1155 (Bengio, Ducharme, Vincent and Jauvin)
    url: https://www.jmlr.org/papers/v3/bengio03a.html
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s2
    title: "Efficient Estimation of Word Representations in Vector Space"
    publisher: Mikolov, Chen, Corrado and Dean, arXiv 1301.3781 (2013)
    url: https://arxiv.org/abs/1301.3781
    type: primary
    accessed: 2026-10-31
  - id: s3
    title: "15.1. Word Embedding (word2vec)"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola)
    url: https://d2l.ai/chapter_natural-language-processing-pretraining/word2vec.html
    type: textbook
    accessed: 2026-10-31
  - id: s4
    title: "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"
    publisher: EMNLP-IJCNLP 2019, pages 3982-3992 (Reimers and Gurevych)
    url: https://aclanthology.org/D19-1410
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s5
    title: "Dense Passage Retrieval for Open-Domain Question Answering"
    publisher: EMNLP 2020, pages 6769-6781 (Karpukhin, Oguz, Min, Lewis, Wu, Edunov, Chen and Yih)
    url: https://aclanthology.org/2020.emnlp-main.550
    type: peer-reviewed
    accessed: 2026-10-31
created: 2026-10-31
---

# Embeddings

An **embedding** maps a discrete object (a word, a sentence, a passage, an image, a user) to a dense vector of real numbers so that items with similar meaning or behaviour land near each other in the vector space. *Dive into Deep Learning* defines a word embedding as the mapping of words to real-valued vectors that serve as their feature representations, and contrasts it with one-hot encoding: because every pair of distinct one-hot vectors has a cosine similarity of zero, one-hot codes cannot express that "cat" is closer to "dog" than to "carburettor".[^s3] Embeddings are learned rather than hand-designed, which is why they sit at the heart of modern retrieval, recommendation and language modelling.

## Origin

The idea of learning a *distributed representation* for each word jointly with a predictive model was set out by Bengio, Ducharme, Vincent and Jauvin in the *Journal of Machine Learning Research* in 2003. They framed it as an answer to the curse of dimensionality in language modelling: test sentences are usually novel word sequences, but if each word has a learned vector, a new sentence built from words similar to those in training data can still be assigned high probability. Their neural model outperformed state-of-the-art n-gram models on two corpora, at the cost of millions of parameters that were hard to train at the time.[^s1]

A decade later, Mikolov, Chen, Corrado and Dean at Google proposed two much cheaper architectures (published in 2013 as arXiv 1301.3781), popularised as **word2vec**. They reported learning high-quality vectors from a corpus of about 1.6 billion words in under a day, with vectors that captured both syntactic and semantic similarities and beat earlier neural techniques on a word-similarity test set.[^s2]

## How it works

Word2vec has two variants. **Skip-gram** takes a centre word and predicts the words within a window of size *m* around it; the probability of a context word *o* given centre word *c* is a softmax over dot products, P(o | c) = exp(u_o · v_c) / Σ_i exp(u_i · v_c), where *v* and *u* are each word's centre and context vectors. **Continuous bag of words (CBOW)** reverses the task, predicting the centre word from the average of its context vectors.[^s3] Training is self-supervised: the raw text provides the targets, and gradient updates push words that occur in similar contexts toward similar vectors.[^s3]

Similarity between embeddings is usually measured with cosine similarity or a dot product. As an illustration, if "king" and "queen" are each represented by 300 numbers and their vectors point in nearly the same direction, their cosine similarity approaches 1, while an unrelated word's vector sits closer to orthogonal.[^s3]

## From words to sentences and passages

Word vectors alone do not give a good representation of a whole sentence, and full cross-encoding transformers are expensive to use for search. Reimers and Gurevych (EMNLP 2019) noted that finding the most similar pair among 10,000 sentences with BERT, which reads both sentences together, needs roughly 50 million inference passes, about 65 hours. Their **Sentence-BERT** fine-tunes BERT in siamese and triplet structures so each sentence is encoded independently into a vector compared by cosine similarity, cutting that search to about 5 seconds while keeping BERT-level accuracy on their benchmarks.[^s4]

The same *bi-encoder* (dual-encoder) idea underpins dense retrieval. Karpukhin and colleagues (EMNLP 2020) trained separate question and passage encoders on a relatively small set of question-passage pairs and reported that this dense retriever beat a strong Lucene-BM25 baseline by 9 to 19 percentage points absolute in top-20 passage retrieval accuracy across several open-domain QA datasets.[^s5]

## Limitations and open questions

Embeddings compress meaning into a fixed number of dimensions, so they can blur distinctions that matter, such as negation or exact identifiers, which is why sparse lexical methods like BM25 remain strong baselines and are often combined with dense vectors.[^s5] Static word vectors give each word a single vector regardless of context, a limitation that contextual encoders built on transformers were designed to address.[^s3][^s4] Because vectors are learned from data, they also inherit whatever associations and gaps that training data contains, and comparing vectors from different models is generally meaningless since each model defines its own space.[^s1][^s4]

## In practice

Today embeddings are produced by dedicated encoder models and stored in vector indexes, so that a query can be embedded once and matched against precomputed document vectors; this independence of encoding is exactly what made Sentence-BERT and DPR fast enough for large collections.[^s4][^s5] That pipeline is the retrieval half of retrieval-augmented generation, and it also powers semantic search, clustering, deduplication and recommendation.[^s4][^s5]

## Connections

Embeddings are a product of **representation learning** within **machine learning**, and are learned by **artificial neural networks**; the 2003 neural probabilistic language model is the work that introduced learned word vectors in this sense.[^s1] **Word2vec** is the classic method for producing them.[^s2][^s3] Sentence and passage embeddings **enable semantic search**, are stored and queried in a **vector database**, and are **used in retrieval-augmented generation** to give a **large language model** relevant context.[^s4][^s5] Dense embedding retrieval is the main **alternative to** sparse lexical ranking such as **BM25**, and the two are frequently combined.[^s5]

## Sources

[^s1]: Bengio, Ducharme, Vincent and Jauvin, "A Neural Probabilistic Language Model", Journal of Machine Learning Research 3 (2003), 1137-1155. https://www.jmlr.org/papers/v3/bengio03a.html (accessed 2026-10-31)
[^s2]: Mikolov, Chen, Corrado and Dean, "Efficient Estimation of Word Representations in Vector Space", arXiv 1301.3781 (2013). https://arxiv.org/abs/1301.3781 (accessed 2026-10-31)
[^s3]: Zhang, Lipton, Li and Smola, "15.1. Word Embedding (word2vec)", Dive into Deep Learning. https://d2l.ai/chapter_natural-language-processing-pretraining/word2vec.html (accessed 2026-10-31)
[^s4]: Reimers and Gurevych, "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks", EMNLP-IJCNLP 2019, 3982-3992. https://aclanthology.org/D19-1410 (accessed 2026-10-31)
[^s5]: Karpukhin et al., "Dense Passage Retrieval for Open-Domain Question Answering", EMNLP 2020, 6769-6781. https://aclanthology.org/2020.emnlp-main.550 (accessed 2026-10-31)
