---
id: kt:generative-adversarial-network
type: Architecture
title: Generative adversarial network
aliases: [GAN, generative adversarial nets, adversarial generative model]
domain: computer-vision-and-multimodal
summary: >-
  A generative modelling framework in which two neural networks are trained against each other: a generator
  that maps random noise to synthetic samples, and a discriminator that tries to tell those samples apart from
  real training data, so that the generator gradually learns to produce data the discriminator cannot distinguish.
maturity: established
broader: [kt:generative-model, kt:deep-learning]
related: [kt:wasserstein-gan, kt:stylegan]
relations:
  - {predicate: introducedIn, object: kt:generative-adversarial-nets}
  - {predicate: createdBy, object: kt:ian-goodfellow}
  - {predicate: alternativeTo, object: kt:diffusion-model}
  - {predicate: contrastsWith, object: kt:variational-autoencoder}
sources:
  - id: s1
    title: "Generative Adversarial Nets"
    publisher: NeurIPS 2014, Advances in Neural Information Processing Systems 27 (Goodfellow et al.)
    url: https://proceedings.neurips.cc/paper/5423-generative-adversarial-nets
    type: peer-reviewed
    accessed: 2026-10-30
  - id: s2
    title: "Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks"
    publisher: arXiv 1511.06434 (Radford, Metz and Chintala)
    url: https://arxiv.org/abs/1511.06434
    type: primary
    accessed: 2026-10-30
  - id: s3
    title: "Wasserstein Generative Adversarial Networks"
    publisher: Proceedings of ICML 2017, PMLR 70:214–223 (Arjovsky, Chintala and Bottou)
    url: https://proceedings.mlr.press/v70/arjovsky17a.html
    type: peer-reviewed
    accessed: 2026-10-30
  - id: s4
    title: "A Style-Based Generator Architecture for Generative Adversarial Networks"
    publisher: CVPR 2019, pp. 4401–4410 (Karras, Laine and Aila)
    url: https://openaccess.thecvf.com/content_CVPR_2019/html/Karras_A_Style-Based_Generator_Architecture_for_Generative_Adversarial_Networks_CVPR_2019_paper.html
    type: peer-reviewed
    accessed: 2026-10-30
  - id: s5
    title: "Diffusion Models Beat GANs on Image Synthesis"
    publisher: NeurIPS 2021, Advances in Neural Information Processing Systems 34 (Dhariwal and Nichol)
    url: https://papers.nips.cc/paper/2021/hash/49ad23d1ec9fa4bd8d77d02681df5cfa-Abstract.html
    type: peer-reviewed
    accessed: 2026-10-30
created: 2026-10-30
---

# Generative adversarial network

A **generative adversarial network (GAN)** learns to generate data by pitting two models against each other. A *generator* turns random noise into candidate samples, and a *discriminator* estimates whether a given sample came from the training set or from the generator. The generator is trained to make the discriminator wrong, so as the discriminator gets better at spotting fakes, the generator is pushed to produce more realistic data.[^s1] GANs were among the strongest image generators until diffusion models surpassed them on ImageNet sample quality in 2021.[^s5]

## Origin

The framework was introduced by Ian Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David Warde-Farley, Sherjil Ozair, Aaron Courville and Yoshua Bengio in *Generative Adversarial Nets*, published at NeurIPS (then NIPS) 2014.[^s1] Its selling point at the time was simplicity: when both networks are multilayer perceptrons, the whole system trains with ordinary backpropagation, with no Markov chains or unrolled approximate inference networks needed either for training or for drawing samples.[^s1]

## How it works

The paper frames training as a **two-player minimax game**.[^s1] Writing *D(x)* for the discriminator's estimated probability that *x* is real and *G(z)* for the generator's output on noise *z*, the value function is

V(D, G) = E<sub>x∼data</sub>[log D(x)] + E<sub>z∼noise</sub>[log(1 − D(G(z)))]

The discriminator ascends *V* (classifying real and fake correctly), while the generator descends it (fooling the discriminator). In practice the two networks are updated in alternation with stochastic gradients. Goodfellow et al. showed that, if *G* and *D* could be any functions, the game has a unique solution in which the generator exactly reproduces the data distribution and the discriminator outputs 1/2 everywhere, because it can no longer tell the two apart.[^s1] Sampling afterwards is a single forward pass through the generator.

## Major developments

- **DCGAN (2015).** Alec Radford, Luke Metz and Soumith Chintala proposed deep convolutional GANs, a family of convolutional generators and discriminators built under specific architectural constraints that trained more reliably on images. They reported that both networks learned a hierarchy of representations from object parts to whole scenes, and that discriminator features transferred to other tasks.[^s2]
- **Wasserstein GAN (2017).** Martin Arjovsky, Chintala and Léon Bottou replaced the original objective with one based on the Wasserstein (earth-mover) distance. They reported more stable learning, an end to problems such as mode collapse in their experiments, and loss curves that actually track sample quality, which helps with debugging and hyperparameter search.[^s3]
- **StyleGAN (2019).** Tero Karras, Samuli Laine and Timo Aila of NVIDIA borrowed ideas from style transfer to redesign the generator. Their model separates high-level attributes such as pose and identity from stochastic detail such as freckles and hair without supervision, and allows control at different image scales. They also released a new, highly varied dataset of human faces.[^s4]

## Limitations

GAN training is a saddle-point search, not a straightforward minimisation, and it is known to be unstable. Two failure modes are the most cited: *mode collapse*, where the generator produces only a narrow slice of the data distribution, and losses that say little about whether samples are improving. The Wasserstein GAN was proposed specifically to address both.[^s3] Because the generator learns only through the discriminator's judgements, GAN papers typically compare models on sample-quality metrics such as FID.[^s1][^s5]

The clearest marker of GANs losing their lead is Prafulla Dhariwal and Alexander Nichol's NeurIPS 2021 paper, which showed diffusion models beating the best GANs of the time on ImageNet sample quality. They reported FIDs of 2.97 at 128×128, 4.59 at 256×256 and 7.72 at 512×512, and used classifier guidance to trade diversity for fidelity.[^s5] GANs remain attractive where generation speed matters, because they need one network evaluation per sample rather than an iterative denoising loop.

## Connections

GANs are a family of **generative models** within **deep learning**.[^s1] They were **introduced in** the 2014 paper *Generative Adversarial Nets*, **created by** Ian Goodfellow and colleagues.[^s1] **Diffusion models** are the main **alternative**: they surpassed GAN image quality in 2021 at the cost of many sequential sampling steps.[^s5] GANs **contrast with variational autoencoders**, the other major deep generative family of the mid-2010s; a GAN's generator never sees the data directly and learns only through the discriminator's feedback.[^s1] Notable descendants include the **Wasserstein GAN**, which changed the training objective,[^s3] and **StyleGAN**, which changed the generator architecture.[^s4]

## Sources

[^s1]: Goodfellow, Pouget-Abadie, Mirza, Xu, Warde-Farley, Ozair, Courville and Bengio, "Generative Adversarial Nets", NeurIPS 2014 (NIPS 27). https://proceedings.neurips.cc/paper/5423-generative-adversarial-nets (accessed 2026-10-30)
[^s2]: Radford, Metz and Chintala, "Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks", arXiv:1511.06434, 2015. https://arxiv.org/abs/1511.06434 (accessed 2026-10-30)
[^s3]: Arjovsky, Chintala and Bottou, "Wasserstein Generative Adversarial Networks", ICML 2017, PMLR 70:214–223. https://proceedings.mlr.press/v70/arjovsky17a.html (accessed 2026-10-30)
[^s4]: Karras, Laine and Aila, "A Style-Based Generator Architecture for Generative Adversarial Networks", CVPR 2019, pp. 4401–4410. https://openaccess.thecvf.com/content_CVPR_2019/html/Karras_A_Style-Based_Generator_Architecture_for_Generative_Adversarial_Networks_CVPR_2019_paper.html (accessed 2026-10-30)
[^s5]: Dhariwal and Nichol, "Diffusion Models Beat GANs on Image Synthesis", NeurIPS 2021 (NeurIPS 34). https://papers.nips.cc/paper/2021/hash/49ad23d1ec9fa4bd8d77d02681df5cfa-Abstract.html (accessed 2026-10-30)
