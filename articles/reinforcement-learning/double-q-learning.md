---
id: kt:double-q-learning
type: Algorithm
title: Double Q-learning
aliases: [double learning, double estimator Q-learning]
domain: reinforcement-learning
summary: >-
  An off-policy temporal-difference control algorithm that keeps two independent action-value estimates
  and uses one to pick the greedy next action and the other to value it, removing the upward
  maximization bias that makes standard Q-learning overestimate action values.
maturity: foundational
broader: [kt:q-learning, kt:temporal-difference-learning]
related: [kt:deep-q-network, kt:sarsa, kt:actor-critic, kt:soft-actor-critic, kt:exploration-exploitation]
relations:
  - {predicate: extends, object: kt:q-learning}
  - {predicate: createdBy, object: kt:hado-van-hasselt}
  - {predicate: mitigates, object: kt:maximization-bias}
  - {predicate: dependsOn, object: kt:markov-decision-process}
  - {predicate: enables, object: kt:twin-delayed-ddpg}
sources:
  - id: s1
    title: "Double Q-learning"
    publisher: Advances in Neural Information Processing Systems 23 (NIPS 2010), van Hasselt
    url: https://papers.nips.cc/paper/3964-double-q-learning
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s2
    title: "Reinforcement Learning: An Introduction (2nd ed.), section 6.7 Maximization Bias and Double Learning"
    publisher: MIT Press, 2018 (Sutton and Barto), course copy hosted by Texas A&M CSCE 421
    url: https://people.engr.tamu.edu/guni/csce421/files/RLbook2018.pdf
    type: textbook
    accessed: 2026-11-19
  - id: s3
    title: "Deep Reinforcement Learning with Double Q-learning"
    publisher: AAAI 2016 (van Hasselt, Guez and Silver), authors' arXiv version 1509.06461 via ar5iv
    url: https://ar5iv.labs.arxiv.org/html/1509.06461
    type: primary
    accessed: 2026-11-19
  - id: s4
    title: "Addressing Function Approximation Error in Actor-Critic Methods"
    publisher: ICML 2018, PMLR 80 (Fujimoto, van Hoof and Meger), arXiv 1802.09477
    url: https://www.arxiv.org/pdf/1802.09477
    type: primary
    accessed: 2026-11-19
created: 2026-11-19
---

# Double Q-learning

**Double Q-learning** is a model-free, off-policy reinforcement learning algorithm that fixes a systematic flaw in Q-learning: its tendency to overestimate action values. Hado van Hasselt introduced it at NIPS 2010, tracing the overestimation to Q-learning's use of the maximum of *estimated* action values as a stand-in for the maximum *expected* action value.[^s1] His remedy was a double estimator for the maximum expected value of a set of random variables, which he proved still converges to the optimal policy and showed to work well in stochastic settings where Q-learning struggles.[^s1]

## The problem: maximization bias

Control methods such as Q-learning build their targets from a maximum over estimated values, which Sutton and Barto call *maximization bias*.[^s2] If several actions all have true value zero but noisy estimates, the largest estimate is probably positive, so the maximum is biased upward.[^s2] Their Example 6.7 makes this concrete: from start state A, action *right* ends the episode with reward zero, while *left* leads to state B, where many actions end with rewards drawn from a normal distribution with mean −0.1 and variance 1.0.[^s2] Going left is always worse, yet noise makes some action at B look good, so ε-greedy Q-learning (ε = 0.1) at first strongly prefers left and, even asymptotically, takes it about 5% more often than optimal.[^s2]

## How it works

The bias arises because the same samples both choose the best action and estimate its value. Double learning splits the experience into two independent estimates, Q₁ and Q₂: one selects A* = argmax Q₁(a) and the other values it as Q₂(A*), and since E[Q₂(A*)] = q(A*) this estimate is unbiased.[^s2] The double estimator can therefore sometimes *underestimate*, rather than consistently overestimate.[^s1]

In the MDP setting, each step flips a coin to decide which table to update. On heads the update is

Q₁(S,A) ← Q₁(S,A) + α [R + γ Q₂(S′, argmaxₐ Q₁(S′,a)) − Q₁(S,A)],

and on tails the roles of Q₁ and Q₂ are swapped.[^s2] Because only one table changes per step, double learning doubles memory but adds no computation per step; the behaviour policy can act ε-greedily on both estimates, for example on Q₁ + Q₂.[^s2] In Example 6.7 Double Q-learning was essentially unaffected by the bias, and the same idea yields double versions of Sarsa and Expected Sarsa.[^s2]

## Deep and actor-critic extensions

Van Hasselt, Guez and Silver (AAAI 2016) found that DQN overestimated values in all 49 Atari 2600 games they tested, to varying degrees, and that in games such as Asterix and Wizard of Wor rising estimates coincided with falling scores.[^s3] Their **Double DQN** reuses DQN's existing target network as the second estimator: the online network selects argmaxₐ Q(S′,a; θ) and the target network θ⁻ evaluates it, so no extra networks or parameters are needed.[^s3] In the paper's no-op evaluation, median human-normalized score rose from 93.5% for DQN to 114.7% for Double DQN; under human starts it rose from 47.5% to 88.4%, and to 116.7% with tuning (figures as reported in 2015–2016).[^s3] The same paper derives a lower bound showing that, with estimation errors present, the max over estimates must exceed the true optimal value by a margin that shrinks as the number of actions grows, whereas Double Q-learning's corresponding lower bound on absolute error is zero.[^s3]

Fujimoto, van Hoof and Meger (ICML 2018) showed that overestimation also afflicts actor-critic methods such as DDPG, but that Double DQN-style decoupling helps little there because the slowly changing policy leaves the online and target critics too similar to be independent.[^s4] Their **clipped double Q-learning** trains two critics and uses the minimum of the two in the target, accepting some underestimation on the grounds that undervalued actions are avoided by the policy and so do not propagate, unlike overvalued ones.[^s4] It is one of three components of TD3, alongside delayed policy updates and target policy smoothing.[^s4]

## Limitations and open questions

Double Q-learning trades one bias for another: its estimator can be pessimistic, and the clipped variant deliberately leans towards underestimation.[^s1][^s4] It needs two estimates and, in the tabular form, splits experience between them so each table sees roughly half the updates.[^s2] With function approximation, the two estimates are only as independent as the networks are; that weakness motivated the clipped minimum in actor-critic methods.[^s4]

## Connections

Double Q-learning **extends** Q-learning and sits within **temporal-difference learning**, using the same bootstrapped off-policy update over a **Markov decision process** but with decoupled selection and evaluation.[^s1][^s2] It was **created by** Hado van Hasselt and directly **mitigates** maximization bias.[^s1][^s2] It is related to **SARSA**, whose double variant Sutton and Barto describe, and to the **exploration–exploitation** trade-off, since the bias interacts with ε-greedy behaviour.[^s2] Its deep form, Double DQN, is a standard refinement of the **deep Q-network**.[^s3] In **actor-critic** methods its clipped form **enables** TD3,[^s4] and it links to **soft actor-critic** as a neighbouring off-policy actor-critic method that trains critics with Q-learning-style targets.

## Sources

[^s1]: van Hasselt, "Double Q-learning", NIPS 2010. https://papers.nips.cc/paper/3964-double-q-learning (accessed 2026-11-19)
[^s2]: Sutton and Barto, *Reinforcement Learning: An Introduction*, 2nd ed., MIT Press 2018, section 6.7. https://people.engr.tamu.edu/guni/csce421/files/RLbook2018.pdf (accessed 2026-11-19)
[^s3]: van Hasselt, Guez and Silver, "Deep Reinforcement Learning with Double Q-learning", AAAI 2016 (arXiv 1509.06461). https://ar5iv.labs.arxiv.org/html/1509.06461 (accessed 2026-11-19)
[^s4]: Fujimoto, van Hoof and Meger, "Addressing Function Approximation Error in Actor-Critic Methods", ICML 2018 (arXiv 1802.09477). https://www.arxiv.org/pdf/1802.09477 (accessed 2026-11-19)
