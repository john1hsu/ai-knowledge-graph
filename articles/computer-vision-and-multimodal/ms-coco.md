---
id: kt:ms-coco
type: Benchmark
title: MS COCO
aliases: [Microsoft COCO, COCO dataset, Common Objects in Context, Microsoft Common Objects in Context]
domain: computer-vision-and-multimodal
summary: >-
  A large-scale image dataset and benchmark of everyday scenes with per-instance segmentation masks,
  introduced by Lin et al. in 2014, that became the standard yardstick for object detection, instance
  segmentation and image captioning, scored with IoU-averaged average precision.
maturity: established
broader: [kt:ai-evaluation, kt:computer-vision]
related: [kt:object-detection, kt:semantic-segmentation, kt:imagenet-and-alexnet, kt:faster-r-cnn, kt:yolo, kt:bleu]
relations:
  - {predicate: introducedIn, object: kt:microsoft-coco-common-objects-in-context}
  - {predicate: precededBy, object: kt:pascal-voc}
  - {predicate: followedBy, object: kt:lvis}
  - {predicate: usedIn, object: kt:image-captioning}
sources:
  - id: s1
    title: "Microsoft COCO: Common Objects in Context"
    publisher: Lin, Maire, Belongie, Bourdev, Girshick, Hays, Perona, Ramanan, Zitnick and Dollár; arXiv 1405.0312 (full version of the ECCV 2014 paper)
    url: https://arxiv.org/abs/1405.0312v2
    type: primary
    accessed: 2026-11-17
  - id: s2
    title: "Detection Evaluation"
    publisher: COCO Consortium (cocodataset.github.io, official COCO website source)
    url: https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/detection-eval.htm
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "Microsoft COCO Captions: Data Collection and Evaluation Server"
    publisher: Chen, Fang, Lin, Vedantam, Gupta, Dollár and Zitnick; arXiv 1504.00325, 2015
    url: https://arxiv.org/abs/1504.00325
    type: primary
    accessed: 2026-11-17
  - id: s4
    title: "LVIS: A Dataset for Large Vocabulary Instance Segmentation"
    publisher: Gupta, Dollár and Girshick, CVPR 2019 (CVF Open Access)
    url: https://openaccess.thecvf.com/content_CVPR_2019/papers/Gupta_LVIS_A_Dataset_for_Large_Vocabulary_Instance_Segmentation_CVPR_2019_paper.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "COCO Dataset"
    publisher: Ultralytics documentation
    url: https://docs.ultralytics.com/datasets/detect/coco
    type: official-docs
    accessed: 2026-11-17
created: 2026-11-17
---

# MS COCO

MS COCO (Microsoft Common Objects in Context) is an image dataset built to push object recognition toward full scene understanding. A team led by Tsung-Yi Lin, with co-authors including Ross Girshick, Pietro Perona, C. Lawrence Zitnick and Piotr Dollár, released it in 2014 with photographs of everyday scenes in which common objects appear in their natural surroundings, each object instance labelled with a segmentation mask. The original paper reports about 328,000 images, 91 object categories and 2.5 million labelled instances, and an abridged version appeared at ECCV 2014.[^s1] It remains one of the most commonly used benchmarks for comparing computer vision models, especially object detectors.[^s5]

## How it was built

The category list was meant to cover things a four-year-old could name. Candidates were drawn from PASCAL VOC, frequent object words and naming exercises with young children, then filtered for balance across supercategories; categories that could not reach more than 5,000 instances were dropped, and 82 of the 91 exceed that count.[^s1] COCO deliberately labels only countable "things" (people, cars, chairs) and leaves amorphous "stuff" such as sky or grass for future work.[^s1]

A key design choice was to collect non-iconic images. Instead of photos of a single, centred object, the team searched Flickr for pairs of object categories and object-scene combinations, capped how many photos one photographer could contribute, and filtered out iconic shots. As a result COCO averages 7.7 instances per image, against roughly 3.0 for ImageNet and 2.3 for PASCAL VOC, which makes small, occluded and cluttered objects far more common.[^s1]

Annotation ran on Amazon Mechanical Turk in three stages: category labelling (five workers per image, 17,751 worker hours), instance spotting (8,417 worker hours) and per-instance polygon segmentation, which needed over 22 worker hours per 1,000 masks and a qualification task that only about one in three workers passed. The paper puts the total effort at about 60,000 worker hours, and reports that five crowd workers matched the recall of most expert annotators.[^s1]

## Evaluation protocol

COCO's most lasting influence is its scoring. The headline detection metric, written simply as AP, averages precision over ten intersection-over-union (IoU) thresholds from 0.50 to 0.95 in steps of 0.05, so a detector is rewarded for tight localisation rather than merely overlapping boxes. The protocol also reports AP at IoU 0.50 (the older PASCAL VOC criterion) and 0.75, AP by object size (small below 32² pixels, medium up to 96², large above), and average recall given 1, 10 or 100 detections per image; at most 100 detections per image are scored. The official page notes that it uses AP and mAP interchangeably, since AP is already averaged over all 80 evaluated categories.[^s2]

In practice the benchmark uses 80 of the categories. The widely used 2017 split has 118,287 training images and 5,000 validation images, plus 20,288 test-dev images whose labels are withheld, so test results must be submitted to an evaluation server.[^s5] The original paper had already withheld test annotations for the same reason, to limit overfitting to the test set.[^s1]

## Captions and other extensions

In 2015 the team added COCO Captions: five independent human-written captions for each training and validation image, more than 1.5 million captions over 330,000 images once complete, plus a server that scores generated captions with BLEU, METEOR, ROUGE and CIDEr.[^s3] This made COCO a core benchmark for image captioning and, later, a common training and evaluation source for vision-language models.[^s3]

## Limitations and critiques

COCO's 80-category vocabulary is small next to the long tail of objects in real images. The LVIS dataset, built by some of the same researchers on the 164,000 COCO 2017 images, targets over 1,000 categories and argues that rigorous detection evaluation had been confined to a few-category regime.[^s4] LVIS also reports that COCO's masks are relatively coarse: against expert re-annotations COCO masks reached a mean mask IoU of about 0.83–0.87, versus 0.90–0.92 for LVIS, and COCO caps instances per category in crowded images by using "crowd" regions instead of segmenting every object. The person class alone accounts for roughly 30% of COCO instances.[^s4] The original authors also showed that a detector trained on PASCAL lost 12.7 AP when tested on COCO, a sign of how much harder and differently distributed the scenes are.[^s1]

## Connections

COCO is a benchmark within **AI evaluation** and a pillar of **computer vision**. It is the standard evaluation set for **object detection**, including **Faster R-CNN** and **YOLO**, and its masks support segmentation research related to **semantic segmentation**.[^s5] It is **preceded by** PASCAL VOC, which it was designed to succeed with harder scenes, and it complements the iconic images of **ImageNet and AlexNet**.[^s1] COCO Captions scores generated text with metrics such as **BLEU**, linking it to image captioning, and it is **followed by** LVIS, which extends its images to a large vocabulary.[^s3][^s4]

## Sources

[^s1]: Lin et al., "Microsoft COCO: Common Objects in Context", arXiv 1405.0312 (ECCV 2014). https://arxiv.org/abs/1405.0312v2 (accessed 2026-11-17)
[^s2]: COCO Consortium, "Detection Evaluation". https://raw.githubusercontent.com/cocodataset/cocodataset.github.io/master/dataset/detection-eval.htm (accessed 2026-11-17)
[^s3]: Chen et al., "Microsoft COCO Captions: Data Collection and Evaluation Server", arXiv 1504.00325, 2015. https://arxiv.org/abs/1504.00325 (accessed 2026-11-17)
[^s4]: Gupta, Dollár and Girshick, "LVIS: A Dataset for Large Vocabulary Instance Segmentation", CVPR 2019. https://openaccess.thecvf.com/content_CVPR_2019/papers/Gupta_LVIS_A_Dataset_for_Large_Vocabulary_Instance_Segmentation_CVPR_2019_paper.pdf (accessed 2026-11-17)
[^s5]: Ultralytics, "COCO Dataset" documentation. https://docs.ultralytics.com/datasets/detect/coco (accessed 2026-11-17)
