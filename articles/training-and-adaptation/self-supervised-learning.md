---
id: kt:self-supervised-learning
type: Paradigm
title: Self-supervised learning
aliases: [SSL (self-supervised learning), self-supervision, self-supervised representation learning]
domain: training-and-adaptation
summary: >-
  A learning paradigm in which a model is trained on unlabeled data with a pretext task whose targets are
  derived automatically from the data itself, such as predicting masked tokens or matching augmented views,
  so that it learns representations that transfer to downstream tasks.
maturity: established
broader: [kt:representation-learning, kt:machine-learning]
related: [kt:unsupervised-learning, kt:transfer-learning, kt:large-language-model, kt:bert]
relations:
  - {predicate: enables, object: kt:pretraining}
  - {predicate: hasPart, object: kt:contrastive-learning}
  - {predicate: hasPart, object: kt:masked-language-modeling}
  - {predicate: contrastsWith, object: kt:supervised-learning}
  - {predicate: enables, object: kt:foundation-model}
sources:
  - id: s1
    title: "A Cookbook of Self-Supervised Learning"
    publisher: arXiv 2304.12210 (Balestriero, Ibrahim, Sobal, Morcos, ..., LeCun, Goldblum), 2023
    url: https://arxiv.org/abs/2304.12210
    type: primary
    accessed: 2026-11-16
  - id: s2
    title: "Self-supervised learning: The dark matter of intelligence"
    publisher: Meta AI blog (Yann LeCun and Ishan Misra), 4 March 2021
    url: https://ai.meta.com/blog/self-supervised-learning-the-dark-matter-of-intelligence/
    type: lab-research
    accessed: 2026-11-16
  - id: s3
    title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
    publisher: NAACL-HLT 2019, pp. 4171–4186 (Devlin, Chang, Lee and Toutanova), ACL Anthology N19-1423
    url: https://aclanthology.org/N19-1423/
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s4
    title: "Unsupervised Visual Representation Learning by Context Prediction"
    publisher: ICCV 2015 (Doersch, Gupta and Efros), CVF Open Access
    url: https://openaccess.thecvf.com/content_iccv_2015/html/Doersch_Unsupervised_Visual_Representation_ICCV_2015_paper.html
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "A Cookbook of Self-Supervised Learning (HTML rendering of arXiv 2304.12210)"
    publisher: ar5iv, arXiv Labs
    url: https://ar5iv.labs.arxiv.org/html/2304.12210
    type: primary
    accessed: 2026-11-16
created: 2026-11-16
---

# Self-supervised learning

**Self-supervised learning (SSL)** trains a model on unlabeled data by hiding or transforming part of each input and asking the model to recover or match it. The supervisory signal comes from the data itself rather than from human annotators: a language model predicts masked words, a video model predicts future frames, an image model predicts how patches fit together.[^s2] LeCun and Misra argue that "unsupervised" is a misleading name for this, because the model receives far more feedback per example than in standard supervised or reinforcement learning.[^s2] The goal is usually not the pretext task itself but the **representations** the model learns along the way, which are then reused for downstream tasks with little labeled data.[^s1][^s5]

## Origins and pretext tasks

Early SSL in vision designed hand-crafted *pretext tasks*. Doersch, Gupta and Efros (ICCV 2015) sampled pairs of patches from unlabeled images and trained a convolutional network to predict the second patch's position relative to the first; because the label comes from the image's own layout, no annotation is needed, and the authors argued the task forces the network to recognise objects and their parts.[^s4] Initialising R-CNN with these features gave a substantial gain over random initialisation on Pascal VOC detection.[^s4] The SSL cookbook by Balestriero et al. (2023) surveys this pre-2020 era, listing colorization of grayscale images, inpainting of masked regions, rotation prediction (RotNet), jigsaw puzzles, counting, video-based tasks and clustering.[^s5]

In language, the decisive step was **BERT** (Devlin et al., NAACL 2019). Its masked language model selects 15% of tokens in each sequence, replaces most of them with a [MASK] symbol (80%, with 10% random tokens and 10% unchanged), and trains the network to predict the originals; a second task predicts whether one sentence actually follows another.[^s3] Pretrained this way on BooksCorpus (about 800M words) and English Wikipedia (about 2,500M words), BERT could be fine-tuned with a single extra output layer and raised the GLUE score to 80.5, a 7.7-point absolute gain at the time.[^s3]

## How modern methods work

The cookbook groups post-2020 SSL into four families.[^s5] **Deep metric learning** methods such as SimCLR build positive pairs from two augmentations of the same input, treat other samples as negatives, and optimise a contrastive InfoNCE loss through a projector MLP.[^s5] **Self-distillation** methods such as BYOL and DINO drop explicit negatives, training a student network with a predictor to match targets produced by a momentum ("teacher") copy of itself.[^s5] **Canonical correlation analysis** methods such as VICReg and Barlow Twins regularise the statistics of the embeddings instead, and **masked image modeling** reconstructs hidden patches, extending the older inpainting idea.[^s5]

The joint-embedding methods share one failure mode. LeCun and Misra describe them as twin networks whose output distance acts as an energy: training pulls embeddings of distorted views of the same image together, but without a safeguard both networks can emit the same vector for every input, a **collapse** that makes the energy useless.[^s2] Contrastive methods prevent this by pushing apart chosen negative pairs, which the authors consider inefficient in high-dimensional spaces; non-contrastive methods (SwAV, SimSiam, BYOL, Barlow Twins and others) avoid collapse by other means.[^s2] They also explain why SSL advanced faster in text than in images: a finite vocabulary lets a softmax express uncertainty over every candidate masked word, whereas continuous, high-dimensional image patches admit effectively infinite plausible completions.[^s2]

## Evidence, limitations and practice

Evidence that SSL can match labeled pretraining comes from scale. Meta's SEER, a SwAV-trained ConvNet described in 2021 as having about a billion parameters, was pretrained on roughly one billion random, unlabeled public Instagram images and reached 84.2% ImageNet top-1 accuracy after fine-tuning, a figure Meta reported as ahead of earlier self-supervised systems.[^s2] Representations are typically judged by linear probing or k-nearest-neighbour accuracy on a labeled benchmark, and features taken before the projector head often transfer better.[^s5]

The cookbook's authors stress that SSL remains hard to reproduce: they call training it a delicate art with a high barrier to entry, because many hyperparameters, from the choice of augmentations to the projector design, shape the final representation and are often under-documented.[^s1][^s5] There is also no single objective that dominates across modalities; the methods above encode different assumptions about which invariances a good representation should have.[^s5] In practice, self-supervised objectives underpin almost all large-scale pretraining today: next-token or masked-token prediction for language models, and contrastive, distillation or masked-patch objectives for vision backbones.[^s1][^s3]

## Connections

Self-supervised learning is a branch of **representation learning** within **machine learning**, and it **contrasts with** **supervised learning**, which needs human labels, while overlapping with **unsupervised learning** in using unlabeled data.[^s2] It is the objective behind **pretraining**, which it **enables**, and hence a key ingredient of **transfer learning**, **large language models** and **foundation models**.[^s1][^s3] **BERT** popularised **masked language modeling**, one of its main forms, and **contrastive learning** is another of its families.[^s3][^s5]

## Sources

[^s1]: Balestriero et al., "A Cookbook of Self-Supervised Learning", arXiv 2304.12210 (2023). https://arxiv.org/abs/2304.12210 (accessed 2026-11-16)
[^s2]: LeCun and Misra, "Self-supervised learning: The dark matter of intelligence", Meta AI blog, 4 March 2021. https://ai.meta.com/blog/self-supervised-learning-the-dark-matter-of-intelligence/ (accessed 2026-11-16)
[^s3]: Devlin, Chang, Lee and Toutanova, "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", NAACL-HLT 2019. https://aclanthology.org/N19-1423/ (accessed 2026-11-16)
[^s4]: Doersch, Gupta and Efros, "Unsupervised Visual Representation Learning by Context Prediction", ICCV 2015. https://openaccess.thecvf.com/content_iccv_2015/html/Doersch_Unsupervised_Visual_Representation_ICCV_2015_paper.html (accessed 2026-11-16)
[^s5]: Balestriero et al., "A Cookbook of Self-Supervised Learning", full text via ar5iv. https://ar5iv.labs.arxiv.org/html/2304.12210 (accessed 2026-11-16)
