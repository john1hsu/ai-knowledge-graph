---
id: kt:reinforcement-learning
type: Field
title: Reinforcement learning
aliases: [RL, learning from rewards, trial-and-error learning]
domain: reinforcement-learning
summary: >-
  The branch of machine learning in which an agent learns a policy for sequential decision-making by
  interacting with an environment and adjusting its behavior to maximize cumulative reward, rather than
  learning from labeled examples.
maturity: foundational
broader: [kt:machine-learning]
related: [kt:markov-decision-process, kt:exploration-exploitation, kt:q-learning, kt:policy-gradient, kt:actor-critic, kt:rlhf]
relations:
  - {predicate: partOf, object: kt:machine-learning}
  - {predicate: contrastsWith, object: kt:supervised-learning}
  - {predicate: hasPart, object: kt:temporal-difference-learning}
  - {predicate: dependsOn, object: kt:markov-decision-process}
  - {predicate: enables, object: kt:deep-q-network}
  - {predicate: enables, object: kt:alphago}
sources:
  - id: s1
    title: "Reinforcement Learning: A Survey"
    publisher: Journal of Artificial Intelligence Research 4:237-285, 1996 (Kaelbling, Littman and Moore)
    url: https://jair.org/index.php/jair/article/view/10166
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s2
    title: "CS234 Lecture 1: Introduction to Reinforcement Learning"
    publisher: Stanford University CS234, Winter 2018 (Emma Brunskill)
    url: https://web.stanford.edu/class/archive/cs/cs234/cs234.1224/CS234Win2018/slides/cs234_2018_l1.pdf
    type: academic
    accessed: 2026-11-09
  - id: s3
    title: "ACM A.M. Turing Award Honors Two Researchers Who Led the Development of Cornerstone AI Technology"
    publisher: Association for Computing Machinery, 2024 A.M. Turing Award announcement (March 2025)
    url: https://awards.acm.org/about/2024-turing
    type: primary
    accessed: 2026-11-09
  - id: s4
    title: "From Pixels to Actions: Human-level control through Deep Reinforcement Learning"
    publisher: Google Research blog (Kumaran and Hassabis, Google DeepMind), 2015
    url: https://research.google/blog/from-pixels-to-actions-human-level-control-through-deep-reinforcement-learning/
    type: lab-research
    accessed: 2026-11-09
  - id: s5
    title: "Mastering the game of Go with deep neural networks and tree search"
    publisher: Nature 529, 2016 (Silver et al.), Google Research publication page
    url: https://research.google/pubs/mastering-the-game-of-go-with-deep-neural-networks-and-tree-search/
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# Reinforcement learning

**Reinforcement learning (RL)** is the part of machine learning concerned with an agent that learns how to behave through trial and error while interacting with a dynamic environment.[^s1] Instead of being shown the correct answer for each input, the agent takes actions, observes what happens, and receives a scalar reward; its goal is to choose actions that maximize the total expected future reward, which can mean sacrificing immediate reward for a larger payoff later.[^s2] The name echoes behavioral psychology, but the computational field differs from it in its details and in how it uses the word "reinforcement."[^s1]

## Origin

Andrew Barto and his PhD student Richard Sutton began framing RL as a general problem in the early 1980s, building on Markov decision processes, and over the following decades published the core ideas, theory and algorithms of the field.[^s3] Their 1998 textbook *Reinforcement Learning: An Introduction* became the standard reference. ACM credits temporal-difference learning as their most important contribution, alongside policy-gradient methods, the use of neural networks to represent learned functions, and agents that combine learning with planning. The two received the 2024 ACM A.M. Turing Award (announced March 2025) for this work.[^s3] A widely cited 1996 survey by Kaelbling, Littman and Moore consolidated the field's computer-science view and identified Markov decision theory as its formal foundation.[^s1]

## How it works

At each discrete time step the agent chooses an action a_t; the environment then returns an observation o_t and a reward r_t. When the current state captures everything relevant about the future (the Markov property) the problem is a Markov decision process; when the true state is hidden it is a partially observable MDP.[^s2] A typical agent is built from up to three components: a **policy** that maps states to actions, a **value function** giving the expected discounted sum of future rewards under that policy, and optionally a **model** that predicts transitions P(s′|s, a) and rewards. A discount factor γ between 0 and 1 sets how much future reward counts relative to immediate reward.[^s2]

These components define the main families of methods. *Model-based* agents learn or are given a model and can plan with it; *model-free* agents learn a value function and/or policy directly from experience. Value-based agents (such as Q-learning) keep an explicit value function and act greedily on it, policy-based agents optimize the policy directly, and actor-critic agents maintain both.[^s2]

## What makes RL distinctive

Stanford's CS234 course frames RL around four intertwined challenges: optimization (finding a very good decision strategy), delayed consequences (actions may pay off only much later, creating a temporal credit-assignment problem), exploration (the agent only sees outcomes of the actions it actually takes), and generalization (large state spaces such as raw images cannot be enumerated).[^s2] Supervised learning sidesteps exploration because correct labels are supplied, unsupervised learning has no reward signal at all, and imitation learning reduces the problem to supervised learning on demonstrations but is limited by the quality and cost of that data.[^s2] The tension between trying new actions and exploiting known good ones, and learning from delayed reward, were already named as central issues in the 1996 survey, together with hierarchy, generalization and hidden state.[^s1]

## In practice

Combining RL with deep neural networks produced several landmark results. DeepMind's DQN, reported in *Nature* in February 2015, learned to play 49 Atari 2600 games from raw pixels and the score alone, using one architecture and one set of hyperparameters; Google reported that it beat earlier machine-learning methods on 43 of the games, and experience replay proved essential to its performance.[^s4] AlphaGo (*Nature*, 2016) trained policy and value networks first by supervised learning on expert human games and then by RL from self-play, combined them with Monte Carlo tree search, and defeated the European Go champion 5–0.[^s5] ACM's award citation also points to RL's role in robotic manipulation, network congestion control, chip design and internet advertising, and to reinforcement learning from human feedback as the second training phase of ChatGPT.[^s3]

RL remains demanding in practice: rewards must be specified by hand and can be gamed, exploration in large spaces is expensive, and many successes depend on cheap simulators or self-play. CS234 lists the question of where rewards come from as an open problem.[^s2]

## Connections

RL is one of the main branches of `kt:machine-learning` and contrasts with `kt:supervised-learning`, which learns from labeled targets rather than reward.[^s2] Its formal foundation is the `kt:markov-decision-process`, and the `kt:exploration-exploitation` trade-off is one of its defining problems.[^s1] `kt:temporal-difference-learning` is a core idea within it, and value-based `kt:q-learning`, `kt:policy-gradient` methods and `kt:actor-critic` hybrids are its main algorithm families.[^s2][^s3] Deep RL systems such as `kt:deep-q-network` and `kt:alphago` are flagship applications,[^s4][^s5] and `kt:rlhf` carries RL into the fine-tuning of large language models.[^s3]

## Sources
[^s1]: Kaelbling, Littman and Moore, "Reinforcement Learning: A Survey", Journal of Artificial Intelligence Research 4:237-285, 1996. https://jair.org/index.php/jair/article/view/10166 (accessed 2026-11-09)
[^s2]: Brunskill, "CS234 Lecture 1: Introduction to Reinforcement Learning", Stanford University, Winter 2018. https://web.stanford.edu/class/archive/cs/cs234/cs234.1224/CS234Win2018/slides/cs234_2018_l1.pdf (accessed 2026-11-09)
[^s3]: ACM, "ACM A.M. Turing Award Honors Two Researchers Who Led the Development of Cornerstone AI Technology" (2024 Turing Award, Barto and Sutton). https://awards.acm.org/about/2024-turing (accessed 2026-11-09)
[^s4]: Kumaran and Hassabis, "From Pixels to Actions: Human-level control through Deep Reinforcement Learning", Google Research blog, 2015. https://research.google/blog/from-pixels-to-actions-human-level-control-through-deep-reinforcement-learning/ (accessed 2026-11-09)
[^s5]: Silver et al., "Mastering the game of Go with deep neural networks and tree search", Nature 529, 2016. https://research.google/pubs/mastering-the-game-of-go-with-deep-neural-networks-and-tree-search/ (accessed 2026-11-09)
