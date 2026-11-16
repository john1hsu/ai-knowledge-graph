---
id: kt:connectionism
type: Paradigm
title: Connectionism
aliases: [connectionist AI, parallel distributed processing, PDP, neuronlike computing, connectionist models of cognition]
domain: ai-history
summary: >-
  The approach in AI and cognitive science that explains intelligent behaviour as the emergent activity of networks of
  simple, neuron-like units joined by weighted connections, with knowledge stored in the connection strengths and
  acquired by learning; it is the intellectual lineage of today's artificial neural networks and deep learning.
maturity: historical
broader: [kt:artificial-intelligence]
related: [kt:artificial-neural-network, kt:perceptron, kt:geoffrey-hinton, kt:ai-winter, kt:representation-learning]
relations:
  - {predicate: contrastsWith, object: kt:symbolic-ai}
  - {predicate: influencedBy, object: kt:a-logical-calculus-of-the-ideas-immanent-in-nervous-activity}
  - {predicate: dependsOn, object: kt:backpropagation}
  - {predicate: followedBy, object: kt:deep-learning}
  - {predicate: studiedIn, object: kt:cognitive-science}
sources:
  - id: s1
    title: "Connectionism"
    publisher: J. Garson, Stanford Encyclopedia of Philosophy (first published 1997-05-18; substantive revision 2019-08-16)
    url: https://plato.stanford.edu/entries/connectionism/
    type: academic
    accessed: 2026-11-16
  - id: s2
    title: "Connectionist models of cognition"
    publisher: M. S. C. Thomas and J. L. McClelland, chapter hosted on J. L. McClelland's Stanford page
    url: https://stanford.edu/%7Ejlmcc/papers/ThomasMcCIPCambEncy.pdf
    type: academic
    accessed: 2026-11-16
  - id: s3
    title: "Artificial intelligence: Connectionism"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/technology/artificial-intelligence/Connectionism
    type: encyclopedia
    accessed: 2026-11-16
  - id: s4
    title: "Learning representations by back-propagating errors"
    publisher: D. E. Rumelhart, G. E. Hinton and R. J. Williams, Nature 323, 533 (October 1986) — NASA ADS abstract record
    url: https://ui.adsabs.harvard.edu/abs/1986Natur.323..533R/abstract
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "Connectionism and Cognitive Architecture: A Critical Analysis"
    publisher: J. A. Fodor and Z. W. Pylyshyn, Cognition 28(1-2), 3-71, 1988 (copy hosted for a UC San Diego course)
    url: https://pages.ucsd.edu/~msereno/_170_2003/fodor-pylyshyn.pdf
    type: primary
    accessed: 2026-11-16
created: 2026-11-16
---

# Connectionism

**Connectionism** is a research programme in artificial intelligence and cognitive science that models thinking with networks of many simple processing units, loosely analogous to neurons, linked by weighted connections that play the role of synapses.[^s1] Processing is the spread of activation across those connections, and what a network "knows" is stored in the pattern of connection strengths rather than in explicit rules; the approach is also called artificial-neural-network or **parallel distributed processing (PDP)** modelling.[^s2] Philosophers and AI researchers have treated it as the main alternative to the classical, symbolic view that the mind works like a digital computer manipulating symbols.[^s1]

## Core principles

A connectionist model is specified by a handful of ingredients: a set of units, their activation states, a pattern of connectivity (a weight matrix), a rule for propagating activation, an activation function, a learning rule, and a representation of the environment the network is exposed to.[^s2] Each unit sums the weighted activity arriving from other units, with negative weights acting as inhibition, and passes the result through a squashing or threshold function.[^s1] Because every unit computes much the same simple function, differences in what networks can do come mainly from their weights, so finding good weights—learning—is the central research problem.[^s1]

Several properties made the approach attractive as a theory of cognition. Representations are **distributed**: a concept is a pattern over many units, not a single symbol.[^s2] Networks **degrade gracefully** when units are damaged or inputs are noisy, instead of failing outright as brittle symbolic programs tend to.[^s1] They satisfy many soft constraints in parallel, handle graded, similarity-based categories, act as content-addressable memories that complete partial patterns, and can show rule-like behaviour—such as regular past-tense formation—without any rule being written down.[^s1][^s2]

## History

The roots go back to 1943, when Warren McCulloch and Walter Pitts described the brain as a network of simple binary threshold neurons that could compute logical functions.[^s3] Donald Hebb proposed in 1949 that learning consists of changes in synaptic strength between co-active cells, and between 1958 and 1962 Frank Rosenblatt's perceptron convergence rule showed how two-layer networks could be trained.[^s2] Britannica also credits Belmont Farley and Wesley Clark of MIT with running a small artificial neural network in 1954 that kept working when up to a tenth of its units were destroyed.[^s3]

Momentum stalled after Marvin Minsky and Seymour Papert showed in 1969 that two-layer networks have sharp limits, at a time when no algorithm was known for training networks with hidden units.[^s2] The revival came in 1986. Rumelhart, Hinton and Williams showed in *Nature* that back-propagating errors lets hidden units learn internal representations of task-relevant features, which earlier procedures such as perceptron learning could not do.[^s4] The same year, the two-volume *Parallel Distributed Processing* by Rumelhart, McClelland and colleagues set out the framework, ushering in what the Stanford Encyclopedia calls connectionism's golden age through the early 1990s.[^s1][^s2] Showcase models included NETtalk, which learned to pronounce English text, Rumelhart and McClelland's past-tense learner, and Elman's simple recurrent network for sequences.[^s1][^s2]

## Critiques

The best-known objection came from Jerry Fodor and Zenon Pylyshyn in 1988. They argued that thought is productive and **systematic**—anyone who can think "John loves Mary" can think "Mary loves John"—and that only representations with combinatorial syntax and compositional semantics explain this.[^s5] They concluded that networks could at best describe how a classical symbol system is *implemented* in neural hardware, not the architecture of cognition itself.[^s5] Replies held that classical models do not guarantee systematicity either, or that suitably trained networks generalize systematically; later tests of recurrent networks found success in some settings and failure on commands of unfamiliar length.[^s1] Other critics questioned the biological plausibility of backpropagation, Pinker and Prince attacked the past-tense model's representations and generalization, and some dismissed connectionist models as statistical function approximators with many free parameters.[^s2]

## Legacy

Deep learning is widely read as connectionism's successor: networks with many hidden layers, especially convolutional networks inspired by studies of visual cortex, have achieved results such as AlphaZero's play in chess, shogi and Go.[^s1] The old debates carried over too—concerns about adversarial examples and the opacity of deep networks echo earlier worries about what, exactly, a trained network has learned.[^s1]

## Connections

Connectionism sits under **artificial intelligence** as one of its two classic paradigms and **contrasts with symbolic AI**, the rule-and-symbol tradition that Fodor and Pylyshyn defended.[^s1][^s5] It was **influenced by** McCulloch and Pitts's 1943 threshold-neuron paper and grew through the **perceptron**, whose limits fed the **AI winter**.[^s2][^s3] Its 1980s revival **depends on backpropagation**, co-developed by **Geoffrey Hinton**, which lets hidden units perform **representation learning**.[^s4] Its computational vehicle is the **artificial neural network**, it is **studied in cognitive science** as a theory of mind, and it was **followed by deep learning**, which scaled the same ideas.[^s1][^s2]

## Sources

[^s1]: J. Garson, "Connectionism", Stanford Encyclopedia of Philosophy (rev. 2019-08-16). https://plato.stanford.edu/entries/connectionism/ (accessed 2026-11-16)
[^s2]: M. S. C. Thomas and J. L. McClelland, "Connectionist models of cognition". https://stanford.edu/%7Ejlmcc/papers/ThomasMcCIPCambEncy.pdf (accessed 2026-11-16)
[^s3]: Encyclopaedia Britannica, "Artificial intelligence: Connectionism". https://www.britannica.com/technology/artificial-intelligence/Connectionism (accessed 2026-11-16)
[^s4]: D. E. Rumelhart, G. E. Hinton and R. J. Williams, "Learning representations by back-propagating errors", Nature 323, 533 (1986). https://ui.adsabs.harvard.edu/abs/1986Natur.323..533R/abstract (accessed 2026-11-16)
[^s5]: J. A. Fodor and Z. W. Pylyshyn, "Connectionism and Cognitive Architecture: A Critical Analysis", Cognition 28 (1988) 3-71. https://pages.ucsd.edu/~msereno/_170_2003/fodor-pylyshyn.pdf (accessed 2026-11-16)
