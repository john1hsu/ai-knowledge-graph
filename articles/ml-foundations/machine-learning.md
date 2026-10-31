---
id: kt:machine-learning
type: Field
title: Machine learning
aliases: [ML, statistical learning from data]
domain: ml-foundations
summary: >-
  The subfield of artificial intelligence that studies computer programs which improve their performance at a task
  through experience, typically by fitting a model to data rather than being explicitly programmed with rules.
maturity: foundational
broader: [kt:artificial-intelligence]
related: [kt:bias-variance-tradeoff, kt:deep-learning]
relations:
  - {predicate: hasPart, object: kt:supervised-learning}
  - {predicate: hasPart, object: kt:unsupervised-learning}
  - {predicate: hasPart, object: kt:reinforcement-learning}
  - {predicate: createdBy, object: kt:arthur-samuel}
sources:
  - id: s1
    title: "Some Studies in Machine Learning Using the Game of Checkers"
    publisher: IBM Journal of Research and Development 3(3), 210–229 (1959) (Arthur L. Samuel), ML Anthology record
    url: https://mlanthology.org/misc/1959/samuel1959misc-some
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s2
    title: "Some Studies in Machine Learning Using the Game of Checkers (full text)"
    publisher: Arthur L. Samuel, IBM Journal, July 1959; copy hosted by MIT CSAIL (Rodney Brooks)
    url: https://people.csail.mit.edu/brooks/idocs/Samuel.pdf
    type: primary
    accessed: 2026-10-31
  - id: s3
    title: "CS229 Lecture Notes"
    publisher: Stanford University CS229 Machine Learning (Andrew Ng and Tengyu Ma)
    url: https://cs229.stanford.edu/main_notes.pdf
    type: academic
    accessed: 2026-10-31
  - id: s4
    title: "Chapter 1: Introduction (lecture notes based on Mitchell, Machine Learning)"
    publisher: CS 5751 Machine Learning, University of Minnesota Duluth (Richard Maclin)
    url: https://www.d.umn.edu/~rmaclin/cs5751/notes/Chapter01-1PerPage.pdf
    type: academic
    accessed: 2026-10-31
  - id: s5
    title: "new Machine Learning book (announcement of Mitchell, Machine Learning, McGraw Hill 1997)"
    publisher: Connectionists mailing list archive, Carnegie Mellon University, 13 April 1997 (Tom Mitchell)
    url: https://mailman.srv.cs.cmu.edu/pipermail/connectionists/1997-April/017688.html
    type: primary
    accessed: 2026-10-31
  - id: s6
    title: "ISO/IEC 23053:2022 Framework for Artificial Intelligence (AI) Systems Using Machine Learning (ML)"
    publisher: Standards Council of Canada standards database record
    url: https://scc-ccn.ca/standardsdb/standards/2049844
    type: standards-body
    accessed: 2026-10-31
created: 2026-10-31
---

# Machine learning

**Machine learning (ML)** is the branch of artificial intelligence concerned with programs that get better at a task through experience instead of being handed every rule in advance. The widely taught formulation, from Tom Mitchell's textbook tradition, says a program learns when its performance on a task *T*, as judged by a measure *P*, improves with experience *E*. For a checkers player, *T* is playing the game, *P* is the share of games won, and *E* is practice games against itself.[^s4] In modern practice the "experience" is usually a dataset, and learning means choosing a function from some family so that it predicts well on new inputs.[^s3]

## Origin

Arthur Samuel's 1959 paper in the *IBM Journal of Research and Development* is a classic early statement of the field, with the phrase "machine learning" in its title. Samuel argued that teaching computers to learn from experience could eventually remove much of the need for detailed hand programming. His checkers program started with little more than the rules, a sense of direction and an incomplete set of evaluation terms whose signs and weights were unknown, and he reported that it learned to play better than its author after roughly 8 to 10 hours of machine time.[^s1] He compared two strategies: *rote learning*, which stored scored board positions and helped most with openings and endgames, and *generalisation learning*, which adjusted the weights of scoring terms and produced a strong middle game. Samuel also cautioned that his experiments were too few to prove the learning was stable.[^s2]

By 1997 the field was mature enough for Mitchell's 414-page McGraw Hill textbook, whose thirteen chapters ran from concept learning and decision trees through neural networks, Bayesian and computational learning theory, instance-based and genetic methods, to analytical and reinforcement learning.[^s5]

## How it works

Designing a learner involves a few recurring choices: what target function to learn, how to represent it (rules, a polynomial over features, a neural network), and what algorithm fits it to experience. In Mitchell's checkers example, a board-evaluation function is written as a weighted sum of features, and the weights are nudged by a least-mean-squares rule in proportion to the error between estimated and target values, an instance of gradient descent.[^s4]

Stanford's CS229 notes frame the core supervised case precisely. Given a training set of *n* pairs (x⁽ⁱ⁾, y⁽ⁱ⁾), the goal is a hypothesis *h* mapping inputs to outputs such that *h(x)* predicts *y* well; when *y* is continuous the problem is *regression*, and when it takes a few discrete values it is *classification*.[^s3] The same notes organise the rest of the field into deep learning, generalisation and regularisation (including the bias-variance tradeoff and double descent), unsupervised learning (clustering, EM, PCA, ICA), generative and foundation models, and reinforcement learning and control.[^s3]

## Limitations and open questions

A learned model is only as good as its fit to unseen data, so the central technical worry is generalisation: models can underfit or overfit, and the classical rules about model size were complicated by over-parameterised networks that generalise despite fitting their training data exactly.[^s3] Representation choice also matters; Mitchell's framing stresses that the ideal target function is often not computable directly and must be approximated.[^s4] Samuel's own caveat about too few experiments foreshadows a lasting concern with reproducibility and evaluation.[^s2]

## In practice

Machine learning now underlies most deployed AI, from classifiers and recommenders to large language models, which the CS229 notes treat as one family of foundation models.[^s3] Because ML components sit inside larger systems, the international standard ISO/IEC 23053:2022, published in June 2022, sets out a framework describing a generic AI system that uses ML, its components and their functions, for organisations of any type or size that build or use such systems.[^s6]

## Connections

Machine learning sits under **artificial intelligence** as its data-driven branch.[^s4] Its main parts are **supervised learning**, **unsupervised learning** and **reinforcement learning**, the divisions used to structure the CS229 notes.[^s3] **Deep learning** is the subset built on multi-layer neural networks, and the **bias-variance tradeoff** is one of its central theoretical tools for reasoning about generalisation.[^s3] **Arthur Samuel** is linked to the field through that early landmark checkers study.[^s1]

## Sources

[^s1]: Arthur L. Samuel, "Some Studies in Machine Learning Using the Game of Checkers", IBM Journal of Research and Development 3(3):210–229, 1959 (doi 10.1147/rd.33.0210). https://mlanthology.org/misc/1959/samuel1959misc-some (accessed 2026-10-31)
[^s2]: Arthur L. Samuel, "Some Studies in Machine Learning Using the Game of Checkers", full text, MIT CSAIL copy. https://people.csail.mit.edu/brooks/idocs/Samuel.pdf (accessed 2026-10-31)
[^s3]: Andrew Ng and Tengyu Ma, CS229 Lecture Notes, Stanford University. https://cs229.stanford.edu/main_notes.pdf (accessed 2026-10-31)
[^s4]: Richard Maclin, CS 5751 Machine Learning, Chapter 1 notes (based on Mitchell, *Machine Learning*), University of Minnesota Duluth. https://www.d.umn.edu/~rmaclin/cs5751/notes/Chapter01-1PerPage.pdf (accessed 2026-10-31)
[^s5]: Tom Mitchell, "new Machine Learning book", Connectionists mailing list, 13 April 1997. https://mailman.srv.cs.cmu.edu/pipermail/connectionists/1997-April/017688.html (accessed 2026-10-31)
[^s6]: Standards Council of Canada, record for ISO/IEC 23053:2022, Framework for AI Systems Using Machine Learning. https://scc-ccn.ca/standardsdb/standards/2049844 (accessed 2026-10-31)
