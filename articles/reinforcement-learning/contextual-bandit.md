---
id: kt:contextual-bandit
type: Concept
title: Contextual bandit
aliases: [contextual bandits, contextual multi-armed bandit, bandits with side information, associative bandit]
domain: reinforcement-learning
summary: >-
  A sequential decision problem in which the learner observes a context each round, picks one of K
  actions, and sees the reward of that action only; the goal is to compete with the best policy
  (a mapping from contexts to actions) in a given class.
maturity: established
broader: [kt:multi-armed-bandit, kt:reinforcement-learning]
related: [kt:exploration-exploitation, kt:thompson-sampling, kt:upper-confidence-bound, kt:recommender-system, kt:off-policy-evaluation, kt:online-learning]
relations:
  - {predicate: introducedIn, object: kt:the-epoch-greedy-algorithm-for-contextual-multi-armed-bandits}
  - {predicate: usedIn, object: kt:recommender-system}
  - {predicate: implementedIn, object: kt:vowpal-wabbit}
  - {predicate: contrastsWith, object: kt:markov-decision-process}
  - {predicate: contrastsWith, object: kt:supervised-learning}
sources:
  - id: s1
    title: "The Epoch-Greedy Algorithm for Multi-armed Bandits with Side Information"
    publisher: NeurIPS 2007 (Langford and Zhang)
    url: https://papers.neurips.cc/paper_files/paper/2007/file/4b04a686b0ad13dce35fa99fa4161c65-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "Contextual Bandit Algorithms with Supervised Learning Guarantees"
    publisher: AISTATS 2011, PMLR 15:19-26 (Beygelzimer, Langford, Li, Reyzin and Schapire)
    url: https://proceedings.mlr.press/v15/beygelzimer11a.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "Taming the Monster: A Fast and Simple Algorithm for Contextual Bandits"
    publisher: arXiv 1402.0555; ICML 2014, PMLR 32(2):1638-1646 (Agarwal, Hsu, Kale, Langford, Li and Schapire)
    url: https://arxiv.org/pdf/1402.0555
    type: primary
    accessed: 2026-11-18
  - id: s4
    title: "Doubly Robust Policy Evaluation and Learning"
    publisher: arXiv 1103.4601; ICML 2011 (Dudík, Langford and Li)
    url: https://www.arxiv.org/abs/1103.4601
    type: primary
    accessed: 2026-11-18
  - id: s5
    title: "Contextual Bandits (Vowpal Wabbit Python tutorial, v9.6.0)"
    publisher: Vowpal Wabbit project documentation
    url: https://vowpalwabbit.org/docs/vowpal_wabbit/python/9.6.0/tutorials/python_Contextual_bandits_and_Vowpal_Wabbit.html
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# Contextual bandit

A **contextual bandit** is a repeated game in which, every round, the learner is shown a context x (for example user and page features), chooses one of k actions, and observes a reward in [0, 1] for the chosen action only; the rewards of the actions it did not take stay hidden.[^s1] Langford and Zhang's 2007 formulation draws the context and the full reward vector together from a fixed but unknown distribution, and measures the learner against a hypothesis class H of functions from contexts to actions: regret is the expected reward of the best h in H minus the learner's expected reward.[^s1] The same problem appears in the literature as bandits with side information and as associative reinforcement learning.[^s1] It sits between the plain multi-armed bandit, which has no context, and full reinforcement learning, where actions also change future states.

## Relation to supervised learning

The contextual bandit is often described as supervised learning with partial labels. If the learner picks actions at random with known probabilities, it can divide each observed reward by the probability of the chosen action, and this importance-weighted data has the same expected reward as fully labelled data for every candidate policy.[^s1] That reduction lets ordinary supervised sample-complexity bounds control bandit regret, and it is why most practical algorithms are built around a supervised learner, or "oracle", rather than per-policy bookkeeping.[^s1][^s3] The difference from supervised learning is that the learner chooses which label it gets to see, so poor exploration produces biased data that no later training can repair.

## Key algorithms

- **Epoch-Greedy (2007).** Alternates single uniformly random exploration rounds with growing runs of exploitation using the empirically best hypothesis; it needs no known horizon and has regret of order T^(2/3) in the worst case.[^s1]
- **Exp4 and Exp4.P (2011).** Exp4 keeps exponential weights over N expert policies; Exp4.P modifies it so the O(√(KT ln N)) regret holds with high probability, and extends to infinite classes of VC dimension d.[^s2]
- **ILOVETOCONBANDITS (2014).** Agarwal and colleagues reach the optimal regret rate for general policy classes while calling a cost-sensitive classification oracle only about √(KT) times in T rounds, by solving a small convex program that keeps estimated regret low and bounds the variance of every policy's value estimate.[^s3]

Linear-payoff methods such as LinUCB instead assume a parametric reward model and add a confidence bonus to its predictions, trading generality for a simpler update.[^s3] In the 2014 paper's experiment on the RCV1 text dataset (781,265 examples) recast as a bandit problem, the online variant "Online Cover" reached 0.053 progressive 0/1 loss against 0.051 for a fully supervised learner, while ε-greedy reached 0.148 and LinUCB 0.128 at far higher running time.[^s3] These are the authors' own reported figures on one benchmark.

## Off-policy evaluation

Because deployed systems log their contexts, actions and action probabilities, a new policy can be scored on old data without being launched. Dudík, Langford and Li note that estimators which model rewards tend to be biased, while those which reweight by the logging policy's probabilities tend to have high variance.[^s4] Their **doubly robust** estimator combines the two and stays accurate if either the reward model or the model of the past policy is good; in experiments it lowered the variance of value estimates and yielded better learned policies.[^s4] This ability to evaluate and train counterfactually from logs is a large part of why contextual bandits are used in production advertising and recommendation.[^s4]

## In practice

The open-source Vowpal Wabbit library exposes contextual bandit learning directly: each logged example records the action, its cost and the probability with which it was chosen, plus features, and the probability field is what makes learning from logged data possible.[^s5] As of its 9.x documentation, it offers exploration strategies including explore-first, ε-greedy, bagging, online cover and softmax, estimators selected as inverse propensity scoring, doubly robust, direct method or MTR, and an "action-dependent features" format for action sets that change or carry their own features, such as a shifting pool of news articles.[^s5] Common limitations are that the action is assumed not to affect future contexts, and that guarantees depend on logged probabilities being recorded correctly and kept away from zero, which is why algorithms such as ILOVETOCONBANDITS give every action a minimum probability.[^s1][^s3][^s4]

## Connections

The contextual bandit is the context-aware extension of the `kt:multi-armed-bandit` and the simplest setting of `kt:reinforcement-learning` with features; it `contrastsWith` the `kt:markov-decision-process`, where actions change state, and with `kt:supervised-learning`, where every label is observed.[^s1] Langford and Zhang's Epoch-Greedy paper set out the policy-class formulation used by later work.[^s1] It is the standard formal model of the `kt:exploration-exploitation` trade-off when side information is available, and `kt:upper-confidence-bound` rules such as LinUCB carry over to it, while `kt:thompson-sampling` is a related Bayesian alternative.[^s3] Its importance-weighted estimators underpin `kt:off-policy-evaluation`, and it is widely `usedIn` `kt:recommender-system` personalization.[^s4] Exp4-style algorithms come from adversarial `kt:online-learning`, and practical systems are `implementedIn` `kt:vowpal-wabbit`.[^s2][^s5]

## Sources
[^s1]: Langford, J. and Zhang, T., "The Epoch-Greedy Algorithm for Multi-armed Bandits with Side Information", NeurIPS 2007. https://papers.neurips.cc/paper_files/paper/2007/file/4b04a686b0ad13dce35fa99fa4161c65-Paper.pdf (accessed 2026-11-18)
[^s2]: Beygelzimer, A., Langford, J., Li, L., Reyzin, L. and Schapire, R. E., "Contextual Bandit Algorithms with Supervised Learning Guarantees", AISTATS 2011, PMLR 15:19–26. https://proceedings.mlr.press/v15/beygelzimer11a.html (accessed 2026-11-18)
[^s3]: Agarwal, A., Hsu, D., Kale, S., Langford, J., Li, L. and Schapire, R. E., "Taming the Monster: A Fast and Simple Algorithm for Contextual Bandits", ICML 2014 (arXiv:1402.0555). https://arxiv.org/pdf/1402.0555 (accessed 2026-11-18)
[^s4]: Dudík, M., Langford, J. and Li, L., "Doubly Robust Policy Evaluation and Learning", ICML 2011 (arXiv:1103.4601). https://www.arxiv.org/abs/1103.4601 (accessed 2026-11-18)
[^s5]: Vowpal Wabbit, "Contextual Bandits" Python tutorial (v9.6.0). https://vowpalwabbit.org/docs/vowpal_wabbit/python/9.6.0/tutorials/python_Contextual_bandits_and_Vowpal_Wabbit.html (accessed 2026-11-18)
