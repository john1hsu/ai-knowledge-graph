---
id: kt:vision-transformer
type: Architecture
title: Vision transformer
aliases: [ViT, vision transformers, visual transformer backbone]
domain: computer-vision-and-multimodal
summary: >-
  A family of image models that apply Transformer self-attention to a sequence of image-patch tokens
  instead of using convolutions, spanning the plain ViT, data-efficient variants such as DeiT, hierarchical
  windowed designs such as Swin, and self-supervised ViT backbones used for classification, detection,
  segmentation and as the vision encoder of multimodal models.
maturity: established
broader: [kt:transformer-architecture, kt:computer-vision]
related: [kt:image-classification, kt:swin-transformer, kt:clip, kt:knowledge-distillation]
relations:
  - {predicate: introducedIn, object: kt:an-image-is-worth-16x16-words}
  - {predicate: basedOn, object: kt:self-attention}
  - {predicate: alternativeTo, object: kt:convolutional-neural-network}
  - {predicate: usedIn, object: kt:object-detection}
  - {predicate: trainedWith, object: kt:masked-autoencoder}
  - {predicate: enables, object: kt:vision-language-model}
sources:
  - id: s1
    title: "Training data-efficient image transformers & distillation through attention"
    publisher: Touvron, Cord, Douze, Massa, Sablayrolles and Jégou, Proceedings of the 38th ICML, PMLR 139:10347-10357, 2021
    url: https://proceedings.mlr.press/v139/touvron21a.html
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s2
    title: "Swin Transformer: Hierarchical Vision Transformer using Shifted Windows"
    publisher: Liu, Lin, Cao, Hu, Wei, Zhang, Lin and Guo (Microsoft Research Asia), ICCV 2021, CVF Open Access
    url: https://openaccess.thecvf.com/content/ICCV2021/papers/Liu_Swin_Transformer_Hierarchical_Vision_Transformer_Using_Shifted_Windows_ICCV_2021_paper.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "Masked Autoencoders Are Scalable Vision Learners"
    publisher: He, Chen, Xie, Li, Dollár and Girshick, CVPR 2022, CVF Open Access
    url: https://openaccess.thecvf.com/content/CVPR2022/html/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "Exploring Plain Vision Transformer Backbones for Object Detection"
    publisher: Li, Mao, Girshick and He, ECCV 2022, ECVA
    url: https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/2151_ECCV_2022_paper.php
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "A ConvNet for the 2020s"
    publisher: Liu, Mao, Wu, Feichtenhofer, Darrell and Xie, CVPR 2022, CVF Open Access
    url: https://openaccess.thecvf.com/content/CVPR2022/html/Liu_A_ConvNet_for_the_2020s_CVPR_2022_paper.html
    type: peer-reviewed
    accessed: 2026-11-14
created: 2026-11-14
---

# Vision transformer

A vision transformer is an image model whose core computation is Transformer self-attention over a sequence of tokens cut from the image, rather than stacked convolutions. The term names both the specific ViT model from Dosovitskiy et al. (covered in its own paper node) and the broader architecture family that grew from it between 2020 and 2022: data-efficient ViTs, hierarchical windowed transformers, and plain ViTs pre-trained with self-supervision.[^s1][^s2][^s3] By the early 2020s these models had displaced convolutional networks as the leading image classifiers, although, as discussed below, that lead was later contested.[^s5]

## How the family works

Every member turns pixels into tokens. A plain ViT splits the image into fixed-size patches, projects each patch to an embedding, adds position information and runs a standard Transformer encoder over the resulting sequence; all tokens share one resolution throughout the network.[^s4] Because global self-attention compares every token with every other one, its cost grows quadratically with the number of patches, which is what most later designs try to tame.[^s2]

Three design lines dominate:

- **Data-efficient plain ViTs.** DeiT (Touvron et al., ICML 2021) showed that a convolution-free ViT can be trained competitively on ImageNet alone, on a single machine in under three days, reaching 83.1% top-1 with an 86M-parameter model (as reported in 2021).[^s1]
- **Distillation through attention.** DeiT also added a dedicated distillation token so the student learns from a teacher, typically a convnet, through attention; this raised its reported top-1 to 85.2%.[^s1]
- **Hierarchical, windowed ViTs.** Swin Transformer (Microsoft Research Asia, ICCV 2021) starts from 4×4-pixel patches and uses patch-merging layers to halve resolution and double channel width across four stages, giving CNN-like multi-scale feature maps.[^s2]
- **Shifted windows.** Swin computes self-attention only inside local windows (default 7×7 patches), so cost grows linearly with image size, and shifts the window grid between consecutive blocks so information still crosses window borders.[^s2]
- **Self-supervised plain ViTs.** Masked autoencoders (MAE, CVPR 2022) hide about 75% of patches, encode only the visible ones and reconstruct the rest with a light decoder; the authors report at least 3x faster training and 87.8% ImageNet-1K accuracy for a vanilla ViT-Huge using only ImageNet-1K data.[^s3]

## Backbones beyond classification

Dense tasks such as detection and segmentation need multi-scale features, which plain ViTs lack. Swin's hierarchy let it slot into feature-pyramid and U-Net style heads, and its authors reported 58.7 box AP and 51.1 mask AP on COCO test-dev and 53.5 mIoU on ADE20K with its largest model (2021 figures).[^s2] ViTDet later showed that hierarchy is not strictly required: a plain, MAE-pretrained ViT with a simple pyramid built from its single-scale output, window attention and a few cross-window propagation blocks reached up to 61.3 box AP on COCO with only ImageNet-1K pre-training (2022 figures).[^s4] This decoupling matters in practice, because one plain ViT can be pre-trained once and reused across tasks with minimal changes.[^s4]

## Limitations and the convnet response

The family's main costs are its appetite for data or heavy training recipes, which DeiT addressed with stronger augmentation and distillation, and the quadratic attention cost at high resolution, which windowing addresses at the price of reintroducing locality priors.[^s1][^s2] That trade-off fed a critique. The ConvNeXt authors argued that hierarchical transformers succeed largely by borrowing convolutional design ideas, and that the inductive biases of convolution are undervalued; by modernizing a ResNet step by step toward transformer-style design, they built a pure ConvNet family reaching 87.8% ImageNet top-1 and outperforming Swin on COCO detection and ADE20K segmentation (as reported in 2022).[^s5] The open question since has been less "attention or convolution" than which training recipe, scale and architectural priors matter most.[^s5]

## Connections

The vision transformer is a specialization of the **transformer architecture** and part of **computer vision**, **based on** **self-attention** and **introduced in** *An Image Is Worth 16x16 Words*.[^s4] It stands as an **alternative to** the **convolutional neural network**, a rivalry the ConvNeXt work reframes.[^s5] Its line includes the **Swin Transformer** and DeiT, whose recipe draws on **knowledge distillation**; it is commonly **trained with** **masked autoencoders** and **used in** **object detection** through backbones such as ViTDet.[^s1][^s2][^s3][^s4] Its first and most benchmarked task is **image classification**, where DeiT and MAE report their headline results.[^s1][^s3] The edges to **CLIP** and **vision-language models**, which this node **enables**, record that such models use patch-token image encoders of this kind; the details are covered in those nodes.

## Sources

[^s1]: Touvron et al., "Training data-efficient image transformers & distillation through attention", ICML 2021, PMLR 139. https://proceedings.mlr.press/v139/touvron21a.html (accessed 2026-11-14)
[^s2]: Liu et al., "Swin Transformer: Hierarchical Vision Transformer using Shifted Windows", ICCV 2021. https://openaccess.thecvf.com/content/ICCV2021/papers/Liu_Swin_Transformer_Hierarchical_Vision_Transformer_Using_Shifted_Windows_ICCV_2021_paper.pdf (accessed 2026-11-14)
[^s3]: He et al., "Masked Autoencoders Are Scalable Vision Learners", CVPR 2022. https://openaccess.thecvf.com/content/CVPR2022/html/He_Masked_Autoencoders_Are_Scalable_Vision_Learners_CVPR_2022_paper (accessed 2026-11-14)
[^s4]: Li, Mao, Girshick and He, "Exploring Plain Vision Transformer Backbones for Object Detection", ECCV 2022. https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/2151_ECCV_2022_paper.php (accessed 2026-11-14)
[^s5]: Liu et al., "A ConvNet for the 2020s", CVPR 2022. https://openaccess.thecvf.com/content/CVPR2022/html/Liu_A_ConvNet_for_the_2020s_CVPR_2022_paper.html (accessed 2026-11-14)
