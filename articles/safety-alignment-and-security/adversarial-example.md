---
id: kt:adversarial-example
type: Concept
title: Adversarial example
aliases: [adversarial examples, adversarial input, adversarial perturbation]
domain: safety-alignment-and-security
summary: >-
  An input that has been deliberately and usually imperceptibly perturbed so that a trained model assigns it a wrong
  output, often with high confidence, while a human would still label it correctly.
maturity: established
broader: [kt:adversarial-machine-learning]
related: [kt:adversarial-training, kt:image-classification, kt:convolutional-neural-network]
relations:
  - {predicate: introducedIn, object: kt:intriguing-properties-of-neural-networks}
  - {predicate: createdBy, object: kt:christian-szegedy}
  - {predicate: contrastsWith, object: kt:data-poisoning}
  - {predicate: contrastsWith, object: kt:generative-adversarial-network}
sources:
  - id: s1
    title: "Intriguing properties of neural networks"
    publisher: arXiv:1312.6199 (Szegedy, Zaremba, Sutskever, Bruna, Erhan, Goodfellow, Fergus), ICLR 2014
    url: https://ar5iv.labs.arxiv.org/html/1312.6199
    type: primary
    accessed: 2026-11-16
  - id: s2
    title: "Explaining and Harnessing Adversarial Examples"
    publisher: arXiv:1412.6572 (Goodfellow, Shlens, Szegedy), ICLR 2015
    url: https://ar5iv.arxiv.org/html/1412.6572
    type: primary
    accessed: 2026-11-16
  - id: s3
    title: "Adversarial examples in the physical world"
    publisher: arXiv:1607.02533 (Kurakin, Goodfellow, Bengio), 2016
    url: https://ar5iv.labs.arxiv.org/html/1607.02533
    type: primary
    accessed: 2026-11-16
  - id: s4
    title: "Towards Evaluating the Robustness of Neural Networks"
    publisher: arXiv:1608.04644 (Carlini, Wagner), 2016–2017
    url: https://arxiv.org/abs/1608.04644v2
    type: primary
    accessed: 2026-11-16
  - id: s5
    title: "Adversarial Examples Are Not Bugs, They Are Features"
    publisher: NeurIPS 2019 proceedings (Ilyas, Santurkar, Tsipras, Engstrom, Tran, Madry)
    url: https://proceedings.neurips.cc/paper/2019/hash/e2c420d928d4bf8ce0ff2ec19b371514-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-16
created: 2026-11-16
---

# Adversarial example

An adversarial example is an input x' = x + r built from a correctly handled input x by adding a small, purposely chosen perturbation r, such that the model's prediction changes even though a person would see no meaningful difference. The term and the phenomenon entered deep learning through Szegedy and colleagues' paper "Intriguing properties of neural networks" (arXiv 2013, ICLR 2014), whose authors were at Google, NYU, the University of Montreal and Facebook.[^s1] It is the central object of study in adversarial machine learning and the standard illustration that high test accuracy does not imply robust behaviour.

## Discovery

Szegedy et al. posed the search as an optimization problem: find the smallest r for which the classifier outputs a chosen target label, while keeping the perturbed image inside the valid pixel range. Because the exact problem is hard, they approximated it with box-constrained L-BFGS.[^s1] On AlexNet the resulting distortions averaged about 0.0065 in their normalized measure, and the perturbed images were visually hard to tell apart from the originals. They found that perturbations crafted against one network often fooled networks with different layer counts or hyperparameters, and even networks trained on a disjoint half of the MNIST training set.[^s1] Their explanation was that deep networks' input-output maps are not smooth: adversarial inputs sit in low-probability "pockets" that random noise almost never hits but targeted optimization finds efficiently.[^s1]

## The linearity explanation

A year later, Goodfellow, Shlens and Szegedy argued the opposite cause: models are vulnerable because they behave too linearly, not too nonlinearly.[^s2] For a linear unit with weights w, a perturbation whose every coordinate is bounded by ε can shift the activation by w·r. Choosing r = ε·sign(w) makes that shift grow roughly in proportion to the input dimension n, so many tiny per-pixel changes add up to a large change in output. The same reasoning yields the fast gradient sign method (FGSM), which sets the perturbation to ε times the sign of the loss gradient with respect to the input and needs only one backward pass.[^s2]

The paper reported that a maxout network on MNIST misclassified 89.4% of such inputs at ε = 0.25, with 97.6% average confidence in the wrong answer.[^s2] The linear view also explains transfer: models trained for the same task learn similar weight directions, so a perturbation aligned with one model tends to align with others. Radial basis function networks, which are far less linear, were much harder to fool confidently but generalized poorly, suggesting a tension between ease of optimization and robustness.[^s2]

## Beyond the digital setting

Kurakin, Goodfellow and Bengio printed adversarial images for an ImageNet Inception v3 classifier and photographed them with a phone camera. In their prefiltered setting, top-1 accuracy on photos of adversarial images was 5.1%, compared with 81.8% on photos of clean ones; one-step perturbations survived the camera better than subtler iterative ones.[^s3] They concluded that systems taking input from cameras and other sensors are exposed too, and that their numbers were a lower bound because the attack did not model the camera.[^s3]

## Evaluation and the arms race

Adversarial examples quickly became a benchmark for proposed defenses, and many defenses fell to stronger attacks. Carlini and Wagner showed that defensive distillation, which had cut the success rate of earlier attacks from 95% to 0.5%, did not meaningfully raise robustness: their optimization-based attacks succeeded on both distilled and undistilled networks with 100% probability.[^s4] The authors offered their attacks as a baseline for testing future defenses, a lesson that shaped later evaluation practice: robustness claims should be checked against adaptive, well-tuned attacks rather than weak ones.[^s4]

## Why they exist: bugs or features?

Ilyas et al. (NeurIPS 2019) reframed the phenomenon. They argued that standard datasets contain "non-robust features": patterns that genuinely predict the label but are brittle and meaningless to humans. Models exploit them because they help accuracy, and adversarial perturbations work by flipping them.[^s5] On this view an adversarial example reflects a mismatch between human notions of similarity and the statistics of the data rather than a training defect, which also explains why perturbations transfer between independently trained models.[^s5]

## Connections

Adversarial examples are the test-time, input-side attack studied within **adversarial machine learning**; they contrast with **data poisoning**, which corrupts training data instead.[^s1][^s4] The idea was **introduced in** *Intriguing properties of neural networks*, with **Christian Szegedy** as first author.[^s1] **Adversarial training**, mixing perturbed inputs into training, is the main defense explored from the first papers onward: Szegedy et al. reported early regularization gains and Goodfellow et al. reduced the maxout network's error on FGSM inputs from 89.4% to 17.9%.[^s1][^s2] The canonical setting is **image classification** with **convolutional neural networks**.[^s1][^s3] Despite the shared word, the **generative adversarial network** uses an adversary as a training partner, not an attacker.

## Sources
[^s1]: Szegedy et al., "Intriguing properties of neural networks", arXiv:1312.6199 (ICLR 2014). https://ar5iv.labs.arxiv.org/html/1312.6199 (accessed 2026-11-16)
[^s2]: Goodfellow, Shlens & Szegedy, "Explaining and Harnessing Adversarial Examples", arXiv:1412.6572 (ICLR 2015). https://ar5iv.arxiv.org/html/1412.6572 (accessed 2026-11-16)
[^s3]: Kurakin, Goodfellow & Bengio, "Adversarial examples in the physical world", arXiv:1607.02533. https://ar5iv.labs.arxiv.org/html/1607.02533 (accessed 2026-11-16)
[^s4]: Carlini & Wagner, "Towards Evaluating the Robustness of Neural Networks", arXiv:1608.04644. https://arxiv.org/abs/1608.04644v2 (accessed 2026-11-16)
[^s5]: Ilyas et al., "Adversarial Examples Are Not Bugs, They Are Features", NeurIPS 2019. https://proceedings.neurips.cc/paper/2019/hash/e2c420d928d4bf8ce0ff2ec19b371514-Abstract.html (accessed 2026-11-16)
