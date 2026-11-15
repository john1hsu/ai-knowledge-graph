---
id: kt:monte-carlo-tree-search
type: Algorithm
title: Monte Carlo tree search
aliases: [MCTS, UCT, Upper Confidence bounds applied to Trees]
domain: reinforcement-learning
summary: >-
  A best-first planning algorithm that grows a search tree incrementally from repeated simulations,
  using bandit-style selection to balance trying promising moves against exploring uncertain ones,
  and backing up simulated outcomes to estimate the value of each action.
maturity: established
broader: [kt:reinforcement-learning, kt:monte-carlo-methods]
related: [kt:exploration-exploitation, kt:multi-armed-bandit, kt:markov-decision-process, kt:alphazero, kt:tree-of-thoughts]
relations:
  - {predicate: introducedIn, object: kt:efficient-selectivity-and-backup-operators-in-monte-carlo-tree-search}
  - {predicate: basedOn, object: kt:upper-confidence-bound}
  - {predicate: usedIn, object: kt:alphago}
  - {predicate: usedIn, object: kt:muzero}
  - {predicate: alternativeTo, object: kt:alpha-beta-pruning}
sources:
  - id: s1
    title: "Efficient Selectivity and Backup Operators in Monte-Carlo Tree Search"
    publisher: Computers and Games 2006 (Coulom), author's version
    url: https://www.remi-coulom.fr/CG2006/CG2006.pdf
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "Bandit Based Monte-Carlo Planning"
    publisher: ECML 2006, pp. 282-293 (Kocsis and Szepesvári)
    url: https://cs.nyu.edu/~shasha/papers/uct.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "A Survey of Monte Carlo Tree Search Methods"
    publisher: IEEE Transactions on Computational Intelligence and AI in Games 4(1), March 2012 (Browne et al.)
    url: https://turing.iimas.unam.mx/~luis/cursos/IA2022-1/lecturas/SurveyMCTS.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "Mastering the game of Go with deep neural networks and tree search"
    publisher: Nature 529, 484-489, 2016 (Silver et al.)
    url: https://papers.baulab.info/papers/Silver-2016.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model"
    publisher: arXiv 1911.08265 (Schrittwieser et al., DeepMind)
    url: https://arxiv.org/abs/1911.08265v2
    type: primary
    accessed: 2026-11-15
created: 2026-11-15
---

# Monte Carlo tree search

**Monte Carlo tree search (MCTS)** is a family of planning algorithms that decide what to do in a sequential decision problem by running many simulations from the current state, storing their statistics in a search tree that grows towards the most promising lines, and choosing the action whose subtree looks best. The name was coined by Rémi Coulom in 2006, and in the same year Kocsis and Szepesvári combined tree search with the UCB bandit rule to produce **UCT**, the variant most implementations start from.[^s3] MCTS was the dominant approach in computer Go for a decade and became the planning engine inside AlphaGo, AlphaZero and MuZero.[^s3][^s4][^s5]

## Origin

Coulom's paper, written for his 9×9 Go program Crazy Stone, rejected the earlier split between a min-max phase near the root and a Monte Carlo phase below it. Instead, random games are simulated from the root, nodes near the root store visit counts and value sums, a new node is added whenever a simulation passes through an already-visited one, and the tree grows best-first. Its backup operator blended the mean outcome with the value of the most-simulated move, shifting from averaging towards min-max as visits accumulate; Coulom tuned it empirically rather than deriving it. Crazy Stone won the 10th KGS computer-Go tournament, a result its author attributed partly to luck in a short six-round event.[^s1]

Kocsis and Szepesvári framed the problem for general Markov decision processes and treated the choice of action at each tree node as a separate multi-armed bandit, solved with a modified UCB1 rule.[^s2] For finite-horizon MDPs with rewards in [0, 1] they proved that the bias of the root estimate shrinks as O(log n / n) in the number of episodes and that the probability of picking a wrong root action falls to zero, making UCT consistent; they sketched the discounted case.[^s2] They reported that UCT needed markedly fewer samples than competing planners in their test domains.[^s2]

## How it works

Browne et al.'s survey describes each MCTS iteration as four steps:[^s3]

1. **Selection** — from the root, a *tree policy* repeatedly picks children until it reaches a node that can still be expanded.[^s3]
2. **Expansion** — one or more child nodes are added.[^s3]
3. **Simulation** — a *default policy*, uniformly random in the simplest case, plays from the new node to an outcome.[^s3]
4. **Backpropagation** — the outcome updates the visit counts and value estimates of every node on the path.[^s3]

In UCT, the tree policy picks the action maximising the current value estimate plus an exploration bonus that grows with the logarithm of the parent's visit count and shrinks with the square root of the action's own count, so neglected moves are periodically revisited.[^s2] The survey highlights three properties: MCTS is *aheuristic* (only terminal outcomes need evaluating), *anytime* (it can return its best move whenever stopped, improving with more iterations) and *asymmetric* (the tree is deepest where play looks most promising).[^s3]

## Neural-guided MCTS

AlphaGo (2016) replaced most of the hand-crafted knowledge in MCTS with deep networks. Selection maximised the action value plus a bonus proportional to a policy network's prior divided by one plus the visit count, and each leaf was scored by mixing a value network's estimate with the outcome of a fast rollout.[^s4] The paper notes that the strongest Go programs before it were already MCTS-based; AlphaGo won 494 of 495 games against them and beat European champion Fan Hui 5–0, the first defeat of a professional by a program on the full board.[^s4] MuZero (preprint 2019) kept the search but planned inside a *learned* model that predicts reward, policy and value, so it needed no game rules; DeepMind reported that it matched AlphaZero in Go, chess and shogi and set a new state of the art on 57 Atari games.[^s5]

## Limitations

The survey lists several weaknesses as of 2012: plain UCT struggles in games with *trap states* where a loss follows within a few moves, one reason MCTS lagged in chess; minimax search can be preferable when a reliable evaluation heuristic exists; convergence guarantees need ample time and memory; strong play often requires domain knowledge that slows simulations; and simultaneous-move or imperfect-information games need extra machinery because standard UCT may not converge to a Nash equilibrium.[^s3] It also judged 19×19 Go to be far beyond top human level for MCTS programs at that time, a gap AlphaGo closed four years later by adding learned networks.[^s3][^s4]

## In practice

Beyond Go, the survey catalogues MCTS in Hex, Havannah, general game playing, single-player puzzles, real-time video games and non-game tasks such as scheduling, SAT, feature selection and procedural content generation.[^s3] In modern deep reinforcement learning it is chiefly used as a *policy improvement* step: search produces better move choices than the raw network, and those choices become training targets.[^s4][^s5]

## Connections

MCTS sits under `kt:reinforcement-learning` as a planning method for `kt:markov-decision-process` problems and under `kt:monte-carlo-methods` because it estimates values by averaging sampled returns.[^s2] It is `basedOn` the `kt:upper-confidence-bound` rule from the `kt:multi-armed-bandit` literature, which is how it handles the `kt:exploration-exploitation` dilemma inside the tree.[^s2][^s3] It was `introducedIn` Coulom's 2006 paper.[^s1] It is `usedIn` `kt:alphago` and `kt:muzero`, and `kt:alphazero` is built on it.[^s4][^s5] It is an `alternativeTo` minimax search with `kt:alpha-beta-pruning`, preferred when no good evaluation function is available.[^s3] Search over LLM reasoning steps, as in `kt:tree-of-thoughts`, borrows the same idea of exploring a tree of partial solutions.

## Sources
[^s1]: Coulom, R., "Efficient Selectivity and Backup Operators in Monte-Carlo Tree Search", Computers and Games 2006. https://www.remi-coulom.fr/CG2006/CG2006.pdf (accessed 2026-11-15)
[^s2]: Kocsis, L. and Szepesvári, C., "Bandit Based Monte-Carlo Planning", ECML 2006, pp. 282–293. https://cs.nyu.edu/~shasha/papers/uct.pdf (accessed 2026-11-15)
[^s3]: Browne, C. et al., "A Survey of Monte Carlo Tree Search Methods", *IEEE Transactions on Computational Intelligence and AI in Games* 4(1), 2012. https://turing.iimas.unam.mx/~luis/cursos/IA2022-1/lecturas/SurveyMCTS.pdf (accessed 2026-11-15)
[^s4]: Silver, D. et al., "Mastering the game of Go with deep neural networks and tree search", *Nature* 529, 484–489, 2016. https://papers.baulab.info/papers/Silver-2016.pdf (accessed 2026-11-15)
[^s5]: Schrittwieser, J. et al., "Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model", arXiv:1911.08265. https://arxiv.org/abs/1911.08265v2 (accessed 2026-11-15)
