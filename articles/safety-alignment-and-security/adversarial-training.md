---
id: kt:adversarial-training
type: Technique
title: Adversarial training
aliases: [PGD adversarial training, robust training against adversarial examples]
domain: safety-alignment-and-security
summary: >-
  A defense against adversarial examples that trains a model on worst-case perturbed inputs generated on the fly,
  framed as a min-max (saddle-point) robust optimization problem over the model's parameters and a bounded attack.
maturity: established
broader: [kt:adversarial-machine-learning]
related: [kt:regularization, kt:image-classification, kt:cifar-10]
relations:
  - {predicate: mitigates, object: kt:adversarial-example}
  - {predicate: basedOn, object: kt:robust-optimization}
  - {predicate: dependsOn, object: kt:projected-gradient-descent}
  - {predicate: evaluatedOn, object: kt:robustbench}
sources:
  - id: s1
    title: "Towards Deep Learning Models Resistant to Adversarial Attacks"
    publisher: arXiv:1706.06083 (Madry, Makelov, Schmidt, Tsipras, Vladu; MIT), ICLR 2018
    url: https://ar5iv.labs.arxiv.org/html/1706.06083
    type: primary
    accessed: 2026-11-17
  - id: s2
    title: "Theoretically Principled Trade-off between Robustness and Accuracy"
    publisher: Proceedings of ICML 2019, PMLR 97 (Zhang, Yu, Jiao, Xing, El Ghaoui, Jordan)
    url: https://proceedings.mlr.press/v97/zhang19p.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "Robustness May Be at Odds with Accuracy"
    publisher: ICLR 2019 (Tsipras, Santurkar, Engstrom, Turner, Madry)
    url: https://iclr.cc/virtual/2019/poster/1032
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "Fast is better than free: Revisiting adversarial training"
    publisher: ICLR 2020 (Wong, Rice, Kolter)
    url: https://iclr.cc/virtual_2020/poster_BJx040EFvH.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "RobustBench: a standardized adversarial robustness benchmark"
    publisher: arXiv:2010.09670 (Croce, Andriushchenko, Sehwag, Debenedetti, Flammarion, Chiang, Mittal, Hein), NeurIPS 2021 Datasets and Benchmarks Track
    url: https://ar5iv.labs.arxiv.org/html/2010.09670
    type: primary
    accessed: 2026-11-17
created: 2026-11-17
---

# Adversarial training

Adversarial training is the practice of making a classifier robust to adversarial examples by generating such examples during training and fitting the model to them, so the network learns to give the right answer anywhere inside a small region around each input. Mixing perturbed inputs into training was explored from the first adversarial-example papers onward, but the formulation that defines the technique today comes from Aleksander Madry and colleagues at MIT in "Towards Deep Learning Models Resistant to Adversarial Attacks" (arXiv 2017, ICLR 2018), which recast it as robust optimization against a strong iterative attacker.[^s1] Despite many alternatives proposed since, variants of this recipe still top standardized robustness leaderboards.[^s5]

## The min-max formulation

Madry et al. write the training goal as a saddle-point problem: minimize over parameters θ the expected value of the largest loss an adversary can reach, max over δ in S of L(θ, x + δ, y), where S is an allowed perturbation set such as an ℓ∞ ball of radius ε.[^s1] The inner maximization is the attack and the outer minimization is ordinary training on the attacked points. This view gives a precise target: a model with small saddle-point loss is, by definition, robust to every perturbation in S, rather than to one particular attack algorithm.[^s1]

Solving the inner problem exactly is intractable, so the authors approximate it with projected gradient descent (PGD): start from a random point in the ε-ball, take repeated signed-gradient steps that increase the loss, and project back into the ball after each step.[^s1] They ran 10⁵ random restarts of PGD and found that the local maxima it reaches have tightly concentrated loss values, which led them to conjecture (experimentally, not as a proof) that PGD is a "universal" first-order adversary: a model robust to it should resist any attack that uses only gradient information.[^s1]

## Evidence and results

On MNIST at ε = 0.3, the PGD-trained network kept 89.3% accuracy against the strongest white-box attack the authors tried (100-step PGD with 20 restarts), against 98.8% accuracy on clean inputs. On CIFAR-10 at ε = 8 (on the 0–255 pixel scale), clean accuracy was 87.3% and accuracy under 20-step PGD was 45.8%, a result the authors themselves described as still far from satisfactory.[^s1] Training only against the one-step fast gradient sign method overfit to that attack and did not give robustness to PGD at large ε. They also found that robust training needs more model capacity than standard training: small networks trained against PGD could collapse to predicting a single class.[^s1]

## Limitations and the accuracy trade-off

Robustness costs clean accuracy. Tsipras et al. proved that in a simple, natural setting a trade-off between adversarial robustness and standard accuracy is unavoidable, and argued that the cause is that robust classifiers learn different features than standard ones; those features turned out to align better with human perception.[^s3] Zhang et al. decomposed robust error into natural error plus a "boundary" error from points near the decision boundary, derived a differentiable upper bound, and built the TRADES loss to trade the two off explicitly. A TRADES-based entry won the NeurIPS 2018 Adversarial Vision Challenge, placing first among roughly 2,000 submissions.[^s2]

Cost is the other drawback. Every training step requires several extra forward and backward passes to run PGD, so adversarial training was long considered far more expensive than ordinary training.[^s4] Wong, Rice and Kolter showed that single-step FGSM training with random initialization can match PGD training in effectiveness, reaching 45% robust accuracy on CIFAR-10 at ε = 8/255 in 6 minutes and 43% on ImageNet at ε = 2/255 in 12 hours (as reported in 2020), against 10 and 50 hours for the earlier "free" adversarial training method.[^s4] Robustness also stays tied to the chosen threat model: Madry et al. saw MNIST accuracy fall sharply for ε just above the training value, and cautioned that their ℓ2 numbers were probably overestimates.[^s1]

## In practice

Claims of robustness are now checked against standardized, adaptive evaluations. RobustBench scores models with AutoAttack, an ensemble of two PGD variants, a targeted FAB attack and the black-box Square Attack, and at launch listed more than 120 leaderboard evaluations and over 80 models in its Model Zoo.[^s5] Its authors report that the best ℓp entries remained variants of PGD adversarial training, improved with extra training data, early stopping or weight averaging; extra data raised both clean and robust accuracy, but the top models still showed noticeable clean-accuracy drops at ε = 8/255.[^s5]

## Connections

Adversarial training is the main defense studied within **adversarial machine learning** and directly **mitigates** **adversarial examples**.[^s1] It is **based on** **robust optimization**, the saddle-point view of training that Madry et al. applied to deep networks, and **depends on** **projected gradient descent** as its inner attack.[^s1] Its results are typically reported on **CIFAR-10** and ImageNet **image classification** and **evaluated on** **RobustBench**.[^s1][^s5] Because it fits the model to perturbed copies of the data, it acts as a form of **regularization**, one that changes which features the model relies on rather than only shrinking its weights.[^s3]

## Sources
[^s1]: Madry, Makelov, Schmidt, Tsipras & Vladu, "Towards Deep Learning Models Resistant to Adversarial Attacks", arXiv:1706.06083 (ICLR 2018). https://ar5iv.labs.arxiv.org/html/1706.06083 (accessed 2026-11-17)
[^s2]: Zhang et al., "Theoretically Principled Trade-off between Robustness and Accuracy", ICML 2019, PMLR 97:7472–7482. https://proceedings.mlr.press/v97/zhang19p.html (accessed 2026-11-17)
[^s3]: Tsipras, Santurkar, Engstrom, Turner & Madry, "Robustness May Be at Odds with Accuracy", ICLR 2019. https://iclr.cc/virtual/2019/poster/1032 (accessed 2026-11-17)
[^s4]: Wong, Rice & Kolter, "Fast is better than free: Revisiting adversarial training", ICLR 2020. https://iclr.cc/virtual_2020/poster_BJx040EFvH.html (accessed 2026-11-17)
[^s5]: Croce et al., "RobustBench: a standardized adversarial robustness benchmark", arXiv:2010.09670 (NeurIPS 2021 Datasets and Benchmarks). https://ar5iv.labs.arxiv.org/html/2010.09670 (accessed 2026-11-17)
