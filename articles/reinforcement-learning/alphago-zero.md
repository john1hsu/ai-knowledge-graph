---
id: kt:alphago-zero
type: Model
title: AlphaGo Zero
aliases: [AlphaGo Zero (2017)]
domain: reinforcement-learning
summary: >-
  DeepMind's 2017 Go program that learned purely by self-play reinforcement learning from random play,
  with no human game records or hand-crafted features, using a single residual network with policy and
  value heads to guide Monte Carlo tree search; it beat the earlier AlphaGo that defeated Lee Sedol 100-0.
maturity: historical
broader: [kt:reinforcement-learning, kt:deep-learning]
related: [kt:alphago, kt:residual-connection, kt:supervised-learning, kt:exploration-exploitation, kt:inductive-bias]
relations:
  - {predicate: introducedIn, object: kt:mastering-the-game-of-go-without-human-knowledge}
  - {predicate: createdBy, object: kt:google-deepmind}
  - {predicate: basedOn, object: kt:monte-carlo-tree-search}
  - {predicate: trainedWith, object: kt:self-play}
  - {predicate: supersedes, object: kt:alphago}
  - {predicate: followedBy, object: kt:alphazero}
sources:
  - id: s1
    title: "Mastering the game of Go without human knowledge"
    publisher: Nature 550(7676), 354-359, October 2017 (Silver et al., DeepMind), DOI 10.1038/nature24270; RePEc/IDEAS bibliographic record
    url: https://ideas.repec.org/a/nat/nature/v550y2017i7676d10.1038_nature24270.html
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Mastering the game of Go without human knowledge (full text)"
    publisher: Silver et al., Nature 2017; manuscript text hosted on a University of Athens course page (eClass DI437)
    url: https://eclass.uoa.gr/modules/document/file.php/DI437/agz_unformatted_nature.pdf
    type: primary
    accessed: 2026-11-16
  - id: s3
    title: "AlphaGo Zero: Starting from scratch"
    publisher: Google DeepMind blog (David Silver and Demis Hassabis), 18 October 2017
    url: https://deepmind.google/blog/alphago-zero-starting-from-scratch/
    type: lab-research
    accessed: 2026-11-16
  - id: s4
    title: "News & Views commentary on AlphaGo Zero (Singh; Okun and Jackson)"
    publisher: Satinder Singh (University of Michigan), Andy Okun and Andrew Jackson, Nature 550, 336-337, 19 October 2017; hosted on Singh's university page
    url: https://web.eecs.umich.edu/~baveja/Papers/NatureNV2017.pdf
    type: academic
    accessed: 2026-11-16
  - id: s5
    title: "Innateness, AlphaZero, and Artificial Intelligence"
    publisher: arXiv:1801.05667 (Gary Marcus), January 2018
    url: https://arxiv.org/abs/1801.05667
    type: preprint
    accessed: 2026-11-16
created: 2026-11-16
---

# AlphaGo Zero

AlphaGo Zero is a Go-playing system from DeepMind that reached superhuman strength by reinforcement learning from self-play alone, starting from random moves and given only the rules of the game.[^s1][^s2] It was described by David Silver, Julian Schrittwieser and 15 DeepMind co-authors in *Nature* in October 2017 under the title "Mastering the game of Go without human knowledge".[^s1][^s3] Unlike the original AlphaGo, it used no records of human expert games during training, and after about three days of self-play it beat the version of AlphaGo that had defeated Lee Sedol by 100 games to 0.[^s1][^s3]

## What changed from AlphaGo

DeepMind summarised the break with its predecessors in three points. The input is just the black and white stones (plus recent history), not a set of hand-engineered Go features; one network replaces the separate policy and value networks; and positions are evaluated by the network alone, with no fast random rollouts.[^s3] The earlier AlphaGo had also relied on several networks and multiple training data sources, including supervised learning on human games, which Satinder Singh's *Nature* commentary contrasted with Zero's single learning signal.[^s4]

## How it works

The network $(\mathbf{p}, v) = f_\theta(s)$ reads a 19×19×17 stack of binary planes (eight past positions for each player plus a colour-to-move plane). A convolutional block is followed by a tower of residual blocks, giving 20-block and 40-block versions, and the tower feeds a policy head over 362 moves (361 points plus pass) and a tanh value head estimating the outcome.[^s2]

Each move is chosen by Monte Carlo tree search with 1,600 simulations (about 0.4 seconds). Edges store a prior $P$, visit count $N$ and mean value $Q$; selection favours high $Q + U$ with $U \propto P\sqrt{\sum N}/(1+N)$, and every leaf is expanded and scored by the network rather than by a rollout. Dirichlet noise at the root and a temperature on early moves keep self-play diverse.[^s2]

Training loops between self-play and learning.[^s2] Each finished game labels its positions with the result $z$ and the search's visit-count distribution $\boldsymbol{\pi}$, and the network is trained on

$$l = (z - v)^2 - \boldsymbol{\pi}^\top \log \mathbf{p} + c\lVert\theta\rVert^2,$$

so the policy imitates the stronger search and the value predicts the winner.[^s2] Search therefore acts as a policy-improvement operator, and a new checkpoint replaced the best player only if it won more than 55% of 400 evaluation games.[^s2]

## Results

The main run used 4.9 million self-play games and 700,000 mini-batches of 2,048 positions over roughly three days; a 40-block run trained for about 40 days on 29 million games.[^s2] According to DeepMind, it needed a single machine with 4 TPUs at play time, against 48 TPUs for the Lee Sedol version.[^s3][^s4] On the paper's Elo scale the 40-block system reached 5,185, against 4,858 for AlphaGo Master, 3,739 for AlphaGo Lee and 3,144 for AlphaGo Fan, and it beat Master 89-11 in a 100-game match; the raw network without search rated 3,055.[^s2] The authors caution that these self-play Elo figures can be inflated unless anchored to results against humans.[^s2]

Two experiments in the paper are often cited. A network trained by supervised learning on human games predicted expert moves better (60.4% versus about 49-51%), yet the self-play player beat it within 24 hours of training, suggesting it learned a different style of play.[^s2] Ablations showed that residual towers and a shared policy-value network each added roughly 600 Elo.[^s2] Along the way the system rediscovered standard opening sequences (joseki) and later preferred unfamiliar variants, while ladder captures, basic for human beginners, were understood only late in training.[^s2][^s4]

## Limitations and critiques

"Without human knowledge" is a claim about training data, not about the design. The paper itself lists what was built in: the rules, Tromp-Taylor scoring, the board's grid structure in the network, and its rotation and reflection symmetries for data augmentation.[^s2] Gary Marcus argued that these choices, together with the hand-designed tree search and convolutional layers, make the tabula-rasa framing overstated, and that the system shows the value of the right innate structure.[^s5] The method also assumes a perfect simulator of a two-player, perfect-information game, and Singh noted that such systems remain extremely limited compared with human or animal intelligence.[^s2][^s4]

## Connections

AlphaGo Zero is a landmark of `kt:reinforcement-learning` and `kt:deep-learning`. It was **introduced in** `kt:mastering-the-game-of-go-without-human-knowledge` and **created by** `kt:google-deepmind`.[^s1] It is **based on** `kt:monte-carlo-tree-search` and **trained with** `kt:self-play`, using root noise and visit-count sampling to manage `kt:exploration-exploitation`, and its network is a tower of `kt:residual-connection` blocks.[^s2] It **supersedes** `kt:alphago`, dropping that system's `kt:supervised-learning` stage, and was **followed by** `kt:alphazero`, which generalised the same algorithm to chess and shogi.[^s3] The debate over what it learned versus what it was given is a case study in `kt:inductive-bias`.[^s5]

## Sources
[^s1]: Silver et al., "Mastering the game of Go without human knowledge", Nature 550, 354-359, 2017 (RePEc/IDEAS record). https://ideas.repec.org/a/nat/nature/v550y2017i7676d10.1038_nature24270.html (accessed 2026-11-16)
[^s2]: Silver et al., "Mastering the game of Go without human knowledge", full text. https://eclass.uoa.gr/modules/document/file.php/DI437/agz_unformatted_nature.pdf (accessed 2026-11-16)
[^s3]: Silver and Hassabis, "AlphaGo Zero: Starting from scratch", Google DeepMind blog, 2017. https://deepmind.google/blog/alphago-zero-starting-from-scratch/ (accessed 2026-11-16)
[^s4]: Singh, Okun and Jackson, News & Views commentary on AlphaGo Zero, Nature 550, 336-337, 2017. https://web.eecs.umich.edu/~baveja/Papers/NatureNV2017.pdf (accessed 2026-11-16)
[^s5]: Marcus, "Innateness, AlphaZero, and Artificial Intelligence", arXiv:1801.05667, 2018. https://arxiv.org/abs/1801.05667 (accessed 2026-11-16)
