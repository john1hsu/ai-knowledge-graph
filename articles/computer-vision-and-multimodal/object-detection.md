---
id: kt:object-detection
type: Application
title: Object detection
aliases: [visual object detection, object localization and recognition]
domain: computer-vision-and-multimodal
summary: >-
  The computer vision task of finding every instance of a set of object categories in an image and
  reporting, for each one, a class label, a confidence score and a bounding box giving its position;
  it generalizes image classification from "what is in the picture" to "what is where".
maturity: established
broader: [kt:computer-vision]
related: [kt:convolutional-neural-network, kt:faster-r-cnn, kt:yolo, kt:vision-transformer, kt:imagenet-and-alexnet]
relations:
  - {predicate: contrastsWith, object: kt:image-classification}
  - {predicate: hasPart, object: kt:non-maximum-suppression}
  - {predicate: evaluatedOn, object: kt:ms-coco}
  - {predicate: evaluatedOn, object: kt:pascal-voc}
  - {predicate: usedIn, object: kt:autonomous-driving}
sources:
  - id: s1
    title: "14.3. Object Detection and Bounding Boxes"
    publisher: Dive into Deep Learning (d2l.ai)
    url: https://d2l.ai/chapter_computer-vision/bounding-box.html
    type: textbook
    accessed: 2026-11-12
  - id: s2
    title: "14.4. Anchor Boxes"
    publisher: Dive into Deep Learning (d2l.ai)
    url: https://d2l.ai/chapter_computer-vision/anchor.html
    type: textbook
    accessed: 2026-11-12
  - id: s3
    title: "The PASCAL Visual Object Classes (VOC) Challenge"
    publisher: Everingham, Van Gool, Williams, Winn and Zisserman, International Journal of Computer Vision 88 (authors' manuscript)
    url: https://homepages.inf.ed.ac.uk/ckiw/postscript/ijcv_voc09.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation"
    publisher: Girshick, Donahue, Darrell and Malik, CVPR 2014 (CVF Open Access)
    url: https://openaccess.thecvf.com/content_cvpr_2014/html/Girshick_Rich_Feature_Hierarchies_2014_CVPR_paper.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s5
    title: "COCO Detection Evaluation"
    publisher: COCO Consortium (cocodataset.org site source)
    url: https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/detection-eval.htm
    type: primary
    accessed: 2026-11-12
  - id: s6
    title: "End-to-End Object Detection with Transformers"
    publisher: Carion, Massa, Synnaeve, Usunier, Kirillov and Zagoruyko (authors' arXiv version, 2005.12872)
    url: https://arxiv.org/abs/2005.12872
    type: primary
    accessed: 2026-11-12
created: 2026-11-12
---

# Object detection

Object detection is the task of locating and labeling every object of interest in an image. Image classification assumes a single dominant object and predicts only its category; a detector must handle many objects at once and say both what each one is and where it sits.[^s1] Position is usually expressed as an axis-aligned bounding box, written either as the coordinates of its upper-left and lower-right corners or as a center point plus width and height.[^s1] Typical uses include perceiving vehicles, pedestrians and obstacles for self-driving cars, finding targets for robots, and flagging unusual objects in security systems.[^s1]

## How it works

Most detectors score a large set of candidate regions and then regress refined boxes from them. In anchor-based designs, the network places many reference boxes of different scales and aspect ratios around each image location; during training each anchor is matched to a ground-truth box (or marked as background) and learns two targets, a class label and an offset that moves and resizes it toward the true box.[^s2] Overlap between boxes is measured by intersection over union (IoU), the area of their intersection divided by the area of their union, running from 0 for disjoint boxes to 1 for identical ones.[^s2] Because many candidates fire on the same object, inference ends with non-maximum suppression: keep the most confident box, discard others that overlap it beyond an IoU threshold, and repeat.[^s2]

In the region-based approach that opened the deep learning era, a detector first generates bottom-up region proposals and then runs a convolutional network on each one to classify and localize it.[^s4] Later region-based models such as Faster R-CNN, and single-pass models such as YOLO that predict all boxes at once, refined this trade-off between accuracy and speed. A different design treats detection as direct set prediction: DETR feeds a fixed set of learned object queries through a transformer encoder-decoder and trains with a bipartite-matching loss that assigns each object exactly one prediction, which removes hand-built anchors and non-maximum suppression.[^s6]

## Evaluation

Detection is scored by matching predictions to ground truth. The PASCAL VOC challenge, covering 20 object classes, counted a detection as correct when its IoU with an unmatched ground-truth box exceeded 50%, and treated repeat detections of an already-matched object as false positives.[^s3] Per-class performance was summarized as average precision, computed in that paper as interpolated precision averaged over eleven recall levels, and averaged across classes into mean average precision (mAP).[^s3] The COCO benchmark made the metric stricter: its primary score averages AP over ten IoU thresholds from 0.50 to 0.95 and over 80 categories, explicitly rewarding tighter localization, and it also reports AP separately for small, medium and large objects.[^s5] COCO notes that about 41% of its objects are small (under 32×32 pixels in area), which makes small-object detection a persistent weak spot.[^s5]

## History and limitations

Before deep learning, detectors relied on hand-engineered features, and progress on PASCAL VOC had largely plateaued, with the best systems being complex ensembles.[^s4] In 2014 Girshick, Donahue, Darrell and Malik's R-CNN ran a high-capacity convolutional network on bottom-up region proposals and raised mAP on VOC 2012 by more than 30% relative to the prior best, to 53.3%; it also showed that supervised pre-training on a large auxiliary task followed by fine-tuning works well when labeled detection data is scarce.[^s4] That recipe of an ImageNet-pretrained backbone plus a detection head shaped the field for years. DETR, reported in 2020, matched a well-tuned Faster R-CNN baseline on COCO in both accuracy and run time while dropping several hand-designed components.[^s6]

Open issues remain: the 50% VOC threshold was deliberately lenient because box boundaries are subjective for non-convex objects, so a single number hides localization quality;[^s3] small objects, the largest share of COCO's annotations, stay hard;[^s5] and labeled detection data is often scarce, which is why pre-training on a larger auxiliary task matters.[^s4]

## Connections

Object detection is a core task within **computer vision** and **contrasts with** **image classification**, which assigns one label per image instead of boxes for every object.[^s1] Modern detectors grew out of **convolutional neural networks** applied to region proposals,[^s4] and DETR brought transformer encoder-decoders into the pipeline, linking the task to transformer-based vision models such as the **vision transformer**.[^s6] **Faster R-CNN** and **YOLO** are its best-known region-based and single-pass architectures, each with its own node. Pipelines usually include **non-maximum suppression** as a final step.[^s2] Progress is **evaluated on** **PASCAL VOC** and **MS COCO**,[^s3][^s5] and R-CNN's pretrain-then-fine-tune recipe ties it to **ImageNet and AlexNet**.[^s4] A leading application is **autonomous driving**.[^s1]

## Sources
[^s1]: Dive into Deep Learning, "14.3. Object Detection and Bounding Boxes". https://d2l.ai/chapter_computer-vision/bounding-box.html (accessed 2026-11-12)
[^s2]: Dive into Deep Learning, "14.4. Anchor Boxes". https://d2l.ai/chapter_computer-vision/anchor.html (accessed 2026-11-12)
[^s3]: Everingham, Van Gool, Williams, Winn and Zisserman, "The PASCAL Visual Object Classes (VOC) Challenge", International Journal of Computer Vision (authors' manuscript). https://homepages.inf.ed.ac.uk/ckiw/postscript/ijcv_voc09.pdf (accessed 2026-11-12)
[^s4]: Girshick, Donahue, Darrell and Malik, "Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation", CVPR 2014. https://openaccess.thecvf.com/content_cvpr_2014/html/Girshick_Rich_Feature_Hierarchies_2014_CVPR_paper.html (accessed 2026-11-12)
[^s5]: COCO Consortium, "Detection Evaluation". https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/detection-eval.htm (accessed 2026-11-12)
[^s6]: Carion, Massa, Synnaeve, Usunier, Kirillov and Zagoruyko, "End-to-End Object Detection with Transformers", arXiv 2005.12872. https://arxiv.org/abs/2005.12872 (accessed 2026-11-12)
