---
id: kt:least-to-most-prompting
type: Technique
title: Least-to-most prompting
aliases: [least-to-most, LtM prompting, L2M prompting]
domain: prompting-and-reasoning
summary: >-
  A few-shot prompting technique that first asks a language model to break a hard problem into a sequence of
  simpler subproblems, then solves those subproblems in order, feeding each earlier answer into the prompt for
  the next, so the model can generalise to problems harder than its exemplars.
maturity: established
broader: [kt:prompt-engineering]
related: [kt:few-shot-prompting, kt:decomposed-prompting, kt:compositional-generalization]
relations:
  - {predicate: introducedIn, object: kt:least-to-most-prompting-enables-complex-reasoning-in-large-language-models}
  - {predicate: extends, object: kt:chain-of-thought}
  - {predicate: evaluatedOn, object: kt:gsm8k}
sources:
  - id: s1
    title: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models"
    publisher: arXiv 2205.10625v3 (Zhou, Schärli, Hou, Wei, Scales, Wang, Schuurmans, Cui, Bousquet, Le, Chi)
    url: https://arxiv.org/pdf/2205.10625v3
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models (ICLR 2023 poster)"
    publisher: ICLR 2023
    url: https://iclr.cc/virtual/2023/poster/12263
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models (publication record)"
    publisher: ML Anthology (ICLR 2023)
    url: https://mlanthology.org/iclr/2023/zhou2023iclr-leasttomost
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "Compositional Semantic Parsing with Large Language Models"
    publisher: arXiv 2209.15003 (Drozdov, Schärli, Akyürek, Scales, Song, Chen, Bousquet, Zhou)
    url: https://arxiv.org/pdf/2209.15003
    type: primary
    accessed: 2026-11-15
  - id: s5
    title: "Decomposed Prompting: A Modular Approach for Solving Complex Tasks"
    publisher: arXiv 2210.02406v2 (Khot, Trivedi, Finlayson, Fu, Richardson, Clark, Sabharwal)
    url: https://arxiv.org/abs/2210.02406v2
    type: primary
    accessed: 2026-11-15
  - id: s6
    title: "Decomposed Prompting: A Modular Approach for Solving Complex Tasks (publication record)"
    publisher: ML Anthology (ICLR 2023)
    url: https://mlanthology.org/iclr/2023/khot2023iclr-decomposed
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Least-to-most prompting

**Least-to-most prompting** is a prompting strategy in which a language model solves a hard problem by first reducing it to a list of easier subproblems and then answering those subproblems one at a time, with every answer so far carried forward into the next prompt.[^s1] It was proposed by Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans, Claire Cui, Olivier Bousquet, Quoc Le and Ed Chi at Google, first posted to arXiv in May 2022 and published at ICLR 2023.[^s1][^s2][^s3] The name is borrowed from educational psychology, where it describes a progressive sequence of prompts used to help a learner acquire a new skill.[^s1]

## Motivation

The authors observed that chain-of-thought prompting works well when test problems resemble the worked examples in the prompt, but degrades when a problem is harder than any of those exemplars, an *easy-to-hard generalisation* gap.[^s1] Their remedy is to make the model teach itself a curriculum: if a hard problem can be expressed as a chain of easier ones, each step is close in difficulty to what the exemplars demonstrate.[^s1][^s2]

## How it works

The method has two stages, both implemented purely with few-shot prompting and no training or fine-tuning.[^s1]

1. **Decomposition.** A prompt with fixed examples of how to split problems into subproblems is followed by the new question; the model outputs an ordered list of subquestions.[^s1]
2. **Sequential subproblem solving.** For each subquestion, the prompt contains fixed examples of solved subproblems, the subquestions already answered together with their generated answers, and then the next subquestion. The original question is posed last.[^s1]

For example, to concatenate the last letters of a long list of words, the model first handles the first two words, then appends the next word's last letter to that intermediate result, and so on, so each call is only slightly harder than the previous one.[^s1] For some tasks the two stages can be merged into a single prompt.[^s1] The key difference from chain-of-thought is that later steps are conditioned on explicitly answered earlier subproblems rather than on one free-running rationale.[^s1]

## Evidence

All figures below are from the 2023 paper and use GPT-3 `code-davinci-002`.[^s1] On **SCAN**, a compositional-generalisation benchmark that maps commands to action sequences, least-to-most prompting with 14 exemplars reached at least 99% accuracy on every split, including the length split, while chain-of-thought reached 16%; the authors contrast this with specialised neural-symbolic models trained on more than 15,000 examples.[^s1][^s2] On **last-letter concatenation**, accuracy fell from 94.0% to 74.0% as lists grew from 4 to 12 words, versus a fall from 84.2% to 31.8% for chain-of-thought.[^s1] On **GSM8K** math word problems the overall gain was small (62.39% versus 60.87%), but larger on problems needing at least five steps (45.23% versus 39.07%); on numerical subsets of **DROP** it beat chain-of-thought by roughly 8 to 14 points.[^s1]

## Limitations

Decomposition prompts transfer poorly: a prompt written for math word problems does not help with commonsense questions, so each domain needs its own decomposition exemplars.[^s1] Decomposing can itself be the bottleneck; the authors report that nearly all GSM8K problems were solved when the model was given a correct decomposition, implying errors stem mainly from splitting the problem.[^s1] They also note that the striking SCAN and last-letter results rely on tasks whose decomposition is comparatively easy.[^s1] Because each subproblem is a separate model call, the method also costs more calls and tokens than a single chain-of-thought pass.[^s1]

## In practice and follow-ups

Least-to-most prompting became a standard baseline for problem decomposition in LLM reasoning research. A follow-up by several of the same authors, **dynamic least-to-most prompting**, first decomposes inputs through prompting-based syntactic parsing and uses that decomposition to choose exemplars; with `code-davinci-002` it reported 95.0% average exact-match accuracy on the CFQ semantic-parsing benchmark's MCD splits while using about 1% of the training data of traditional approaches (as reported in 2022).[^s4] **Decomposed Prompting** (Khot et al., ICLR 2023) generalises the idea into a modular library of sub-task handlers, where each sub-task can be decomposed further or delegated to a trained model or symbolic function.[^s5][^s6]

## Connections

Least-to-most prompting **extends chain-of-thought prompting** by making the intermediate steps explicit, separately answered subquestions, and it is **introduced in** Zhou et al.'s ICLR 2023 paper.[^s1][^s2] It is a technique within **prompt engineering** that relies on **few-shot prompting** for both of its stages.[^s1] It was **evaluated on GSM8K** among other benchmarks, and its headline SCAN results made it a reference point for **compositional generalisation** with prompted models, extended by dynamic least-to-most prompting.[^s1][^s4] **Decomposed Prompting** is a closely related, more modular decomposition framework.[^s5][^s6]

## Sources
[^s1]: Zhou et al., "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models", arXiv 2205.10625v3 (ICLR 2023). https://arxiv.org/pdf/2205.10625v3 (accessed 2026-11-15)
[^s2]: ICLR 2023 poster, "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models". https://iclr.cc/virtual/2023/poster/12263 (accessed 2026-11-15)
[^s3]: ML Anthology, publication record for Zhou et al., ICLR 2023. https://mlanthology.org/iclr/2023/zhou2023iclr-leasttomost (accessed 2026-11-15)
[^s4]: Drozdov et al., "Compositional Semantic Parsing with Large Language Models", arXiv 2209.15003. https://arxiv.org/pdf/2209.15003 (accessed 2026-11-15)
[^s5]: Khot et al., "Decomposed Prompting: A Modular Approach for Solving Complex Tasks", arXiv 2210.02406v2. https://arxiv.org/abs/2210.02406v2 (accessed 2026-11-15)
[^s6]: ML Anthology, publication record for Khot et al., "Decomposed Prompting", ICLR 2023. https://mlanthology.org/iclr/2023/khot2023iclr-decomposed (accessed 2026-11-15)
