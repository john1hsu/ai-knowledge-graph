---
id: kt:instance-segmentation
type: Application
title: Instance segmentation
aliases: [simultaneous detection and segmentation, object instance segmentation]
domain: computer-vision-and-multimodal
summary: >-
  The computer vision task of detecting every object instance in an image and outlining each one with
  its own pixel-level mask and class label, so that two objects of the same class are kept apart; it
  combines object detection's per-object outputs with semantic segmentation's per-pixel precision.
maturity: established
broader: [kt:computer-vision]
related: [kt:object-detection, kt:faster-r-cnn, kt:mask-r-cnn, kt:panoptic-segmentation, kt:segment-anything-model]
relations:
  - {predicate: contrastsWith, object: kt:semantic-segmentation}
  - {predicate: evaluatedOn, object: kt:ms-coco}
  - {predicate: evaluatedOn, object: kt:cityscapes}
  - {predicate: dependsOn, object: kt:convolutional-neural-network}
sources:
  - id: s1
    title: "14.9. Semantic Segmentation and the Dataset"
    publisher: Dive into Deep Learning (d2l.ai)
    url: https://www.d2l.ai/_sources/chapter_computer-vision/semantic-segmentation-and-dataset.rst.txt
    type: textbook
    accessed: 2026-11-19
  - id: s2
    title: "Simultaneous Detection and Segmentation (project page)"
    publisher: UC Berkeley EECS (Hariharan, Arbeláez, Girshick, Malik; ECCV 2014)
    url: https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/shape/sds
    type: academic
    accessed: 2026-11-19
  - id: s3
    title: "Mask R-CNN"
    publisher: ICCV 2017 (He, Gkioxari, Dollár, Girshick), CVF Open Access
    url: https://openaccess.thecvf.com/content_ICCV_2017/papers/He_Mask_R-CNN_ICCV_2017_paper.pdf
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s4
    title: "Panoptic Segmentation"
    publisher: CVPR 2019 (Kirillov, He, Girshick, Rother, Dollár), CVF Open Access
    url: https://openaccess.thecvf.com/content_CVPR_2019/papers/Kirillov_Panoptic_Segmentation_CVPR_2019_paper.pdf
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s5
    title: "Segment Anything"
    publisher: ICCV 2023 (Kirillov et al.), CVF Open Access
    url: https://openaccess.thecvf.com/content/ICCV2023/papers/Kirillov_Segment_Anything_ICCV_2023_paper.pdf
    type: peer-reviewed
    accessed: 2026-11-19
created: 2026-11-19
---

# Instance segmentation

Instance segmentation is the task of finding every object in an image and marking exactly which pixels belong to each individual object. The *Dive into Deep Learning* textbook separates three related problems: plain image segmentation splits an image into regions using pixel correlations and no labels; semantic segmentation tags every pixel with a class such as "dog" or "background"; and instance segmentation, also called simultaneous detection and segmentation, must additionally decide which of two dogs a given pixel belongs to.[^s1] In other words, it pairs the per-object outputs of object detection with the pixel-level boundaries of semantic segmentation.[^s3]

## Origin

The task was framed for deep learning as *Simultaneous Detection and Segmentation* (SDS) by Bharath Hariharan, Pablo Arbeláez, Ross Girshick and Jitendra Malik at ECCV 2014. Their system built on R-CNN: a convolutional network scored category-independent region proposals, and category-specific top-down figure-ground predictions refined those bottom-up proposals into masks.[^s2] Early successors followed a "segment-first" recipe, producing mask proposals and then classifying them, an ordering the Mask R-CNN authors later argued was slow and less accurate.[^s3]

## How it works

The dominant design for several years was detect-then-segment, exemplified by Mask R-CNN (He, Gkioxari, Dollár and Girshick, ICCV 2017). It adds a third branch to the two-stage Faster R-CNN detector: alongside the class and box heads, a small fully convolutional network predicts an m×m binary mask for every region of interest.[^s3] Two details mattered:

- **Decoupled masks.** Each class gets its own mask trained with a per-pixel sigmoid and binary cross-entropy, and the box head's predicted class picks which mask to use. Replacing this with a per-pixel softmax over classes cut COCO mask AP from 30.3 to 24.8 in the paper's ablation.[^s3]
- **RoIAlign.** The older RoIPool operation rounded region coordinates to the feature grid, misaligning features and pixels. RoIAlign samples features by bilinear interpolation instead, improving mask AP by about 3 points on a ResNet-50-C4 backbone and by 7.3 points on a coarser stride-32 backbone.[^s3]

In 2017 a ResNet-101-FPN Mask R-CNN ran at roughly 5 frames per second on an M40 GPU, with the mask branch adding about 20% to Faster R-CNN's cost, and reached 35.7 mask AP on COCO test-dev versus 29.2 for FCIS, the 2016 COCO challenge winner.[^s3] Fully convolutional single-shot alternatives such as FCIS are faster but, per the same paper, made systematic errors on overlapping objects.[^s3]

## Evaluation

Instance segmentation outputs are allowed to overlap, so one pixel may belong to several predicted segments, and each segment carries a confidence score. That is why the task is scored with average precision (AP) over mask IoU, built from a precision/recall curve over those confidences, much as in box detection.[^s4] MS COCO's mask AP is the standard benchmark; Cityscapes provides instance annotations for 8 of its 19 urban-driving classes.[^s3][^s4]

## Limitations and open questions

Instance segmentation covers only countable "things" (people, cars, animals) and ignores amorphous "stuff" such as sky, grass or road. Kirillov et al. (CVPR 2019) proposed *panoptic segmentation* to unify the two, requiring every pixel to receive exactly one class label and one instance ID, which forbids the overlaps instance methods produce; they noted that region-based methods, which treat each object independently, struggle with that constraint.[^s4]

## In practice

Promptable foundation models have changed how masks are produced. Meta's Segment Anything Model (SAM, ICCV 2023), trained on the SA-1B dataset of about 11 million images and 1.1 billion masks, returns a mask for a point, box or rough mask prompt in about 50 ms after a one-time image encoding.[^s5] SAM outputs masks without class labels, so it is not an instance segmenter on its own; its authors obtain instance masks by feeding it the boxes from an existing object detector.[^s5] This detector-plus-segmenter pattern echoes Mask R-CNN's split between "what and where" and "which pixels".

## Connections

Instance segmentation sits under **computer vision** as one of its core dense-prediction tasks.[^s1] It **contrasts with semantic segmentation**, which labels pixels by class but merges all instances of a class into one region, and it extends **object detection** by replacing each box with a mask.[^s1][^s3] **Mask R-CNN** is its canonical model and is built directly on **Faster R-CNN**, using **convolutional neural network** backbones with a feature pyramid.[^s3] **Panoptic segmentation** generalizes it to stuff classes with non-overlapping outputs.[^s4] It is **evaluated on MS COCO** and **Cityscapes**.[^s3][^s4] The **Segment Anything Model** supplies class-agnostic masks that become instance masks when prompted by a detector.[^s5]

## Sources
[^s1]: Zhang et al., "14.9. Semantic Segmentation and the Dataset", *Dive into Deep Learning*. https://www.d2l.ai/_sources/chapter_computer-vision/semantic-segmentation-and-dataset.rst.txt (accessed 2026-11-19)
[^s2]: Hariharan, Arbeláez, Girshick, Malik, "Simultaneous Detection and Segmentation", ECCV 2014, UC Berkeley project page. https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/shape/sds (accessed 2026-11-19)
[^s3]: He, Gkioxari, Dollár, Girshick, "Mask R-CNN", ICCV 2017. https://openaccess.thecvf.com/content_ICCV_2017/papers/He_Mask_R-CNN_ICCV_2017_paper.pdf (accessed 2026-11-19)
[^s4]: Kirillov, He, Girshick, Rother, Dollár, "Panoptic Segmentation", CVPR 2019. https://openaccess.thecvf.com/content_CVPR_2019/papers/Kirillov_Panoptic_Segmentation_CVPR_2019_paper.pdf (accessed 2026-11-19)
[^s5]: Kirillov et al., "Segment Anything", ICCV 2023. https://openaccess.thecvf.com/content/ICCV2023/papers/Kirillov_Segment_Anything_ICCV_2023_paper.pdf (accessed 2026-11-19)
