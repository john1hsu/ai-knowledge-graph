---
id: kt:autoencoder
type: Architecture
title: Autoencoder
aliases: [auto-encoder, autoassociative neural network, denoising autoencoder]
domain: deep-learning
summary: >-
  A neural network trained to reproduce its own input, made of an encoder that maps the input to a
  constrained internal code and a decoder that reconstructs the input from that code, so that the code
  becomes a learned representation of the data.
maturity: foundational
broader: [kt:artificial-neural-network, kt:unsupervised-learning]
related: [kt:representation-learning, kt:dimensionality-reduction, kt:principal-component-analysis, kt:self-supervised-learning, kt:mechanistic-interpretability]
relations:
  - {predicate: introducedIn, object: kt:reducing-the-dimensionality-of-data-with-neural-networks}
  - {predicate: trainedWith, object: kt:backpropagation}
  - {predicate: hasPart, object: kt:variational-autoencoder}
  - {predicate: hasPart, object: kt:sparse-autoencoder}
  - {predicate: alternativeTo, object: kt:principal-component-analysis}
  - {predicate: usedIn, object: kt:latent-diffusion-model}
sources:
  - id: s1
    title: "Chapter: Autoencoders (6.390 Introduction to Machine Learning lecture notes, Fall 2024)"
    publisher: MIT EECS
    url: https://introml.mit.edu/_static/fall24/LectureNotes/chapter_Autoencoders.pdf
    type: academic
    accessed: 2026-11-17
  - id: s2
    title: "Reducing the Dimensionality of Data with Neural Networks"
    publisher: Science 313(5786), 504–507, 2006 (Hinton and Salakhutdinov); author copy hosted by UC Irvine
    url: https://sites.socsci.uci.edu/~lpearl/courses/readings/HintonSalakhudinov2006_DeepBeliefScience.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "Extracting and Composing Robust Features with Denoising Autoencoders"
    publisher: ICML 2008 (Vincent, Larochelle, Bengio and Manzagol)
    url: https://icml.cc/imls/conferences/2008/papers/592.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "Auto-Encoding Variational Bayes"
    publisher: arXiv:1312.6114 (v11, December 2022; Kingma and Welling)
    url: https://arxiv.org/abs/1312.6114v11
    type: primary
    accessed: 2026-11-17
  - id: s5
    title: "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning"
    publisher: Anthropic, Transformer Circuits Thread (Bricken et al., October 2023)
    url: https://transformer-circuits.pub/2023/monosemantic-features/
    type: lab-research
    accessed: 2026-11-17
created: 2026-11-17
---

# Autoencoder

An autoencoder is a network whose training target is its own input. It has two halves: an **encoder** that turns an input vector into a code, usually of lower dimension, and a **decoder** that turns the code back into something in the input space. Because no labels are needed, it is a standard example of unsupervised learning; the useful product is usually not the reconstruction but the code, which serves as a compact learned representation.[^s1]

## How it works

For an input x in R^d, the encoder produces a code a in R^k and the decoder produces a reconstruction x̃. Training minimises a reconstruction loss between x̃ and x, typically squared error summed over dimensions, with stochastic gradient descent.[^s1] The constraint that makes this non-trivial is the narrow middle layer, often called the bottleneck: if k equalled d and both halves were the identity, the network would copy its input perfectly and learn nothing. Squeezing the data through a small k forces the network to find a simpler description, and individual code dimensions sometimes align with factors such as stroke thickness or rotation in handwritten digits, though nothing guarantees that.[^s1]

A purely linear autoencoder has a closed-form solution equivalent to principal components analysis; adding nonlinear layers generalises PCA in roughly the way a multilayer network generalises linear regression.[^s1] In the classic single-layer form, the encoder computes a sigmoid of an affine map of x, the decoder applies a second affine map and sigmoid, and the decoder weights are sometimes tied to the transpose of the encoder weights; squared error or cross-entropy serves as the loss.[^s3]

## History and key variants

**Deep autoencoders (2006).** Geoffrey Hinton and Ruslan Salakhutdinov showed in *Science* that deep autoencoders could learn far better low-dimensional codes than PCA, but only with the right initialisation. Training deep stacks from random weights tended either to stall in poor solutions or to suffer vanishing gradients in early layers. Their fix was to pretrain each layer greedily as a restricted Boltzmann machine, feed one layer's activations to the next, then "unroll" the stack into an encoder and decoder and fine-tune the whole network with backpropagation. They demonstrated it on synthetic curves, MNIST, Olivetti face patches and Reuters newswire documents, where the codes also beat latent semantic analysis for retrieval.[^s2] This paper is one of the milestones that revived interest in deep networks.

**Denoising autoencoders (2008).** Pascal Vincent, Hugo Larochelle, Yoshua Bengio and Pierre-Antoine Manzagol replaced plain reconstruction with a harder task: corrupt the input (for example by zeroing a random fraction of its components) and train the network to recover the clean original. Because the identity map no longer solves the task, no bottleneck is strictly required, and their best models often had overcomplete first layers. Stacks of denoising autoencoders, pretrained layer by layer and then fine-tuned with labels, matched or beat deep belief networks and SVMs on most of a suite of MNIST-variant benchmarks and consistently beat stacks of ordinary autoencoders. The authors also gave manifold-learning and information-theoretic interpretations of the objective.[^s3]

**Variational autoencoders (2013).** Diederik Kingma and Max Welling recast the encoder as an approximate inference (recognition) model for a latent-variable generative model and introduced a reparameterisation of the variational lower bound that ordinary stochastic gradient methods can optimise.[^s4] Instead of a single code, the encoder outputs a distribution over the latent space, so sampling from that space and decoding produces new data; this turned autoencoders into generative models.[^s1][^s4]

**Sparse autoencoders for interpretability (2023).** Anthropic researchers trained sparse autoencoders on the 512-neuron MLP activations of a one-layer transformer, using dictionaries ranging from 512 to 131,072 features. They reported that the learned features were substantially more monosemantic than individual neurons and that features split into finer ones as the dictionary grew.[^s5] Here the autoencoder is overcomplete rather than compressive, with sparsity doing the work of the bottleneck.

## Limitations and practical notes

Reconstruction quality is not the same as usefulness: an autoencoder can reconstruct well while its code still mixes factors of variation, and interpretable latent dimensions are not guaranteed.[^s1] Deep autoencoders were historically hard to optimise without careful initialisation or pretraining.[^s2] Ordinary autoencoders also lack a principled way to sample new data, the gap the variational form fills.[^s4] In practice the encoder is often kept and the decoder discarded, with the code feeding a downstream classifier trained on a smaller labelled set, or used for compression, 2-D visualisation and exploring factors of variation.[^s1]

## Connections

The autoencoder is a kind of **artificial neural network** and a core **unsupervised learning** method, trained end to end with **backpropagation**.[^s1][^s2] It is a central tool of **representation learning** and a nonlinear method for **dimensionality reduction**, standing as an alternative to **principal component analysis**, which it reduces to in the linear case.[^s1] Its descendants include the **variational autoencoder** and the **sparse autoencoder**; the latter is a workhorse of **mechanistic interpretability**.[^s4][^s5] Reconstructing a corrupted input is an early form of the pretext tasks used in **self-supervised learning**.[^s3] Autoencoders also supply the compressed latent space in which a **latent diffusion model** operates. The node's origin edge points to the 2006 *Science* paper by Hinton and Salakhutdinov.[^s2]

## Sources
[^s1]: MIT EECS 6.390, "Autoencoders" lecture notes, Fall 2024. https://introml.mit.edu/_static/fall24/LectureNotes/chapter_Autoencoders.pdf (accessed 2026-11-17)
[^s2]: Hinton and Salakhutdinov, "Reducing the Dimensionality of Data with Neural Networks", Science 313, 504–507 (2006). https://sites.socsci.uci.edu/~lpearl/courses/readings/HintonSalakhudinov2006_DeepBeliefScience.pdf (accessed 2026-11-17)
[^s3]: Vincent, Larochelle, Bengio and Manzagol, "Extracting and Composing Robust Features with Denoising Autoencoders", ICML 2008. https://icml.cc/imls/conferences/2008/papers/592.pdf (accessed 2026-11-17)
[^s4]: Kingma and Welling, "Auto-Encoding Variational Bayes", arXiv:1312.6114. https://arxiv.org/abs/1312.6114v11 (accessed 2026-11-17)
[^s5]: Bricken et al., "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning", Anthropic, October 2023. https://transformer-circuits.pub/2023/monosemantic-features/ (accessed 2026-11-17)
