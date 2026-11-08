---
id: kt:q-learning
type: Algorithm
title: Q-learning
aliases: [Watkins Q-learning, tabular Q-learning]
domain: reinforcement-learning
summary: >-
  A model-free, off-policy, value-based reinforcement learning algorithm that learns the expected return
  of taking each action in each state (the action-value or Q-function) by temporal-difference updates
  toward the reward plus the discounted best next-state value.
maturity: foundational
broader: [kt:reinforcement-learning, kt:temporal-difference-learning]
related: [kt:markov-decision-process, kt:actor-critic, kt:policy-gradient, kt:exploration-exploitation]
relations:
  - {predicate: createdBy, object: kt:christopher-watkins}
  - {predicate: dependsOn, object: kt:markov-decision-process}
  - {predicate: enables, object: kt:deep-q-network}
  - {predicate: enables, object: kt:double-q-learning}
  - {predicate: contrastsWith, object: kt:sarsa}
  - {predicate: alternativeTo, object: kt:actor-critic}
sources:
  - id: s1
    title: "Technical Note: Q-Learning"
    publisher: Machine Learning 8:279-292, 1992 (Watkins and Dayan), via ML Anthology
    url: https://mlanthology.org/mlj/1992/watkins1992mlj-technical
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s2
    title: "An Introduction to Q-Learning Part 2/2"
    publisher: Hugging Face Deep RL Course, Unit 2 (Simonini, 2022)
    url: https://huggingface.co/blog/deep-rl-q-part2
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Double Q-learning"
    publisher: Advances in Neural Information Processing Systems 23 (NIPS 2010) (van Hasselt)
    url: https://papers.nips.cc/paper/3964-double-q-learning
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s4
    title: "From Pixels to Actions: Human-level control through Deep Reinforcement Learning"
    publisher: Google Research blog (Kumaran and Hassabis, Google DeepMind), 2015
    url: https://research.google/blog/from-pixels-to-actions-human-level-control-through-deep-reinforcement-learning/
    type: lab-research
    accessed: 2026-11-08
  - id: s5
    title: "Deep Reinforcement Learning with Double Q-learning"
    publisher: van Hasselt, Guez and Silver (Google DeepMind), AAAI 2016; authors' arXiv version
    url: https://arxiv.org/pdf/1509.06461
    type: primary
    accessed: 2026-11-08
created: 2026-11-08
---

# Q-learning

Q-learning is one of the founding algorithms of reinforcement learning. An agent using it learns a table (or, later, a function approximator) of **Q-values**: for each state s and action a, Q(s, a) estimates the long-run discounted reward of taking a in s and behaving optimally afterwards. Once those values are accurate, acting optimally is trivial, because the best action in any state is simply the one with the highest Q-value.[^s2] The method is *model-free*: it never needs to know the environment's transition probabilities, only to observe the transitions and rewards it experiences.[^s1]

## Origin

Q-learning is credited to Christopher Watkins, and its standard citation is the 1992 *Machine Learning* technical note by Watkins and Peter Dayan (volume 8, pages 279–292). That note gave a detailed proof that Q-learning converges to the optimal action-values with probability 1, provided every action is sampled repeatedly in every state and the action-values are stored discretely. It also sketched extensions to non-discounted absorbing environments and to updating many Q-values per step.[^s1]

## How it works

Q-learning is a temporal-difference (TD) method: rather than waiting for an episode to finish, it updates after every single step. Training typically starts from a Q-table filled with arbitrary values, often zeros.[^s2] After taking action A_t in state S_t, receiving reward R_{t+1} and landing in S_{t+1}, the agent applies

Q(S_t, A_t) ← Q(S_t, A_t) + α [ R_{t+1} + γ · max_a Q(S_{t+1}, a) − Q(S_t, A_t) ]

where α is the learning rate and γ the discount factor. The bracketed quantity is the TD error; the term R + γ·max Q is the *TD target*, and building it from the agent's own current estimates is called bootstrapping.[^s2] The Hugging Face course works a small maze example with α = 0.1 and γ = 0.99.[^s2]

Exploration is usually handled with an **ε-greedy** behaviour policy: with probability 1 − ε take the highest-valued action, otherwise a random one, with ε decayed over training as the table becomes trustworthy.[^s2] Crucially, the action actually taken (ε-greedy) and the action assumed in the target (the greedy max) come from different policies. That makes Q-learning **off-policy**. Its on-policy sibling SARSA instead plugs the value of the next action the ε-greedy policy actually chooses into the update.[^s2]

## Limitations

The max operator is a source of systematic error. Hado van Hasselt showed at NIPS 2010 that, in stochastic environments, Q-learning tends to overestimate action values because the maximum of noisy estimates is a positively biased stand-in for the maximum of the true expected values. His **Double Q-learning** keeps two estimators, using one to pick the best action and the other to value it; the double estimator can underestimate instead, and the resulting off-policy algorithm still converges to the optimal policy while doing better where overestimation hurts plain Q-learning.[^s3]

Tabular Q-learning also does not scale: the convergence guarantee assumes discrete, repeatedly visited state-action pairs,[^s1] which is impossible when states are raw images. Replacing the table with a neural network breaks those guarantees and introduces instability, which is what the deep-RL variants below set out to tame.[^s5]

## In practice

The best-known descendant is DeepMind's **deep Q-network (DQN)**, published in *Nature* in February 2015. A single architecture with fixed hyperparameters learned 49 Atari 2600 games from screen pixels, actions and score alone; DeepMind reported that it beat earlier machine-learning methods on 43 of them and exceeded 75% of a professional human tester's score on more than half.[^s4] Two stabilising tricks made this work. **Experience replay** trains on transitions sampled at random from a stored pool, and DeepMind reported a severe performance drop without it.[^s4] A **target network**, a periodically refreshed frozen copy of the online network, keeps the TD target from shifting every step.[^s5]

Overestimation reappeared at scale: van Hasselt, Guez and Silver (AAAI 2016) found DQN overestimating values across the Atari suite and proposed **Double DQN**, in which the online network selects the next action and the target network evaluates it. They reported a median normalised score of 114.7% versus 93.5% for DQN under their no-op evaluation.[^s5] Tabular Q-learning remains a standard first algorithm in courses and a baseline for small discrete problems.[^s2]

## Connections

Q-learning is a temporal-difference method within reinforcement learning, and it assumes the world can be framed as a Markov decision process (`dependsOn kt:markov-decision-process`).[^s1] Its ε-greedy behaviour is the textbook illustration of the exploration–exploitation trade-off.[^s2] It contrasts with on-policy SARSA (`contrastsWith kt:sarsa`) and is a value-based `alternativeTo` actor-critic and policy-gradient methods, which learn the policy directly.[^s2] It was created by Christopher Watkins (`createdBy`),[^s1] and it `enables` Double Q-learning[^s3] and the deep Q-network.[^s4]

## Sources
[^s1]: Watkins, C. J. C. H. and Dayan, P., "Technical Note: Q-Learning", *Machine Learning* 8:279–292, 1992. https://mlanthology.org/mlj/1992/watkins1992mlj-technical (accessed 2026-11-08)
[^s2]: Simonini, T., "An Introduction to Q-Learning Part 2/2", Hugging Face Deep RL Course, 2022. https://huggingface.co/blog/deep-rl-q-part2 (accessed 2026-11-08)
[^s3]: van Hasselt, H., "Double Q-learning", NIPS 2010. https://papers.nips.cc/paper/3964-double-q-learning (accessed 2026-11-08)
[^s4]: Kumaran, D. and Hassabis, D., "From Pixels to Actions: Human-level control through Deep Reinforcement Learning", Google Research blog, 2015. https://research.google/blog/from-pixels-to-actions-human-level-control-through-deep-reinforcement-learning/ (accessed 2026-11-08)
[^s5]: van Hasselt, H., Guez, A. and Silver, D., "Deep Reinforcement Learning with Double Q-learning", AAAI 2016. https://arxiv.org/pdf/1509.06461 (accessed 2026-11-08)
