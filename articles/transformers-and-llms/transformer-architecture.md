---
id: kt:transformer-architecture
type: Architecture
title: Transformer architecture
aliases: [Transformer, transformer model, transformer neural network]
domain: transformers-and-llms
summary: >-
  A neural network design that builds sequence representations from stacked blocks of multi-head
  self-attention and position-wise feed-forward layers joined by residual connections and normalization,
  used in encoder-only, decoder-only and encoder-decoder forms and the backbone of modern large language models.
maturity: established
broader: [kt:artificial-neural-network, kt:deep-learning]
related: [kt:context-window, kt:hugging-face-transformers, kt:layer-normalization, kt:residual-connection, kt:bert]
relations:
  - {predicate: introducedIn, object: kt:attention-is-all-you-need}
  - {predicate: hasPart, object: kt:self-attention}
  - {predicate: hasPart, object: kt:positional-encoding}
  - {predicate: alternativeTo, object: kt:recurrent-neural-network}
  - {predicate: enables, object: kt:large-language-model}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
sources:
  - id: s1
    title: "CS224N Lecture 5: Attention and Transformers (Winter 2026 slides)"
    publisher: Stanford University, CS224N Natural Language Processing with Deep Learning (Diyi Yang)
    url: https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture05-transformers.pdf
    type: academic
    accessed: 2026-11-11
  - id: s2
    title: "On Layer Normalization in the Transformer Architecture"
    publisher: Xiong et al., Proceedings of the 37th International Conference on Machine Learning (ICML 2020), PMLR 119
    url: https://proceedings.mlr.press/v119/xiong20b.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
    publisher: Devlin, Chang, Lee and Toutanova, NAACL-HLT 2019 (ACL Anthology N19-1423)
    url: https://aclanthology.org/N19-1423/
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"
    publisher: Raffel et al., Journal of Machine Learning Research 21(140), 2020
    url: https://www.jmlr.org/papers/v21/20-074.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "LLaMA: Open and Efficient Foundation Language Models (arXiv 2302.13971)"
    publisher: Touvron et al., Meta AI, February 2023 (authors' arXiv version)
    url: https://arxiv.org/pdf/2302.13971
    type: primary
    accessed: 2026-11-11
created: 2026-11-11
---

# Transformer architecture

The **Transformer architecture** is a way of building neural networks for sequences in which every layer lets each token gather information directly from every other token through **self-attention**, rather than passing a hidden state along step by step as a recurrent network does.[^s1] Introduced in 2017 for machine translation, the design has since become a general-purpose template: it is the backbone of masked language models such as BERT, of the unified text-to-text Transformer of Raffel et al., and of decoder-only large language models such as LLaMA.[^s3][^s4][^s5] This node covers the architecture as a reusable design and how it has changed; the founding paper has its own node.

## The Transformer block

A Transformer is a stack of identical blocks. Each block has two sub-layers.[^s1]

1. **Multi-head self-attention.** Every position produces a query, key and value vector from the same input sequence; a softmax over scaled query-key dot products decides how much of each value to mix in. Scores are divided by the square root of the per-head dimension so softmax inputs do not grow too large, and several heads run in parallel on separate projections before being concatenated.[^s1]
2. **Position-wise feed-forward network.** A small two-layer MLP applied to each position independently, supplying the nonlinearity that attention alone lacks.[^s1]

Each sub-layer is wrapped in a **residual connection**, so the layer learns only a correction to its input and gradients pass through the skip path unchanged, and in **layer normalization**, which rescales each vector to zero mean and unit variance with a learned gain and bias.[^s1] Because attention is order-blind, position information must be injected separately, through fixed sinusoids, learned absolute position vectors, or relative schemes.[^s1]

## Three families

Masking is what distinguishes the main variants.[^s1]

- **Encoder-only:** no mask, so every token sees full left and right context; suited to understanding tasks.[^s1] BERT is the canonical case, conditioning on both directions in every layer and adapting to new tasks with a single added output layer.[^s3]
- **Decoder-only:** a causal mask sets scores for future positions to negative infinity, so each token attends only to the past; this lets a language model train on all positions in parallel while still generating left to right.[^s1]
- **Encoder-decoder:** a bidirectional encoder reads the source and a masked decoder attends to it through cross-attention, the arrangement used for translation and other sequence-to-sequence tasks.[^s1]

Raffel et al. compared architectures, objectives and datasets systematically within one text-to-text framework, casting every language task as text in, text out.[^s4]

## How the design has evolved

**Where normalization goes.** The original layout normalized after each residual addition (Post-LN). Xiong et al. (ICML 2020) used mean-field analysis to show that this makes expected gradients near the output layer large at initialization, which is why Post-LN models need a carefully tuned learning-rate warm-up; moving normalization inside the residual branch (Pre-LN) kept gradients well behaved and let models train without warm-up in less time.[^s2]

**The modern decoder recipe.** Meta's LLaMA paper (February 2023) illustrates the changes most open decoder-only models adopted. It normalizes the input rather than the output of each sub-layer using RMSNorm, replaces ReLU with the SwiGLU activation, and drops absolute position embeddings in favour of rotary position embeddings (RoPE) applied at every layer, crediting these choices to GPT-3, PaLM and GPT-Neo respectively.[^s5] The LLaMA family spanned roughly 7B to 65B parameters.[^s5]

## Limitations and open questions

Self-attention compares every pair of positions, so its compute grows quadratically with sequence length, which becomes a bottleneck for inputs of tens of thousands of tokens.[^s1] Stanford's CS224N notes (Winter 2026) observe that, despite many cheaper attention variants, almost no large Transformer language models use anything but standard quadratic attention, because the alternatives often underperform at scale; whether better long-context architectures are possible remains open.[^s1] Learned absolute positions also cannot represent indices beyond the trained length, and sinusoidal encodings extrapolate poorly in practice.[^s1] Training stability is a further practical concern, addressed in part by normalization placement.[^s2]

## Connections

The architecture was **introduced in** *Attention Is All You Need* and is a kind of **artificial neural network** within **deep learning**.[^s1] Its core parts are **self-attention** and **positional encoding**, held together by **residual connections** and **layer normalization**.[^s1][^s2] It is the **alternative to** the **recurrent neural network** for sequence modelling, since it replaces stepwise recurrence with direct pairwise attention.[^s1] Encoder-only descendants include **BERT**, and the decoder-only form **enables** the **large language model**, as LLaMA's design shows.[^s3][^s5] Quadratic attention cost is what bounds a model's **context window**, and the **Hugging Face Transformers** library implements these model families in practice.[^s1]

## Sources
[^s1]: Diyi Yang, CS224N Lecture 5: Attention and Transformers, Stanford University, Winter 2026. https://web.stanford.edu/class/cs224n/slides_w26/cs224n-2026-lecture05-transformers.pdf (accessed 2026-11-11)
[^s2]: Xiong et al., "On Layer Normalization in the Transformer Architecture", ICML 2020, PMLR 119. https://proceedings.mlr.press/v119/xiong20b.html (accessed 2026-11-11)
[^s3]: Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", NAACL-HLT 2019. https://aclanthology.org/N19-1423/ (accessed 2026-11-11)
[^s4]: Raffel et al., "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", JMLR 21(140), 2020. https://www.jmlr.org/papers/v21/20-074.html (accessed 2026-11-11)
[^s5]: Touvron et al., "LLaMA: Open and Efficient Foundation Language Models", arXiv 2302.13971, 2023. https://arxiv.org/pdf/2302.13971 (accessed 2026-11-11)
