---
id: kt:recurrent-neural-network
type: Architecture
title: Recurrent neural network
aliases: [RNN, recurrent net, simple recurrent network, Elman network]
domain: deep-learning
summary: >-
  A neural network for sequential data that carries a hidden state from one time step to the next,
  applying the same weights at every step so that each output can depend on the whole input history.
maturity: established
broader: [kt:artificial-neural-network, kt:deep-learning]
related: [kt:long-short-term-memory, kt:gated-recurrent-unit, kt:vanishing-gradient-problem, kt:sequence-to-sequence-learning, kt:hidden-markov-model]
relations:
  - {predicate: trainedWith, object: kt:backpropagation-through-time}
  - {predicate: basedOn, object: kt:backpropagation}
  - {predicate: usedIn, object: kt:automatic-speech-recognition}
  - {predicate: usedIn, object: kt:neural-machine-translation-by-jointly-learning-to-align-and-translate}
  - {predicate: supersededBy, object: kt:transformer-architecture}
  - {predicate: contrastsWith, object: kt:convolutional-neural-network}
sources:
  - id: s1
    title: "9.4. Recurrent Neural Networks"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola)
    url: https://www.d2l.ai/chapter_recurrent-neural-networks/rnn.html
    type: textbook
    accessed: 2026-11-12
  - id: s2
    title: "9. Recurrent Neural Networks (chapter introduction)"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola)
    url: https://d2l.ai/chapter_recurrent-neural-networks/
    type: textbook
    accessed: 2026-11-12
  - id: s3
    title: "Finding Structure in Time"
    publisher: Cognitive Science 14:179–211 (1990) (J. L. Elman), PDF hosted by Saarland University
    url: https://www.coli.uni-saarland.de/~crocker/Teaching/Connectionist/CogSci90-Elman.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "On the difficulty of training recurrent neural networks"
    publisher: ICML 2013, PMLR 28(3):1310–1318 (Pascanu, Mikolov and Bengio)
    url: https://proceedings.mlr.press/v28/pascanu13.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s5
    title: "Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation"
    publisher: EMNLP 2014, pp. 1724–1734 (Cho et al.)
    url: https://aclanthology.org/D14-1179
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s6
    title: "10.2. Gated Recurrent Units (GRU)"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola)
    url: https://d2l.ai/chapter_recurrent-modern/gru.html
    type: textbook
    accessed: 2026-11-12
created: 2026-11-12
---

# Recurrent neural network

A **recurrent neural network (RNN)** is a neural network designed for sequences — text, speech, time series, video, music — whose inputs or outputs vary in length. Instead of seeing a fixed-size input all at once, it reads one element per time step and maintains a **hidden state** that summarises everything seen so far. Recurrent connections pass that state from each step to the next, so the network's prediction at step *t* can depend on the entire prefix of the sequence rather than on a fixed window.[^s1][^s2]

## Origin

RNNs were first popularised by cognitive scientists as models of how the brain processes time, and only later became a mainstream machine-learning tool.[^s2] A landmark was Jeffrey Elman's 1990 paper *Finding Structure in Time*, which argued that representing time as an extra spatial dimension (a buffer of recent inputs) imposes a fixed pattern length and treats shifted copies of a pattern as different. Elman instead represented time implicitly: his "simple recurrent network" fed a copy of the previous hidden-layer activations back in through *context units* alongside the current input, building on an earlier recurrent design by Jordan (1986).[^s3] Trained only to predict the next element, Elman's networks learned that prediction error spikes at word boundaries in an unsegmented letter stream, and their hidden states clustered words into noun and verb categories and finer subclasses — structure no one had labelled.[^s3]

## How it works

For a minibatch input **X**ₜ at step *t*, a basic RNN computes

**H**ₜ = φ(**X**ₜ **W**ₓₕ + **H**ₜ₋₁ **W**ₕₕ + **b**ₕ),  **O**ₜ = **H**ₜ **W**ₕq + **b**q

where φ is an activation function (often tanh) and the output **O**ₜ may be passed through a softmax for classification.[^s1] The crucial design choice is **parameter sharing**: the same weight matrices are reused at every step, so the parameter count does not grow with sequence length — unlike an *n*-gram model, whose table grows exponentially with *n*.[^s1] In a character-level language model, for example, the input "machin" is paired with the shifted target "achine"; at each position the network is scored with cross-entropy on predicting the next character from the hidden state built up so far.[^s1]

Although the recurrence looks like a cycle, an RNN can be **unrolled** across time into a deep feedforward network whose layers share weights. Gradients are then computed by ordinary backpropagation through this unrolled graph, a procedure called backpropagation through time (BPTT).[^s2]

## Limitations

Because BPTT multiplies through the same recurrent weights many times, gradients over long spans tend either to shrink towards zero (**vanishing**) or grow without bound (**exploding**). Pascanu, Mikolov and Bengio (ICML 2013) analysed both problems from analytical, geometric and dynamical-systems viewpoints; they proposed **gradient-norm clipping** for exploding gradients and a soft regularisation constraint for vanishing ones.[^s4] Clipping is part of the standard from-scratch RNN training loop in *Dive into Deep Learning*.[^s2]

Vanishing gradients are better addressed architecturally. **Gated** RNNs add multiplicative gates that decide what to keep and what to overwrite. The gated recurrent unit (GRU), introduced with Cho et al.'s encoder–decoder in 2014, uses a *reset* gate (how much past state feeds the new candidate) and an *update* gate (how much old state to carry forward); it is a lighter alternative to the LSTM that often performs comparably.[^s6][^s5]

## In practice

RNNs rose to prominence in the 2010s through results in handwriting recognition, machine translation and medical diagnosis.[^s2] Cho et al. showed that one RNN can encode a variable-length source phrase into a fixed-length vector while a second decodes it into a target phrase, improving a statistical machine-translation system — an early form of the encoder–decoder pattern behind sequence-to-sequence models.[^s5] Since then, as the *Dive into Deep Learning* authors put it, RNNs have "ceded considerable market share to Transformer models", though they remain standard sequence models and a key teaching foundation.[^s2]

## Connections

An RNN is a kind of **artificial neural network** and one of the core architectures of **deep learning**.[^s2] It is trained with **backpropagation**, applied to the unrolled graph as **backpropagation through time**, and that training exposes the **vanishing-gradient problem**.[^s2][^s4] **Long short-term memory** and the **gated recurrent unit** are gated RNN variants built to overcome it.[^s6] Encoder–decoder RNNs underpin **sequence-to-sequence learning** and attention-based **neural machine translation**.[^s5] Speech is one of the sequential data types RNNs are built to model, which links them to **automatic speech recognition**.[^s2] Like a **hidden Markov model**, an RNN summarises history in a state, but its state is continuous and learned. Where a **convolutional neural network** shares weights across space, an RNN shares them across time.[^s1] The **Transformer**, which replaces recurrence with attention, has largely superseded RNNs in large-scale language modelling.[^s2]

## Sources
[^s1]: Zhang, Lipton, Li and Smola, "9.4. Recurrent Neural Networks", *Dive into Deep Learning*. https://www.d2l.ai/chapter_recurrent-neural-networks/rnn.html (accessed 2026-11-12)
[^s2]: Zhang, Lipton, Li and Smola, "9. Recurrent Neural Networks", *Dive into Deep Learning*. https://d2l.ai/chapter_recurrent-neural-networks/ (accessed 2026-11-12)
[^s3]: Elman, "Finding Structure in Time", *Cognitive Science* 14:179–211 (1990). https://www.coli.uni-saarland.de/~crocker/Teaching/Connectionist/CogSci90-Elman.pdf (accessed 2026-11-12)
[^s4]: Pascanu, Mikolov and Bengio, "On the difficulty of training recurrent neural networks", ICML 2013, PMLR 28(3):1310–1318. https://proceedings.mlr.press/v28/pascanu13.html (accessed 2026-11-12)
[^s5]: Cho et al., "Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation", EMNLP 2014. https://aclanthology.org/D14-1179 (accessed 2026-11-12)
[^s6]: Zhang, Lipton, Li and Smola, "10.2. Gated Recurrent Units (GRU)", *Dive into Deep Learning*. https://d2l.ai/chapter_recurrent-modern/gru.html (accessed 2026-11-12)
