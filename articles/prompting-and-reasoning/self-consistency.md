---
id: kt:self-consistency
type: Technique
title: Self-consistency
aliases: [self-consistency decoding, self-consistency prompting, CoT-SC, majority voting over reasoning paths]
domain: prompting-and-reasoning
summary: >-
  A decoding strategy for chain-of-thought prompting that samples many independent reasoning paths from a
  language model and returns the final answer that the largest number of paths agree on, instead of trusting
  a single greedily decoded chain.
maturity: established
broader: [kt:test-time-compute, kt:prompt-engineering]
related: [kt:ensemble-methods, kt:sampling-temperature-and-top-p, kt:universal-self-consistency, kt:large-language-monkeys]
relations:
  - {predicate: introducedIn, object: kt:self-consistency-improves-chain-of-thought-reasoning-in-language-models}
  - {predicate: extends, object: kt:chain-of-thought}
  - {predicate: basedOn, object: kt:large-language-model}
  - {predicate: evaluatedOn, object: kt:gsm8k}
  - {predicate: alternativeTo, object: kt:beam-search}
sources:
  - id: s1
    title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
    publisher: arXiv 2203.11171v4 (Wang, Wei, Schuurmans, Le, Chi, Narang, Chowdhery, Zhou)
    url: https://arxiv.org/pdf/2203.11171v4
    type: primary
    accessed: 2026-11-08
  - id: s2
    title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models (ICLR 2023)"
    publisher: Google Research publications
    url: https://research.google/pubs/self-consistency-improves-chain-of-thought-reasoning-in-language-models/
    type: lab-research
    accessed: 2026-11-08
  - id: s3
    title: "Universal Self-Consistency for Large Language Model Generation"
    publisher: arXiv 2311.17311v1 (Chen, Aksitov, Alon, Ren, Xiao, Yin, Prakash, Sutton, Wang, Zhou)
    url: https://arxiv.org/abs/2311.17311v1
    type: primary
    accessed: 2026-11-08
  - id: s4
    title: "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling"
    publisher: arXiv 2407.21787v3 (Brown, Juravsky, Ehrlich, Clark, Le, Ré, Mirhoseini)
    url: https://arxiv.org/abs/2407.21787v3
    type: preprint
    accessed: 2026-11-08
created: 2026-11-08
---

# Self-consistency

**Self-consistency** is a decoding method for chain-of-thought (CoT) prompting. Rather than letting a language model produce one reasoning chain with greedy decoding, it samples a set of diverse reasoning paths, reads off the final answer of each, and returns the answer that occurs most often.[^s1] It was proposed by Xuezhi Wang, Jason Wei, Denny Zhou and colleagues at Google, first posted to arXiv in March 2022 and published at ICLR 2023.[^s1][^s2] The idea rests on a simple intuition: a hard problem can usually be solved by several different lines of reasoning, and correct lines tend to converge on the same answer while mistaken ones scatter.[^s2]

## How it works

The procedure has three steps.[^s1]

1. Prompt the model with few-shot chain-of-thought exemplars, exactly as in ordinary CoT prompting.[^s1]
2. Instead of greedy decoding, draw *m* independent samples with stochastic decoding, so each sample contains its own reasoning path *r_i* and a final answer *a_i*.[^s1]
3. Aggregate by "marginalizing out" the reasoning paths: choose the answer *a* that maximizes the count of samples with *a_i = a*, i.e. a plurality vote.[^s1]

The authors also tried weighting each answer by the model's probability of its path. Weighting by length-normalized probability performed about as well as the plain vote, while unnormalized weighting was worse, so the unweighted vote became the standard form.[^s1] In the original experiments the models were UL2-20B, GPT-3 (code-davinci-001 and -002), LaMDA-137B and PaLM-540B, all used few-shot with no fine-tuning; sampling used temperatures of 0.5–0.7, top-k of 40 for most models, and 40 sampled paths per question.[^s1]

A small example: asked a multi-step word problem, five sampled chains might end in 18, 18, 26, 18 and 14. Greedy CoT might have produced the chain ending in 26; self-consistency returns 18 because three of five paths agree on it, which is the paper's own motivating pattern.[^s1]

## Evidence

Applied on top of CoT prompting, self-consistency raised accuracy by 17.9 points on GSM8K, 11.0 on SVAMP, 12.2 on AQuA, 6.4 on StrategyQA and 3.9 on ARC-challenge (as reported in the 2023 paper).[^s1][^s2] Accuracy generally rose as the number of sampled paths grew from 1 through 5, 10, 20 and 40.[^s1] It beat several alternatives at equal sample counts: ranking samples by log probability gave much smaller gains, beam search produced less diverse outputs and scored lower, and ensembling over prompt orderings helped less (on LaMDA-137B GSM8K, CoT scored 17.1, a 40-permutation prompt ensemble 19.2, and self-consistency 27.7).[^s1] The agreement rate among samples also correlated with accuracy, giving a rough signal of when the model is unsure.[^s1]

## Limitations

The main cost is compute: every question needs many full generations, though the authors note that 5–10 paths often recover most of the gain.[^s1] The vote also assumes answers can be compared exactly, which holds for numbers or multiple-choice labels but not for free-form text such as summaries or code.[^s1] Universal Self-Consistency (Chen et al., 2023) addresses this by asking the model itself to pick the most consistent candidate; its authors report gains on open-ended tasks and parity with standard voting on math.[^s3] Voting cannot rescue a model whose most common answer is wrong, and sampled chains can still contain flawed reasoning.[^s1] At very large sample budgets, Brown et al. (2024) found that majority voting and reward-model selection stop improving after several hundred samples on problems without an automatic verifier, even while the share of problems solved by at least one sample keeps rising.[^s4]

## In practice

Self-consistency is a common baseline whenever reasoning accuracy matters more than latency, and it is often reported in benchmark tables as "maj@k" or "CoT-SC". It is one of the simplest ways to trade extra inference compute for accuracy, a theme that later work on repeated sampling and inference-time scaling made central.[^s4] Practitioners typically pair it with a moderate sampling temperature and an answer-extraction step that normalizes outputs before voting.[^s1]

## Connections

Self-consistency **extends chain-of-thought prompting**, replacing its single greedy decode with many sampled paths, and is **introduced in** the Wang et al. paper.[^s1] It is an instance of **test-time compute** scaling and sits within **prompt engineering** because it requires no training.[^s4] It is an **alternative to beam search** and sample-and-rank decoding, both of which it outperformed, and its benchmark results were **evaluated on GSM8K** among others.[^s1] It depends on **sampling temperature and top-p/top-k** for path diversity, resembles **ensemble methods** applied within a single model, and is generalized by **universal self-consistency** for free-form outputs.[^s1][^s3] The **Large Language Monkeys** study maps where majority voting stops scaling.[^s4]

## Sources
[^s1]: Wang et al., "Self-Consistency Improves Chain of Thought Reasoning in Language Models", arXiv 2203.11171v4. https://arxiv.org/pdf/2203.11171v4 (accessed 2026-11-08)
[^s2]: Google Research, "Self-Consistency Improves Chain of Thought Reasoning in Language Models", ICLR 2023. https://research.google/pubs/self-consistency-improves-chain-of-thought-reasoning-in-language-models/ (accessed 2026-11-08)
[^s3]: Chen et al., "Universal Self-Consistency for Large Language Model Generation", arXiv 2311.17311v1. https://arxiv.org/abs/2311.17311v1 (accessed 2026-11-08)
[^s4]: Brown et al., "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling", arXiv 2407.21787v3. https://arxiv.org/abs/2407.21787v3 (accessed 2026-11-08)
