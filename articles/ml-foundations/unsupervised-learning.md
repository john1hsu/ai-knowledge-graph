---
id: kt:unsupervised-learning
type: Paradigm
title: Unsupervised learning
aliases: [learning from unlabeled data, learning without a teacher]
domain: ml-foundations
summary: >-
  The machine learning paradigm in which a model is fitted to unlabeled data to discover its structure,
  such as clusters, low-dimensional subspaces, useful representations or the data density itself.
maturity: foundational
broader: [kt:machine-learning]
related: [kt:dimensionality-reduction, kt:principal-component-analysis, kt:representation-learning, kt:generative-model, kt:pretraining]
relations:
  - {predicate: contrastsWith, object: kt:supervised-learning}
  - {predicate: hasPart, object: kt:k-means-clustering}
  - {predicate: hasPart, object: kt:expectation-maximization}
  - {predicate: hasPart, object: kt:self-supervised-learning}
sources:
  - id: s1
    title: "Dive into Deep Learning"
    publisher: Zhang, Lipton, Li and Smola, arXiv:2106.11342 (book, d2l.ai)
    url: https://export.arxiv.org/pdf/2106.11342v3.pdf
    type: textbook
    accessed: 2026-11-15
  - id: s2
    title: "Introduction to Unsupervised Learning: Foundations of Neural Computation"
    publisher: MIT Press, 1999 (G. E. Hinton and T. J. Sejnowski, eds.), Salk Institute CNL copy
    url: https://papers.cnl.salk.edu/PDFs/Unsupervised%20Learning_%20Foundations%20of%20Neural%20Computation%201999-3514.pdf
    type: academic
    accessed: 2026-11-15
  - id: s3
    title: "Unsupervised Learning"
    publisher: Neural Computation 1(3):295–311, 1989 (H. B. Barlow)
    url: https://mlanthology.org/neco/1989/barlow1989neco-unsupervised
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "CS229 Lecture Notes: Mixtures of Gaussians and the EM Algorithm"
    publisher: Stanford University CS229 (Andrew Ng), course copy hosted at IIT Delhi
    url: https://web.iitd.ac.in/~sumeet/cs229-notes7b.pdf
    type: academic
    accessed: 2026-11-15
  - id: s5
    title: "Least Squares Quantization in PCM"
    publisher: IEEE Transactions on Information Theory IT-28(2):129–137, 1982 (S. P. Lloyd), CMU course copy
    url: https://www.stat.cmu.edu/~rnugent/PCMI2016/papers/LloydKMeans.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s6
    title: "Maximum Likelihood from Incomplete Data via the EM Algorithm"
    publisher: Journal of the Royal Statistical Society, Series B 39(1):1–38, 1977 (Dempster, Laird and Rubin), Brown course copy
    url: https://cs.brown.edu/courses/csci1820/spring-2022/resources/Dempster_Laird_Rubin_1977.pdf
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Unsupervised learning

**Unsupervised learning** is the branch of machine learning that works with data that carries no labels. Without a target to predict, its goal is open-ended: *Dive into Deep Learning* frames it as a family of questions one can ask of raw data, such as whether items can be grouped around a few prototypes, whether a handful of parameters captures the data's key properties, whether objects can be embedded so their relations are preserved, and how likely a given example is under the data's distribution.[^s1] Hinton and Sejnowski describe it as supervised learning with an unknown output, or equivalently as modelling the probability density of the inputs: the learner fits a generative model that assigns high likelihood to what it observes.[^s2]

## Origins

Much of the early motivation came from neuroscience. In a 1989 *Neural Computation* paper titled simply "Unsupervised Learning", Horace Barlow asked how the brain could exploit the vast stream of sensory input that arrives with no reward or punishment attached. He argued that the redundancy in sensory messages is itself the knowledge a brain needs, that some of it can be extracted from simple statistics such as means and covariances (and perhaps by "minimum entropy coding"), and that such a model of typical events lets surprising inputs be detected and is a prerequisite for ordinary associative learning.[^s3] Hinton and Sejnowski's 1999 MIT Press collection of *Neural Computation* papers traces the same line through redundancy reduction, maximising mutual information, independent component analysis, sparse coding and Hebbian learning rules.[^s2]

The core algorithms are older and came from statistics and signal processing. Stuart Lloyd's least-squares quantization method, circulated at Bell Labs in 1957 and published in 1982, alternates between moving each representative point to the centroid of its cell and redrawing the cells by nearest neighbour; each step cannot increase mean squared error, which is the procedure now taught as k-means.[^s5] Dempster, Laird and Rubin's 1977 paper generalised maximum likelihood estimation to incomplete data with the expectation-maximization (EM) algorithm, proving that each iteration never lowers the likelihood and listing finite mixtures and factor analysis among its applications.[^s6]

## Main task families

- **Clustering** groups points around prototypes, for example photos or users with similar behaviour; k-means is the canonical hard-assignment method.[^s1][^s5]
- **Subspace estimation and dimensionality reduction** find a few parameters that summarise the data; when the relationship is linear this is principal component analysis.[^s1]
- **Representation learning** embeds objects so relations survive, as in the word-vector analogy Rome − Italy + France ≈ Paris.[^s1]
- **Density estimation and deep generative models** estimate p(x) to score or sample data; variational autoencoders, GANs, normalizing flows and diffusion models belong here.[^s1]

Hinton and Sejnowski note that clustering, factor analysis, PCA and ICA can all be cast as special cases of fitting a generative model, which gives the field a common probabilistic language.[^s2]

## How it works: a worked example

Stanford's CS229 notes illustrate the generative view with a mixture of Gaussians. Each unlabeled point x⁽ⁱ⁾ is assumed to come from first drawing a hidden component z⁽ⁱ⁾ with probabilities φ, then sampling from a Gaussian with mean μⱼ and covariance Σⱼ. Because the z⁽ⁱ⁾ are latent, maximum likelihood has no closed form, so EM alternates an **E-step**, which uses Bayes' rule to compute each point's soft membership in each component, with an **M-step**, which re-estimates φ, μ and Σ as weighted averages using those memberships.[^s4] The notes point out that this resembles k-means except that assignments are probabilistic rather than hard.[^s4]

## Limitations and open questions

Without labels there is no single score of success, so objectives are proxies such as likelihood or reconstruction error. Both of the classic algorithms only guarantee a stationary point: Lloyd could not establish conditions for a global minimum of quantization error,[^s5] EM converges to a stationary point of the likelihood at a rate governed by how much information is missing,[^s6] and CS229 advises running k-means and EM from several random initialisations because of local optima.[^s4] Hinton and Sejnowski argued that richer structure would require nonlinear, multilayer generative models, and that the difficulty of inference in such models must be traded against their likelihood.[^s2]

## In practice: self-supervision

The most consequential modern descendant is **self-supervised learning**, which manufactures supervision from the unlabeled data itself: predicting masked words from their context, predicting an occluded image region, or telling whether two images are perturbed views of the same one. The resulting representations are then typically fine-tuned for downstream tasks,[^s1] which is the recipe behind large-scale pretraining of language and vision models.

## Connections

Unsupervised learning is a paradigm of machine learning that **contrasts with** supervised learning, whose examples carry the labels it lacks.[^s1] It **has part** k-means clustering, introduced by Lloyd,[^s5] expectation-maximization, introduced by Dempster, Laird and Rubin,[^s6] and self-supervised learning.[^s1] It is closely **related** to dimensionality reduction and principal component analysis (its subspace-estimation branch), to representation learning and generative models (its embedding and density-estimation branches), and to pretraining, which applies self-supervised objectives at scale.[^s1][^s2]

## Sources
[^s1]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, §1.3.2 "Unsupervised and Self-Supervised Learning", arXiv:2106.11342. https://export.arxiv.org/pdf/2106.11342v3.pdf (accessed 2026-11-15)
[^s2]: G. E. Hinton and T. J. Sejnowski (eds.), introduction to *Unsupervised Learning: Foundations of Neural Computation*, MIT Press, 1999. https://papers.cnl.salk.edu/PDFs/Unsupervised%20Learning_%20Foundations%20of%20Neural%20Computation%201999-3514.pdf (accessed 2026-11-15)
[^s3]: H. B. Barlow, "Unsupervised Learning", *Neural Computation* 1(3):295–311, 1989. https://mlanthology.org/neco/1989/barlow1989neco-unsupervised (accessed 2026-11-15)
[^s4]: A. Ng, CS229 lecture notes, "Mixtures of Gaussians and the EM algorithm", Stanford University. https://web.iitd.ac.in/~sumeet/cs229-notes7b.pdf (accessed 2026-11-15)
[^s5]: S. P. Lloyd, "Least Squares Quantization in PCM", *IEEE Transactions on Information Theory* IT-28(2):129–137, 1982 (Bell Labs draft, 1957). https://www.stat.cmu.edu/~rnugent/PCMI2016/papers/LloydKMeans.pdf (accessed 2026-11-15)
[^s6]: A. P. Dempster, N. M. Laird and D. B. Rubin, "Maximum Likelihood from Incomplete Data via the EM Algorithm", *JRSS Series B* 39(1):1–38, 1977. https://cs.brown.edu/courses/csci1820/spring-2022/resources/Dempster_Laird_Rubin_1977.pdf (accessed 2026-11-15)
