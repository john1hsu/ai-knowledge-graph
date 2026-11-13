---
id: kt:alphazero
type: Algorithm
title: AlphaZero
aliases: [Alpha Zero]
domain: reinforcement-learning
summary: >-
  DeepMind's general self-play reinforcement learning algorithm (2017-2018) that, given only the rules,
  learned chess, shogi and Go from random play using one deep neural network to guide Monte Carlo tree
  search, and defeated the strongest existing program in each game.
maturity: established
broader: [kt:reinforcement-learning, kt:deep-learning]
related: [kt:alphago, kt:exploration-exploitation, kt:deep-blue, kt:mechanistic-interpretability, kt:tpu]
relations:
  - {predicate: introducedIn, object: kt:mastering-chess-and-shogi-by-self-play-with-a-general-reinforcement-learning-algorithm}
  - {predicate: createdBy, object: kt:google-deepmind}
  - {predicate: extends, object: kt:alphago-zero}
  - {predicate: basedOn, object: kt:monte-carlo-tree-search}
  - {predicate: trainedWith, object: kt:self-play}
  - {predicate: supersededBy, object: kt:muzero}
sources:
  - id: s1
    title: "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm"
    publisher: arXiv:1712.01815 (Silver et al., Google DeepMind), December 2017
    url: https://arxiv.org/abs/1712.01815v1
    type: primary
    accessed: 2026-11-13
  - id: s2
    title: "A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play"
    publisher: Science 362(6419), 1140-1144, 2018 (Silver et al.); full text hosted on a UNAM IIMAS course page
    url: https://turing.iimas.unam.mx/~luis/cursos/IA2022-1/lecturas/AlphaZero.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "AlphaZero: Shedding new light on chess, shogi, and Go"
    publisher: Google DeepMind blog, 6 December 2018
    url: https://deepmind.google/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/
    type: lab-research
    accessed: 2026-11-13
  - id: s4
    title: "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model"
    publisher: arXiv:1911.08265 (Schrittwieser et al., DeepMind), v2 February 2020
    url: https://arxiv.org/abs/1911.08265v2
    type: primary
    accessed: 2026-11-13
  - id: s5
    title: "Acquisition of chess knowledge in AlphaZero"
    publisher: PNAS 119(47), e2206625119, 2022 (McGrath et al.), PubMed Central
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9704706
    type: peer-reviewed
    accessed: 2026-11-13
created: 2026-11-13
---

# AlphaZero

AlphaZero is a reinforcement learning algorithm from DeepMind that learns to play two-player board games purely by playing against itself, starting from random moves and given nothing but the rules. A single algorithm, with essentially the same settings, reached superhuman strength in chess, shogi (Japanese chess) and Go.[^s1][^s2] It was first described in a December 2017 arXiv preprint by David Silver, Thomas Hubert, Julian Schrittwieser and colleagues, and a fuller evaluation was published in *Science* in December 2018.[^s1][^s2] Its significance was less the games themselves than the demonstration that one general learning-plus-search method could replace decades of hand-tuned, game-specific engineering.[^s1]

## How it works

AlphaZero uses one deep neural network, $(\mathbf{p}, v) = f_\theta(s)$, that takes a board position $s$ and outputs a probability distribution $\mathbf{p}$ over moves (the policy) and a scalar $v$ estimating the expected game outcome (the value).[^s2] In the published version the network is a residual convolutional network with separate policy and value heads on a shared torso; the chess network studied later had 20 residual blocks.[^s2][^s5]

Instead of the alpha-beta search used by classical engines, AlphaZero runs a general-purpose Monte Carlo tree search (MCTS). Each simulation descends the tree favouring moves with high prior probability, high estimated value and few prior visits, then expands a leaf and evaluates it with the network rather than by playing a random game to the end.[^s2] The visit counts at the root form an improved policy $\boldsymbol{\pi}$, from which the move is chosen.[^s2]

Training alternates self-play and learning. Games are generated with MCTS using the latest network; at the end of each game every position is labelled with the final result $z$.[^s2] The network parameters are then updated by gradient descent on

$$l = (z - v)^2 - \boldsymbol{\pi}^\top \log \mathbf{p} + c\lVert\theta\rVert^2,$$

so the value head regresses toward actual outcomes and the policy head imitates the search's improved move distribution, with L2 regularisation.[^s2] In effect, the search proposes stronger moves than the raw network and the network is trained to reproduce them, so each round of self-play starts from a better player.[^s2]

## What changed from AlphaGo Zero

AlphaZero generalised the earlier AlphaGo Zero, which learned only Go. The *Science* paper lists the main changes: it predicts expected outcome rather than win probability because chess and shogi allow draws; it drops data augmentation by board symmetries, since chess and shogi are not symmetric; it updates one network continually instead of gating each new network on a 55% win rate against the previous best; and it reuses the same architecture and hyperparameters across all three games, apart from exploration noise and the learning-rate schedule.[^s2]

## Results

As reported by DeepMind in the 2018 paper, each game was trained for 700,000 steps with mini-batches of 4,096 positions, using 5,000 first-generation TPUs to generate self-play games and 16 second-generation TPUs to train. Training took about 9 hours for chess, 12 hours for shogi and 13 days for Go.[^s2][^s3] In matches at 3 hours per game plus 15 seconds per move, AlphaZero beat the 2016 TCEC champion Stockfish (155 wins and 6 losses in 1,000 games), scored 91.2% against the 2017 CSA champion Elmo in shogi, and won 61% of games against AlphaGo Zero.[^s2][^s3] It searched about 60,000 positions per second in chess against roughly 60 million for Stockfish, relying on a much stronger evaluation to compensate for a far smaller search.[^s2][^s3]

## Limitations and critiques

The comparisons are not like-for-like. The authors themselves note that AlphaZero ran on TPUs while Stockfish and Elmo ran on CPUs, that frequent draws compress chess ratings, and that unbalanced opening positions inflated losses for both sides.[^s2] More fundamentally, AlphaZero needs a perfect simulator: it must be given the rules to search ahead, which restricts it to domains with known dynamics.[^s4]

Its play also raised interpretability questions. A 2022 *PNAS* study used sparse linear probes on each residual block and found that many human chess concepts, such as material, mobility and king safety, can be decoded from the network, emerging at different points in training; the authors stress that probing shows correlation, not causation.[^s5]

## In practice

DeepMind described AlphaZero's chess as dynamic and willing to sacrifice material for long-term activity, and its games were studied by grandmasters and used in commentary on the 2018 World Chess Championship.[^s3] The approach was extended by MuZero (preprint 2019), which plans with a learned model instead of the rules and matched AlphaZero in Go, chess and shogi while also handling Atari games.[^s4]

## Connections

AlphaZero is a landmark of `kt:reinforcement-learning` and `kt:deep-learning`. It **extends** `kt:alphago-zero`, the rules-only successor of `kt:alphago`, and was **introduced in** the 2017 preprint by `kt:google-deepmind`.[^s1][^s2] It is **based on** `kt:monte-carlo-tree-search` and **trained with** `kt:self-play`, where search-guided move sampling handles `kt:exploration-exploitation` through visit counts and exploration noise.[^s2] Training ran on `kt:tpu` hardware.[^s2] It contrasts with the brute-force, hand-crafted approach of `kt:deep-blue`-style engines, is a case study for `kt:mechanistic-interpretability`, and was **superseded by** `kt:muzero`, which learns its own model of the environment.[^s4][^s5]

## Sources
[^s1]: Silver et al., "Mastering Chess and Shogi by Self-Play with a General Reinforcement Learning Algorithm", arXiv:1712.01815, 2017. https://arxiv.org/abs/1712.01815v1 (accessed 2026-11-13)
[^s2]: Silver et al., "A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play", Science 362(6419), 2018. https://turing.iimas.unam.mx/~luis/cursos/IA2022-1/lecturas/AlphaZero.pdf (accessed 2026-11-13)
[^s3]: Google DeepMind, "AlphaZero: Shedding new light on chess, shogi, and Go", 2018. https://deepmind.google/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/ (accessed 2026-11-13)
[^s4]: Schrittwieser et al., "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model", arXiv:1911.08265, 2019/2020. https://arxiv.org/abs/1911.08265v2 (accessed 2026-11-13)
[^s5]: McGrath et al., "Acquisition of chess knowledge in AlphaZero", PNAS 119(47), 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9704706 (accessed 2026-11-13)
