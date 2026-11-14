---
id: kt:ensemble-methods
type: Technique
title: Ensemble methods
aliases: [ensemble learning, model ensembles, classifier ensembles, multiple classifier systems]
domain: ml-foundations
summary: >-
  Techniques that train several models and combine their predictions, by averaging, voting or a learned combiner,
  so that the group is more accurate and robust than any single member; the main families are bagging and random
  forests, boosting, and voting or stacking.
maturity: foundational
broader: [kt:machine-learning, kt:supervised-learning]
related: [kt:bias-variance-tradeoff, kt:decision-tree]
relations:
  - {predicate: hasPart, object: kt:bagging}
  - {predicate: hasPart, object: kt:boosting}
  - {predicate: hasPart, object: kt:random-forest}
  - {predicate: mitigates, object: kt:overfitting}
sources:
  - id: s1
    title: "Bagging Predictors"
    publisher: Machine Learning 24, 123–140 (1996) (Leo Breiman), author's technical-report copy hosted by UW–Madison
    url: https://www.biostat.wisc.edu/~kbroman/teaching/statgen/2004/refs/bagging.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s2
    title: "A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting"
    publisher: Journal of Computer and System Sciences 55(1), 119–139 (1997) (Freund and Schapire), Princeton University research record
    url: https://collaborate.princeton.edu/en/publications/a-decision-theoretic-generalization-of-on-line-learning-and-an-ap/
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "Random Forests"
    publisher: Machine Learning 45, 5–32 (2001) (Leo Breiman), author's copy at UC Berkeley Statistics
    url: https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "An Experimental Comparison of Three Methods for Constructing Ensembles of Decision Trees: Bagging, Boosting, and Randomization"
    publisher: Machine Learning 40, 139–157 (2000) (Thomas G. Dietterich), author's copy hosted by Karl Broman (UW–Madison course materials)
    url: https://kbroman.org/teaching_old/statgen/2004/refs/dietterich.pdf
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "Ensembles: Gradient boosting, random forests, bagging, voting, stacking"
    publisher: scikit-learn User Guide, section 1.11 (stable)
    url: https://scikit-learn.org/stable/modules/ensemble
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# Ensemble methods

**Ensemble methods** build a collection of models and combine their outputs into one prediction, with the aim of generalising better and being more robust than any individual estimator.[^s5] Thomas Dietterich characterised a good ensemble as a set of classifiers that are each reasonably accurate yet diverse, so that their mistakes do not coincide and can be outvoted.[^s4] The idea underlies some of the most widely used tools in applied machine learning, notably random forests and gradient-boosted trees.[^s5]

## Origin

Two papers from the mid-1990s defined the field's main families. Leo Breiman's *Bagging Predictors* (Machine Learning, 1996) introduced **bootstrap aggregating**: train many copies of a predictor on bootstrap resamples of the data and average them for regression or take a plurality vote for classification.[^s1] Yoav Freund and Robert Schapire's 1997 paper in the *Journal of Computer and System Sciences* adapted multiplicative weight updates from on-line learning into a boosting algorithm that, unlike earlier schemes, needed no prior knowledge of how good the weak learner was; this is the algorithm now known as AdaBoost.[^s2] Breiman then combined bagging with random feature selection in *Random Forests* (Machine Learning, 2001).[^s3]

## How it works

Ensembles differ mainly in how they create diversity and how they combine members.

- **Bagging and randomisation.** Each member sees a different random view of the data: a bootstrap sample, a random subset of features, or both (scikit-learn calls the variants pasting, random subspaces and random patches).[^s5] Breiman found that the key ingredient is an *unstable* base learner, one whose output changes a lot with small data changes. Bagging cut classification-tree test error by 6% to 43% across his benchmark datasets and regression-tree mean squared error by 21% to 46%, yet left stable k-nearest-neighbour classifiers essentially unchanged.[^s1]
- **Random forests.** Each tree is grown on a bootstrap sample, and each split is chosen from a small random subset of inputs. Breiman showed that, by the strong law of large numbers, generalisation error converges as trees are added, and bounded it in terms of the strength of individual trees and the correlation between them.[^s3] Roughly a third of examples are left out of each bootstrap sample, giving "out-of-bag" error estimates without a separate test set.[^s3]
- **Boosting.** Members are trained sequentially, each concentrating on the examples its predecessors got wrong. Gradient boosting generalises the idea to any differentiable loss by fitting each new tree to the negative gradient of the loss, with a learning rate shrinking each tree's contribution.[^s5]
- **Voting and stacking.** Conceptually different models (say, logistic regression, a forest and naive Bayes) are combined by hard majority vote or by averaging predicted probabilities (soft voting). Stacking instead trains a final estimator on the base models' out-of-fold predictions.[^s5]

In bias-variance terms, averaging decorrelated high-variance models mainly reduces variance, sometimes at the cost of a slight increase in bias, which is why bagging works best with fully grown trees.[^s5]

## Evidence and limitations

Dietterich's controlled comparison on decision trees found AdaBoost beat bagged C4.5 in 5 domains and lost in none without label noise, but with 20% of labels corrupted it lost in 6 domains and won in none, because boosting concentrated much of its weight on the mislabelled examples.[^s4] Breiman likewise reported that random forests were competitive with AdaBoost in accuracy, faster to train, and far less affected when 5% of training labels were flipped.[^s3]

The costs are practical. Ensembles multiply training and inference compute, and stacking is expensive because base models must be refit inside cross-validation.[^s5] Gains also depend on diversity: Dietterich noted that more accurate members tend to be less diverse, so the two goals pull against each other.[^s4] Combining many models also makes the result harder to interpret than a single tree.

## In practice

As of scikit-learn's current user guide, gradient-boosted trees and random forests are presented as the two best-known ensemble families, and gradient boosting is described as especially strong on tabular data. The histogram-based variant bins features, handles missing values and categorical features natively, and is recommended for datasets with tens of thousands of samples or more.[^s5] Random forests remain a common first baseline because they need little tuning and provide out-of-bag estimates and variable importances.[^s3][^s5]

## Connections

Ensembles are a core technique of **machine learning**, used mostly in **supervised learning**, where averaging or voting over labelled-data predictors is well defined.[^s1][^s5] They are a direct application of the **bias-variance tradeoff**: bagging and random forests attack variance, while boosting and stacking aim to reduce bias.[^s5] **Decision trees** are the classic base learner because they are unstable, which is what makes resampling produce diverse members.[^s1][^s4] The family **has parts** **bagging**, **boosting** and **random forests**,[^s1][^s2][^s3] and it **mitigates overfitting**: Breiman showed that adding trees to a random forest does not drive generalisation error up.[^s3]

## Sources
[^s1]: Breiman, "Bagging Predictors", Machine Learning 24 (1996). https://www.biostat.wisc.edu/~kbroman/teaching/statgen/2004/refs/bagging.pdf (accessed 2026-11-14)
[^s2]: Freund and Schapire, "A Decision-Theoretic Generalization of On-Line Learning and an Application to Boosting", Journal of Computer and System Sciences 55(1) (1997). https://collaborate.princeton.edu/en/publications/a-decision-theoretic-generalization-of-on-line-learning-and-an-ap/ (accessed 2026-11-14)
[^s3]: Breiman, "Random Forests", Machine Learning 45 (2001). https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf (accessed 2026-11-14)
[^s4]: Dietterich, "An Experimental Comparison of Three Methods for Constructing Ensembles of Decision Trees", Machine Learning 40 (2000). https://kbroman.org/teaching_old/statgen/2004/refs/dietterich.pdf (accessed 2026-11-14)
[^s5]: scikit-learn User Guide, "Ensembles: Gradient boosting, random forests, bagging, voting, stacking". https://scikit-learn.org/stable/modules/ensemble (accessed 2026-11-14)
