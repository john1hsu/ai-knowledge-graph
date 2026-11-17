---
id: kt:upper-confidence-bound
type: Algorithm
title: Upper confidence bound
aliases: [UCB, UCB1, UCB algorithm, upper confidence bound algorithm]
domain: reinforcement-learning
summary: >-
  A family of bandit algorithms built on optimism in the face of uncertainty: each round the learner
  picks the action whose empirical mean reward plus a confidence bonus is largest, with the bonus
  shrinking as the action is tried more, which yields logarithmic regret.
maturity: foundational
broader: [kt:multi-armed-bandit, kt:exploration-exploitation]
related: [kt:thompson-sampling, kt:contextual-bandit, kt:reinforcement-learning, kt:recommender-system]
relations:
  - {predicate: introducedIn, object: kt:finite-time-analysis-of-the-multiarmed-bandit-problem}
  - {predicate: usedIn, object: kt:monte-carlo-tree-search}
  - {predicate: alternativeTo, object: kt:thompson-sampling}
  - {predicate: influencedBy, object: kt:asymptotically-efficient-adaptive-allocation-rules}
sources:
  - id: s1
    title: "Finite-time Analysis of the Multiarmed Bandit Problem"
    publisher: Machine Learning 47:235-256, 2002 (Auer, Cesa-Bianchi and Fischer), author's copy
    url: https://homes.di.unimi.it/%7Ecesabian/Pubblicazioni/ml-02.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "Bandit Algorithms (draft text), ch. 7 The Upper Confidence Bound Algorithm"
    publisher: Lattimore and Szepesvári, course copy hosted by IISc E1 245 Online Prediction and Learning, 2018
    url: https://ece.iisc.ac.in/~aditya/E1245_Online_Prediction_Learning_F2018/lattimore-szepesvari18bandit-algorithms.pdf
    type: textbook
    accessed: 2026-11-17
  - id: s3
    title: "Bandit Based Monte-Carlo Planning"
    publisher: ECML 2006, LNAI 4212 (Kocsis and Szepesvári), author's copy
    url: https://cs.nyu.edu/~shasha/papers/uct.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "The KL-UCB Algorithm for Bounded Stochastic Bandits and Beyond"
    publisher: COLT 2011, PMLR 19:359-376 (Garivier and Cappé)
    url: https://proceedings.mlr.press/v19/garivier11a.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "A Contextual-Bandit Approach to Personalized News Article Recommendation"
    publisher: WWW 2010 (Li, Chu, Langford and Schapire), Microsoft Research copy
    url: https://microsoft.com/en-us/research/wp-content/uploads/2016/02/p661.pdf
    type: peer-reviewed
    accessed: 2026-11-17
created: 2026-11-17
---

# Upper confidence bound

**Upper confidence bound (UCB)** algorithms are index policies for the stochastic multi-armed bandit. In every round each arm gets a score equal to its average observed reward plus an exploration bonus, and the learner plays the arm with the highest score.[^s1] The idea is the principle of *optimism in the face of uncertainty*: Lattimore and Szepesvári phrase it as acting as if the environment is as favourable as the data still plausibly allows.[^s2] An arm that has been tried only a few times has a wide confidence interval, so its optimistic estimate is high and it gets explored; an arm that has been tried often is judged mostly on its mean, so exploitation takes over.[^s2]

## Origins

Lattimore and Szepesvári credit Lai and Robbins (1985) with introducing confidence bounds into the bandit problem and analysing their asymptotics, and attribute the first UCB algorithm to Lai (1987); Katehakis and Robbins (1995) gave a simple analysis for Gaussian rewards, and Agrawal (1995) observed that any suitable sequence of upper confidence bounds suffices.[^s2] Lai and Robbins also proved that any consistent policy must incur regret growing at least logarithmically in the number of plays, with a constant set by the Kullback–Leibler divergence between arms.[^s1] The version most practitioners know, **UCB1**, comes from Auer, Cesa-Bianchi and Fischer's 2002 *Machine Learning* paper, whose contribution was to show that logarithmic regret holds uniformly over time, not just asymptotically, with a policy that is simple to compute and needs only rewards bounded in [0, 1].[^s1]

## How it works

UCB1 first plays each of the K arms once. Afterwards, at round n it plays the arm j maximizing x̄ⱼ + √(2 ln n / nⱼ), where x̄ⱼ is that arm's average reward and nⱼ the number of times it has been played.[^s1] The bonus acts as a confidence width: it grows slowly with total time, so neglected arms are eventually revisited, and it shrinks as an arm accumulates samples.[^s1] Auer et al. proved that UCB1's expected regret after n plays is at most 8 Σ (ln n)/Δᵢ over suboptimal arms plus a constant term, where Δᵢ is the gap between arm i's mean and the best mean.[^s1] The textbook variant UCB(δ) uses the bonus √(2 log(1/δ)/Tᵢ); with δ = 1/n² it has a gap-dependent regret bound of order Σ log(n)/Δᵢ and a worst-case bound of order √(nK log n).[^s2]

As a small example, suppose two arms have average rewards 0.6 after 100 pulls and 0.5 after 4 pulls at round 104. The second arm's bonus, √(2 ln 104 / 4) ≈ 1.52, dwarfs the first's ≈ 0.30, so UCB1 tries the less-sampled arm despite its lower mean. The arithmetic follows directly from the UCB1 index.[^s1]

## Variants and limitations

UCB1's leading constant is worse than the optimal Lai–Robbins constant, which its authors acknowledged; their UCB2 schedules plays in exponentially growing epochs and brings the constant arbitrarily close to the optimum, while the heuristic UCB1-Tuned replaces the fixed width with a variance-aware one.[^s1] In their Bernoulli experiments UCB1-Tuned performed comparably to a well-tuned ε-greedy rule and was robust to arm variance, but no regret bound was proved for it; ε-greedy itself did well only when tuned using knowledge of the reward gap.[^s1] Garivier and Cappé's **KL-UCB** builds the confidence bound from the Kullback–Leibler divergence instead; at COLT 2011 they showed it matches the Lai–Robbins lower bound for Bernoulli rewards and has a uniformly better regret bound than UCB for bounded rewards, and in their simulations it was the only method that always beat basic UCB.[^s4] Standard UCB assumes stationary, independent rewards per arm; adversarial or changing environments call for other algorithms.[^s2]

## In practice

UCB's biggest legacy is in planning. Kocsis and Szepesvári's **UCT** algorithm treats action choice at every node of a search tree as a separate bandit and selects moves with a UCB1-style bias term, tuned to cope with the drifting payoffs that arise as the subtree below is refined.[^s3] They proved that UCT's probability of choosing a wrong action at the root goes to zero, and in their experiments it needed far fewer samples than competing planners on a sailing MDP.[^s3] In recommendation, Li et al.'s **LinUCB** carries the UCB idea into contextual bandits by adding a confidence width to a ridge-regression estimate of each article's payoff; on Yahoo! front-page traffic it achieved a 12.5% click lift over a context-free ε-greedy baseline (reported in 2010), and a tunable parameter α controls how aggressively it explores.[^s5]

## Connections

UCB is a strategy for the `kt:multi-armed-bandit` problem and one of the two principled answers to the `kt:exploration-exploitation` dilemma, the other being its `alternativeTo`, `kt:thompson-sampling`.[^s2] It was `introducedIn` its finite-time form by `kt:finite-time-analysis-of-the-multiarmed-bandit-problem` and `influencedBy` Lai and Robbins' `kt:asymptotically-efficient-adaptive-allocation-rules`.[^s1][^s2] It is `usedIn` `kt:monte-carlo-tree-search` through UCT, a planning method for the finite-horizon MDPs studied in `kt:reinforcement-learning`.[^s3] LinUCB extends it to the `kt:contextual-bandit` setting that powers `kt:recommender-system` personalization.[^s5]

## Sources
[^s1]: Auer, P., Cesa-Bianchi, N. and Fischer, P., "Finite-time Analysis of the Multiarmed Bandit Problem", *Machine Learning* 47:235–256, 2002. https://homes.di.unimi.it/%7Ecesabian/Pubblicazioni/ml-02.pdf (accessed 2026-11-17)
[^s2]: Lattimore, T. and Szepesvári, C., *Bandit Algorithms* (draft), ch. 7. https://ece.iisc.ac.in/~aditya/E1245_Online_Prediction_Learning_F2018/lattimore-szepesvari18bandit-algorithms.pdf (accessed 2026-11-17)
[^s3]: Kocsis, L. and Szepesvári, C., "Bandit Based Monte-Carlo Planning", ECML 2006. https://cs.nyu.edu/~shasha/papers/uct.pdf (accessed 2026-11-17)
[^s4]: Garivier, A. and Cappé, O., "The KL-UCB Algorithm for Bounded Stochastic Bandits and Beyond", COLT 2011, PMLR 19. https://proceedings.mlr.press/v19/garivier11a.html (accessed 2026-11-17)
[^s5]: Li, L., Chu, W., Langford, J. and Schapire, R. E., "A Contextual-Bandit Approach to Personalized News Article Recommendation", WWW 2010. https://microsoft.com/en-us/research/wp-content/uploads/2016/02/p661.pdf (accessed 2026-11-17)
