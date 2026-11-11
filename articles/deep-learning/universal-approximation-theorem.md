---
id: kt:universal-approximation-theorem
type: Concept
title: Universal approximation theorem
aliases: [universal approximation property, Cybenko's theorem, neural network universality]
domain: deep-learning
summary: >-
  A family of mathematical results showing that feedforward neural networks with a suitable nonlinear activation
  can approximate any continuous function on a compact domain to arbitrary accuracy, given enough hidden units;
  it guarantees expressive power but says nothing about how large the network must be or whether training will
  find the approximating weights.
maturity: foundational
broader: [kt:artificial-neural-network, kt:deep-learning]
related: [kt:perceptron, kt:activation-function, kt:curse-of-dimensionality, kt:backpropagation, kt:bias-variance-tradeoff]
relations:
  - {predicate: introducedIn, object: kt:approximation-by-superpositions-of-a-sigmoidal-function}
  - {predicate: createdBy, object: kt:george-cybenko}
  - {predicate: dependsOn, object: kt:activation-function}
  - {predicate: extends, object: kt:stone-weierstrass-theorem}
sources:
  - id: s1
    title: "Approximation by Superpositions of a Sigmoidal Function"
    publisher: Mathematics of Control, Signals, and Systems 2, 303–314 (1989) (G. Cybenko); PDF hosted by the Bau Lab paper archive
    url: https://papers.baulab.info/papers/Cybenko-1989.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "Multilayer Feedforward Networks With a Nonpolynomial Activation Function Can Approximate Any Function"
    publisher: Neural Networks 6, 861–867 (1993) (Leshno, Lin, Pinkus and Schocken); author copy on Allan Pinkus's Technion site
    url: https://pinkus.net.technion.ac.il/files/2021/02/neural.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "Universal Approximation Bounds for Superpositions of a Sigmoidal Function"
    publisher: IEEE Transactions on Information Theory 39(3), 930–945 (1993) (A. R. Barron); PDF hosted by EPFL
    url: https://documents.epfl.ch/groups/i/ip/ipg/www/2015-2016/Reading%20Group%20on%20Deep%20Neural%20Nets/UniversalApproximationBoundsForSuperpositionsOfASigmoidalFunction.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "The Expressive Power of Neural Networks: A View from the Width"
    publisher: NeurIPS 2017 (Lu, Pu, Wang, Hu and Wang)
    url: https://papers.NeurIPS.cc/paper_files/paper/2017/file/32cbf687880eb1674a07bf717761dd3a-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "Lecture 9: Universal Approximation (CPSC 532D, Fall 2025)"
    publisher: University of British Columbia (Danica J. Sutherland)
    url: https://www.cs.ubc.ca/~dsuth/532D/25w1/notes/9-universal.pdf
    type: academic
    accessed: 2026-11-11
created: 2026-11-11
---

# Universal approximation theorem

The **universal approximation theorem** is the name usually given to a cluster of results, proved independently around 1989, stating that a neural network with a single hidden layer of nonlinear units can approximate any continuous function on a bounded, closed region as closely as desired. The best-known version is George Cybenko's: finite sums of the form G(x) = Σ αⱼ σ(yⱼᵀx + θⱼ), where σ is any continuous sigmoidal function (tending to 0 at −∞ and to 1 at +∞), are dense in the continuous functions on the unit cube under the supremum norm.[^s1] Kurt Hornik, Maxwell Stinchcombe and Halbert White published a closely related result the same year for networks with arbitrary squashing functions, and later work by Hornik and others relaxed the conditions further.[^s2] The theorem is the standard formal answer to the question of why neural networks are a reasonable hypothesis class: in principle, they can represent essentially any input–output mapping.[^s5]

## What the theorem says

Cybenko's proof is non-constructive. It shows that if the closure of the set of such sums were not all of C(Iₙ), the Hahn–Banach and Riesz representation theorems would yield a nonzero measure annihilating every hidden unit, which a "discriminatory" activation rules out; he then shows every bounded measurable sigmoidal function is discriminatory.[^s1] The same paper extends the result to classification, showing a one-hidden-layer network can match any finite decision partition except on a set of arbitrarily small measure, and notes analogous density results in L¹ and for sine, cosine and exponential activations.[^s1]

The sharpest general characterization came from Moshe Leshno, Vladimir Lin, Allan Pinkus and Shimon Schocken in 1993: for a locally bounded, piecewise-continuous activation, single-hidden-layer networks approximate every continuous function on compact sets **if and only if the activation is not a polynomial**.[^s2] The activation need not be continuous, smooth, bounded or monotone, so the result covers the rectified linear unit (ReLU) used in most modern networks. The authors also show the bias (threshold) term matters: without it, networks built from sin(x) produce only odd functions and cannot approximate cos(x).[^s2] A course treatment frames the polynomial exclusion through the Stone–Weierstrass theorem, which gives density for any algebra of continuous functions that separates points and contains constants.[^s5]

## What it does not say

The classical theorems are existence results. Cybenko states the result holds only if no limit is placed on the number of hidden units or the size of the weights, and he speculates that many practical problems might need "astronomical numbers of terms."[^s1] Leshno et al. likewise give no bound on the number of units or on the rate of approximation.[^s2] Lecture notes on the topic stress three further gaps:[^s5]

- **Size:** approximating arbitrary continuous functions on a d-dimensional cube needs a number of units growing exponentially in d, an instance of the curse of dimensionality.[^s5]
- **Optimization:** training is non-convex, and even fitting a single ReLU unit under squared loss is NP-hard, so gradient descent is not guaranteed to find the approximating weights.[^s5]
- **Generalization:** a class rich enough to be universal can shatter any finite set, so it has infinite VC dimension and is not PAC-learnable without further restrictions such as structural risk minimization.[^s5]

## Rates and the role of width and depth

Andrew Barron's 1993 paper turned existence into a rate. For target functions whose Fourier transform has a finite first moment C_f, a one-hidden-layer sigmoidal network with n units achieves integrated squared error of order C_f²/n, a rate that does not depend on the input dimension, whereas any linear combination of n *fixed* basis functions suffers a worst-case error of order (1/n)^(2/d).[^s3] Barron cautions that C_f itself can grow with dimension for some function classes, so the advantage is not unconditional.[^s3]

The classical theorems bound depth (one hidden layer) and let width grow without limit. Zhou Lu and colleagues proved a dual result at NeurIPS 2017: ReLU networks whose width is at most n + 4, for input dimension n, are universal approximators of Lebesgue-integrable functions in L¹ distance when depth is allowed to grow, while networks of width at most n generally are not, a phase transition in width.[^s4] They also exhibit wide, shallow networks that narrower networks cannot approximate without polynomially more size, complementing earlier results on the efficiency of depth.[^s4]

## Connections

The theorem is a property of the **artificial neural network** model and supplies part of the theoretical motivation for **deep learning**. It concerns networks with at least one hidden nonlinear layer, the ingredient missing from the single-layer **perceptron**; the theorem's network form is a weighted sum of such hidden units.[^s1] Its validity **depends on** the choice of **activation function**, which must be non-polynomial.[^s2] It **extends** the logic of the Stone–Weierstrass theorem to sums of ridge functions.[^s5] Its exponential worst-case size links it to the **curse of dimensionality**, which Barron's dimension-free rate partially escapes for smooth targets.[^s3] Because it is silent on learning, it is complemented by **backpropagation**, the algorithm used to search for good weights, and by the **bias–variance tradeoff**, which governs whether a highly expressive model generalizes.[^s5] The result was **introduced in** Cybenko's 1989 paper, **created by** George Cybenko alongside the parallel work of Hornik, Stinchcombe and White.[^s1][^s2]

## Sources
[^s1]: G. Cybenko, "Approximation by Superpositions of a Sigmoidal Function", Mathematics of Control, Signals, and Systems 2, 303–314 (1989). https://papers.baulab.info/papers/Cybenko-1989.pdf (accessed 2026-11-11)
[^s2]: M. Leshno, V. Ya. Lin, A. Pinkus and S. Schocken, "Multilayer Feedforward Networks With a Nonpolynomial Activation Function Can Approximate Any Function", Neural Networks 6, 861–867 (1993). https://pinkus.net.technion.ac.il/files/2021/02/neural.pdf (accessed 2026-11-11)
[^s3]: A. R. Barron, "Universal Approximation Bounds for Superpositions of a Sigmoidal Function", IEEE Transactions on Information Theory 39(3), 930–945 (1993). https://documents.epfl.ch/groups/i/ip/ipg/www/2015-2016/Reading%20Group%20on%20Deep%20Neural%20Nets/UniversalApproximationBoundsForSuperpositionsOfASigmoidalFunction.pdf (accessed 2026-11-11)
[^s4]: Z. Lu, H. Pu, F. Wang, Z. Hu and L. Wang, "The Expressive Power of Neural Networks: A View from the Width", NeurIPS 2017. https://papers.NeurIPS.cc/paper_files/paper/2017/file/32cbf687880eb1674a07bf717761dd3a-Paper.pdf (accessed 2026-11-11)
[^s5]: D. J. Sutherland, "Lecture 9: Universal Approximation", CPSC 532D, University of British Columbia, Fall 2025. https://www.cs.ubc.ca/~dsuth/532D/25w1/notes/9-universal.pdf (accessed 2026-11-11)
