---
id: kt:deep-learning
type: Field
title: Deep learning
aliases: [DL, deep neural networks, deep structured learning]
domain: deep-learning
summary: >-
  The branch of machine learning that uses neural networks with many stacked processing layers, trained end to end
  (usually by backpropagation and gradient descent), to learn representations of data at successively higher
  levels of abstraction directly from raw inputs.
maturity: established
broader: [kt:machine-learning, kt:representation-learning]
related: [kt:convolutional-neural-network, kt:recurrent-neural-network, kt:large-language-model, kt:deep-belief-network]
relations:
  - {predicate: basedOn, object: kt:artificial-neural-network}
  - {predicate: trainedWith, object: kt:backpropagation}
  - {predicate: trainedWith, object: kt:gradient-descent}
  - {predicate: enables, object: kt:large-language-model}
sources:
  - id: s1
    title: "Deep learning"
    publisher: Nature 521(7553), 436–444 (2015) (LeCun, Bengio and Hinton), RePEc/IDEAS record, doi:10.1038/nature14539
    url: https://ideas.repec.org/a/nat/nature/v521y2015i7553d10.1038_nature14539.html
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s2
    title: "A Fast Learning Algorithm for Deep Belief Nets"
    publisher: Neural Computation 18, 1527–1554 (2006) (Hinton, Osindero and Teh), author's copy, University of Toronto
    url: https://www.cs.utoronto.ca/~hinton/absps/ncfast.pdf
    type: primary
    accessed: 2026-10-31
  - id: s3
    title: "ImageNet Classification with Deep Convolutional Neural Networks"
    publisher: NeurIPS 2012, Advances in Neural Information Processing Systems 25 (Krizhevsky, Sutskever and Hinton)
    url: https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s4
    title: "Representation Learning: A Review and New Perspectives"
    publisher: Bengio, Courville and Vincent, Université de Montréal, authors' arXiv version (arXiv:1206.5538v3, 2014)
    url: https://arxiv.org/pdf/1206.5538
    type: primary
    accessed: 2026-10-31
  - id: s5
    title: "Dive into Deep Learning"
    publisher: Zhang, Lipton, Li and Smola, open textbook (arXiv:2106.11342)
    url: https://arxiv.org/pdf/2106.11342
    type: textbook
    accessed: 2026-10-31
  - id: s6
    title: "Understanding deep learning requires rethinking generalization"
    publisher: ICLR 2017 (Zhang, Bengio, Hardt, Recht and Vinyals), Google Research publication page
    url: https://research.google/pubs/understanding-deep-learning-requires-rethinking-generalization/
    type: peer-reviewed
    accessed: 2026-10-31
created: 2026-10-31
---

# Deep learning

**Deep learning** is the part of machine learning built on computational models with multiple processing layers, each of which transforms the representation produced by the layer below into a slightly more abstract one.[^s1] In the definitional review that LeCun, Bengio and Hinton published in *Nature* in 2015, the defining move is that these layered representations are learned from data rather than designed by hand, with backpropagation used to adjust each layer's internal parameters.[^s1] The open textbook *Dive into Deep Learning* explains the name the same way: the models chain many successive transformations of the data together, top to bottom.[^s5]

## Origin and history

The building blocks are older than the name: neural networks and backpropagation long predate it, yet only a few years before deep learning's breakthroughs, neural networks were widely regarded as outmoded.[^s5] A turning point was Hinton, Osindero and Teh's 2006 paper in *Neural Computation*, which showed that a deep belief network could be trained greedily, one layer at a time, with each added layer improving a bound on the model's log probability; the result was then fine-tuned as a whole.[^s2] Their three-hidden-layer network of about 1.7 million weights reached 1.25% test error on permutation-invariant MNIST, which the authors reported as better than the best backpropagation nets and support vector machines on that task at the time.[^s2]

The decisive public demonstration came in 2012. Krizhevsky, Sutskever and Hinton trained a convolutional network with 60 million parameters (five convolutional layers followed by fully connected layers) on 1.3 million ImageNet images, using an efficient GPU implementation and a new regularisation method to curb overfitting; it reached 39.7% top-1 and 18.9% top-5 test error, well ahead of the previous state of the art.[^s3] By 2015 the *Nature* review could report that deep learning had sharply improved speech recognition, visual object recognition and object detection, and was being applied in drug discovery and genomics.[^s1]

## How it works

A deep network is a composition of parameterised functions. Given an input *x*, layer *l* computes *h*⁽ˡ⁾ = f⁽ˡ⁾(*W*⁽ˡ⁾*h*⁽ˡ⁻¹⁾ + *b*⁽ˡ⁾), and the final layer produces a prediction that is scored by a loss. Backpropagation computes the gradient of that loss with respect to every layer's parameters, and gradient-based optimisation updates them, so all layers are trained jointly toward the task.[^s1] Architecture choices encode assumptions about the data: convolutional networks dominate image, video and audio processing, while recurrent networks were the workhorse for sequential data such as text and speech.[^s1]

Bengio, Courville and Vincent give the main theoretical rationale. Real data arise from many interacting explanatory factors, which favours *distributed* representations that reuse each parameter across many inputs; and useful concepts are defined in terms of simpler ones, which favours *deep*, hierarchical representations.[^s4] Depth lets intermediate features be reused along exponentially many paths, so some function families can be represented far more compactly by deep models than by shallow ones, and higher layers tend to become invariant to small local changes in the input.[^s4]

## Limitations and open questions

Why deep networks generalise remains only partly understood. Zhang and colleagues showed at ICLR 2017 that standard image-classification networks trained with stochastic gradient methods can perfectly fit randomly relabelled training data, and even pure noise, with explicit regularisation making little qualitative difference.[^s6] They argued this undermines conventional explanations of generalisation that rely on model-family capacity or regularisation alone.[^s6] Deep models also tend to need large labelled datasets and substantial compute: the 2012 ImageNet result depended on more than a million labelled images and GPU training.[^s3] Representation-learning researchers have long framed the open problem as finding priors that disentangle the underlying explanatory factors of data.[^s4]

## In practice

The methods spread quickly beyond their first benchmarks: by 2015 they were state of the art in image, video, speech and audio processing and in modelling sequences such as text.[^s1] *Dive into Deep Learning* lists computer vision, natural language processing, speech recognition, reinforcement learning and biomedical informatics among the fields it transformed.[^s5] Practitioners rarely implement layers from scratch; textbooks such as *Dive into Deep Learning* teach the field through mature frameworks, which its authors credit with making the methods broadly usable.[^s5]

## Connections

Deep learning is a subfield of **machine learning** and the dominant form of **representation learning**, since its central claim is that representations should be learned rather than engineered.[^s1][^s4] It is **based on** the **artificial neural network**, and deep networks are **trained with** **backpropagation** and **gradient descent**.[^s1] Its signature architectures include the **convolutional neural network**, whose 2012 ImageNet win marked the field's breakthrough, and the **recurrent neural network** for sequences.[^s1][^s3] The **deep belief network** of 2006 helped revive interest in training deep models.[^s2] Scaling these methods to very large text corpora **enables** the **large language model**.

## Sources

[^s1]: LeCun, Bengio and Hinton, "Deep learning", Nature 521, 436–444 (2015), doi:10.1038/nature14539. https://ideas.repec.org/a/nat/nature/v521y2015i7553d10.1038_nature14539.html (accessed 2026-10-31)
[^s2]: Hinton, Osindero and Teh, "A Fast Learning Algorithm for Deep Belief Nets", Neural Computation 18 (2006). https://www.cs.utoronto.ca/~hinton/absps/ncfast.pdf (accessed 2026-10-31)
[^s3]: Krizhevsky, Sutskever and Hinton, "ImageNet Classification with Deep Convolutional Neural Networks", NeurIPS 2012. https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html (accessed 2026-10-31)
[^s4]: Bengio, Courville and Vincent, "Representation Learning: A Review and New Perspectives", arXiv:1206.5538. https://arxiv.org/pdf/1206.5538 (accessed 2026-10-31)
[^s5]: Zhang, Lipton, Li and Smola, "Dive into Deep Learning", arXiv:2106.11342. https://arxiv.org/pdf/2106.11342 (accessed 2026-10-31)
[^s6]: Zhang, Bengio, Hardt, Recht and Vinyals, "Understanding deep learning requires rethinking generalization", ICLR 2017. https://research.google/pubs/understanding-deep-learning-requires-rethinking-generalization/ (accessed 2026-10-31)
