---
id: kt:attention-mechanism
type: Architecture
title: Attention mechanism
aliases: [neural attention, soft attention, Bahdanau attention, additive attention]
domain: transformers-and-llms
summary: >-
  A differentiable neural network component that builds an output as a weighted average of value
  vectors, with the weights computed by scoring a query against a set of keys and normalizing the
  scores with softmax, so a model can focus on the most relevant parts of its input.
maturity: foundational
broader: [kt:deep-learning]
related: [kt:self-attention, kt:sequence-to-sequence-learning, kt:recurrent-neural-network, kt:mechanistic-interpretability, kt:vision-language-model]
relations:
  - {predicate: introducedIn, object: kt:neural-machine-translation-by-jointly-learning-to-align-and-translate}
  - {predicate: extends, object: kt:sequence-to-sequence-learning}
  - {predicate: usedIn, object: kt:transformer-architecture}
  - {predicate: usedIn, object: kt:image-captioning}
  - {predicate: hasPart, object: kt:softmax-function}
sources:
  - id: s1
    title: "Neural Machine Translation by Jointly Learning to Align and Translate"
    publisher: Bahdanau, Cho and Bengio, ICLR 2015 (authors' arXiv version, 1409.0473)
    url: https://arxiv.org/pdf/1409.0473
    type: primary
    accessed: 2026-11-14
  - id: s2
    title: "Effective Approaches to Attention-based Neural Machine Translation"
    publisher: Luong, Pham and Manning, Proceedings of EMNLP 2015, pp. 1412–1421 (ACL Anthology D15-1166)
    url: https://aclanthology.org/D15-1166.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "11.3. Attention Scoring Functions"
    publisher: Zhang, Lipton, Li and Smola, Dive into Deep Learning (d2l.ai)
    url: https://www.d2l.ai/chapter_attention-mechanisms-and-transformers/attention-scoring-functions.html
    type: textbook
    accessed: 2026-11-14
  - id: s4
    title: "Show, Attend and Tell: Neural Image Caption Generation with Visual Attention"
    publisher: Xu et al., ICML 2015, PMLR vol. 37, pp. 2048–2057 (authors' arXiv version, 1502.03044)
    url: https://arxiv.org/abs/1502.03044v3
    type: primary
    accessed: 2026-11-14
  - id: s5
    title: "Attention is not not Explanation"
    publisher: Wiegreffe and Pinter, Proceedings of EMNLP-IJCNLP 2019, pp. 11–20 (ACL Anthology D19-1002)
    url: https://aclanthology.org/D19-1002/
    type: peer-reviewed
    accessed: 2026-11-14
created: 2026-11-14
---

# Attention mechanism

An **attention mechanism** lets a neural network compute, for each step of its work, a weighted average over a set of input representations, where the weights express how relevant each input is to the current need. In the general formulation, a *query* is scored against a set of *keys*, the scores are passed through a softmax so they are nonnegative and sum to one, and the output is the correspondingly weighted average of the *values* paired with those keys.[^s3] Because every step is differentiable, the model learns where to look through ordinary backpropagation rather than through a separate alignment or search procedure.[^s1]

## Origin

Attention entered mainstream deep learning through neural machine translation. Bahdanau, Cho and Bengio (published at ICLR 2015) argued that the standard encoder-decoder, which compresses an entire source sentence into one fixed-length vector, becomes a bottleneck, especially for long sentences.[^s1] Their model instead kept one annotation per source word from a bidirectional recurrent encoder and, before emitting each target word, computed a fresh context vector as a weighted sum of those annotations. The weights came from a small feedforward "alignment model" that scored the previous decoder state against each annotation and was trained jointly with the rest of the network.[^s1] They called the result a *soft* alignment: a weighting rather than a discrete choice, so gradients flow through it.[^s1]

On WMT '14 English-to-French, the baseline encoder-decoder's BLEU score fell sharply as sentences grew longer, while the attention model (RNNsearch-50) showed no clear decline even past 50 words; overall it scored 26.75 BLEU against the baseline's 17.82, though still below the phrase-based Moses system on the full test set.[^s1]

## How it works

Given a query **q**, keys **k**₁…**k**ₙ and values **v**₁…**v**ₙ, attention computes scores *a*(**q**, **k**ᵢ), normalizes them with softmax into weights αᵢ, and returns Σ αᵢ **v**ᵢ.[^s3] The design choice is mostly the scoring function:

- **Additive (Bahdanau) attention:** *a*(**q**, **k**) = **w**ᵥᵀ tanh(**W**_q **q** + **W**_k **k**), a one-hidden-layer MLP. It handles queries and keys of different sizes.[^s3]
- **Dot-product and "general" attention:** Luong, Pham and Manning compared a plain dot product, a bilinear form **h**ₜᵀ**W**ₐ**h̄**ₛ, and a concatenation-based score, alongside a location-only variant that learned poor alignments.[^s2]
- **Scaled dot-product attention:** dividing **q**ᵀ**k** by √*d* keeps the score variance near 1 when components are independent with unit variance, which stops the softmax from saturating; in matrix form it is softmax(**QK**ᵀ/√*d*)**V**, the mainstay of transformers.[^s3]

Practical implementations also apply a **masked softmax**, setting scores for padding positions to a large negative number so they receive effectively zero weight.[^s3]

Luong et al. further split attention into **global** attention over every source position and **local** attention over a window centred on a predicted aligned position, reweighted by a Gaussian.[^s2] Local attention improved on non-attentional baselines by 5.0 BLEU, and an ensemble reached 25.9 BLEU on WMT '15 English-to-German, 1.0 BLEU above the previous best reported system.[^s2]

## Beyond translation

The same idea transferred quickly to vision. Xu et al.'s "Show, Attend and Tell" (ICML 2015) attended over regions of convolutional image features while generating captions, trained either deterministically with backpropagation or stochastically by maximizing a variational lower bound, and reported state-of-the-art results on Flickr8k, Flickr30k and MS COCO at the time.[^s4] Visualizing its weights showed the model focusing on salient objects as it generated the corresponding words, which popularized attention maps as a way to inspect models.[^s4]

## Limitations and open questions

Standard attention scores the query against every key, so cost grows with the number of keys; this motivated Luong et al.'s local variant and, later, many efficient-attention methods.[^s2] Whether attention weights *explain* a prediction is contested: Wiegreffe and Pinter (EMNLP-IJCNLP 2019), responding to a paper titled "Attention is not Explanation," argued the answer depends on how explanation is defined and must account for the whole model, proposing diagnostic tests and concluding that earlier work had not shown attention to be useless for explainability.[^s5]

## Connections

Attention is a component of `kt:deep-learning` models, introduced in the paper `kt:neural-machine-translation-by-jointly-learning-to-align-and-translate`, and it **extends** `kt:sequence-to-sequence-learning` by removing the fixed-length bottleneck of the encoder-decoder built on `kt:recurrent-neural-network` layers.[^s1] Its scaled dot-product form is used in `kt:transformer-architecture`, where `kt:self-attention` applies attention within a single sequence.[^s3] Its weighting step **has part** `kt:softmax-function`.[^s3] It is **used in** `kt:image-captioning` and, by extension, in multimodal systems such as `kt:vision-language-model`.[^s4] The debate over attention as explanation links it to `kt:mechanistic-interpretability`, which seeks more faithful accounts of model internals.[^s5]

## Sources
[^s1]: Bahdanau, Cho and Bengio, "Neural Machine Translation by Jointly Learning to Align and Translate", ICLR 2015 (arXiv:1409.0473). https://arxiv.org/pdf/1409.0473 (accessed 2026-11-14)
[^s2]: Luong, Pham and Manning, "Effective Approaches to Attention-based Neural Machine Translation", EMNLP 2015, pp. 1412–1421. https://aclanthology.org/D15-1166.pdf (accessed 2026-11-14)
[^s3]: Zhang, Lipton, Li and Smola, "11.3. Attention Scoring Functions", Dive into Deep Learning. https://www.d2l.ai/chapter_attention-mechanisms-and-transformers/attention-scoring-functions.html (accessed 2026-11-14)
[^s4]: Xu et al., "Show, Attend and Tell: Neural Image Caption Generation with Visual Attention", ICML 2015, PMLR 37:2048–2057 (arXiv:1502.03044). https://arxiv.org/abs/1502.03044v3 (accessed 2026-11-14)
[^s5]: Wiegreffe and Pinter, "Attention is not not Explanation", EMNLP-IJCNLP 2019, pp. 11–20. https://aclanthology.org/D19-1002/ (accessed 2026-11-14)
