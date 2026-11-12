---
id: kt:convolutional-neural-network
type: Architecture
title: Convolutional neural network
aliases: [CNN, ConvNet, convolutional network]
domain: deep-learning
summary: >-
  A neural network architecture for grid-structured data such as images that replaces dense layers with
  small learned kernels slid across the input, so that weights are local and shared across positions,
  usually interleaved with pooling and stacked into deep feature hierarchies.
maturity: established
broader: [kt:artificial-neural-network, kt:deep-learning]
related: [kt:imagenet-and-alexnet, kt:image-classification, kt:recurrent-neural-network]
relations:
  - {predicate: introducedIn, object: kt:gradient-based-learning-applied-to-document-recognition}
  - {predicate: createdBy, object: kt:yann-lecun}
  - {predicate: influencedBy, object: kt:neocognitron}
  - {predicate: trainedWith, object: kt:backpropagation}
  - {predicate: usedIn, object: kt:faster-r-cnn}
  - {predicate: alternativeTo, object: kt:vision-transformer}
sources:
  - id: s1
    title: "Neocognitron: A Self-Organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position"
    publisher: Biological Cybernetics 36(4):193–202 (1980) (Fukushima), via ML Anthology
    url: https://mlanthology.org/misc/1980/fukushima1980misc-neocognitron
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Gradient-Based Learning Applied to Document Recognition"
    publisher: Proceedings of the IEEE 86(11):2278–2324 (1998) (LeCun, Bottou, Bengio and Haffner), via ML Anthology
    url: https://mlanthology.org/misc/1998/lecun1998misc-gradientbased
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s3
    title: "Deep Residual Learning for Image Recognition"
    publisher: CVPR 2016, pp. 770–778 (He, Zhang, Ren and Sun)
    url: https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "7. Convolutional Neural Networks"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola)
    url: https://d2l.ai/chapter_convolutional-neural-networks/
    type: textbook
    accessed: 2026-11-12
  - id: s5
    title: "7.2. Convolutions for Images"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola)
    url: https://d2l.ai/chapter_convolutional-neural-networks/conv-layer.html
    type: textbook
    accessed: 2026-11-12
  - id: s6
    title: "From Fully Connected Layers to Convolutions"
    publisher: Dive into Deep Learning, DJL edition (Zhang, Lipton, Li and Smola)
    url: https://d2l.djl.ai/chapter_convolutional-neural-networks/why-conv.html
    type: textbook
    accessed: 2026-11-12
created: 2026-11-12
---

# Convolutional neural network

A **convolutional neural network** (CNN, ConvNet) is a neural network built for data laid out on a grid, above all images. Instead of connecting every input pixel to every hidden unit, a convolutional layer slides a small learned kernel across the input and computes the same weighted sum at each position. Flattening an image into a vector for a fully connected network throws away the fact that nearby pixels are usually related; CNNs build that prior into the architecture, which makes them more sample-efficient, cheaper in parameters and easy to parallelise on GPUs.[^s4] They became the core of computer vision and are also applied to audio, text, time series, graphs and recommender systems.[^s4]

## Origin

The architectural idea predates modern deep learning. In 1980 Kunihiko Fukushima proposed the *neocognitron*, a layered network of alternating "S-cells" and "C-cells", loosely modelled on the simple and complex cells Hubel and Wiesel found in the visual cortex. It learned without labels and recognised shapes regardless of where they appeared in the visual field.[^s1] The trainable form came from Yann LeCun and colleagues, who trained convolutional networks end to end with backpropagation. Their 1998 *Proceedings of the IEEE* paper benchmarked handwritten-digit recognisers and found that convolutional networks, designed to cope with the variability of 2D shapes, beat the other methods tested; a cheque-reading system built on them was in commercial use, processing several million cheques a day.[^s2] The *Dive into Deep Learning* textbook describes LeNet as the first convolutional network to be successfully deployed.[^s4]

## How it works

Two design principles turn a dense layer into a convolutional one.[^s6]

- **Locality.** Each hidden unit looks only at a small neighbourhood of the input; weights outside a radius are fixed at zero.[^s6]
- **Translation equivariance via weight sharing.** The same kernel is reused at every position, so shifting the input simply shifts the activations, and a detector responds to a pattern wherever it appears.[^s6]

The saving is dramatic. Mapping a one-megapixel image to 1,000 hidden units with a dense layer needs about 10⁹ weights, whereas a convolutional layer with one shared kernel needs a few hundred.[^s6] The price is an inductive bias: if features are not in fact local and position-independent, the model may fit the data poorly.[^s6]

Strictly, deep-learning libraries compute cross-correlation rather than mathematical convolution (which would flip the kernel), but because the kernel is learned the distinction does not matter.[^s5] For an *n*ₕ×*n*ᵥ input and a *k*ₕ×*k*ᵥ kernel with no padding, the output is (*n*ₕ−*k*ₕ+1)×(*n*ᵥ−*k*ᵥ+1); a 3×3 input and a 2×2 kernel give a 2×2 output.[^s5] That output is called a **feature map**. The **receptive field** of a unit is every earlier element that can affect it, and it grows with depth: stacking two 2×2 layers lets one output depend on all nine pixels of a 3×3 input.[^s5] Kernels are not hand-designed; starting from random values, gradient descent can recover an edge detector such as [1, −1] in a few iterations.[^s5]

A full CNN stacks these layers with padding and stride (to control output size), multiple input and output channels (so each layer learns many filters), and **pooling** layers, which aggregate over adjacent spatial regions with a maximum or average; the classic LeNet pipeline ends in fully connected layers that produce class scores.[^s4]

## Limitations and later developments

Simply adding layers made CNNs harder to optimise. He et al.'s residual networks (ResNets) addressed this with shortcut connections that let layers learn residual functions; at CVPR 2016 they trained networks up to 152 layers deep, eight times deeper than VGG nets yet of lower complexity, and an ensemble reached 3.57% test error on ImageNet, winning the ILSVRC 2015 classification task.[^s3] The locality and translation priors that make CNNs efficient also limit them when long-range relationships matter or when the translation assumption fails: the textbook notes that such a model may then struggle even to fit its training data.[^s6]

## Connections

The CNN is a specialised **artificial neural network** and a signature architecture of **deep learning**.[^s4] It was **introduced in** LeCun et al.'s *Gradient-Based Learning Applied to Document Recognition*, with LeCun as its principal **creator**, and was **influenced by** Fukushima's **neocognitron**.[^s1][^s2] It is **trained with** **backpropagation**, the property that separated LeCun's networks from the neocognitron's unsupervised learning.[^s1][^s2] CNNs are the backbone of **image classification** and drove the ImageNet gains associated with **ImageNet and AlexNet**,[^s4] and they serve as the feature extractor **used in** region-based detectors such as **Faster R-CNN**. The **vision transformer** is an **alternative** that relies on attention rather than convolution's built-in locality prior, while the **recurrent neural network** plays the analogous role for sequences that the CNN plays for grids.[^s4][^s6]

## Sources

[^s1]: Fukushima, "Neocognitron: A Self-Organizing Neural Network Model for a Mechanism of Pattern Recognition Unaffected by Shift in Position", Biological Cybernetics 36(4), 1980. https://mlanthology.org/misc/1980/fukushima1980misc-neocognitron (accessed 2026-11-12)
[^s2]: LeCun, Bottou, Bengio and Haffner, "Gradient-Based Learning Applied to Document Recognition", Proceedings of the IEEE 86(11), 1998. https://mlanthology.org/misc/1998/lecun1998misc-gradientbased (accessed 2026-11-12)
[^s3]: He, Zhang, Ren and Sun, "Deep Residual Learning for Image Recognition", CVPR 2016. https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html (accessed 2026-11-12)
[^s4]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, ch. 7 "Convolutional Neural Networks". https://d2l.ai/chapter_convolutional-neural-networks/ (accessed 2026-11-12)
[^s5]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, §7.2 "Convolutions for Images". https://d2l.ai/chapter_convolutional-neural-networks/conv-layer.html (accessed 2026-11-12)
[^s6]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning* (DJL edition), "From Fully Connected Layers to Convolutions". https://d2l.djl.ai/chapter_convolutional-neural-networks/why-conv.html (accessed 2026-11-12)
