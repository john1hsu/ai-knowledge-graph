---
id: kt:a-neural-probabilistic-language-model
type: Work
title: A Neural Probabilistic Language Model
aliases: [Bengio et al. 2003, NPLM, feedforward neural language model paper]
domain: transformers-and-llms
summary: >-
  The paper by Yoshua Bengio, Réjean Ducharme, Pascal Vincent and Christian Jauvin (NIPS 2000; extended in
  JMLR 2003) that introduced the first widely influential neural language model, jointly learning a vector
  for each word and a feed-forward network that predicts the next word from those vectors.
maturity: foundational
broader: [kt:language-model, kt:artificial-neural-network]
related: [kt:word2vec, kt:perplexity, kt:large-language-model]
relations:
  - {predicate: createdBy, object: kt:yoshua-bengio}
  - {predicate: alternativeTo, object: kt:n-gram-language-model}
  - {predicate: enables, object: kt:embeddings}
sources:
  - id: s1
    title: "A Neural Probabilistic Language Model"
    publisher: Bengio, Ducharme, Vincent and Jauvin, Journal of Machine Learning Research 3 (Feb 2003), 1137-1155
    url: https://www.jmlr.org/papers/v3/bengio03a.html
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s2
    title: "A Neural Probabilistic Language Model (JMLR 2003, full text)"
    publisher: Bengio, Ducharme, Vincent and Jauvin; PDF hosted on Columbia University course reading list
    url: https://www.cs.columbia.edu/%7Eblei/seminar/2016_discrete_data/readings/BengioDucharmeVincentJanvin2003.pdf
    type: primary
    accessed: 2026-11-19
  - id: s3
    title: "A Neural Probabilistic Language Model"
    publisher: Bengio, Ducharme and Vincent, Advances in Neural Information Processing Systems 13 (NIPS 2000)
    url: https://papers.nips.cc/paper/1839-a-neural-probabilistic-language-model
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s4
    title: "Speech and Language Processing (3rd ed. draft), Chapter 6: Neural Networks"
    publisher: D. Jurafsky and J. H. Martin, Stanford University (draft of August 2026)
    url: https://web.stanford.edu/~jurafsky/slp3/6.pdf
    type: textbook
    accessed: 2026-11-19
  - id: s5
    title: "Yoshua Bengio, A.M. Turing Award laureate (2018)"
    publisher: Association for Computing Machinery
    url: https://amturing.acm.org/award_recipient/bengio_3406375
    type: primary
    accessed: 2026-11-19
created: 2026-11-19
---

# A Neural Probabilistic Language Model

*A Neural Probabilistic Language Model* is the paper that showed a neural network could beat the best statistical n-gram models at predicting the next word. A first version by Yoshua Bengio, Réjean Ducharme and Pascal Vincent appeared in *Advances in Neural Information Processing Systems 13* (NIPS 2000).[^s3] An extended journal version, adding Christian Jauvin as an author, was published in the *Journal of Machine Learning Research*, volume 3, pages 1137–1155, in 2003.[^s1] Its central move, learning a dense vector for every word together with the model that uses those vectors, is the direct ancestor of modern word embeddings and of the neural language models that later grew into LLMs.[^s4][^s5]

## The problem it attacked

A language model assigns probabilities to word sequences. The authors framed the difficulty as a curse of dimensionality: the sentences a model sees at test time are almost always different from every sentence in training.[^s3] Conventional n-gram models coped by gluing together very short overlapping fragments seen in training, so they had no way to recognise that an unseen sequence resembled a familiar one.[^s1] The paper's proposal was to fight the curse with a *distributed representation*: if each word is a point in a continuous feature space and similar words sit near one another, a sentence made of words similar to those in known sentences can still receive high probability.[^s1][^s3]

## How the model works

Each vocabulary word *i* is mapped to a real-valued feature vector C(i) of dimension *m*; the lookup matrix C is shared across every position in the context.[^s2] To predict word *t*, the vectors of the previous n−1 words are concatenated into an input x, and the network computes unnormalised scores y = b + Wx + U·tanh(d + Hx), where the optional W gives direct input-to-output connections.[^s2] A softmax over the whole vocabulary turns y into a probability for each candidate next word, and all parameters, including the word vectors, are trained together by stochastic gradient ascent on the penalised log-likelihood.[^s2]

Modern textbooks still present this architecture as the canonical feed-forward neural language model: one-hot context words pass through a shared embedding matrix, are concatenated to preserve order, go through a hidden layer and end in a vocabulary-sized softmax.[^s4] The textbook's illustration is that after training on "cat gets fed", such a model can give "fed" high probability after "the dog gets", because *cat* and *dog* receive similar embeddings; an n-gram model cannot make that leap.[^s4]

## Results

The JMLR paper evaluated on the Brown corpus (about 800,000 training words, vocabulary 16,383) and on 1995–96 Associated Press news (about 14 million training words, vocabulary 17,964).[^s2] On Brown the best neural model, mixed with a trigram, reached a test perplexity of 252 against 312 for the best n-gram baseline, roughly a 24% improvement; on AP News it reached 109 against 117 for a fifth-order Kneser-Ney back-off model, about 8%.[^s2] The network also kept improving as context grew from two to four words, where the n-gram baselines did not.[^s2]

## Costs and limitations

The price was computation. Almost all the work lies in the vocabulary-sized output layer, about 99.7% of computation in the AP News configuration, and training on AP News took about three weeks on 40 CPUs for only five epochs, using a parameter-parallel scheme over a cluster.[^s2] The authors listed remedies as future work: hierarchical decompositions of the output vocabulary, gradients from a subset of output words, and recurrent networks for longer context; they also noted that one vector per word cannot represent polysemy.[^s2] Textbooks still note that neural LMs are slower, costlier and less interpretable than n-gram models, which remain useful for some small tasks.[^s4]

## Influence

When Bengio shared the 2018 ACM A.M. Turing Award, ACM singled out this paper as introducing high-dimensional word embeddings as a representation of word meaning, and credited that idea with a major shift in machine translation and natural language understanding.[^s5] Its ingredients, a learned embedding layer, a neural next-word predictor and a softmax over the vocabulary, reappear in transformer language models, which textbooks present as the next step in neural language modelling.[^s4]

## Connections

The paper is a landmark in **language models** built from **artificial neural networks**, and it was **created by** **Yoshua Bengio** and colleagues.[^s1][^s5] It was proposed as an **alternative to** the **n-gram language model** and was benchmarked against n-grams using **perplexity**.[^s2] Its jointly learned word vectors **enable** the line of work on **embeddings**, including later static embedding methods such as **word2vec**.[^s4][^s5] The same embedding-plus-softmax design survives inside every **large language model**.[^s4]

## Sources
[^s1]: Bengio, Ducharme, Vincent and Jauvin, "A Neural Probabilistic Language Model", JMLR 3 (2003), 1137-1155. https://www.jmlr.org/papers/v3/bengio03a.html (accessed 2026-11-19)
[^s2]: Bengio, Ducharme, Vincent and Jauvin, "A Neural Probabilistic Language Model", JMLR 2003, full text. https://www.cs.columbia.edu/%7Eblei/seminar/2016_discrete_data/readings/BengioDucharmeVincentJanvin2003.pdf (accessed 2026-11-19)
[^s3]: Bengio, Ducharme and Vincent, "A Neural Probabilistic Language Model", NIPS 2000. https://papers.nips.cc/paper/1839-a-neural-probabilistic-language-model (accessed 2026-11-19)
[^s4]: Jurafsky and Martin, Speech and Language Processing, ch. 6 (Aug 2026 draft). https://web.stanford.edu/~jurafsky/slp3/6.pdf (accessed 2026-11-19)
[^s5]: ACM, "Yoshua Bengio", A.M. Turing Award laureate page. https://amturing.acm.org/award_recipient/bengio_3406375 (accessed 2026-11-19)
