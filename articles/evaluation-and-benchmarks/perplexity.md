---
id: kt:perplexity
type: Concept
title: Perplexity
aliases: [PPL, language model perplexity, test-set perplexity]
domain: evaluation-and-benchmarks
summary: >-
  The standard intrinsic metric for language models: the inverse probability a model assigns to held-out text,
  normalized per token, equivalently the exponentiated average negative log-likelihood (cross-entropy); lower is better.
maturity: foundational
broader: [kt:ai-evaluation, kt:language-model]
related: [kt:large-language-model, kt:context-window, kt:tokenization, kt:benchmark-contamination]
relations:
  - {predicate: basedOn, object: kt:cross-entropy}
  - {predicate: extends, object: kt:information-theory}
sources:
  - id: s1
    title: "Speech and Language Processing (3rd ed. draft), Chapter 3: N-gram Language Models"
    publisher: Stanford University (Jurafsky & Martin), draft of August 2026
    url: https://web.stanford.edu/%7Ejurafsky/slp3/3.pdf
    type: textbook
    accessed: 2026-11-14
  - id: s2
    title: "Dive into Deep Learning, 9.3 Language Models (9.3.2 Perplexity)"
    publisher: d2l.ai (Zhang, Lipton, Li, Smola)
    url: https://d2l.ai/chapter_recurrent-neural-networks/language-model.html
    type: textbook
    accessed: 2026-11-14
  - id: s3
    title: "Perplexity of fixed-length models"
    publisher: Hugging Face Transformers documentation
    url: https://HuggingFace.co/docs/transformers/perplexity
    type: official-docs
    accessed: 2026-11-14
  - id: s4
    title: "What is Wrong with Perplexity for Long-context Language Modeling?"
    publisher: ICLR 2025 poster (Fang, Wang, Liu, Zhang, Jegelka, Gao, Ding, Wang)
    url: https://iclr.cc/virtual/2025/poster/28884
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "What is Wrong with Perplexity for Long-context Language Modeling? (arXiv:2410.23771v5, HTML version)"
    publisher: arXiv (Fang et al.; Peking University, MIT, Alibaba Group, TUM)
    url: https://arxiv.org/html/2410.23771v5
    type: primary
    accessed: 2026-11-14
created: 2026-11-14
---

# Perplexity

**Perplexity** (often abbreviated **PPL**) measures how well a probabilistic language model predicts a held-out sample of text. It is defined as the inverse of the probability the model assigns to the test sequence, normalized by the number of tokens, so a model that finds the text less surprising gets a lower score.[^s1] Jurafsky and Martin describe it as the standard intrinsic metric for language models, used both for classic n-gram models and for modern neural large language models.[^s1] Their textbook's historical notes credit the IBM speech recognition group with first applying the terms "language model" and "perplexity" to this technology.[^s1]

## Definition
For a test sequence W = w1…wN, perplexity is PP(W) = P(w1…wN)^(−1/N); expanding with the chain rule gives the N-th root of the product of 1/P(wi | w1…wi−1).[^s1] Hugging Face's documentation gives the same quantity in the form used for autoregressive models: PPL(X) = exp(−(1/t) Σ log pθ(xi | x<i)), the exponentiated average negative log-likelihood per token, which is also the exponentiated cross-entropy between the data and the model.[^s3] In information-theoretic terms, the per-token cross-entropy estimated from a long sample is an upper bound on the true entropy of the language, and perplexity is 2 raised to that cross-entropy in bits; a tighter bound means a better model.[^s1] *Dive into Deep Learning* accordingly defines it as the exponential of the average cross-entropy loss over a sequence's tokens.[^s2]

## Interpretation
Normalizing per token is what makes the metric usable: the raw probability of a sequence shrinks as text gets longer, so likelihoods of documents of different lengths cannot be compared fairly, while a per-token average can.[^s1][^s2] Perplexity can be read as a weighted average branching factor. In Jurafsky and Martin's toy example, a three-word language with a uniform model has perplexity 3, but a model that gives one word probability 0.8 scores about 1.89 on a test set dominated by that word, even though three choices remain possible.[^s1] *Dive into Deep Learning* frames the bounds: a model that is always certain and right scores 1, a model that ever assigns zero probability to the true token scores infinity, and a uniform model over the vocabulary scores the vocabulary size, which any useful model must beat.[^s2] As a classic illustration, n-gram models trained on 38 million words of Wall Street Journal text scored 962 (unigram), 170 (bigram) and 109 (trigram) on a 1.5-million-word test set, as reported in the August 2026 draft of the textbook.[^s1]

## Computing it for transformers
Transformer models have a fixed maximum input length, which complicates scoring long documents. Splitting text into disjoint chunks is fast but gives early tokens in each chunk little context, inflating perplexity; a sliding window gives every token more context but needs many forward passes, so practitioners use a strided window as a compromise.[^s3] In Hugging Face's worked example, GPT-2 Large on WikiText-2 scores about 19.44 with non-overlapping 1,024-token chunks and about 16.44 with a stride of 512, which shows how much the evaluation protocol alone can move the number.[^s3] The same documentation notes that perplexity is not well defined for masked language models such as BERT.[^s3]

## Limitations
- **Comparability.** Scores are only comparable between models with the same vocabulary, and since perplexity is computed over tokens, the tokenizer directly affects it.[^s1][^s3]
- **Test-set hygiene.** A model trained on, or repeatedly tuned against, the test set gets artificially low perplexity, so tuning should use a development set and the test set should match the target domain.[^s1]
- **Intrinsic, not extrinsic.** Lower perplexity does not guarantee better performance on a downstream task, so gains should be checked with an end-to-end evaluation where possible.[^s1]
- **Long context.** Fang et al. (ICLR 2025) argue that averaging over all tokens hides long-context ability, because most tokens are predictable from nearby text. Across their tested models, standard perplexity correlated weakly with long-context benchmarks (Pearson −0.18 on LongBench, 0.24 on LongEval, 0.27 on RULER), while their LongPPL, computed only on "key tokens" whose prediction depends on distant context, reached −0.96, −0.90 and −0.90.[^s4][^s5]

## Connections
Perplexity is a core metric of **AI evaluation** and the defining intrinsic measure of any **language model**, from n-grams to **large language models**.[^s1] It is **based on cross-entropy**, the loss these models are trained on, and **extends** ideas from **information theory** such as entropy measured in bits.[^s1][^s2] Its value depends on **tokenization**, since it is averaged per token, and on the **context window**, which determines how much history each prediction sees during scoring.[^s3][^s4] Because a model that has seen the test text scores deceptively well, it is directly exposed to **benchmark contamination**.[^s1]

## Sources
[^s1]: Jurafsky & Martin, *Speech and Language Processing* (3rd ed. draft, August 2026), Chapter 3: N-gram Language Models. https://web.stanford.edu/%7Ejurafsky/slp3/3.pdf (accessed 2026-11-14)
[^s2]: Zhang, Lipton, Li & Smola, *Dive into Deep Learning*, 9.3 Language Models. https://d2l.ai/chapter_recurrent-neural-networks/language-model.html (accessed 2026-11-14)
[^s3]: Hugging Face, "Perplexity of fixed-length models", Transformers documentation. https://HuggingFace.co/docs/transformers/perplexity (accessed 2026-11-14)
[^s4]: Fang et al., "What is Wrong with Perplexity for Long-context Language Modeling?", ICLR 2025 poster. https://iclr.cc/virtual/2025/poster/28884 (accessed 2026-11-14)
[^s5]: Fang et al., "What is Wrong with Perplexity for Long-context Language Modeling?", arXiv:2410.23771v5. https://arxiv.org/html/2410.23771v5 (accessed 2026-11-14)
