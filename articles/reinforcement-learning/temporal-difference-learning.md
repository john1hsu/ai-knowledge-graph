---
id: kt:temporal-difference-learning
type: Algorithm
title: Temporal-difference learning
aliases: [TD learning, TD(0), TD(lambda), temporal difference methods]
domain: reinforcement-learning
summary: >-
  A family of model-free reinforcement learning methods that learn value predictions from experience by
  nudging each estimate toward a later estimate (bootstrapping), driven by the TD error between
  temporally successive predictions rather than by the final outcome.
maturity: foundational
broader: [kt:reinforcement-learning]
related: [kt:markov-decision-process, kt:q-learning, kt:actor-critic, kt:deep-q-network, kt:sarsa]
relations:
  - {predicate: createdBy, object: kt:richard-sutton}
  - {predicate: introducedIn, object: kt:learning-to-predict-by-the-methods-of-temporal-differences}
  - {predicate: dependsOn, object: kt:markov-decision-process}
  - {predicate: enables, object: kt:q-learning}
  - {predicate: enables, object: kt:td-gammon}
  - {predicate: contrastsWith, object: kt:monte-carlo-methods}
sources:
  - id: s1
    title: "Learning to Predict by the Methods of Temporal Differences"
    publisher: Machine Learning 3:9-44, 1988 (Sutton), via ML Anthology
    url: https://mlanthology.org/mlj/1988/sutton1988mlj-learning
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s2
    title: "Chapter 6: Temporal Difference Learning (lecture slides for Reinforcement Learning: An Introduction)"
    publisher: University of Massachusetts Amherst CS687 (Sutton and Barto)
    url: https://people.cs.umass.edu/~barto/courses/cs687/Chapter%206.pdf
    type: textbook
    accessed: 2026-11-14
  - id: s3
    title: "Temporal Difference Learning and TD-Gammon"
    publisher: Communications of the ACM 38(3), March 1995 (Tesauro), reprinted at bkgm.com
    url: https://bkgm.com/articles/tesauro/tdl.html
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "Analysis of Temporal-Diffference Learning with Function Approximation"
    publisher: Advances in Neural Information Processing Systems 9 (NIPS 1996) (Tsitsiklis and Van Roy)
    url: https://papers.nips.cc/paper/1996/hash/e00406144c1e7e35240afed70f34166a-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "A Neural Substrate of Prediction and Reward"
    publisher: Science 275(5306):1593-1599, 1997 (Schultz, Dayan and Montague), via PubMed
    url: https://pubmed.ncbi.nlm.nih.gov/9054347/
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s6
    title: "A Neural Substrate of Prediction and Reward (author copy)"
    publisher: University of Massachusetts Amherst CS687 course reading (Schultz, Dayan and Montague, 1997)
    url: https://people.cs.umass.edu/~barto/courses/cs687/sdm97.pdf
    type: primary
    accessed: 2026-11-14
created: 2026-11-14
---

# Temporal-difference learning

**Temporal-difference (TD) learning** is a class of methods for learning to predict, and in reinforcement learning to estimate value functions, that assigns credit using the difference between temporally successive predictions instead of the difference between a prediction and the eventual outcome.[^s1] Richard Sutton formalized the idea in a 1988 *Machine Learning* paper, noting that it had appeared earlier, poorly understood, in Arthur Samuel's checkers player, Holland's bucket brigade and Sutton's own Adaptive Heuristic Critic; the paper proved convergence and optimality for special cases.[^s1] TD learning is the core of many later algorithms, including Sarsa, Q-learning and actor-critic methods.[^s2]

## How it works

The simplest variant, TD(0), evaluates a fixed policy. After observing a transition from state s_t to s_{t+1} with reward r_{t+1}, it updates the value estimate as V(s_t) ← V(s_t) + α[r_{t+1} + γV(s_{t+1}) − V(s_t)], where α is a step size and γ the discount factor.[^s2] The bracketed quantity, δ_t = r_{t+1} + γV(s_{t+1}) − V(s_t), is the **TD error**: how much better or worse things turned out one step later than the current estimate predicted.[^s2]

TD sits between two older families of methods. Like Monte Carlo methods it **samples**, learning from real transitions without a model of the environment; like dynamic programming it **bootstraps**, updating an estimate partly from another estimate (V(s_{t+1})) instead of waiting for the full return.[^s2] Monte Carlo needs the episode to end before it can update, while TD can update after every step and can learn from incomplete sequences.[^s2] Sutton argued this makes TD methods cheaper in memory and peak computation and, for most real prediction problems, more accurate than supervised-style methods that wait for outcomes.[^s1]

A worked example in Sutton and Barto's course material shows the difference: on the same eight training episodes, batch Monte Carlo minimizes error on the observed returns and assigns one state a value of 0, whereas batch TD(0) converges to the certainty-equivalence estimate of 0.75 implied by a maximum-likelihood model of the Markov process.[^s2] Under batch updating with a small enough step size, TD(0) converges for any finite Markov prediction task.[^s2]

**TD(λ)** generalizes the one-step update with a parameter λ that controls how far back in time a TD error's correction is propagated to earlier predictions.[^s3]

## From prediction to control

Turning TD prediction into control means learning action values. **Sarsa** is on-policy: it updates Q(s_t, a_t) toward the reward plus the value of the action actually taken next. **Q-learning** is off-policy: it bootstraps from the maximum action value in the next state, so it learns the greedy policy while behaving exploratorily.[^s2] In **actor-critic** methods, a critic learns values with TD and its TD error is used to judge the actor's chosen actions.[^s2]

## Landmark results

Gerald Tesauro's TD-Gammon (described in *Communications of the ACM*, 1995) trained a neural-network backgammon evaluator with TD(λ) purely by self-play from random initial weights.[^s3] Version 2.1 nearly tied expert Bill Robertie over 40 games, and the program's rollouts changed expert opening play.[^s3] Tesauro attributed part of the success to backgammon's dice, which diversify self-play experience, and to its smooth win-probability target.[^s3]

TD learning also became a model in neuroscience. Schultz, Dayan and Montague (*Science*, 1997) reported that primate midbrain dopamine neurons fire for unexpected rewards, shift their response to a predictive cue after learning, and dip below baseline when a predicted reward is omitted.[^s5] The authors modelled this activity with a TD-style prediction error of the form r(t) + γV(t+1) − V(t).[^s6]

## Limitations and open questions

Convergence guarantees are strongest in the tabular and linear cases. Tsitsiklis and Van Roy proved that online TD with a linear function approximator, run on a single trajectory of an irreducible, aperiodic finite Markov chain, converges with probability 1, and they bounded its approximation error; they also gave counter-examples showing the limits of those conditions.[^s4] Tesauro likewise noted that theory for nonlinear networks was limited, and that self-play pathologies had appeared in deterministic games such as checkers and Go.[^s3]

## Connections

TD learning is a core method of reinforcement learning (`broader kt:reinforcement-learning`) and assumes the state-transition structure of a Markov decision process (`dependsOn kt:markov-decision-process`).[^s2] It was created by Richard Sutton (`createdBy`) and formalized in his 1988 paper (`introducedIn`).[^s1] It `enables` Q-learning, which differs from the related on-policy Sarsa in bootstrapping from the greedy rather than the taken action, and the critic in actor-critic methods is a TD learner.[^s2] It also `enables` TD-Gammon, an early demonstration of TD combined with neural networks, a pairing later scaled up in the deep Q-network.[^s3] TD `contrastsWith` Monte Carlo methods, which sample but do not bootstrap.[^s2]

## Sources
[^s1]: R. S. Sutton, "Learning to Predict by the Methods of Temporal Differences", *Machine Learning* 3:9-44, 1988. https://mlanthology.org/mlj/1988/sutton1988mlj-learning (accessed 2026-11-14)
[^s2]: R. S. Sutton and A. G. Barto, "Chapter 6: Temporal Difference Learning", lecture slides for *Reinforcement Learning: An Introduction*, UMass Amherst CS687. https://people.cs.umass.edu/~barto/courses/cs687/Chapter%206.pdf (accessed 2026-11-14)
[^s3]: G. Tesauro, "Temporal Difference Learning and TD-Gammon", *Communications of the ACM* 38(3), 1995. https://bkgm.com/articles/tesauro/tdl.html (accessed 2026-11-14)
[^s4]: J. N. Tsitsiklis and B. Van Roy, "Analysis of Temporal-Diffference Learning with Function Approximation", NIPS 9, 1996. https://papers.nips.cc/paper/1996/hash/e00406144c1e7e35240afed70f34166a-Abstract.html (accessed 2026-11-14)
[^s5]: W. Schultz, P. Dayan and P. R. Montague, "A Neural Substrate of Prediction and Reward", *Science* 275(5306):1593-1599, 1997. https://pubmed.ncbi.nlm.nih.gov/9054347/ (accessed 2026-11-14)
[^s6]: W. Schultz, P. Dayan and P. R. Montague, "A Neural Substrate of Prediction and Reward" (author copy, course reading). https://people.cs.umass.edu/~barto/courses/cs687/sdm97.pdf (accessed 2026-11-14)
