---
id: kt:conditional-random-field
type: Concept
title: Conditional random field
aliases: [CRF, CRFs, conditional random fields, linear-chain CRF]
domain: ml-foundations
summary: >-
  A discriminative, undirected probabilistic model that defines the conditional probability of a whole label sequence
  (or other structured output) given the observations, using weighted feature functions normalized over all possible
  labelings; the linear-chain form became a standard tool for sequence labeling such as part-of-speech tagging and
  named-entity recognition.
maturity: established
broader: [kt:machine-learning, kt:probabilistic-graphical-model]
related: [kt:supervised-learning, kt:recurrent-neural-network, kt:regularization]
relations:
  - {predicate: introducedIn, object: kt:conditional-random-fields-probabilistic-models-for-segmenting-and-labeling-sequence-data}
  - {predicate: alternativeTo, object: kt:hidden-markov-model}
  - {predicate: alternativeTo, object: kt:maximum-entropy-markov-model}
  - {predicate: extends, object: kt:logistic-regression}
  - {predicate: usedIn, object: kt:named-entity-recognition}
sources:
  - id: s1
    title: "Conditional Random Fields: Probabilistic Models for Segmenting and Labeling Sequence Data"
    publisher: ICML 2001 (Lafferty, McCallum, Pereira); author copy hosted on a University of Colorado course page
    url: https://home.cs.colorado.edu/~mozer/Teaching/syllabi/6622/papers/LaffertyMcCallumPereira2001.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s2
    title: "Conditional Random Fields: Probabilistic Models for Segmenting and Labeling Sequence Data (repository record)"
    publisher: University of Pennsylvania ScholarlyCommons, Departmental Papers (CIS); Proceedings of ICML 2001, pp. 282-289
    url: https://repository.upenn.edu/cis_papers/159
    type: primary
    accessed: 2026-11-10
  - id: s3
    title: "An Introduction to Conditional Random Fields"
    publisher: Charles Sutton and Andrew McCallum, arXiv:1011.4088 (tutorial; ar5iv HTML rendering)
    url: https://ar5iv.labs.arxiv.org/html/1011.4088
    type: primary
    accessed: 2026-11-10
  - id: s4
    title: "Speech and Language Processing (3rd ed. draft), Chapter 18: Sequence Labeling for Parts of Speech and Named Entities"
    publisher: Daniel Jurafsky and James H. Martin, Stanford University (draft of August 19, 2026)
    url: https://web.stanford.edu/~jurafsky/slp3/18.pdf
    type: textbook
    accessed: 2026-11-10
  - id: s5
    title: "Neural Architectures for Named Entity Recognition"
    publisher: NAACL-HLT 2016, pp. 260-270 (Lample, Ballesteros, Subramanian, Kawakami, Dyer); arXiv:1603.01360
    url: https://arxiv.org/html/1603.01360
    type: peer-reviewed
    accessed: 2026-11-10
created: 2026-11-10
---

# Conditional random field

A **conditional random field (CRF)** is a probabilistic model of the conditional distribution of a label sequence given an observation sequence. Instead of modelling how the observations were generated, it scores an entire candidate labeling with a single exponential (log-linear) model built from weighted feature functions, and normalizes that score over every possible labeling of the same input.[^s1] Because it models p(y|x) directly, a CRF does not need a model of the inputs, so it can use rich, overlapping features of the observations without making them independent.[^s3] The chain-structured version, the **linear-chain CRF**, became a workhorse for sequence labeling in natural language processing, bioinformatics and computer vision.[^s3]

## Origin

CRFs were introduced by John Lafferty, Andrew McCallum and Fernando Pereira at the 18th International Conference on Machine Learning (ICML 2001).[^s2] The paper positioned them against two existing families. **Hidden Markov models** and stochastic grammars make strong independence assumptions about the observations; **maximum entropy Markov models (MEMMs)** and other directed discriminative models suffer from what the authors called the **label bias problem**.[^s2] In an MEMM, transition scores are normalized separately at each state, so a state's outgoing probability mass is fixed regardless of what is observed; a state with a single successor effectively ignores its observation, which biases decoding toward states with few outgoing transitions.[^s1] A CRF avoids this by normalizing once over whole label sequences, so observations can raise or lower the score of a path anywhere along it.[^s1]

## How it works

For a linear-chain CRF, each feature function f_k(y_t, y_{t-1}, x_t) looks at the current label, the previous label and the input, and has a learned weight θ_k. The probability of a label sequence is the exponential of the summed weighted features divided by an input-specific normalizer Z(x), which sums over all label sequences.[^s3] Features may look anywhere in the input, for example at the next word.[^s3] Jurafsky and Martin describe the model as a sequence-wide version of multinomial logistic regression; typical features come from templates such as the current word with its tag, the previous and current tag, and word-shape patterns that map "I.M.F." to "X.X.X" for unknown words.[^s4]

Inference reuses dynamic programming from HMMs. Despite its exponentially many terms, Z(x) and the per-position marginals are computed with the **forward-backward** algorithm, and the best labeling is found with **Viterbi**, which is the same recursion with max in place of sum.[^s3] Any HMM can be rewritten as a linear-chain CRF whose weights are its log transition and emission probabilities, but a CRF can also let transitions depend on the current observation.[^s3] Training maximizes the conditional log-likelihood; Lafferty et al. used iterative scaling and noted the objective is convex, so training reaches the global optimum.[^s1] Modern treatments use gradient-based optimization, with forward-backward supplying the gradients, and stress L1 or L2 **regularization** because overlapping features make weights redundant.[^s4][^s3]

## Evidence and limitations

On Penn Treebank part-of-speech tagging in the original paper, a CRF reached 5.55% per-word error versus 5.69% for an HMM and 6.37% for an MEMM; with spelling features added to both discriminative models, the CRF reached 4.27% versus 4.81% for the MEMM.[^s1] On synthetic data built to trigger label bias, the CRF learned to separate the two branches while the MEMM did not.[^s1]

The costs are mainly computational. Training calls inference repeatedly, and Lafferty et al. found CRF training slower than MEMM training.[^s1][^s3] Exact inference is efficient for linear chains but intractable for general graph structures, which then need approximate inference.[^s3] Classic CRF taggers also depend on feature templates designed by hand, and rare features are typically pruned.[^s4]

## In practice

Open-source implementations include CRF++, CRFSuite, MALLET and FACTORIE.[^s3] Since Collobert et al. (2011) placed a CRF on top of a convolutional network, CRFs have often served as the output layer of neural taggers rather than as standalone models.[^s4] In the LSTM-CRF of Lample et al. (NAACL 2016), a bidirectional LSTM produces per-token tag scores and a CRF layer adds a learned tag-to-tag transition matrix, so the model learns constraints such as I-PER never following B-LOC.[^s5] On CoNLL-2003 English named-entity recognition the LSTM-CRF scored 90.94 F1, and the CRF layer added about 1.8 F1 over the same LSTM without it.[^s5] As of the 2026 Jurafsky and Martin draft, neural taggers such as Transformer-based models are state of the art, with HMM and CRF taggers described as only slightly behind on part-of-speech tagging.[^s4]

## Connections

- **Broader:** a supervised **machine learning** model and an undirected **probabilistic graphical model** whose factors are log-linear.[^s3]
- **Introduced in:** Lafferty, McCallum and Pereira's ICML 2001 paper.[^s2]
- **Alternative to:** the **hidden Markov model**, its generative counterpart, and the **maximum entropy Markov model**, whose per-state normalization causes label bias.[^s1][^s3]
- **Extends:** **logistic regression**, which is the simplest CRF, with a single output variable.[^s3]
- **Used in:** **named-entity recognition**, framed as BIO sequence labeling.[^s4][^s5]
- **Related:** **supervised learning** (CRFs are trained on labeled sequences), **regularization** (essential with overlapping features), and **recurrent neural networks**, which supply the features in LSTM-CRF taggers.[^s4][^s5]

## Sources

[^s1]: Lafferty, McCallum, Pereira, "Conditional Random Fields: Probabilistic Models for Segmenting and Labeling Sequence Data", ICML 2001. https://home.cs.colorado.edu/~mozer/Teaching/syllabi/6622/papers/LaffertyMcCallumPereira2001.pdf (accessed 2026-11-10)
[^s2]: University of Pennsylvania ScholarlyCommons record for the ICML 2001 paper, pp. 282-289. https://repository.upenn.edu/cis_papers/159 (accessed 2026-11-10)
[^s3]: Sutton and McCallum, "An Introduction to Conditional Random Fields", arXiv:1011.4088. https://ar5iv.labs.arxiv.org/html/1011.4088 (accessed 2026-11-10)
[^s4]: Jurafsky and Martin, *Speech and Language Processing* (3rd ed. draft, August 2026), Chapter 18. https://web.stanford.edu/~jurafsky/slp3/18.pdf (accessed 2026-11-10)
[^s5]: Lample et al., "Neural Architectures for Named Entity Recognition", NAACL-HLT 2016, arXiv:1603.01360. https://arxiv.org/html/1603.01360 (accessed 2026-11-10)
