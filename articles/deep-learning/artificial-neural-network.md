---
id: kt:artificial-neural-network
type: Architecture
title: Artificial neural network
aliases: [ANN, neural network, neural net, connectionist network]
domain: deep-learning
summary: >-
  A computational model built from many simple, interconnected units ("neurons") that each combine weighted
  inputs and apply a nonlinear function, with the connection weights learned from data so that the network as a
  whole computes a useful function of its input.
maturity: foundational
broader: [kt:machine-learning]
related: [kt:deep-learning, kt:convolutional-neural-network, kt:universal-approximation-theorem]
relations:
  - {predicate: introducedIn, object: kt:a-logical-calculus-of-the-ideas-immanent-in-nervous-activity}
  - {predicate: trainedWith, object: kt:backpropagation}
  - {predicate: hasPart, object: kt:activation-function}
  - {predicate: influencedBy, object: kt:perceptron}
sources:
  - id: s1
    title: "A logical calculus of the ideas immanent in nervous activity"
    publisher: The Bulletin of Mathematical Biophysics 5, 115–133 (1943) (McCulloch and Pitts)
    url: https://link.springer.com/doi/10.1007/BF02478259
    type: peer-reviewed
    accessed: 2026-10-30
  - id: s2
    title: "The perceptron: A probabilistic model for information storage and organization in the brain"
    publisher: Psychological Review 65(6), 386–408 (1958) (Rosenblatt), author's paper hosted by UIC
    url: https://homepages.math.uic.edu/~lreyzin/papers/rosenblatt58.pdf
    type: primary
    accessed: 2026-10-30
  - id: s3
    title: "Learning representations by back-propagating errors"
    publisher: Nature 323, 533–536 (1986) (Rumelhart, Hinton and Williams), NASA ADS record
    url: https://ui.adsabs.harvard.edu/abs/1986Natur.323..533R/abstract
    type: peer-reviewed
    accessed: 2026-10-30
  - id: s4
    title: "Dive into Deep Learning: Multilayer Perceptron"
    publisher: Zhang, Lipton, Li and Smola, Dive into Deep Learning (d2l.ai)
    url: https://ja.d2l.ai/chapter_deep-learning-basics/mlp.html
    type: textbook
    accessed: 2026-10-30
  - id: s5
    title: "Multilayer Feedforward Networks with Non-Polynomial Activation Function Can Approximate Any Function"
    publisher: NYU Stern working paper IS-92-13, 1992 (Leshno, Lin, Pinkus and Schocken)
    url: https://archive.nyu.edu/bitstream/2451/14329/1/IS-92-13.pdf
    type: primary
    accessed: 2026-10-30
  - id: s6
    title: "ImageNet Classification with Deep Convolutional Neural Networks"
    publisher: NeurIPS 2012, Advances in Neural Information Processing Systems 25 (Krizhevsky, Sutskever and Hinton)
    url: https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
    type: peer-reviewed
    accessed: 2026-10-30
created: 2026-10-30
---

# Artificial neural network

An **artificial neural network (ANN)** is a model made of many simple processing units connected to one another. Each unit takes a weighted sum of its inputs, adds a bias, and passes the result through a nonlinear *activation function*; units are arranged in layers so that the output of one layer becomes the input of the next. What the network computes is determined by its connection weights, and those weights are not programmed by hand but adjusted from data, typically by gradient-based training.[^s3][^s4] Neural networks are the common substrate of modern deep learning, from image classifiers to large language models.

## Origin

The idea began as a model of the brain. In 1943 Warren McCulloch and Walter Pitts argued that, because neurons fire in an all-or-none fashion, networks of idealised neurons can be described with propositional logic, and they showed how to build a network that realises a given logical expression.[^s1] Their units had fixed connections, however; they computed but did not learn.

Learning entered with Frank Rosenblatt's **perceptron**, described in 1958 from the Cornell Aeronautical Laboratory. Rosenblatt modelled a "retina" of sensory units feeding association units, which in turn fed response units, and stored information as changes in connection strength rather than as stored copies of stimuli. Reinforcing active association units made the same response more likely the next time a similar stimulus appeared.[^s2] He was candid about limits: relational judgements, such as naming the object to the left of a square, proved very hard for the model.[^s2]

The decisive step was a practical way to train networks with **hidden layers**. In 1986 David Rumelhart, Geoffrey Hinton and Ronald Williams showed in *Nature* that back-propagation, which repeatedly adjusts weights to shrink the gap between actual and desired outputs, lets hidden units discover their own internal features. They stressed that this ability to create new features set the method apart from the earlier perceptron-convergence procedure.[^s3]

## How it works

A standard feedforward network, or **multilayer perceptron**, computes a chain of transformations. With one hidden layer, h = σ(W₁x + b₁) and o = W₂h + b₂, where the W are weight matrices, the b are bias vectors and σ is an activation function applied element-wise.[^s4] The nonlinearity is essential. Without it, two stacked linear layers collapse into a single linear map (W = W₂W₁), so adding depth would add nothing.[^s4] Common activations include the sigmoid, which squashes values into (0, 1); tanh, which maps to (−1, 1); and the rectified linear unit, ReLU(x) = max(x, 0), which has largely displaced the sigmoid because its gradient does not vanish for positive inputs.[^s4] For classification, the final layer is usually followed by a softmax that turns scores into probabilities.[^s4]

Training sets the weights by minimising a loss over examples. Back-propagation applies the chain rule to compute how the loss changes with every weight, and an optimiser such as stochastic gradient descent then nudges each weight downhill.[^s3]

## Expressive power and limitations

Why should such a simple structure be so general? **Universal approximation** results answer part of the question. Leshno, Lin, Pinkus and Schocken proved that a feedforward network with a single hidden layer can approximate any continuous function to arbitrary accuracy if and only if its activation function is not a polynomial, a result they argue subsumes most earlier versions of the theorem, including the 1989 work of Hornik, Stinchcombe and White.[^s5] They also showed that the bias (threshold) term is necessary for this to hold.[^s5] Such theorems guarantee existence, not learnability: they do not say how large the network must be or whether gradient training will find the right weights. Textbook treatments add that deeper networks can often represent functions more compactly than very wide shallow ones.[^s4]

Other well-known limitations follow from how networks learn. They need large amounts of labelled data and compute, their learned features are hard to interpret, and saturating activations such as the sigmoid can make gradients vanish in deep stacks, one reason ReLU became the default.[^s4]

## In practice

Neural networks moved from niche to dominant when scale became affordable. In 2012 Alex Krizhevsky, Ilya Sutskever and Hinton trained a convolutional network with 60 million parameters and 500,000 neurons, built from five convolutional layers, two globally connected layers and a final 1000-way softmax, to classify ImageNet images.[^s6] Specialised variants followed for different data: convolutional networks for images, recurrent networks for sequences, and transformers, which now underpin language and multimodal models. All share the same core recipe of layered weighted sums, nonlinear activations and gradient-based training.[^s4][^s6]

## Connections

An artificial neural network is a family of models within **machine learning**, and **deep learning** is the study of networks with many layers.[^s4] The concept was **introduced in** McCulloch and Pitts's 1943 paper *A logical calculus of the ideas immanent in nervous activity*,[^s1] and it was **influenced by** Rosenblatt's **perceptron**, the first learning network.[^s2] Networks are **trained with backpropagation**,[^s3] and each unit **has an activation function** as a part.[^s4] The **universal approximation theorem** describes what they can represent in principle,[^s5] and the **convolutional neural network** is the specialised architecture behind the 2012 ImageNet classifier of Krizhevsky, Sutskever and Hinton.[^s6]

## Sources

[^s1]: McCulloch and Pitts, "A logical calculus of the ideas immanent in nervous activity", The Bulletin of Mathematical Biophysics 5, 115–133, 1943. https://link.springer.com/doi/10.1007/BF02478259 (accessed 2026-10-30)
[^s2]: Rosenblatt, "The perceptron: A probabilistic model for information storage and organization in the brain", Psychological Review 65(6), 386–408, 1958. https://homepages.math.uic.edu/~lreyzin/papers/rosenblatt58.pdf (accessed 2026-10-30)
[^s3]: Rumelhart, Hinton and Williams, "Learning representations by back-propagating errors", Nature 323, 533–536, 1986. https://ui.adsabs.harvard.edu/abs/1986Natur.323..533R/abstract (accessed 2026-10-30)
[^s4]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, "Multilayer Perceptron". https://ja.d2l.ai/chapter_deep-learning-basics/mlp.html (accessed 2026-10-30)
[^s5]: Leshno, Lin, Pinkus and Schocken, "Multilayer Feedforward Networks with Non-Polynomial Activation Function Can Approximate Any Function", NYU Stern working paper IS-92-13, 1992. https://archive.nyu.edu/bitstream/2451/14329/1/IS-92-13.pdf (accessed 2026-10-30)
[^s6]: Krizhevsky, Sutskever and Hinton, "ImageNet Classification with Deep Convolutional Neural Networks", NeurIPS 2012 (NIPS 25). https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html (accessed 2026-10-30)
