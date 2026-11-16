---
id: kt:u-net
type: Architecture
title: U-Net
aliases: [UNet, U-Net architecture, U-shaped encoder-decoder network]
domain: computer-vision-and-multimodal
summary: >-
  A fully convolutional encoder-decoder architecture, introduced by Ronneberger, Fischer and Brox at MICCAI
  2015 for biomedical image segmentation, whose contracting path captures context and whose symmetric
  expanding path recovers resolution by concatenating same-scale encoder features through skip connections.
maturity: established
broader: [kt:convolutional-neural-network]
related: [kt:semantic-segmentation, kt:diffusion-model, kt:data-augmentation, kt:residual-connection, kt:dropout]
relations:
  - {predicate: introducedIn, object: kt:u-net-convolutional-networks-for-biomedical-image-segmentation}
  - {predicate: createdBy, object: kt:olaf-ronneberger}
  - {predicate: extends, object: kt:fully-convolutional-network}
  - {predicate: hasPart, object: kt:transposed-convolution}
  - {predicate: usedIn, object: kt:medical-image-analysis}
  - {predicate: usedIn, object: kt:latent-diffusion-model}
sources:
  - id: s1
    title: "U-Net: Convolutional Networks for Biomedical Image Segmentation"
    publisher: Ronneberger, Fischer and Brox, arXiv:1505.04597 (authors' version, ar5iv rendering)
    url: https://ar5iv.labs.arxiv.org/html/1505.04597
    type: primary
    accessed: 2026-11-16
  - id: s2
    title: "U-Net: Convolutional Networks for Biomedical Image Segmentation (project page)"
    publisher: Computer Vision Group, University of Freiburg
    url: https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/
    type: academic
    accessed: 2026-11-16
  - id: s3
    title: "14.11. Fully Convolutional Networks"
    publisher: Dive into Deep Learning (d2l.ai)
    url: https://d2l.ai/chapter_computer-vision/fcn.html
    type: textbook
    accessed: 2026-11-16
  - id: s4
    title: "nnU-Net: Self-adapting Framework for U-Net-Based Medical Image Segmentation"
    publisher: Isensee et al., German Cancer Research Center (DKFZ), arXiv:1809.10486
    url: https://ar5iv.labs.arxiv.org/html/1809.10486
    type: primary
    accessed: 2026-11-16
  - id: s5
    title: "High-Resolution Image Synthesis with Latent Diffusion Models"
    publisher: Rombach, Blattmann, Lorenz, Esser and Ommer, arXiv:2112.10752 (CVPR 2022)
    url: https://arxiv.org/pdf/2112.10752
    type: primary
    accessed: 2026-11-16
created: 2026-11-16
---

# U-Net

U-Net is a convolutional network for dense, per-pixel prediction, built as a "U": a contracting (encoder) path that progressively downsamples the image to capture context, and a roughly symmetric expanding (decoder) path that upsamples back to full resolution for precise localization.[^s1] It was introduced by Olaf Ronneberger, Philipp Fischer and Thomas Brox of the University of Freiburg, first posted on arXiv in May 2015 and published at MICCAI 2015 (Springer LNCS vol. 9351, pp. 234–241).[^s1][^s2] Its defining trait is that each decoder stage concatenates the feature map from the encoder stage at the same scale, so fine spatial detail lost by pooling is handed straight to the layers that reconstruct the segmentation mask.[^s1]

## Origin

U-Net was designed for biomedical segmentation, where annotated images are scarce. The authors built on the fully convolutional network (FCN) of Long, Shelhamer and Darrell, which replaces a classifier's dense layers so the network outputs a class score per pixel and uses learned upsampling to restore resolution.[^s1][^s3] U-Net's changes were a much wider upsampling path with many feature channels, a near-symmetric shape, and skip connections combining high-resolution encoder features with upsampled decoder features.[^s1] The paper reported beating the previous best sliding-window convolutional method on the ISBI electron-microscopy neuron-segmentation challenge, and the same network won the ISBI 2015 cell-tracking challenge in the phase-contrast and DIC categories by a large margin.[^s1][^s2] The authors released Caffe-based code and trained weights.[^s2]

## How it works

The encoder repeats a block of two unpadded 3×3 convolutions, each followed by a ReLU, then a 2×2 max-pool with stride 2; the channel count doubles at every downsampling step.[^s1] Each decoder step upsamples, applies a 2×2 "up-convolution" that halves the channels, concatenates the (cropped) encoder map of matching scale, and applies two more 3×3 convolutions with ReLU. A final 1×1 convolution maps each 64-channel feature vector to class scores; the original network has 23 convolutional layers and no fully connected layers.[^s1] Learned upsampling of this kind is usually implemented as a transposed convolution, which can be initialized to perform bilinear interpolation, and a 1×1 convolution acts as a per-pixel classifier.[^s3]

Three training details mattered as much as the shape. An overlap-tile strategy predicts only pixels whose full context is in the input tile and mirrors the image at borders, so arbitrarily large images can be segmented tile by tile.[^s1] Heavy augmentation with random elastic deformations (displacements on a coarse 3×3 grid, 10-pixel standard deviation) plus dropout at the end of the encoder let the model learn from very few labeled images.[^s1] And a pixel-wise weighted cross-entropy loss up-weights the thin borders between touching cells, forcing the model to separate adjacent objects.[^s1] The authors reported that segmenting a 512×512 image took under a second on a GPU of the time.[^s1]

## Limitations and evolution

The original design used unpadded convolutions, so the output map is smaller than the input and skip features must be cropped; many later implementations pad instead. Training used a batch size of one image with high momentum (0.99), a choice tied to the large tiles and 2015-era GPU memory.[^s1] A recurring finding is that U-Net variants often differ less than their pipelines do: the nnU-Net work from the German Cancer Research Center (2018) kept a nearly standard 2D/3D U-Net and a cascaded 3D variant, automated preprocessing, training, inference and postprocessing per dataset, and reported the top mean Dice scores on the Medical Segmentation Decathlon's phase-1 leaderboard at submission time, arguing that non-architectural choices have the larger impact.[^s4]

## In practice

U-Net remains a default baseline for medical and scientific image segmentation.[^s4] It also became the standard denoising backbone of image diffusion models: the latent diffusion model behind Stable Diffusion realizes its denoiser as a time-conditional U-Net made mostly of 2D convolutions, and injects text or other conditioning into the U-Net's intermediate layers via cross-attention, noting that earlier diffusion work used U-Net backbones too.[^s5]

## Connections

U-Net is a kind of **convolutional neural network** that **extends** the **fully convolutional network** idea for **semantic segmentation**, and it **has as a part** the **transposed convolution** used for upsampling.[^s1][^s3] It was **introduced in** the 2015 MICCAI paper and **created by** Olaf Ronneberger with Fischer and Brox.[^s1][^s2] Its concatenating skip connections differ from the additive shortcuts of a **residual connection** but play a related role of carrying information across depth, while **dropout** and elastic **data augmentation** were central to its small-data training.[^s1] It is **used in** **medical image analysis**, where nnU-Net systematized it,[^s4] and as the denoising network of many **diffusion model** systems, including the **latent diffusion model**.[^s5]

## Sources
[^s1]: Ronneberger, Fischer and Brox, "U-Net: Convolutional Networks for Biomedical Image Segmentation", arXiv:1505.04597 / MICCAI 2015. https://ar5iv.labs.arxiv.org/html/1505.04597 (accessed 2026-11-16)
[^s2]: University of Freiburg Computer Vision Group, U-Net project page. https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/ (accessed 2026-11-16)
[^s3]: Zhang et al., Dive into Deep Learning, "14.11. Fully Convolutional Networks". https://d2l.ai/chapter_computer-vision/fcn.html (accessed 2026-11-16)
[^s4]: Isensee et al., "nnU-Net: Self-adapting Framework for U-Net-Based Medical Image Segmentation", arXiv:1809.10486. https://ar5iv.labs.arxiv.org/html/1809.10486 (accessed 2026-11-16)
[^s5]: Rombach et al., "High-Resolution Image Synthesis with Latent Diffusion Models", arXiv:2112.10752 (CVPR 2022). https://arxiv.org/pdf/2112.10752 (accessed 2026-11-16)
