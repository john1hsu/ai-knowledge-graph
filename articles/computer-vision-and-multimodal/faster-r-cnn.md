---
id: kt:faster-r-cnn
type: Architecture
title: Faster R-CNN
aliases: [Faster RCNN, Faster Region-based Convolutional Neural Network]
domain: computer-vision-and-multimodal
summary: >-
  A two-stage object detector, introduced by Ren, He, Girshick and Sun at NIPS 2015, that adds a Region
  Proposal Network sharing convolutional features with a Fast R-CNN detection head, making region proposals
  nearly free and letting the whole detector run at about 5 frames per second on a GPU.
maturity: established
broader: [kt:object-detection, kt:r-cnn]
related: [kt:yolo, kt:convolutional-neural-network, kt:imagenet-and-alexnet, kt:deep-learning]
relations:
  - {predicate: introducedIn, object: kt:faster-r-cnn-towards-real-time-object-detection-with-region-proposal-networks}
  - {predicate: extends, object: kt:fast-r-cnn}
  - {predicate: followedBy, object: kt:mask-r-cnn}
  - {predicate: alternativeTo, object: kt:yolo}
  - {predicate: evaluatedOn, object: kt:ms-coco}
  - {predicate: implementedIn, object: kt:pytorch}
sources:
  - id: s1
    title: "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks"
    publisher: Ren, He, Girshick and Sun, Advances in Neural Information Processing Systems 28 (NIPS 2015)
    url: https://papers.nips.cc/paper/2015/hash/14bfa6bb14875e45bba028a21ed38046-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks (arXiv v3)"
    publisher: Ren, He, Girshick and Sun (authors' arXiv version, 1506.01497v3)
    url: https://arxiv.org/pdf/1506.01497v3
    type: primary
    accessed: 2026-11-11
  - id: s3
    title: "Fast R-CNN"
    publisher: Ross Girshick, ICCV 2015 (CVF Open Access)
    url: https://openaccess.thecvf.com/content_iccv_2015/html/Girshick_Fast_R-CNN_ICCV_2015_paper.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "14.8. Region-based CNNs (R-CNNs)"
    publisher: Dive into Deep Learning (d2l.ai)
    url: https://d2l.ai/chapter_computer-vision/rcnn.html
    type: textbook
    accessed: 2026-11-11
  - id: s5
    title: "Mask R-CNN"
    publisher: He, Gkioxari, Dollár and Girshick, ICCV 2017 (CVF Open Access)
    url: https://openaccess.thecvf.com/content_iccv_2017/html/He_Mask_R-CNN_ICCV_2017_paper.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s6
    title: "torchvision.models.detection.fasterrcnn_resnet50_fpn"
    publisher: PyTorch (torchvision documentation)
    url: https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.detection.fasterrcnn_resnet50_fpn.html
    type: official-docs
    accessed: 2026-11-11
created: 2026-11-11
---

# Faster R-CNN

**Faster R-CNN** is a two-stage convolutional object detector introduced by Shaoqing Ren, Kaiming He, Ross Girshick and Jian Sun at NIPS 2015.[^s1] Its contribution is the **Region Proposal Network (RPN)**, a small fully convolutional network that predicts object boxes and "objectness" scores at every feature-map position and shares its convolutional features with the detector, so proposing candidate regions costs almost nothing.[^s1] With a VGG-16 backbone the full system ran at about 5 frames per second on a GPU and reported 73.2% mAP on PASCAL VOC 2007 and 70.4% on VOC 2012, using 300 proposals per image.[^s1]

## Background: the R-CNN line

The original R-CNN used selective search to propose roughly 2,000 regions per image, ran a pretrained CNN separately on each one, classified them with SVMs and refined boxes with linear regression, which made it slow.[^s4] Fast R-CNN (Girshick, ICCV 2015) ran the CNN once over the whole image and pooled each region's features from the shared map with **RoI pooling**; it trained VGG-16 about 9 times faster and tested about 213 times faster than R-CNN.[^s3][^s4] That left the proposal step itself as the bottleneck: selective search took around 1.5 to 2 seconds per image on a CPU, while the detection network needed only a fraction of that on a GPU.[^s2]

## How it works

A backbone CNN computes a feature map for the image. The RPN slides a 3×3 window over that map; at each location it considers *k* reference boxes called **anchors**, centred on that location.[^s4] The paper uses k = 9 anchors per location (three scales, 128², 256² and 512² pixels, times three aspect ratios, 1:1, 1:2 and 2:1), and its output layers emit 2k objectness scores and 4k box-offset values.[^s2] Because the same anchors and weights apply at every position, the proposals are translation invariant, and the output layer needs only about 2.8×10⁴ parameters with VGG-16, versus about 6.1×10⁶ for the earlier MultiBox approach.[^s2]

Training labels an anchor positive if it has an IoU above 0.7 with a ground-truth box (or the highest IoU for that box) and negative if its IoU is below 0.3 with every box; the rest are ignored.[^s2] Each image contributes a minibatch of 256 sampled anchors, and the loss adds a two-class log loss to a smooth-L1 box-regression loss on positive anchors, weighted by λ = 10.[^s2] Overlapping proposals are pruned with non-maximum suppression at IoU 0.7, and the survivors feed the Fast R-CNN head through RoI pooling, which classifies each region and refines its box.[^s2][^s4] To make the two networks share layers, the authors used a four-step alternating scheme: train the RPN, train a detector on its proposals, then fine-tune the RPN-specific and detector-specific layers in turn on frozen shared layers.[^s2]

## Results and limitations

On a K40 GPU, VGG-16 with RPN took about 198 ms per image (10 ms of it for proposals) against about 1,830 ms with selective search; the smaller ZF network reached about 17 fps.[^s2] On MS COCO test-dev, the VGG-16 model scored 42.7 mAP@0.5 and 21.9 mAP@[.5,.95], and swapping in ResNet-101 raised COCO val results to 48.4 and 27.2.[^s2] Faster R-CNN and RPN were the basis of first-place entries in several ILSVRC and COCO 2015 tracks.[^s1] The limitation is speed: "real-time" in the title means roughly 5 fps with VGG-16, because every image still passes through two stages, proposal and per-region classification.[^s2]

## In practice

Faster R-CNN remains a standard baseline and building block. Mask R-CNN (He et al., ICCV 2017) extends it with a parallel branch that predicts a pixel mask for each detected object, adding little overhead and running at about 5 fps.[^s5] Mask R-CNN also replaces RoI pooling with RoI alignment, which uses bilinear interpolation to keep spatial detail.[^s4] PyTorch's torchvision library ships a `fasterrcnn_resnet50_fpn` model; as of its current documentation, the COCO-trained weights report 37.0 box mAP on COCO val2017 with about 41.8 million parameters, and training returns separate losses for the RPN and detection heads.[^s6]

## Connections

Faster R-CNN is an approach to **object detection** and the third member of the **R-CNN** family, built on a **convolutional neural network** within **deep learning**.[^s1][^s4] It was **introduced in** the NIPS 2015 paper and directly **extends** **Fast R-CNN** by replacing selective search with the RPN.[^s1][^s3] It was **followed by** **Mask R-CNN**, which adds instance segmentation.[^s5] It is the main two-stage **alternative to** single-stage **YOLO**, was **evaluated on** **MS COCO** and PASCAL VOC, and its backbones start from ImageNet-pretrained classifiers, tying it to **ImageNet and AlexNet**.[^s2] A widely used reference version is **implemented in** **PyTorch**'s torchvision.[^s6]

## Sources
[^s1]: Ren, He, Girshick and Sun, "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks", NIPS 2015. https://papers.nips.cc/paper/2015/hash/14bfa6bb14875e45bba028a21ed38046-Abstract.html (accessed 2026-11-11)
[^s2]: Ren, He, Girshick and Sun, arXiv 1506.01497v3. https://arxiv.org/pdf/1506.01497v3 (accessed 2026-11-11)
[^s3]: Girshick, "Fast R-CNN", ICCV 2015. https://openaccess.thecvf.com/content_iccv_2015/html/Girshick_Fast_R-CNN_ICCV_2015_paper.html (accessed 2026-11-11)
[^s4]: Dive into Deep Learning, "14.8. Region-based CNNs (R-CNNs)". https://d2l.ai/chapter_computer-vision/rcnn.html (accessed 2026-11-11)
[^s5]: He, Gkioxari, Dollár and Girshick, "Mask R-CNN", ICCV 2017. https://openaccess.thecvf.com/content_iccv_2017/html/He_Mask_R-CNN_ICCV_2017_paper.html (accessed 2026-11-11)
[^s6]: PyTorch, "torchvision.models.detection.fasterrcnn_resnet50_fpn". https://docs.pytorch.org/vision/stable/models/generated/torchvision.models.detection.fasterrcnn_resnet50_fpn.html (accessed 2026-11-11)
