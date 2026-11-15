---
id: kt:generative-model
type: Concept
title: Generative model
aliases: [generative modeling, generative modelling, statistical generative model, deep generative model]
domain: ml-foundations
summary: >-
  A model that learns the probability distribution of the data itself, p(x) or the joint p(x, y),
  so that it can score how likely an example is and sample new examples, in contrast to a
  discriminative model, which learns only p(y | x).
maturity: foundational
broader: [kt:machine-learning]
related: [kt:unsupervised-learning, kt:large-language-model]
relations:
  - {predicate: contrastsWith, object: kt:discriminative-model}
  - {predicate: hasPart, object: kt:variational-autoencoder}
  - {predicate: hasPart, object: kt:generative-adversarial-network}
  - {predicate: hasPart, object: kt:diffusion-model}
sources:
  - id: s1
    title: "CS 236: Deep Generative Models, Lecture 1 (Introduction)"
    publisher: Stanford University (Stefano Ermon and Aditya Grover), 2018
    url: https://deepgenerativemodels.github.io/2018/assets/slides/cs236_lecture1.pdf
    type: academic
    accessed: 2026-11-15
  - id: s2
    title: "On Discriminative vs. Generative Classifiers: A comparison of logistic regression and naive Bayes"
    publisher: NeurIPS 2001 (Andrew Y. Ng and Michael I. Jordan)
    url: https://papers.nips.cc/paper/2001/hash/7b7a53e239400a13bd6be6c91c4f6c4e-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "Background: What is a Generative Model?"
    publisher: Google for Developers, Machine Learning course on GANs
    url: https://developers.google.com/machine-learning/gan/generative
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Deep Generative Modelling: A Comparative Review of VAEs, GANs, Normalizing Flows, Energy-Based and Autoregressive Models"
    publisher: Bond-Taylor, Leach, Long and Willcocks, arXiv:2103.04922 (authors' version; DOI 10.1109/TPAMI.2021.3116668)
    url: https://arxiv.org/abs/2103.04922
    type: primary
    accessed: 2026-11-15
  - id: s5
    title: "A Note on the Evaluation of Generative Models"
    publisher: ICLR 2016 (Lucas Theis, Aäron van den Oord and Matthias Bethge)
    url: https://mlanthology.org/iclr/2016/theis2016iclr-note
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Generative model

A **generative model** is a probabilistic model of the data distribution itself. Stanford's CS 236 course frames a statistical generative model simply as a probability distribution p(x), learned from data plus prior knowledge such as a parametric form, a loss (typically maximum likelihood) and an optimizer; it is called *generative* because drawing samples from p(x) produces new data, such as new images.[^s1] Google's machine learning course gives the same contrast in plain terms: generative models capture the joint distribution p(X, Y), or just p(X) when there are no labels, and can say how likely an example is, while discriminative models capture only p(Y | X) and separate one kind of instance from another.[^s3]

## Generative versus discriminative

The distinction is about *what* is modeled, not which algorithm is used. A discriminative classifier takes the input as given and learns a decision boundary; it never models p(x), which is why it cannot easily cope with missing inputs.[^s1] A generative model must instead account for how the data are spread across the whole input space, including correlations a classifier could ignore, such as which objects tend to appear together in a photo. That makes the generative task strictly harder.[^s3] The two views also meet: a conditional generative model p(x | y) generates inputs given a label, and a discriminative model can itself be read as a simple conditional generative model of the label.[^s1]

The classic analysis is Ng and Jordan's 2001 NeurIPS paper, which compared naive Bayes (generative) with logistic regression (its discriminative counterpart). They argued against the folk wisdom that discriminative training is nearly always better: logistic regression reaches a lower asymptotic error, but naive Bayes approaches its own, higher asymptote much faster, so it can win when training data are scarce. The result is two performance regimes that depend on sample size.[^s2]

## Families of deep generative models

Modern "deep" generative models use neural networks to represent the distribution, and they differ mainly in how they make that distribution tractable.[^s1][^s4] The CS 236 syllabus groups them into fully observed likelihood-based models (autoregressive models and normalizing flows), latent-variable models trained variationally (variational autoencoders), and implicit models trained with two-sample tests or divergences (generative adversarial networks).[^s1] Bond-Taylor and colleagues' comparative review adds energy-based models, under which they also discuss diffusion and score-based models, and observes that each family pays for tractability with run-time, architectural restrictions or a proxy objective.[^s4]

- **Autoregressive models** factor p(x) into a product of conditionals, giving exact likelihoods, but sampling is sequential and slow on high-dimensional data.[^s4]
- **Normalizing flows** give exact likelihoods via change of variables, but need invertible layers with tractable Jacobians and matching input and output sizes.[^s4]
- **VAEs** sample fast but optimize a lower bound (the ELBO) and tend to produce blurry samples on complex data.[^s4]
- **GANs** sample fast without Markov chains but have no tractable likelihood, are hard to train and suffer mode collapse.[^s4]
- **Energy-based and diffusion models** have unnormalized or approximate densities and traditionally need many sampling steps, which motivates step-skipping and SDE solvers.[^s4]

## Evaluation and limitations

Judging a generative model is notoriously hard. Theis, van den Oord and Bethge showed at ICLR 2016 that average log-likelihood, Parzen-window estimates and visual sample quality are largely independent of one another for high-dimensional data, so doing well on one says little about the others. They recommended evaluating a model directly on the application it was built for and avoiding Parzen-window estimates altogether.[^s5] The review by Bond-Taylor et al. accordingly reports several axes side by side (training and sampling speed, parameter count, FID and negative log-likelihood in bits per dimension) rather than a single score.[^s4]

## In practice

Generative models underpin compression, denoising, inpainting and texture synthesis,[^s5] and today's text and image generators. Google's course notes that a next-word prediction model is also a generative model, only far simpler than a GAN;[^s3] scaled up, the same autoregressive idea is the basis of large language models.

## Connections

The broader node is **machine learning**: generative modeling is one of its basic ways of framing a learning problem.[^s1] It **contrasts with** the discriminative model, the p(y | x) view analysed by Ng and Jordan.[^s2] It is closely **related** to **unsupervised learning**, since learning p(x) needs no labels and CS 236 lists recovering features from raw data as a core goal,[^s1] and to **large language models**, which are autoregressive next-token generative models.[^s3] Its main deep families appear as parts: the **variational autoencoder**, the **generative adversarial network** and the **diffusion model**.[^s4]

## Sources
[^s1]: S. Ermon and A. Grover, CS 236 "Deep Generative Models", Lecture 1, Stanford University, 2018. https://deepgenerativemodels.github.io/2018/assets/slides/cs236_lecture1.pdf (accessed 2026-11-15)
[^s2]: A. Y. Ng and M. I. Jordan, "On Discriminative vs. Generative Classifiers: A comparison of logistic regression and naive Bayes", NeurIPS 2001. https://papers.nips.cc/paper/2001/hash/7b7a53e239400a13bd6be6c91c4f6c4e-Abstract.html (accessed 2026-11-15)
[^s3]: Google for Developers, "Background: What is a Generative Model?", Generative Adversarial Networks course. https://developers.google.com/machine-learning/gan/generative (accessed 2026-11-15)
[^s4]: S. Bond-Taylor, A. Leach, Y. Long and C. G. Willcocks, "Deep Generative Modelling: A Comparative Review of VAEs, GANs, Normalizing Flows, Energy-Based and Autoregressive Models", arXiv:2103.04922 (IEEE TPAMI). https://arxiv.org/abs/2103.04922 (accessed 2026-11-15)
[^s5]: L. Theis, A. van den Oord and M. Bethge, "A Note on the Evaluation of Generative Models", ICLR 2016. https://mlanthology.org/iclr/2016/theis2016iclr-note (accessed 2026-11-15)
