---
id: kt:computer-vision
type: Field
title: Computer vision
aliases: [CV, machine vision, visual recognition]
domain: computer-vision-and-multimodal
summary: >-
  The field of artificial intelligence concerned with getting computers to extract meaningful descriptions of
  the world (objects, regions, shape, motion, illumination) from images and video; it is an inverse problem
  that today is tackled mostly with deep learning trained on large labeled datasets.
maturity: established
broader: [kt:artificial-intelligence, kt:machine-learning]
related: [kt:image-classification, kt:object-detection, kt:vision-transformer, kt:vision-language-model, kt:pattern-recognition]
relations:
  - {predicate: hasPart, object: kt:semantic-segmentation}
  - {predicate: dependsOn, object: kt:convolutional-neural-network}
  - {predicate: influencedBy, object: kt:imagenet-and-alexnet}
  - {predicate: contrastsWith, object: kt:computer-graphics}
sources:
  - id: s1
    title: "computer vision"
    publisher: Encyclopaedia Britannica (The Editors; revised by Erik Gregersen)
    url: https://www.britannica.com:443/technology/computer-vision
    type: encyclopedia
    accessed: 2026-11-14
  - id: s2
    title: "Computer Vision: Algorithms and Applications, 2nd ed. (Chapter 1 excerpt, pp. 1–10)"
    publisher: Richard Szeliski, Springer 2022 (final draft 2021-09-30; course reading hosted by UT Austin)
    url: https://cs.utexas.edu/~pstone/Courses/309fall24/preclass/readings/week6_Szeliski_CVAA_Book_p_1_10.pdf
    type: textbook
    accessed: 2026-11-14
  - id: s3
    title: "The Summer Vision Project (AI Memo AIM-100)"
    publisher: MIT Artificial Intelligence Project, DSpace@MIT (Seymour A. Papert, 1966)
    url: https://dspace.mit.edu/handle/1721.1/6125
    type: primary
    accessed: 2026-11-14
  - id: s4
    title: "Lecture 1, Part 2 (CS231n: Deep Learning for Computer Vision, 2024)"
    publisher: Stanford University CS231n (lecture slides)
    url: https://cs231n.Stanford.edu/slides/2024/lecture_1_part_2.pdf
    type: academic
    accessed: 2026-11-14
  - id: s5
    title: "ImageNet Classification with Deep Convolutional Neural Networks"
    publisher: NeurIPS 2012 (Krizhevsky, Sutskever and Hinton)
    url: https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-14
created: 2026-11-14
---

# Computer vision

**Computer vision** is the branch of artificial intelligence that tries to make computers "see": to take the raw pixels captured by a camera and turn them into descriptions of what is in the scene, such as which objects are present, where they are, and what shape they have. Britannica treats the term as interchangeable with *machine vision* and stresses that modern systems learn visual features and patterns from large collections of images and then apply them to new images.[^s1] In Richard Szeliski's widely used textbook, the goal is framed more broadly as recovering properties of the world, including shape, illumination and colour distributions, from one or more images.[^s2]

## Why vision is hard

Szeliski describes computer vision as the inverse of computer graphics. Graphics and physics supply *forward* models: radiometry, optics and sensor design describe how light reflects, scatters and refracts off surfaces and is projected onto an image plane. Vision has to run that process backwards, inferring the scene from the image.[^s2] Because a 2D image does not contain enough information to pin down a unique 3D answer, vision is an ill-posed inverse problem; practitioners resolve the ambiguity either with physics-based and probabilistic models or by learning from very large sets of examples.[^s2] Szeliski also notes that early AI researchers expected perception to be easier than "higher" abilities such as logic and planning, an expectation that proved badly wrong.[^s2]

## History

That optimism is visible in one of the field's founding documents. In July 1966 Seymour Papert's MIT memo AIM-100, *The Summer Vision Project*, proposed using summer workers to build a significant part of a visual system in a single summer. Its plan ran from figure–ground analysis (separating a scanned picture into likely objects, background and "chaos"), through region and shape description, to naming objects by matching them against a vocabulary of known objects.[^s3] The memo framed the work as a contribution to pattern recognition, and the gap between its one-summer ambition and the decades the problem actually took is the clearest illustration of how badly the difficulty of perception was underestimated.[^s3][^s2]

The modern era is usually dated to 2012. Krizhevsky, Sutskever and Hinton trained a convolutional network with 60 million parameters and five convolutional layers on 1.3 million ImageNet images in 1,000 classes, using GPUs and a new regularisation method; they reported 39.7% top-1 and 18.9% top-5 test error on the 2010 benchmark, well ahead of the previous state of the art.[^s5] Stanford's CS231n course connects this line of work to the 2018 Turing Award given to LeCun, Hinton and Bengio for deep learning, and notes that the original 2009 ImageNet paper received CVPR 2019's Longuet-Higgins Prize for lasting impact.[^s4]

## Core tasks

CS231n (2024) organises the field around a ladder of increasingly detailed outputs:[^s4]

- **Image classification** assigns one label to a whole image, with no spatial extent.[^s4]
- **Semantic segmentation** labels every pixel by class but does not separate individual objects.[^s4]
- **Object detection** finds and localises multiple objects; **instance segmentation** also outlines each one.[^s4]
- **Video classification** and multimodal video understanding extend these tasks over time.[^s4]
- **Visualisation and understanding** studies what trained networks have actually learned.[^s4]

Beyond these tasks, the same course lists self-supervised learning, generative modelling, vision–language models, 3D vision and embodied intelligence as active research directions.[^s4]

## Applications

Szeliski catalogues a wide range of deployed uses: optical character recognition, industrial machine inspection, retail checkout, warehouse logistics, medical imaging, self-driving vehicles, photogrammetry, motion capture, surveillance and biometrics. On the consumer side he lists panorama stitching, exposure bracketing, 3D modelling from snapshots, video stabilisation, face detection and visual authentication.[^s2] Britannica highlights facial recognition and augmented reality as everyday examples.[^s1]

## Limitations and open questions

Because vision is underdetermined, data-driven systems resolve ambiguity using the regularities in their training examples, so their answers are only as good as that data; the deep-learning breakthrough itself depended on a dataset of over a million labelled images and on GPU compute to train on it.[^s2][^s5] Current research is pushing toward less labelling (self-supervision), 3D and embodied understanding, and tighter links with language.[^s4]

## Connections

Computer vision is a subfield of **artificial intelligence** and today a major application area of **machine learning**.[^s1] Its canonical tasks have their own nodes: **image classification**, **object detection** and **semantic segmentation**, the last treated here as a part of the field.[^s4] The deep-learning turn **depends on convolutional neural networks** and was strongly **influenced by ImageNet and AlexNet**,[^s5] while newer architectures such as the **vision transformer** and **vision–language models** carry the field into multimodal AI.[^s4] It is closely tied to **pattern recognition** and is defined in **contrast to computer graphics**, which solves the forward problem that vision inverts.[^s1][^s2]

## Sources

[^s1]: Encyclopaedia Britannica, "computer vision" (The Editors; revised by Erik Gregersen). https://www.britannica.com:443/technology/computer-vision (accessed 2026-11-14)
[^s2]: Richard Szeliski, *Computer Vision: Algorithms and Applications*, 2nd ed., Springer 2022, Chapter 1 excerpt. https://cs.utexas.edu/~pstone/Courses/309fall24/preclass/readings/week6_Szeliski_CVAA_Book_p_1_10.pdf (accessed 2026-11-14)
[^s3]: Seymour A. Papert, "The Summer Vision Project", MIT AI Memo AIM-100, July 1966. https://dspace.mit.edu/handle/1721.1/6125 (accessed 2026-11-14)
[^s4]: Stanford CS231n, "Deep Learning for Computer Vision", Lecture 1 Part 2 slides, 2024. https://cs231n.Stanford.edu/slides/2024/lecture_1_part_2.pdf (accessed 2026-11-14)
[^s5]: Krizhevsky, Sutskever and Hinton, "ImageNet Classification with Deep Convolutional Neural Networks", NeurIPS 2012. https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html (accessed 2026-11-14)
