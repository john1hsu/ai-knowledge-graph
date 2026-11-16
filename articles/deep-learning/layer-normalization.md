---
id: kt:layer-normalization
type: Technique
title: Layer normalization
aliases: [LayerNorm, layer norm, LN]
domain: deep-learning
summary: >-
  A neural-network normalization layer that standardizes the summed inputs of a layer using the mean and
  variance computed across that layer's features for each individual example, then applies a learned
  per-feature gain and bias; introduced by Ba, Kiros and Hinton in 2016, it is independent of batch size and
  is a standard component of transformers.
maturity: established
broader: [kt:deep-learning]
related: [kt:batch-normalization, kt:residual-connection, kt:attention-is-all-you-need, kt:vision-transformer]
relations:
  - {predicate: createdBy, object: kt:geoffrey-hinton}
  - {predicate: alternativeTo, object: kt:batch-normalization}
  - {predicate: usedIn, object: kt:transformer-architecture}
  - {predicate: usedIn, object: kt:recurrent-neural-network}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: alternativeTo, object: kt:rmsnorm}
sources:
  - id: s1
    title: "Layer Normalization"
    publisher: arXiv:1607.06450 (Ba, Kiros and Hinton, 2016)
    url: https://arxiv.org/abs/1607.06450v1
    type: primary
    accessed: 2026-11-16
  - id: s2
    title: "On Layer Normalization in the Transformer Architecture"
    publisher: Proceedings of the 37th ICML, PMLR 119:10524–10533 (2020) (Xiong et al.)
    url: https://proceedings.mlr.press/v119/xiong20b.html
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "Root Mean Square Layer Normalization"
    publisher: NeurIPS 2019 (Zhang and Sennrich)
    url: https://nips.cc/virtual/2019/poster/14195
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s4
    title: "LayerNorm"
    publisher: PyTorch documentation (v2.3)
    url: https://docs.pytorch.org/docs/2.3/generated/torch.nn.LayerNorm.html
    type: official-docs
    accessed: 2026-11-16
created: 2026-11-16
---

# Layer normalization

**Layer normalization** (LayerNorm, LN) is a layer that rescales the activations of a neural network so that, for each individual training example, the summed inputs to a layer have zero mean and unit variance across that layer's units, followed by a learned per-unit gain and bias. Jimmy Lei Ba, Jamie Ryan Kiros and Geoffrey Hinton proposed it in a July 2016 arXiv paper as a way to keep the training speed-ups of batch normalization while removing that method's two practical weaknesses: its dependence on the mini-batch size and its awkward fit with recurrent networks.[^s1]

## How it works

For a layer with H units and summed inputs a₁…a_H for one example, LN computes the mean μ and variance σ² over those H values, standardizes each input, and applies a learned gain γ and bias β before the nonlinearity:[^s1][^s4]

LN(a) = γ ⊙ (a − μ) / √(σ² + ε) + β

The key difference from batch normalization is the axis of the statistics. Batch normalization averages one feature over the examples in a mini-batch; layer normalization averages all features of one example. Because no other examples are involved, LN performs exactly the same computation during training and at test time, with no running averages to maintain.[^s1] The PyTorch implementation states the same property: its statistics come from the input in both training and evaluation modes.[^s4]

In PyTorch, `nn.LayerNorm(normalized_shape)` normalizes over the trailing dimensions given by `normalized_shape`, so passing the hidden size normalizes over the last dimension of each token vector. The default ε is 1e-5, the variance uses the biased estimator, and the learnable weight and bias are per element (initialized to ones and zeros), unlike batch and instance normalization, which learn one scale and shift per channel.[^s4]

## Recurrent networks

Batch normalization needs separate statistics for each time step of a recurrent network, which is impractical when sequences vary in length. Layer normalization sidesteps this by computing statistics independently at every time step from the current summed inputs, and the original authors reported that it markedly stabilized hidden-state dynamics in recurrent models and substantially reduced training time compared with earlier techniques.[^s1]

## Placement in transformers: Post-LN vs Pre-LN

LN became one of the defining components of the transformer, where it is applied together with residual connections around each attention and feed-forward sub-layer. Its position turns out to matter. Xiong and colleagues showed at ICML 2020 that in the original *Post-LN* arrangement, where normalization is applied after each residual addition, gradients for parameters near the output are large at initialization, making training with a large learning rate unstable and explaining why such models need a learning-rate warm-up phase.[^s2] Moving LN inside the residual branch, before each sub-layer (*Pre-LN*), keeps gradients well behaved at initialization; in their experiments Pre-LN transformers trained without warm-up matched the baselines while needing much less training time and hyperparameter tuning.[^s2]

## Limitations and variants

LN adds per-token reductions that cost time, which matters most in recurrent networks and very large models. Zhang and Sennrich (NeurIPS 2019) hypothesized that LN's re-centering (mean subtraction) is unnecessary and proposed **RMSNorm**, which divides by the root mean square of the inputs and keeps only re-scaling invariance.[^s3] Across several tasks and architectures RMSNorm performed comparably to LN while cutting running time by 7% to 64% depending on the model, as reported by its authors.[^s3] The broader lesson from both lines of work is that normalization choices interact with optimization, so the "right" variant and placement depend on architecture and training setup rather than being settled once and for all.[^s2][^s3]

## Connections

Layer normalization is a core technique of **deep learning** and an **alternative to batch normalization**: it trades batch statistics for per-example statistics, which removes batch-size sensitivity and the train/test discrepancy.[^s1] It was created by a group including **Geoffrey Hinton** and was designed with **recurrent neural networks** in mind, where it is applied at each time step.[^s1] It is **used in the transformer architecture** introduced in *Attention Is All You Need* and in descendants such as the **vision transformer**, where it works hand in hand with **residual connections**; the Pre-LN versus Post-LN choice is about exactly how the two are combined.[^s2] It is **implemented in PyTorch** as `nn.LayerNorm`.[^s4] **RMSNorm** is a cheaper alternative that drops mean-centering while keeping comparable accuracy in its authors' experiments.[^s3]

## Sources
[^s1]: Ba, J. L., Kiros, J. R. and Hinton, G. E., "Layer Normalization", arXiv:1607.06450, 2016. https://arxiv.org/abs/1607.06450v1 (accessed 2026-11-16)
[^s2]: Xiong, R. et al., "On Layer Normalization in the Transformer Architecture", ICML 2020, PMLR 119:10524–10533. https://proceedings.mlr.press/v119/xiong20b.html (accessed 2026-11-16)
[^s3]: Zhang, B. and Sennrich, R., "Root Mean Square Layer Normalization", NeurIPS 2019. https://nips.cc/virtual/2019/poster/14195 (accessed 2026-11-16)
[^s4]: PyTorch documentation, "LayerNorm" (v2.3). https://docs.pytorch.org/docs/2.3/generated/torch.nn.LayerNorm.html (accessed 2026-11-16)
