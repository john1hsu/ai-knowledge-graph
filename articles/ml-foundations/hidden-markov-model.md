---
id: kt:hidden-markov-model
type: Concept
title: Hidden Markov model
aliases: [HMM, hidden Markov models, probabilistic function of a Markov chain]
domain: ml-foundations
summary: >-
  A generative probabilistic model of sequences in which an unobserved Markov chain of discrete states emits the
  observed symbols or feature vectors; its likelihood, most probable state path and parameters are computed with the
  forward, Viterbi and Baum-Welch (forward-backward) algorithms.
maturity: established
broader: [kt:machine-learning, kt:generative-model]
related: [kt:automatic-speech-recognition, kt:markov-decision-process, kt:recurrent-neural-network, kt:finite-automaton]
relations:
  - {predicate: basedOn, object: kt:markov-chain}
  - {predicate: dependsOn, object: kt:expectation-maximization}
  - {predicate: usedIn, object: kt:automatic-speech-recognition}
  - {predicate: alternativeTo, object: kt:conditional-random-field}
sources:
  - id: s1
    title: "Speech and Language Processing (3rd ed. draft), Appendix A: Hidden Markov Models"
    publisher: Daniel Jurafsky and James H. Martin, Stanford University (draft of August 19, 2026)
    url: https://web.stanford.edu/~jurafsky/slp3/A.pdf
    type: textbook
    accessed: 2026-11-09
  - id: s2
    title: "A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition"
    publisher: Lawrence R. Rabiner, Proceedings of the IEEE 77(2), February 1989 (copy hosted on a Texas A&M course page)
    url: https://people.engr.tamu.edu/rgutier/web_courses/cpsc689_s07/rabiner1989tutorialHMM.pdf
    type: primary
    accessed: 2026-11-09
  - id: s3
    title: "What is a hidden Markov model?"
    publisher: Sean R. Eddy, Nature Biotechnology 22(10):1315-1316, 2004 (doi 10.1038/nbt1004-1315)
    url: https://www.nature.com/articles/nbt1004-1315
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "What is a hidden Markov model? (author's preprint)"
    publisher: Sean R. Eddy, preprint of the 2004 Nature Biotechnology primer (copy hosted at Universidad de la República)
    url: https://www.fing.edu.uy/~alopeza/biohpc/papers/hmm/Eddy-What-is-a-HMM-ATG4-preprint.pdf
    type: primary
    accessed: 2026-11-09
  - id: s5
    title: "Conditional Random Fields: Probabilistic Models for Segmenting and Labeling Sequence Data"
    publisher: John Lafferty, Andrew McCallum, Fernando Pereira, 2001 (copy hosted on a CU Boulder course page)
    url: https://home.cs.colorado.edu/~mozer/Teaching/syllabi/6622/papers/LaffertyMcCallumPereira2001.pdf
    type: primary
    accessed: 2026-11-09
created: 2026-11-09
---

# Hidden Markov model

A **hidden Markov model (HMM)** describes a sequence of observations as the output of a process that moves through a set of states the observer cannot see. At each step the hidden state changes according to a Markov chain, and the current state emits an observation, such as a word, a nucleotide or a frame of acoustic features.[^s1] The model became the workhorse of statistical speech recognition from the 1970s until the deep-learning era, and it remains a standard tool for labeling biological sequences.[^s2][^s3]

## Definition

An HMM is specified by four ingredients: a set of N hidden states; a transition matrix A whose entry a_ij is the probability of moving from state i to state j (each row sums to 1); emission probabilities B giving the likelihood of each observation from each state; and an initial distribution π over states. Together these parameters are often written λ = (A, B, π).[^s1] Two simplifying assumptions make the model tractable. The **Markov assumption** says the next state depends only on the current one, and **output independence** says an observation depends only on the state that produced it.[^s1]

Jurafsky and Martin's running example is a toy one: infer whether each summer day was hot or cold from a diary that records only how many ice creams someone ate (one, two or three).[^s1] The weather is the hidden state, and the ice-cream counts are the emissions.

## The three problems and their algorithms

Following Rabiner's 1989 tutorial, HMM practice is usually organized around three questions.[^s1][^s2]

1. **Likelihood:** how probable is an observation sequence O under a model λ? Summing over all N^T state paths is exponential, but the **forward algorithm** uses dynamic programming to compute P(O | λ) in O(N²T) time.[^s1][^s2]
2. **Decoding:** which hidden state sequence best explains O? The **Viterbi algorithm** has the same structure as the forward pass but takes a maximum instead of a sum and keeps back-pointers to recover the best path.[^s1] Posterior decoding with the forward and backward passes instead gives a confidence for each individual label.[^s4]
3. **Learning:** given only observations, what A and B maximize their likelihood? The **Baum-Welch** or forward-backward algorithm, a special case of expectation-maximization, alternates between computing expected state and transition counts and re-estimating the parameters.[^s1] It converges only to a local maximum, so initialization matters in practice.[^s1][^s2]

Real implementations must also handle numerical underflow. Forward and backward probabilities shrink exponentially with sequence length, so Rabiner recommends rescaling at every time step, or working in log space for Viterbi.[^s2]

## History

The underlying mathematics came from Baum and colleagues, beginning with Baum and Petrie in 1966.[^s1] Rabiner notes that it was applied to speech in the 1970s by Baker at Carnegie Mellon and by Jelinek's group at IBM, but came into wide use only in the several years before his tutorial. He attributes the delay to the theory sitting in mathematics journals that speech engineers did not read.[^s2] For speech, he favoured left-to-right (Bakis) topologies, where the state index never decreases, because the signal's properties change over time.[^s2] In computational biology, Eddy calls HMMs the "Legos of computational sequence analysis". They underpin gene finding, profile searches, multiple alignment and regulatory-site detection.[^s4]

## Limitations

The assumptions that make HMMs efficient also limit them. Rabiner names state duration as perhaps their major weakness: self-transitions imply an exponentially distributed stay in each state, which fits most physical signals poorly.[^s2] Because each residue depends only on its state, HMMs also struggle with long-range correlations such as RNA base pairing.[^s4] As generative models, they must model the observations themselves, which makes rich, overlapping input features hard to use. Lafferty, McCallum and Pereira introduced conditional random fields partly to remove this restriction. On Penn Treebank part-of-speech tagging their first-order CRF reached a 5.55% error rate against the HMM's 5.69%.[^s5]

## Connections

- **Broader:** a **generative model** of sequences and a classic tool of **machine learning**, defined by a joint distribution over states and observations.[^s1][^s5]
- **Based on / depends on:** a **Markov chain** over hidden states, with parameters learned by **expectation-maximization** in the form of Baum-Welch.[^s1]
- **Used in:** **automatic speech recognition**, where HMMs modeled the timing of speech for decades.[^s2]
- **Alternative to:** **conditional random fields**, discriminative sequence labelers that drop the HMM's observation-independence assumptions.[^s5]
- **Related:** the **Markov decision process**, which adds actions and rewards to a Markov chain; **recurrent neural networks**, which replaced HMMs in many sequence tasks; and the **finite automaton**, which HMMs extend with probabilities.[^s1]

## Sources

[^s1]: Jurafsky and Martin, *Speech and Language Processing* (3rd ed. draft, August 2026), Appendix A, "Hidden Markov Models". https://web.stanford.edu/~jurafsky/slp3/A.pdf (accessed 2026-11-09)
[^s2]: Rabiner, "A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition", Proceedings of the IEEE 77(2), 1989. https://people.engr.tamu.edu/rgutier/web_courses/cpsc689_s07/rabiner1989tutorialHMM.pdf (accessed 2026-11-09)
[^s3]: Eddy, "What is a hidden Markov model?", Nature Biotechnology 22:1315-1316, 2004. https://www.nature.com/articles/nbt1004-1315 (accessed 2026-11-09)
[^s4]: Eddy, "What is a hidden Markov model?" (author's preprint). https://www.fing.edu.uy/~alopeza/biohpc/papers/hmm/Eddy-What-is-a-HMM-ATG4-preprint.pdf (accessed 2026-11-09)
[^s5]: Lafferty, McCallum and Pereira, "Conditional Random Fields: Probabilistic Models for Segmenting and Labeling Sequence Data", 2001. https://home.cs.colorado.edu/~mozer/Teaching/syllabi/6622/papers/LaffertyMcCallumPereira2001.pdf (accessed 2026-11-09)
