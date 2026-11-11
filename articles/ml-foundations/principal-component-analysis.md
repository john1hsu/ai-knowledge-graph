---
id: kt:principal-component-analysis
type: Algorithm
title: Principal component analysis
aliases: [PCA, principal components analysis, Hotelling transform]
domain: ml-foundations
summary: >-
  A linear dimensionality-reduction method that re-expresses centred data in an orthonormal basis of directions,
  the principal components, ordered by how much variance they capture; keeping the top k components gives the
  k-dimensional linear projection with the smallest squared reconstruction error.
maturity: foundational
broader: [kt:unsupervised-learning, kt:dimensionality-reduction]
related: [kt:embeddings, kt:factor-analysis, kt:kernel-pca]
relations:
  - {predicate: createdBy, object: kt:karl-pearson}
  - {predicate: createdBy, object: kt:harold-hotelling}
  - {predicate: basedOn, object: kt:singular-value-decomposition}
  - {predicate: implementedIn, object: kt:scikit-learn}
sources:
  - id: s1
    title: "Probabilistic Principal Component Analysis"
    publisher: Journal of the Royal Statistical Society, Series B 61(3), 611–622 (1999) (Tipping and Bishop), Virginia Tech course copy
    url: https://www.leman.stat.vt.edu/VTCourses/PPCA.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "Dimensionality Reduction: Principal Component Analysis (PCA)"
    publisher: Stanford University CS229 Machine Learning, Fall 2022 (Carlos Guestrin)
    url: https://cs229.stanford.edu/notes2022fall/pca.pdf
    type: academic
    accessed: 2026-11-11
  - id: s3
    title: "6.5.5. Principal Components"
    publisher: NIST/SEMATECH e-Handbook of Statistical Methods, National Institute of Standards and Technology
    url: https://itl.nist.gov/div898/handbook/pmc/section5/pmc55.htm
    type: government
    accessed: 2026-11-11
  - id: s4
    title: "Hotelling, Harold"
    publisher: Encyclopedia of Mathematics (EMS / Springer), entry by Allan R. Sampson
    url: https://encyclopediaofmath.org/wiki/Hotelling,_Harold
    type: encyclopedia
    accessed: 2026-11-11
  - id: s5
    title: "Nonlinear Component Analysis as a Kernel Eigenvalue Problem"
    publisher: Neural Computation 10, 1299–1319 (1998) (Schölkopf, Smola and Müller), ML Anthology record
    url: https://mlanthology.org/neco/1998/scholkopf1998neco-nonlinear
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s6
    title: "sklearn.decomposition.PCA"
    publisher: scikit-learn 1.8 API documentation
    url: https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.PCA.html
    type: official-docs
    accessed: 2026-11-11
created: 2026-11-11
---

# Principal component analysis

**Principal component analysis (PCA)** is the classic method for compressing many correlated variables into a few new ones. It finds an orthonormal set of directions in the data, the *principal components*, such that projecting onto the first one preserves as much variance as any single direction can, the second preserves the most remaining variance subject to being orthogonal to the first, and so on. Equivalently, the top k components define the k-dimensional linear subspace onto which the data can be projected with the least squared reconstruction error.[^s1][^s2] NIST's engineering statistics handbook describes the goal as shrinking a large set of variables to a small set that still carries most of the information.[^s3]

## Origin

PCA has two classic derivations. Karl Pearson (1901) posed it geometrically, as finding the lines and planes that fit a cloud of points most closely, which amounts to minimising squared reconstruction error among orthogonal projections. Harold Hotelling (1933) derived it as the linear projection that maximises variance in the projected space.[^s1] Hotelling's paper, "Analysis of a complex of statistical variables into principal components" in the *Journal of Educational Psychology*, framed the components as uncorrelated linear combinations of the original measurements.[^s4]

## How it works

Given N data vectors in d dimensions, the standard recipe is:[^s2]

1. Centre the data by subtracting the mean vector x̄.
2. Form the sample covariance matrix S = (1/N) X_cᵀ X_c of the centred data X_c.
3. Compute the eigenvectors u₁, …, u_d of S and sort them by eigenvalue, largest first.
4. Keep the top k eigenvectors; the new coordinates of a point x are z_i = (x − x̄) · u_i.[^s2]

Each eigenvalue is the variance captured along its component, so the discarded eigenvalues measure exactly what the projection throws away. For high-dimensional data the d × d covariance matrix is expensive, so implementations instead take the singular value decomposition of the centred data matrix and keep its top singular vectors.[^s2][^s6]

Whether to standardise each variable first is a real modelling choice. NIST's tutorial standardises to mean 0 and variance 1 and works from the correlation matrix,[^s3] whereas scikit-learn's `PCA` centres each feature but does not scale it, so variables measured on large scales dominate unless the user rescales them.[^s6]

## Limitations and extensions

PCA is linear: it can only find flat subspaces. Schölkopf, Smola and Müller (1998) introduced **kernel PCA**, which uses kernel functions to perform PCA implicitly in a high-dimensional nonlinear feature space, such as the space of all products of five pixels in 16 × 16 images.[^s5] Classical PCA also has no probability model for the data. Tipping and Bishop (1999) showed that the principal subspace arises as the maximum-likelihood solution of a Gaussian latent-variable model related to factor analysis, with isotropic noise whose estimated variance equals the average of the discarded eigenvalues; this **probabilistic PCA** supports an EM fitting algorithm, missing data and mixtures of PCA models.[^s1] Because the components are combinations of all original variables, the reduced variables are not a one-to-one recoding of the originals, and the original variables cannot be recovered from them exactly.[^s3]

Choosing k is a judgement call. Common practice keeps enough components to explain a chosen fraction of total variance; scikit-learn accepts that fraction directly and also offers Minka's automatic maximum-likelihood estimate of the dimension.[^s6]

## In practice

Stanford's CS229 notes list the main uses: shrinking inputs so downstream learners have fewer parameters, projecting to two or three dimensions for visualisation, revealing the intrinsic dimensionality of data, and building low-dimensional embeddings of images and words; the "eigenfaces" face-recognition work of Turk and Pentland (1991) is the canonical example.[^s2] As of scikit-learn 1.8, `PCA` chooses automatically between an exact SVD, an eigendecomposition of the covariance matrix, ARPACK and the randomized SVD of Halko et al., depending on data shape, and exposes `explained_variance_ratio_` and optional whitening.[^s6]

## Connections

PCA is a core **unsupervised learning** technique and the standard linear method of **dimensionality reduction**.[^s2] It was **created by** Karl Pearson and Harold Hotelling through their separate derivations,[^s1][^s4] and its computation is **based on** the **singular value decomposition**.[^s2][^s6] It is closely **related** to **factor analysis**, from which probabilistic PCA borrows its latent-variable form,[^s1] and to **kernel PCA**, its nonlinear generalisation.[^s5] Its projections are an early form of learned **embeddings**.[^s2] A widely used Python version is **implemented in** **scikit-learn**.[^s6]

## Sources
[^s1]: Tipping and Bishop, "Probabilistic Principal Component Analysis", Journal of the Royal Statistical Society Series B 61(3), 1999. https://www.leman.stat.vt.edu/VTCourses/PPCA.pdf (accessed 2026-11-11)
[^s2]: Guestrin, "Dimensionality Reduction: Principal Component Analysis (PCA)", Stanford CS229, Fall 2022. https://cs229.stanford.edu/notes2022fall/pca.pdf (accessed 2026-11-11)
[^s3]: NIST/SEMATECH e-Handbook of Statistical Methods, section 6.5.5 "Principal Components". https://itl.nist.gov/div898/handbook/pmc/section5/pmc55.htm (accessed 2026-11-11)
[^s4]: Sampson, "Hotelling, Harold", Encyclopedia of Mathematics. https://encyclopediaofmath.org/wiki/Hotelling,_Harold (accessed 2026-11-11)
[^s5]: Schölkopf, Smola and Müller, "Nonlinear Component Analysis as a Kernel Eigenvalue Problem", Neural Computation 10 (1998). https://mlanthology.org/neco/1998/scholkopf1998neco-nonlinear (accessed 2026-11-11)
[^s6]: scikit-learn 1.8 documentation, "sklearn.decomposition.PCA". https://scikit-learn.org/1.8/modules/generated/sklearn.decomposition.PCA.html (accessed 2026-11-11)
