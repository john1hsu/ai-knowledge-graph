---
id: kt:backpropagation
type: Algorithm
title: Backpropagation algorithm
aliases: [backpropagation, backprop, back-propagation, backward propagation of errors, error backpropagation]
domain: deep-learning
summary: >-
  An algorithm that computes the gradient of a network's loss with respect to every parameter by applying the
  chain rule backward through the computation, from the output to the inputs, reusing values stored during the
  forward pass; it is the reverse mode of automatic differentiation specialised to neural networks.
maturity: foundational
broader: [kt:automatic-differentiation, kt:deep-learning]
related: [kt:artificial-neural-network, kt:gradient-descent, kt:activation-function, kt:policy-gradient]
relations:
  - {predicate: introducedIn, object: kt:learning-representations-by-back-propagating-errors}
  - {predicate: enables, object: kt:artificial-neural-network}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: contrastsWith, object: kt:perceptron}
sources:
  - id: s1
    title: "Learning representations by back-propagating errors"
    publisher: Nature 323, 533 (October 1986) (Rumelhart, Hinton and Williams), NASA ADS record
    url: https://ui.adsabs.harvard.edu/abs/1986Natur.323..533R/abstract
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s2
    title: "Who Invented the Reverse Mode of Differentiation?"
    publisher: Documenta Mathematica, Extra Volume ISMP (2012), 389–400 (Andreas Griewank)
    url: https://papers.baulab.info/papers/also/Griewank-2012.pdf
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s3
    title: "Forward Propagation, Backward Propagation, and Computational Graphs"
    publisher: Zhang, Lipton, Li and Smola, Dive into Deep Learning (d2l.ai), section 5.3
    url: https://d2l.ai/chapter_multilayer-perceptrons/backprop.html
    type: textbook
    accessed: 2026-10-31
  - id: s4
    title: "CS231n Section 2: Backpropagation"
    publisher: Stanford University, CS231n Deep Learning for Computer Vision, Spring 2026
    url: https://cs231n.stanford.edu/slides/2026/section_2_backprop.pdf
    type: academic
    accessed: 2026-10-31
  - id: s5
    title: "Autograd mechanics"
    publisher: PyTorch documentation
    url: https://docs.pytorch.org/docs/main/notes/autograd.html
    type: official-docs
    accessed: 2026-10-31
  - id: s6
    title: "Backpropagation and the brain"
    publisher: Nature Reviews Neuroscience 21, 335–346 (2020), doi:10.1038/s41583-020-0277-3 (Lillicrap, Santoro, Marris, Akerman and Hinton), University of Oxford record
    url: https://www.neuroscience.ox.ac.uk/publications/1100959
    type: peer-reviewed
    accessed: 2026-10-31
created: 2026-10-31
---

# Backpropagation algorithm

**Backpropagation** (backprop) is the procedure that computes how a neural network's loss changes with respect to each of its weights. It traverses the network in reverse, from the output layer back to the input, applying the chain rule so that each intermediate gradient is built from the one computed just before it.[^s3] Those gradients are then handed to an optimiser such as stochastic gradient descent, which updates the weights; training alternates forward passes, backward passes and updates.[^s3] Virtually every modern deep network, from image classifiers to large language models, is trained this way.

## Origin

Backpropagation was discovered several times. In his history of the method, Andreas Griewank credits Seppo Linnainmaa's 1970 master's thesis with the reverse mode of differentiation, though Linnainmaa used it to estimate how rounding errors propagate rather than to compute gradients; Griewank also notes reported earlier use by Gerardi Ostrowski in chemical-engineering models and later independent versions by Bennett, Speelpenning, Baur and Strassen, and Paul Werbos, whose 1982 work was motivated by neural networks.[^s2] The version that reshaped machine learning appeared in *Nature* in October 1986, when David Rumelhart, Geoffrey Hinton and Ronald Williams described a procedure that repeatedly adjusts connection weights to shrink the gap between actual and desired outputs.[^s1] Their key observation was that hidden units, which are neither inputs nor outputs, come to represent useful features of the task, an ability to create new features that set the method apart from the older perceptron-convergence procedure.[^s1]

## How it works

Consider a network with one hidden layer: z = W₁x, h = φ(z), o = W₂h, followed by a loss L. The **forward pass** computes and stores each intermediate value. The **backward pass** starts from ∂L/∂L = 1 and works toward the input: first the gradient for W₂, then ∂L/∂h, then ∂L/∂z (an element-wise product with φ′(z)), and finally the gradient for W₁.[^s3]

Viewed as a computational graph, every node only needs its own local derivative and the gradient arriving from above: the upstream gradient times the local gradient gives the gradient passed further down.[^s4] Simple patterns follow. An addition node passes the upstream gradient unchanged to all its inputs; a multiplication node gives each input the other input's value times the upstream gradient; a max node routes the whole gradient to the larger input, which is why ReLU blocks gradients wherever its input is non-positive; and when a value feeds several nodes, the gradients from each path are summed.[^s4] For f = (x + y)·z with x = −2, y = 5, z = −4, this gives ∂f/∂x = ∂f/∂y = −4 and ∂f/∂z = 3.[^s4] In matrix form, for Y = XW the gradients are Xᵀ(∂ℓ/∂Y) for W and (∂ℓ/∂Y)Wᵀ for X.[^s4]

The method's power comes from its cost. Griewank, citing Phil Wolfe, describes a "cheap gradient principle": evaluating a function together with its full gradient costs only a small, platform-dependent constant multiple of evaluating the function alone, rather than growing with the number of inputs as finite differencing would.[^s2] For a network with millions or billions of parameters, that difference is what makes gradient-based training feasible.

## Limitations

The speed is bought with memory. Because the backward pass reuses intermediate values from the forward pass, those values must be kept until backpropagation finishes, so training needs far more memory than prediction, and the requirement grows roughly with depth and batch size.[^s3] The cheap-gradient result also does not extend to full Jacobians, whose cost grows with the number of outputs.[^s2]

A second, long-running question is biological. Lillicrap, Hinton and colleagues note that backpropagation solves the credit-assignment problem in deep artificial networks but has long been regarded as implausible in the brain, since it is unclear how feedback connections in cortex could carry the precise error signals the algorithm requires. They propose that feedback might instead induce activity differences that locally approximate those errors.[^s6]

## In practice

Practitioners rarely write backward passes by hand. PyTorch's autograd, which its documentation describes as a reverse automatic differentiation system, records operations as a directed acyclic graph during the forward pass, saves the tensors the backward pass will need, and then traces from outputs to inputs applying the chain rule.[^s5] The graph is rebuilt on every iteration, so ordinary Python control flow can change the computation from step to step, and gradients accumulate into the `.grad` field of leaf tensors.[^s5]

## Connections

Backpropagation is an instance of **automatic differentiation** in reverse mode, the broader family Griewank traces back to the 1960s and 1970s,[^s2] and it is the workhorse of **deep learning**. It **enables** the training of multilayer **artificial neural networks** with hidden units, the capability that distinguished it from the single-layer **perceptron** rule.[^s1] It supplies gradients to **gradient descent**, depends on the derivatives of each **activation function**,[^s3][^s4] and is linked to **policy gradient** methods, which rely on it whenever the policy is a neural network. It was popularised in the 1986 paper **Learning representations by back-propagating errors**,[^s1] and is **implemented in** frameworks such as **PyTorch**.[^s5]

## Sources
[^s1]: Rumelhart, Hinton and Williams, "Learning representations by back-propagating errors", Nature 323, 533 (1986). https://ui.adsabs.harvard.edu/abs/1986Natur.323..533R/abstract (accessed 2026-10-31)
[^s2]: Griewank, "Who Invented the Reverse Mode of Differentiation?", Documenta Mathematica, Extra Volume ISMP (2012), 389–400. https://papers.baulab.info/papers/also/Griewank-2012.pdf (accessed 2026-10-31)
[^s3]: Zhang et al., "Forward Propagation, Backward Propagation, and Computational Graphs", Dive into Deep Learning. https://d2l.ai/chapter_multilayer-perceptrons/backprop.html (accessed 2026-10-31)
[^s4]: Stanford CS231n, "Section 2: Backpropagation", Spring 2026. https://cs231n.stanford.edu/slides/2026/section_2_backprop.pdf (accessed 2026-10-31)
[^s5]: PyTorch documentation, "Autograd mechanics". https://docs.pytorch.org/docs/main/notes/autograd.html (accessed 2026-10-31)
[^s6]: Lillicrap, Santoro, Marris, Akerman and Hinton, "Backpropagation and the brain", Nature Reviews Neuroscience 21, 335–346 (2020). https://www.neuroscience.ox.ac.uk/publications/1100959 (accessed 2026-10-31)
