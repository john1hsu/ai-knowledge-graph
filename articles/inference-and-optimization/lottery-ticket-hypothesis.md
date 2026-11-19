---
id: kt:lottery-ticket-hypothesis
type: Concept
title: Lottery ticket hypothesis
aliases: [LTH, winning tickets, winning lottery tickets]
domain: inference-and-optimization
summary: >-
  The conjecture, introduced by Frankle and Carbin (ICLR 2019), that a dense randomly initialized neural network
  contains sparse subnetworks ("winning tickets") that, trained in isolation from their original initial weights,
  reach accuracy comparable to the full network in a similar number of iterations.
maturity: established
broader: [kt:model-pruning]
related: [kt:model-compression, kt:weight-initialization, kt:stochastic-gradient-descent, kt:linear-mode-connectivity]
relations:
  - {predicate: introducedIn, object: kt:the-lottery-ticket-hypothesis-finding-sparse-trainable-neural-networks}
  - {predicate: createdBy, object: kt:jonathan-frankle}
  - {predicate: dependsOn, object: kt:iterative-magnitude-pruning}
sources:
  - id: s1
    title: "The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks"
    publisher: ICLR 2019 (Frankle and Carbin), conference poster page
    url: https://iclr.cc/virtual/2019/poster/972
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s2
    title: "The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks (full paper)"
    publisher: Frankle and Carbin, authors' arXiv version 1803.03635
    url: https://arxiv.org/pdf/1803.03635.pdf
    type: primary
    accessed: 2026-11-19
  - id: s3
    title: "Linear Mode Connectivity and the Lottery Ticket Hypothesis"
    publisher: ICML 2020, PMLR 119 (Frankle, Dziugaite, Roy and Carbin)
    url: https://proceedings.mlr.press/v119/frankle20a
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s4
    title: "Rethinking the Value of Network Pruning"
    publisher: ICLR 2019 (Liu, Sun, Zhou, Huang and Darrell), authors' arXiv version 1810.05270
    url: https://arxiv.org/abs/1810.05270v2
    type: primary
    accessed: 2026-11-19
  - id: s5
    title: "Deconstructing Lottery Tickets: Zeros, Signs, and the Supermask"
    publisher: NeurIPS 2019 (Zhou, Lan, Liu and Yosinski)
    url: https://papers.nips.cc/paper/2019/hash/1113d7a76ffceca1bb350bfe145467c6-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-19
created: 2026-11-19
---

# Lottery ticket hypothesis

The **lottery ticket hypothesis** (LTH) is a conjecture about why over-parameterized neural networks train well and why pruning works. Jonathan Frankle and Michael Carbin of MIT proposed it in a paper presented at ICLR 2019: a dense, randomly initialized network contains sparse subnetworks that, if trained on their own, reach test accuracy comparable to the full network in a similar number of iterations.[^s1] They called these subnetworks **winning tickets**, by analogy with a lottery in which a large network holds many tickets and training happens to pick out the lucky ones.[^s2]

The paper started from a puzzle. Pruning could already remove more than 90% of a trained network's parameters without hurting accuracy, yet the sparse architectures produced by pruning were usually hard to train from scratch.[^s1] The hypothesis explains the gap: what makes a pruned subnetwork trainable is not only its connectivity but the specific initial weights it was given.[^s2]

## How winning tickets are found

Frankle and Carbin identify tickets with **iterative magnitude pruning** (IMP):[^s2]

1. Randomly initialize the dense network and record the initial weights.[^s2]
2. Train it for a fixed number of iterations.[^s2]
3. Prune a percentage of the remaining weights with the smallest magnitudes, producing a binary mask.[^s2]
4. Reset the surviving weights to their *original* initial values, not new random ones.[^s2]
5. Repeat, pruning a further share of the survivors each round.[^s2]

One-shot pruning, which removes the whole fraction in a single round, also finds tickets, but they are larger and weaker than the iterative ones.[^s2] Smaller networks were pruned layer by layer, while ResNet-18 and VGG-19 were pruned globally across layers.[^s2]

## Evidence

On fully connected and convolutional networks for MNIST and CIFAR-10, winning tickets were consistently found at under 10-20% of the original size, and in a range above that size they learned faster and reached higher test accuracy than the dense originals.[^s1] For example, the authors report Conv-2, Conv-4 and Conv-6 tickets at 8.8%, 9.2% and 15.1% of their weights reaching minimum validation loss up to 3.5 times faster, and LeNet tickets as small as about 3.6% matching the dense network on MNIST.[^s2] Initialization was the key ingredient: keeping a ticket's mask but resampling its starting weights made it learn more slowly and lose accuracy after relatively little pruning.[^s2]

## Limitations, critiques and refinements

The original study was limited to small vision datasets; ImageNet was not tested because iterative pruning is expensive. Only magnitude pruning was tried, and the resulting unstructured sparsity is not well suited to current hardware and libraries, so tickets do not automatically speed up inference.[^s2] For the deeper VGG-19 and ResNet-18, IMP found tickets at the standard learning rate only when learning-rate warmup was added, a dependence the authors could not explain.[^s2]

Liu and colleagues, also at ICLR 2019, challenged the role of initialization. They found that for the structured pruning methods they studied, training the pruned architecture from random weights matched or beat fine-tuning it, and that with an optimal learning rate the winning-ticket initialization gave no gain over random initialization; they argued the learning rate largely determines whether tickets look special.[^s4]

Follow-up work by Frankle, Dziugaite, Roy and Carbin (ICML 2020) tied the phenomenon to **stability to SGD noise**: whether runs that differ only in data order and augmentation end in minima joined by a linear path of low loss. IMP subnetworks reached full accuracy only when they were stable in this sense. For small MNIST networks stability holds at initialization, but for ResNet-50 and Inception-v3 on ImageNet it appears only early in training, so for large networks tickets are found by resetting to early-training weights rather than to the initial ones.[^s3]

Zhou, Lan, Liu and Yosinski (NeurIPS 2019) dissected the algorithm and found that the zeroing of pruned weights matters, that the signs of the initial weights alone are enough to let a reinitialized ticket train, and that masking behaves like training. They found **supermasks**, masks that give an *untrained* random network accuracy far above chance, about 86% on MNIST and 41% on CIFAR-10.[^s5]

## Why it matters

The hypothesis reframes pruning as a search for a favorable initialization rather than only a way to delete redundant weights.[^s2] It motivates the goal of finding sparse, trainable networks early, which could cut the cost of training, not just of inference, although IMP itself requires training the dense network repeatedly.[^s2] The debate it started, over whether tickets owe their success to initialization, to the learning rate, or to the pruned architecture alone, remains a reference point for research on sparse training.[^s3][^s4]

## Connections

The lottery ticket hypothesis is a theory about **model pruning**, and through pruning it belongs to **model compression**.[^s1] Its central variable is **weight initialization**, since tickets lose their advantage when reinitialized.[^s2] It is defined by the **iterative magnitude pruning** procedure,[^s2] and was introduced in Frankle and Carbin's ICLR 2019 paper, with Jonathan Frankle as lead author.[^s1] Its ICML 2020 extension links tickets to **linear mode connectivity** and to the noise in **stochastic gradient descent**.[^s3] The finding that tickets reach higher test accuracy with smaller train-test gaps also bears on how large networks generalize.[^s2]

## Sources
[^s1]: Frankle and Carbin, "The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks", ICLR 2019. https://iclr.cc/virtual/2019/poster/972 (accessed 2026-11-19)
[^s2]: Frankle and Carbin, "The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks", arXiv 1803.03635. https://arxiv.org/pdf/1803.03635.pdf (accessed 2026-11-19)
[^s3]: Frankle, Dziugaite, Roy and Carbin, "Linear Mode Connectivity and the Lottery Ticket Hypothesis", ICML 2020, PMLR 119:3259-3269. https://proceedings.mlr.press/v119/frankle20a (accessed 2026-11-19)
[^s4]: Liu, Sun, Zhou, Huang and Darrell, "Rethinking the Value of Network Pruning", ICLR 2019, arXiv 1810.05270. https://arxiv.org/abs/1810.05270v2 (accessed 2026-11-19)
[^s5]: Zhou, Lan, Liu and Yosinski, "Deconstructing Lottery Tickets: Zeros, Signs, and the Supermask", NeurIPS 2019. https://papers.nips.cc/paper/2019/hash/1113d7a76ffceca1bb350bfe145467c6-Abstract.html (accessed 2026-11-19)
