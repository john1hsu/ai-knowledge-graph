---
id: kt:supervised-learning
type: Paradigm
title: Supervised learning
aliases: [learning from labeled data, learning from labelled examples, predictive learning]
domain: ml-foundations
summary: >-
  The machine learning paradigm in which a model is fitted to a dataset of input–label pairs so that it
  predicts the correct label for new, unseen inputs; regression and classification are its two classic forms.
maturity: foundational
broader: [kt:machine-learning]
related: [kt:bias-variance-tradeoff, kt:overfitting, kt:loss-function, kt:pretraining]
relations:
  - {predicate: contrastsWith, object: kt:unsupervised-learning}
  - {predicate: contrastsWith, object: kt:reinforcement-learning}
  - {predicate: studiedIn, object: kt:statistical-learning-theory}
  - {predicate: hasPart, object: kt:empirical-risk-minimization}
sources:
  - id: s1
    title: "CS229 Lecture Notes"
    publisher: Stanford University CS229 Machine Learning (Andrew Ng and Tengyu Ma)
    url: https://cs229.stanford.edu/main_notes.pdf
    type: academic
    accessed: 2026-11-12
  - id: s2
    title: "Understanding Machine Learning: From Theory to Algorithms"
    publisher: Cambridge University Press, 2014 (Shalev-Shwartz and Ben-David), authors' online copy
    url: https://cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf
    type: textbook
    accessed: 2026-11-12
  - id: s3
    title: "Dive into Deep Learning"
    publisher: Zhang, Lipton, Li and Smola, arXiv:2106.11342 (book, d2l.ai)
    url: https://arxiv.org/pdf/2106.11342
    type: textbook
    accessed: 2026-11-12
  - id: s4
    title: "A Theory of the Learnable"
    publisher: Communications of the ACM 27(11), November 1984 (L. G. Valiant), Princeton COS 511 course copy
    url: https://www.cs.princeton.edu/courses/archive/spring13/cos511/handouts/valiant.pdf
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Supervised learning

**Supervised learning** is the setting in which a learner is given examples that pair an input with the output it should produce, and must learn a rule that predicts the output for inputs it has not seen. Stanford's CS229 notes call each pair (x⁽ⁱ⁾, y⁽ⁱ⁾) a training example, a list of them a training set, and the learned function h : X → Y a *hypothesis*.[^s1] Shalev-Shwartz and Ben-David characterise the paradigm by the extra information, such as a spam or not-spam label, that training examples carry and test examples lack; the learner's job is to supply that missing information for new data.[^s2]

## Formal setting

In the standard statistical model, inputs are drawn from an unknown distribution D over a domain X and labelled by an unknown target, and the learner sees only a finite sample S = ((x₁, y₁), …, (xₘ, yₘ)). What it actually cares about is the **true error** (also called generalization error or risk): how often its predictor errs on fresh draws from D. Because D is unknown, the learner can only compute the **training error** on S.[^s2] The basic strategy, **empirical risk minimization (ERM)**, picks the predictor that minimises training error. Unrestricted ERM can fail badly: a predictor that simply memorises the training points scores zero training error yet generalises no better than chance. The remedy is an *inductive bias*, fixing a hypothesis class in advance; a narrower class guards better against overfitting at the price of a stronger bias, and for a finite class a sample on the order of log(|H|/δ)/ε examples suffices to get error at most ε with probability 1 − δ under the book's assumptions.[^s2]

## Task types

When the target is continuous, such as a house price, the problem is **regression**; when it takes a small number of discrete values, it is **classification**.[^s1] CS229 introduces linear regression with the least-squares cost J(θ) = ½ Σᵢ (h_θ(x⁽ⁱ⁾) − y⁽ⁱ⁾)², minimised by gradient descent or the normal equations, and logistic regression for binary labels, which squashes θᵀx through a sigmoid and is fitted by maximising log-likelihood.[^s1] *Dive into Deep Learning* adds the practical variants: binary, multiclass and hierarchical classification (usually trained with cross-entropy), multi-label tagging, search ranking, recommender systems, and sequence-to-sequence problems such as speech recognition and machine translation in which input and output lengths differ.[^s3] It frames most supervised models as estimating the conditional probability of a label given the features.[^s3]

## Origins

The learnability question was given a computational footing by Leslie Valiant's 1984 *Communications of the ACM* paper, which defined learning as acquiring a concept without explicit programming, from examples drawn according to an arbitrary fixed distribution. A learner succeeded if, in polynomial time, it produced a rule whose error could be made arbitrarily small with high probability, the template later known as probably approximately correct (PAC) learning.[^s4] Shalev-Shwartz and Ben-David build their formal treatment of supervised learning on this framework.[^s2]

## Limitations

Supervised learning depends on labels, which may need to be produced by paid human annotators.[^s3] It is also an *offline* paradigm: models train on a fixed dataset and never act on the world, so they ignore how predictions change future data, and performance can degrade under **distribution shift**, when test data differ from training data.[^s3] The guarantees above hold only when test inputs come from the same distribution as the sample.[^s2]

## In practice

The paradigm covers everyday prediction problems, from estimating a patient's length of hospital stay to flagging cancer in a CT image or ranking search results.[^s3] Where labels are scarce, self-supervised methods manufacture supervision from unlabelled data, for example by predicting masked words in text or the relative position of image crops, so that the familiar predict-the-target machinery can run without human annotation.[^s3] The same building blocks, a hypothesis class, a loss and an optimiser such as gradient descent, carry over from linear and logistic regression to deep networks.[^s1][^s3]

## Connections

Supervised learning is a core branch of **machine learning**, and it **contrasts with unsupervised learning**, which works without labels, and with **reinforcement learning**, where feedback is less direct than the quantity being predicted and the learner interacts with an environment.[^s2][^s3] **Empirical risk minimization** is its basic learning rule, analysed in **statistical learning theory**, where the tension between hypothesis-class size and generalization mirrors the **bias-variance tradeoff** and explains **overfitting**.[^s2] Every supervised method optimises a **loss function**, such as squared error or cross-entropy,[^s1][^s3] and **pretraining** with self-supervised objectives borrows its predict-the-target recipe while generating the targets from unlabelled data.[^s3]

## Sources
[^s1]: Ng and Ma, "CS229 Lecture Notes", Stanford University. https://cs229.stanford.edu/main_notes.pdf (accessed 2026-11-12)
[^s2]: Shalev-Shwartz and Ben-David, "Understanding Machine Learning: From Theory to Algorithms", Cambridge University Press, 2014. https://cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf (accessed 2026-11-12)
[^s3]: Zhang, Lipton, Li and Smola, "Dive into Deep Learning", arXiv:2106.11342. https://arxiv.org/pdf/2106.11342 (accessed 2026-11-12)
[^s4]: Valiant, "A Theory of the Learnable", Communications of the ACM 27(11), 1984. https://www.cs.princeton.edu/courses/archive/spring13/cos511/handouts/valiant.pdf (accessed 2026-11-12)
