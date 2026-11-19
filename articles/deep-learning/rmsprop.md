---
id: kt:rmsprop
type: Algorithm
title: RMSprop
aliases: [RMSProp, root mean square propagation, rmsprop optimizer]
domain: deep-learning
summary: >-
  An adaptive learning-rate optimizer, presented by Geoffrey Hinton in his 2012 Coursera lectures and credited to
  Tijmen Tieleman, that divides each parameter's gradient by the square root of an exponential moving average of
  that parameter's recent squared gradients; it was never formally published but became a standard deep-learning
  optimizer and a direct ancestor of Adam.
maturity: established
broader: [kt:stochastic-gradient-descent, kt:deep-learning]
related: [kt:adagrad, kt:adam-optimizer, kt:deep-q-network, kt:long-short-term-memory, kt:momentum]
relations:
  - {predicate: createdBy, object: kt:geoffrey-hinton}
  - {predicate: createdBy, object: kt:tijmen-tieleman}
  - {predicate: basedOn, object: kt:rprop}
  - {predicate: extends, object: kt:adagrad}
  - {predicate: alternativeTo, object: kt:adadelta}
  - {predicate: implementedIn, object: kt:pytorch}
sources:
  - id: s1
    title: "Neural Networks for Machine Learning, Lecture 6 (6e: rmsprop) slides"
    publisher: Geoffrey Hinton with Nitish Srivastava and Kevin Swersky; hosted for University of Toronto CSC321 (2016)
    url: https://www.cs.toronto.edu/~bonner/courses/2016s/csc321/lectures/lec6.pdf
    type: academic
    accessed: 2026-11-19
  - id: s2
    title: "12.8. RMSProp"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), d2l.ai
    url: https://d2l.ai/chapter_optimization/rmsprop.html
    type: textbook
    accessed: 2026-11-19
  - id: s3
    title: "torch.optim.RMSprop (PyTorch 2.3 documentation)"
    publisher: PyTorch
    url: https://docs.pytorch.org/docs/2.3/generated/torch.optim.RMSprop.html
    type: official-docs
    accessed: 2026-11-19
  - id: s4
    title: "Generating Sequences With Recurrent Neural Networks"
    publisher: Alex Graves, arXiv:1308.0850 (2013), ar5iv rendering
    url: https://ar5iv.labs.arxiv.org/html/1308.0850
    type: primary
    accessed: 2026-11-19
  - id: s5
    title: "An overview of gradient descent optimization algorithms"
    publisher: Sebastian Ruder, arXiv:1609.04747 (2016)
    url: https://arxiv.org/pdf/1609.04747
    type: preprint
    accessed: 2026-11-19
created: 2026-11-19
---

# RMSprop

**RMSprop** (root mean square propagation) is a first-order optimizer that gives every weight its own effective step size. For each weight it keeps a running average of recent squared gradients and divides the current gradient by the square root of that average, so weights with consistently large gradients take smaller steps and weights with small gradients take relatively larger ones.[^s1][^s2] Geoffrey Hinton presented it in Lecture 6e of his Coursera course *Neural Networks for Machine Learning* (2012), where the slides attribute the idea to Tijmen Tieleman as unpublished work.[^s1] It never appeared as a peer-reviewed paper; researchers still cite the lecture.[^s2][^s5]

## Origin: a mini-batch version of rprop

Hinton framed RMSprop as a fix for **rprop**, a full-batch method that uses only the sign of each gradient, which amounts to dividing the gradient by its own magnitude.[^s1] That breaks down with mini-batches because each batch is divided by a different number. In the lecture's example, a weight gets a small positive gradient on nine mini-batches and a larger negative one on the tenth, so it should stay roughly where it is. Mini-batch rprop would instead push it up nine times and down once, so it would drift.[^s1] RMSprop makes the divisor change slowly by averaging squared gradients over many mini-batches.[^s1]

## How it works

With gradient *g_t*, decay rate *γ* and learning rate *η*, RMSprop maintains a leaky average of squared gradients and scales the step by it:[^s2]

- *s_t = γ·s_{t−1} + (1 − γ)·g_t²*
- *θ_t = θ_{t−1} − η·g_t / √(s_t + ε)*

The lecture slide uses γ = 0.9, so each step mixes 90% history with 10% new squared gradient.[^s1] Hinton also suggested a learning rate of 0.001.[^s5] The small constant ε prevents division by zero, and d2l.ai uses 10⁻⁶.[^s2] Because the average forgets old gradients, it reflects about the last 1/(1 − γ) steps rather than the whole history.[^s2]

That forgetting is the key difference from **AdaGrad**. AdaGrad sums every past squared gradient, so its effective learning rate can only shrink, roughly as t^(−1/2). RMSprop's leaky average lets the per-coordinate scaling adapt without forcing that decay. The global learning-rate schedule is then up to the practitioner.[^s2] Ruder therefore describes RMSprop as a response to AdaGrad's rapidly vanishing learning rates. He notes that **Adadelta** was developed independently around the same time and that RMSprop matches the first update vector of Adadelta.[^s5]

## Variants and implementation details

Alex Graves's 2013 handwriting-generation experiments used a variant that also tracks a running average of the gradient itself. It divides by √(n − g² + ε), an estimate of the gradient's running variance rather than its raw second moment, and adds a momentum term (decay 0.95, momentum 0.9, learning rate 0.0001).[^s4] PyTorch exposes this as `centered=True` and cites Graves for it.[^s3]

Frameworks differ in their defaults and arithmetic. As of the PyTorch 2.3 documentation, `torch.optim.RMSprop` defaults to `lr=0.01`, `alpha=0.99` (the decay rate), `eps=1e-08`, `momentum=0` and `centered=False`.[^s3] PyTorch adds ε *after* taking the square root, √v + ε, and its documentation notes that TensorFlow does the reverse. Hyperparameters therefore don't transfer exactly between libraries.[^s3]

## Limitations and practice

The lecture itself flagged open questions. Standard momentum helps less with RMSprop than usual, and the best way to combine RMSprop with per-connection adaptive rates was left unresolved.[^s1] RMSprop has no bias correction. Its averages start at zero, so the scaling is unreliable in early steps. **Adam** adds bias correction and a momentum-style first moment on top of RMSprop. Ruder cites evidence that this gives Adam a slight edge late in training, when gradients get sparser, and suggests Adam as a reasonable default overall.[^s5] RMSprop is still a built-in optimizer in mainstream frameworks, and it has a track record on recurrent networks: Graves used it to train LSTM sequence generators.[^s3][^s4]

## Connections

RMSprop is a form of **stochastic gradient descent** with per-parameter preconditioning, and it became one of the workhorse optimizers of **deep learning**.[^s2] It was **created by** Geoffrey Hinton and Tijmen Tieleman, and it is **based on** rprop, recast for mini-batches.[^s1] It **extends** AdaGrad by replacing AdaGrad's ever-growing sum with a moving average.[^s2][^s5] It is an **alternative to** Adadelta, its independently developed near-twin.[^s5] The Adam optimizer builds directly on it.[^s5] It is **implemented in** PyTorch, including the centered variant introduced in Graves's LSTM work.[^s3][^s4] It is related to momentum, which RMSprop can be combined with.[^s1][^s3] The deep Q-network article also records its use in DQN training.

## Sources
[^s1]: G. Hinton, N. Srivastava and K. Swersky, *Neural Networks for Machine Learning*, Lecture 6 slides (6e: rmsprop), hosted for University of Toronto CSC321. https://www.cs.toronto.edu/~bonner/courses/2016s/csc321/lectures/lec6.pdf (accessed 2026-11-19)
[^s2]: A. Zhang, Z. C. Lipton, M. Li and A. J. Smola, *Dive into Deep Learning*, §12.8 "RMSProp". https://d2l.ai/chapter_optimization/rmsprop.html (accessed 2026-11-19)
[^s3]: PyTorch, "torch.optim.RMSprop", PyTorch 2.3 documentation. https://docs.pytorch.org/docs/2.3/generated/torch.optim.RMSprop.html (accessed 2026-11-19)
[^s4]: A. Graves, "Generating Sequences With Recurrent Neural Networks", arXiv:1308.0850, 2013. https://ar5iv.labs.arxiv.org/html/1308.0850 (accessed 2026-11-19)
[^s5]: S. Ruder, "An overview of gradient descent optimization algorithms", arXiv:1609.04747, 2016. https://arxiv.org/pdf/1609.04747 (accessed 2026-11-19)
