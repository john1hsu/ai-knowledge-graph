---
id: kt:variational-autoencoder
type: Architecture
title: Variational autoencoder
aliases: [VAE, variational auto-encoder, auto-encoding variational Bayes]
domain: deep-learning
summary: >-
  A deep latent-variable generative model that pairs a neural encoder approximating the posterior over
  latent codes with a neural decoder that generates data from them, trained jointly by maximizing the
  evidence lower bound (ELBO) with the reparameterization trick.
maturity: established
broader: [kt:autoencoder, kt:generative-model]
related: [kt:generative-adversarial-network, kt:diffusion-model, kt:representation-learning, kt:variational-inference]
relations:
  - {predicate: introducedIn, object: kt:auto-encoding-variational-bayes}
  - {predicate: createdBy, object: kt:diederik-kingma}
  - {predicate: dependsOn, object: kt:reparameterization-trick}
  - {predicate: trainedWith, object: kt:backpropagation}
  - {predicate: usedIn, object: kt:latent-diffusion-model}
  - {predicate: contrastsWith, object: kt:generative-adversarial-network}
sources:
  - id: s1
    title: "Auto-Encoding Variational Bayes"
    publisher: arXiv:1312.6114 (Kingma and Welling), authors' version v11
    url: https://arxiv.org/abs/1312.6114v11
    type: primary
    accessed: 2026-11-17
  - id: s2
    title: "Stochastic Backpropagation and Approximate Inference in Deep Generative Models"
    publisher: ICML 2014, PMLR 32 (Rezende, Mohamed and Wierstra)
    url: https://proceedings.mlr.press/v32/rezende14.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "An Introduction to Variational Autoencoders"
    publisher: Foundations and Trends in Machine Learning 12(4), 2019 (Kingma and Welling), authors' arXiv version
    url: https://ar5iv.arxiv.org/html/1906.02691
    type: primary
    accessed: 2026-11-17
  - id: s4
    title: "Variational autoencoders (Deep Generative Models course notes)"
    publisher: Deep Generative Models course notes (Aditya Grover)
    url: https://deepgenerativemodels.github.io/notes/vae
    type: academic
    accessed: 2026-11-17
  - id: s5
    title: "Neural Discrete Representation Learning"
    publisher: NeurIPS 2017 (van den Oord, Vinyals and Kavukcuoglu)
    url: https://papers.nips.cc/paper/7210-neural-discrete-representation-learning
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s6
    title: "High-Resolution Image Synthesis with Latent Diffusion Models"
    publisher: arXiv:2112.10752 (Rombach et al.), CVPR 2022
    url: https://arxiv.org/pdf/2112.10752
    type: primary
    accessed: 2026-11-17
  - id: s7
    title: "beta-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework"
    publisher: ICLR 2017 (Higgins et al.), ML Anthology record
    url: https://mlanthology.org/iclr/2017/higgins2017iclr-beta
    type: peer-reviewed
    accessed: 2026-11-17
created: 2026-11-17
---

# Variational autoencoder

A **variational autoencoder (VAE)** is a generative model with continuous latent variables in which two neural networks are trained together: a *decoder* (generative model) that maps a latent code z to a distribution over data x, and an *encoder* (recognition or inference model) that maps each datapoint to an approximate posterior over z. Although it looks like an **autoencoder**, its purpose is different: it learns a probability model of the data that can be sampled, rather than just a compressed code.[^s1][^s3]

## Origin

The VAE was introduced by Diederik Kingma and Max Welling in "Auto-Encoding Variational Bayes", first posted to arXiv in December 2013. The paper targeted directed models whose posteriors are intractable and large datasets, and made two contributions: a reparameterized, low-variance estimator of the variational lower bound that works with ordinary stochastic gradient methods, and a learned recognition model fitted with that estimator.[^s1] In parallel, Rezende, Mohamed and Wierstra proposed essentially the same combination, a recognition model optimizing a variational bound plus "stochastic backpropagation" through random variables, at ICML 2014.[^s2] Kingma and Welling's 2019 monograph frames the VAE as a successor to the Helmholtz machine and its wake-sleep algorithm, which did not optimize a single objective.[^s3]

## How it works

The model assumes a prior p(z), usually a standard normal, and a decoder likelihood p_θ(x|z). The true posterior p_θ(z|x) is intractable, so the encoder q_φ(z|x) approximates it.[^s3] The log-likelihood decomposes as

log p_θ(x) = ELBO(x) + KL(q_φ(z|x) ‖ p_θ(z|x)),

where ELBO = E_q[log p_θ(x|z)] − KL(q_φ(z|x) ‖ p(z)). Because a KL divergence is never negative, the ELBO is a lower bound on the log-likelihood, and raising it both improves the generative model and pulls the approximate posterior toward the true one.[^s3][^s4] The first term rewards accurate reconstruction; the second keeps each code distribution close to the prior so the latent space can be sampled.

Training uses **amortized inference**: instead of solving a separate optimization for every datapoint, as in black-box variational inference, one encoder network outputs the variational parameters for any input.[^s4] The obstacle is that the ELBO involves an expectation over a random sample of z. The **reparameterization trick** rewrites the sample as a deterministic function of parameter-free noise, for a Gaussian encoder z = μ + σ ⊙ ε with ε ~ N(0, I), so gradients flow through μ and σ by ordinary backpropagation.[^s1][^s3] The course notes report that this estimator has much lower variance in practice than the score-function (REINFORCE) alternative, which makes training more stable.[^s4] New data is generated by drawing z from the prior and decoding it.

## Limitations and variants

VAE samples, especially of images, are often blurrier than those of adversarial models. Kingma and Welling attribute this partly to the direction of the KL divergence implicit in maximum likelihood, which only weakly penalizes the model for spreading probability where there is no data, and point to more expressive encoders and decoders as the fix.[^s3] Optimization can also stall in a state where the encoder's output matches the prior and latents go unused; KL annealing (ramping the KL weight from 0 to 1) and "free bits" objectives are standard remedies.[^s3] This failure, often called **posterior collapse**, is worst with powerful autoregressive decoders; the VQ-VAE replaced continuous codes with vector-quantized discrete codes and a learned prior partly to avoid it, generating images, video and speech.[^s5]

Other well-known variants reshape the objective. β-VAE multiplies the KL term by a weight β; Higgins et al. reported at ICLR 2017 that β > 1 yields more disentangled, interpretable latent factors on faces and chairs datasets, at some cost in reconstruction.[^s7] More flexible posteriors such as inverse autoregressive flows and tighter multi-sample bounds such as importance-weighted autoencoders are also covered in the 2019 monograph.[^s3]

## In practice

The VAE's most visible role today is as a learned compressor for other generative models. Latent diffusion models run diffusion in the latent space of a pretrained autoencoder; Rombach et al. regularize that autoencoder either with a slight KL penalty toward a standard normal, "similar to a VAE", or with vector quantization.[^s6] VAEs are also used for representation learning, semi-supervised learning and data imputation.[^s2][^s3]

## Connections

- Broader: the VAE is a probabilistic member of the **autoencoder** family and one of the main classes of deep **generative models**.[^s1][^s3]
- `introducedIn` *Auto-Encoding Variational Bayes*, `createdBy` Diederik Kingma (with Max Welling).[^s1]
- `dependsOn` the reparameterization trick, which makes the ELBO differentiable, and is `trainedWith` backpropagation and stochastic gradient methods.[^s1][^s4]
- It is an application of variational inference with amortized, neural posteriors.[^s4]
- `contrastsWith` **generative adversarial networks**, which avoid likelihood bounds and tend to give sharper samples. It is also a common comparison point for **diffusion models**, which can run inside a VAE-style latent space.[^s3][^s6]
- `usedIn` **latent diffusion models** as the KL-regularized image autoencoder.[^s6]

## Sources
[^s1]: Kingma and Welling, "Auto-Encoding Variational Bayes", arXiv:1312.6114. https://arxiv.org/abs/1312.6114v11 (accessed 2026-11-17)
[^s2]: Rezende, Mohamed and Wierstra, "Stochastic Backpropagation and Approximate Inference in Deep Generative Models", ICML 2014. https://proceedings.mlr.press/v32/rezende14.html (accessed 2026-11-17)
[^s3]: Kingma and Welling, "An Introduction to Variational Autoencoders", Foundations and Trends in Machine Learning, 2019. https://ar5iv.arxiv.org/html/1906.02691 (accessed 2026-11-17)
[^s4]: Grover, "Variational autoencoders", Deep Generative Models course notes. https://deepgenerativemodels.github.io/notes/vae (accessed 2026-11-17)
[^s5]: van den Oord, Vinyals and Kavukcuoglu, "Neural Discrete Representation Learning", NeurIPS 2017. https://papers.nips.cc/paper/7210-neural-discrete-representation-learning (accessed 2026-11-17)
[^s6]: Rombach et al., "High-Resolution Image Synthesis with Latent Diffusion Models", CVPR 2022. https://arxiv.org/pdf/2112.10752 (accessed 2026-11-17)
[^s7]: Higgins et al., "beta-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework", ICLR 2017. https://mlanthology.org/iclr/2017/higgins2017iclr-beta (accessed 2026-11-17)
