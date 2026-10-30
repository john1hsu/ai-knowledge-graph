---
id: kt:large-language-model
type: Concept
title: Large language model
aliases: [LLM, LLMs, large language models]
domain: transformers-and-llms
summary: >-
  A neural language model, almost always a transformer, with billions of parameters that is pretrained on
  very large text corpora to predict the next token and can then be prompted or adapted to perform a wide
  range of language tasks.
maturity: established
broader: [kt:language-model, kt:foundation-model]
related: [kt:scaling-laws, kt:in-context-learning, kt:ai-agent]
relations:
  - {predicate: basedOn, object: kt:transformer-architecture}
  - {predicate: trainedWith, object: kt:pretraining}
  - {predicate: trainedWith, object: kt:rlhf}
sources:
  - id: s1
    title: "Speech and Language Processing (3rd ed. draft), Chapter 7: Transformers and Pretraining"
    publisher: D. Jurafsky and J. H. Martin, Stanford University (draft of August 2026)
    url: https://web.stanford.edu/~jurafsky/slp3/7.pdf
    type: textbook
    accessed: 2026-10-30
  - id: s2
    title: "Language Models are Few-Shot Learners"
    publisher: Brown et al. (OpenAI), NeurIPS 2020
    url: https://papers.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html
    type: peer-reviewed
    accessed: 2026-10-30
  - id: s3
    title: "Scaling Laws for Neural Language Models"
    publisher: Kaplan et al. (OpenAI), arXiv 2001.08361 (authors' version)
    url: https://arxiv.org/abs/2001.08361v1
    type: primary
    accessed: 2026-10-30
  - id: s4
    title: "Training language models to follow instructions with human feedback"
    publisher: Ouyang et al. (OpenAI), NeurIPS 2022
    url: https://neurips.cc/virtual/2022/poster/52886
    type: peer-reviewed
    accessed: 2026-10-30
  - id: s5
    title: "On the Opportunities and Risks of Foundation Models"
    publisher: Bommasani et al., Stanford Center for Research on Foundation Models, arXiv 2108.07258
    url: https://arxiv.org/abs/2108.07258
    type: primary
    accessed: 2026-10-30
created: 2026-10-30
---

# Large language model

A large language model (LLM) is a neural network trained to assign probabilities to sequences of tokens, scaled to billions of parameters and trained on very large text corpora. Jurafsky and Martin's textbook describes the transformer as the standard architecture for building such models, and the dominant design is a causal (left-to-right, autoregressive or "decoder-only") model that generates text one token at a time, each conditioned on everything before it.[^s1] There is no sharp size threshold that makes a language model "large"; the term came into wide use after models such as GPT-3, a 175-billion-parameter autoregressive model that OpenAI reported in 2020 as roughly ten times larger than any previous non-sparse language model.[^s2]

## How it works

**Architecture.** A transformer LLM is a stack of identical blocks, from about 12 layers in small models to 96 or more in large ones. Each block combines multi-head self-attention, a position-wise feedforward layer (typically with a hidden size about four times the model width), residual connections and layer normalisation. Text is first split into tokens and mapped to embeddings; the final layer produces a probability distribution over the vocabulary for the next token.[^s1]

**Pretraining.** The model learns by next-token prediction on web crawls and other curated text, which in current practice often totals trillions of tokens. The textbook calls this self-supervised, because the text itself supplies the labels and no human annotation is needed. Training minimises cross-entropy loss, the negative log probability the model gives to the true next token, using teacher forcing so every position in a sequence contributes a training signal. Perplexity, the exponential of the mean cross-entropy, is the classic intrinsic measure, though it is only comparable between models that share a tokenizer.[^s1]

**Generation.** At inference the model is run repeatedly, appending each chosen token to the context. Greedy decoding tends to repeat itself, and pure random sampling can pick odd low-probability tokens, so practical systems use temperature, top-k or top-p (nucleus) sampling; a key-value (KV) cache stores earlier attention keys and values so they are not recomputed at every step.[^s1]

**Post-training.** A pretrained model continues text but does not reliably follow instructions. Ouyang et al. (NeurIPS 2022) fine-tuned GPT-3 on human-written demonstrations and then applied reinforcement learning from human feedback using human rankings of outputs; human raters preferred the resulting 1.3-billion-parameter InstructGPT over the 175-billion-parameter GPT-3, despite its 100x fewer parameters, and it was more truthful and less toxic.[^s4] Instruction tuning and preference optimisation of this kind turn a base model into a chat assistant.

## Why scale matters

Kaplan et al. (2020) found that language-model loss falls as a smooth power law in model size, dataset size and training compute across more than seven orders of magnitude, while details such as width versus depth matter little within a broad range. They also reported that larger models are more sample-efficient, implying that compute-efficient training uses very large models stopped well before convergence.[^s3] GPT-3 put the payoff on display: given a task description and a few examples purely as text, with no gradient updates, it performed well on translation, question answering and cloze tasks, sometimes approaching fine-tuned systems. This ability is now called in-context or few-shot learning.[^s2]

## Limitations and open questions

The GPT-3 authors themselves noted datasets where few-shot performance still lagged and concerns arising from training on large web corpora.[^s2] Ouyang et al. observed that making models larger does not by itself make them follow user intent: base models can produce untruthful, toxic or unhelpful text, and even the aligned models still made simple mistakes.[^s4] Bommasani et al., who group LLMs with similar systems under the term "foundation model", argue that capabilities which emerge from scale are poorly understood, that homogenisation around a few base models means their defects are inherited by everything built on top, and that the models raise questions of inequity, misuse, environmental and economic impact, and law.[^s5]

## In practice

Because one pretrained model can be adapted to many downstream tasks by prompting or fine-tuning, a handful of base models now sit beneath a large share of deployed language applications, the pattern Bommasani et al. describe as homogenisation.[^s5][^s2] Modern models handle context windows of hundreds of thousands of tokens, according to the 2026 draft of Jurafsky and Martin's textbook.[^s1]

## Connections

An LLM is a kind of **language model** and the best-known kind of **foundation model**, in Bommasani et al.'s sense of a broadly trained model adapted to many tasks.[^s5] It is **based on** the **transformer architecture** and **trained with** large-scale **pretraining** on next-token prediction, usually followed by **RLHF** or similar preference tuning.[^s1][^s4] Its behaviour as models grow is described by **scaling laws**, and its ability to learn tasks from examples in the prompt is **in-context learning**.[^s3][^s2] An **AI agent** typically uses an LLM as the component that decides which step or tool call to make next.

## Sources
[^s1]: D. Jurafsky and J. H. Martin, *Speech and Language Processing* (3rd ed. draft), Chapter 7 "Transformers and Pretraining", August 2026. https://web.stanford.edu/~jurafsky/slp3/7.pdf (accessed 2026-10-30)
[^s2]: T. Brown et al., "Language Models are Few-Shot Learners", NeurIPS 2020. https://papers.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html (accessed 2026-10-30)
[^s3]: J. Kaplan et al., "Scaling Laws for Neural Language Models", arXiv 2001.08361, 2020. https://arxiv.org/abs/2001.08361v1 (accessed 2026-10-30)
[^s4]: L. Ouyang et al., "Training language models to follow instructions with human feedback", NeurIPS 2022. https://neurips.cc/virtual/2022/poster/52886 (accessed 2026-10-30)
[^s5]: R. Bommasani et al., "On the Opportunities and Risks of Foundation Models", arXiv 2108.07258, 2021 (v3 2022). https://arxiv.org/abs/2108.07258 (accessed 2026-10-30)
