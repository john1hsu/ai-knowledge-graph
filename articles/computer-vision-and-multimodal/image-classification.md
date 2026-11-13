---
id: kt:image-classification
type: Application
title: Image classification
aliases: [image recognition, visual classification, image categorization]
domain: computer-vision-and-multimodal
summary: >-
  The computer vision task of assigning an entire image one label (or, in the multi-label variant,
  several labels) from a fixed set of categories, usually by training a model such as a convolutional
  network or vision transformer on labeled examples; it is the benchmark task on which much of modern
  deep learning was developed.
maturity: established
broader: [kt:computer-vision, kt:supervised-learning]
related: [kt:convolutional-neural-network, kt:imagenet-and-alexnet, kt:residual-connection, kt:vision-transformer, kt:an-image-is-worth-16x16-words]
relations:
  - {predicate: contrastsWith, object: kt:object-detection}
  - {predicate: evaluatedOn, object: kt:ilsvrc}
  - {predicate: evaluatedOn, object: kt:cifar-10}
  - {predicate: dependsOn, object: kt:softmax-regression}
sources:
  - id: s1
    title: "Lecture 2: Image Classification with Linear Classifiers (CS231n, 2024)"
    publisher: Stanford University CS231n, Deep Learning for Computer Vision (lecture slides)
    url: https://cs231n.Stanford.edu/slides/2024/lecture_2.pdf
    type: academic
    accessed: 2026-11-13
  - id: s2
    title: "4.1. Softmax Regression"
    publisher: Dive into Deep Learning (d2l.ai)
    url: https://d2l.ai/chapter_linear-classification/softmax-regression.html
    type: textbook
    accessed: 2026-11-13
  - id: s3
    title: "ImageNet Large Scale Visual Recognition Challenge"
    publisher: Russakovsky, Deng, Su, Krause, Satheesh, Ma, Huang, Karpathy, Khosla, Bernstein, Berg and Fei-Fei (authors' arXiv version of the IJCV 2015 paper, 1409.0575)
    url: https://arxiv.org/pdf/1409.0575
    type: primary
    accessed: 2026-11-13
  - id: s4
    title: "Deep Residual Learning for Image Recognition"
    publisher: He, Zhang, Ren and Sun, CVPR 2016 (CVF Open Access)
    url: https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s5
    title: "Do ImageNet Classifiers Generalize to ImageNet?"
    publisher: Recht, Roelofs, Schmidt and Shankar, ICML 2019 (PMLR volume 97)
    url: https://proceedings.mlr.press/v97/recht19a
    type: peer-reviewed
    accessed: 2026-11-13
created: 2026-11-13
---

# Image classification

Image classification is the task of taking an input image and assigning it a label from a fixed set of categories, such as {dog, cat, truck, plane}.[^s1] To a computer the image is only a grid of integers from 0 to 255; an 800×600 color photo, for example, is an 800×600×3 array of numbers.[^s1] The difficulty lies in the "semantic gap" between those raw pixel values and a concept like "cat": no hand-written rule reliably bridges it, because the same object's pixels change with viewpoint, lighting, deformation, partial occlusion and background clutter, and members of one class can look very different from each other.[^s1] In the standard single-label setting each image gets exactly one category; multi-label classification instead allows several labels to be true at once.[^s2]

## How it works

Because rules cannot be written by hand, image classification is approached in a data-driven way: collect a dataset of labeled images, train a classifier with a machine learning algorithm, then evaluate it on images it has not seen.[^s1] The simplest baseline, nearest neighbor, memorizes the training set and copies the label of the closest training image under an L1 or L2 pixel distance; its k-nearest-neighbor variant takes a majority vote over the k closest images, with k chosen on a validation set and the test set touched only once at the end.[^s1] Pixel distances carry little semantic meaning, so this approach is rarely used in practice.[^s1]

Parametric models replace memorization with a learned scoring function. A linear classifier computes class scores as f(x, W) = Wx + b: for a 32×32×3 CIFAR-10 image flattened to 3,072 numbers, W is a 10×3,072 matrix that yields one score per class.[^s1] Labels are encoded as one-hot vectors, the softmax function turns scores o into probabilities ŷᵢ = exp(oᵢ) / Σⱼ exp(oⱼ), and training minimizes cross-entropy loss, the negative log of the probability given to the true class.[^s2] Deep classifiers keep this softmax-and-cross-entropy output layer but replace the linear map with many learned layers, convolutional or transformer-based, that extract features from pixels.[^s2][^s4]

## Benchmarks and history

Small benchmarks such as CIFAR-10, with 10 classes, 50,000 training images and 10,000 test images at 32×32 pixels, are used for teaching and quick experiments.[^s1] The field's defining benchmark was the ImageNet Large Scale Visual Recognition Challenge (ILSVRC), run from 2010 to 2014 in the form described by its organizers: 1,000 categories and about 1.28 million training images from 2012 on, scored by top-5 error, where a prediction counts as correct if any of five guessed labels matches the single ground-truth label.[^s3] Five guesses were allowed because images often contain several objects while only one is labeled.[^s3] Winning top-5 error fell from 28.2% in 2010 to 16.4% in 2012, when the deep convolutional network SuperVision (AlexNet) won, and to 6.7% for GoogLeNet in 2014.[^s3] In 2015, residual networks up to 152 layers deep, trained using shortcut connections, reached 3.57% top-5 error as an ensemble and won the ILSVRC classification task.[^s4]

## Limitations and critiques

Leaderboard numbers overstate how well classifiers understand images. The ILSVRC organizers compared GoogLeNet with a trained human annotator on 1,500 test images: the human reached 5.1% top-5 error against the network's 6.8%, and the two failed differently, with the network struggling on small or thin objects, color or contrast filters and abstract depictions such as paintings and sketches, and the human struggling mostly on fine-grained classes like dog breeds.[^s3] Recht and colleagues rebuilt fresh test sets for CIFAR-10 and ImageNet by following the original collection procedures, and reported in 2019 that accuracy dropped by about 3% to 15% on CIFAR-10 and 11% to 14% on ImageNet.[^s5] They attributed the drop not to test-set reuse but to models' brittleness on slightly harder images, although models that ranked higher on the old test sets still tended to rank higher on the new ones.[^s5] Single-label annotation also makes evaluation ambiguous for scenes with several objects, a problem the top-5 metric only partly addresses.[^s3]

## Connections

Image classification is a core task of **computer vision** and a canonical case of **supervised learning**, since classifiers are trained on labeled examples.[^s1] It **contrasts with** **object detection**, which must also say where each object is rather than labeling the whole image. Progress is **evaluated on** **ILSVRC** and **CIFAR-10**,[^s3][^s1] and the output layer **depends on** **softmax regression** with cross-entropy loss.[^s2] The 2012 ILSVRC result links it to **ImageNet and AlexNet** and to **convolutional neural networks**;[^s3] networks built from **residual connections** pushed ImageNet error below 4%;[^s4] and the **vision transformer**, introduced in **An Image Is Worth 16x16 Words**, brought transformers to the same task.

## Sources
[^s1]: Stanford CS231n, "Lecture 2: Image Classification with Linear Classifiers" (2024 slides). https://cs231n.Stanford.edu/slides/2024/lecture_2.pdf (accessed 2026-11-13)
[^s2]: Dive into Deep Learning, "4.1. Softmax Regression". https://d2l.ai/chapter_linear-classification/softmax-regression.html (accessed 2026-11-13)
[^s3]: Russakovsky et al., "ImageNet Large Scale Visual Recognition Challenge", International Journal of Computer Vision 2015, arXiv 1409.0575. https://arxiv.org/pdf/1409.0575 (accessed 2026-11-13)
[^s4]: He, Zhang, Ren and Sun, "Deep Residual Learning for Image Recognition", CVPR 2016. https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html (accessed 2026-11-13)
[^s5]: Recht, Roelofs, Schmidt and Shankar, "Do ImageNet Classifiers Generalize to ImageNet?", ICML 2019. https://proceedings.mlr.press/v97/recht19a (accessed 2026-11-13)
