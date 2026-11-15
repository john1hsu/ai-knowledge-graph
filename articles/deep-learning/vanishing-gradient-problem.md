---
id: kt:vanishing-gradient-problem
type: Concept
title: Vanishing gradient problem
aliases: [vanishing gradients, vanishing and exploding gradients, exploding gradient problem]
domain: deep-learning
summary: >-
  The tendency of error gradients to shrink exponentially as backpropagation carries them through many
  layers or time steps, so that early layers of deep or recurrent networks learn very slowly or not at all;
  its mirror image, exploding gradients, makes updates blow up instead.
maturity: foundational
broader: [kt:backpropagation, kt:deep-learning]
related: [kt:recurrent-neural-network, kt:long-short-term-memory, kt:activation-function, kt:weight-initialization, kt:gradient-clipping]
relations:
  - {predicate: introducedIn, object: kt:learning-long-term-dependencies-with-gradient-descent-is-difficult}
sources:
  - id: s1
    title: "On the difficulty of training recurrent neural networks"
    publisher: ICML 2013, PMLR 28(3):1310–1318 (Pascanu, Mikolov and Bengio)
    url: https://proceedings.mlr.press/v28/pascanu13.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s2
    title: "On the difficulty of training Recurrent Neural Networks (arXiv 1211.5063, full text)"
    publisher: arXiv / ar5iv (Pascanu, Mikolov and Bengio)
    url: https://ar5iv.arxiv.org/html/1211.5063
    type: primary
    accessed: 2026-11-15
  - id: s3
    title: "Understanding the difficulty of training deep feedforward neural networks"
    publisher: AISTATS 2010, PMLR 9:249–256 (Glorot and Bengio)
    url: https://proceedings.mlr.press/v9/glorot10a.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "Dive into Deep Learning, §5.4 Numerical Stability and Initialization"
    publisher: d2l.ai (Zhang, Lipton, Li and Smola)
    url: https://d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html
    type: textbook
    accessed: 2026-11-15
  - id: s5
    title: "Deep Residual Learning for Image Recognition (arXiv 1512.03385v1, full text)"
    publisher: arXiv / ar5iv (He, Zhang, Ren and Sun, Microsoft Research)
    url: https://ar5iv.labs.arxiv.org/html/1512.03385v1
    type: primary
    accessed: 2026-11-15
created: 2026-11-15
---

# Vanishing gradient problem

The **vanishing gradient problem** is the observation that, when a network is trained by backpropagation, the gradient reaching early layers is a product of many per-layer factors, and that product can shrink toward zero as depth grows. Parameters far from the loss then receive updates too small to learn anything useful. The same product can also grow without bound, the **exploding gradient** problem; textbooks treat the two together as a question of numerical stability, since either one leaves updates too small to make progress or so large they wreck the model.[^s4] In recurrent networks the "depth" is the number of time steps, so vanishing gradients make it hard to learn dependencies between inputs that are far apart in a sequence.[^s1]

## Origin

Pascanu, Mikolov and Bengio credit Bengio, Simard and Frasconi's 1994 paper "Learning long-term dependencies with gradient descent is difficult" with the detailed description of both the vanishing and exploding gradient problems in recurrent networks; their own ICML 2013 paper generalised that single-unit analysis and examined it from analytical, geometric and dynamical-systems viewpoints.[^s1][^s2] For feedforward networks, Glorot and Bengio (AISTATS 2010) studied how activations and gradients change from layer to layer during training. They found that the logistic sigmoid, because of its non-zero mean, can drive top hidden layers into saturation, and that training appears harder when the singular values of each layer's Jacobian are far from 1.[^s3]

## How it works

By the chain rule, the gradient with respect to an early layer's weights is a product with one Jacobian matrix per later layer, times the gradient of the loss. Depending on the size of those matrices, the product either decays or explodes, roughly exponentially in depth.[^s4] Saturating activations make decay the usual outcome: the sigmoid's derivative is close to zero for large positive or negative inputs and never exceeds 1/4, so a long chain of sigmoid layers multiplies many small numbers together.[^s4][^s2] As a numerical illustration of the opposite case, *Dive into Deep Learning* multiplies 100 random 4×4 Gaussian matrices and obtains entries on the order of 10^23 or more, a scale at which gradient descent has no realistic chance of converging.[^s4]

For a recurrent network, Pascanu et al. split each gradient into "long-term" contributions (from time steps far in the past) and "short-term" ones. If γ bounds the derivative of the nonlinearity (1 for tanh, 1/4 for sigmoid) and the largest eigenvalue magnitude λ₁ of the recurrent weight matrix is below 1/γ, the long-term contributions are guaranteed to shrink exponentially with the time gap; λ₁ above 1/γ is necessary for them to explode.[^s2] The network can therefore still fit short-range structure while remaining blind to long-range structure.[^s1]

## Remedies

- **Initialization.** Glorot and Bengio proposed an initialization that keeps activation and gradient variances roughly constant across layers, reporting substantially faster convergence;[^s3] for Gaussian weights it uses variance 2/(n_in + n_out).[^s4]
- **Non-saturating activations.** ReLU's gradient does not decay for positive inputs, and *Dive into Deep Learning* notes it became the common default partly for this stability.[^s4]
- **Gradient clipping and regularisation.** For recurrent nets, Pascanu et al. rescale the gradient whenever its norm exceeds a threshold (for explosion) and add a soft constraint that discourages gradients from vanishing.[^s1][^s2]
- **Gated and shortcut architectures.** LSTM cells, which Pascanu et al. cite as a solution to vanishing gradients, keep a memory path along which error can flow;[^s2] residual connections give gradients an identity path through very deep stacks.[^s5]

## Limitations and current view

By 2015, He et al. described vanishing and exploding gradients as largely addressed by normalized initialization and intermediate normalization layers, which let networks with tens of layers start converging. They argued that the remaining obstacle to very deep plain networks, the *degradation* problem in which training error rises as layers are added, is a separate optimization difficulty: in their batch-normalized plain nets they checked that backward gradients had healthy norms.[^s5] The practical lesson is that "my deep network won't train" is not always a vanishing-gradient story; inspecting per-layer gradient norms distinguishes the cases.[^s5][^s4]

## Connections

The problem is a property of **backpropagation** applied to deep compositions, which is why it sits under both backpropagation and **deep learning**.[^s4] It is traced to (**introduced in**) Bengio, Simard and Frasconi's 1994 analysis of **recurrent neural networks**, and **long short-term memory** was designed in large part to get around it.[^s1][^s2] Choice of **activation function** and **weight initialization** are the first-line defences in feedforward networks;[^s3][^s4] **gradient clipping** handles the exploding side;[^s1] and **batch normalization** and **residual connections** are the architectural fixes that, together, made networks of a hundred or more layers routine.[^s5]

## Sources
[^s1]: Pascanu, Mikolov and Bengio, "On the difficulty of training recurrent neural networks", ICML 2013, PMLR 28(3):1310–1318. https://proceedings.mlr.press/v28/pascanu13.html (accessed 2026-11-15)
[^s2]: Pascanu, Mikolov and Bengio, "On the difficulty of training Recurrent Neural Networks", arXiv 1211.5063 (full text via ar5iv). https://ar5iv.arxiv.org/html/1211.5063 (accessed 2026-11-15)
[^s3]: Glorot and Bengio, "Understanding the difficulty of training deep feedforward neural networks", AISTATS 2010, PMLR 9:249–256. https://proceedings.mlr.press/v9/glorot10a.html (accessed 2026-11-15)
[^s4]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, §5.4 "Numerical Stability and Initialization". https://d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html (accessed 2026-11-15)
[^s5]: He, Zhang, Ren and Sun, "Deep Residual Learning for Image Recognition", arXiv 1512.03385v1 (full text via ar5iv). https://ar5iv.labs.arxiv.org/html/1512.03385v1 (accessed 2026-11-15)
