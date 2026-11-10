---
id: kt:perceptron
type: Algorithm
title: Perceptron
aliases: [Rosenblatt perceptron, perceptron learning rule, perceptron algorithm, Mark I Perceptron]
domain: ai-history
summary: >-
  Frank Rosenblatt's 1958 learning machine and the error-driven rule behind it: a single layer of adjustable
  weights that classifies inputs by the sign of a weighted sum and nudges the weights toward each misclassified
  example, guaranteed to converge when the classes are linearly separable.
maturity: foundational
broader: [kt:artificial-neural-network, kt:supervised-learning]
related: [kt:backpropagation, kt:ai-winter, kt:connectionism, kt:support-vector-machine, kt:marvin-minsky]
relations:
  - {predicate: createdBy, object: kt:frank-rosenblatt}
  - {predicate: introducedIn, object: kt:the-perceptron-a-probabilistic-model-for-information-storage-and-organization-in-the-brain}
  - {predicate: influencedBy, object: kt:a-logical-calculus-of-the-ideas-immanent-in-nervous-activity}
sources:
  - id: s1
    title: "The perceptron: A probabilistic model for information storage and organization in the brain"
    publisher: F. Rosenblatt, Cornell Aeronautical Laboratory; Psychological Review 65(6), 1958
    url: https://homepages.math.uic.edu/~lreyzin/papers/rosenblatt58.pdf
    type: primary
    accessed: 2026-11-10
  - id: s2
    title: "The Perceptron (CS4780/5780 lecture notes)"
    publisher: Cornell University, CS 4780/5780 Machine Learning for Intelligent Systems (Kilian Weinberger)
    url: https://cs.cornell.edu/courses/cs4780/2024sp/lectures/pdfs/lecturenote03.pdf
    type: academic
    accessed: 2026-11-10
  - id: s3
    title: "Large Margin Classification Using the Perceptron Algorithm"
    publisher: Y. Freund and R. E. Schapire, Machine Learning 37(3), 277–296, 1999 (copy hosted by Princeton COS 402)
    url: https://www.cs.princeton.edu/courses/archive/fall08/cos402/readings/voted-perceptron.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s4
    title: "Professor's perceptron paved the way for AI – 60 years too soon"
    publisher: Melanie Lefkowitz, Cornell Chronicle (September 25, 2019)
    url: https://news.cornell.edu/node/313946
    type: news
    accessed: 2026-11-10
  - id: s5
    title: "Perceptrons; an Introduction to Computational Geometry (Informationland exhibit)"
    publisher: Lehigh University Library & Technology Services
    url: https://exhibits.lib.lehigh.edu/exhibits/show/informationland/logic-computers-ai/perceptrons
    type: academic
    accessed: 2026-11-10
created: 2026-11-10
---

# Perceptron

The **perceptron** is the first neural network model that *learned* its connection strengths from experience rather than having them wired in by hand. Frank Rosenblatt, a research psychologist at the Cornell Aeronautical Laboratory, set out the theory in a 1958 *Psychological Review* paper sponsored by the U.S. Office of Naval Research.[^s1] Today the word names both that historical machine and the simple error-driven training rule for a single linear threshold unit, which is still the opening example in many machine learning courses.[^s2]

## Origin

Rosenblatt pictured a three-stage system. A "retina" of all-or-nothing sensory units fed randomly connected association units, each of which fired when its net excitatory and inhibitory input crossed a threshold; association units in turn fed mutually exclusive response units.[^s1] Learning lived in the association units' values: reinforcement raised the value of units that were active, so a rewarded stimulus became more likely to evoke the same response again. He argued that memory is therefore stored as connection strengths distributed across the network, not as copies of past stimuli, and that damage degrades it gradually.[^s1] He also flagged limits. Generalization only beat chance when stimulus classes were genuinely distinct, and his paper warns that statistical separability alone cannot support higher-order abstraction such as relational judgements.[^s1]

The idea reached the public in July 1958, when the Office of Naval Research demonstrated a perceptron simulated on an IBM 704 that, after 50 trials, learned to tell punch cards marked on the left from those marked on the right.[^s4] Newspaper coverage was breathless, and Rosenblatt went on to lead Cornell's Cognitive Systems Research Program; the Mark I Perceptron is now held by the Smithsonian Institution.[^s4]

## How the learning rule works

In its modern textbook form, the perceptron solves binary classification with labels y ∈ {−1, +1}. It predicts h(x) = sign(wᵀx + b); appending a constant 1 to every input folds the bias b into the weight vector w, so the rule becomes h(x) = sign(wᵀx).[^s2] A point is correctly classified exactly when y·wᵀx > 0. Training starts from w = 0 and loops over the data; whenever a point is misclassified, it updates w ← w + y·x, and it stops when a full pass makes no mistakes.[^s2]

The **perceptron convergence theorem** explains why this works. If every input has norm at most 1 and some unit-length separator w* classifies all points with margin γ, the algorithm makes at most 1/γ² mistakes. Each update raises wᵀw* by at least γ while increasing wᵀw by at most 1, and combining the two inequalities bounds the number of updates.[^s2] Freund and Schapire credit this finite-mistake result to Block and to Novikoff, both in 1962, and stress that the bound depends on the margin rather than on the input dimension.[^s3]

## Limitations and the 1969 critique

The flip side of the theorem is that a single perceptron can only draw one hyperplane. If the data are not linearly separable, the update loop never terminates.[^s2] The XOR function, where the positive examples sit on opposite corners of a square, is the standard example of such a dataset.[^s2] Marvin Minsky, who had debated Rosenblatt publicly, and Seymour Papert formalized these limits in *Perceptrons: An Introduction to Computational Geometry* (MIT Press, 1969), which analysed what single-layer perceptrons can and cannot compute, including XOR-type Boolean problems.[^s5] The book is widely credited with making neural networks an unfashionable research area for years, and Cornell's own account links the loss of enthusiasm and government funding to the onset of an "AI winter".[^s4][^s5] Rosenblatt died in a sailing accident in 1971, before multilayer training methods revived his approach.[^s4]

## Afterlife in practice

The perceptron never disappeared from machine learning theory. In 1999 Freund and Schapire's **voted perceptron** stored every weight vector produced during training, weighted each by how many examples it survived, and predicted by weighted vote.[^s3] Because the algorithm touches inputs only through inner products, they could swap in polynomial kernels. On NIST handwritten digits it came close to, though not quite level with, Cortes and Vapnik's maximal-margin classifier (about 1.6% versus 1.1% error in their table), while being much simpler and cheaper to train.[^s3] In teaching, it remains the standard first example of a linear classifier and of a mistake-bound proof, and introductory courses still use its XOR failure to motivate models with hidden layers.[^s2]

## Connections

The perceptron is a learning algorithm within **supervised learning** and the first trainable **artificial neural network**; it was **influenced by** McCulloch and Pitts's 1943 threshold-neuron model, which it extended with adjustable weights.[^s1] It was **created by** Frank Rosenblatt and **introduced in** his 1958 paper.[^s1] Its single-layer limits were the target of **Marvin Minsky** and Papert's critique, a strand of the history of the **AI winter**,[^s4][^s5] and they were overcome by **backpropagation**, which trains hidden layers. Its margin-based convergence analysis and kernelized variants tie it to the **support vector machine**,[^s3] and it sits at the root of **connectionism**, the view that intelligence can emerge from networks of simple units.[^s1]

## Sources
[^s1]: F. Rosenblatt, "The perceptron: A probabilistic model for information storage and organization in the brain", Psychological Review 65(6), 1958. https://homepages.math.uic.edu/~lreyzin/papers/rosenblatt58.pdf (accessed 2026-11-10)
[^s2]: Cornell CS 4780/5780, "The Perceptron" lecture notes. https://cs.cornell.edu/courses/cs4780/2024sp/lectures/pdfs/lecturenote03.pdf (accessed 2026-11-10)
[^s3]: Y. Freund and R. E. Schapire, "Large Margin Classification Using the Perceptron Algorithm", Machine Learning 37(3), 277–296, 1999. https://www.cs.princeton.edu/courses/archive/fall08/cos402/readings/voted-perceptron.pdf (accessed 2026-11-10)
[^s4]: M. Lefkowitz, "Professor's perceptron paved the way for AI – 60 years too soon", Cornell Chronicle, 2019-09-25. https://news.cornell.edu/node/313946 (accessed 2026-11-10)
[^s5]: Lehigh University Library & Technology Services, "Perceptrons; an Introduction to Computational Geometry", Informationland exhibit. https://exhibits.lib.lehigh.edu/exhibits/show/informationland/logic-computers-ai/perceptrons (accessed 2026-11-10)
