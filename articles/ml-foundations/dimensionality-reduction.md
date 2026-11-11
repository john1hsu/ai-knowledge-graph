---
id: kt:dimensionality-reduction
type: Technique
title: Dimensionality reduction
aliases: [dimension reduction, manifold learning, nonlinear dimensionality reduction]
domain: ml-foundations
summary: >-
  The family of methods that map high-dimensional data to a much smaller number of coordinates while keeping
  the structure that matters, such as variance, neighbourhoods or geodesic distances, for compression,
  visualisation or as input to other learners.
maturity: foundational
broader: [kt:unsupervised-learning, kt:machine-learning]
related: [kt:principal-component-analysis, kt:embeddings, kt:autoencoder, kt:t-sne, kt:umap]
relations:
  - {predicate: mitigates, object: kt:curse-of-dimensionality}
  - {predicate: implementedIn, object: kt:scikit-learn}
  - {predicate: influencedBy, object: kt:geoffrey-hinton}
sources:
  - id: s1
    title: "Lecture 2: k-nearest neighbors / Curse of Dimensionality"
    publisher: Cornell University CS 4780/5780 Machine Learning for Intelligent Systems, Spring 2022 lecture notes
    url: https://courses.cs.cornell.edu/cs4780/2022sp/notes/LectureNotes03.html
    type: academic
    accessed: 2026-11-11
  - id: s2
    title: "A Global Geometric Framework for Nonlinear Dimensionality Reduction"
    publisher: Science 290(5500), 2319–2323 (2000) (Tenenbaum, de Silva and Langford), MIT course copy
    url: https://www.mit.edu/~9.520/spring06/Papers/Tenenbaum-science-00.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "Reducing the Dimensionality of Data with Neural Networks"
    publisher: Science 313(5786), 504–507 (2006) (Hinton and Salakhutdinov), UC Irvine course copy
    url: https://sites.socsci.uci.edu/~lpearl/courses/readings/HintonSalakhudinov2006_DeepBeliefScience.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "Visualizing Data using t-SNE"
    publisher: Journal of Machine Learning Research 9(86), 2579–2605 (2008) (van der Maaten and Hinton)
    url: https://www.jmlr.org/papers/v9/vandermaaten08a.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction"
    publisher: arXiv:1802.03426v3 (McInnes, Healy and Melville), authors' version dated 2018-12-07
    url: https://arxiv.org/pdf/1802.03426v3.pdf
    type: primary
    accessed: 2026-11-11
  - id: s6
    title: "Manifold learning"
    publisher: scikit-learn user guide (stable documentation source)
    url: https://scikit-learn.org/stable/_sources/modules/manifold.rst.txt
    type: official-docs
    accessed: 2026-11-11
created: 2026-11-11
---

# Dimensionality reduction

**Dimensionality reduction** is the task of re-describing data that has many measured variables with far fewer coordinates, while preserving whatever structure the analyst cares about: variance, local neighbourhoods, or distances along the shape the data actually occupies. It is usually unsupervised, learning the mapping from the data alone, and serves three purposes: compressing inputs for downstream models, making high-dimensional data visible in two or three dimensions, and estimating how many degrees of freedom the data really has.[^s2][^s6]

## Why it is needed

The motivation is the **curse of dimensionality**. Cornell's CS 4780 notes give a concrete case: with 1,000 points spread uniformly in a unit hypercube, the smallest cube holding a point's 10 nearest neighbours has edge length about 0.1 in two dimensions but about 0.63 in ten and 0.955 in a hundred, so "nearest" neighbours stop being near; shrinking that cube back to 0.1 needs a number of points that grows exponentially with dimension.[^s1] Pairwise distances also bunch into a narrow range as dimension rises.[^s1] The saving grace is that real data rarely fills its ambient space. Tenenbaum and colleagues note that 64×64-pixel face images live in 4,096 dimensions yet vary along roughly three underlying factors (two pose angles and lighting direction).[^s2] Dimensionality reduction tries to recover that low-dimensional structure, often called a **manifold**.[^s6]

## Families of methods

**Linear projections.** Principal component analysis, independent component analysis and linear discriminant analysis pick a linear projection that is "interesting" by a fixed criterion; random projections are cheaper but tend to miss the most informative directions. Linear methods are fast and well understood but cannot unfold curved structure.[^s6]

**Manifold learning.** Isomap (2000) builds a k-nearest-neighbour graph, estimates geodesic distances as shortest paths through that graph, and then runs classical multidimensional scaling on those distances. On the "Swiss roll", a 2-D sheet rolled up in 3-D, PCA and MDS fail to find the two intrinsic dimensions while Isomap recovers them, and it keeps a non-iterative, globally optimal solution.[^s2] Locally linear embedding, Hessian eigenmaps, LTSA and spectral embedding (Laplacian eigenmaps) instead preserve local neighbourhood relations; scikit-learn's guide lists their costs, which scale with the number of samples N, neighbours k and target dimension d.[^s6]

**Neighbour-embedding methods for visualisation.** t-SNE (van der Maaten and Hinton, 2008) refines stochastic neighbour embedding so that maps are easier to optimise and less crowded in the centre, and it reveals structure at several scales; the authors reported clearer maps than Sammon mapping, Isomap and LLE on nearly all datasets tested.[^s4] UMAP (McInnes, Healy and Melville, 2018) grounds the same goal in Riemannian geometry and fuzzy simplicial sets; its authors report visual quality competitive with t-SNE, faster run times, and no practical limit on output dimension, while cautioning that it still emphasises local over global structure.[^s5]

**Neural autoencoders.** Hinton and Salakhutdinov (2006) trained deep autoencoders, an encoder squeezing inputs into a small code layer and a decoder reconstructing them, by first pretraining stacked restricted Boltzmann machines and then fine-tuning with backpropagation. A 784-1000-500-250-30 network on MNIST cut average squared reconstruction error to 3.00, versus 13.87 for 30-component PCA, and 10-dimensional document codes beat latent semantic analysis at retrieving same-topic newswire stories.[^s3]

## Limitations and pitfalls

Nonlinear methods are sensitive to their neighbourhood graph. Noise can create "short-circuit" edges that join distant parts of a manifold; duplicate points or disconnected clusters can make the underlying matrices singular; and features on different scales distort nearest-neighbour search, so scaling inputs first is recommended.[^s6] Isomap's guarantees can require impractically many samples when curvature is high or density uneven.[^s2] For t-SNE, the perplexity setting controls the effective neighbourhood size, results vary across random seeds, and distances between clusters in the plot should not be over-interpreted; a poorly separated 2-D map does not prove the classes are inseparable.[^s6] t-SNE is also slow: scikit-learn notes it can take hours on a million samples where PCA takes seconds or minutes.[^s6]

## In practice

A common pattern is to use a linear method first, both for speed and as initialisation (scikit-learn's `TSNE` supports `init="pca"`), then a neighbour-embedding method for a 2-D plot of embeddings, single-cell profiles or image features.[^s6] The intrinsic dimension can be estimated from where reconstruction or residual-variance error stops falling as components are added.[^s2][^s6] Learned representations inside modern deep networks play the same compressive role that autoencoders demonstrated in 2006.[^s3]

## Connections

Dimensionality reduction is a core branch of **unsupervised learning** within **machine learning**, and it exists to **mitigate** the **curse of dimensionality**.[^s1][^s6] **Principal component analysis** is its standard linear method, while **t-SNE** and **UMAP** are its dominant visualisation tools.[^s4][^s5] The **autoencoder** results of Hinton and Salakhutdinov, together with t-SNE, show the field's **influence** from **Geoffrey Hinton**, and they link it to learned **embeddings**.[^s3][^s4] Most classical methods are **implemented in** **scikit-learn**.[^s6]

## Sources
[^s1]: Cornell CS 4780/5780, "k-nearest neighbors / Curse of Dimensionality" lecture notes, Spring 2022. https://courses.cs.cornell.edu/cs4780/2022sp/notes/LectureNotes03.html (accessed 2026-11-11)
[^s2]: Tenenbaum, de Silva and Langford, "A Global Geometric Framework for Nonlinear Dimensionality Reduction", Science 290 (2000). https://www.mit.edu/~9.520/spring06/Papers/Tenenbaum-science-00.pdf (accessed 2026-11-11)
[^s3]: Hinton and Salakhutdinov, "Reducing the Dimensionality of Data with Neural Networks", Science 313 (2006). https://sites.socsci.uci.edu/~lpearl/courses/readings/HintonSalakhudinov2006_DeepBeliefScience.pdf (accessed 2026-11-11)
[^s4]: van der Maaten and Hinton, "Visualizing Data using t-SNE", JMLR 9 (2008). https://www.jmlr.org/papers/v9/vandermaaten08a.html (accessed 2026-11-11)
[^s5]: McInnes, Healy and Melville, "UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction", arXiv:1802.03426v3 (2018). https://arxiv.org/pdf/1802.03426v3.pdf (accessed 2026-11-11)
[^s6]: scikit-learn user guide, "Manifold learning". https://scikit-learn.org/stable/_sources/modules/manifold.rst.txt (accessed 2026-11-11)
