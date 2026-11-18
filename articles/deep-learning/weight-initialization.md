---
id: kt:weight-initialization
type: Technique
title: Weight initialization
aliases: [parameter initialization, Xavier initialization, Glorot initialization, He initialization, Kaiming initialization]
domain: deep-learning
summary: >-
  The choice of starting values for a neural network's weights before training. Schemes such as Xavier/Glorot
  and He/Kaiming initialization draw random weights whose variance is scaled by layer width, so that activations
  and gradients keep a stable magnitude across many layers and symmetry between units is broken.
maturity: foundational
broader: [kt:deep-learning, kt:artificial-neural-network]
related: [kt:vanishing-gradient-problem, kt:activation-function, kt:batch-normalization, kt:residual-connection, kt:backpropagation]
relations:
  - {predicate: mitigates, object: kt:vanishing-gradient-problem}
  - {predicate: introducedIn, object: kt:understanding-the-difficulty-of-training-deep-feedforward-neural-networks}
  - {predicate: introducedIn, object: kt:delving-deep-into-rectifiers}
  - {predicate: dependsOn, object: kt:activation-function}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: usedIn, object: kt:stochastic-gradient-descent}
sources:
  - id: s1
    title: "Understanding the difficulty of training deep feedforward neural networks"
    publisher: Proceedings of AISTATS 2010, PMLR 9:249–256 (Glorot and Bengio)
    url: https://proceedings.mlr.press/v9/glorot10a.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification"
    publisher: ICCV 2015, pp. 1026–1034, CVF Open Access (He, Zhang, Ren and Sun)
    url: https://openaccess.thecvf.com/content_iccv_2015/html/He_Delving_Deep_into_ICCV_2015_paper
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "Delving Deep into Rectifiers (arXiv:1502.01852, HTML rendering)"
    publisher: arXiv / ar5iv (He, Zhang, Ren and Sun)
    url: https://ar5iv.labs.arxiv.org/html/1502.01852
    type: primary
    accessed: 2026-11-18
  - id: s4
    title: "Numerical Stability and Initialization"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), d2l.ai
    url: https://classic.d2l.ai/_sources/chapter_multilayer-perceptrons/numerical-stability-and-init.rst.txt
    type: textbook
    accessed: 2026-11-18
  - id: s5
    title: "torch.nn.init"
    publisher: PyTorch 2.3 documentation
    url: https://docs.pytorch.org/docs/2.3/nn.init.html
    type: official-docs
    accessed: 2026-11-18
  - id: s6
    title: "Exact solutions to the nonlinear dynamics of learning in deep linear neural networks"
    publisher: arXiv:1312.6120 (Saxe, McClelland and Ganguli, 2013–2014)
    url: https://arxiv.org/abs/1312.6120
    type: primary
    accessed: 2026-11-18
created: 2026-11-18
---

# Weight initialization

**Weight initialization** is the procedure that sets a neural network's parameters before the first gradient step. It looks like a detail, but in deep networks it decides whether training starts at all: the gradient reaching an early layer is a product of many layer-wise Jacobians, so weights that are slightly too small make that product shrink toward zero and weights slightly too large make it blow up. The *Dive into Deep Learning* textbook illustrates the danger by multiplying 100 random Gaussian matrices of unit variance, which yields entries on the order of 10^24.[^s4]

## Why initialization must be random

If every weight in a hidden layer starts at the same constant, every unit in that layer computes the same activation and receives the same gradient, so gradient descent keeps them identical and the layer behaves like a single unit. Drawing weights at random breaks this symmetry.[^s4] Biases, by contrast, are commonly set to zero; He et al. do exactly that in their rectifier networks.[^s3] Deep-learning frameworks ship a default random initializer that usually works for moderately sized models.[^s4]

## Xavier (Glorot) initialization

Xavier Glorot and Yoshua Bengio, at AISTATS 2010, studied why plain gradient descent from random starting weights trained deep feedforward networks so poorly. They found that the logistic sigmoid, because of its non-zero mean, could drive the top hidden layer into saturation, producing training plateaus. They also found that training gets harder when the singular values of each layer's Jacobian drift far from 1. From that analysis they proposed a normalized initialization that converged substantially faster.[^s1]

The usual derivation treats a layer as linear. With zero-mean, independent weights of variance σ², an output's variance is the input variance multiplied by n_in·σ², where n_in is the fan-in. Keeping the forward signal constant needs n_in·σ² = 1, while keeping the backward gradient constant needs n_out·σ² = 1. Both cannot hold unless the layer is square, so the scheme splits the difference with **σ² = 2 / (n_in + n_out)**. The uniform version samples from U(−a, a) with a = √(6 / (n_in + n_out)).[^s4] PyTorch implements both as `xavier_normal_` and `xavier_uniform_`, each with an optional gain factor.[^s5]

## He (Kaiming) initialization

The linear assumption fails for rectified linear units, which zero out roughly half their inputs and whose outputs are not zero-mean. Kaiming He and colleagues at Microsoft Research rederived the variance condition for rectifiers in their ICCV 2015 paper and arrived at (1/2)·n·Var[w] = 1 per layer, meaning zero-mean Gaussian weights with standard deviation **√(2/n)**, where n is the number of incoming connections.[^s3] They report that their initialization let a 30-layer rectifier model converge where Xavier initialization stalled, so very deep networks could be trained from scratch.[^s3][^s2] The same paper introduced the parametric ReLU and reported 4.94% top-5 error on ImageNet 2012. The authors described this as the first result to surpass the reported human-level figure of 5.1%.[^s2]

In PyTorch, `kaiming_normal_` and `kaiming_uniform_` scale by a nonlinearity-specific gain (√2 for ReLU, 5/3 for tanh). A `mode` argument chooses between preserving variance in the forward pass (`fan_in`, the default) and in the backward pass (`fan_out`).[^s5]

## Orthogonal and other schemes

Andrew Saxe, James McClelland and Surya Ganguli analysed learning dynamics in deep *linear* networks. They showed that random orthogonal starting weights can give learning times that do not grow with depth, much like unsupervised pretraining, and that gradients propagate faithfully in nonlinear networks operating near the "edge of chaos".[^s6] PyTorch exposes this as `orthogonal_`. It also provides a truncated normal initializer, which redraws samples outside a fixed interval. Its documentation notes that self-normalizing networks should use the linear gain, giving weights a variance of 1/N.[^s5]

## Limitations and practice

These schemes rest on simplifying assumptions: independent weights, linear or piecewise-linear units and stationary input statistics. Even so, they work well in practice despite the idealized derivation.[^s4] Today they are rarely the only safeguard. Normalization layers and residual connections also stabilize signal propagation, so initialization interacts with those choices rather than replacing them. A common default is to match the scheme to the activation: Xavier for tanh-like units, He for ReLU-family units.[^s5][^s3]

## Connections

Initialization is a direct remedy for the **vanishing-gradient problem**, attacking it at the starting point rather than through architecture.[^s4] Its formulas depend on the **activation function**, which is why He et al. had to revise the Xavier analysis for rectifiers.[^s3] It sits inside **deep learning** and applies to any **artificial neural network** trained by **backpropagation** and **stochastic gradient descent**.[^s1] **Batch normalization** and **residual connections** are complementary techniques that make networks less sensitive to the initial scale. **PyTorch** implements the standard schemes in `torch.nn.init`.[^s5]

## Sources
[^s1]: Glorot & Bengio, "Understanding the difficulty of training deep feedforward neural networks", AISTATS 2010, PMLR 9:249–256. https://proceedings.mlr.press/v9/glorot10a.html (accessed 2026-11-18)
[^s2]: He, Zhang, Ren & Sun, "Delving Deep into Rectifiers", ICCV 2015. https://openaccess.thecvf.com/content_iccv_2015/html/He_Delving_Deep_into_ICCV_2015_paper (accessed 2026-11-18)
[^s3]: He et al., "Delving Deep into Rectifiers", arXiv:1502.01852 (ar5iv). https://ar5iv.labs.arxiv.org/html/1502.01852 (accessed 2026-11-18)
[^s4]: Zhang, Lipton, Li & Smola, *Dive into Deep Learning*, "Numerical Stability and Initialization". https://classic.d2l.ai/_sources/chapter_multilayer-perceptrons/numerical-stability-and-init.rst.txt (accessed 2026-11-18)
[^s5]: PyTorch documentation, "torch.nn.init" (v2.3). https://docs.pytorch.org/docs/2.3/nn.init.html (accessed 2026-11-18)
[^s6]: Saxe, McClelland & Ganguli, "Exact solutions to the nonlinear dynamics of learning in deep linear neural networks", arXiv:1312.6120. https://arxiv.org/abs/1312.6120 (accessed 2026-11-18)
