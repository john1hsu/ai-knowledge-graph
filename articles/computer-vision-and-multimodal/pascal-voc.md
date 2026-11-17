---
id: kt:pascal-voc
type: Benchmark
title: PASCAL VOC
aliases: [PASCAL Visual Object Classes, PASCAL VOC Challenge, Visual Object Classes Challenge, VOC2007, VOC2012]
domain: computer-vision-and-multimodal
summary: >-
  An annotated image dataset and annual competition (2005–2012) for recognising 20 everyday object
  classes, organised by Everingham, Van Gool, Williams, Winn and Zisserman, whose classification,
  detection and segmentation tasks and IoU-based average-precision scoring became the standard
  object-detection benchmark before MS COCO.
maturity: historical
broader: [kt:ai-evaluation, kt:computer-vision]
related: [kt:object-detection, kt:semantic-segmentation, kt:imagenet-and-alexnet, kt:faster-r-cnn, kt:transfer-learning, kt:deformable-part-model]
relations:
  - {predicate: introducedIn, object: kt:the-pascal-visual-object-classes-voc-challenge}
  - {predicate: followedBy, object: kt:ms-coco}
  - {predicate: usedIn, object: kt:r-cnn}
sources:
  - id: s1
    title: "The PASCAL Visual Object Classes (VOC) Challenge"
    publisher: Everingham, Van Gool, Williams, Winn and Zisserman; authors' copy hosted at the University of Edinburgh
    url: https://homepages.inf.ed.ac.uk/ckiw/postscript/ijcv_voc09.pdf
    type: primary
    accessed: 2026-11-17
  - id: s2
    title: "The Pascal Visual Object Classes (VOC) Challenge (publication record)"
    publisher: Microsoft Research; International Journal of Computer Vision vol. 88
    url: https://www.microsoft.com/en-us/research/publication/the-pascal-visual-object-classes-voc-challenge/
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "The Pascal Visual Object Classes Challenge: A Retrospective"
    publisher: Everingham, Eslami, Van Gool, Williams, Winn and Zisserman; authors' copy hosted at the University of Edinburgh
    url: https://homepages.inf.ed.ac.uk/ckiw/postscript/ijcv_voc14.pdf
    type: primary
    accessed: 2026-11-17
  - id: s4
    title: "The Pascal Visual Object Classes Challenge: A Retrospective"
    publisher: International Journal of Computer Vision 111(1), Springer, 2015
    url: https://link.springer.com/doi/10.1007/S11263-014-0733-5
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "Rich feature hierarchies for accurate object detection and semantic segmentation"
    publisher: Girshick, Donahue, Darrell and Malik; arXiv 1311.2524 (extended version of the CVPR 2014 paper)
    url: https://arxiv.org/abs/1311.2524.pdf
    type: primary
    accessed: 2026-11-17
created: 2026-11-17
---

# PASCAL VOC

PASCAL VOC (Visual Object Classes) was a benchmark for recognising categories of objects in natural photographs. It had two parts: a public dataset of annotated images with standard evaluation software, and an annual competition with a workshop at which results were compared.[^s1][^s4] The organisers were Mark Everingham, Luc Van Gool, Christopher Williams, John Winn and Andrew Zisserman. Their journal description of the challenge appeared online in 2009 and in the *International Journal of Computer Vision* (vol. 88) in 2010, and it called VOC the accepted benchmark for object detection.[^s2] A second paper looking back over the 2008–2012 editions was published in the same journal in 2015, after Everingham's death in 2012.[^s3][^s4]

## History and dataset

The competition started in 2005 with four classes: car, motorbike, bicycle and person. It grew to 10 classes in 2006 and to 20 in 2007. The final 20 classes cover vehicles (aeroplane, bicycle, boat, bus, car, motorbike, train), animals (bird, cat, cow, dog, horse, sheep), household objects (bottle, chair, dining table, potted plant, sofa, tv/monitor) and people.[^s1] To build VOC2007, the team downloaded about 500,000 Flickr images using class-related keywords. The images were then annotated at a supervised "annotation party" following written guidelines. Each object received an axis-aligned bounding box, an optional viewpoint and a truncation flag, and could be marked *difficult*. Difficult objects are left out of scoring, and detecting them is not penalised. The 2007 release had 9,963 images containing 24,640 annotated objects.[^s1] By VOC2012 the main trainval set had grown to 11,540 images and 31,561 objects, and the segmentation trainval set to 2,913 images.[^s3]

## Tasks and evaluation

The three main tasks were image classification (is at least one instance of a class present?), detection (draw a box around every instance), and pixel-level segmentation. Two smaller "taster" tasks were added: person layout (locating the head, hands and feet) and, from 2010, action classification.[^s1][^s3] Detection set the template that later benchmarks reused. A predicted box counts as correct only if its intersection-over-union (IoU) with a ground-truth box exceeds 50%. Each extra detection of the same object counts as a false positive. Results are ranked by average precision (AP) per class and by its mean across classes (mAP).[^s1] Until 2009, AP was the mean of interpolated precision at 11 evenly spaced recall levels. From 2010 the organisers used every point on the precision–recall curve, because the coarse interpolation had blurred the differences between low-scoring methods.[^s1][^s3] Test annotations were kept secret behind an evaluation server. The organisers adopted this after the 2005 edition: labels for that year's test images were released, and the reported results proved optimistic.[^s1][^s3]

## Lessons and critiques

The organisers analysed their own benchmark candidly. Many classifiers seemed to rely on scene context rather than on the object itself. For example, birds perched on branches were mistaken for bicycles. Searching Flickr by recency introduced a seasonal bias. Methods scored 5–13% lower on VOC2006 test data than on VOC2007 data, which suggested dataset-specific overfitting.[^s1] The retrospective added bootstrapped significance tests, AP normalised across classes, and a "super-method" that combined entries; the combination improved average AP by about 3.6 points over the best single method. It also found that Mechanical Turk could provide image-level labels reliably but not bounding boxes of adequate quality.[^s3] Participation in the final 2012 segmentation competition dropped to three organisations, which the authors read as a sign that established methods were hard for newcomers to beat.[^s3]

## Legacy

VOC tracked the change in computer vision from hand-built features to deep learning. In 2013, R-CNN combined region proposals with a convolutional network that was pre-trained on ImageNet and fine-tuned on VOC. Its authors reported 53.3% mAP on VOC 2012, a relative gain of more than 30% over the previous best result.[^s5] The retrospective credits VOC with feeding the growth of category-recognition research and with leading to larger challenges such as ImageNet. The organisers planned to keep the 2008–2012 test annotations private and the evaluation server open.[^s3]

## Connections

VOC is an early, defining instance of **AI evaluation** within **computer vision**. Its tasks correspond directly to **object detection** and **semantic segmentation**, and both of those articles cite it as an evaluation benchmark.[^s1] The challenge was introduced in the IJCV paper **"The PASCAL Visual Object Classes (VOC) Challenge"**.[^s2] The retrospective singles out the open-source deformable part model detector among VOC-era methods, and the benchmark later measured the jump made by **R-CNN**, whose line led to **Faster R-CNN**.[^s3][^s5] The pre-train-on-ImageNet, fine-tune-on-VOC recipe is a canonical case of **transfer learning** and links VOC to **ImageNet and AlexNet**.[^s3][^s5] Its IoU-matched AP metric was carried forward and extended by the larger **MS COCO** benchmark that followed it.

## Sources
[^s1]: Everingham et al., "The PASCAL Visual Object Classes (VOC) Challenge", authors' copy. https://homepages.inf.ed.ac.uk/ckiw/postscript/ijcv_voc09.pdf (accessed 2026-11-17)
[^s2]: Microsoft Research publication record, "The Pascal Visual Object Classes (VOC) Challenge", IJCV 88 (2010). https://www.microsoft.com/en-us/research/publication/the-pascal-visual-object-classes-voc-challenge/ (accessed 2026-11-17)
[^s3]: Everingham et al., "The Pascal Visual Object Classes Challenge: A Retrospective", authors' copy. https://homepages.inf.ed.ac.uk/ckiw/postscript/ijcv_voc14.pdf (accessed 2026-11-17)
[^s4]: Everingham et al., "The Pascal Visual Object Classes Challenge: A Retrospective", IJCV 111(1), 2015. https://link.springer.com/doi/10.1007/S11263-014-0733-5 (accessed 2026-11-17)
[^s5]: Girshick, Donahue, Darrell and Malik, "Rich feature hierarchies for accurate object detection and semantic segmentation", arXiv 1311.2524. https://arxiv.org/abs/1311.2524.pdf (accessed 2026-11-17)
