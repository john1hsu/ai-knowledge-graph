---
id: kt:thompson-sampling
type: Algorithm
title: Thompson sampling
aliases: [posterior sampling, probability matching, Bayesian bandit sampling]
domain: reinforcement-learning
summary: >-
  A Bayesian strategy for the exploration-exploitation trade-off in which the learner draws one sample
  from its posterior over each action's value and plays the action whose sample is best, so each action
  is chosen with the posterior probability that it is optimal.
maturity: foundational
broader: [kt:multi-armed-bandit, kt:exploration-exploitation]
related: [kt:contextual-bandit, kt:recommender-system, kt:bayesian-inference, kt:reinforcement-learning, kt:information-directed-sampling]
relations:
  - {predicate: introducedIn, object: kt:on-the-likelihood-that-one-unknown-probability-exceeds-another}
  - {predicate: createdBy, object: kt:william-r-thompson}
  - {predicate: alternativeTo, object: kt:upper-confidence-bound}
sources:
  - id: s1
    title: "A Tutorial on Thompson Sampling"
    publisher: Foundations and Trends in Machine Learning 11(1):1-96, 2018 (Russo, Van Roy, Kazerouni, Osband and Wen), authors' arXiv version 1707.02038v3
    url: https://arxiv.org/pdf/1707.02038
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "An Empirical Evaluation of Thompson Sampling"
    publisher: Advances in Neural Information Processing Systems 24 (NIPS 2011), Chapelle and Li
    url: https://papers.nips.cc/paper/2011/hash/e53a0a2978c28872a4505bdb51db06dc-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "Analysis of Thompson Sampling for the Multi-armed Bandit Problem"
    publisher: Proceedings of the 25th Conference on Learning Theory (COLT 2012), PMLR 23:39.1-39.26 (Agrawal and Goyal)
    url: https://proceedings.mlr.press/v23/agrawal12.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "On the Likelihood that One Unknown Probability Exceeds Another in View of the Evidence of Two Samples"
    publisher: Biometrika 25(3/4):285-294, 1933 (W. R. Thompson), bibliographic record via Scilit, DOI 10.2307/2332286
    url: https://scilit.com/publications/3b2c486513e80dfc7acce5004b46ba1e
    type: primary
    accessed: 2026-11-18
  - id: s5
    title: "Bandit Algorithms, table of contents (ch. 36 Thompson Sampling)"
    publisher: Cambridge University Press, 2020 (Lattimore and Szepesvári)
    url: https://assets.cambridge.org/97811084/86828/toc/9781108486828_toc.pdf
    type: textbook
    accessed: 2026-11-18
created: 2026-11-18
---

# Thompson sampling

**Thompson sampling** (also called posterior sampling or probability matching) is a Bayesian algorithm for sequential decision problems in which an agent must trade off exploiting what it already knows against exploring to learn more. In each round it samples a plausible model of the world from its current posterior and acts optimally for that sample, which means each action is played with the posterior probability that it is the best one.[^s1][^s3] It is one of the two canonical approaches to the stochastic multi-armed bandit (`kt:multi-armed-bandit`), alongside upper confidence bound methods, and has a dedicated chapter in Lattimore and Szepesvári's standard bandit textbook.[^s5]

## Origin

William R. Thompson proposed the idea in a 1933 *Biometrika* paper on judging, from two small samples, how likely it is that one unknown success probability exceeds another, motivated by deciding which of two treatments to give patients.[^s4][^s1] The method was rediscovered several times but largely ignored by the academic literature for decades.[^s1] Interest returned around 2010–2011, notably after Chapelle and Li reported at NIPS 2011 that this very old heuristic was highly competitive with alternatives on simulated and real data, and argued that its simplicity made it a natural standard baseline.[^s2][^s1]

## How it works

The textbook case is the Beta-Bernoulli bandit, where each of K actions succeeds with an unknown probability θ_k.[^s1]

1. Give each action a Beta(α_k, β_k) prior over θ_k (Beta(1,1) is uniform).[^s1]
2. Each round, draw one sample θ̂_k from every action's Beta posterior and play the action with the largest sample.[^s1]
3. Observe the 0/1 reward r and update only the chosen action: α ← α + r and β ← β + (1 − r).[^s1]

Exploration arises automatically: an action with few observations has a wide posterior, so it occasionally produces a high sample and gets tried, while actions confidently known to be poor almost never win the draw. Russo and colleagues stress that the randomness is over the model parameter, not over the observed outcome.[^s1] When the posterior has no closed form, as with neural network models or rich contextual problems, practitioners substitute approximate samples from Gibbs sampling, a Laplace (Gaussian) approximation, Langevin Monte Carlo, or a bootstrap over the data history.[^s1]

## Theory

For years the method's strong empirical results outpaced its theory. Agrawal and Goyal (COLT 2012) gave the first proof that Thompson sampling achieves logarithmic expected regret on the stochastic multi-armed bandit problem, with bounds they describe as optimal up to the dependence on the reward gaps and constant factors.[^s3] Later work, summarised in the 2018 tutorial, showed that for Beta-Bernoulli bandits its regret matches the Lai–Robbins asymptotic lower bound, gave near-optimal worst-case bounds of order √(KT log T), and developed Bayesian-regret and information-theoretic analyses for linear and structured problems.[^s1]

## Limitations

Thompson sampling is not universally the right tool. The tutorial identifies settings where it underperforms: problems that need no active exploration (where greedier methods win), pure best-arm identification (where it exploits too early), time-sensitive problems where settling quickly for a good-enough action beats finding the best, and problems where an action that is never optimal is nonetheless the most informative one to try. Information-directed sampling was proposed to handle the last class, at higher computational cost.[^s1] Its quality also depends on the prior and on how faithfully approximate posterior samples reflect real uncertainty.[^s1]

## In practice

According to the 2018 tutorial, Thompson sampling had been adopted at companies including Adobe, Amazon, Facebook, Google, LinkedIn, Microsoft, Netflix and Twitter, for tasks such as online advertising, recommendation and website optimisation.[^s1] Its appeal is that it is easy to implement, extends naturally to structured and contextual problems, and copes well with delayed feedback.[^s1][^s3]

## Connections

Thompson sampling is a specific algorithm for the multi-armed bandit (`kt:multi-armed-bandit`) problem and a principled answer to the exploration-exploitation (`kt:exploration-exploitation`) dilemma, hence its broader links.[^s1] It is an alternative to upper confidence bound (`kt:upper-confidence-bound`) methods: UCB is explicitly optimistic, while Thompson sampling's optimism is implicit in posterior randomness, and UCB-style analyses can be reused to bound its regret.[^s1] It extends to the contextual bandit (`kt:contextual-bandit`) setting used in recommender systems (`kt:recommender-system`), rests on Bayesian inference (`kt:bayesian-inference`), and generalises to reinforcement learning (`kt:reinforcement-learning`) in Markov decision processes as posterior sampling for RL.[^s1] It was introduced in Thompson's 1933 paper, and `kt:information-directed-sampling` was later proposed to address its weaknesses on information-gathering problems.[^s4][^s1]

## Sources
[^s1]: Russo, Van Roy, Kazerouni, Osband and Wen, "A Tutorial on Thompson Sampling", Foundations and Trends in Machine Learning 11(1), 2018. https://arxiv.org/pdf/1707.02038 (accessed 2026-11-18)
[^s2]: Chapelle and Li, "An Empirical Evaluation of Thompson Sampling", NIPS 2011. https://papers.nips.cc/paper/2011/hash/e53a0a2978c28872a4505bdb51db06dc-Abstract.html (accessed 2026-11-18)
[^s3]: Agrawal and Goyal, "Analysis of Thompson Sampling for the Multi-armed Bandit Problem", COLT 2012, PMLR 23. https://proceedings.mlr.press/v23/agrawal12.html (accessed 2026-11-18)
[^s4]: Thompson, "On the Likelihood that One Unknown Probability Exceeds Another in View of the Evidence of Two Samples", Biometrika 25(3/4), 1933. https://scilit.com/publications/3b2c486513e80dfc7acce5004b46ba1e (accessed 2026-11-18)
[^s5]: Lattimore and Szepesvári, *Bandit Algorithms*, Cambridge University Press, table of contents. https://assets.cambridge.org/97811084/86828/toc/9781108486828_toc.pdf (accessed 2026-11-18)
