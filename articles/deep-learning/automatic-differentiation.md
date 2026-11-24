---
id: kt:automatic-differentiation
type: Technique
title: Automatic differentiation
aliases: [autodiff, algorithmic differentiation, AD, autograd]
domain: deep-learning
summary: >-
  A family of techniques that computes exact derivatives of functions written as computer programs by
  decomposing them into elementary operations and applying the chain rule to each, in forward mode
  (Jacobian-vector products) or reverse mode (vector-Jacobian products); reverse mode underlies the
  gradient computation of every major deep learning framework.
maturity: foundational
broader: [kt:numerical-analysis, kt:mathematical-optimization]
related: [kt:backpropagation, kt:gradient-descent, kt:activation-checkpointing, kt:pytorch]
relations:
  - {predicate: introducedIn, object: kt:a-simple-automatic-derivative-evaluation-program}
  - {predicate: enables, object: kt:backpropagation}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: implementedIn, object: kt:jax}
  - {predicate: contrastsWith, object: kt:numerical-differentiation}
  - {predicate: contrastsWith, object: kt:symbolic-differentiation}
sources:
  - id: s1
    title: "Automatic Differentiation in Machine Learning: a Survey"
    publisher: Journal of Machine Learning Research 18(153):1-43, 2018 (Baydin, Pearlmutter, Radul and Siskind)
    url: https://jmlr.org/papers/v18/17-468.html
    type: peer-reviewed
    accessed: 2026-11-24
  - id: s2
    title: "Automatic Differentiation in Machine Learning: a Survey (arXiv v4, full text)"
    publisher: arXiv 1502.05767 (authors' version of the JMLR paper, February 2018)
    url: https://arxiv.org/pdf/1502.05767
    type: primary
    accessed: 2026-11-24
  - id: s3
    title: "A Simple Automatic Derivative Evaluation Program"
    publisher: Communications of the ACM 7(8):463-464, August 1964 (R. E. Wengert), Princeton COS 597C course copy
    url: https://www.cs.princeton.edu/courses/archive/fall19/cos597C/files/wengert1964.pdf
    type: peer-reviewed
    accessed: 2026-11-24
  - id: s4
    title: "2.5. Automatic Differentiation"
    publisher: Zhang, Lipton, Li and Smola, Dive into Deep Learning (d2l.ai)
    url: https://d2l.ai/chapter_preliminaries/autograd.html
    type: textbook
    accessed: 2026-11-24
  - id: s5
    title: "The Autodiff Cookbook"
    publisher: JAX documentation (archived version of the cookbook)
    url: https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html
    type: official-docs
    accessed: 2026-11-24
created: 2026-11-24
---

# Automatic differentiation

**Automatic differentiation** (AD, autodiff, or algorithmic differentiation) evaluates the derivatives of a numeric function that is expressed as a program, rather than as a closed-form formula. Baydin, Pearlmutter, Radul and Siskind's 2018 survey in the *Journal of Machine Learning Research* describes it as a family of techniques akin to backpropagation but more general, and stresses that it is neither numerical nor symbolic differentiation.[^s1] Because gradients and Hessians are needed throughout machine learning, AD is the machinery that lets practitioners write a loss in ordinary code and receive its gradient for free.[^s1][^s4]

## How it differs from other ways to differentiate

Finite differences approximate a gradient by perturbing each of the *n* inputs in turn, so they need on the order of *n* function evaluations and suffer from both round-off and truncation error. Symbolic differentiation manipulates expressions and tends to produce bloated, deeply nested results, a problem the survey calls *expression swell*. AD instead records the program as a sequence of elementary operations (an evaluation trace, sometimes called a Wengert list) and applies the chain rule to each operation numerically. The result is exact to machine precision, costs only a small constant factor more than evaluating the function, and works through loops, branches and recursion.[^s2]

## Forward and reverse mode

In **forward mode**, every intermediate value carries a tangent alongside it. Seeding one input's tangent with 1 and the rest with 0 yields one column of the Jacobian per pass, so a function from R^n to R^m needs *n* passes for the full Jacobian; one pass computes a Jacobian-vector product. Dual numbers of the form v + v'ε with ε² = 0 give a compact algebraic view of the same idea.[^s2] JAX exposes this as `jvp` and builds `jacfwd` from it.[^s5]

In **reverse mode**, a forward sweep evaluates the program and records its dependencies, then a backward sweep propagates *adjoints* (sensitivities of an output to each intermediate) from the output to the inputs. One reverse pass yields a full row of the Jacobian, so the gradient of a scalar loss over millions of parameters costs a single backward pass. Citing Griewank and Walther, the survey gives Jacobian costs of roughly n·c·ops(f) for forward mode and m·c·ops(f) for reverse mode, with c below 6 and typically between 2 and 3; reverse mode therefore wins when outputs are fewer than inputs.[^s2] In its benchmark, the reverse-mode gradient took about twice the time of the function itself regardless of input dimension, while forward-mode cost grew with the number of inputs.[^s2]

The price of reverse mode is memory: the stored trace can grow, in the worst case, in proportion to the number of operations, which is why checkpointing schemes trade recomputation for storage.[^s2] The JAX documentation likewise notes that the shape of the Jacobian decides which mode is cheaper, recommending `jacrev` for wide Jacobians, `jacfwd` for tall ones, and forward-over-reverse composition for Hessians.[^s5]

## History

The survey traces AD ideas to the 1950s. R. E. Wengert of General Electric published a short program in *Communications of the ACM* in August 1964 that split a function into intermediate variables, evaluated each one's value and derivative with a small subroutine library, and obtained partial derivatives as a by-product of function evaluation, one run per input variable; this is forward accumulation.[^s3][^s2] Reverse mode has roots in optimal control and in Seppo Linnainmaa's 1970 and 1976 work, often cited as its first published description, while Bert Speelpenning's 1980 implementation is credited with reverse-mode AD in its modern automatic form.[^s2] The neural-network backpropagation popularised by Rumelhart, Hinton and Williams in 1986 is, in the survey's framing, essentially reverse-mode AD applied to a network composed with its loss.[^s2]

## In practice

Implementations follow two broad strategies: **operator overloading**, where tensor types record operations at run time, and **source code transformation**, where a tool rewrites the program to emit derivative code.[^s2] Deep learning frameworks mostly use the first. *Dive into Deep Learning* shows the pattern in PyTorch, TensorFlow, MXNet and JAX: mark tensors as requiring gradients, run the forward computation to build a graph, then call a backward routine. It also covers practical details such as PyTorch accumulating gradients until they are zeroed, needing a seed vector when the output is not a scalar, detaching tensors to block gradient flow, and differentiating through data-dependent Python control flow, which works because each call builds a fresh graph for that input.[^s4] JAX instead offers composable function transformations (`grad`, `jvp`, `vjp`, `jacfwd`, `jacrev`, `hessian`) that can be nested to obtain higher-order derivatives.[^s5]

The main practical limit is the memory growth of reverse mode on very deep or long computations; the JAX cookbook also shows how Hessian-vector products can be computed without ever materialising the full Hessian, which matters for second-order methods on large models.[^s2][^s5]

## Connections

AD is the general technique of which **backpropagation** is the special case used to train neural networks, and it supplies the gradients consumed by **gradient descent** and other methods of **mathematical optimization**.[^s2] Its reverse-mode memory cost motivates **activation checkpointing**, which stores only some intermediates and recomputes the rest.[^s2] It is the core engine of frameworks such as **PyTorch** and **JAX**.[^s4][^s5] It contrasts with **numerical differentiation** (approximate, O(n) evaluations) and **symbolic differentiation** (exact but prone to expression swell), and it sits within **numerical analysis** as a computational method; Wengert's 1964 paper is recorded as an early introduction of the forward mode.[^s2][^s3]

## Sources

[^s1]: Baydin, Pearlmutter, Radul and Siskind, "Automatic Differentiation in Machine Learning: a Survey", JMLR 18(153):1-43, 2018. https://jmlr.org/papers/v18/17-468.html (accessed 2026-11-24)
[^s2]: Baydin et al., authors' arXiv version (v4) of the same survey. https://arxiv.org/pdf/1502.05767 (accessed 2026-11-24)
[^s3]: R. E. Wengert, "A Simple Automatic Derivative Evaluation Program", Communications of the ACM 7(8):463-464, 1964. https://www.cs.princeton.edu/courses/archive/fall19/cos597C/files/wengert1964.pdf (accessed 2026-11-24)
[^s4]: Zhang, Lipton, Li and Smola, "2.5. Automatic Differentiation", Dive into Deep Learning. https://d2l.ai/chapter_preliminaries/autograd.html (accessed 2026-11-24)
[^s5]: JAX documentation, "The Autodiff Cookbook". https://docs.jax.dev/en/latest/notebooks/autodiff_cookbook.html (accessed 2026-11-24)
