---
id: kt:a-logical-calculus-of-the-ideas-immanent-in-nervous-activity
type: Work
title: A Logical Calculus of the Ideas Immanent in Nervous Activity
aliases: [McCulloch and Pitts 1943, McCulloch–Pitts paper]
domain: ai-history
summary: >-
  The 1943 paper by Warren McCulloch and Walter Pitts that modelled neurons as all-or-none threshold units,
  showed that networks of such units realize logical propositions, and so supplied the first formal model of a
  neural network and an early model of finite automata.
maturity: historical
broader: [kt:connectionism]
related: [kt:artificial-neural-network, kt:perceptron, kt:finite-automaton]
relations:
  - {predicate: createdBy, object: kt:warren-mcculloch}
  - {predicate: createdBy, object: kt:walter-pitts}
  - {predicate: influencedBy, object: kt:turing-machine}
  - {predicate: followedBy, object: kt:perceptron}
sources:
  - id: s1
    title: "A Logical Calculus of the Ideas Immanent in Nervous Activity"
    publisher: Bulletin of Mathematical Biophysics 5, 115–133 (1943), DOI 10.1007/BF02478259; ML Anthology record
    url: https://mlanthology.org/misc/1943/mcculloch1943misc-logical
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s2
    title: "A Logical Calculus of the Ideas Immanent in Nervous Activity (full text)"
    publisher: McCulloch and Pitts, 1943; copy hosted for a University of Illinois ECE course
    url: https://jontallen.ece.illinois.edu/uploads/498-NS.S21/McCulloch-Pitts-1943-neural-networks-ocr.pdf
    type: primary
    accessed: 2026-10-31
  - id: s3
    title: "Walter Pitts"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/biography/Walter-Pitts
    type: encyclopedia
    accessed: 2026-10-31
  - id: s4
    title: "CS7015 Deep Learning, Lecture 2: McCulloch Pitts Neuron, Thresholding Logic, Perceptrons"
    publisher: IIT Madras (Mitesh M. Khapra), course handout
    url: https://www.cse.iitm.ac.in/~miteshk/CS7015/Slides/Handout/Lecture2.pdf
    type: academic
    accessed: 2026-10-31
  - id: s5
    title: "Representation of Events in Nerve Nets and Finite Automata"
    publisher: S. C. Kleene, RAND Research Memorandum RM-704, 1951
    url: https://www.rand.org/pubs/research_memoranda/RM704.html
    type: primary
    accessed: 2026-10-31
created: 2026-10-31
---

# A Logical Calculus of the Ideas Immanent in Nervous Activity

*A Logical Calculus of the Ideas Immanent in Nervous Activity* is a paper by the neurophysiologist Warren S. McCulloch and the logician Walter Pitts, published in 1943 in the *Bulletin of Mathematical Biophysics* (volume 5, pages 115–133).[^s1] It treated each neuron as a simple digital switching element and the brain as a kind of computing machine, and it is usually counted as the founding formal model of an artificial neural network.[^s3] The idealized unit it described is still taught today as the McCulloch–Pitts (MP) neuron.[^s4]

## The model

The authors began from five simplifying assumptions about nerve cells. A neuron's activity is all-or-none; a fixed number of synapses must be excited within a short summation period for it to fire, independent of earlier activity or where the synapses sit; synaptic delay is the only delay that matters; an active inhibitory synapse absolutely prevents firing at that moment; and the structure of the net does not change over time.[^s2] Under these assumptions the firing of a neuron behaves like the truth value of a proposition, so the behaviour of a network can be written in logic.[^s2]

In modern course notation an MP neuron takes binary inputs, sums them (g(x) = Σxᵢ) and outputs 1 if the sum reaches a hand-set threshold θ, and 0 otherwise; if any inhibitory input is on, the output is forced to 0.[^s4] Choosing θ and the inhibitory lines appropriately gives AND, OR, NOT and NOR gates. A single unit carves its input space with a line or hyperplane, so it can represent only linearly separable Boolean functions.[^s4]

## Main results

For nets without cycles, the paper proved a two-way correspondence: every such net can be described by a "temporal propositional expression" built from conjunction, disjunction, negation and a one-step time shift, and every such expression can be realized by some net.[^s2] Further theorems showed that alternative physiological assumptions, such as relative rather than absolute inhibition or learning by alterable synapses, can be simulated by the idealized nets up to timing.[^s2]

Nets with cycles ("circles") let activity reverberate, so a net's response can depend on events indefinitely far in the past. The authors argued that a net equipped with a tape, scanners and motor outputs can compute exactly the numbers a Turing machine can, while a net with circles alone computes only some of them, and they presented this as a psychological justification for Turing's definition of computability.[^s2] The paper closed with philosophical claims: knowledge of the world obtained through such a net is incomplete in space and indefinite in time, and the basic relations of psychology are those of two-valued logic.[^s2]

## Influence and limitations

The paper fed directly into automata theory. In a 1951 RAND memorandum, Stephen Kleene opened by asking which kinds of events a McCulloch–Pitts nerve net could respond to by firing a given neuron, then generalized the question to finite automata.[^s5] Britannica notes that McCulloch–Pitts automata accept the same class of languages as finite-state grammars, the regular sets.[^s3]

As a model of learning, however, the MP neuron is static. Its inputs are Boolean, all inputs count equally, the threshold must be set by hand and nothing is learned from data.[^s4] Rosenblatt's perceptron addressed these gaps with real-valued inputs, numerical weights, a threshold rewritten as a learnable bias, and a training rule, though a single perceptron still cannot represent XOR.[^s4] Physiologically, the assumptions of fixed structure and absolute inhibition are idealizations that the authors themselves framed as simplifications.[^s2]

## Connections

The paper is the origin point of **connectionism**, the tradition of modelling cognition with networks of simple units, and the work in which the **artificial neural network** concept was introduced.[^s3] It was **created by** Warren McCulloch and Walter Pitts, who later worked together at MIT's Research Laboratory of Electronics,[^s3] and it was **influenced by** Turing's machine model of computation, which it explicitly compares its nets against.[^s2] It was **followed by** the **perceptron**, which added learnable weights to the threshold unit,[^s4] and it underlies the theory of the **finite automaton** through Kleene's analysis of nerve nets.[^s5]

## Sources
[^s1]: McCulloch and Pitts, "A Logical Calculus of the Ideas Immanent in Nervous Activity", Bulletin of Mathematical Biophysics 5, 115–133, 1943 (ML Anthology record). https://mlanthology.org/misc/1943/mcculloch1943misc-logical (accessed 2026-10-31)
[^s2]: McCulloch and Pitts, full text, 1943 (University of Illinois course copy). https://jontallen.ece.illinois.edu/uploads/498-NS.S21/McCulloch-Pitts-1943-neural-networks-ocr.pdf (accessed 2026-10-31)
[^s3]: "Walter Pitts", Encyclopaedia Britannica. https://www.britannica.com/biography/Walter-Pitts (accessed 2026-10-31)
[^s4]: Khapra, CS7015 Deep Learning, Lecture 2, IIT Madras. https://www.cse.iitm.ac.in/~miteshk/CS7015/Slides/Handout/Lecture2.pdf (accessed 2026-10-31)
[^s5]: Kleene, "Representation of Events in Nerve Nets and Finite Automata", RAND RM-704, 1951. https://www.rand.org/pubs/research_memoranda/RM704.html (accessed 2026-10-31)
