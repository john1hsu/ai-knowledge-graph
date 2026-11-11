---
id: kt:imagenet-and-alexnet
type: Event
title: ImageNet and AlexNet
aliases: [AlexNet, SuperVision (ILSVRC-2012 entry), ImageNet moment, ILSVRC 2012 breakthrough]
domain: ai-history
summary: >-
  The 2012 turning point when AlexNet, a GPU-trained deep convolutional network by Krizhevsky, Sutskever and
  Hinton, won the ImageNet Large Scale Visual Recognition Challenge with a 15.3% top-5 error against 26.2% for the
  runner-up, showing that features learned from a very large labeled dataset could beat hand-engineered vision pipelines.
maturity: historical
broader: [kt:deep-learning, kt:convolutional-neural-network]
related: [kt:image-classification, kt:dropout, kt:algorithmic-bias-and-fairness, kt:yolo]
relations:
  - {predicate: createdBy, object: kt:geoffrey-hinton}
  - {predicate: introducedIn, object: kt:imagenet-classification-with-deep-convolutional-neural-networks}
  - {predicate: evaluatedOn, object: kt:imagenet-large-scale-visual-recognition-challenge}
  - {predicate: runsOn, object: kt:gpu-computing}
  - {predicate: implementedIn, object: kt:cuda}
  - {predicate: influencedBy, object: kt:lenet}
sources:
  - id: s1
    title: "ImageNet Classification with Deep Convolutional Neural Networks"
    publisher: NIPS 2012 (Krizhevsky, Sutskever and Hinton), abstract page
    url: https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "ImageNet Classification with Deep Convolutional Neural Networks (full paper)"
    publisher: NIPS 2012 proceedings PDF (Krizhevsky, Sutskever and Hinton)
    url: https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "ImageNet: A Large-Scale Hierarchical Image Database"
    publisher: CVPR 2009 (Deng, Dong, Socher, Li, Li and Fei-Fei), via ML Anthology
    url: https://mlanthology.org/cvpr/2009/deng2009cvpr-imagenet
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "ImageNet Large Scale Visual Recognition Challenge"
    publisher: Russakovsky et al., International Journal of Computer Vision 2015 (authors' arXiv version 1409.0575)
    url: https://arxiv.org/pdf/1409.0575
    type: primary
    accessed: 2026-11-11
  - id: s5
    title: "8.1. Deep Convolutional Neural Networks (AlexNet)"
    publisher: Dive into Deep Learning (d2l.ai)
    url: https://d2l.ai/chapter_convolutional-modern/alexnet.html
    type: textbook
    accessed: 2026-11-11
  - id: s6
    title: "Towards Fairer Datasets: Filtering and Balancing the Distribution of the People Subtree in the ImageNet Hierarchy"
    publisher: Yang, Qinami, Fei-Fei, Deng and Russakovsky, FAT* 2020 (ImageNet project page)
    url: https://image-net.org/filtering-and-balancing/
    type: peer-reviewed
    accessed: 2026-11-11
created: 2026-11-11
---

# ImageNet and AlexNet

**ImageNet and AlexNet** names the pairing of a dataset and a model that, in 2012, convinced most of computer vision to switch to deep learning. ImageNet supplied more than a million labeled, high-resolution images across 1,000 classes for an annual benchmark; AlexNet, a deep convolutional neural network trained on two GPUs, won that benchmark by a margin large enough to reset the field's methods.[^s2][^s4] The network was entered in the challenge under the team name SuperVision.[^s4]

## Origin

ImageNet was introduced at CVPR 2009 by Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li and Li Fei-Fei. It organizes images under WordNet's noun hierarchy, aiming to illustrate most of WordNet's roughly 80,000 synsets with 500 to 1,000 clean images each; the first release already held 3.2 million images in 5,247 synsets, and labels were verified with crowd workers on Amazon Mechanical Turk.[^s3] From 2010 to 2014 the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) used a 1,000-class subset with about 1.2 million training, 50,000 validation and 100,000 test images, scored from 2012 onward mainly by top-5 error, in which a system may name five labels per image.[^s4]

Before 2012, the leading vision systems combined hand-engineered descriptors such as SIFT and SURF with shallow classifiers, while kernel and ensemble methods often outperformed neural networks; Dive into Deep Learning argues that the missing ingredients for deep networks were large datasets and affordable parallel hardware.[^s5] ImageNet supplied the first and consumer GPUs the second.[^s5]

## The model and how it worked

Alex Krizhevsky, Ilya Sutskever and Geoffrey Hinton, all at the University of Toronto, described AlexNet in a NIPS 2012 paper. The network had about 60 million parameters and 650,000 neurons, arranged as five convolutional layers, some followed by max pooling, and three fully connected layers ending in a 1,000-way softmax.[^s1] Several design choices became standard:[^s2]

- **ReLU activations.** Rectified linear units let a four-layer test network reach 25% training error on CIFAR-10 six times faster than an equivalent tanh network.[^s2]
- **Dropout.** Hidden units in the first two fully connected layers were zeroed with probability 0.5 during training to curb overfitting, at the cost of roughly doubling the iterations to converge.[^s2]
- **Data augmentation.** Random 224×224 crops and horizontal flips of 256×256 images, plus PCA-based colour jitter, enlarged the effective training set; the colour scheme alone cut top-1 error by over 1%.[^s2]
- **GPU training.** The net was split across two NVIDIA GTX 580 GPUs with 3 GB each and trained for five to six days, about 90 passes over the training set.[^s2]

The paper also used local response normalization and overlapping 3×3 pooling with stride 2, each worth a fraction of a percentage point to a little over one point of error, and reported that removing any single convolutional layer hurt accuracy even though each held at most 1% of the parameters, an early argument that depth itself mattered.[^s2] Compared with LeNet, the textbook view is that AlexNet was mainly much larger and deeper, with ReLU in place of sigmoid, dropout in place of weight decay alone, and far heavier augmentation.[^s5]

## Results and impact

On the ILSVRC-2010 test set the network reached 37.5% top-1 and 17.0% top-5 error, well ahead of the previous best published results.[^s2] In ILSVRC-2012 a seven-network ensemble scored 15.3% top-5 test error against 26.2% for the second-best entry; the challenge organisers' own retrospective lists the figures as 16.42% for SuperVision against 26.17% for the ISI team.[^s2][^s4] Russakovsky et al. describe 2012 as a turning point: by 2014 nearly every top entry used convolutional networks, and classification error had fallen from 28.2% in 2010 to 6.7% with GoogLeNet.[^s4] In their comparison on a 1,500-image sample, one trained human annotator still did better, at 5.1% top-5 error against GoogLeNet's 6.8%.[^s4]

## Critiques and limitations

ImageNet's reliance on WordNet also carried problems. A 2020 study by members of the ImageNet team examined the dataset's "person" subtree and identified three sources of harm: a stagnant concept vocabulary inherited from WordNet, the attempt to illustrate every concept with images even when a concept is not visual, and unequal representation of people within categories; the authors proposed filtering and rebalancing as first steps.[^s6] The challenge organisers' retrospective answers other criticisms: that objects are often large and centred, which they dispute by comparison with PASCAL VOC; that crowd labels contain errors, concentrated in fine-grained classes such as bird species, though they estimate 99.7% label precision; and that rules on outside training data were hard to define, which led to separate tracks in 2014. They also note that accuracy stayed weaker on small, thin and untextured man-made objects.[^s4]

## Connections

The event sits under **deep learning** and **convolutional neural networks**, the paradigm and architecture it popularised.[^s5] It was **created by** a team including **Geoffrey Hinton**, **introduced in** the 2012 NIPS paper, and **evaluated on** the **ILSVRC** benchmark.[^s1][^s4] It **ran on** **GPU computing** and was **implemented in** **CUDA**, and it was **influenced by** **LeNet**, the earlier convolutional network it scaled up.[^s2][^s5] It is related to **image classification**, the task it transformed; to **dropout**, which it brought into wide use; to **YOLO** and later vision models built on its methods; and to **algorithmic bias and fairness**, through the critiques of ImageNet's person categories.[^s2][^s6]

## Sources
[^s1]: Krizhevsky, Sutskever and Hinton, "ImageNet Classification with Deep Convolutional Neural Networks", NIPS 2012 (abstract). https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html (accessed 2026-11-11)
[^s2]: Krizhevsky, Sutskever and Hinton, "ImageNet Classification with Deep Convolutional Neural Networks", NIPS 2012 (full paper). https://papers.nips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf (accessed 2026-11-11)
[^s3]: Deng et al., "ImageNet: A Large-Scale Hierarchical Image Database", CVPR 2009. https://mlanthology.org/cvpr/2009/deng2009cvpr-imagenet (accessed 2026-11-11)
[^s4]: Russakovsky et al., "ImageNet Large Scale Visual Recognition Challenge", IJCV 2015 (arXiv 1409.0575). https://arxiv.org/pdf/1409.0575 (accessed 2026-11-11)
[^s5]: Dive into Deep Learning, §8.1 "Deep Convolutional Neural Networks (AlexNet)". https://d2l.ai/chapter_convolutional-modern/alexnet.html (accessed 2026-11-11)
[^s6]: Yang et al., "Towards Fairer Datasets", FAT* 2020. https://image-net.org/filtering-and-balancing/ (accessed 2026-11-11)
