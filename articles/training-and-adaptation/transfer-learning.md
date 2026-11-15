---
id: kt:transfer-learning
type: Paradigm
title: Transfer learning
aliases: [inductive transfer, knowledge transfer (machine learning)]
domain: training-and-adaptation
summary: >-
  A machine-learning paradigm that improves learning on a target task or domain by reusing knowledge (instances,
  features or parameters) acquired on a different but related source task or domain, reducing the labelled target
  data needed.
maturity: established
broader: [kt:machine-learning]
related: [kt:pretraining, kt:fine-tuning, kt:parameter-efficient-fine-tuning, kt:imagenet-and-alexnet]
relations:
  - {predicate: hasPart, object: kt:domain-adaptation}
  - {predicate: dependsOn, object: kt:representation-learning}
  - {predicate: enables, object: kt:foundation-model}
  - {predicate: causes, object: kt:negative-transfer}
  - {predicate: contrastsWith, object: kt:multi-task-learning}
sources:
  - id: s1
    title: "A Survey on Transfer Learning"
    publisher: IEEE Transactions on Knowledge and Data Engineering, doi:10.1109/TKDE.2009.191 (Pan and Yang); authors' copy, HKUST
    url: https://www.cse.ust.hk/%7eqyang/Docs/2009/tkde_transfer_learning.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s2
    title: "How transferable are features in deep neural networks?"
    publisher: NeurIPS 2014, Advances in Neural Information Processing Systems 27 (Yosinski, Clune, Bengio and Lipson)
    url: https://proceedings.nips.cc/paper_files/paper/2014/file/375c71349b295fbe2dcdca9206f20a06-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "A theory of learning from different domains"
    publisher: Machine Learning 79, pp. 151–175, 2010 (Ben-David, Blitzer, Crammer, Kulesza, Pereira and Vaughan); Google Research publication page
    url: https://research.google/pubs/a-theory-of-learning-from-different-domains/
    type: lab-research
    accessed: 2026-11-15
  - id: s4
    title: "14.2. Fine-Tuning"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), d2l.ai
    url: https://d2l.ai/chapter_computer-vision/fine-tuning.html
    type: textbook
    accessed: 2026-11-15
  - id: s5
    title: "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"
    publisher: Journal of Machine Learning Research 21(140):1–67, 2020 (Raffel et al.)
    url: https://www.jmlr.org/papers/v21/20-074.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s6
    title: "A Comprehensive Survey on Transfer Learning"
    publisher: arXiv 1911.02685 (Zhuang, Qi, Duan, Xi, Zhu, Zhu, Xiong and He), 2019
    url: https://arxiv.org/abs/1911.02685v1
    type: primary
    accessed: 2026-11-15
created: 2026-11-15
---

# Transfer learning

**Transfer learning** is the practice of using what a model learned on one problem (the *source*) to learn a different but related problem (the *target*) better or with less data.[^s1] Pan and Yang's widely cited survey formalises it: a *domain* is a feature space plus a marginal distribution over inputs, a *task* is a label space plus a predictive function, and transfer learning improves the target predictive function using source knowledge whenever the source and target domains or tasks differ. If both are identical, the problem collapses back into ordinary machine learning.[^s1] Unlike multi-task learning, which tries to do well on all tasks at once, transfer learning is asymmetric: the target task is what matters.[^s1]

## Origin

The survey traces the modern research agenda to a NIPS-95 workshop on "learning to learn", which emphasised lifelong methods that retain and reuse prior knowledge; the same idea has also circulated as inductive transfer, multi-task learning and meta-learning.[^s1] It notes that DARPA's Information Processing Technology Office framed the goal in 2005 as letting a system apply knowledge from earlier tasks to novel ones.[^s1]

## Settings and what gets transferred

Pan and Yang sort problems by what is labelled.[^s1]

- **Inductive transfer:** the target task differs from the source, and some labelled target data exist.[^s1]
- **Transductive transfer:** the task is the same but the domains differ, as in domain adaptation and covariate shift.[^s1]
- **Unsupervised transfer:** neither domain has labels; targets include clustering and dimensionality reduction.[^s1]

They also classify methods by *what* is transferred: re-weighted source **instances**, a shared **feature representation**, **parameters** or priors shared between models, or **relational knowledge** among data points.[^s1] A later survey by Zhuang and colleagues regroups more than forty approaches into data-based and model-based families and benchmarks over twenty of them on Amazon Reviews, Reuters-21578 and Office-31, concluding that choosing the right method for the application matters.[^s6]

## Theory: when does it work?

Ben-David and colleagues bound a source-trained classifier's error on the target domain by its source error plus a divergence between the two domains, a divergence that can be estimated from unlabelled samples alone.[^s3] They also show how to weight a mix of source and target training error: the best weighting depends on that divergence, both sample sizes and model complexity.[^s3] The intuition is that transfer helps when domains are close and a single hypothesis does well on both.

## Transfer in deep learning

Yosinski and colleagues measured layer-by-layer transferability by splitting ImageNet into two 500-class halves and swapping layers between networks trained on each.[^s2] First-layer features (Gabor-like filters and colour blobs) proved general, last-layer features task-specific.[^s2] Transfer degraded for two reasons: higher-layer neurons specialise, and cutting between co-adapted layers makes optimisation harder. The drop also grew when source and target tasks were dissimilar, such as man-made versus natural object classes.[^s2] Even so, transferred features beat random initialisation, and initialising from transferred weights then fine-tuning improved generalisation in a way that persisted through long training.[^s2]

The textbook *Dive into Deep Learning* explains the practical motivation: most real datasets sit between Fashion-MNIST's 60,000 images and ImageNet's more than ten million, and collecting ImageNet-scale labels is very expensive.[^s4] Its recipe copies a pretrained network, replaces the output layer, and trains the new head with a learning rate ten times that of the pretrained layers. On a small hot-dog dataset the fine-tuned ResNet reached about 94% test accuracy versus about 85% from scratch in the PyTorch run.[^s4]

In natural language processing, Raffel and colleagues describe pretraining on a data-rich task followed by fine-tuning on a downstream task as a powerful technique. Their T5 study cast every task as text-to-text to compare objectives, architectures, datasets and transfer approaches systematically, and released the C4 corpus.[^s5] This pretrain-then-adapt pattern is the basis of today's large pretrained models.[^s5]

## Limitations and open questions

**Negative transfer**, where source knowledge hurts the target, is the classic failure. Pan and Yang called avoiding it an important, under-studied problem and suggested measuring task relatedness to select sources.[^s1] Yosinski's results show the same risk grows with task distance.[^s2] The domain-adaptation bound makes clear why: if no single hypothesis performs well on both domains, minimising source error offers little guarantee on the target.[^s3]

## Connections

Transfer learning is a broad paradigm within **machine learning**, defined against the single-distribution setting of ordinary supervised learning.[^s1] **Pretraining** and **fine-tuning** are its dominant deep-learning workflow, and **parameter-efficient fine-tuning** is a cheaper way to do the adaptation step.[^s4][^s5] It depends on **representation learning**, since reusable general features in early layers are what make transfer possible.[^s2] **Domain adaptation** is its transductive special case, with its own theory.[^s1][^s3] It contrasts with **multi-task learning**, which treats tasks symmetrically, and its main failure mode is **negative transfer**.[^s1] ImageNet-pretrained networks (**ImageNet and AlexNet**) made transfer standard in vision, and large-scale text pretraining such as T5 extended it into the **foundation models** of today.[^s2][^s5]

## Sources

[^s1]: Pan and Yang, "A Survey on Transfer Learning", IEEE TKDE (doi:10.1109/TKDE.2009.191). https://www.cse.ust.hk/%7eqyang/Docs/2009/tkde_transfer_learning.pdf (accessed 2026-11-15)
[^s2]: Yosinski, Clune, Bengio and Lipson, "How transferable are features in deep neural networks?", NeurIPS 2014. https://proceedings.nips.cc/paper_files/paper/2014/file/375c71349b295fbe2dcdca9206f20a06-Paper.pdf (accessed 2026-11-15)
[^s3]: Ben-David et al., "A theory of learning from different domains", Machine Learning 79 (2010). https://research.google/pubs/a-theory-of-learning-from-different-domains/ (accessed 2026-11-15)
[^s4]: Zhang, Lipton, Li and Smola, "14.2. Fine-Tuning", Dive into Deep Learning. https://d2l.ai/chapter_computer-vision/fine-tuning.html (accessed 2026-11-15)
[^s5]: Raffel et al., "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", JMLR 21 (2020). https://www.jmlr.org/papers/v21/20-074.html (accessed 2026-11-15)
[^s6]: Zhuang et al., "A Comprehensive Survey on Transfer Learning", arXiv 1911.02685 (2019). https://arxiv.org/abs/1911.02685v1 (accessed 2026-11-15)
