---
id: kt:representation-learning
type: Paradigm
title: Representation learning
aliases: [feature learning, learned representations, unsupervised feature learning]
domain: deep-learning
summary: >-
  The approach of having a model learn, from data, the transformations that turn raw inputs into features
  (representations) that make later prediction or analysis easier, instead of relying on features designed
  by hand.
maturity: foundational
broader: [kt:deep-learning, kt:machine-learning]
related: [kt:embeddings, kt:pretraining, kt:dimensionality-reduction, kt:clip, kt:word2vec, kt:self-supervised-learning]
relations:
  - {predicate: influencedBy, object: kt:representation-learning-a-review-and-new-perspectives}
  - {predicate: hasPart, object: kt:contrastive-learning}
  - {predicate: enables, object: kt:transfer-learning}
  - {predicate: contrastsWith, object: kt:feature-engineering}
  - {predicate: basedOn, object: kt:autoencoder}
sources:
  - id: s1
    title: "Representation Learning: A Review and New Perspectives"
    publisher: arXiv:1206.5538 (v3, April 2014; Bengio, Courville and Vincent)
    url: https://arxiv.org/pdf/1206.5538
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "Representation Learning: A Review and New Perspectives (bibliographic record)"
    publisher: IEEE Transactions on Pattern Analysis and Machine Intelligence 35(8), 1798–1828 (2013), via BibBase
    url: https://bibbase.org/network/publication/bengio-courville-vincent-representationlearningareviewandnewperspectives-2013
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "A Simple Framework for Contrastive Learning of Visual Representations"
    publisher: ICML 2020 (Chen, Kornblith, Norouzi and Hinton)
    url: https://icml.cc/virtual/2020/poster/6762
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "Masked Autoencoders Are Scalable Vision Learners"
    publisher: CVPR 2022, CVF Open Access (He, Chen, Xie, Li, Dollár and Girshick)
    url: https://openaccess.thecvf.com/content/CVPR2022/html/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations"
    publisher: arXiv:1811.12359 (Locatello et al.)
    url: https://arxiv.org/abs/1811.12359
    type: primary
    accessed: 2026-11-15
  - id: s6
    title: "Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations (ICML 2019 poster page)"
    publisher: ICML 2019 (Locatello, Bauer, Lucic, Rätsch, Gelly, Schölkopf and Bachem)
    url: https://icml.cc/virtual/2019/poster/4085
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Representation learning

**Representation learning** (also called feature learning) is the practice of letting a model discover, from data, the transformations that map raw inputs such as pixels, waveforms or characters into features that make it easier to build classifiers or other predictors. The idea's standard statement comes from Yoshua Bengio, Aaron Courville and Pascal Vincent of the University of Montreal, whose review argues that a learner's performance depends heavily on how its data is represented, because a representation can either expose or bury the explanatory factors behind the observations.[^s1] The review appeared in *IEEE Transactions on Pattern Analysis and Machine Intelligence* in 2013.[^s2]

## Why learn features instead of designing them

Before deep learning, much of the effort in applied machine learning went into preprocessing pipelines and hand-designed features. Bengio and colleagues read that dependence as a weakness: it means the learner cannot itself pull out and organize the useful information in the input, and it caps how far a method can be applied without expert labor. Reducing it, they argue, is needed for broader applicability and for progress toward AI.[^s1]

They offer two working criteria for a good representation. In a probabilistic model, it often captures the posterior distribution over the latent factors that generated an input; in practice, it is also one that works well as input to a supervised predictor.[^s1]

## Priors behind good representations

The review lists general-purpose assumptions that representation learners exploit:[^s1]

- **Smoothness and manifolds:** similar inputs should map to similar outputs, and real data concentrates near low-dimensional regions of input space.[^s1]
- **Multiple, hierarchical explanatory factors:** data is produced by several roughly independent factors, with abstract concepts built from less abstract ones.[^s1]
- **Sharing across tasks:** features useful for modeling the inputs, or for one task, often help predict other targets, which is why unlabeled data helps.[^s1]
- **Sparsity, clustering and coherence:** only a few factors matter for any one input, categories tend to form separated regions, and nearby observations in time or space share high-level values.[^s1]

From these, the authors favor *disentangling*: features that separate the underlying factors while keeping their information. Merely invariant features, by contrast, can throw away information that a later task needs.[^s1] They also argue that depth and distributed representations are complementary: stacked nonlinear layers reuse features and yield more abstract features higher up, while distributed codes cover many input configurations with relatively few parameters.[^s1]

## Families of methods

The 2013 review groups methods into probabilistic models (for example sparse coding and restricted Boltzmann machines), autoencoders trained to reconstruct their inputs, manifold-learning approaches, and deep networks built by greedy layer-wise pretraining such as Deep Belief Networks.[^s1] It cites early payoffs in speech recognition, object recognition, music transcription, natural-language tasks via word embeddings, and two 2011 transfer-learning challenges won by representation-learning entries.[^s1]

Later work shifted toward self-supervised objectives on large unlabeled datasets. SimCLR (Chen, Kornblith, Norouzi and Hinton, ICML 2020) learns image representations by pulling together two augmented views of the same image; it found that composing augmentations and adding a learnable nonlinear head before the contrastive loss mattered a great deal, and that larger batches and longer training help. A linear classifier on its learned features reached 76.5% top-1 accuracy on ImageNet, which the authors report as matching a supervised ResNet-50.[^s3] Masked autoencoders (He et al., CVPR 2022) instead hide about 75% of image patches and reconstruct them with a lightweight decoder, while the encoder sees only visible patches; the authors report training at least three times faster, 87.8% ImageNet-1K accuracy for a ViT-Huge, and transfer that beats supervised pretraining.[^s4] These results illustrate the field's central claim: features learned without labels can rival or beat features learned from labels.

## Limitations and open questions

What makes a representation "good" remains contested. Locatello and colleagues argued theoretically that unsupervised disentanglement is impossible without inductive biases on both models and data. In more than 12,000 trained models across seven datasets, they could not reliably pick out well-disentangled models without supervision, and more disentanglement did not clearly cut the sample cost of downstream tasks.[^s5] The paper was named an outstanding paper at ICML 2019.[^s6] Bengio and colleagues likewise left open which training objectives work best and how representation learning relates to density estimation and manifold learning.[^s1] Self-supervised methods also bring their own engineering choices, such as augmentations, masking ratios and batch sizes. Those choices act as hidden priors, so results depend on them.[^s3][^s4]

## Connections

Representation learning is the organizing idea under **deep learning** and a broad paradigm within **machine learning**: depth is valued largely because it builds layered, increasingly abstract representations.[^s1] **Embeddings**, **word2vec** and the image-text space of **CLIP** are concrete learned representations, and **dimensionality reduction** methods such as PCA are early, linear relatives, which the review treats as probabilistic or manifold models.[^s1] **Pretraining** and **transfer learning** depend on it, since a representation learned once is reused across tasks.[^s1][^s4] **Self-supervised learning** and **contrastive learning** (SimCLR) are its dominant modern forms, and **autoencoders**, including masked autoencoders, are a long-standing method family.[^s3][^s4] It contrasts with **feature engineering**, the hand-design it was meant to replace.[^s1]

## Sources
[^s1]: Bengio, Courville and Vincent, "Representation Learning: A Review and New Perspectives", arXiv:1206.5538v3, 2014. https://arxiv.org/pdf/1206.5538 (accessed 2026-11-15)
[^s2]: Bibliographic record of Bengio, Courville and Vincent, IEEE TPAMI 35(8):1798–1828, 2013, via BibBase. https://bibbase.org/network/publication/bengio-courville-vincent-representationlearningareviewandnewperspectives-2013 (accessed 2026-11-15)
[^s3]: Chen, Kornblith, Norouzi and Hinton, "A Simple Framework for Contrastive Learning of Visual Representations", ICML 2020. https://icml.cc/virtual/2020/poster/6762 (accessed 2026-11-15)
[^s4]: He, Chen, Xie, Li, Dollár and Girshick, "Masked Autoencoders Are Scalable Vision Learners", CVPR 2022. https://openaccess.thecvf.com/content/CVPR2022/html/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper (accessed 2026-11-15)
[^s5]: Locatello et al., "Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations", arXiv:1811.12359. https://arxiv.org/abs/1811.12359 (accessed 2026-11-15)
[^s6]: ICML 2019 poster page for Locatello et al., marked Outstanding Paper. https://icml.cc/virtual/2019/poster/4085 (accessed 2026-11-15)
