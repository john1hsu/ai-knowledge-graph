---
id: kt:scratchpad
type: Technique
title: Scratchpad
aliases: [scratchpads, scratchpad reasoning, show your work, intermediate computation scratchpad]
domain: prompting-and-reasoning
summary: >-
  A technique in which a language model is trained or few-shot prompted to write the intermediate steps of a
  multi-step computation (such as partial sums or a program's execution trace) into a delimited buffer before
  emitting its final answer, which markedly improves accuracy on algorithmic tasks.
maturity: established
broader: [kt:prompt-engineering, kt:test-time-compute]
related: [kt:chain-of-thought, kt:reasoning-models, kt:star-self-taught-reasoner, kt:context-window, kt:large-language-model]
relations:
  - {predicate: introducedIn, object: kt:show-your-work-scratchpads-for-intermediate-computation-with-language-models}
  - {predicate: basedOn, object: kt:large-language-model}
  - {predicate: influencedBy, object: kt:program-induction-by-rationale-generation}
  - {predicate: followedBy, object: kt:chain-of-thought}
  - {predicate: dependsOn, object: kt:context-window}
sources:
  - id: s1
    title: "Show Your Work: Scratchpads for Intermediate Computation with Language Models"
    publisher: arXiv 2112.00114 (Nye, Andreassen, Gur-Ari, Michalewski, Austin, Bieber, Dohan, Lewkowycz, Bosma, Luan, Sutton, Odena)
    url: https://arxiv.org/pdf/2112.00114
    type: primary
    accessed: 2026-11-10
  - id: s2
    title: "Show Your Work: Scratchpads for Intermediate Computation with Language Models"
    publisher: Google Research publications
    url: https://research.google/pubs/show-your-work-scratchpads-for-intermediate-computation-with-language-models/
    type: lab-research
    accessed: 2026-11-10
  - id: s3
    title: "Program Induction by Rationale Generation: Learning to Solve and Explain Algebraic Word Problems"
    publisher: ACL 2017 (Ling, Yogatama, Dyer, Blunsom)
    url: https://aclanthology.org/P17-1015/
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s4
    title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    publisher: NeurIPS 2022 (Wei et al.)
    url: https://proceedings.nips.cc/paper_files/paper/2022/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s5
    title: "STaR: Bootstrapping Reasoning With Reasoning"
    publisher: NeurIPS 2022 (Zelikman, Wu, Mu, Goodman)
    url: https://proceedings.neurips.cc/paper_files/paper/2022/hash/639a9a172c044fbb64175b5fad42e9a5-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s6
    title: "Extended thinking"
    publisher: Claude Platform documentation (Anthropic)
    url: https://platform.claude.com/docs/en/build-with-claude/extended-thinking.md
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# Scratchpad

A **scratchpad** is a buffer of intermediate steps that a language model writes out before it commits to a final answer. The idea was introduced by Maxwell Nye, Augustus Odena and colleagues at Google in the paper "Show Your Work: Scratchpads for Intermediate Computation with Language Models", posted to arXiv in November 2021.[^s1][^s2] Its starting observation was that large pretrained transformers handle tasks that can be solved in one forward pass, such as writing text or code, yet fail at tasks needing many sequential steps, such as adding long integers or predicting what a program prints.[^s1] Letting the model "show its work" turned many of these failures into successes.[^s2]

## How it works

Training or prompting examples are rewritten so that the target output contains the intermediate computation, wrapped in `<scratch>` and `</scratch>` delimiters, followed by the final answer.[^s1] For long addition, the scratchpad records each digit-wise step with its carry; for polynomial evaluation it lists the value of each term; for Python programs it is a line-by-line execution trace that records the values of local variables after each line runs.[^s1] Because a transformer does a fixed amount of computation per generated token, emitting the trace gives the model extra steps of computation, and the earlier steps become context it can read back when producing later ones.[^s1] The approach works both with fine-tuning on traced examples and with few-shot prompting, where a handful of traced exemplars sit in the prompt.[^s1]

## Evidence

The original experiments used models from about 2 million to 1 billion parameters for addition, and a 137B-parameter decoder for few-shot work.[^s1] In addition, models were trained on 1–8 digit sums and tested on 9- and 10-digit sums; direct-answer baselines failed out of distribution even at the largest size, while scratchpad models improved with scale.[^s1] For polynomial evaluation, scratchpads raised accuracy from 8.8% to 20.1% few-shot and from 31.8% to 50.7% after fine-tuning.[^s1] For synthetic Python programs, fine-tuned execution accuracy rose from 20% (direct) to 41.5% (scratchpad).[^s1] On real MBPP programs the gains depended on data: with only the small MBPP training set neither method did well, but after adding model-sampled programs and CodeNet traces the best scratchpad model reached 26.6% per-task execution accuracy, while direct execution trained on the augmented programs managed 5.1% (all figures as reported in the 2021 paper).[^s1]

## Limitations

Scratchpads lengthen outputs, so they are bounded by the context window; the authors capped generation at 512 tokens in a 1,024-token context and had to restrict MBPP evaluation to a 212-task subset whose traces fit.[^s1] Supervised scratchpads also need traced training data, which is easy to produce for programs but costly for natural-language problems; Wei et al. stress that building large sets of high-quality rationales is expensive.[^s4] Nye et al. themselves named learning to use a scratchpad without supervision, for example with reinforcement learning, as an open direction.[^s1] A written trace is also not proof of correct computation: even the best model produced exact traces for only about 42% of examples under greedy decoding.[^s1]

## Lineage and in practice

Scratchpads sit in a line of work on intermediate steps. Ling et al. (ACL 2017) trained models to generate natural-language rationales mixed with arithmetic for algebra word problems, using a dataset of about 100,000 rationale-annotated questions.[^s3] Chain-of-thought prompting (Wei et al., 2022) lists the scratchpad work among its predecessors and showed that a few natural-language reasoning exemplars suffice with large models, with no fine-tuning at all.[^s4] STaR (Zelikman et al., 2022) then addressed the data cost by bootstrapping rationales: the model generates its own reasoning, keeps chains that reach correct answers, and is fine-tuned on them iteratively.[^s5] Today's reasoning models generate a dedicated stream of reasoning before the visible answer. For example, as of November 2026 Anthropic's API returns "thinking" blocks ahead of the final text block and bills that reasoning as output tokens, a productized descendant of the scratchpad idea.[^s6]

## Connections

Scratchpad is **introduced in** Nye et al. (2021) and is **based on** large language models, either fine-tuned or few-shot prompted.[^s1] It was **influenced by** rationale generation for word problems from Ling et al.[^s3] and was **followed by** chain-of-thought prompting, which moved intermediate steps from supervised traces to natural-language exemplars.[^s4] It is an early form of **test-time compute**, spending more generated tokens per question for accuracy, and it **depends on** the **context window**, which limits trace length.[^s1] **STaR** extends it by having models write their own rationales,[^s5] and **reasoning models** expose a scratchpad-like thinking stream as a product feature.[^s6]

## Sources
[^s1]: Nye et al., "Show Your Work: Scratchpads for Intermediate Computation with Language Models", arXiv 2112.00114. https://arxiv.org/pdf/2112.00114 (accessed 2026-11-10)
[^s2]: Google Research, "Show Your Work: Scratchpads for Intermediate Computation with Language Models" (2021). https://research.google/pubs/show-your-work-scratchpads-for-intermediate-computation-with-language-models/ (accessed 2026-11-10)
[^s3]: Ling, Yogatama, Dyer & Blunsom, "Program Induction by Rationale Generation", ACL 2017. https://aclanthology.org/P17-1015/ (accessed 2026-11-10)
[^s4]: Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", NeurIPS 2022. https://proceedings.nips.cc/paper_files/paper/2022/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf (accessed 2026-11-10)
[^s5]: Zelikman, Wu, Mu & Goodman, "STaR: Bootstrapping Reasoning With Reasoning", NeurIPS 2022. https://proceedings.neurips.cc/paper_files/paper/2022/hash/639a9a172c044fbb64175b5fad42e9a5-Abstract-Conference.html (accessed 2026-11-10)
[^s6]: Anthropic, "Extended thinking", Claude Platform documentation. https://platform.claude.com/docs/en/build-with-claude/extended-thinking.md (accessed 2026-11-10)
