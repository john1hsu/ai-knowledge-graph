---
id: kt:adam-optimizer
type: Algorithm
title: Adam optimizer
aliases: [Adam, adaptive moment estimation, Adam optimization algorithm]
domain: deep-learning
summary: >-
  A first-order stochastic optimization algorithm that gives every parameter its own step size, computed from
  bias-corrected exponential moving averages of the gradient (first moment) and the squared gradient (second
  moment); introduced by Kingma and Ba in 2014, it and its decoupled-weight-decay variant AdamW are the default
  optimizers for training most deep networks, including large language models.
maturity: established
broader: [kt:gradient-descent, kt:deep-learning]
related: [kt:backpropagation, kt:adamw, kt:rmsprop, kt:adagrad, kt:large-language-model, kt:dropout]
relations:
  - {predicate: introducedIn, object: kt:adam-a-method-for-stochastic-optimization}
  - {predicate: createdBy, object: kt:diederik-kingma}
  - {predicate: basedOn, object: kt:rmsprop}
  - {predicate: basedOn, object: kt:adagrad}
  - {predicate: dependsOn, object: kt:backpropagation}
  - {predicate: alternativeTo, object: kt:stochastic-gradient-descent}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: usedIn, object: kt:large-language-model}
sources:
  - id: s1
    title: "Adam: A Method for Stochastic Optimization"
    publisher: ICLR 2015 (Kingma and Ba), arXiv:1412.6980 v9
    url: https://arxiv.org/pdf/1412.6980
    type: primary
    accessed: 2026-11-10
  - id: s2
    title: "On the Convergence of Adam and Beyond"
    publisher: ICLR 2018 (Reddi, Kale and Kumar), ML Anthology
    url: https://mlanthology.org/iclr/2018/reddi2018iclr-convergence
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s3
    title: "Decoupled Weight Decay Regularization"
    publisher: ICLR 2019 (Loshchilov and Hutter), arXiv:1711.05101
    url: https://arxiv.org/abs/1711.05101
    type: primary
    accessed: 2026-11-10
  - id: s4
    title: "Dive into Deep Learning, section 12.10: Adam"
    publisher: Zhang, Lipton, Li and Smola (d2l.ai)
    url: https://d2l.ai/chapter_optimization/adam.html
    type: textbook
    accessed: 2026-11-10
  - id: s5
    title: "torch.optim.Adam"
    publisher: PyTorch documentation (main, 2.16 development build)
    url: https://docs.pytorch.org/docs/main/generated/torch.optim.Adam.html
    type: official-docs
    accessed: 2026-11-10
  - id: s6
    title: "Llama 2: Open Foundation and Fine-Tuned Chat Models"
    publisher: Meta AI (Touvron et al.), arXiv:2307.09288, 2023
    url: https://arxiv.org/pdf/2307.09288
    type: primary
    accessed: 2026-11-10
created: 2026-11-10
---

# Adam optimizer

**Adam** (short for *adaptive moment estimation*) is a first-order, gradient-based method for optimizing
stochastic objectives that adapts a separate step size for each parameter using running estimates of the
gradient's first and second moments.[^s1] Diederik Kingma and Jimmy Ba first posted the paper in December 2014
and published it at ICLR 2015; they presented it as easy to implement, cheap in computation and memory, and
well suited to problems with large datasets or many parameters.[^s1] Its stated design goal was to combine
the strengths of two earlier adaptive methods: AdaGrad, which copes well with sparse gradients, and RMSProp,
which copes well with online and non-stationary objectives.[^s1]

## How it works

At each step *t*, Adam takes the minibatch gradient *g_t* (computed by backpropagation) and updates two
exponential moving averages per parameter: a first moment *m_t = β1·m_(t−1) + (1−β1)·g_t* and an
uncentred second moment *v_t = β2·v_(t−1) + (1−β2)·g_t²*.[^s1] Because both averages start at zero, they are
biased toward zero early in training, especially when β is close to 1, so Adam divides them by *1 − β1^t*
and *1 − β2^t* to obtain bias-corrected estimates m̂ and v̂.[^s1] The parameter update is then
*θ_t = θ_(t−1) − α·m̂_t / (√v̂_t + ε)*.[^s1]

Read intuitively, the numerator is a momentum term that smooths noisy gradients, and the denominator rescales
each coordinate RMSProp-style, so parameters with consistently large gradients take smaller steps and rarely
updated ones take larger steps.[^s4] The paper's recommended defaults were α = 0.001, β1 = 0.9, β2 = 0.999 and
ε = 10⁻⁸,[^s1] and PyTorch's `torch.optim.Adam` uses the same defaults for learning rate, betas and epsilon.[^s5]
The same paper introduced **AdaMax**, a variant that replaces the second moment with an infinity-norm running
maximum and needs no bias correction for that term.[^s1]

## Limitations and open questions

Kingma and Ba proved an O(√T) regret bound in the online convex setting, under assumptions such as bounded
gradients.[^s1] Reddi, Kale and Kumar later showed at ICLR 2018 that this analysis had problems: they built a
simple convex example on which Adam fails to converge to the optimum, traced the failure to the short memory
of the exponential moving average, and proposed variants with "long-term memory" of past gradients — the
AMSGrad idea.[^s2] PyTorch exposes this as the `amsgrad` flag, which keeps a running elementwise maximum of the
second-moment estimate.[^s5] *Dive into Deep Learning* describes the same weakness as poor variance control
when gradient variance is high, and covers Yogi, which changes only the second-moment update so the estimate
does not forget past values too quickly.[^s4]

A second issue is regularization. Loshchilov and Hutter showed that L2 regularization and weight decay, which
are equivalent for plain SGD once scaled by the learning rate, are not equivalent for adaptive methods such as
Adam, and that many libraries implemented L2 while calling it weight decay.[^s3] Decoupling the decay from the
gradient step (**AdamW**) made the best decay factor independent of the learning rate and substantially
improved Adam's generalization on image classification, narrowing its gap with SGD plus momentum.[^s3] In
PyTorch, the `weight_decay` argument of `Adam` still adds the decay term to the gradient, while
`decoupled_weight_decay=True` makes it behave as AdamW.[^s5]

## In practice

Adam and AdamW are standard in modern deep learning, and large-model recipes usually tune the betas rather
than keep the defaults. For example, Meta's Llama 2 models (2023) were pretrained with AdamW using β1 = 0.9,
β2 = 0.95, ε = 10⁻⁵, weight decay 0.1, gradient clipping at 1.0, 2,000 warmup steps and a cosine learning-rate
schedule decaying to 10% of the peak.[^s6] The lower β2 makes the second-moment estimate react faster than the
0.999 default.[^s1][^s6] The textbook treatment also notes that the learning rate should still be reduced as
training converges, so Adam is normally paired with a schedule rather than run at a fixed rate.[^s4] A
practical cost is memory: Adam stores two extra state tensors per parameter (m and v), on top of the weights
and gradients.[^s1][^s5]

## Connections

Adam is a refinement of **gradient descent**, the broader family of first-order optimizers, and is a core
training tool of **deep learning**; it consumes gradients produced by **backpropagation**.[^s1][^s4] It is
**based on** **RMSProp** and **AdaGrad**, whose ideas it explicitly merges, and was **created by** Diederik
Kingma with Jimmy Ba in the paper *Adam: A Method for Stochastic Optimization*.[^s1] Its main **alternative**
is **stochastic gradient descent** with momentum, which Loshchilov and Hutter used as the generalization
baseline,[^s3] and its best-known descendant is **AdamW**.[^s3] It is **implemented in** **PyTorch**[^s5] and is
**used in** pretraining **large language models** such as Llama 2.[^s6] Like **dropout**, it is one of the
standard components of a deep-network training recipe, and the two interact through regularization choices.[^s3][^s4]

## Sources

[^s1]: Kingma and Ba, "Adam: A Method for Stochastic Optimization", ICLR 2015, arXiv:1412.6980 (v9, 2017). https://arxiv.org/pdf/1412.6980 (accessed 2026-11-10)
[^s2]: Reddi, Kale and Kumar, "On the Convergence of Adam and Beyond", ICLR 2018. https://mlanthology.org/iclr/2018/reddi2018iclr-convergence (accessed 2026-11-10)
[^s3]: Loshchilov and Hutter, "Decoupled Weight Decay Regularization", ICLR 2019, arXiv:1711.05101. https://arxiv.org/abs/1711.05101 (accessed 2026-11-10)
[^s4]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, section 12.10 "Adam". https://d2l.ai/chapter_optimization/adam.html (accessed 2026-11-10)
[^s5]: PyTorch documentation, "torch.optim.Adam" (main branch, 2.16 development build). https://docs.pytorch.org/docs/main/generated/torch.optim.Adam.html (accessed 2026-11-10)
[^s6]: Touvron et al. (Meta AI), "Llama 2: Open Foundation and Fine-Tuned Chat Models", arXiv:2307.09288, 2023. https://arxiv.org/pdf/2307.09288 (accessed 2026-11-10)
