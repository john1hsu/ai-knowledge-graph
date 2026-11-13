---
id: kt:activation-function
type: Concept
title: Activation function
aliases: [activation functions, nonlinearity, transfer function (neural networks), squashing function]
domain: deep-learning
summary: >-
  The elementwise nonlinear function a neural network applies to each unit's weighted input sum (for example
  sigmoid, tanh, ReLU, GELU or Swish); without it, any stack of layers collapses into a single linear map, so the
  choice of activation decides both what a network can represent and how easily gradients flow during training.
maturity: foundational
broader: [kt:artificial-neural-network, kt:deep-learning]
related: [kt:backpropagation, kt:vanishing-gradient-problem, kt:universal-approximation-theorem, kt:rectified-linear-unit, kt:gelu, kt:swiglu]
relations:
  - {predicate: partOf, object: kt:artificial-neural-network}
  - {predicate: influencedBy, object: kt:perceptron}
  - {predicate: partOf, object: kt:transformer-architecture}
sources:
  - id: s1
    title: "5.1. Multilayer Perceptrons (Dive into Deep Learning)"
    publisher: Zhang, Lipton, Li and Smola, Dive into Deep Learning (d2l.ai)
    url: https://d2l.ai/chapter_multilayer-perceptrons/mlp.html
    type: textbook
    accessed: 2026-11-13
  - id: s2
    title: "Rectified Linear Units Improve Restricted Boltzmann Machines"
    publisher: ICML 2010, pp. 807–814 (Nair and Hinton), via ML Anthology
    url: https://mlanthology.org/icml/2010/nair2010icml-rectified
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "Deep Sparse Rectifier Neural Networks"
    publisher: AISTATS 2011, PMLR 15:315–323 (Glorot, Bordes and Bengio)
    url: https://proceedings.mlr.press/v15/glorot11a.html
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "Gaussian Error Linear Units (GELUs)"
    publisher: arXiv:1606.08415 (Hendrycks and Gimpel, June 2016; v5 June 2023)
    url: https://arxiv.org/abs/1606.08415
    type: primary
    accessed: 2026-11-13
  - id: s5
    title: "Searching for Activation Functions"
    publisher: arXiv:1710.05941 (Ramachandran, Zoph and Le, October 2017)
    url: https://arxiv.org/abs/1710.05941v2
    type: primary
    accessed: 2026-11-13
  - id: s6
    title: "GLU Variants Improve Transformer"
    publisher: arXiv:2002.05202 (Shazeer, February 2020), ar5iv HTML rendering
    url: https://ar5iv.labs.arxiv.org/html/2002.05202
    type: primary
    accessed: 2026-11-13
  - id: s7
    title: "LLaMA: Open and Efficient Foundation Language Models"
    publisher: arXiv:2302.13971 (Touvron et al., Meta AI, February 2023), ar5iv HTML rendering
    url: https://ar5iv.labs.arxiv.org/html/2302.13971
    type: primary
    accessed: 2026-11-13
created: 2026-11-13
---

# Activation function

An activation function is the nonlinearity a neural network applies, unit by unit, to the weighted sum of a layer's inputs. Its first job is to prevent collapse: an affine map applied to another affine map is still affine, so a stack of purely linear layers is mathematically equivalent to a single linear model no matter how deep it is. Inserting a nonlinear function σ after each hidden layer breaks that equivalence and lets the network represent nonlinear relationships.[^s1]

## Classic choices: threshold, sigmoid and tanh

The earliest artificial neurons, following McCulloch and Pitts (1943), were hard threshold units. Once networks were trained by gradient-based methods, a smooth stand-in was needed, and the logistic sigmoid, 1/(1 + e^−x), filled that role. It squashes any input into (0, 1); its derivative is σ(x)(1 − σ(x)), which peaks at only 0.25 at zero and shrinks toward zero for large positive or negative inputs.[^s1] The hyperbolic tangent has the same S-shape but maps into (−1, 1) and is symmetric about the origin, with derivative 1 − tanh²(x) peaking at 1; the two are related by tanh(x) = 2·sigmoid(2x) − 1.[^s1] Glorot, Bordes and Bengio observed that although logistic units are more biologically plausible, tanh units train multilayer networks better.[^s3]

Saturation is the central weakness of both. When a unit's input is far from zero its gradient is nearly zero, and backpropagation multiplies such small factors across layers, producing the vanishing gradients and hard-to-escape plateaus that made deep sigmoid networks difficult to optimize.[^s1] Sigmoid survives today mainly at output units for binary classification.[^s1]

## The rectifier

The rectified linear unit, ReLU(x) = max(0, x), keeps positive inputs unchanged and zeroes negative ones. Its derivative is simply 1 for positive inputs and 0 for negative ones (by convention 0 at exactly zero, which almost never matters in practice), so gradients either pass through intact or are cut off, rather than being repeatedly shrunk.[^s1] Nair and Hinton introduced rectified units in restricted Boltzmann machines at ICML 2010, deriving them as an approximation to a sum of many sigmoid copies with shifted biases and showing better features for object recognition on NORB and face verification.[^s2] Glorot, Bordes and Bengio then showed at AISTATS 2011 that deep rectifier networks match or beat tanh networks despite the kink at zero, produce sparse representations with exact zeros, and reach their best supervised performance without unsupervised pretraining.[^s3] Dive into Deep Learning credits this ease of optimization as a key ingredient in the deep-learning resurgence.[^s1]

ReLU's own weakness is that units stuck in the negative region receive no gradient. Leaky and parametric variants such as pReLU, max(0, x) + α·min(0, x), let a small signal through for negative inputs.[^s1]

## Smooth gated activations

Later functions keep ReLU's near-linear behaviour for large positive inputs but are smooth and weight inputs by magnitude rather than gating purely on sign. Hendrycks and Gimpel's GELU (2016) is x·Φ(x), where Φ is the standard Gaussian CDF; they reported gains over ReLU and ELU across vision, language and speech tasks.[^s4] Ramachandran, Zoph and Le used exhaustive and reinforcement-learning-based search over candidate formulas and found Swish, x·sigmoid(βx); in their 2017 paper, swapping ReLU for Swish raised ImageNet top-1 accuracy by 0.9 points for Mobile NASNet-A and 0.6 points for Inception-ResNet-v2.[^s5]

Shazeer (2020) took a different route with gated linear units, which multiply one linear projection elementwise by an activated second projection, for example Swish(xW) ⊗ xV in SwiGLU. Used in a Transformer's feed-forward sublayer, with the hidden width cut to two-thirds to keep parameters constant, GEGLU and SwiGLU reached a held-out log-perplexity on C4 of about 1.63–1.64 versus 1.677 for ReLU, while plain GELU and Swish were no better than ReLU in that setup. Shazeer offered no theory for the gains, half-jokingly crediting "divine benevolence".[^s6]

## In practice

The activation is now usually chosen per layer role: sigmoid or softmax at outputs, ReLU-family functions as a cheap default in convolutional networks, and GELU or gated variants inside Transformer feed-forward blocks.[^s1][^s6] Meta's LLaMA models (February 2023), for instance, replaced ReLU with SwiGLU, citing Shazeer, and used a 2/3·4d hidden dimension.[^s7] Gains between modern activations are typically a fraction of a point and depend on architecture and training setup, so the empirical comparisons above should be read as reported by their authors rather than as universal rankings.[^s5][^s6]

## Connections

Activation functions are a component of every **artificial neural network** and a defining ingredient of **deep learning**, since depth only adds expressive power when layers are nonlinear.[^s1] Their derivatives are what **backpropagation** multiplies layer by layer, which ties the choice of function directly to the **vanishing gradient problem** that saturating sigmoids worsen and rectifiers ease.[^s1][^s3] The **universal approximation theorem** relies on a nonlinear activation, though representability says little about how easily a network learns.[^s1] Smooth threshold units descend from the **perceptron** era's step functions.[^s1] Specific members of the family, **rectified linear unit**, **GELU** and **SwiGLU**, are separate nodes, and gated variants are now standard in the feed-forward layers of the **Transformer architecture**.[^s2][^s4][^s6][^s7]

## Sources

[^s1]: Zhang, Lipton, Li and Smola, "5.1. Multilayer Perceptrons", Dive into Deep Learning. https://d2l.ai/chapter_multilayer-perceptrons/mlp.html (accessed 2026-11-13)
[^s2]: Nair and Hinton, "Rectified Linear Units Improve Restricted Boltzmann Machines", ICML 2010. https://mlanthology.org/icml/2010/nair2010icml-rectified (accessed 2026-11-13)
[^s3]: Glorot, Bordes and Bengio, "Deep Sparse Rectifier Neural Networks", AISTATS 2011, PMLR 15. https://proceedings.mlr.press/v15/glorot11a.html (accessed 2026-11-13)
[^s4]: Hendrycks and Gimpel, "Gaussian Error Linear Units (GELUs)", arXiv:1606.08415. https://arxiv.org/abs/1606.08415 (accessed 2026-11-13)
[^s5]: Ramachandran, Zoph and Le, "Searching for Activation Functions", arXiv:1710.05941. https://arxiv.org/abs/1710.05941v2 (accessed 2026-11-13)
[^s6]: Shazeer, "GLU Variants Improve Transformer", arXiv:2002.05202. https://ar5iv.labs.arxiv.org/html/2002.05202 (accessed 2026-11-13)
[^s7]: Touvron et al., "LLaMA: Open and Efficient Foundation Language Models", arXiv:2302.13971. https://ar5iv.labs.arxiv.org/html/2302.13971 (accessed 2026-11-13)
