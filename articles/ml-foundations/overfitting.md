---
id: kt:overfitting
type: Concept
title: Overfitting
aliases: [over-fitting, overfit model]
domain: ml-foundations
summary: >-
  The failure mode in which a learned model fits its training data, including noise and quirks of the particular
  sample, more closely than the underlying data distribution, so that training error is low but error on new data
  is high; the gap between the two is the generalization gap.
maturity: foundational
broader: [kt:machine-learning, kt:supervised-learning]
related: [kt:bias-variance-tradeoff, kt:regularization, kt:cross-validation, kt:dropout, kt:double-descent]
relations:
  - {predicate: contrastsWith, object: kt:underfitting}
  - {predicate: studiedIn, object: kt:statistical-learning-theory}
sources:
  - id: s1
    title: "3.6. Generalization"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), d2l.ai
    url: https://d2l.ai/chapter_linear-regression/generalization.html
    type: textbook
    accessed: 2026-11-13
  - id: s2
    title: "Overfitting"
    publisher: Google for Developers, Machine Learning Crash Course
    url: https://developers.google.com/machine-learning/crash-course/overfitting/overfitting?hl=en
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "Overfitting in Neural Nets: Backpropagation, Conjugate Gradient, and Early Stopping"
    publisher: Advances in Neural Information Processing Systems 13 (NIPS 2000) (Caruana, Lawrence and Giles)
    url: https://proceedings.neurips.cc/paper/2000/hash/059fdcd96baeb75112f09fa1dcc740cc-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
    publisher: Journal of Machine Learning Research 15(56), 1929–1958 (2014) (Srivastava, Hinton, Krizhevsky, Sutskever and Salakhutdinov)
    url: https://www.jmlr.org/papers/v15/srivastava14a.html
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s5
    title: "Understanding Deep Learning Requires Rethinking Generalization"
    publisher: ICLR 2017 (Zhang, Bengio, Hardt, Recht and Vinyals), ML Anthology record
    url: https://mlanthology.org/iclr/2017/zhang2017iclr-understanding
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s6
    title: "5.5. Generalization in Deep Learning"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), d2l.ai
    url: https://d2l.ai/chapter_multilayer-perceptrons/generalization-deep.html
    type: textbook
    accessed: 2026-11-13
created: 2026-11-13
---

# Overfitting

**Overfitting** happens when a model fits its training data more closely than it fits the distribution that produced that data, so the patterns it learns do not carry over to new examples.[^s1] The symptom is a gap between low training error and high generalization error, the expected error over the whole data distribution, which can only be estimated from held-out data.[^s1] Google's Machine Learning Crash Course describes the overfit model as one that has effectively memorized its training set and predicts new data poorly, and treats it as a routine practical problem rather than a theoretical curiosity.[^s2] Its opposite, **underfitting**, shows up as high error on both training and validation data with only a small gap between them, usually because the model is too simple for the pattern.[^s1][^s2]

## How it arises

Learning from data only makes sense under some assumption linking training data to future data; the usual one is that training and test examples are drawn independently from the same distribution (IID).[^s1] Google's course adds stationarity and similar train, validation and test partitions as conditions for generalization, and names two main causes of overfitting: a training set that does not represent real-world data well, and a model that is too complex.[^s2] Complexity here means expressiveness, such as the number of parameters and the range of values they can take. A model flexible enough to fit arbitrary labels can reach near-zero training error without that saying anything about test error.[^s1] For a fixed model, fewer training examples make overfitting more likely and more severe, so model complexity should not grow faster than the amount of data.[^s1]

## Detecting it

Because generalization error cannot be computed directly, practitioners hold out a **validation set** for model selection and keep a separate test set untouched until hyperparameters are fixed; when data is scarce, **K-fold cross-validation** trains K times on different splits and averages the validation errors.[^s1] The standard diagnostic is a generalization curve that plots training and validation loss against training iterations: overfitting appears when training loss keeps falling or levels off while validation loss turns upward.[^s2] Shuffling before splitting helps partitions resemble one another, while sorting non-stationary data by time can make them diverge.[^s2]

## Mitigations

**Early stopping** halts training when validation error stops improving, usually with a patience window; Dive into Deep Learning notes that networks tend to fit clean labels before mislabeled ones, which makes early stopping especially useful under label noise.[^s6] Caruana, Lawrence and Giles showed at NIPS 2000 that oversized networks trained with backpropagation and early stopping can generalize as well as smaller ones, because networks of different sizes learn subcomponents of a task in a similar order; conjugate gradient, by contrast, tended to overfit smooth regions of the input space.[^s3] **Regularization** constrains the hypothesis space: weight decay (ℓ2 or ℓ1 penalties) remains common, and **dropout**, which randomly removes units during training, was introduced explicitly as a way to reduce overfitting by discouraging units from co-adapting; its authors reported gains across vision, speech, document classification and computational biology.[^s4][^s6] More, or more representative, data addresses the root cause directly.[^s1][^s2]

## Overfitting in modern deep learning

Deep networks complicate the classical picture. Zhang and colleagues showed at ICLR 2017 that standard image-classification networks trained with stochastic gradient methods can fit completely random labels, and even random noise in place of images, and that explicit regularization barely changes this.[^s5] Such networks clearly have the capacity to memorize, yet they generalize well on real labels, so capacity-based explanations alone do not account for their behaviour.[^s5][^s6] Dive into Deep Learning summarizes the consequences: complexity bounds such as VC dimension say little about these models, extra capacity can sometimes lower test error, and the error curve can follow a **double descent** pattern instead of the classic U-shape.[^s6] Over-parameterized networks that interpolate their training data may be better understood as nonparametric models, much as a 1-nearest-neighbour classifier has zero training error but still generalizes. Why particular design choices close the generalization gap remains an open question.[^s6]

## Connections

Overfitting is a central concern of **machine learning** and particularly **supervised learning**, where performance on unseen labelled data is the goal.[^s1] The **bias-variance tradeoff** is its classical explanation: overfitting corresponds to the high-variance end, and it **contrasts with underfitting** at the high-bias end.[^s1][^s2] **Cross-validation** and held-out validation sets are how it is detected,[^s1] while **regularization** and **dropout** are the standard defences.[^s4][^s6] The **double descent** results and random-label experiments show the limits of the classical account for deep networks,[^s5][^s6] and generalization is studied formally in **statistical learning theory**.[^s6]

## Sources
[^s1]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, §3.6 "Generalization". https://d2l.ai/chapter_linear-regression/generalization.html (accessed 2026-11-13)
[^s2]: Google for Developers, Machine Learning Crash Course, "Overfitting". https://developers.google.com/machine-learning/crash-course/overfitting/overfitting?hl=en (accessed 2026-11-13)
[^s3]: Caruana, Lawrence and Giles, "Overfitting in Neural Nets: Backpropagation, Conjugate Gradient, and Early Stopping", NIPS 2000. https://proceedings.neurips.cc/paper/2000/hash/059fdcd96baeb75112f09fa1dcc740cc-Abstract.html (accessed 2026-11-13)
[^s4]: Srivastava et al., "Dropout: A Simple Way to Prevent Neural Networks from Overfitting", JMLR 15 (2014). https://www.jmlr.org/papers/v15/srivastava14a.html (accessed 2026-11-13)
[^s5]: Zhang, Bengio, Hardt, Recht and Vinyals, "Understanding Deep Learning Requires Rethinking Generalization", ICLR 2017. https://mlanthology.org/iclr/2017/zhang2017iclr-understanding (accessed 2026-11-13)
[^s6]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, §5.5 "Generalization in Deep Learning". https://d2l.ai/chapter_multilayer-perceptrons/generalization-deep.html (accessed 2026-11-13)
