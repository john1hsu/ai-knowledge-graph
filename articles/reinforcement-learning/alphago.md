---
id: kt:alphago
type: Model
title: AlphaGo
aliases: [AlphaGo Fan, AlphaGo Lee]
domain: reinforcement-learning
summary: >-
  DeepMind's Go-playing system that combined deep policy and value networks, trained by supervised
  learning on expert games and then reinforcement learning from self-play, with Monte Carlo tree search;
  in 2015-2016 it became the first program to beat professional human players at full-sized Go.
maturity: historical
broader: [kt:reinforcement-learning, kt:deep-learning]
related: [kt:deep-q-network, kt:supervised-learning, kt:alphazero]
relations:
  - {predicate: introducedIn, object: kt:mastering-the-game-of-go-with-deep-neural-networks-and-tree-search}
  - {predicate: createdBy, object: kt:google-deepmind}
  - {predicate: basedOn, object: kt:monte-carlo-tree-search}
  - {predicate: basedOn, object: kt:convolutional-neural-network}
  - {predicate: trainedWith, object: kt:policy-gradient}
  - {predicate: supersededBy, object: kt:alphago-zero}
sources:
  - id: s1
    title: "Mastering the game of Go with deep neural networks and tree search"
    publisher: Nature 529, 484-503, 2016 (Silver et al.), Google Research publication page
    url: https://research.google/pubs/mastering-the-game-of-go-with-deep-neural-networks-and-tree-search/
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s2
    title: "Mastering the game of Go with deep neural networks and tree search (full text)"
    publisher: Silver et al., Nature 2016; paper PDF hosted by the Bau Lab, Northeastern University
    url: https://papers.baulab.info/papers/Silver-2016.pdf
    type: primary
    accessed: 2026-11-10
  - id: s3
    title: "Mastering the game of Go without human knowledge"
    publisher: Nature 550(7676), 354-359, 2017 (Silver et al.), UCL Discovery record
    url: https://discovery.ucl.ac.uk/id/eprint/10045895/
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s4
    title: "A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play"
    publisher: Science 362(6419), 1140-1144, 2018 (Silver et al.), UCL Discovery record
    url: https://discovery.ucl.ac.uk/id/eprint/10069050/
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s5
    title: "Computer takes first game in match against Go world champion"
    publisher: Science News (Meghan Rosen), 9 March 2016
    url: https://www.sciencenews.org/?p=39575
    type: news
    accessed: 2026-11-10
  - id: s6
    title: "AlphaGo wins final game after neck-and-neck race"
    publisher: The Korea Times (Park Si-soo and Lee Han-soo), 15 March 2016
    url: https://www.koreatimes.co.kr/business/tech-science/20160315/alphago-wins-final-game-after-neck-and-neck-race
    type: news
    accessed: 2026-11-10
created: 2026-11-10
---

# AlphaGo

AlphaGo is a computer Go program built by DeepMind (now Google DeepMind) and described by David Silver, Aja Huang, Demis Hassabis and colleagues in a 2016 *Nature* paper.[^s1] Go had long been regarded as the hardest of the classic board games for AI, because its search space is enormous and because positions and moves are hard to evaluate. AlphaGo addressed both problems with deep neural networks: "policy networks" that propose moves and "value networks" that judge positions, combined with Monte Carlo tree search (MCTS).[^s1] According to the paper, it was the first program to defeat a human professional on a full-sized 19×19 board, a result the authors said had been expected to be at least a decade away.[^s1]

## How it works

AlphaGo's training pipeline has several stages.[^s2] First, a 13-layer convolutional supervised-learning (SL) policy network was trained to predict expert moves from about 29.4 million positions drawn from 160,000 games on the KGS Go server. It reached 57.0% test accuracy, against a previous state of the art of 44.4%.[^s2] A much weaker but far faster linear "rollout" policy, trained on Tygem game positions, could pick a move in about 2 microseconds versus roughly 3 milliseconds for the deep network, which made it usable for rapid playouts.[^s2]

Second, a reinforcement-learning (RL) policy network was initialised from the SL network and improved by policy-gradient updates from games of self-play against randomly chosen earlier versions of itself. It won more than 80% of games against the SL network and, with no search at all, 85% against the open-source MCTS program Pachi.[^s2] Third, a value network was trained by regression to predict the eventual winner from a position, using over 30 million positions each sampled from a separate self-play game, which reduced the overfitting that came from using correlated positions from the same game.[^s2]

At play time, MCTS uses the SL policy network as a prior to steer exploration and scores each leaf by mixing the value network's estimate with the outcome of a fast rollout; the paper's best setting weighted the two equally (λ = 0.5).[^s2] The search ran asynchronously, with simulations on CPUs and network evaluations on GPUs. The single-machine version used 48 CPUs and 8 GPUs, and the distributed version used 1,202 CPUs and 176 GPUs, with estimated Elo ratings of 2890 and 3140 respectively in the paper's internal tournament.[^s2]

## Milestones

The 2016 paper reported a 99.8% win rate against other Go programs and a 5-0 formal match win over European champion Fan Hui, played 5-9 October 2015.[^s1][^s2] In March 2016 an upgraded AlphaGo played world-class professional Lee Sedol in a five-game match for a US$1 million prize; it won the opening game,[^s5] and took the series 4-1 in Seoul, with DeepMind saying it would donate the prize to charity.[^s6] The match was widely covered as a landmark for AI.[^s5][^s6]

## Limitations and successors

AlphaGo depended on human expert data to bootstrap its policy, on hand-crafted input features and a separate rollout policy, and on large amounts of compute at play time.[^s2] Its successor AlphaGo Zero, published in 2017, dropped human games entirely: it learned only from self-play, starting from the rules, with a single network that predicts both moves and the winner, and it beat the version of AlphaGo that had defeated a world champion by 100 games to 0.[^s3] AlphaZero (*Science*, 2018) generalised that self-play algorithm, from random play and no domain knowledge beyond the rules, to chess and shogi as well as Go, defeating a world-champion program in each of chess and shogi.[^s4]

## Connections

AlphaGo is a flagship application of `kt:reinforcement-learning` and of `kt:deep-learning`: its networks are `kt:convolutional-neural-network`s, its RL stage is trained with `kt:policy-gradient` updates, and its move-selection procedure is built on `kt:monte-carlo-tree-search`.[^s2] It was introduced in `kt:mastering-the-game-of-go-with-deep-neural-networks-and-tree-search` and created by `kt:google-deepmind`.[^s1] Its first training stage is ordinary `kt:supervised-learning` on expert moves, which distinguishes it from purely self-taught systems.[^s2] It was superseded by `kt:alphago-zero` and generalised by `kt:alphazero`.[^s3][^s4] Alongside `kt:deep-q-network`, another DeepMind system, it is one of the best-known demonstrations of deep RL on games.[^s1]

## Sources
[^s1]: Silver et al., "Mastering the game of Go with deep neural networks and tree search", Nature 529, 2016 (Google Research publication page). https://research.google/pubs/mastering-the-game-of-go-with-deep-neural-networks-and-tree-search/ (accessed 2026-11-10)
[^s2]: Silver et al., "Mastering the game of Go with deep neural networks and tree search", Nature 2016, full-text PDF. https://papers.baulab.info/papers/Silver-2016.pdf (accessed 2026-11-10)
[^s3]: Silver et al., "Mastering the game of Go without human knowledge", Nature 550, 354-359, 2017. https://discovery.ucl.ac.uk/id/eprint/10045895/ (accessed 2026-11-10)
[^s4]: Silver et al., "A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play", Science 362, 1140-1144, 2018. https://discovery.ucl.ac.uk/id/eprint/10069050/ (accessed 2026-11-10)
[^s5]: M. Rosen, "Computer takes first game in match against Go world champion", Science News, 9 March 2016. https://www.sciencenews.org/?p=39575 (accessed 2026-11-10)
[^s6]: Park Si-soo and Lee Han-soo, "AlphaGo wins final game after neck-and-neck race", The Korea Times, 15 March 2016. https://www.koreatimes.co.kr/business/tech-science/20160315/alphago-wins-final-game-after-neck-and-neck-race (accessed 2026-11-10)
