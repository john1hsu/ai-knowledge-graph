---
id: kt:batch-normalization
type: Technique
title: Batch normalization
aliases: [BatchNorm, batch norm, BN layer]
domain: deep-learning
summary: >-
  A neural-network layer that standardizes each feature (or each convolutional channel) using the mean and
  variance of the current mini-batch, then applies a learned scale and shift; introduced by Ioffe and Szegedy
  in 2015, it permits higher learning rates and faster, more stable training.
maturity: established
broader: [kt:deep-learning]
related: [kt:layer-normalization, kt:dropout, kt:regularization, kt:convolutional-neural-network, kt:residual-connection, kt:image-classification]
relations:
  - {predicate: introducedIn, object: kt:batch-normalization-accelerating-deep-network-training}
  - {predicate: createdBy, object: kt:google}
  - {predicate: usedIn, object: kt:convolutional-neural-network}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: alternativeTo, object: kt:layer-normalization}
  - {predicate: mitigates, object: kt:vanishing-gradient-problem}
sources:
  - id: s1
    title: "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift"
    publisher: Proceedings of the 32nd ICML, PMLR 37:448–456 (2015) (Ioffe and Szegedy)
    url: https://proceedings.mlr.press/v37/ioffe15
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s2
    title: "How Does Batch Normalization Help Optimization?"
    publisher: NeurIPS 2018 (Santurkar, Tsipras, Ilyas and Madry)
    url: https://papers.nips.cc/paper/2018/hash/905056c1ac1dad141560467e0a99e1cf-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "8.5. Batch Normalization"
    publisher: Dive into Deep Learning (d2l.ai)
    url: https://d2l.ai/chapter_convolutional-modern/batch-norm.html
    type: textbook
    accessed: 2026-11-14
  - id: s4
    title: "BatchNorm2d"
    publisher: PyTorch documentation (v2.3)
    url: https://docs.pytorch.org/docs/2.3/generated/torch.nn.BatchNorm2d.html
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# Batch normalization

**Batch normalization** (BatchNorm, BN) is a layer that rescales the inputs to a layer so that, within each training mini-batch, every feature has roughly zero mean and unit variance, and then lets the network learn how far to undo that standardization. Sergey Ioffe and Christian Szegedy of Google introduced it at ICML 2015, arguing that the shifting distribution of each layer's inputs during training (which they named *internal covariate shift*) forces small learning rates and careful initialization, and makes networks with saturating nonlinearities hard to train.[^s1] Making normalization part of the architecture, computed per mini-batch, allowed much higher learning rates, reduced sensitivity to initialization and in some cases removed the need for dropout.[^s1]

## How it works

For a mini-batch B, BN computes the batch mean μ_B and variance σ²_B of each feature, standardizes the input, and then applies two learned parameters, a scale γ and a shift β:[^s3]

BN(x) = γ ⊙ (x − μ_B) / √(σ²_B + ε) + β

The small constant ε prevents division by zero. Because γ and β are trained, the layer can recover the identity transformation if that is what the downstream layer needs, so normalization does not reduce what the network can represent.[^s3] For fully connected layers the statistics are computed per feature, and the original paper placed BN after the affine transform and before the activation; for convolutional layers they are computed per channel, pooled over the batch and all spatial positions, with one γ and one β per channel.[^s3] PyTorch's `BatchNorm2d` follows this per-channel scheme, averaging over the batch, height and width dimensions.[^s4]

BN behaves differently at training and inference time. During training it normalizes with the current batch's statistics and maintains running averages of the mean and variance; at inference it uses those stored averages so that a prediction does not depend on which other examples share its batch.[^s3] In PyTorch the defaults are ε = 1e-5, a running-average momentum of 0.1, and learnable γ and β initialized to 1 and 0; the forward pass uses the biased variance estimate while the running variance is stored with the unbiased one.[^s4] If running statistics are disabled, the layer falls back to batch statistics in both modes.[^s4]

## Evidence and results

Ioffe and Szegedy reported that adding BN to a then state-of-the-art image classifier matched its accuracy with 14 times fewer training steps, and that an ensemble of batch-normalized networks reached 4.82% top-5 test error on ImageNet, which they described as better than the best published result at the time.[^s1] The textbook treats it as a standard ingredient of modern convolutional networks.[^s3]

## Why it works: an open question

The internal-covariate-shift explanation has been contested. Santurkar and colleagues showed at NeurIPS 2018 that the distributional stability of layer inputs has little to do with BN's success; they found instead that BN makes the optimization landscape significantly smoother, so gradients are more predictable and larger steps are safe.[^s2] The *Dive into Deep Learning* textbook notes that the phenomenon BN targets is not covariate shift in the statistical sense, that the original explanation is under-specified, and that BN's well-supported benefits are faster convergence and a regularizing effect from the noise in mini-batch statistics.[^s3]

## Limitations

Because it depends on batch statistics, BN is sensitive to batch size. A batch of one makes a fully connected BN layer output zero for every unit, very small batches inject excessive noise, and the textbook suggests moderate batches of roughly 50–100 work well.[^s3] Layer normalization (Ba et al., 2016) instead normalizes across the features of a single example, making it independent of batch size and identical in training and inference.[^s3]

## Connections

BN is a core technique of **deep learning** and is a standard part of **convolutional neural network** models for **image classification**, where it is applied per channel.[^s1][^s3] It is an alternative to **layer normalization**, which removes the batch dependence and so suits settings where batch statistics are unreliable, such as very small batches.[^s3] Its noisy batch statistics give it a **regularization** effect that the original paper found could sometimes replace **dropout**.[^s1] By keeping activations in a well-scaled range it helps networks with saturating activations train, easing the **vanishing gradient problem**; together with **residual connection** blocks it is one of the ingredients that made very deep image models trainable.[^s1][^s3] It was introduced in Ioffe and Szegedy's 2015 paper from **Google** and is implemented in **PyTorch** with layers such as `BatchNorm2d`.[^s1][^s4]

## Sources
[^s1]: Ioffe, S. and Szegedy, C., "Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift", ICML 2015, PMLR 37:448–456. https://proceedings.mlr.press/v37/ioffe15 (accessed 2026-11-14)
[^s2]: Santurkar, S., Tsipras, D., Ilyas, A. and Madry, A., "How Does Batch Normalization Help Optimization?", NeurIPS 2018. https://papers.nips.cc/paper/2018/hash/905056c1ac1dad141560467e0a99e1cf-Abstract.html (accessed 2026-11-14)
[^s3]: *Dive into Deep Learning*, §8.5 "Batch Normalization". https://d2l.ai/chapter_convolutional-modern/batch-norm.html (accessed 2026-11-14)
[^s4]: PyTorch documentation, "BatchNorm2d" (v2.3). https://docs.pytorch.org/docs/2.3/generated/torch.nn.BatchNorm2d.html (accessed 2026-11-14)
