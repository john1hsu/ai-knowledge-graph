---
id: kt:residual-connection
type: Technique
title: Residual connection
aliases: [skip connection, shortcut connection, identity shortcut, residual block, residual learning]
domain: deep-learning
summary: >-
  An architectural shortcut that adds a block's input directly to the block's output, so the stacked layers
  learn only a residual correction F(x) = H(x) − x; introduced in ResNets by He et al. (CVPR 2016), it made
  networks of hundreds of layers trainable and is now a standard part of transformers.
maturity: established
broader: [kt:deep-learning, kt:artificial-neural-network]
related: [kt:batch-normalization, kt:layer-normalization, kt:convolutional-neural-network, kt:image-classification, kt:highway-network]
relations:
  - {predicate: introducedIn, object: kt:deep-residual-learning-for-image-recognition}
  - {predicate: createdBy, object: kt:microsoft-research}
  - {predicate: influencedBy, object: kt:highway-network}
  - {predicate: mitigates, object: kt:vanishing-gradient-problem}
  - {predicate: usedIn, object: kt:convolutional-neural-network}
  - {predicate: usedIn, object: kt:transformer-architecture}
sources:
  - id: s1
    title: "Deep Residual Learning for Image Recognition"
    publisher: CVPR 2016, pp. 770–778 (He, Zhang, Ren and Sun)
    url: https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s2
    title: "Deep Residual Learning for Image Recognition (arXiv 1512.03385v1, full text)"
    publisher: arXiv / ar5iv (He, Zhang, Ren and Sun, Microsoft Research)
    url: https://ar5iv.labs.arxiv.org/html/1512.03385v1
    type: primary
    accessed: 2026-11-14
  - id: s3
    title: "Identity Mappings in Deep Residual Networks"
    publisher: arXiv 1603.05027 (He, Zhang, Ren and Sun, 2016)
    url: https://arxiv.org/abs/1603.05027v3
    type: primary
    accessed: 2026-11-14
  - id: s4
    title: "Residual Networks Behave Like Ensembles of Relatively Shallow Networks"
    publisher: NeurIPS 2016 (Veit, Wilber and Belongie)
    url: https://proceedings.neurips.cc/paper/2016/hash/37bc2f75bf1bcfe8450a1a41c200364c-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "8.6. Residual Networks (ResNet) and ResNeXt"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola)
    url: https://d2l.ai/chapter_convolutional-modern/resnet.html
    type: textbook
    accessed: 2026-11-14
  - id: s6
    title: "On Layer Normalization in the Transformer Architecture"
    publisher: ICML 2020 (Xiong et al.), Microsoft Research publication page
    url: https://www.microsoft.com/en-us/research/publication/on-layer-normalization-in-the-transformer-architecture/
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s7
    title: "Highway Networks"
    publisher: arXiv 1505.00387 (Srivastava, Greff and Schmidhuber, 2015)
    url: https://arxiv.org/abs/1505.00387v2
    type: primary
    accessed: 2026-11-14
created: 2026-11-14
---

# Residual connection

A **residual connection** (also called a skip or shortcut connection) routes a block's input around the block and adds it to the block's output. If the desired mapping of a few stacked layers is H(x), the layers are asked to learn only the residual F(x) = H(x) − x, and the block emits F(x) + x.[^s2] Kaiming He, Xiangyu Zhang, Shaoqing Ren and Jian Sun of Microsoft Research introduced the idea in their residual networks (ResNets), published at CVPR 2016, where it let them train image classifiers up to 152 layers deep.[^s1][^s2]

## Origin: the degradation problem

The motivation was not overfitting but optimisation. He et al. observed that adding layers to an already deep "plain" network made its *training* error go up: on ImageNet their 34-layer plain network had higher top-1 error (28.54%) than an 18-layer one (27.94%).[^s2] A deeper network could in principle copy the shallower one and set the extra layers to the identity, so the failure pointed to the solver struggling to fit identity mappings through stacks of nonlinear layers. Their hypothesis was that driving a residual toward zero is easier than learning an identity from scratch.[^s2] The *Dive into Deep Learning* textbook frames the same argument through nested function classes: a bigger model is only guaranteed to be at least as good if its function class contains the smaller one, and a residual block makes the identity the easy default for every added layer.[^s5]

## How it works

In the simplest form the shortcut is a parameter-free identity, so it adds no weights and almost no computation, which let the authors compare plain and residual networks of equal depth, width and parameter count.[^s2] When a block changes the number of channels or the spatial resolution, the shortcut must be reshaped before the addition; the paper compared zero-padding, projections only where dimensions grow, and projections everywhere, and found the differences small.[^s2] In practice a 1×1 convolution, optionally with stride 2, serves as that projection.[^s5] A basic block stacks two 3×3 convolutions, each followed by batch normalization, and adds the input before the final ReLU; deeper ResNets use a "bottleneck" block of 1×1, 3×3 and 1×1 convolutions to keep cost down.[^s5][^s2]

Gradients benefit directly. Differentiating F(x) + x gives the block's own Jacobian plus the identity, so a gradient signal always has an unattenuated path back to earlier layers. He et al.'s follow-up paper showed that when the shortcut is a pure identity and the activation is moved out of the post-addition path, forward and backward signals can propagate directly between any two blocks; their reworked "pre-activation" unit trained a 1001-layer ResNet to 4.62% error on CIFAR-10.[^s3]

## Evidence and results

The residual networks were striking in 2015–2016: a 152-layer ResNet was eight times deeper than VGG yet cheaper, an ensemble reached 3.57% top-5 error on the ImageNet test set to win the ILSVRC 2015 classification task, and the same backbones won the ImageNet detection and localization and COCO detection and segmentation tracks.[^s1] Depth alone was not a free lunch, though: on CIFAR-10 a 1202-layer ResNet trained successfully but tested worse (7.93% error) than a 110-layer one (6.43%) despite having roughly eleven times the parameters (19.4M vs 1.7M).[^s2]

Why residual networks work is still debated. Veit, Wilber and Belongie (NeurIPS 2016) "unravelled" a ResNet into many paths of different lengths and found it behaves like an ensemble of fairly independent, mostly short paths; in a 110-layer network most of the gradient flowed through paths only 10–34 layers deep.[^s4] That suggests residual connections avoid vanishing gradients less by making very long paths trainable than by keeping short ones available.[^s4]

## In practice

Residual connections spread far beyond image models. The d2l textbook lists their use in residual LSTMs, graph neural networks, detectors such as YOLOv3 and Faster R-CNN, and transformers, which rely on them to stack many layers.[^s5] In transformers the placement of normalization relative to the residual path matters: Xiong et al. (ICML 2020) showed that putting layer normalization after the addition (Post-LN) creates large gradients near the output at initialization and demands a learning-rate warm-up, while placing it inside the residual branch (Pre-LN) keeps gradients well behaved and lets warm-up be dropped.[^s6]

## Connections

Residual connections are a technique of **deep learning** applied to **artificial neural networks**, **introduced in** *Deep Residual Learning for Image Recognition* and **created by** researchers at **Microsoft Research**.[^s1][^s2] They were **influenced by** **highway networks** (Srivastava, Greff and Schmidhuber, 2015), which used learned gates to let information flow across hundreds of layers; ResNet's shortcuts differ by having no parameters and never closing.[^s7][^s2] They **mitigate** the **vanishing gradient problem** by giving gradients short, identity paths.[^s3][^s4] They are **used in** **convolutional neural networks** for **image classification**, usually paired with **batch normalization**, and **used in** the **transformer architecture**, where their interplay with **layer normalization** governs training stability.[^s5][^s6]

## Sources
[^s1]: He, Zhang, Ren and Sun, "Deep Residual Learning for Image Recognition", CVPR 2016. https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html (accessed 2026-11-14)
[^s2]: He, Zhang, Ren and Sun, "Deep Residual Learning for Image Recognition", arXiv 1512.03385v1 (ar5iv full text). https://ar5iv.labs.arxiv.org/html/1512.03385v1 (accessed 2026-11-14)
[^s3]: He, Zhang, Ren and Sun, "Identity Mappings in Deep Residual Networks", arXiv 1603.05027v3, 2016. https://arxiv.org/abs/1603.05027v3 (accessed 2026-11-14)
[^s4]: Veit, Wilber and Belongie, "Residual Networks Behave Like Ensembles of Relatively Shallow Networks", NeurIPS 2016. https://proceedings.neurips.cc/paper/2016/hash/37bc2f75bf1bcfe8450a1a41c200364c-Abstract.html (accessed 2026-11-14)
[^s5]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, §8.6 "Residual Networks (ResNet) and ResNeXt". https://d2l.ai/chapter_convolutional-modern/resnet.html (accessed 2026-11-14)
[^s6]: Xiong et al., "On Layer Normalization in the Transformer Architecture", ICML 2020. https://www.microsoft.com/en-us/research/publication/on-layer-normalization-in-the-transformer-architecture/ (accessed 2026-11-14)
[^s7]: Srivastava, Greff and Schmidhuber, "Highway Networks", arXiv 1505.00387v2, 2015. https://arxiv.org/abs/1505.00387v2 (accessed 2026-11-14)
