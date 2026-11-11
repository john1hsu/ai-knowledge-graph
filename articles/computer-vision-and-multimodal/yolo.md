---
id: kt:yolo
type: Architecture
title: YOLO
aliases: [You Only Look Once, YOLO object detector, YOLO family of detectors]
domain: computer-vision-and-multimodal
summary: >-
  A family of single-stage, real-time object detectors, introduced by Redmon, Divvala, Girshick and Farhadi
  at CVPR 2016, that frames detection as one regression problem: a single convolutional network pass over
  the whole image predicts all bounding boxes and class probabilities at once.
maturity: established
broader: [kt:object-detection, kt:convolutional-neural-network]
related: [kt:deep-learning, kt:imagenet-and-alexnet, kt:quantization, kt:vision-transformer, kt:batch-normalization, kt:faster-r-cnn]
relations:
  - {predicate: introducedIn, object: kt:you-only-look-once-unified-real-time-object-detection}
  - {predicate: createdBy, object: kt:joseph-redmon}
  - {predicate: alternativeTo, object: kt:r-cnn}
  - {predicate: evaluatedOn, object: kt:ms-coco}
  - {predicate: usedIn, object: kt:autonomous-driving}
sources:
  - id: s1
    title: "You Only Look Once: Unified, Real-Time Object Detection"
    publisher: Redmon, Divvala, Girshick and Farhadi, CVPR 2016 (CVF Open Access)
    url: https://openaccess.thecvf.com/content_cvpr_2016/papers/Redmon_You_Only_Look_CVPR_2016_paper.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s2
    title: "YOLO9000: Better, Faster, Stronger"
    publisher: Redmon and Farhadi, CVPR 2017 (CVF Open Access)
    url: https://openaccess.thecvf.com/content_cvpr_2017/papers/Redmon_YOLO9000_Better_Faster_CVPR_2017_paper.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s3
    title: "YOLOv3: An Incremental Improvement"
    publisher: Redmon and Farhadi, arXiv 1804.02767, 2018 (technical report)
    url: https://arxiv.org/abs/1804.02767
    type: primary
    accessed: 2026-11-10
  - id: s4
    title: "YOLO advances to its genesis: a decadal and comprehensive review of the You Only Look Once (YOLO) series"
    publisher: Sapkota et al., Artificial Intelligence Review 58, article 274 (2025); authors' arXiv version 2406.19407
    url: https://arxiv.org/pdf/2406.19407
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s5
    title: "Ultralytics YOLO26"
    publisher: Ultralytics documentation
    url: https://docs.ultralytics.com/models/yolo26/
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# YOLO

**YOLO** ("You Only Look Once") is a family of real-time object detectors. The original paper, by Joseph Redmon, Santosh Divvala, Ross Girshick and Ali Farhadi (University of Washington, Allen Institute for AI and Facebook AI Research), appeared at CVPR 2016 and recast detection as a single regression problem that maps image pixels directly to bounding-box coordinates and class probabilities.[^s1] Because one network evaluation produces every detection, the whole pipeline can be trained end to end and run fast enough for video.[^s1]

## How it works

Earlier detectors chained separate stages. DPM slid a classifier across the image, and R-CNN scored roughly 2,000 Selective Search region proposals per image, taking over 40 seconds per image at test time.[^s1] YOLO replaced this pipeline with one convolutional network.[^s1]

The input image is divided into an S×S grid; the cell containing an object's centre is responsible for detecting it. Each cell predicts B boxes (x, y, width, height and a confidence score) and C class probabilities conditioned on an object being present, giving an output tensor of size S×S×(5B+C). For PASCAL VOC the authors used S=7, B=2 and C=20, a 7×7×30 tensor.[^s1] The network had 24 convolutional layers and 2 fully connected layers, loosely based on GoogLeNet; Fast YOLO used 9 convolutional layers.[^s1]

Training uses a sum-squared error loss with two weights: coordinate errors are scaled up (λ_coord = 5) and confidence errors for empty cells scaled down (λ_noobj = 0.5), so the many background cells do not swamp the gradient. The network predicts the square root of box width and height, so a given error matters more for a small box than for a large one.[^s1]

## Results and limitations

On PASCAL VOC 2007 (trained on 2007+2012), YOLO reached 63.4 mAP at 45 frames per second and Fast YOLO 52.7 mAP at 155 fps.[^s1] Its error profile differed from Fast R-CNN's: about 19% of its top detections were localization errors (versus 8.6%) but only about 4.75% were background false positives (versus 13.6%), because the network sees the whole image and so uses global context.[^s1] It also transferred better to artwork, losing far less accuracy than R-CNN on the Picasso and People-Art datasets.[^s1]

The authors listed clear weaknesses. Each grid cell predicts only two boxes and one class, so YOLO struggles with small objects in groups such as flocks of birds; it generalizes poorly to unusual aspect ratios; and coarse features after repeated downsampling hurt localization, which was its main error source.[^s1]

## Evolution of the family

YOLOv2 (CVPR 2017) added batch normalization, a higher-resolution classifier, anchor boxes whose shapes come from k-means clustering of training boxes, and multi-scale training; it reported 76.8 mAP at 67 fps on VOC 2007 at 416×416 input.[^s2] The same paper's YOLO9000 jointly trained on COCO detection and ImageNet classification data, merging labels through a WordTree hierarchy, to detect over 9,000 categories.[^s2] YOLOv3 (2018) made further incremental changes; its authors reported 28.2 mAP at 22 ms per 320×320 image and AP50 comparable to RetinaNet at about 3.8 times the speed.[^s3]

After v3, development passed to other groups, and version numbers no longer imply a single lineage. A 2025 review in *Artificial Intelligence Review* traces YOLOv4 (Bochkovskiy et al., 2020), YOLOv5 (Ultralytics, 2020), YOLOv6 (Meituan, 2022), YOLOv7 and YOLOv9 (Wang et al.), YOLOv8 and YOLO11 (Ultralytics, 2023 and 2024), YOLOv10 (Tsinghua, 2024) and YOLOv12 (2025).[^s4] It identifies three trends: anchor-free heads (YOLOv8), removal of non-maximum suppression (NMS) for end-to-end detection (YOLOv10), and growing use of attention (YOLO11, YOLOv12).[^s4]

## In practice

YOLO models are widely used where latency matters: the 2025 review surveys deployments in autonomous vehicles and traffic safety, medical imaging, manufacturing defect detection, surveillance and agriculture.[^s4] As of November 2026, Ultralytics documents YOLO26 in five sizes (n to x) for detection, segmentation, pose, classification and oriented boxes. Ultralytics reports COCO mAP50-95 from 40.9 (YOLO26n) to 57.5 (YOLO26x), an optional NMS-free end-to-end head, and up to 43% faster CPU inference than YOLO11n; these are vendor-reported figures.[^s5] The Ultralytics code is licensed under AGPL-3.0 or a commercial enterprise licence, which matters for closed-source products.[^s5]

## Connections

YOLO is a specific approach to **object detection** built from a **convolutional neural network**, and part of the **deep learning** turn in computer vision.[^s1] It was **introduced in** the CVPR 2016 paper and **created by** Joseph Redmon and colleagues.[^s1] It is the main single-stage **alternative to** the two-stage **R-CNN** family, trading some localization accuracy for speed.[^s1] Its backbones are pretrained on ImageNet classification, linking it to **ImageNet and AlexNet**, and YOLOv2 adopted **batch normalization**.[^s2] Recent versions are **evaluated on** MS COCO, borrow attention ideas related to the **Vision Transformer**, and target edge devices through low-precision **quantization**, while **autonomous driving** is a leading application.[^s4][^s5]

## Sources
[^s1]: Redmon, Divvala, Girshick and Farhadi, "You Only Look Once: Unified, Real-Time Object Detection", CVPR 2016. https://openaccess.thecvf.com/content_cvpr_2016/papers/Redmon_You_Only_Look_CVPR_2016_paper.pdf (accessed 2026-11-10)
[^s2]: Redmon and Farhadi, "YOLO9000: Better, Faster, Stronger", CVPR 2017. https://openaccess.thecvf.com/content_cvpr_2017/papers/Redmon_YOLO9000_Better_Faster_CVPR_2017_paper.pdf (accessed 2026-11-10)
[^s3]: Redmon and Farhadi, "YOLOv3: An Incremental Improvement", arXiv 1804.02767, 2018. https://arxiv.org/abs/1804.02767 (accessed 2026-11-10)
[^s4]: Sapkota et al., "YOLO advances to its genesis: a decadal and comprehensive review of the You Only Look Once (YOLO) series", Artificial Intelligence Review 58:274, 2025 (arXiv 2406.19407). https://arxiv.org/pdf/2406.19407 (accessed 2026-11-10)
[^s5]: Ultralytics, "Ultralytics YOLO26", Ultralytics documentation. https://docs.ultralytics.com/models/yolo26/ (accessed 2026-11-10)
