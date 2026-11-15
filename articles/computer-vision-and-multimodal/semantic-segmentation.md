---
id: kt:semantic-segmentation
type: Application
title: Semantic segmentation
aliases: [pixel-wise classification, dense semantic labeling, scene parsing]
domain: computer-vision-and-multimodal
summary: >-
  The dense-prediction computer vision task of assigning a semantic class label to every pixel of an
  image, producing a label map the same size as the input; it refines object detection's bounding
  boxes into exact region boundaries but does not separate individual object instances.
maturity: established
broader: [kt:computer-vision]
related: [kt:convolutional-neural-network, kt:object-detection, kt:image-classification, kt:u-net, kt:vision-transformer]
relations:
  - {predicate: contrastsWith, object: kt:instance-segmentation}
  - {predicate: hasPart, object: kt:transposed-convolution}
  - {predicate: evaluatedOn, object: kt:pascal-voc}
  - {predicate: evaluatedOn, object: kt:cityscapes}
  - {predicate: usedIn, object: kt:autonomous-driving}
  - {predicate: usedIn, object: kt:medical-image-analysis}
sources:
  - id: s1
    title: "14.9. Semantic Segmentation and the Dataset"
    publisher: Dive into Deep Learning (d2l.ai)
    url: https://www.d2l.ai/chapter_computer-vision/semantic-segmentation-and-dataset.html
    type: textbook
    accessed: 2026-11-15
  - id: s2
    title: "14.11. Fully Convolutional Networks"
    publisher: Dive into Deep Learning (d2l.ai)
    url: https://d2l.ai/chapter_computer-vision/fcn.html
    type: textbook
    accessed: 2026-11-15
  - id: s3
    title: "Fully Convolutional Networks for Semantic Segmentation"
    publisher: CVPR 2015 (Long, Shelhamer and Darrell), CVF Open Access
    url: https://openaccess.thecvf.com/content_cvpr_2015/html/Long_Fully_Convolutional_Networks_2015_CVPR_paper.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "U-Net: Convolutional Networks for Biomedical Image Segmentation"
    publisher: Ronneberger, Fischer and Brox, arXiv:1505.04597 (authors' version)
    url: https://arxiv.org/abs/1505.04597
    type: primary
    accessed: 2026-11-15
  - id: s5
    title: "DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs"
    publisher: Chen, Papandreou, Kokkinos, Murphy and Yuille, arXiv:1606.00915v2 (authors' version)
    url: https://arxiv.org/abs/1606.00915v2
    type: primary
    accessed: 2026-11-15
  - id: s6
    title: "Panoptic Segmentation"
    publisher: CVPR 2019 (Kirillov, He, Girshick, Rother and Dollár), CVF Open Access
    url: https://openaccess.thecvf.com/content_CVPR_2019/papers/Kirillov_Panoptic_Segmentation_CVPR_2019_paper.pdf
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Semantic segmentation

**Semantic segmentation** is the computer vision task of labeling every pixel of an image with the semantic class it belongs to, such as road, person, dog or sky. Where object detection marks objects with rectangular boxes, semantic segmentation predicts at pixel level and so recovers much finer boundaries.[^s1] The output is a label map with the same height and width as the input, in which pixels of the same class share one label.[^s1]

It sits between two neighbouring tasks. Classical *image segmentation* only splits an image into regions using correlations between pixels, without class labels, so its regions need not correspond to meaningful categories. *Instance segmentation* goes further than semantic segmentation by also telling apart individual objects of the same class: with two dogs in a frame, a semantic map marks both as "dog", while an instance map says which dog each pixel belongs to.[^s1] *Panoptic segmentation*, proposed by Kirillov and colleagues at Facebook AI Research in 2019, unifies the two by giving every pixel both a class label and an instance ID, with IDs ignored for amorphous "stuff" classes like grass or sky and used for countable "things" like people and cars.[^s6]

## How it works

The modern deep-learning approach dates to **fully convolutional networks (FCNs)** by Long, Shelhamer and Darrell (CVPR 2015). They showed that classification networks such as AlexNet, VGG and GoogLeNet could be converted into networks that take inputs of any size and produce correspondingly sized outputs, then fine-tuned end-to-end, pixels to pixels. A skip architecture combined coarse, deep semantic features with shallow, fine appearance features to sharpen boundaries. The paper reported 62.2% mean IU on PASCAL VOC 2012, roughly a 20% relative improvement over prior work, with inference under a fifth of a second per image.[^s3]

The *Dive into Deep Learning* textbook gives a compact recipe for an FCN. A pretrained ResNet-18 backbone, with its pooling and fully connected head removed, turns a 320×480 image into a 512×10×15 feature map (1/32 resolution). A 1×1 convolution maps those 512 channels to one channel per class (21 for Pascal VOC), and a transposed convolution with stride 32, initialized with bilinear-interpolation weights, upsamples back to full resolution. Training uses cross-entropy loss computed at every pixel and averaged over the image; at inference the argmax over channels gives each pixel's class.[^s2]

Later architectures attacked the tension between context and resolution. **U-Net** (Ronneberger, Fischer and Brox, 2015) pairs a contracting path that captures context with a symmetric expanding path for precise localization, and leans on heavy data augmentation so it can be trained from very few annotated images; it won the ISBI 2015 cell-tracking challenge in two microscopy categories by a large margin.[^s4] **DeepLab** (Chen et al.) introduced atrous (dilated) convolution to enlarge the field of view without extra parameters, atrous spatial pyramid pooling to handle objects at several scales, and a fully connected conditional random field to restore boundaries blurred by downsampling, reporting 79.7% mIOU on the PASCAL VOC 2012 test set.[^s5]

## Data, metrics and limitations

Pascal VOC 2012 is one of the most important benchmarks: 20 object classes plus background, with labels stored as images the same size as their inputs.[^s1] Urban-scene datasets such as Cityscapes (5,000 driving images, 19 classes) and ADE20k (over 25,000 densely annotated images) broadened evaluation to cluttered real-world scenes.[^s6] Performance is usually reported as mean intersection-over-union (mIoU) across classes;[^s3] panoptic quality (PQ) extends evaluation to instances by matching segments at IoU above 0.5 and factoring into segmentation and recognition quality.[^s6]

Practical difficulties follow from the dense output. Labels are expensive to produce, which is why data-efficient designs like U-Net matter.[^s4] Preprocessing must keep image and label aligned: the textbook pipeline crops both identically rather than rescaling, because mapping rescaled predictions back to the original size is inaccurate at class boundaries.[^s1] Repeated pooling trades spatial detail for context, the core problem that skip connections, atrous convolution and CRF post-processing each try to solve.[^s3][^s5] And because semantic maps merge touching objects of one class, applications that must count or track objects need instance or panoptic segmentation instead.[^s6]

## Connections

Semantic segmentation is a core task of **computer vision** and extends **image classification** from one label per image to one label per pixel, while contrasting with **object detection**'s box outputs and with instance segmentation's per-object masks.[^s1] Its methods are built on **convolutional neural network** backbones and depend on upsampling layers such as the transposed convolution;[^s2][^s3] U-Net is the dominant design in medical image analysis,[^s4] and driving datasets like Cityscapes tie the task to autonomous driving.[^s6] Transformer backbones such as the **vision transformer** are a more recent alternative to convolutional encoders for the same dense-prediction role.

## Sources
[^s1]: Dive into Deep Learning, "14.9. Semantic Segmentation and the Dataset". https://www.d2l.ai/chapter_computer-vision/semantic-segmentation-and-dataset.html (accessed 2026-11-15)
[^s2]: Dive into Deep Learning, "14.11. Fully Convolutional Networks". https://d2l.ai/chapter_computer-vision/fcn.html (accessed 2026-11-15)
[^s3]: Long, Shelhamer and Darrell, "Fully Convolutional Networks for Semantic Segmentation", CVPR 2015. https://openaccess.thecvf.com/content_cvpr_2015/html/Long_Fully_Convolutional_Networks_2015_CVPR_paper.html (accessed 2026-11-15)
[^s4]: Ronneberger, Fischer and Brox, "U-Net: Convolutional Networks for Biomedical Image Segmentation", arXiv:1505.04597, 2015. https://arxiv.org/abs/1505.04597 (accessed 2026-11-15)
[^s5]: Chen et al., "DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs", arXiv:1606.00915v2. https://arxiv.org/abs/1606.00915v2 (accessed 2026-11-15)
[^s6]: Kirillov et al., "Panoptic Segmentation", CVPR 2019. https://openaccess.thecvf.com/content_CVPR_2019/papers/Kirillov_Panoptic_Segmentation_CVPR_2019_paper.pdf (accessed 2026-11-15)
