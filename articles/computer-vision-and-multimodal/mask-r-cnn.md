---
id: kt:mask-r-cnn
type: Architecture
title: Mask R-CNN
aliases: [Mask RCNN, Mask Region-based Convolutional Neural Network]
domain: computer-vision-and-multimodal
summary: >-
  A two-stage instance segmentation model, introduced by He, Gkioxari, Dollár and Girshick at ICCV 2017,
  that extends Faster R-CNN with a small fully convolutional branch predicting a binary mask for each
  detected object, and replaces RoI pooling with the quantization-free RoIAlign operation.
maturity: established
broader: [kt:instance-segmentation, kt:r-cnn]
related: [kt:object-detection, kt:semantic-segmentation, kt:residual-connection, kt:human-pose-estimation]
relations:
  - {predicate: extends, object: kt:faster-r-cnn}
  - {predicate: createdBy, object: kt:meta-ai}
  - {predicate: dependsOn, object: kt:feature-pyramid-network}
  - {predicate: evaluatedOn, object: kt:ms-coco}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: implementedIn, object: kt:detectron2}
sources:
  - id: s1
    title: "Mask R-CNN"
    publisher: He, Gkioxari, Dollár and Girshick, ICCV 2017, pp. 2961-2969 (CVF Open Access)
    url: https://openaccess.thecvf.com/content_iccv_2017/html/He_Mask_R-CNN_ICCV_2017_paper.html
    type: peer-reviewed
    accessed: 2026-11-23
  - id: s2
    title: "Mask R-CNN (arXiv 1703.06870v3)"
    publisher: He, Gkioxari, Dollár and Girshick (authors' arXiv version)
    url: https://arxiv.org/abs/1703.06870v3
    type: primary
    accessed: 2026-11-23
  - id: s3
    title: "Mask R-CNN (full text, ar5iv rendering of arXiv 1703.06870)"
    publisher: He, Gkioxari, Dollár and Girshick (arXiv, rendered by ar5iv)
    url: https://ar5iv.labs.arxiv.org/html/1703.06870
    type: primary
    accessed: 2026-11-23
  - id: s4
    title: "torchvision.models.detection.maskrcnn_resnet50_fpn"
    publisher: PyTorch (torchvision documentation)
    url: https://docs.pytorch.org/vision/master/models/generated/torchvision.models.detection.maskrcnn_resnet50_fpn.html
    type: official-docs
    accessed: 2026-11-23
  - id: s5
    title: "Detectron2"
    publisher: Meta AI (Facebook AI Research)
    url: https://ai.meta.com/tools/detectron2/
    type: lab-research
    accessed: 2026-11-23
created: 2026-11-23
---

# Mask R-CNN

**Mask R-CNN** is a model for instance segmentation: it finds each object in an image, labels it, and outlines it with its own pixel mask. Kaiming He, Georgia Gkioxari, Piotr Dollár and Ross Girshick of Facebook AI Research introduced it in a paper first posted to arXiv on 20 March 2017 and published at ICCV 2017.[^s1][^s2] The idea is deliberately simple: take the Faster R-CNN detector and add a third output branch, running in parallel with the existing classification and box-regression branches, that predicts a segmentation mask for every region of interest (RoI).[^s1] The authors reported that the extra branch adds only a small overhead, that the system runs at about 5 frames per second, and that the same framework extends to human pose (keypoint) estimation.[^s1]

## How it works

The first stage is unchanged from Faster R-CNN: a region proposal network suggests candidate boxes from a shared convolutional feature map.[^s3] In the second stage each RoI feeds three heads. The mask head is a small fully convolutional network that outputs *K* binary masks of size *m*×*m*, one per class, so it produces *Km*² values per RoI.[^s3] Training minimizes a multi-task loss per RoI, *L* = *L*cls + *L*box + *L*mask, where the mask term is the average binary cross-entropy after a per-pixel sigmoid, computed only on the mask for the RoI's ground-truth class.[^s3]

This **decouples** mask prediction from classification: the classifier decides *what* the object is, and the mask head only has to decide, for that class, which pixels belong to it. The paper's ablation on a ResNet-50-C4 model shows why it matters: a per-pixel softmax across classes reached 24.8 mask AP, while independent per-class sigmoids reached 30.3, a gain of 5.5 points.[^s3]

## RoIAlign

The second key change concerns how features are cut out for each region. Earlier RoI pooling rounds the region's coordinates and its sub-bins to the feature-map grid, and the resulting misalignment between features and image matters little for box labels but hurts pixel-accurate masks.[^s3] **RoIAlign** removes all rounding: it keeps fractional coordinates (for example *x*/16 rather than a rounded value), samples four regular points in each bin with bilinear interpolation, and then aggregates them by max or average.[^s3] In the ablation, RoIPool scored 26.9 mask AP and RoIAlign 30.3, with the larger jump at the strict AP75 threshold (26.4 to 31.5); the authors summarize the gain as roughly 3 AP and 5 AP75, and say it improves mask accuracy by 10% to 50% in relative terms.[^s3]

## Results

On COCO test-dev, the paper's single-model results were 35.7 mask AP with a ResNet-101 feature pyramid network (FPN) backbone and 37.1 with ResNeXt-101-FPN, ahead of the 2015 challenge winner MNC (24.6) and the 2016 winner FCIS+++ (33.6).[^s3] Backbone choice mattered: on the validation ablation, mask AP rose from 30.3 with ResNet-50-C4 to 33.6 with ResNet-50-FPN and 36.7 with ResNeXt-101-FPN.[^s3] At inference the mask branch runs only on the top 100 detections, and its soft masks are binarized at 0.5; the authors put the added cost at about 20% on typical models, with whole-image inference around 200 ms on a GPU and training taking one to two days on one 8-GPU machine.[^s3] The paper presents these as wins over prior single-model entries without extra tricks, not as a final ceiling.[^s1]

## Limitations

Mask R-CNN keeps the two-stage pipeline of its parent, so its reported speed of about 5 frames per second is far from real time for video.[^s1] Each mask is a fixed *m*×*m* grid predicted inside its box, and masks exist only for the *K* classes the model was trained on, since the head emits one mask per class.[^s3]

## In practice

Mask R-CNN became a standard baseline for instance segmentation. Meta's Detectron2 library, described by Meta as FAIR's next-generation platform for detection and segmentation, implements it alongside Faster R-CNN, RetinaNet and PointRend.[^s5] PyTorch's torchvision ships `maskrcnn_resnet50_fpn`; as of its current documentation the COCO weights score 37.9 box mAP and 34.6 mask mAP on COCO val2017, with about 44.4 million parameters, and the model returns boxes, labels, scores and per-object soft masks to threshold at 0.5.[^s4]

## Connections

Mask R-CNN is a method for **instance segmentation** and a descendant of the **R-CNN** family through Faster R-CNN.[^s1] It **extends** **Faster R-CNN** with a mask branch and RoIAlign, so it performs **object detection** and per-pixel labelling at once, linking detection with **semantic segmentation**.[^s3] It was **created by** researchers at Facebook AI Research, now part of **Meta AI**.[^s1][^s5] Its strongest variants **depend on** a **feature pyramid network** over deep ResNet or ResNeXt backbones built with **residual connections**, and it was **evaluated on** **MS COCO**.[^s3] The same framework carries over to **human pose estimation**, where the paper's keypoint variant also runs at about 5 fps.[^s1][^s3] Reference versions are **implemented in** **PyTorch**'s torchvision and in **Detectron2**.[^s4][^s5]

## Sources
[^s1]: He, Gkioxari, Dollár and Girshick, "Mask R-CNN", ICCV 2017. https://openaccess.thecvf.com/content_iccv_2017/html/He_Mask_R-CNN_ICCV_2017_paper.html (accessed 2026-11-23)
[^s2]: He, Gkioxari, Dollár and Girshick, "Mask R-CNN", arXiv 1703.06870v3. https://arxiv.org/abs/1703.06870v3 (accessed 2026-11-23)
[^s3]: He, Gkioxari, Dollár and Girshick, "Mask R-CNN", full text via ar5iv. https://ar5iv.labs.arxiv.org/html/1703.06870 (accessed 2026-11-23)
[^s4]: PyTorch, "torchvision.models.detection.maskrcnn_resnet50_fpn". https://docs.pytorch.org/vision/master/models/generated/torchvision.models.detection.maskrcnn_resnet50_fpn.html (accessed 2026-11-23)
[^s5]: Meta AI, "Detectron2". https://ai.meta.com/tools/detectron2/ (accessed 2026-11-23)
