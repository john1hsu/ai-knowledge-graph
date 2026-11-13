---
id: kt:regularization
type: Concept
title: Regularization
aliases: [regularisation, model regularization, regularizer]
domain: ml-foundations
summary: >-
  Any modification to a learning algorithm, most classically a penalty on the size of the model's parameters, that
  is meant to improve performance on unseen data rather than on the training set, typically by trading a little
  extra bias for a large reduction in variance.
maturity: foundational
broader: [kt:machine-learning]
related: [kt:bias-variance-tradeoff, kt:dropout, kt:double-descent, kt:adam-optimizer, kt:ensemble-methods]
relations:
  - {predicate: mitigates, object: kt:overfitting}
  - {predicate: hasPart, object: kt:weight-decay}
  - {predicate: hasPart, object: kt:lasso}
  - {predicate: hasPart, object: kt:early-stopping}
  - {predicate: studiedIn, object: kt:statistical-learning-theory}
sources:
  - id: s1
    title: "3.7. Weight Decay"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), d2l.ai
    url: https://d2l.ai/chapter_linear-regression/weight-decay.html
    type: textbook
    accessed: 2026-11-13
  - id: s2
    title: "Regression Shrinkage and Selection via the Lasso"
    publisher: Journal of the Royal Statistical Society, Series B 58(1), 267–288 (1996) (Tibshirani); course-reading copy hosted by the University of Washington
    url: https://sites.stat.washington.edu/courses/stat527/s13/readings/j_royal_stat_soc_b1996.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "A Simple Weight Decay Can Improve Generalization"
    publisher: Advances in Neural Information Processing Systems 4 (NIPS 1991) (Krogh and Hertz)
    url: https://papers.nips.cc/paper/1991/hash/8eefcfdf5990e441f0fb6f3fad709e21-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "Decoupled Weight Decay Regularization"
    publisher: ICLR 2019 (Loshchilov and Hutter), arXiv:1711.05101
    url: https://arxiv.org/abs/1711.05101
    type: primary
    accessed: 2026-11-13
  - id: s5
    title: "Understanding deep learning requires rethinking generalization"
    publisher: Google Research publication page; ICLR 2017 (Zhang, Bengio, Hardt, Recht and Vinyals)
    url: https://research.google/pubs/understanding-deep-learning-requires-rethinking-generalization/
    type: lab-research
    accessed: 2026-11-13
created: 2026-11-13
---

# Regularization

**Regularization** is the umbrella term for techniques that constrain or perturb how a model is fit so that it generalizes better to data it has not seen. The classic form adds a penalty on parameter size to the training objective, which limits model complexity by keeping weights small instead of by cutting the number of features; *Dive into Deep Learning* calls weight decay perhaps the most widely used regularizer for parametric models.[^s1] Regularization is the main practical lever against overfitting: it deliberately accepts slightly worse training error in exchange for lower error on held-out data.[^s1]

## How it works

The canonical penalized objective is the data loss plus a weighted norm of the weights. For the squared L2 norm this is L(**w**, b) + (λ/2)‖**w**‖², where the non-negative hyperparameter λ sets the trade-off between fitting the training data and keeping weights small; λ = 0 recovers the unregularized problem, and the bias term is often left unpenalized.[^s1] The ½ factor is a convention that makes the gradient tidy. Under minibatch stochastic gradient descent the penalty turns each update into "shrink every weight by a factor (1 − ηλ), then take the usual gradient step", which is why L2 regularization is called **weight decay** in deep learning.[^s1] In linear statistics the same penalty gives **ridge regression**.[^s1]

Swapping the L2 norm for the L1 norm gives the **lasso**. Tibshirani's 1996 paper defined it as least squares subject to a bound on the sum of absolute coefficient values; that constraint drives some coefficients to exactly zero, producing sparse, interpretable models while keeping ridge-like continuous shrinkage and stability.[^s2] The practical contrast is that L2 spreads weight across many correlated features, whereas L1 concentrates it on a few and so doubles as feature selection.[^s1]

A worked example from *Dive into Deep Learning* shows the effect: a linear model with 200 input dimensions and only 20 training examples overfits badly without a penalty, while a sizeable λ raises training error slightly but lowers validation error.[^s1] λ itself is chosen on validation data, never on the training set.[^s1]

## History and theory

Weight decay was already in use in neural networks when Krogh and Hertz analysed it at NIPS 1991. They showed that, in linear networks, it suppresses components of the weight vector irrelevant to the task by favouring the smallest solution, and that a well-chosen strength damps the effect of static noise in the targets; they extended the analysis to nonlinear networks with hidden units and checked it on NetTalk data.[^s3] The statistical rationale, stated in Tibshirani's lasso paper, is that shrinking or zeroing coefficients gives up a little bias to reduce the variance of predictions.[^s2]

## Limitations and open questions

Regularization does not fully explain why large neural networks generalize. Zhang et al. (ICLR 2017) found that state-of-the-art image classifiers trained with SGD can perfectly fit randomly assigned labels, and that this is qualitatively unaffected by explicit regularization. They also showed that a simple two-layer network can fit any finite sample once its parameter count exceeds the number of data points, so conventional capacity-plus-penalty accounts cannot by themselves explain why such networks generalize.[^s5] The question of what else (the optimizer, the architecture, the data) supplies "implicit" regularization remains open.

Implementation details matter too. Loshchilov and Hutter showed that L2 regularization and weight decay are equivalent for plain SGD (after rescaling by the learning rate) but not for adaptive methods such as Adam, where adding the L2 term to the gradient is not the same as decaying the weights directly. Decoupling the decay from the gradient step (the AdamW variant) made the best decay value less dependent on the learning rate and substantially improved Adam's generalization on image classification.[^s4]

## In practice

Deep learning frameworks build weight decay into their optimizers at no extra cost, since the optimizer already touches every parameter.[^s1] Practitioners usually combine a norm penalty with other regularizers such as early stopping on a validation set, dropout, data augmentation and ensembling, with λ chosen on validation data.[^s1] Because explicit penalties do not stop large networks from memorizing noise, they are best treated as one tuning knob among several rather than a guarantee of good generalization.[^s5] Decoupled weight decay is the variant to use with Adam-style optimizers, since it separates the decay setting from the learning rate.[^s4]

## Connections

Regularization is a core idea of **machine learning** (broader) and the standard remedy for **overfitting**, which it *mitigates*. It is the practical knob on the **bias–variance trade-off**: a stronger penalty adds bias and removes variance.[^s2] Its main members are **weight decay** (L2, ridge), the **lasso** (L1)[^s1][^s2] and **early stopping**; **dropout** and **ensemble methods** are related regularizers for neural networks. The interaction between weight decay and the **Adam optimizer** is the subject of the decoupled-weight-decay work.[^s4] Explaining why heavily overparameterized models generalize even without explicit penalties, the territory of **double descent** and **statistical learning theory**, remains an open question.[^s5]

## Sources
[^s1]: Zhang, Lipton, Li and Smola, "3.7. Weight Decay", *Dive into Deep Learning*. https://d2l.ai/chapter_linear-regression/weight-decay.html (accessed 2026-11-13)
[^s2]: Tibshirani, "Regression Shrinkage and Selection via the Lasso", *Journal of the Royal Statistical Society, Series B* 58(1), 267–288, 1996. https://sites.stat.washington.edu/courses/stat527/s13/readings/j_royal_stat_soc_b1996.pdf (accessed 2026-11-13)
[^s3]: Krogh and Hertz, "A Simple Weight Decay Can Improve Generalization", NIPS 1991. https://papers.nips.cc/paper/1991/hash/8eefcfdf5990e441f0fb6f3fad709e21-Abstract.html (accessed 2026-11-13)
[^s4]: Loshchilov and Hutter, "Decoupled Weight Decay Regularization", ICLR 2019. https://arxiv.org/abs/1711.05101 (accessed 2026-11-13)
[^s5]: Zhang, Bengio, Hardt, Recht and Vinyals, "Understanding deep learning requires rethinking generalization", ICLR 2017. https://research.google/pubs/understanding-deep-learning-requires-rethinking-generalization/ (accessed 2026-11-13)
