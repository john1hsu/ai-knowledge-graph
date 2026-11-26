---
id: kt:empirical-risk-minimization
type: Concept
title: Empirical risk minimization
aliases: [ERM, ERM principle, empirical risk minimisation]
domain: ml-foundations
summary: >-
  The learning principle that, because the expected loss over the true data distribution cannot be computed,
  chooses the hypothesis that minimizes the average loss on the training sample instead; it underlies least
  squares, logistic regression, SVMs and neural-network training, and its success depends on controlling the
  capacity of the hypothesis class.
maturity: foundational
broader: [kt:statistical-learning-theory, kt:supervised-learning]
related: [kt:loss-function, kt:regularization, kt:overfitting, kt:mathematical-optimization, kt:bias-variance-tradeoff, kt:double-descent]
relations:
  - {predicate: createdBy, object: kt:vladimir-vapnik}
  - {predicate: hasPart, object: kt:loss-function}
  - {predicate: dependsOn, object: kt:vc-dimension}
  - {predicate: enables, object: kt:structural-risk-minimization}
  - {predicate: alternativeTo, object: kt:mixup}
  - {predicate: usedIn, object: kt:support-vector-machine}
  - {predicate: usedIn, object: kt:logistic-regression}
sources:
  - id: s1
    title: "Principles of Risk Minimization for Learning Theory"
    publisher: Advances in Neural Information Processing Systems 4 (NIPS 1991) (V. Vapnik)
    url: https://proceedings.neurips.cc/paper/1991/hash/ff4d5fbbafdf976cfdc032e3bde78de5-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-26
  - id: s2
    title: "Understanding Machine Learning: From Theory to Algorithms"
    publisher: Cambridge University Press, 2014 (S. Shalev-Shwartz and S. Ben-David), authors' free edition
    url: https://cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf
    type: textbook
    accessed: 2026-11-26
  - id: s3
    title: "10: Empirical Risk Minimization"
    publisher: Cornell University CS 4780/5780 Machine Learning, lecture notes (Spring 2023)
    url: https://www.cs.cornell.edu/courses/cs4780/2023sp/lectures/lecturenote10.html
    type: academic
    accessed: 2026-11-26
  - id: s4
    title: "mixup: Beyond Empirical Risk Minimization"
    publisher: ICLR 2018 (H. Zhang, M. Cisse, Y. N. Dauphin, D. Lopez-Paz), authors' arXiv version
    url: https://arxiv.org/abs/1710.09412v2
    type: primary
    accessed: 2026-11-26
created: 2026-11-26
---

# Empirical risk minimization

**Empirical risk minimization (ERM)** is the rule at the heart of supervised learning: since the quantity we actually care about, the expected loss of a predictor on the unknown data-generating distribution, cannot be evaluated, pick the predictor whose *average loss on the training sample* is smallest. Vladimir Vapnik's 1991 NIPS paper set out ERM and its refinement, structural risk minimization, as the two principles of a general theory of learning as function estimation, and noted that classical least squares and maximum likelihood are both realizations of ERM.[^s1]

## Definition

Vapnik's setup has a generator drawing inputs *x* from a fixed but unknown distribution, a supervisor returning outputs *y*, and a learning machine implementing a family of functions f(x, w). Given a loss L(y, f(x, w)), the **risk** is the expected loss R(w) = ∫ L(y, f(x, w)) dP(x, y). Because P is unknown, ERM replaces it with the **empirical risk** E(w) = (1/ℓ) Σᵢ L(yᵢ, f(xᵢ, w)) over ℓ i.i.d. training pairs, and hopes that the minimizer of E also nearly minimizes R.[^s1] Zhang et al. describe the same move as substituting the empirical distribution, a set of point masses on the *n* training examples, for the true one.[^s4] Shalev-Shwartz and Ben-David's textbook writes the rule as ERM_H(S), any hypothesis in a class H that minimizes training error L_S(h).[^s2]

In practice the objective is almost always regularized. Cornell's CS 4780 notes write the general form as the mean training loss plus λ·r(w), where the loss penalizes training error and the regularizer penalizes complexity, and point out that this penalized form is equivalent to minimizing loss subject to r(w) ≤ B for a suitable B.[^s3] Choosing the loss and regularizer recovers familiar methods: squared loss gives ordinary least squares (with an l2 penalty, ridge regression; with l1, the lasso), log loss gives logistic regression, hinge loss with an l2 penalty gives the linear SVM, and exponential loss underlies AdaBoost.[^s3] The 0-1 loss is what classification really cares about, but it is discontinuous and impractical to optimize, so convex surrogates such as the hinge and exponential losses, which upper-bound it, are minimized instead.[^s3]

## When ERM works

The central question is whether a low empirical risk implies a low true risk. Vapnik states that ERM is consistent exactly when empirical risk converges to true risk *uniformly* over the whole function class, which turns learnability into a question about the class's capacity.[^s1] For binary classification he bounds the gap with the VC dimension *h*: with probability 1 − η, the true error is at most the training error plus a confidence term that shrinks roughly like √(h·ln(ℓ/h)/ℓ). When the ratio ℓ/h is large the term is negligible and ERM is justified; when it is small, even zero training error guarantees nothing.[^s1]

The textbook's **fundamental theorem of statistical learning** makes this precise for binary classification with 0-1 loss: a class has finite VC dimension if and only if it has the uniform convergence property, if and only if any ERM rule is a successful (agnostic) PAC learner for it.[^s2] The quantitative version puts the sample complexity between constants times (d + log(1/δ))/ε and (d·log(1/ε) + log(1/δ))/ε for VC dimension *d*. The authors caution that the equivalence is specific to binary classification; in other learning problems ERM can fail even though some other rule learns.[^s2]

## Structural risk minimization and regularization

Vapnik's answer to small samples is **structural risk minimization (SRM)**: arrange the hypotheses into nested subsets of increasing VC dimension, run ERM inside each, and choose the subset that minimizes empirical risk plus the confidence term. Larger subsets fit the data better but pay a larger capacity penalty.[^s1] He gives neural-network examples of such structures: growing the number of hidden units, or bounding the weight norm, which for a convex loss amounts to adding a λ‖w‖² penalty, the procedure known as weight decay.[^s1] The textbook generalizes SRM to countable unions of classes, weighting each class's complexity term.[^s2] This is the theoretical root of the regularized ERM objective used everywhere today.[^s3]

## Limitations and critiques

Zhang et al. argue that plain ERM is a poor fit for modern deep networks. Because the empirical risk only checks the model at the *n* training points, a network with roughly as many parameters as examples can drive it to zero by memorizing the data, even with random labels, and ERM-trained networks can change predictions sharply on inputs just outside the training distribution, such as adversarial examples.[^s4] Their remedy, **mixup**, belongs to the vicinal risk minimization family: it trains on convex combinations of random pairs of inputs and of their one-hot labels, with the mixing weight drawn from a Beta(α, α) distribution, and recovers ordinary ERM as α approaches 0.[^s4] The textbook also notes that uniform convergence, and hence the classic ERM guarantee, is not necessary for learnability outside binary classification.[^s2]

## Connections

ERM is the basic learning rule of **supervised learning** and the main object analysed by **statistical learning theory**, which explains when it succeeds through capacity measures like the **VC dimension**.[^s1][^s2] Its inner term is a **loss function**, and the specific loss chosen yields the **support vector machine**, **logistic regression** and least squares.[^s3] Adding **regularization** turns ERM into the penalized objective that **mathematical optimization** methods such as gradient descent solve, and Vapnik's **structural risk minimization**, which ERM is the building block of, formalizes the capacity control that guards against **overfitting** and mirrors the **bias-variance tradeoff**.[^s1][^s3] **Mixup** is an explicit alternative that changes the distribution being averaged over, motivated by memorization in over-parameterized networks, the same regime studied under **double descent**.[^s4]

## Sources
[^s1]: V. Vapnik, "Principles of Risk Minimization for Learning Theory", NIPS 1991. https://proceedings.neurips.cc/paper/1991/hash/ff4d5fbbafdf976cfdc032e3bde78de5-Abstract.html (accessed 2026-11-26)
[^s2]: S. Shalev-Shwartz and S. Ben-David, *Understanding Machine Learning: From Theory to Algorithms*, Cambridge University Press, 2014, chs. 2, 6 and 7. https://cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf (accessed 2026-11-26)
[^s3]: Cornell CS 4780/5780, "10: Empirical Risk Minimization", lecture notes, Spring 2023. https://www.cs.cornell.edu/courses/cs4780/2023sp/lectures/lecturenote10.html (accessed 2026-11-26)
[^s4]: H. Zhang, M. Cisse, Y. N. Dauphin and D. Lopez-Paz, "mixup: Beyond Empirical Risk Minimization", ICLR 2018. https://arxiv.org/abs/1710.09412v2 (accessed 2026-11-26)
