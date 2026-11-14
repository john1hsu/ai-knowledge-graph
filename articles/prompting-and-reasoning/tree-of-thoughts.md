---
id: kt:tree-of-thoughts
type: Technique
title: Tree of Thoughts
aliases: [ToT, tree-of-thought prompting, Tree-of-Thought]
domain: prompting-and-reasoning
summary: >-
  An inference-time framework in which a language model generates several candidate intermediate reasoning
  steps ("thoughts"), evaluates them itself, and explores the resulting tree with a search algorithm such as
  breadth-first or depth-first search, allowing lookahead and backtracking instead of a single left-to-right chain.
maturity: established
broader: [kt:test-time-compute, kt:prompt-engineering]
related: [kt:self-consistency, kt:planning-in-llms, kt:graph-of-thoughts]
relations:
  - {predicate: introducedIn, object: kt:tree-of-thoughts-deliberate-problem-solving-with-large-language-models}
  - {predicate: extends, object: kt:chain-of-thought}
  - {predicate: influencedBy, object: kt:heuristic-search}
sources:
  - id: s1
    title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    publisher: arXiv 2305.10601 (Yao, Yu, Zhao, Shafran, Griffiths, Cao, Narasimhan)
    url: https://arxiv.org/pdf/2305.10601
    type: primary
    accessed: 2026-11-14
  - id: s2
    title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models (NeurIPS 2023 oral)"
    publisher: NeurIPS 2023
    url: https://neurips.cc/virtual/2023/oral/73874
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "Tree of Thoughts: Deliberate Problem Solving with Large Language Models (publication record)"
    publisher: Princeton University research portal
    url: https://collaborate.princeton.edu/en/publications/tree-of-thoughts-deliberate-problem-solving-with-large-language-m-2/
    type: academic
    accessed: 2026-11-14
  - id: s4
    title: "Large Language Model Guided Tree-of-Thought"
    publisher: arXiv 2305.08291 (Jieyi Long)
    url: https://arxiv.org/abs/2305.08291
    type: primary
    accessed: 2026-11-14
  - id: s5
    title: "Graph of Thoughts: Solving Elaborate Problems with Large Language Models"
    publisher: arXiv 2308.09687 (Besta et al.)
    url: https://arxiv.org/pdf/2308.09687
    type: primary
    accessed: 2026-11-14
  - id: s6
    title: "Graph of Thoughts: Solving Elaborate Problems with Large Language Models (AAAI 2024)"
    publisher: ML Anthology (AAAI 2024, pp. 17682–17690)
    url: https://mlanthology.org/aaai/2024/besta2024aaai-graph
    type: peer-reviewed
    accessed: 2026-11-14
created: 2026-11-14
---

# Tree of Thoughts

**Tree of Thoughts (ToT)** is an inference framework that turns a language model's reasoning into an explicit search. Instead of producing one chain of reasoning token by token, the model proposes several coherent intermediate steps, called *thoughts*, judges how promising each partial solution is, and a search procedure decides which branches to expand, look ahead on, or abandon.[^s1] It was introduced by Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao and Karthik Narasimhan (Princeton University and Google DeepMind), posted to arXiv in May 2023 and presented as an oral paper at NeurIPS 2023.[^s1][^s2][^s3] A closely related "Tree-of-Thought" system by Jieyi Long appeared on arXiv two days earlier, independently framing LLM problem solving as tree exploration with backtracking.[^s4]

## Motivation

The authors argue that left-to-right decoding suits tasks where each step follows easily from the last, but fails when early choices are decisive or when solving requires exploration and lookahead.[^s1] They draw on Newell, Shaw and Simon's classical view of problem solving as search through a tree of partial solutions, and on dual-process theory: token-level generation plays the role of fast "System 1", while the search wrapped around it supplies deliberate "System 2" planning.[^s1]

## How it works

A ToT instance is defined by four design choices.[^s1]

1. **Thought decomposition.** Split the problem into steps sized for the task: a few words in a crossword, one equation in an arithmetic puzzle, a paragraph-level plan in writing.[^s1]
2. **Thought generator.** Either *sample* several independent thoughts from a chain-of-thought-style prompt (useful when the space of thoughts is rich), or *propose* several distinct thoughts in one prompt (useful when the space is constrained, to avoid duplicates).[^s1]
3. **State evaluator.** The model itself rates states, either by *valuing* each one independently (for example, labelling a Game of 24 state "sure", "maybe" or "impossible" to reach 24) or by *voting* across candidates for the most promising one.[^s1]
4. **Search algorithm.** Breadth-first search keeps the best *b* states at each depth; depth-first search follows the most promising branch, prunes states the evaluator rejects, and backtracks.[^s1]

The paper treats ordinary input–output prompting, chain-of-thought, self-consistency and self-refinement as special cases of ToT with trees of limited depth and breadth.[^s1]

## Evidence

All results below are from the 2023 paper, using GPT-4.[^s1] On **Game of 24**, a puzzle requiring arithmetic on four numbers to reach 24, chain-of-thought prompting solved 4.0% of problems, self-consistency 9.0%, ToT with breadth 1 45%, and ToT with breadth 5 74%.[^s1][^s2] On **Mini Crosswords** (5×5), word-level accuracy rose from 15.6% with chain-of-thought to 60% with ToT using DFS, and full games solved rose from 1 to 4 of 20.[^s1] On **Creative Writing**, GPT-4-scored coherency averaged 7.56 for ToT versus 6.93 for chain-of-thought, and in a blind human comparison ToT was preferred in 41 of 100 pairs against 21 for chain-of-thought.[^s1]

## Limitations

The gains come at a steep price: the authors estimate ToT can generate 5 to 100 times more tokens than chain-of-thought, roughly $0.74 per Game of 24 problem with GPT-4 at the time.[^s1] They also note that deliberate search may be unnecessary on tasks a strong model already handles, that their evaluation covered only three fairly simple tasks, and that the self-evaluation used for pruning is an imperfect heuristic that can wrongly discard valid steps.[^s1] ToT also requires hand-designed, task-specific decomposition and evaluation prompts, which limits how directly it transfers to new problems.[^s1]

## In practice

ToT is mostly used as a research pattern and as a baseline in work on LLM reasoning and planning, and it helped popularise the idea of spending extra inference compute on structured search rather than one long sample.[^s1] Follow-up work generalised the structure: **Graph of Thoughts** (Besta et al., AAAI 2024) represents thoughts as vertices in an arbitrary graph, adding aggregation of several thoughts and iterative refinement, and reports about 62% higher sorting quality than ToT at over 31% lower cost.[^s5][^s6] The authors of ToT themselves suggested fine-tuning models for this kind of deliberate decision making as future work, a direction later explored by trained reasoning models.[^s1]

## Connections

Tree of Thoughts **extends chain-of-thought prompting** from a single path to a searchable tree and is **introduced in** the Yao et al. NeurIPS 2023 paper.[^s1][^s2] It is a form of **test-time compute** scaling and sits within **prompt engineering**, because it wraps an unmodified model in prompts and search code.[^s1] It is **influenced by heuristic search** in classical AI, the Newell–Shaw–Simon tradition the authors cite.[^s1] It generalises **self-consistency**, which samples paths but never evaluates or expands partial ones, and it is an early technique for **planning in LLMs**.[^s1] It is itself generalised by **Graph of Thoughts**.[^s5]

## Sources
[^s1]: Yao et al., "Tree of Thoughts: Deliberate Problem Solving with Large Language Models", arXiv 2305.10601 (NeurIPS 2023 camera-ready). https://arxiv.org/pdf/2305.10601 (accessed 2026-11-14)
[^s2]: NeurIPS 2023 oral, "Tree of Thoughts: Deliberate Problem Solving with Large Language Models". https://neurips.cc/virtual/2023/oral/73874 (accessed 2026-11-14)
[^s3]: Princeton University research portal, publication record for "Tree of Thoughts", Advances in Neural Information Processing Systems 36. https://collaborate.princeton.edu/en/publications/tree-of-thoughts-deliberate-problem-solving-with-large-language-m-2/ (accessed 2026-11-14)
[^s4]: Long, "Large Language Model Guided Tree-of-Thought", arXiv 2305.08291. https://arxiv.org/abs/2305.08291 (accessed 2026-11-14)
[^s5]: Besta et al., "Graph of Thoughts: Solving Elaborate Problems with Large Language Models", arXiv 2308.09687. https://arxiv.org/pdf/2308.09687 (accessed 2026-11-14)
[^s6]: ML Anthology, "Graph of Thoughts: Solving Elaborate Problems with Large Language Models", AAAI 2024. https://mlanthology.org/aaai/2024/besta2024aaai-graph (accessed 2026-11-14)
