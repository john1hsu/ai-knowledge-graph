---
id: kt:word2vec
type: Algorithm
title: Word2vec
aliases: [word2vec, skip-gram with negative sampling, SGNS, skip-gram model, continuous bag-of-words model, CBOW]
domain: retrieval-and-knowledge
summary: >-
  A family of shallow, self-supervised models from Mikolov and colleagues at Google (2013) that learn one static
  dense vector per word by training a classifier to tell words that co-occur in a small window apart from randomly
  sampled noise words; the skip-gram and CBOW variants made large-scale word embeddings cheap to train.
maturity: foundational
broader: [kt:embeddings, kt:representation-learning]
related: [kt:semantic-search, kt:glove, kt:fasttext, kt:algorithmic-bias-and-fairness, kt:tf-idf]
relations:
  - {predicate: introducedIn, object: kt:efficient-estimation-of-word-representations-in-vector-space}
  - {predicate: createdBy, object: kt:google}
  - {predicate: influencedBy, object: kt:a-neural-probabilistic-language-model}
  - {predicate: alternativeTo, object: kt:glove}
  - {predicate: supersededBy, object: kt:transformer-architecture}
sources:
  - id: s1
    title: "Efficient Estimation of Word Representations in Vector Space"
    publisher: arXiv 1301.3781v3 (Mikolov, Chen, Corrado and Dean, Google), submitted 16 Jan 2013
    url: https://arxiv.org/abs/1301.3781
    type: primary
    accessed: 2026-11-11
  - id: s2
    title: "Distributed Representations of Words and Phrases and their Compositionality (full text)"
    publisher: ar5iv rendering of arXiv 1310.4546 (Mikolov, Sutskever, Chen, Corrado and Dean), NIPS 2013
    url: https://ar5iv.arxiv.org/html/1310.4546
    type: primary
    accessed: 2026-11-11
  - id: s3
    title: "Distributed Representations of Words and Phrases and their Compositionality"
    publisher: Google Research publication page, Neural Information Processing Systems (NIPS) 2013
    url: https://research.google/pubs/distributed-representations-of-words-and-phrases-and-their-compositionality/
    type: lab-research
    accessed: 2026-11-11
  - id: s4
    title: "Neural Word Embedding as Implicit Matrix Factorization"
    publisher: NeurIPS 2014 proceedings (Levy and Goldberg)
    url: https://proceedings.neurips.cc/paper/2014/hash/b78666971ceae55a8e87efb7cbfd9ad4-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings"
    publisher: NeurIPS 2016 proceedings (Bolukbasi, Chang, Zou, Saligrama and Kalai)
    url: https://proceedings.neurips.cc/paper/2016/hash/a486cd07e4ac3d270571622f4f316ec5-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s6
    title: "Speech and Language Processing, Chapter 5: Embeddings"
    publisher: Jurafsky and Martin, 3rd edition draft (August 2026 release), Stanford University
    url: https://web.stanford.edu/~jurafsky/slp3/5.pdf
    type: textbook
    accessed: 2026-11-11
created: 2026-11-11
---

# Word2vec

**Word2vec** is the name of a small group of neural models, and of the open-source tool that trains them, for learning *static* word embeddings: every vocabulary word receives one fixed vector, no matter which sentence it appears in. Tomas Mikolov, Kai Chen, Greg Corrado and Jeffrey Dean at Google described two cheap architectures in January 2013 and reported learning good vectors from a 1.6-billion-word dataset in under a day.[^s1] A follow-up paper at NIPS 2013, adding Ilya Sutskever, introduced negative sampling, subsampling of frequent words and phrase vectors, and released the training code publicly.[^s2][^s3]

## How it works

The two architectures invert each other. **Skip-gram** reads a centre word and predicts the words around it within a window; **continuous bag-of-words (CBOW)** predicts the centre word from its neighbours.[^s1][^s6] Computing a full softmax over the vocabulary is impractical because its cost grows with vocabulary size, which in these experiments ran from roughly 10^5 to 10^7 words.[^s2] The NIPS paper offered two cheaper training objectives:

- **Hierarchical softmax** places words at the leaves of a binary Huffman tree, so scoring a word touches only about log2 of the vocabulary size nodes.[^s2]
- **Negative sampling** turns the problem into binary classification: each real (word, context) pair is contrasted with *k* noise words drawn from the unigram distribution raised to the 3/4 power.[^s2]

The authors suggested *k* of 5–20 for small datasets and 2–5 for large ones.[^s2] Jurafsky and Martin's textbook frames skip-gram with negative sampling (SGNS) as logistic regression in which the probability that *c* is a true context of *w* is the sigmoid of their dot product; the model keeps separate target and context matrices, and practitioners use the target vectors alone or the sum of both.[^s6] The 0.75 exponent slightly boosts how often rare words are chosen as negatives.[^s6]

Two further tricks mattered in practice. Frequent words such as "the" are randomly discarded with probability 1 − √(t / f(w)), with *t* around 10^-5, which in the paper's experiments both sped training (about 2x to 10x) and made the learned vectors more consistent.[^s2] A simple count-based score merged frequent bigrams into single tokens over several passes, so that multi-word names could get their own vectors; the authors learned vectors for millions of phrases.[^s2]

## Results and the analogy property

On a news corpus of about one billion words, 300-dimensional skip-gram vectors trained with 15 negative samples reached 61% on the authors' word-analogy test, against 47% for hierarchical softmax without subsampling.[^s2] With about 33 billion words and 1,000 dimensions, the best phrase model scored 72% on a 3,218-question phrase-analogy set.[^s2] The vectors also composed additively: the sum of "Vietnam" and "capital" landed near "Hanoi".[^s2] The textbook cautions that this parallelogram trick needs the input words excluded from the answers and works best for frequent words and certain relations.[^s6]

## Theory, critiques and limitations

Levy and Goldberg showed that SGNS implicitly factorises a word-context matrix of pointwise mutual information shifted by a constant, linking word2vec to older count-based distributional methods; an exact SVD could match it on word similarity, though SGNS stayed ahead on analogies.[^s4] Because each word gets one vector, word2vec cannot separate senses ("bank" of a river versus a bank account), a limitation later addressed by contextual encoders.[^s6] Window size changes what is captured: short windows favour syntactically similar neighbours, long ones topical relatives.[^s6]

The vectors also absorb social bias from their training text. Bolukbasi and colleagues found strong gender stereotypes in embeddings trained on Google News and proposed a projection-based debiasing method.[^s5] The textbook notes that later work showed such debiasing reduces bias without removing it, so the problem remains open.[^s6]

## In practice

The open-source word2vec tool made large-scale embedding training routine, and the resulting static vectors, alongside GloVe, became standard fixed input representations for neural text models.[^s2][^s6] Successors kept the static-vector idea: fastText builds a word's vector from character n-grams, so it can embed unseen words, and GloVe fits vectors to global co-occurrence ratios.[^s6] Contextual models such as BERT instead give a word a different vector in each sentence, which is why newer retrieval and language-model systems generally rely on them rather than on one vector per word type.[^s6]

## Connections

Word2vec is a specific method for producing **embeddings**, itself an instance of **representation learning**.[^s6] It was **introduced in** *Efficient Estimation of Word Representations in Vector Space* and **created at Google**, and was **influenced by** earlier neural language models, which its authors reported beating on accuracy at lower computational cost.[^s1] **GloVe** is a contemporaneous **alternative**, and **fastText** extends the idea to subwords.[^s6] Its dense vectors contrast with sparse count-based weighting such as **TF-IDF**, although Levy and Goldberg showed the two families are closely linked through PMI; dense similarity is the basis of **semantic search**.[^s4][^s6] Its documented stereotypes made it a reference case in **algorithmic bias and fairness**.[^s5][^s6] For most tasks it has been **superseded by** contextual representations from the **transformer architecture**.[^s6]

## Sources

[^s1]: Mikolov, Chen, Corrado and Dean, "Efficient Estimation of Word Representations in Vector Space", arXiv 1301.3781 (2013). https://arxiv.org/abs/1301.3781 (accessed 2026-11-11)
[^s2]: Mikolov, Sutskever, Chen, Corrado and Dean, "Distributed Representations of Words and Phrases and their Compositionality", NIPS 2013 (ar5iv full text of arXiv 1310.4546). https://ar5iv.arxiv.org/html/1310.4546 (accessed 2026-11-11)
[^s3]: Google Research, "Distributed Representations of Words and Phrases and their Compositionality" (NIPS 2013). https://research.google/pubs/distributed-representations-of-words-and-phrases-and-their-compositionality/ (accessed 2026-11-11)
[^s4]: Levy and Goldberg, "Neural Word Embedding as Implicit Matrix Factorization", NeurIPS 2014. https://proceedings.neurips.cc/paper/2014/hash/b78666971ceae55a8e87efb7cbfd9ad4-Abstract.html (accessed 2026-11-11)
[^s5]: Bolukbasi, Chang, Zou, Saligrama and Kalai, "Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings", NeurIPS 2016. https://proceedings.neurips.cc/paper/2016/hash/a486cd07e4ac3d270571622f4f316ec5-Abstract.html (accessed 2026-11-11)
[^s6]: Jurafsky and Martin, *Speech and Language Processing*, 3rd ed. draft, Chapter 5 "Embeddings" (August 2026 release). https://web.stanford.edu/~jurafsky/slp3/5.pdf (accessed 2026-11-11)
