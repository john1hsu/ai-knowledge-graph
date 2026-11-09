---
id: kt:test-time-compute
type: Concept
title: Test-time compute
aliases: [inference-time compute, test-time scaling, inference-time scaling, thinking time]
domain: prompting-and-reasoning
summary: >-
  The computation a trained model spends at inference on a given input, and the practice of deliberately
  increasing it (longer reasoning chains, many samples, search against a verifier) to improve answer quality
  instead of, or in addition to, training a larger model.
maturity: emerging
broader: [kt:scaling-laws, kt:large-language-model]
related: [kt:chain-of-thought, kt:self-consistency, kt:reasoning-models, kt:reinforcement-learning, kt:gsm8k]
relations:
  - {predicate: dependsOn, object: kt:process-reward-model}
  - {predicate: alternativeTo, object: kt:pretraining}
  - {predicate: usedIn, object: kt:reasoning-models}
sources:
  - id: s1
    title: "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"
    publisher: arXiv 2408.03314v1 (Snell, Lee, Xu, Kumar), 6 August 2024
    url: https://arxiv.org/abs/2408.03314v1
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling"
    publisher: arXiv 2407.21787 (Brown, Juravsky, Ehrlich, Clark, Le, Ré, Mirhoseini), 2024
    url: https://arxiv.org/abs/2407.21787
    type: primary
    accessed: 2026-11-09
  - id: s3
    title: "Learning to reason with LLMs"
    publisher: OpenAI, 12 September 2024
    url: https://openai.com/index/learning-to-reason-with-llms/
    type: lab-research
    accessed: 2026-11-09
  - id: s4
    title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
    publisher: DeepSeek-AI (Guo, Yang, Zhang et al.); arXiv 2501.12948, published in Nature 645 (2025)
    url: https://arxiv.org/abs/2501.12948
    type: primary
    accessed: 2026-11-09
  - id: s5
    title: "s1: Simple test-time scaling"
    publisher: arXiv 2501.19393 (Muennighoff, Yang, Shi, Li, Fei-Fei, Hajishirzi, Zettlemoyer, Liang, Candès, Hashimoto), 2025
    url: https://arxiv.org/abs/2501.19393
    type: primary
    accessed: 2026-11-09
  - id: s6
    title: "Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs"
    publisher: arXiv 2412.21187 (Chen, Xu, Liang et al., Tencent AI Lab), 2024
    url: https://arxiv.org/abs/2412.21187
    type: preprint
    accessed: 2026-11-09
created: 2026-11-09
---

# Test-time compute

**Test-time compute** (also *inference-time compute* or *test-time scaling*) is the amount of computation a trained model uses when answering a particular input, and, by extension, the strategy of spending more of it to get better answers. Instead of only making a model bigger or pretraining it longer, a system can let the same model generate longer reasoning, draw many candidate solutions, or search over partial solutions with a verifier. Snell et al. framed the central question in 2024: given a fixed, non-trivial inference budget on a hard prompt, how much can an LLM improve, and how should that budget be traded against pretraining compute?[^s1] Brown et al. likewise proposed inference compute as a second axis of scaling alongside training.[^s2]

## How it works

Approaches fall into two broad families, which Snell et al. distinguish explicitly.[^s1]

- **Parallel sampling and selection.** Generate *N* independent answers and pick one: majority vote (as in self-consistency), best-of-*N* with a reward model, or an automatic checker such as unit tests. Brown et al. measured *coverage*, the share of problems solved by at least one sample, and found it grows roughly log-linearly with the number of samples across four orders of magnitude, fitting an exponentiated power law. With DeepSeek-Coder-V2-Instruct on SWE-bench Lite, solve rate rose from 15.9% with one sample to 56% with 250 samples (reported in 2024).[^s2]
- **Sequential refinement and search.** Let the model revise its own answer, or search step by step guided by a dense *process* reward model that scores intermediate steps. Snell et al. studied both verifier-guided search and adaptive revision of the model's output distribution.[^s1]

A third route is to *train* the model to use more inference compute on its own. OpenAI described o1 (September 2024) as trained with reinforcement learning to produce a long internal chain of thought, and reported that its accuracy kept rising with both more RL training compute and more thinking time at inference.[^s3] DeepSeek-R1, published in *Nature* in 2025, argued that pure RL on verifiable tasks, without human-written reasoning traces, can elicit behaviours such as self-reflection, verification and strategy switching.[^s4] The s1 paper showed a minimal recipe: fine-tune Qwen2.5-32B-Instruct on 1,000 curated reasoning traces, then apply *budget forcing*, which either cuts reasoning off or appends "Wait" when the model tries to stop, prompting it to re-check its work.[^s5]

## Evidence

The main empirical claim is that inference compute can partly substitute for parameters. Snell et al. reported that allocating compute adaptively by prompt difficulty (a "compute-optimal" strategy) was more than four times as efficient as a best-of-*N* baseline, and that in a FLOPs-matched comparison a smaller model with extra test-time compute could beat a 14× larger model, but only on problems where the small model already had a non-trivial success rate.[^s1] OpenAI's own figures for o1 on AIME 2024 illustrate the same pattern: 74% with one sample, 83% with consensus over 64 samples, and 93% when re-ranking 1,000 samples with a learned scorer; these are lab-reported results.[^s3] For s1-32B, budget forcing raised AIME24 accuracy from 50% to 57% as reported by its authors in 2025.[^s5]

## Limitations and open questions

Gains are uneven. The best method depends strongly on prompt difficulty, and extra compute does little when the base model almost never finds a correct answer.[^s1] Selection is the bottleneck in open-ended domains: without an automatic verifier, majority voting and reward-model ranking plateau after several hundred samples, even while coverage keeps rising.[^s2] Long reasoning also has costs. Chen et al. documented *overthinking*, where o1-style models spend excessive tokens on trivial problems for little benefit, and proposed self-training to shorten reasoning without losing accuracy on GSM8K, MATH500, GPQA and AIME.[^s6] Because inference compute is paid on every query, latency and serving cost become first-order design concerns. Finally, providers may hide raw reasoning: OpenAI chose to show users a model-written summary of o1's chain of thought rather than the chain itself.[^s3]

## In practice

As of 2026, test-time compute is exposed in production chiefly through reasoning models with adjustable "thinking" budgets, and through agent and coding systems that sample multiple candidates and filter them with tests.[^s3][^s2] Open recipes such as s1 and DeepSeek-R1 made the approach reproducible outside frontier labs.[^s4][^s5]

## Connections

- **Broader:** it is the inference-side counterpart to **scaling laws** for pretraining, and a property of how **large language models** are deployed.[^s1][^s2]
- **Chain-of-thought** prompting is the basic way to spend more tokens per answer, and **self-consistency** (majority voting over sampled chains) is the classic parallel-sampling instance; overthinking studies measure reasoning efficiency on benchmarks including **GSM8K**.[^s2][^s6]
- **Reinforcement learning** is how o1- and R1-style **reasoning models** learn to use long reasoning, making test-time compute a trained behaviour.[^s3][^s4]
- It **depends on** verifiers, especially **process reward models**, for search and selection, and is an **alternative to** spending the same budget on more **pretraining**.[^s1]

## Sources
[^s1]: Snell, Lee, Xu, Kumar, "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters", arXiv 2408.03314v1, 2024. https://arxiv.org/abs/2408.03314v1 (accessed 2026-11-09)
[^s2]: Brown et al., "Large Language Monkeys: Scaling Inference Compute with Repeated Sampling", arXiv 2407.21787, 2024. https://arxiv.org/abs/2407.21787 (accessed 2026-11-09)
[^s3]: OpenAI, "Learning to reason with LLMs", 12 September 2024. https://openai.com/index/learning-to-reason-with-llms/ (accessed 2026-11-09)
[^s4]: DeepSeek-AI, "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning", arXiv 2501.12948; Nature 645 (2025). https://arxiv.org/abs/2501.12948 (accessed 2026-11-09)
[^s5]: Muennighoff et al., "s1: Simple test-time scaling", arXiv 2501.19393, 2025. https://arxiv.org/abs/2501.19393 (accessed 2026-11-09)
[^s6]: Chen et al., "Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs", arXiv 2412.21187, 2024. https://arxiv.org/abs/2412.21187 (accessed 2026-11-09)
