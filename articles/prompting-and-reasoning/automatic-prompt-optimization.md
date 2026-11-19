---
id: kt:automatic-prompt-optimization
type: Technique
title: Automatic prompt optimization
aliases: [APO, prompt optimization, automated prompt engineering, LLM-driven prompt search]
domain: prompting-and-reasoning
summary: >-
  A family of methods that treat a language model's prompt as a parameter to be searched or edited
  automatically, usually by another LLM, so as to maximize a task metric on a set of examples instead
  of hand-tuning the wording.
maturity: emerging
broader: [kt:prompt-engineering, kt:mathematical-optimization]
related: [kt:prompt-sensitivity, kt:chain-of-thought, kt:few-shot-prompting]
relations:
  - {predicate: implementedIn, object: kt:dspy}
  - {predicate: contrastsWith, object: kt:prompt-tuning}
  - {predicate: evaluatedOn, object: kt:gsm8k}
sources:
  - id: s1
    title: "Large Language Models Are Human-Level Prompt Engineers"
    publisher: arXiv 2211.01910v2 (Zhou, Muresanu, Han, Paster, Pitis, Chan, Ba)
    url: https://arxiv.org/abs/2211.01910
    type: primary
    accessed: 2026-11-19
  - id: s2
    title: "Large Language Models as Optimizers"
    publisher: ICLR 2024 proceedings (Yang, Wang, Lu, Liu, Le, Zhou, Chen)
    url: https://proceedings.iclr.cc/paper_files/paper/2024/hash/3339f19c5fcee3ad74502947a32be9e6-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s3
    title: "Large Language Models as Optimizers (full text, v3)"
    publisher: arXiv 2309.03409v3 (Yang et al.)
    url: https://arxiv.org/html/2309.03409v3
    type: primary
    accessed: 2026-11-19
  - id: s4
    title: "Automatic Prompt Optimization with \"Gradient Descent\" and Beam Search"
    publisher: EMNLP 2023, pp. 7957-7968 (Pryzant, Iter, Li, Lee, Zhu, Zeng)
    url: https://aclanthology.org/2023.emnlp-main.494
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s5
    title: "DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines"
    publisher: ICLR 2024 proceedings (Khattab, Singhvi, Maheshwari, Zhang, Santhanam, Vardhamanan, Haq, Sharma, Joshi, Moazam, Miller, Zaharia, Potts)
    url: https://proceedings.iclr.cc/paper_files/paper/2024/hash/f1cf02ce09757f57c3b93c0db83181e0-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s6
    title: "Optimizers: choosing one"
    publisher: DSPy documentation (Stanford NLP)
    url: https://dspy.ai/current/diving-deeper/choosing-an-optimizer/
    type: official-docs
    accessed: 2026-11-19
created: 2026-11-19
---

# Automatic prompt optimization

**Automatic prompt optimization** (APO) is the practice of letting an algorithm, rather than a person, search for the wording of a prompt. The prompt is treated as a parameter: candidates are generated, scored against a metric on a small labelled set, and the best are kept or refined. Because large language models are notoriously sensitive to phrasing, a search over prompts can recover accuracy that hand-tuning leaves on the table.[^s1][^s3] Unlike prompt tuning, which learns continuous "soft" embeddings, APO works on ordinary text and only needs API access to a model, so the result can be read, edited and reused.[^s4]

## Origin

An early influential formulation was **Automatic Prompt Engineer (APE)** by Zhou et al. (preprint first posted November 2022). It framed the instruction as a "program" to be synthesized: one LLM proposes a pool of candidate instructions from input-output examples, each candidate is scored by how well a target LLM performs zero-shot when following it, and the highest-scoring one is selected. Across 24 NLP tasks the authors reported that generated instructions were better than or comparable to human-written ones on 19.[^s1] Two 2023 papers then turned selection into iterative optimization: **ProTeGi** by Pryzant et al. (EMNLP 2023) and **OPRO** by Yang et al. (ICLR 2024).[^s4][^s2]

## How it works

Most methods share a loop: *propose → evaluate on training examples → keep the best → propose again*. They differ in how new candidates are proposed.[^s1][^s3][^s4]

- **Optimization by prompting (OPRO).** A meta-prompt lists earlier instructions with their training accuracies, sorted ascending, plus a few task exemplars; the optimizer LLM writes a new instruction, which is scored and added back.[^s3]
- **Textual gradients (ProTeGi).** An LLM critiques the current prompt's errors on a minibatch in natural language, then edits the prompt to address them; beam search and bandit selection pick which edits to keep.[^s4]
- **Program-level compilation (DSPy).** Pipelines of several LM calls are written as declarative modules, and a compiler tunes their prompts and demonstrations against a metric.[^s5]

OPRO's best-known result illustrates the payoff. On GSM8K with PaLM 2-L as the scorer, the instruction "Take a deep breath and work on this problem step-by-step" reached 80.2% zero-shot test accuracy versus 71.8% for the classic "Let's think step by step."[^s3] Across several LLMs, the authors report optimized prompts beating human-designed ones by up to 8% on GSM8K and up to 50% on Big-Bench Hard tasks (figures from the 2024 paper).[^s2] ProTeGi reported improving initial prompts by up to 31% on three NLP benchmarks and a jailbreak-detection task, results its authors called preliminary.[^s4]

## Limitations and open questions

APO needs a labelled training set and a metric; OPRO's authors note that small subsets suffice (about 3.5% of GSM8K's training set in their setup) but the dependence remains.[^s3] The search costs many model calls, and the optimizer's own context window caps how much history it can consider. OPRO's authors also observed that some objective landscapes are too rugged for the LLM to find a good direction, and that the method does not compete with dedicated solvers on classic optimization problems.[^s3] A selected prompt can overfit the examples it was tuned on, and the documentation for DSPy warns that demonstration tuning in particular can overfit a small training set, recommending instruction optimization when evaluation data is small or skewed.[^s6] Whether prompts tuned for one model transfer to another is not settled, which links APO to the wider problem of prompt sensitivity.[^s3]

## In practice

DSPy is an open-source framework built around this idea. Its documentation (as of November 2026) lists optimizers that tune demonstrations (BootstrapFewShot, KNNFewShot), instructions (COPRO, GEPA), both (MIPROv2, SIMBA), or model weights (BootstrapFinetune); each takes a program, a metric and a training set, and returns a compiled copy.[^s6] In the ICLR 2024 paper, compiled DSPy pipelines outperformed standard few-shot prompting and expert-written demonstrations for GPT-3.5 and Llama2-13b-chat.[^s5] Typical uses are tuning classifiers, extraction prompts and multi-step retrieval or agent pipelines where a reliable metric exists.

## Connections

APO is a branch of **prompt engineering** that automates its trial-and-error side, and it borrows the vocabulary of **mathematical optimization** (objectives, search, even "gradients").[^s3][^s4] It is a practical response to **prompt sensitivity**: if small wording changes move accuracy, searching over wording is worthwhile.[^s1] Its headline results involve **chain-of-thought** triggers evaluated on **GSM8K**, and frameworks such as **DSPy** also tune **few-shot** demonstrations alongside instructions.[^s3][^s5][^s6] It **contrasts with prompt tuning**, which learns continuous prompt embeddings and so needs access to model internals, whereas text-based APO methods such as ProTeGi need only training data and API access to the model.[^s4]

## Sources
[^s1]: Zhou et al., "Large Language Models Are Human-Level Prompt Engineers", arXiv 2211.01910. https://arxiv.org/abs/2211.01910 (accessed 2026-11-19)
[^s2]: Yang et al., "Large Language Models as Optimizers", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/3339f19c5fcee3ad74502947a32be9e6-Abstract-Conference.html (accessed 2026-11-19)
[^s3]: Yang et al., "Large Language Models as Optimizers", arXiv 2309.03409v3 (full text). https://arxiv.org/html/2309.03409v3 (accessed 2026-11-19)
[^s4]: Pryzant et al., "Automatic Prompt Optimization with 'Gradient Descent' and Beam Search", EMNLP 2023. https://aclanthology.org/2023.emnlp-main.494 (accessed 2026-11-19)
[^s5]: Khattab et al., "DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/f1cf02ce09757f57c3b93c0db83181e0-Abstract-Conference.html (accessed 2026-11-19)
[^s6]: DSPy documentation, "Optimizers: choosing one". https://dspy.ai/current/diving-deeper/choosing-an-optimizer/ (accessed 2026-11-19)
