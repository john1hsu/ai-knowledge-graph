---
id: kt:bias-variance-tradeoff
type: Concept
title: Bias-variance tradeoff
aliases: [bias-variance dilemma, bias-variance decomposition, bias–variance trade-off]
domain: ml-foundations
summary: >-
  The tension between a learner's systematic error (bias) and its sensitivity to the particular training sample
  (variance), formalised by decomposing expected squared test error into bias squared, variance and irreducible
  noise; it explains underfitting and overfitting and guides choices of model complexity.
maturity: foundational
broader: [kt:machine-learning, kt:supervised-learning]
related: [kt:overfitting, kt:regularization, kt:cross-validation, kt:artificial-neural-network, kt:ensemble-methods]
relations:
  - {predicate: contrastsWith, object: kt:double-descent}
  - {predicate: studiedIn, object: kt:statistical-learning-theory}
sources:
  - id: s1
    title: "Neural Networks and the Bias/Variance Dilemma"
    publisher: Neural Computation 4, 1–58 (1992) (Geman, Bienenstock and Doursat), ML Anthology record
    url: https://mlanthology.org/neco/1992/geman1992neco-neural
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s2
    title: "Lecture Notes: Bias-Variance Tradeoff"
    publisher: Cornell University CS 4/5780 Machine Learning, Spring 2022
    url: https://www.cs.cornell.edu/courses/cs4780/2022sp/notes/LectureNotes17.html
    type: academic
    accessed: 2026-10-31
  - id: s3
    title: "Modeling Basics: Assessment, Selection, and Complexity"
    publisher: Carnegie Mellon University, Statistical Machine Learning lecture notes (Ryan Tibshirani, Larry Wasserman)
    url: https://www.stat.cmu.edu/~ryantibs/statml/review/modelbasics.pdf
    type: academic
    accessed: 2026-10-31
  - id: s4
    title: "Reconciling modern machine learning practice and the bias-variance trade-off"
    publisher: Belkin, Hsu, Ma and Mandal, arXiv:1812.11118 (authors' version; published in PNAS, doi 10.1073/pnas.1903070116)
    url: https://arxiv.org/abs/1812.11118v2
    type: primary
    accessed: 2026-10-31
  - id: s5
    title: "Deep Double Descent: Where Bigger Models and More Data Hurt"
    publisher: ICLR 2020 (Nakkiran, Kaplun, Bansal, Yang, Barak and Sutskever)
    url: https://iclr.cc/virtual/2020/poster/1489
    type: peer-reviewed
    accessed: 2026-10-31
created: 2026-10-31
---

# Bias-variance tradeoff

The **bias-variance tradeoff** describes two competing sources of prediction error in a learned model. *Bias* is the error a learner would still make even with unlimited training data, because of the built-in preferences of its hypothesis class (for example, insisting on a straight line). *Variance* is how much the learned predictor would change if it were trained on a different sample from the same distribution. Rigid models tend toward high bias and underfitting; very flexible ones tend toward high variance and overfitting.[^s2][^s3]

## Origin

The decomposition comes from classical statistics, but it entered machine learning as a named "dilemma" through Stuart Geman, Elie Bienenstock and René Doursat's 1992 paper in *Neural Computation*. They treated feedforward networks trained by backpropagation as nonparametric regression estimators and used the bias/variance lens to argue that such networks, on their own, were poorly suited to hard perception problems; in their view the real obstacle was choosing good representations rather than learning itself.[^s1]

## How it works

For squared loss, the expected test error of a learning algorithm at an input *x*, averaged over random training sets *D* and label noise, splits into three non-negative terms:[^s2][^s3]

E[(h_D(x) − y)²] = Var(h_D(x)) + (E[h_D(x)] − ȳ(x))² + E[(ȳ(x) − y)²]

that is, **variance + bias² + noise**. The noise term reflects ambiguity in the data and features and cannot be removed by any learner.[^s2] Complexity knobs, such as polynomial degree, the number of neighbours *k* in k-nearest neighbours, or a regularization strength, move a model along the tradeoff: small *k* yields low bias but high variance, while large *k* does the reverse. The relationship is not one-for-one, so a small increase in bias can buy a large reduction in variance.[^s3]

Training error is a misleading guide because it is optimistically biased: the fit is chosen to match the very data on which it is scored, and the gap grows with effective degrees of freedom. Held-out estimates such as K-fold cross-validation are therefore used to locate the bottom of the U-shaped test-error curve; the choice of K has its own bias-variance tradeoff.[^s3]

## Diagnosis and remedies

Cornell's CS 4780 notes give a practical recipe. When training error is low but test error is high (a high-variance regime), add data, reduce model complexity, or use bagging. When training error itself is too high (a high-bias regime), move to a more expressive model, add features, or use boosting.[^s2]

## Limitations and open questions

The classical picture predicts that test error rises once a model is complex enough to fit the training data exactly. Modern over-parameterised networks contradict this: they routinely interpolate training data yet generalise well. Belkin, Hsu, Ma and Mandal (later published in *PNAS*) proposed the **double descent** curve, in which the textbook U-shape is followed by a second fall in test error as capacity grows beyond the interpolation point, and reported it across several model families and datasets.[^s4] Nakkiran and colleagues (ICLR 2020) extended the observation to deep networks, showed an epoch-wise version as training length increases, proposed an "effective model complexity" measure, and identified regimes in which adding more training samples temporarily hurts test performance.[^s5] These findings do not invalidate the decomposition itself, which remains an identity for squared loss, but they limit the folk rule that bigger models always overfit.[^s3][^s4]

## In practice

Practitioners use the tradeoff as a diagnostic vocabulary: comparing training and validation curves to decide whether to gather more data, regularise, simplify, or scale up. Ensemble methods map directly onto it, with bagging aimed mainly at variance and boosting at bias.[^s2] For large neural networks, the double descent results explain why scaling past the point of perfect training fit is often worthwhile rather than wasteful.[^s4][^s5]

## Connections

The tradeoff is a core idea in **machine learning** and especially **supervised learning**, where test error on labelled data is the target.[^s2] It is the theoretical account of **overfitting** and of why **regularization** and **cross-validation** work.[^s3] Its entry into the field came through analysis of **artificial neural networks**,[^s1] and **ensemble methods** such as bagging and boosting are standard tools for trading one term against the other.[^s2] It **contrasts with double descent**, the modern observation that the classical U-curve is only the first part of a longer story,[^s4][^s5] and it is studied formally within **statistical learning theory**.[^s3]

## Sources
[^s1]: Geman, Bienenstock and Doursat, "Neural Networks and the Bias/Variance Dilemma", Neural Computation 4 (1992). https://mlanthology.org/neco/1992/geman1992neco-neural (accessed 2026-10-31)
[^s2]: Cornell CS 4/5780, "Bias-Variance Tradeoff" lecture notes, Spring 2022. https://www.cs.cornell.edu/courses/cs4780/2022sp/notes/LectureNotes17.html (accessed 2026-10-31)
[^s3]: Tibshirani and Wasserman, "Modeling Basics: Assessment, Selection, and Complexity", CMU Statistical Machine Learning notes. https://www.stat.cmu.edu/~ryantibs/statml/review/modelbasics.pdf (accessed 2026-10-31)
[^s4]: Belkin, Hsu, Ma and Mandal, "Reconciling modern machine learning practice and the bias-variance trade-off", arXiv:1812.11118, later published in PNAS. https://arxiv.org/abs/1812.11118v2 (accessed 2026-10-31)
[^s5]: Nakkiran et al., "Deep Double Descent: Where Bigger Models and More Data Hurt", ICLR 2020. https://iclr.cc/virtual/2020/poster/1489 (accessed 2026-10-31)
