---
id: kt:deep-q-network
type: Algorithm
title: "Deep Q-network: human-level control through deep reinforcement learning"
aliases: [DQN, deep Q-network, deep Q-learning, Nature DQN]
domain: reinforcement-learning
summary: >-
  DeepMind's deep Q-network (DQN) approximates the Q-learning action-value function with a convolutional
  network trained from raw pixels, stabilised by experience replay and a periodically updated target
  network; it was the first agent to learn dozens of Atari 2600 games with one architecture and one set
  of hyperparameters.
maturity: established
broader: [kt:reinforcement-learning, kt:q-learning]
related: [kt:double-q-learning, kt:convolutional-neural-network, kt:exploration-exploitation, kt:actor-critic]
relations:
  - {predicate: basedOn, object: kt:q-learning}
  - {predicate: introducedIn, object: kt:playing-atari-with-deep-reinforcement-learning}
  - {predicate: createdBy, object: kt:google-deepmind}
  - {predicate: dependsOn, object: kt:markov-decision-process}
  - {predicate: evaluatedOn, object: kt:arcade-learning-environment}
sources:
  - id: s1
    title: "Human-level control through deep reinforcement learning"
    publisher: Nature 518, 529-533, 2015 (Mnih et al.), reading copy hosted by Harvard Neuro 230
    url: https://klab.tch.harvard.edu/academia/classes/Neuro230/ReadingAssignments/MnihEtAlHassibis15NatureControlDeepRL.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "Playing Atari with Deep Reinforcement Learning"
    publisher: arXiv:1312.5602 (Mnih et al., DeepMind, 2013)
    url: https://arxiv.org/abs/1312.5602
    type: primary
    accessed: 2026-11-11
  - id: s3
    title: "From Pixels to Actions: Human-level control through Deep Reinforcement Learning"
    publisher: Google Research Blog (Kumaran and Hassabis, 2015)
    url: https://research.google/blog/from-pixels-to-actions-human-level-control-through-deep-reinforcement-learning/
    type: lab-research
    accessed: 2026-11-11
  - id: s4
    title: "Deep Reinforcement Learning with Double Q-Learning"
    publisher: AAAI 2016, pp. 2094-2100 (van Hasselt, Guez and Silver), via ML Anthology
    url: https://mlanthology.org/aaai/2016/vanhasselt2016aaai-deep
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "Rainbow: Combining Improvements in Deep Reinforcement Learning"
    publisher: AAAI 2018, pp. 3215-3222 (Hessel et al.), via ML Anthology
    url: https://mlanthology.org/aaai/2018/hessel2018aaai-rainbow
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s6
    title: "The Deep Q-Learning Algorithm"
    publisher: Hugging Face Deep RL Course, Unit 3
    url: https://huggingface.co/learn/deep-rl-course/unit3/deep-q-algorithm
    type: official-docs
    accessed: 2026-11-11
created: 2026-11-11
---

# Deep Q-network: human-level control through deep reinforcement learning

The **deep Q-network (DQN)** is a value-based deep reinforcement learning agent developed at DeepMind. It replaces the lookup table of classic Q-learning with a convolutional neural network that maps raw screen pixels to an estimated action value for every available action.[^s1] A first version appeared as an arXiv preprint in December 2013: trained on seven Atari 2600 games with no per-game changes to architecture or algorithm, it beat earlier approaches on six and a human expert on three.[^s2] The full system was published in *Nature* in February 2015, where one architecture with one hyperparameter setting was run on 49 games.[^s1]

## How it works

DQN learns an action-value function Q(s, a; θ) by regressing it toward a bootstrapped target, y = r + γ · max over a′ of Q(s′, a′; θ⁻), using a squared-error loss whose error term is clipped to the range −1 to 1.[^s1] Training alternates between two phases: the agent acts and stores transitions, then samples a small random batch of stored transitions and takes a gradient step.[^s6]

Two additions made this stable enough to work with a deep network:

- **Experience replay.** Transitions go into a memory (the 2015 paper kept the most recent one million frames) and are sampled uniformly, so each experience can be reused and consecutive, correlated samples are broken up.[^s1][^s6]
- **Target network.** The target uses a separate parameter copy θ⁻ that is frozen and refreshed from the online network only every C steps, so the regression target does not shift after every update.[^s1][^s6]

The *Nature* network took the four most recent frames, converted to luminance and rescaled to 84×84, as input; it applied three convolutional layers (32 8×8, 64 4×4 and 64 3×3 filters) and a 512-unit fully connected layer, then a linear output with one value per action, so all action values come from a single forward pass.[^s1] Other reported settings include minibatches of 32 with RMSProp, a discount of 0.99, ε-greedy exploration annealed from 1.0 to 0.1 over the first million frames, and 50 million training frames per game. Rewards were clipped to −1, 0 or +1 during training so one learning rate could serve games with very different score scales.[^s1]

## Results and limitations

DeepMind reported that DQN outperformed the best prior reinforcement learning methods on 43 of 49 games and exceeded 75% of a professional human tester's score on 29 of them.[^s1] Its Google blog post highlighted Breakout, where the agent learned to tunnel through one side of the wall, and stated that removing experience replay severely degraded performance; the authors likened replay to the hippocampus reactivating recent experience during rest.[^s3] The paper's ablations also found that removing the target network or the convolutional architecture hurt results.[^s1]

The method has well-known weaknesses. The authors themselves noted that games needing temporally extended planning, such as Montezuma's Revenge, remained a major challenge.[^s1] Taking a max over noisy estimates biases values upward: van Hasselt, Guez and Silver (AAAI 2016) found substantial overestimation in some Atari games and proposed Double DQN, which reduced it and scored much better on several games.[^s4] DQN is also restricted to discrete action sets, because acting requires a max over all actions, and it is data-hungry, needing tens of millions of frames per game.[^s1]

## Legacy

DQN became the base for a family of extensions. The Rainbow agent (Hessel et al., AAAI 2018) combined six independent DQN improvements and, according to its authors, reached state-of-the-art Atari performance in both data efficiency and final score, with ablations measuring each component's contribution.[^s5] Its two stabilising devices, replay buffers and target networks, are now standard teaching material in deep RL courses.[^s6]

## Connections

DQN is a form of reinforcement learning and is `basedOn` tabular Q-learning, inheriting its off-policy temporal-difference update and its assumption of a Markov decision process.[^s1][^s6] It was `introducedIn` the 2013 Atari preprint[^s2] and `createdBy` DeepMind, now Google DeepMind.[^s3] Its pixel encoder is a convolutional neural network, and its ε-greedy behaviour is a simple answer to the exploration–exploitation dilemma.[^s1] It was `evaluatedOn` Atari 2600 games from the Arcade Learning Environment.[^s2] Its overestimation bias was addressed by carrying Double Q-learning over to the deep setting as Double DQN.[^s4] It is also linked to actor-critic methods, the main family that learns a policy directly rather than deriving it from action values.

## Sources
[^s1]: Mnih et al., "Human-level control through deep reinforcement learning", *Nature* 518, 529–533 (2015). https://klab.tch.harvard.edu/academia/classes/Neuro230/ReadingAssignments/MnihEtAlHassibis15NatureControlDeepRL.pdf (accessed 2026-11-11)
[^s2]: Mnih et al., "Playing Atari with Deep Reinforcement Learning", arXiv:1312.5602 (2013). https://arxiv.org/abs/1312.5602 (accessed 2026-11-11)
[^s3]: Kumaran and Hassabis, "From Pixels to Actions: Human-level control through Deep Reinforcement Learning", Google Research Blog (2015). https://research.google/blog/from-pixels-to-actions-human-level-control-through-deep-reinforcement-learning/ (accessed 2026-11-11)
[^s4]: van Hasselt, Guez and Silver, "Deep Reinforcement Learning with Double Q-Learning", AAAI 2016. https://mlanthology.org/aaai/2016/vanhasselt2016aaai-deep (accessed 2026-11-11)
[^s5]: Hessel et al., "Rainbow: Combining Improvements in Deep Reinforcement Learning", AAAI 2018. https://mlanthology.org/aaai/2018/hessel2018aaai-rainbow (accessed 2026-11-11)
[^s6]: Hugging Face, "The Deep Q-Learning Algorithm", Deep RL Course Unit 3. https://huggingface.co/learn/deep-rl-course/unit3/deep-q-algorithm (accessed 2026-11-11)
