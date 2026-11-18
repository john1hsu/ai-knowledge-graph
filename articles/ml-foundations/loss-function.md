---
id: kt:loss-function
type: Concept
title: Loss function
aliases: [cost function, objective function (training), error function, training loss]
domain: ml-foundations
summary: >-
  A function that scores how far a model's prediction is from the true target, returning a non-negative penalty
  that is zero for a perfect prediction; training chooses parameters that minimize its average over the data,
  as with squared error for regression or cross-entropy (log loss) for classification.
maturity: foundational
broader: [kt:machine-learning, kt:mathematical-optimization]
related: [kt:supervised-learning, kt:regularization, kt:statistical-learning-theory, kt:overfitting, kt:support-vector-machine, kt:logistic-regression]
relations:
  - {predicate: partOf, object: kt:empirical-risk-minimization}
  - {predicate: hasPart, object: kt:cross-entropy}
  - {predicate: usedIn, object: kt:gradient-descent}
  - {predicate: usedIn, object: kt:backpropagation}
  - {predicate: implementedIn, object: kt:pytorch}
sources:
  - id: s1
    title: "3.1. Linear Regression"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), d2l.ai
    url: https://d2l.ai/chapter_linear-regression/linear-regression.html
    type: textbook
    accessed: 2026-11-18
  - id: s2
    title: "3.4. Softmax Regression"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), classic.d2l.ai
    url: https://classic.d2l.ai/chapter_linear-networks/softmax-regression.html
    type: textbook
    accessed: 2026-11-18
  - id: s3
    title: "Lecture 10: Empirical Risk Minimization"
    publisher: Cornell University CS 4780/5780 Machine Learning for Intelligent Systems, course notes
    url: https://cs.cornell.edu/courses/cs4780/2022fa/lectures/lecturenote10.html
    type: academic
    accessed: 2026-11-18
  - id: s4
    title: "Convexity, Classification, and Risk Bounds (Technical Report 638)"
    publisher: Department of Statistics, UC Berkeley (Bartlett, Jordan and McAuliffe), 2003
    url: https://statistics.berkeley.edu/node/1593
    type: primary
    accessed: 2026-11-18
  - id: s5
    title: "Are Loss Functions All the Same?"
    publisher: Neural Computation 16, 2004 (Rosasco, De Vito, Caponnetto, Piana and Verri), via ML Anthology
    url: https://mlanthology.org/neco/2004/rosasco2004neco-loss
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s6
    title: "CrossEntropyLoss"
    publisher: PyTorch 2.12 documentation
    url: https://docs.pytorch.org/docs/2.12/generated/torch.nn.CrossEntropyLoss.html
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# Loss function

A **loss function** (also called a cost or error function) measures the gap between a model's prediction and the true target for a single example. By convention it is non-negative, smaller values are better, and a perfect prediction scores zero.[^s1] Training a model means choosing parameters that make the average loss over the training set as small as possible, so the loss function is the precise, mathematical statement of what "doing well" means for a learning algorithm.[^s1][^s3]

## How it works

**From per-example loss to an objective.** Given a per-example loss ℓ(ŷ, y), the quantity actually minimized is the mean of ℓ over the *n* training examples, often with a penalty on model complexity added. In the empirical risk minimization framing used in Cornell's CS 4780 notes, the objective is the average training loss plus λ times a regularizer r(w), where the loss penalizes training error and the regularizer penalizes complexity.[^s3] Because this objective is usually minimized with gradient-based methods, practitioners care about whether a loss is differentiable and convex, not only about what it measures.[^s1][^s3]

**Regression losses.** The default is squared error, ½(ŷ − y)², where the ½ is a convenience that cancels when differentiating.[^s1] Squared loss estimates the conditional mean and is differentiable everywhere, but because errors are squared, large residuals dominate; the d2l textbook calls this a double-edged sword that discourages big mistakes yet makes the fit sensitive to anomalous data.[^s1] Absolute loss estimates the median and is less sensitive to noise, but is not differentiable at zero. Huber loss is quadratic for small errors and linear for large ones, and log-cosh behaves similarly while being twice differentiable.[^s3]

**Classification losses.** The loss that actually matches the task, the zero-one loss (1 if wrong, 0 if right), is discontinuous and impractical to optimize directly, so learners minimize a smoother **surrogate**.[^s3] With labels y ∈ {−1, +1} and score h(x), common surrogates are the hinge loss max(0, 1 − y·h(x)) used by support vector machines, the log loss log(1 + e^(−y·h(x))) used by logistic regression, and the exponential loss used by AdaBoost, which grows so fast on mistakes that noisy labels can cause trouble.[^s3] For multi-class neural networks the standard choice is **cross-entropy**: the negative log of the probability the softmax assigns to the correct class. Its gradient with respect to each logit is simply the predicted probability minus the label, which makes it cheap to backpropagate.[^s2]

## Why the choice matters

A loss is not just a scoring rule; it encodes assumptions about the data. Minimizing squared error is equivalent to maximum likelihood estimation for a linear model with additive Gaussian noise, and minimizing cross-entropy is equivalent to maximizing the log-likelihood of the observed labels.[^s1][^s2] Read through information theory, cross-entropy is the expected surprisal of a model's predictions under the true label distribution, lowest when the two distributions match.[^s2] Choosing a loss therefore amounts to choosing a noise model, and a mismatched one (squared loss on heavy-tailed data, say) yields biased or brittle fits.[^s1][^s3]

Theory also constrains which surrogates are safe. Bartlett, Jordan and McAuliffe showed that for convex surrogates of the zero-one loss, excess classification risk can be bounded by excess surrogate risk under a pointwise form of Fisher consistency, so driving the surrogate down provably drives classification error down.[^s4] Rosasco and colleagues compared convex classification losses and concluded, other things equal, that hinge and logistic losses give nearly identical convergence rates, both much better than square loss, and they named hinge loss the loss of choice.[^s5] An open practical caveat is that the training loss is a proxy: a model can keep lowering it while held-out accuracy stalls, which is one face of overfitting and the reason regularization is added to the objective.[^s3]

## In practice

Deep learning frameworks package losses as modules. PyTorch's `CrossEntropyLoss`, for example, takes unnormalized logits and is equivalent to a log-softmax followed by negative log-likelihood; it supports per-class weights for imbalanced data, label smoothing toward a uniform distribution, an `ignore_index` for padded targets, and a `reduction` of mean, sum or none (as documented for PyTorch 2.12).[^s6]

## Connections

The loss is the inner term of **empirical risk minimization** and the quantity that **statistical learning theory** bounds; adding a **regularization** term to it is how the objective trades fit against complexity and guards against **overfitting**.[^s3] It defines the training signal in **supervised learning**, and it is what **gradient descent** minimizes and what **backpropagation** differentiates.[^s1] Specific losses tie it to specific models: hinge loss to the **support vector machine**, log loss to **logistic regression**, and **cross-entropy** to softmax classifiers and neural language models.[^s2][^s3] Its broader home is **mathematical optimization**, since every loss turns learning into an optimization problem, and frameworks such as **PyTorch** implement the common ones.[^s6]

## Sources
[^s1]: Zhang, Lipton, Li and Smola, "3.1. Linear Regression", *Dive into Deep Learning*. https://d2l.ai/chapter_linear-regression/linear-regression.html (accessed 2026-11-18)
[^s2]: Zhang, Lipton, Li and Smola, "3.4. Softmax Regression", *Dive into Deep Learning*. https://classic.d2l.ai/chapter_linear-networks/softmax-regression.html (accessed 2026-11-18)
[^s3]: Cornell CS 4780/5780, "Lecture 10: Empirical Risk Minimization", course notes. https://cs.cornell.edu/courses/cs4780/2022fa/lectures/lecturenote10.html (accessed 2026-11-18)
[^s4]: Bartlett, Jordan and McAuliffe, "Convexity, Classification, and Risk Bounds", UC Berkeley Statistics Technical Report 638, 2003. https://statistics.berkeley.edu/node/1593 (accessed 2026-11-18)
[^s5]: Rosasco, De Vito, Caponnetto, Piana and Verri, "Are Loss Functions All the Same?", *Neural Computation* 16, 2004. https://mlanthology.org/neco/2004/rosasco2004neco-loss (accessed 2026-11-18)
[^s6]: PyTorch, "CrossEntropyLoss", PyTorch 2.12 documentation. https://docs.pytorch.org/docs/2.12/generated/torch.nn.CrossEntropyLoss.html (accessed 2026-11-18)
