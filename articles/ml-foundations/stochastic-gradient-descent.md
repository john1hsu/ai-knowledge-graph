---
id: kt:stochastic-gradient-descent
type: Algorithm
title: Stochastic gradient descent
aliases: [SGD, stochastic gradient method, minibatch stochastic gradient descent, mini-batch SGD, minibatch SGD]
domain: ml-foundations
summary: >-
  An iterative optimization method that updates model parameters using a gradient estimated from one randomly chosen
  training example or a small random minibatch rather than the whole dataset, trading noisy steps for a per-step cost
  that does not grow with dataset size; with its momentum and adaptive descendants it is the standard way to train
  neural networks.
maturity: foundational
broader: [kt:gradient-descent, kt:mathematical-optimization]
related: [kt:backpropagation, kt:adam-optimizer, kt:adagrad, kt:data-parallelism, kt:batch-normalization, kt:overfitting]
relations:
  - {predicate: basedOn, object: kt:stochastic-approximation}
  - {predicate: introducedIn, object: kt:a-stochastic-approximation-method}
  - {predicate: dependsOn, object: kt:loss-function}
  - {predicate: hasPart, object: kt:momentum}
  - {predicate: usedIn, object: kt:deep-learning}
sources:
  - id: s1
    title: "12.4. Stochastic Gradient Descent"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), d2l.ai
    url: https://d2l.ai/chapter_optimization/sgd.html
    type: textbook
    accessed: 2026-11-17
  - id: s2
    title: "12.5. Minibatch Stochastic Gradient Descent"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), d2l.ai
    url: https://d2l.ai/chapter_optimization/minibatch-sgd.html
    type: textbook
    accessed: 2026-11-17
  - id: s3
    title: "Optimization Methods for Large-Scale Machine Learning"
    publisher: SIAM Review 60(2), 223–311 (2018) (Bottou, Curtis and Nocedal); authors' copy hosted at leon.bottou.org
    url: https://leon.bottou.org/publications/pdf/sirev-2018.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "Large-Scale Machine Learning with Stochastic Gradient Descent"
    publisher: Proceedings of COMPSTAT'2010, Springer, pp. 177–187 (Bottou); author's paper page
    url: https://leon.bottou.org/papers/bottou-2010
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "On the importance of initialization and momentum in deep learning"
    publisher: Proceedings of the 30th ICML, PMLR 28(3), 1139–1147 (2013) (Sutskever, Martens, Dahl and Hinton)
    url: https://proceedings.mlr.press/v28/sutskever13.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s6
    title: "On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima"
    publisher: Keskar, Mudigere, Nocedal, Smelyanskiy and Tang, arXiv:1609.04836 (ICLR 2017)
    url: https://arxiv.org/abs/1609.04836v2
    type: primary
    accessed: 2026-11-17
created: 2026-11-17
---

# Stochastic gradient descent

Stochastic gradient descent (SGD) minimizes a training objective written as an average of per-example losses, f(x) = (1/n) Σᵢ fᵢ(x), without ever computing the full gradient. At each step it draws an index i at random and applies x ← x − η∇fᵢ(x), where η is the learning rate. Because the expected value of ∇fᵢ(x) over a uniformly random i equals ∇f(x), each step follows the true gradient on average, while costing O(1) per iteration instead of the O(n) a full-batch step requires.[^s1] Bottou, Curtis and Nocedal trace the method to the stochastic approximation scheme of Robbins and Monro and treat it as the central algorithm of large-scale machine learning.[^s3]

## Why it works at scale

Three arguments explain SGD's dominance. Real datasets contain much exact or approximate redundancy, so a full-batch method spends most of its work re-reading near-duplicate information; SGD's per-step cost is independent of n; and in practice it makes far faster early progress, as in a logistic-regression experiment on RCV1 where it outpaced batch L-BFGS per data access.[^s3] Bottou's COMPSTAT 2010 paper framed this as a change of regime: once data grows faster than compute, learning is limited by computing time rather than sample size, the optimizer's cost enters the error trade-off, and simple stochastic methods win on large problems.[^s4] The same paper reports that averaged SGD and second-order SGD become asymptotically efficient after a single pass over the training data.[^s4]

## Convergence and learning-rate schedules

The noise that makes steps cheap also stops plain SGD from settling. For a strongly convex objective, a fixed step size gives fast initial contraction but only to a neighborhood of the optimum whose size grows with the step; diminishing steps that satisfy the Robbins–Monro conditions (Σαₖ = ∞, Σαₖ² < ∞) converge at a sublinear O(1/k) rate. Batch gradient descent converges linearly, but its total work to reach accuracy ε scales like n log(1/ε), whereas SGD's scales like 1/ε, independent of n, which favors SGD when data is large.[^s3] For general convex problems with bounded gradients the averaged iterate converges at O(1/√T); d2l.ai notes that such guarantees do not carry over to nonconvex deep networks.[^s1]

Schedules therefore matter. The d2l.ai textbook compares piecewise-constant, exponential and polynomial decay. On a noisy two-dimensional quadratic, a constant rate keeps the iterates wandering, exponential decay shrinks the variance so quickly that progress stalls short of the optimum, and polynomial decay of the form η₀(1 + βt)^(−0.5) converges noticeably better within 50 steps.[^s1] The book also recommends sampling without replacement, shuffling the data each epoch, because sampling with replacement reaches only about 63% of examples per pass and adds variance.[^s1]

## Minibatches

Modern practice almost always uses minibatches: each step averages gradients over b examples. The expectation is unchanged, but the standard deviation of the estimate falls by a factor of b^(−1/2), and batching lets GPUs and CPUs use vectorized matrix operations.[^s2] On d2l.ai's airfoil-noise regression (1,500 examples, PyTorch run), single-example SGD took about 0.69 s per epoch while minibatches of 100 took about 0.025 s and reached a similar loss, slightly faster per epoch than full-batch gradient descent.[^s2] Returns diminish as b grows, so batch size is usually set by memory and hardware efficiency.[^s2]

Bigger is not free. Keskar et al. found that large-batch training tends to converge to sharp minimizers that generalize worse, while small batches of roughly 32 to 512 examples consistently reach flatter ones; they attribute the difference to the inherent noise of small-batch gradient estimates.[^s6] SGD's noise is thus part of how it regularizes, not only a cost.

## Momentum and descendants

Momentum accumulates a running velocity of past gradients to damp oscillation across ill-conditioned directions. Sutskever, Martens, Dahl and Hinton showed in 2013 that SGD with momentum, combined with good random initialization and a slowly increasing momentum schedule, could train deep and recurrent networks to levels previously reached only with Hessian-free second-order optimization, and that both ingredients were essential.[^s5] Adaptive methods such as AdaGrad and Adam keep the stochastic minibatch gradient but rescale it per parameter.[^s3]

## Connections

SGD is the stochastic form of **gradient descent** and a method of **mathematical optimization** (broader).[^s1] It is *based on* **stochastic approximation**, *introduced in* Robbins and Monro's "A Stochastic Approximation Method",[^s3] and minimizes a **loss function** (*dependsOn*). In neural networks the per-batch gradient comes from **backpropagation**, which is why SGD is *used in* **deep learning**.[^s5] **Momentum** is a standard component (*hasPart*),[^s5] and **AdaGrad** and the **Adam optimizer** extend it with per-parameter step sizes.[^s3] **Data parallelism** distributes each minibatch across devices, and **batch normalization** computes statistics per minibatch.[^s2] Its gradient noise links it to **overfitting** and generalization through the sharp-versus-flat-minima findings.[^s6]

## Sources
[^s1]: Zhang, Lipton, Li and Smola, "12.4. Stochastic Gradient Descent", *Dive into Deep Learning*. https://d2l.ai/chapter_optimization/sgd.html (accessed 2026-11-17)
[^s2]: Zhang, Lipton, Li and Smola, "12.5. Minibatch Stochastic Gradient Descent", *Dive into Deep Learning*. https://d2l.ai/chapter_optimization/minibatch-sgd.html (accessed 2026-11-17)
[^s3]: Bottou, Curtis and Nocedal, "Optimization Methods for Large-Scale Machine Learning", *SIAM Review* 60(2), 223–311, 2018. https://leon.bottou.org/publications/pdf/sirev-2018.pdf (accessed 2026-11-17)
[^s4]: Bottou, "Large-Scale Machine Learning with Stochastic Gradient Descent", *Proceedings of COMPSTAT'2010*, Springer, 177–187. https://leon.bottou.org/papers/bottou-2010 (accessed 2026-11-17)
[^s5]: Sutskever, Martens, Dahl and Hinton, "On the importance of initialization and momentum in deep learning", ICML 2013, PMLR 28(3), 1139–1147. https://proceedings.mlr.press/v28/sutskever13.html (accessed 2026-11-17)
[^s6]: Keskar, Mudigere, Nocedal, Smelyanskiy and Tang, "On Large-Batch Training for Deep Learning: Generalization Gap and Sharp Minima", arXiv:1609.04836 (ICLR 2017). https://arxiv.org/abs/1609.04836v2 (accessed 2026-11-17)
