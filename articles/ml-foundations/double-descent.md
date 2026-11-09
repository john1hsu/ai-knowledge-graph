---
id: kt:double-descent
type: Concept
title: Double descent
aliases: [double descent curve, deep double descent, double-descent risk curve]
domain: ml-foundations
summary: >-
  The empirical and theoretical finding that test error, as model capacity, training time or sample size grows, can
  first fall, then rise to a peak where the model just barely fits the training data (the interpolation threshold),
  and then fall again in the over-parameterized regime.
maturity: established
broader: [kt:machine-learning]
related: [kt:overfitting, kt:regularization, kt:deep-learning, kt:scaling-laws, kt:ensemble-methods]
relations:
  - {predicate: contrastsWith, object: kt:bias-variance-tradeoff}
  - {predicate: introducedIn, object: kt:reconciling-modern-machine-learning-practice-and-the-bias-variance-trade-off}
  - {predicate: studiedIn, object: kt:statistical-learning-theory}
sources:
  - id: s1
    title: "Reconciling modern machine learning practice and the bias-variance trade-off"
    publisher: arXiv:1812.11118 (Belkin, Hsu, Ma, Mandal), 2018; v2 2019; published in PNAS, doi 10.1073/pnas.1903070116
    url: https://arxiv.org/pdf/1812.11118
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "Deep Double Descent: Where Bigger Models and More Data Hurt"
    publisher: ICLR 2020 (Nakkiran, Kaplun, Bansal, Yang, Barak, Sutskever)
    url: https://mlanthology.org/iclr/2020/nakkiran2020iclr-deep
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s3
    title: "Deep Double Descent: Where Bigger Models and More Data Hurt (authors' version)"
    publisher: arXiv:1912.02292 (Nakkiran, Kaplun, Bansal, Yang, Barak, Sutskever), 2019
    url: https://arxiv.org/pdf/1912.02292
    type: primary
    accessed: 2026-11-09
  - id: s4
    title: "Surprises in High-Dimensional Ridgeless Least Squares Interpolation"
    publisher: arXiv:1903.08560v3 (Hastie, Montanari, Rosset, Tibshirani), 2019
    url: https://arxiv.org/abs/1903.08560v3
    type: primary
    accessed: 2026-11-09
  - id: s5
    title: "A brief prehistory of double descent"
    publisher: arXiv:2004.04328 (Loog, Viering, Mey, Krijthe, Tax), letter accepted by PNAS, 2020
    url: https://arxiv.org/pdf/2004.04328
    type: primary
    accessed: 2026-11-09
  - id: s6
    title: "Optimal Regularization Can Mitigate Double Descent"
    publisher: ICLR 2021 (Nakkiran, Venkat, Kakade, Ma)
    url: https://mlanthology.org/iclr/2021/nakkiran2021iclr-optimal
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# Double descent

**Double descent** names a shape that test-error curves can take when a learner is given more capacity. Classical intuition expects a single U: error falls as the model gains expressiveness, then climbs once it starts fitting noise. Under double descent the climb ends in a spike at the **interpolation threshold**, the capacity at which the model can first fit its training set exactly, and beyond that point error descends a second time, often to a lower level than the best classical model reached.[^s1] The phenomenon offers one explanation for why heavily over-parameterized networks that drive training error to zero still generalize.[^s1][^s2]

## Origin

Mikhail Belkin, Daniel Hsu, Siyuan Ma and Soumik Mandal coined the term in a December 2018 preprint, later published in *PNAS*, proposing one unified risk curve that extends the textbook U-shape past the interpolation point.[^s1] They observed the curve with random Fourier features and random ReLU features, fully connected two-layer networks, random forests and L2-boosted trees, on datasets including MNIST, CIFAR-10, SVHN, TIMIT and 20 Newsgroups.[^s1]

The name was new; the peak was not. A 2020 letter by Loog and colleagues traced similar learning curves back to Vallet et al. (1989), who saw them for pseudo-inverse linear regression on synthetic data, and to Opper et al. (1990), who analysed the same peak theoretically at the point where the sample-to-feature ratio equals one. Work by Raudys, Skurichina and Duin in the late 1990s found it for the pseudo-Fisher linear discriminant, while the linear SVM and the optimal-stability perceptron showed no such peak.[^s5]

## How it works

The threshold depends on the model family. For random-feature regression it sits where the number of features N equals the number of training points n; for fully connected networks Belkin et al. place it near n·K parameters for K outputs.[^s1] Below it, the model cannot interpolate and the usual trade-off applies. Exactly at it, there is essentially one interpolating solution, and it must bend sharply to pass through every noisy label, so its norm and its test error blow up. Above it, infinitely many interpolants exist, and the training procedure picks one with small norm; Belkin et al. argue that this implicit preference acts like Occam's razor, and that SGD started at zero converges to the minimum-norm fit when only the final layer is trained.[^s1]

Hastie, Montanari, Rosset and Tibshirani gave a precise account for "ridgeless" minimum-ℓ2-norm least squares in high dimensions. Their analysis covers both linear feature models and features generated by a random one-layer network, and it reproduces the double-descent risk curve and the possible benefit of over-parameterization exactly, rather than only empirically.[^s4]

Nakkiran et al. (ICLR 2020) showed the effect in modern deep networks and broadened it. They define **effective model complexity** as the largest training-set size on which a given procedure reaches near-zero training error, and conjecture that test error peaks when this quantity roughly equals the number of samples.[^s2][^s3] That framing predicts three versions:[^s3]

- **Model-wise:** test error rises then falls as width grows (ResNet18, five-layer CNNs and Transformers).[^s3]
- **Epoch-wise:** for a large model, error falls, rises near the point where training error reaches zero, then falls again with longer training.[^s3]
- **Sample-wise:** more data moves the peak toward larger models, so adding samples can temporarily hurt. In one case, 4.5 times more data worsened a Transformer on IWSLT'14 German–English translation.[^s3]

## Limitations and open questions

The peak is strongest with label noise. Nakkiran et al. used 10–20% noise in most experiments and argue the deeper cause is model mis-specification, which noise only stands in for.[^s3] Several common practices also shrink or hide it. With optimal early stopping most of their effects vanished, and data augmentation shifted the threshold to larger models.[^s3] Nakkiran, Venkat, Kakade and Ma proved that for certain isotropic linear-regression settings, optimally tuned ℓ2 regularization makes test risk monotone in both sample size and model size, and found empirically that tuned regularization also dampens the peak in neural networks.[^s6] Belkin et al. add that on very large datasets such as ImageNet, models may never leave the classical regime.[^s1] So the curve is best read as a description of unregularized interpolating learners rather than a universal law.

## In practice

The practical lessons are about what to avoid. The critical regime near the threshold is fragile: small changes in data or width can make test performance unexpectedly worse, and ensembling helps most there.[^s3] Moving well past the threshold, or tuning regularization and early stopping, generally avoids the spike.[^s3][^s6] For linear models the theory also gives a clear warning: a feature count close to the sample count is the worst place to be.[^s4][^s5]

## Connections

- **Broader:** a finding about generalization in **machine learning** that applies across model families, from linear regression to deep networks.[^s1][^s6]
- **Contrasts with:** the **bias-variance tradeoff**, whose classical U-shaped curve double descent extends rather than replaces.[^s1]
- **Introduced in:** Belkin et al.'s *Reconciling modern machine learning practice and the bias-variance trade-off*, which named the curve.[^s1]
- **Studied in:** **statistical learning theory**, through exact analyses of minimum-norm interpolation.[^s4]
- **Related:** **overfitting**, since interpolating noisy labels need not ruin test error;[^s1] **regularization**, which can remove the peak;[^s6] **deep learning**, where model-wise and epoch-wise forms were shown;[^s2] **scaling laws**, which also track error as model and data size grow; and **ensemble methods**, which help most in the critical regime.[^s3]

## Sources

[^s1]: Belkin, Hsu, Ma, Mandal, "Reconciling modern machine learning practice and the bias-variance trade-off", arXiv:1812.11118 (PNAS, doi 10.1073/pnas.1903070116). https://arxiv.org/pdf/1812.11118 (accessed 2026-11-09)
[^s2]: Nakkiran, Kaplun, Bansal, Yang, Barak, Sutskever, "Deep Double Descent: Where Bigger Models and More Data Hurt", ICLR 2020. https://mlanthology.org/iclr/2020/nakkiran2020iclr-deep (accessed 2026-11-09)
[^s3]: Nakkiran et al., "Deep Double Descent: Where Bigger Models and More Data Hurt", arXiv:1912.02292. https://arxiv.org/pdf/1912.02292 (accessed 2026-11-09)
[^s4]: Hastie, Montanari, Rosset, Tibshirani, "Surprises in High-Dimensional Ridgeless Least Squares Interpolation", arXiv:1903.08560v3, 2019. https://arxiv.org/abs/1903.08560v3 (accessed 2026-11-09)
[^s5]: Loog, Viering, Mey, Krijthe, Tax, "A brief prehistory of double descent", arXiv:2004.04328, letter to PNAS, 2020. https://arxiv.org/pdf/2004.04328 (accessed 2026-11-09)
[^s6]: Nakkiran, Venkat, Kakade, Ma, "Optimal Regularization Can Mitigate Double Descent", ICLR 2021. https://mlanthology.org/iclr/2021/nakkiran2021iclr-optimal (accessed 2026-11-09)
