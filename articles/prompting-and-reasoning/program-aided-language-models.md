---
id: kt:program-aided-language-models
type: Technique
title: Program-aided language models
aliases: [PAL, PAL prompting, program-aided language model prompting]
domain: prompting-and-reasoning
summary: >-
  A few-shot prompting technique in which a language model writes its intermediate reasoning as a short
  program, and an external interpreter (typically Python) executes that program to produce the final answer,
  so the model only has to decompose the problem while the runtime does the computation.
maturity: established
broader: [kt:prompt-engineering, kt:tool-use]
related: [kt:program-of-thoughts, kt:scratchpad, kt:self-consistency, kt:toolformer]
relations:
  - {predicate: introducedIn, object: kt:pal-program-aided-language-models}
  - {predicate: extends, object: kt:chain-of-thought}
  - {predicate: evaluatedOn, object: kt:gsm8k}
  - {predicate: evaluatedOn, object: kt:big-bench-hard}
sources:
  - id: s1
    title: "PAL: Program-aided Language Models"
    publisher: arXiv 2211.10435 (Gao, Madaan, Zhou, Alon, Liu, Yang, Callan, Neubig)
    url: https://arxiv.org/pdf/2211.10435
    type: primary
    accessed: 2026-11-17
  - id: s2
    title: "PAL: Program-aided Language Models (ICML 2023, PMLR 202:10764-10799)"
    publisher: Proceedings of Machine Learning Research
    url: https://proceedings.mlr.press/v202/gao23f.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks"
    publisher: arXiv 2211.12588 (Chen, Ma, Wang, Cohen; TMLR 2023)
    url: https://arxiv.org/abs/2211.12588
    type: primary
    accessed: 2026-11-17
  - id: s4
    title: "Augmented Language Models: a Survey"
    publisher: arXiv 2302.07842 (Mialon et al., Meta AI; TMLR 2023)
    url: https://arxiv.org/pdf/2302.07842v1.pdf
    type: primary
    accessed: 2026-11-17
created: 2026-11-17
---

# Program-aided language models

**Program-aided language models (PAL)** is a prompting technique that splits reasoning into two jobs: a large language model reads a natural-language problem and writes a program whose steps mirror its reasoning, and an ordinary interpreter runs that program to compute the answer.[^s1] The method was introduced by Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan and Graham Neubig, mostly at Carnegie Mellon's Language Technologies Institute, posted to arXiv in November 2022 and published at ICML 2023.[^s1][^s2] Its starting observation is that models are often good at breaking a problem into steps yet still slip on the logic or arithmetic within those steps, even when the decomposition is right.[^s2]

## How it works

PAL is a few-shot method. Each exemplar in the prompt pairs a question with a solution written as Python code interleaved with natural-language comments, and the final answer is deliberately left out of the exemplar.[^s1] Where chain-of-thought exemplars already existed for a dataset, the authors rewrote them as programs; otherwise they used three to six randomly chosen examples. Variable names are chosen to name the entities in the question, for example a variable holding the number of tennis balls rather than a single letter.[^s1] At test time the model generates a commented program for the new question, and a standard Python interpreter executes it; the printed or returned value is the answer.[^s1] The model's only task is thus decomposition into runnable steps, while computation is delegated to the runtime.[^s2]

A concurrent paper, **Program of Thoughts (PoT)** prompting by Wenhu Chen, Xueguang Ma, Xinyi Wang and William Cohen, proposed the same separation of reasoning from computation, also mainly with Codex, and evaluated it on math word problems and financial question answering (FinQA, ConvFinQA, TAT-QA).[^s3] PoT reported an average gain of roughly 12% over chain-of-thought in both few-shot and zero-shot settings, and combined it with self-consistency decoding.[^s3]

## Evidence

The PAL paper evaluated 13 tasks: eight arithmetic datasets (including GSM8K, SVAMP and ASDiv), three symbolic tasks from BIG-Bench Hard, and two algorithmic tasks.[^s1] With Codex (code-davinci-002) and greedy decoding, PAL scored 72.0% on GSM8K, against 65.6% for chain-of-thought with the same model and 56.9% for chain-of-thought with the much larger PaLM-540B; majority voting over 40 samples raised PAL to 80.4%.[^s1] The authors also built GSM-HARD, a variant of GSM8K with much larger numbers, where PAL reached 61.2% while Codex chain-of-thought fell to 23.1%, which points to arithmetic, not decomposition, as the weak spot of text-only reasoning.[^s1] PAL beat chain-of-thought on every symbolic and algorithmic task tested, e.g. 96.7% versus 73.0% on object counting.[^s1] These figures date from 2022–2023 models and should not be read as current state of the art.

Ablations isolate where the gain comes from. When the model was asked to predict the program's output itself instead of running it, GSM8K accuracy collapsed to 23.2%, close to direct answering, so the interpreter rather than the code-shaped prompt drives the improvement.[^s1] Replacing meaningful variable names with single letters cut math accuracy from 71.8% to 59.0%, suggesting the names carry part of the reasoning.[^s1]

## Limitations

PAL depends on the base model's coding ability: with the text model text-davinci-001, chain-of-thought outperformed PAL, and weaker code models gave lower absolute accuracy.[^s1] The program is executed once after generation, with no feedback loop letting the model see errors and revise, and gains were small on simple tasks such as single-operation arithmetic.[^s1] Part of GSM-HARD's answer key was produced by PAL itself before manual annotation, which the authors flag as a possible source of error.[^s1] More broadly, a survey of augmented language models notes open questions for tool-using models of this kind: knowing when a tool is actually needed, and the risk that tool-derived answers look more trustworthy than they are.[^s4] The same survey cautions that tools able to act on the world, unlike passive calculators, can cause harm without human validation, a concern that applies whenever model-written code is executed.[^s4]

## In practice

Mialon and colleagues' 2023 survey files PAL both as a reasoning strategy and as a tool-use method, grouping it with approaches that compute via symbolic modules and code interpreters.[^s4] The same idea underlies the code-interpreter or code-execution tools that assistants call for arithmetic, data analysis and table questions, and it is often paired with sampling-based voting to boost accuracy further.[^s1][^s3]

## Connections

PAL **extends** **chain-of-thought prompting** by replacing free-text rationales with executable ones, and sits under **prompt engineering** and **tool use**, since the interpreter is an external tool.[^s1][^s4] It is closely related to **Program of Thoughts**, a concurrent formulation of the same idea, and to **scratchpad** methods that expose intermediate computation.[^s3] Its strongest results combine it with **self-consistency**-style majority voting.[^s1][^s3] **Toolformer** is a neighbouring approach in which the model learns when to call tools rather than being prompted to write a full program.[^s4] PAL was **introduced in** the 2022 paper by Gao et al. and **evaluated on** **GSM8K** and BIG-Bench Hard.[^s1][^s2]

## Sources
[^s1]: Gao, Madaan, Zhou, Alon, Liu, Yang, Callan, Neubig, "PAL: Program-aided Language Models", arXiv 2211.10435. https://arxiv.org/pdf/2211.10435 (accessed 2026-11-17)
[^s2]: Gao et al., "PAL: Program-aided Language Models", ICML 2023, PMLR 202:10764–10799. https://proceedings.mlr.press/v202/gao23f.html (accessed 2026-11-17)
[^s3]: Chen, Ma, Wang, Cohen, "Program of Thoughts Prompting: Disentangling Computation from Reasoning for Numerical Reasoning Tasks", arXiv 2211.12588 (TMLR 2023). https://arxiv.org/abs/2211.12588 (accessed 2026-11-17)
[^s4]: Mialon et al., "Augmented Language Models: a Survey", arXiv 2302.07842. https://arxiv.org/pdf/2302.07842v1.pdf (accessed 2026-11-17)
