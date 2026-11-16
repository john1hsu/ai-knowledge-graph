---
id: kt:multi-armed-bandit
type: Concept
title: Multi-armed bandit
aliases: [multi-armed bandit problem, multiarmed bandit, MAB, bandit problem, k-armed bandit]
domain: reinforcement-learning
summary: >-
  A sequential decision problem in which a learner repeatedly picks one of several actions ("arms"),
  observes only the reward of the arm it picked, and tries to maximize cumulative reward, measured by
  regret against the best arm or policy in hindsight.
maturity: foundational
broader: [kt:reinforcement-learning]
related: [kt:exploration-exploitation, kt:upper-confidence-bound, kt:thompson-sampling, kt:contextual-bandit, kt:recommender-system]
relations:
  - {predicate: usedIn, object: kt:monte-carlo-tree-search}
  - {predicate: contrastsWith, object: kt:markov-decision-process}
sources:
  - id: s1
    title: "Bandit Algorithms (draft text)"
    publisher: Lattimore and Szepesvári, course copy hosted by IISc E1 245 Online Prediction and Learning, 2018
    url: https://ece.iisc.ac.in/~aditya/E1245_Online_Prediction_Learning_F2018/lattimore-szepesvari18bandit-algorithms.pdf
    type: textbook
    accessed: 2026-11-16
  - id: s2
    title: "Bandit Algorithms"
    publisher: Cambridge University Press, 2020 (Lattimore and Szepesvári)
    url: https://www.cambridge.org/9781108486828
    type: textbook
    accessed: 2026-11-16
  - id: s3
    title: "Some aspects of the sequential design of experiments"
    publisher: Bulletin of the American Mathematical Society 58:527-535, 1952 (Robbins)
    url: https://community.ams.org/journals/bull/1952-58-05/S0002-9904-1952-09620-8/S0002-9904-1952-09620-8.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s4
    title: "The Nonstochastic Multiarmed Bandit Problem"
    publisher: SIAM Journal on Computing 32(1):48-77, 2002 (Auer, Cesa-Bianchi, Freund and Schapire)
    url: https://homepages.math.uic.edu/~lreyzin/papers/auer02.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "A Contextual-Bandit Approach to Personalized News Article Recommendation"
    publisher: arXiv 1003.0146; version in WWW 2010 (Li, Chu, Langford and Schapire)
    url: https://arxiv.org/pdf/1003.0146
    type: primary
    accessed: 2026-11-16
created: 2026-11-16
---

# Multi-armed bandit

A **multi-armed bandit** is a sequential game between a learner and an environment. In each of n rounds the learner picks an action and receives a reward; it never sees the future, only its own past actions and rewards, and it does not know the environment beyond the class it belongs to.[^s1] The name comes from the "one-armed bandit" slot machine: in the 1950s Mosteller and Bush studied mice and then people choosing between options with unknown payoffs, and the two-choice version became the "two-armed bandit".[^s1] Lattimore and Szepesvári's 2020 Cambridge textbook treats the problem as a general framework for decision-making under uncertainty, covering stochastic, adversarial and Bayesian settings and ending with learning in Markov decision processes.[^s2]

## Origins

Lattimore and Szepesvári trace the problem to William R. Thompson's 1933 *Biometrika* paper, which was motivated by medical trials that adapt treatment allocation as evidence accumulates, and credit Herbert Robbins with popularizing it.[^s1] Robbins' 1952 paper posed sampling from two populations with unknown means, where the aim is to make the expected sum of observations as large as possible and, unusually for statistics, there is no terminal decision to make.[^s3] For two coins he analysed a "stay on a head, switch on a tail" rule whose worst-case asymptotic loss is about 17.2 cents per toss, against 50 cents for picking a coin at random and sticking with it.[^s3] He then showed that following the higher sample mean, while forcing samples from each population on two sparse, density-zero sequences of rounds, drives the average reward to the better mean for any populations whose means exist.[^s3] That forced-sampling idea is the ancestor of the exploration schedules used in later algorithms.

## Formulation and regret

Performance is measured by **regret**: the gap between the expected total reward of the best policy in some competitor class and the learner's expected total reward. A learner is considered good when regret grows sublinearly in n, so that its average reward approaches the best achievable.[^s1] Two main settings differ in what generates the rewards:[^s1]

- **Stochastic bandits.** Each arm has a fixed reward distribution, independent of past play; a Bernoulli bandit, where each arm pays 1 with an unknown probability, is the textbook case.[^s1]
- **Adversarial bandits.** Rewards are arbitrary bounded values chosen without seeing the learner's actions, and regret is measured against the best single fixed arm.[^s1][^s4]

Auer, Cesa-Bianchi, Freund and Schapire's adversarial analysis drops every statistical assumption and lets an adversary set the payoffs.[^s4] Their **Exp3** algorithm mixes a uniform distribution with exponential weights on estimated cumulative rewards, and divides each observed reward by the probability of having chosen that arm so the estimates stay unbiased for every arm.[^s4] It achieves expected regret of order √(TK ln K) over T rounds and K arms, against a proven lower bound of order √(KT) for any algorithm.[^s4] Intermediate settings, such as stochastic but non-stationary rewards, sit between these two extremes.[^s1]

## Contextual bandits

In many applications the learner sees side information before choosing. In a **contextual bandit** the best arm depends on that context; a crude approach clusters users and runs a separate bandit per cluster, and much of the modern literature studies how to exploit context more efficiently.[^s1] Li, Chu, Langford and Schapire framed Yahoo! front-page news recommendation this way and proposed **LinUCB**, which models each article's click rate as linear in a feature vector, fits the coefficients with ridge regression and chooses the article with the highest estimate plus a confidence term.[^s5] On more than 33 million logged events from the Yahoo! Today Module they reported a 12.5% click lift over a standard context-free bandit, with a larger advantage when data was scarce; they evaluated offline by replaying uniformly random logged traffic, keeping only events where the policy matched the logged choice, which gives an unbiased estimate.[^s5] Context-free bandits struggled there because the article pool changes often and many visitors are new.[^s5]

## Applications and limitations

Lattimore and Szepesvári list A/B testing (where the goal shifts from learning which variant wins to earning reward while testing), advert placement, recommendation, network routing, dynamic pricing, cache allocation and tree search; they note that clinical trials, the original motivation, have not yet widely adopted bandit designs.[^s1] Recommendation stretches the basic model, since action sets become combinatorially large and feedback depends on what users are shown.[^s1] The basic bandit also has no state: an action does not change future situations, which is what separates it from full reinforcement learning in MDPs.[^s1][^s2]

## Connections

The bandit is the simplest formal setting of `kt:reinforcement-learning` and the standard model for the `kt:exploration-exploitation` dilemma.[^s1] `kt:upper-confidence-bound` rules and `kt:thompson-sampling` are its best-known stochastic strategies; Exp3 covers the adversarial case.[^s4] `kt:contextual-bandit` methods such as LinUCB extend it with side information and power `kt:recommender-system` personalization.[^s5] It is `usedIn` `kt:monte-carlo-tree-search`, whose UCT variant treats each tree node as a bandit, and it `contrastsWith` the `kt:markov-decision-process`, where actions change the state.[^s1]

## Sources
[^s1]: Lattimore, T. and Szepesvári, C., *Bandit Algorithms* (draft), ch. 1. https://ece.iisc.ac.in/~aditya/E1245_Online_Prediction_Learning_F2018/lattimore-szepesvari18bandit-algorithms.pdf (accessed 2026-11-16)
[^s2]: Lattimore, T. and Szepesvári, C., *Bandit Algorithms*, Cambridge University Press, 2020. https://www.cambridge.org/9781108486828 (accessed 2026-11-16)
[^s3]: Robbins, H., "Some aspects of the sequential design of experiments", *Bulletin of the AMS* 58:527–535, 1952. https://community.ams.org/journals/bull/1952-58-05/S0002-9904-1952-09620-8/S0002-9904-1952-09620-8.pdf (accessed 2026-11-16)
[^s4]: Auer, P., Cesa-Bianchi, N., Freund, Y. and Schapire, R. E., "The Nonstochastic Multiarmed Bandit Problem", *SIAM Journal on Computing* 32(1):48–77, 2002. https://homepages.math.uic.edu/~lreyzin/papers/auer02.pdf (accessed 2026-11-16)
[^s5]: Li, L., Chu, W., Langford, J. and Schapire, R. E., "A Contextual-Bandit Approach to Personalized News Article Recommendation", WWW 2010 (arXiv:1003.0146). https://arxiv.org/pdf/1003.0146 (accessed 2026-11-16)
