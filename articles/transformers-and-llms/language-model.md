---
id: kt:language-model
type: Concept
title: Language model
aliases: [statistical language model, probabilistic language model, language modeling]
domain: transformers-and-llms
summary: >-
  A model that assigns probabilities to sequences of words or tokens, usually by predicting a
  probability distribution over the next token given the preceding ones; it spans n-gram counting
  models, neural networks and today's large language models.
maturity: foundational
broader: [kt:natural-language-processing, kt:generative-model]
related: [kt:n-gram-language-model, kt:recurrent-neural-network, kt:large-language-model]
relations:
  - {predicate: basedOn, object: kt:markov-chain}
  - {predicate: evaluatedOn, object: kt:perplexity}
  - {predicate: usedIn, object: kt:automatic-speech-recognition}
sources:
  - id: s1
    title: "Speech and Language Processing (3rd ed. draft), Chapter 3: N-gram Language Models"
    publisher: D. Jurafsky and J. H. Martin, Stanford University (draft of August 19, 2026)
    url: https://web.stanford.edu/%7Ejurafsky/slp3/3.pdf
    type: textbook
    accessed: 2026-11-28
  - id: s2
    title: "A Mathematical Theory of Communication"
    publisher: C. E. Shannon, Bell System Technical Journal 27 (1948); reprint hosted by MIT CSAIL
    url: https://people.csail.mit.edu/dmoshkov/courses/codes/shannon1948.pdf
    type: primary
    accessed: 2026-11-28
  - id: s3
    title: "A Neural Probabilistic Language Model"
    publisher: Bengio, Ducharme, Vincent and Jauvin, Journal of Machine Learning Research 3 (2003), 1137-1155
    url: https://www.jmlr.org/papers/v3/bengio03a.html
    type: peer-reviewed
    accessed: 2026-11-28
  - id: s4
    title: "Recurrent neural network based language model"
    publisher: Mikolov, Karafiát, Burget, Černocký and Khudanpur, Proc. Interspeech 2010, 1045-1048
    url: https://www.isca-archive.org/interspeech_2010/mikolov10_interspeech.html
    type: peer-reviewed
    accessed: 2026-11-28
  - id: s5
    title: "Language Models are Unsupervised Multitask Learners"
    publisher: Radford, Wu, Child, Luan, Amodei and Sutskever (OpenAI technical report); PDF hosted by Bau Lab
    url: https://papers.baulab.info/papers/Radford-2018.pdf
    type: primary
    accessed: 2026-11-28
created: 2026-11-28
---

# Language model

A **language model** is a machine learning model that predicts upcoming words: given a context, it outputs a probability for each possible next word, and by extension it can assign a probability to an entire sentence.[^s1] The idea is older than modern machine learning and covers a whole family of methods, from count-based n-gram tables to recurrent networks and the transformer-based large language models that now dominate the field.[^s1][^s4][^s5]

## The core formulation

Any language model rests on the chain rule of probability. The probability of a sequence w₁…wₙ is factored into a product of conditionals, P(w₁:ₙ) = ∏ₖ P(wₖ | w₁:ₖ₋₁), so the whole task reduces to estimating the next-word distribution given a history.[^s1] The same factorization is the starting point of neural work: the GPT-2 report frames language modeling as unsupervised distribution estimation and writes the joint probability exactly as this product of next-symbol conditionals.[^s5]

The practical difficulty is that long histories are almost never repeated, because language is creative, so their probabilities cannot be estimated by counting.[^s1] Bengio and colleagues described this as a curse of dimensionality: the word sequences a model meets at test time are likely to differ from every sequence it saw in training.[^s3] The history of language modeling is largely a history of answers to that problem.

## From Shannon to n-grams

Claude Shannon's 1948 paper treated English text as a stochastic (Markov) process and built a ladder of artificial approximations to it: random letters, letters drawn with English frequencies, letters conditioned on the previous one (digrams) or two (trigrams), and then words drawn independently or conditioned on the previous word.[^s2] He produced the higher-order samples by hand, opening a book at random and recording what followed a chosen letter or word, and observed that each step looked more like English.[^s2] Jurafsky and Martin credit Shannon (1948), along with Miller and Selfridge (1950), with the idea of generating text by sampling from such a model.[^s1]

The **n-gram model** turns this into an estimator through the Markov assumption: it truncates the history to the previous n − 1 words, for example P(wₙ | w₁:ₙ₋₁) ≈ P(wₙ | wₙ₋₁) for a bigram model. Probabilities are then maximum-likelihood estimates from relative frequencies, such as C(wₙ₋₁ wₙ) / C(wₙ₋₁).[^s1] Because most possible n-grams never occur in training, the count matrices are extremely sparse and higher-order models overfit, which is why practical n-gram models rely on smoothing and interpolation and why their training data must match the target genre.[^s1]

## Evaluation

Language models are evaluated extrinsically, by their effect on a downstream system, or intrinsically by **perplexity**: the inverse probability the model assigns to a held-out test set, normalized by the number of tokens, so lower is better.[^s1] In a Wall Street Journal experiment reported by Jurafsky and Martin, models trained on 38 million words scored perplexities of 962 (unigram), 170 (bigram) and 109 (trigram) on a 1.5-million-word test set, showing how longer contexts help.[^s1] Perplexity is closely tied to cross-entropy from information theory, the framework Shannon introduced.[^s1][^s2]

## Neural language models

Bengio et al. (JMLR 2003) proposed learning a distributed vector representation for every word jointly with a neural network that computes next-word probabilities from those vectors, so that an unseen sentence made of words similar to familiar ones still receives high probability. They reported that this significantly improved on state-of-the-art n-gram models and could exploit longer contexts.[^s3] Mikolov et al. (Interspeech 2010) replaced the fixed window with a recurrent network; they reported around a 50% reduction in perplexity from a mixture of RNN models compared with a state-of-the-art backoff model, and around an 18% reduction in word error rate on a Wall Street Journal speech recognition task, while noting the high training cost.[^s4]

Transformers then scaled the same objective. The GPT-2 report from OpenAI trained transformer language models of up to about 1.5 billion parameters on WebText, a corpus of roughly 40 GB built from outbound Reddit links, and showed that such models could attempt downstream tasks zero-shot, without changing parameters or architecture.[^s5] That observation, that a good enough next-token predictor implicitly learns many tasks, is the bridge from classical language modeling to large language models.[^s5]

## Limitations

Every language model is bounded by its training distribution: n-gram models trained on Shakespeare and on newspaper text share almost no predictions, and higher-order n-grams can simply reproduce training passages.[^s1] Neural models generalize far better through shared representations, but their training is computationally expensive, a cost already flagged in the 2003 and 2010 papers.[^s3][^s4]

## Connections

Language modeling is a core task of **natural language processing** and a kind of **generative model**, since a trained model can be sampled to produce text.[^s1] Its classical form, the **n-gram language model**, rests on the Markov assumption of a **Markov chain**, the process Shannon used for his approximations of English.[^s1][^s2] It is measured with **perplexity** and was long developed as a component of **automatic speech recognition**, where both the RNN language model and earlier n-gram models were evaluated.[^s1][^s4] The **recurrent neural network** language model and the transformer models of GPT-2 lead directly to the **large language model**.[^s4][^s5]

## Sources
[^s1]: D. Jurafsky and J. H. Martin, *Speech and Language Processing* (3rd ed. draft, August 19, 2026), Chapter 3: N-gram Language Models. https://web.stanford.edu/%7Ejurafsky/slp3/3.pdf (accessed 2026-11-28)
[^s2]: C. E. Shannon, "A Mathematical Theory of Communication", Bell System Technical Journal 27 (1948). https://people.csail.mit.edu/dmoshkov/courses/codes/shannon1948.pdf (accessed 2026-11-28)
[^s3]: Y. Bengio, R. Ducharme, P. Vincent and C. Jauvin, "A Neural Probabilistic Language Model", JMLR 3 (2003), 1137-1155. https://www.jmlr.org/papers/v3/bengio03a.html (accessed 2026-11-28)
[^s4]: T. Mikolov, M. Karafiát, L. Burget, J. Černocký and S. Khudanpur, "Recurrent neural network based language model", Proc. Interspeech 2010, 1045-1048. https://www.isca-archive.org/interspeech_2010/mikolov10_interspeech.html (accessed 2026-11-28)
[^s5]: A. Radford, J. Wu, R. Child, D. Luan, D. Amodei and I. Sutskever, "Language Models are Unsupervised Multitask Learners", OpenAI technical report. https://papers.baulab.info/papers/Radford-2018.pdf (accessed 2026-11-28)
