---
id: kt:self-refine-iterative-refinement-with-self-feedback
type: Work
title: "Self-Refine: Iterative Refinement with Self-Feedback"
aliases: [Self-Refine, SELF-REFINE, Madaan et al. 2023]
domain: prompting-and-reasoning
summary: >-
  A NeurIPS 2023 paper by Madaan et al. introducing Self-Refine, an inference-time method in which one
  language model drafts an output, critiques it in natural language, and rewrites it using that critique,
  repeating the loop without any extra training, supervised data or reinforcement learning.
maturity: established
broader: [kt:prompt-engineering, kt:self-correction]
related: [kt:self-consistency, kt:test-time-compute, kt:chain-of-thought, kt:reflexion, kt:large-language-model]
relations:
  - {predicate: evaluatedOn, object: kt:gsm8k}
  - {predicate: contrastsWith, object: kt:rlhf}
sources:
  - id: s1
    title: "Self-Refine: Iterative Refinement with Self-Feedback (abstract page)"
    publisher: NeurIPS 2023, Advances in Neural Information Processing Systems 36 (Madaan, Tandon, Gupta, Hallinan, Gao, Wiegreffe, Alon, Dziri, Prabhumoye, Yang, Gupta, Majumder, Hermann, Welleck, Yazdanbakhsh, Clark)
    url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "Self-Refine: Iterative Refinement with Self-Feedback (full paper PDF)"
    publisher: NeurIPS 2023 proceedings (Madaan et al.)
    url: https://proceedings.neurips.cc/paper_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024 poster)"
    publisher: ICLR 2024 (Huang, Chen, Mishra, Zheng, Yu, Song, Zhou)
    url: https://iclr.cc/virtual/2024/poster/18956
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "Large Language Models Cannot Self-Correct Reasoning Yet"
    publisher: arXiv 2310.01798v1 (Huang et al.)
    url: https://arxiv.org/html/2310.01798v1
    type: primary
    accessed: 2026-11-11
  - id: s5
    title: "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs"
    publisher: TACL vol. 12, pp. 1417-1440, 2024 (Kamoi, Zhang, Zhang, Han, Zhang)
    url: https://aclanthology.org/2024.tacl-1.78
    type: peer-reviewed
    accessed: 2026-11-11
created: 2026-11-11
---

# Self-Refine: Iterative Refinement with Self-Feedback

**"Self-Refine: Iterative Refinement with Self-Feedback"** is a paper by Aman Madaan and fifteen co-authors, published at NeurIPS 2023, that introduced the **Self-Refine** method. A single large language model writes a first answer, generates feedback on that answer, and then revises it in light of the feedback, cycling through these steps several times. The method needs no supervised training data, no additional training and no reinforcement learning; it is driven entirely by prompts at inference time.[^s1] The authors motivate it by analogy with how people revise a terse email or tidy up hastily written code.[^s2]

## How it works

Self-Refine uses one model in three roles, each set up with a few-shot prompt.[^s2]

1. **Generate.** The model produces an initial output y₀ for the input.[^s2]
2. **Feedback.** The same model is prompted to critique y₀, ideally pointing to concrete problems and how to fix them.[^s2]
3. **Refine.** The model rewrites the output using that critique. The refine prompt carries the full history of earlier drafts and critiques, so the model can avoid repeating past mistakes.[^s2]

The loop ends after a fixed number of rounds or when the feedback signals that no further changes are needed; the main experiments capped it at four iterations.[^s2]

## Results

The paper tested GPT-3.5 (text-davinci-003), ChatGPT and GPT-4, plus Codex for code, on seven tasks: sentiment reversal, dialogue response generation, code optimization on the PIE dataset, code readability, math reasoning on GSM8K, acronym generation and a new "CommonGen-Hard" constrained-generation task that requires 20–30 keywords in one sentence.[^s2] Averaged across tasks, the authors report roughly a 20-point absolute gain over one-shot generation, judged by humans and automatic metrics.[^s1] Gains were large on open-ended tasks, for example dialogue response with GPT-4 rising from 25.4 to 74.6 and constrained generation from 4.4 to 61.3, but math reasoning barely moved (GPT-4: 92.9 to 93.1).[^s2]

Ablations explain where the gains come from. Specific, actionable feedback beat generic feedback, which beat no feedback at all; without feedback the model tended to repeat itself.[^s2] Against a baseline that drew four independent ChatGPT samples, human raters still preferred refined outputs, suggesting the improvement comes from revision rather than simply more attempts.[^s2] On math, the model judged about 94% of its own flawed solutions as fine, and gains above five points appeared only when an external signal flagged wrong answers.[^s2] Most failures on code and math traced to bad feedback (wrong fix or wrong error location) rather than to the refiner ignoring good feedback.[^s2]

## Limitations and critiques

The authors note that Self-Refine needs a base model with strong few-shot or instruction-following ability: Vicuna-13B often failed to produce feedback in the required format, and experiments were in English on mostly closed models.[^s2]

Later work questioned how far the approach generalises. Huang et al. (ICLR 2024) studied **intrinsic** self-correction, where a model revises its answer with no external feedback, and found that LLMs struggle to correct their reasoning this way and sometimes get worse.[^s3] In a replication on CommonGen-Hard, they argued that Self-Refine's initial prompt omitted the requirement to use every concept, which the feedback prompt then supplied; a plain prompt that stated the requirement up front scored 81.8, above Self-Refine's refined 75.1.[^s4] A 2024 TACL survey by Kamoi et al. concluded that self-correction works well when reliable external feedback is available or after large-scale fine-tuning, but that prior work had not shown success using feedback from prompted LLMs alone except on tasks unusually suited to it.[^s5]

## In practice

For practitioners using a draft–critique–revise loop, the evidence above suggests pairing it with an external check (tests, a verifier, a retrieval lookup) for tasks with verifiable answers, and comparing its cost against simply improving the first prompt.[^s4][^s5]

## Connections

Self-Refine is a prompting technique, so it sits under **prompt engineering**, and it is the best-known instance of the broader idea of **self-correction** by language models.[^s1][^s5] It spends extra inference on revision, making it a form of **test-time compute**, and it differs from **self-consistency**, which samples several independent answers and votes rather than revising one.[^s2] Its math evaluation used **GSM8K**.[^s2] The paper positions it against training-based refinement such as **RLHF**, which needs reward models and parameter updates, and lists **Reflexion** as concurrent work on feedback-driven revision.[^s2] Like **chain-of-thought** prompting, it relies on a **large language model** that follows few-shot instructions well.[^s2]

## Sources
[^s1]: Madaan et al., "Self-Refine: Iterative Refinement with Self-Feedback", NeurIPS 2023 (abstract page). https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract.html (accessed 2026-11-11)
[^s2]: Madaan et al., "Self-Refine: Iterative Refinement with Self-Feedback", NeurIPS 2023 (full paper). https://proceedings.neurips.cc/paper_files/paper/2023/file/91edff07232fb1b55a505a9e9f6c0ff3-Paper-Conference.pdf (accessed 2026-11-11)
[^s3]: Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet", ICLR 2024 poster. https://iclr.cc/virtual/2024/poster/18956 (accessed 2026-11-11)
[^s4]: Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet", arXiv 2310.01798v1. https://arxiv.org/html/2310.01798v1 (accessed 2026-11-11)
[^s5]: Kamoi, Zhang, Zhang, Han and Zhang, "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs", TACL 12 (2024). https://aclanthology.org/2024.tacl-1.78 (accessed 2026-11-11)
