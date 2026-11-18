---
id: kt:zero-shot-learning
type: Paradigm
title: Zero-shot learning
aliases: [ZSL, zero-data learning, generalized zero-shot learning]
domain: training-and-adaptation
summary: >-
  A learning setting in which a model must recognise classes (or perform tasks) for which it saw no labelled training
  examples, by mapping inputs into an auxiliary semantic space, such as attributes, word vectors or natural-language
  descriptions, that also describes the unseen classes.
maturity: established
broader: [kt:transfer-learning, kt:machine-learning]
related: [kt:zero-shot-prompting, kt:embeddings, kt:image-classification, kt:few-shot-learning, kt:in-context-learning]
relations:
  - {predicate: introducedIn, object: kt:zero-shot-learning-with-semantic-output-codes}
  - {predicate: dependsOn, object: kt:representation-learning}
  - {predicate: hasPart, object: kt:attribute-based-classification}
  - {predicate: usedIn, object: kt:clip}
  - {predicate: evaluatedOn, object: kt:animals-with-attributes}
  - {predicate: contrastsWith, object: kt:supervised-learning}
sources:
  - id: s1
    title: "Zero-shot Learning with Semantic Output Codes"
    publisher: NIPS 2009, Advances in Neural Information Processing Systems 22 (Palatucci, Pomerleau, Hinton and Mitchell)
    url: https://proceedings.neurips.cc/paper_files/paper/2009/file/1543843a4723ed2ab08e18053ae6dc5b-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "Learning to detect unseen object classes by between-class attribute transfer"
    publisher: CVPR 2009, pp. 951–958, doi:10.1109/CVPR.2009.5206594 (Lampert, Nickisch and Harmeling); ISTA Research Explorer record
    url: https://research-explorer.ista.ac.at/record/3704
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "Zero-Shot Learning Through Cross-Modal Transfer"
    publisher: NeurIPS 2013, Advances in Neural Information Processing Systems 26 (Socher, Ganjoo, Manning and Ng)
    url: https://proceedings.neurips.cc/paper_files/paper/2013/file/2d6cc4b2d139a53512fb8cbb3086ae2e-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Zero-Shot Learning - The Good, the Bad and the Ugly"
    publisher: CVPR 2017, pp. 4582–4591 (Xian, Schiele and Akata), CVF Open Access
    url: https://openaccess.thecvf.com/content_cvpr_2017/html/Xian_Zero-Shot_Learning_-_CVPR_2017_paper.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s5
    title: "Zero-Shot Learning - A Comprehensive Evaluation of the Good, the Bad and the Ugly (benchmark page)"
    publisher: Max Planck Institute for Informatics, Computer Vision and Machine Learning department
    url: https://mpi-inf.mpg.de/zsl-benchmark
    type: academic
    accessed: 2026-11-18
  - id: s6
    title: "Learning Transferable Visual Models From Natural Language Supervision"
    publisher: ICML 2021, PMLR 139:8748–8763 (Radford et al.)
    url: https://proceedings.mlr.press/v139/radford21a.html
    type: peer-reviewed
    accessed: 2026-11-18
created: 2026-11-18
---

# Zero-shot learning

**Zero-shot learning (ZSL)** asks a model to predict classes that were deliberately left out of its training data.[^s1] Because no labelled examples of those classes exist, the model cannot learn them directly; instead it learns to map inputs into an intermediate *semantic* space, such as a set of human-interpretable attributes, word vectors or text descriptions, in which every class, seen or unseen, has a description. A new class can then be recognised as long as its description is available.[^s1][^s2] It is a special case of transfer learning in which the knowledge carried over from training classes is a mapping into a shared description space rather than a classifier for the target labels themselves.

## Origin

Two 2009 papers established the setting. Palatucci, Pomerleau, Hinton and Mitchell introduced the **semantic output code** classifier at NIPS 2009.[^s1] It composes two functions: one maps raw input to a vector of semantic features (properties such as whether a thing is manmade or can be held), and a second maps that vector to the nearest class in a knowledge base of class descriptions.[^s1] They gave a PAC-style analysis of when such a classifier can correctly predict a class it never saw, which they presented as the first formal guarantee of this kind.[^s1] In parallel, Lampert, Nickisch and Harmeling at CVPR 2009 proposed **attribute-based classification** for object recognition, replacing training images of a target class with a human-specified description of it in terms of attributes such as shape, colour or habitat.[^s2] Because attributes are shared across classes, they can be learned beforehand from other images and then combined to detect novel classes without retraining.[^s2] To test this they built the **Animals with Attributes** dataset: over 30,000 images of 50 animal classes, each annotated against 85 semantic attributes.[^s2]

## How it works

The general recipe has three parts.[^s1][^s3]

1. **A semantic space** that describes every class. Palatucci et al. compared crowdsourced answers to 218 questions per word with co-occurrence statistics from a large web corpus.[^s1] Socher and colleagues later used unsupervised word vectors, arguing this removes the need for manually defined attributes.[^s3]
2. **A learned mapping** from inputs to that space, trained only on seen classes. Socher et al. trained a two-layer network to project image features near the word vector of each image's class.[^s3]
3. **An inference rule** that assigns the nearest (or most likely) class description, including descriptions of classes absent from training.[^s1][^s3]

Palatucci et al. demonstrated this on brain imaging: models decoding fMRI scans of nine participants viewing 60 concrete words identified which of two held-out words was being viewed with mean accuracy of 80.9% using the crowdsourced features, against 50% chance.[^s1]

## Generalized zero-shot learning

The classic protocol tests only on unseen classes, which is unrealistic: deployed systems meet seen and unseen classes together. Socher et al. tackled this mixed setting in 2013 by first deciding whether an image is novel, then routing it to a standard softmax classifier or to the zero-shot classifier.[^s3] On CIFAR-10 with cat and truck held out, their pipeline reached 74.25% overall accuracy versus 45.25% for an attribute baseline, but results depended heavily on which classes were held out.[^s3] Xian, Schiele and Akata called this setting **generalized zero-shot learning** and argued it is the more realistic test.[^s4]

## Limitations and evaluation problems

By 2017 the field had grown quickly without an agreed benchmark, and Xian et al. found published numbers often incomparable and sometimes flawed, for example when a feature extractor had been pretrained on the very classes meant to be unseen.[^s4][^s5] They released unified splits for standard datasets (including CUB, SUN, aPY and a new AWA2) and compared many methods under both classic and generalized protocols.[^s5] The broader lessons are that ZSL performance depends on the quality of the semantic descriptions and on how well the input-to-semantics mapping generalises, and that in the generalized setting, deciding whether an input is novel is itself a trade-off: Socher et al. found a liberal novelty detector raised unseen-class accuracy while a conservative one better preserved seen-class accuracy.[^s3][^s4]

## In practice: from attributes to language

Large-scale pretraining changed how zero-shot recognition is done. CLIP (Radford et al., ICML 2021) learned from 400 million internet image–text pairs by predicting which caption goes with which image; at test time, class names written as text become the classifier, so the model can be applied to new label sets without task-specific training.[^s6] The authors reported that zero-shot CLIP matched the accuracy of the original ResNet-50 on ImageNet without using any of its 1.28 million training images, and evaluated transfer on over 30 vision datasets.[^s6] In this view, free-form natural language replaces hand-built attribute tables as the semantic space. A caveat carries over from Xian et al.: with web-scale pretraining it is hard to guarantee that test classes were truly unseen.[^s4][^s6]

## Connections

Zero-shot learning is a form of **transfer learning** within **machine learning**, and it contrasts with **supervised learning**, which requires labelled examples of every class it predicts.[^s1] It was introduced in the semantic-output-codes paper and in **attribute-based classification**, and is classically evaluated on **Animals with Attributes**.[^s1][^s2] It depends on **representation learning** and **embeddings** that place inputs and class descriptions in one space.[^s3] **Image classification** is its home task, and **CLIP** is its best-known modern instance.[^s6] **Few-shot learning** relaxes it by allowing a handful of examples, and in language models the same idea appears as **zero-shot prompting** and **in-context learning**, where a task description stands in for training data.[^s6]

## Sources

[^s1]: Palatucci, Pomerleau, Hinton and Mitchell, "Zero-shot Learning with Semantic Output Codes", NIPS 2009. https://proceedings.neurips.cc/paper_files/paper/2009/file/1543843a4723ed2ab08e18053ae6dc5b-Paper.pdf (accessed 2026-11-18)
[^s2]: Lampert, Nickisch and Harmeling, "Learning to detect unseen object classes by between-class attribute transfer", CVPR 2009. https://research-explorer.ista.ac.at/record/3704 (accessed 2026-11-18)
[^s3]: Socher, Ganjoo, Manning and Ng, "Zero-Shot Learning Through Cross-Modal Transfer", NeurIPS 2013. https://proceedings.neurips.cc/paper_files/paper/2013/file/2d6cc4b2d139a53512fb8cbb3086ae2e-Paper.pdf (accessed 2026-11-18)
[^s4]: Xian, Schiele and Akata, "Zero-Shot Learning - The Good, the Bad and the Ugly", CVPR 2017. https://openaccess.thecvf.com/content_cvpr_2017/html/Xian_Zero-Shot_Learning_-_CVPR_2017_paper.html (accessed 2026-11-18)
[^s5]: Max Planck Institute for Informatics, "Zero-Shot Learning - A Comprehensive Evaluation of the Good, the Bad and the Ugly" benchmark page. https://mpi-inf.mpg.de/zsl-benchmark (accessed 2026-11-18)
[^s6]: Radford et al., "Learning Transferable Visual Models From Natural Language Supervision", ICML 2021. https://proceedings.mlr.press/v139/radford21a.html (accessed 2026-11-18)
