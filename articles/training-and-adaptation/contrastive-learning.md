---
id: kt:contrastive-learning
type: Technique
title: Contrastive learning
aliases: [contrastive representation learning, contrastive self-supervised learning, InfoNCE loss, NT-Xent loss, contrastive loss]
domain: training-and-adaptation
summary: >-
  A representation learning technique that trains an encoder by pulling the embeddings of related
  ("positive") pairs of inputs together and pushing unrelated ("negative") pairs apart, typically with a
  pairwise margin loss or a softmax-based InfoNCE objective.
maturity: established
broader: [kt:representation-learning]
related: [kt:embeddings, kt:image-classification, kt:geoffrey-hinton]
relations:
  - {predicate: partOf, object: kt:self-supervised-learning}
  - {predicate: usedIn, object: kt:clip}
  - {predicate: contrastsWith, object: kt:supervised-learning}
  - {predicate: enables, object: kt:zero-shot-learning}
sources:
  - id: s1
    title: "Dimensionality Reduction by Learning an Invariant Mapping"
    publisher: CVPR 2006 (Hadsell, Chopra and LeCun), author copy hosted at NYU
    url: https://cs.nyu.edu/~sumit/publications/assets/cvpr06.pdf
    type: primary
    accessed: 2026-11-17
  - id: s2
    title: "Representation Learning with Contrastive Predictive Coding"
    publisher: arXiv 1807.03748 (van den Oord, Li and Vinyals, DeepMind), 2018, via ar5iv
    url: https://ar5iv.labs.arxiv.org/html/1807.03748
    type: primary
    accessed: 2026-11-17
  - id: s3
    title: "A Simple Framework for Contrastive Learning of Visual Representations"
    publisher: ICML 2020, PMLR 119:1597–1607 (Chen, Kornblith, Norouzi and Hinton)
    url: https://proceedings.mlr.press/v119/chen20j.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "A Simple Framework for Contrastive Learning of Visual Representations (full text)"
    publisher: arXiv 2002.05709 (Chen, Kornblith, Norouzi and Hinton)
    url: https://arxiv.org/pdf/2002.05709
    type: primary
    accessed: 2026-11-17
  - id: s5
    title: "Momentum Contrast for Unsupervised Visual Representation Learning"
    publisher: CVPR 2020 (He, Fan, Wu, Xie and Girshick), CVF Open Access
    url: https://openaccess.thecvf.com/content_CVPR_2020/html/He_Momentum_Contrast_for_Unsupervised_Visual_Representation_Learning_CVPR_2020_paper.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s6
    title: "Learning Transferable Visual Models From Natural Language Supervision"
    publisher: ICML 2021, PMLR 139:8748–8763 (Radford et al., OpenAI)
    url: https://proceedings.mlr.press/v139/radford21a.html
    type: peer-reviewed
    accessed: 2026-11-17
created: 2026-11-17
---

# Contrastive learning

**Contrastive learning** shapes an embedding space by comparison. The encoder sees pairs or sets of inputs that are labelled only as "should be close" (positives) or "should be far" (negatives), and it is trained so that distances in its output space reflect those relations.[^s1][^s3] Because the positives can be manufactured from unlabeled data, for example two random augmentations of one photo, or an image and its own caption, the technique became one of the main engines of modern self-supervised pretraining in vision and multimodal models.[^s3][^s6]

## Origins

The pairwise **contrastive loss** comes from Hadsell, Chopra and LeCun's DrLIM method (CVPR 2006). They wanted a parametric mapping from high-dimensional inputs to a low-dimensional space that relied only on neighbourhood relations between training samples, could learn invariances such as lighting or translation, and could embed unseen inputs without recomputing everything.[^s1] For a pair with output distance D, similar pairs pay ½D², and dissimilar pairs pay ½max(0, m − D)², so they are pushed apart only while they sit inside a margin m.[^s1] The authors likened this to springs: attract-only springs join neighbours, repel-only springs separate non-neighbours, and the repulsive term is what stops the network from mapping every input to one point.[^s1]

The softmax form that dominates today was introduced by van den Oord, Li and Vinyals at DeepMind in **Contrastive Predictive Coding** (CPC, 2018). CPC encodes a sequence, summarises the past with an autoregressive model, and predicts future latent vectors rather than raw inputs.[^s2] Its **InfoNCE** loss presents one true future sample among N candidates (the rest drawn as negatives) and trains the model to pick it out, which makes it a categorical cross-entropy over N classes.[^s2] The paper shows that minimising this loss maximises a lower bound on mutual information, I ≥ log N − L, which tightens as N grows, and it applied CPC to speech, images, text and reinforcement learning agents.[^s2]

## How modern methods work

**SimCLR** (Chen, Kornblith, Norouzi and Hinton, ICML 2020) distilled the image recipe into a few parts: create two augmented views of each image, encode them, pass the result through a small projection MLP, and apply a contrastive loss.[^s3] Its **NT-Xent** loss L2-normalises embeddings, measures cosine similarity, divides by a temperature τ, and for each view treats its partner as the positive and the other 2(N−1) views in a batch of N images as negatives, so no memory bank is required.[^s4] The authors found that composing augmentations, especially random crop plus colour distortion, was critical, because cropping alone lets the network match views by colour histograms.[^s4] They also reported that contrastive training gains more from larger batches and longer schedules than supervised training does, testing batches from 256 to 8,192.[^s3][^s4] After training, the projection head is discarded and the layer before it is used downstream, which performed over 10% better under linear evaluation.[^s4]

**MoCo** (He et al., CVPR 2020) attacked the cost of large batches differently. It casts contrastive learning as a dictionary look-up in which a query must find its matching key, keeps a queue of encoded keys from recent mini-batches as negatives, and updates the key encoder as a slow moving average of the query encoder so the queued keys stay consistent.[^s5]

## Evidence and limitations

In 2020 SimCLR features reached 76.5% ImageNet top-1 accuracy under a linear probe, about a 7% relative gain over the previous best and on par with a supervised ResNet-50, and fine-tuning on only 1% of labels gave 85.8% top-5 accuracy.[^s3] MoCo's representations outperformed supervised ImageNet pretraining on 7 detection and segmentation transfer tasks, leading its authors to argue that the unsupervised–supervised gap had largely closed for many vision tasks.[^s5]

The method's weaknesses follow from its reliance on negatives and augmentations. Good results need many negatives, hence SimCLR's very large batches trained with the LARS optimiser or MoCo's queue.[^s4][^s5] Performance is sensitive to embedding normalisation and the temperature, dropping sharply without them.[^s4] And the learned invariances are only as good as the chosen augmentations, which encode assumptions about which changes should not alter meaning.[^s4] The CPC bound also shows that estimated information is capped at log N, tying the quality of the signal to the number of candidates.[^s2]

## In practice

The largest-scale use pairs different modalities rather than augmented views. OpenAI's **CLIP** (ICML 2021) trained image and text encoders on 400 million internet image–caption pairs to predict which caption belongs with which image; the resulting model transferred zero-shot to over 30 vision datasets and matched the original ResNet-50's ImageNet accuracy without using its 1.28 million training labels.[^s6]

## Connections

Contrastive learning is a technique of **representation learning** and one of the main families within **self-supervised learning**, which it is **part of**; it **contrasts with** **supervised learning** because its positives come from the data rather than from annotators.[^s1][^s3] Its output is a space of **embeddings** usually judged by **image classification** probes.[^s3] It is **used in** **CLIP**, where it **enables** **zero-shot learning** through text prompts.[^s6] **Geoffrey Hinton** co-authored SimCLR.[^s3]

## Sources

[^s1]: Hadsell, Chopra and LeCun, "Dimensionality Reduction by Learning an Invariant Mapping", CVPR 2006. https://cs.nyu.edu/~sumit/publications/assets/cvpr06.pdf (accessed 2026-11-17)
[^s2]: van den Oord, Li and Vinyals, "Representation Learning with Contrastive Predictive Coding", arXiv 1807.03748 (2018). https://ar5iv.labs.arxiv.org/html/1807.03748 (accessed 2026-11-17)
[^s3]: Chen, Kornblith, Norouzi and Hinton, "A Simple Framework for Contrastive Learning of Visual Representations", ICML 2020, PMLR 119. https://proceedings.mlr.press/v119/chen20j.html (accessed 2026-11-17)
[^s4]: Chen, Kornblith, Norouzi and Hinton, SimCLR full text, arXiv 2002.05709. https://arxiv.org/pdf/2002.05709 (accessed 2026-11-17)
[^s5]: He, Fan, Wu, Xie and Girshick, "Momentum Contrast for Unsupervised Visual Representation Learning", CVPR 2020. https://openaccess.thecvf.com/content_CVPR_2020/html/He_Momentum_Contrast_for_Unsupervised_Visual_Representation_Learning_CVPR_2020_paper.html (accessed 2026-11-17)
[^s6]: Radford et al., "Learning Transferable Visual Models From Natural Language Supervision", ICML 2021, PMLR 139. https://proceedings.mlr.press/v139/radford21a.html (accessed 2026-11-17)
