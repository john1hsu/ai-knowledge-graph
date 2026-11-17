---
id: kt:mt-bench
type: Benchmark
title: MT-Bench
aliases: [MT-bench, Multi-Turn Benchmark, MT Bench]
domain: evaluation-and-benchmarks
summary: >-
  A benchmark of 80 two-turn, open-ended questions across eight categories, introduced by the LMSYS team
  (Zheng et al., NeurIPS 2023), that scores chat assistants on a 1–10 scale using GPT-4 as an automated judge.
maturity: established
broader: [kt:ai-evaluation]
related: [kt:chatbot-arena, kt:mmlu, kt:truthfulqa, kt:human-evaluation, kt:benchmark-contamination, kt:instruction-tuning]
relations:
  - {predicate: introducedIn, object: kt:judging-llm-as-a-judge-with-mt-bench-and-chatbot-arena}
  - {predicate: createdBy, object: kt:lmsys}
  - {predicate: dependsOn, object: kt:llm-as-a-judge}
  - {predicate: alternativeTo, object: kt:arena-hard}
sources:
  - id: s1
    title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
    publisher: "Advances in Neural Information Processing Systems 36 (NeurIPS 2023), Datasets and Benchmarks Track, pp. 46595–46623 (Zheng, Chiang, Sheng et al.)"
    url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues"
    publisher: "Proceedings of ACL 2024 (Volume 1: Long Papers), pp. 7421–7454 (Bai, Liu, Bu et al.)"
    url: https://aclanthology.org/2024.acl-long.401
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline"
    publisher: "arXiv 2406.11939v2 (Li, Chiang, Frick, Dunlap, Wu, Zhu, Gonzalez, Stoica); ICML 2025"
    url: https://arxiv.org/html/2406.11939v2
    type: primary
    accessed: 2026-11-17
created: 2026-11-17
---

# MT-Bench

**MT-Bench** is a small, hand-written benchmark for chat assistants that asks each model 80 open-ended questions, every one with a scripted follow-up, and has a strong language model grade the replies. It was released by the LMSYS group (Zheng, Chiang, Sheng and colleagues, including Gonzalez and Stoica) in the paper *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*, published in the NeurIPS 2023 Datasets and Benchmarks Track.[^s1] Its purpose was to measure what multiple-choice knowledge tests miss: whether an assistant follows instructions, holds a conversation across turns and writes useful free-form answers that people actually prefer.[^s1]

## Design

The question set has eight categories with ten manually written questions each: writing, roleplay, extraction, reasoning, math, coding, STEM knowledge, and humanities and social-science knowledge.[^s1] Each question has two turns. The second turn builds on the first, for example by asking the model to rewrite its answer under a new constraint or to re-explain a point more simply, so a model must keep track of context rather than answer a single isolated prompt.[^s1] The authors chose prompts that reflect common assistant use and that are hard enough to separate strong models from weaker ones.[^s1]

## Scoring

In the standard setup GPT-4 grades each answer on its own with a score from 1 to 10, and a model's MT-Bench score is the mean over all 160 turns.[^s1] For math, reasoning and coding the judge prompt also includes a reference solution, because the judge otherwise tended to be misled by plausible but wrong answers.[^s1] To check that the automated scores track human taste, the authors collected about 3K pairwise votes from 58 expert labelers, mostly graduate students, who each judged at least 20 randomly chosen multi-turn questions.[^s1] Strong judges such as GPT-4 agreed with these human preferences more than 80% of the time, roughly the level at which humans agree with each other.[^s1]

## Results and what it revealed

The paper's reference scores (GPT-4 as judge, reported in 2023) were 8.99 for GPT-4, 7.94 for GPT-3.5, 6.39 for Vicuna-13B and 2.61 for the base LLaMA-13B.[^s1] Comparing these with MMLU and TruthfulQA showed that the benchmarks measure different things. A LLaMA-7B fine-tuned on only about 3K selected conversations jumped from 2.74 to 5.95 on MT-Bench while its MMLU score barely moved (35.2 to 37.3), suggesting that light **instruction tuning** mostly changes conversational style and helpfulness rather than knowledge.[^s1] The authors therefore argued that a capability benchmark and a preference benchmark should be reported together.[^s1]

## Limitations

The creators list several limits. MT-Bench targets helpfulness only and largely ignores safety and honesty; it folds accuracy, relevance and creativity into a single number; and with 80 questions it is small.[^s1] Because grading relies on an LLM judge, it inherits that judge's position, verbosity and self-enhancement biases, which the paper mitigates but does not remove.[^s1]

Later work quantified the size problem. The same group's Arena-Hard paper (2024, ICML 2025) compared automatic benchmarks against Chatbot Arena rankings of the top 20 models. MT-Bench's Spearman correlation with the Arena was high at 89.9%, yet it confidently separated only 22.6% of model pairs and its confidence agreement with the Arena was 26.6%, against 87.4% and 90.9% for the 500-prompt Arena-Hard-Auto.[^s3] The authors note that rank correlation alone hides this, because it ignores the variance of the rankings.[^s3] In other words, MT-Bench orders models roughly correctly but too noisily to rank close competitors with confidence.[^s3]

Its two-turn format has also been judged too coarse for studying dialogue. MT-Bench-101 (ACL 2024) extends the idea to 1,388 multi-turn dialogues with 4,208 turns organised under a three-tier ability taxonomy of 13 tasks, and its evaluation of 21 models found that common alignment techniques had not clearly improved multi-turn ability.[^s2]

## Connections

MT-Bench is an instance of **AI evaluation** focused on open-ended chat, introduced in the **Judging LLM-as-a-Judge** paper and created by **LMSYS**, the team behind **Chatbot Arena**; the two were released together, with Arena's crowdsourced votes serving as the larger-scale human reference.[^s1] Its scores depend on **LLM-as-a-judge** grading, and its validity is anchored in **human evaluation** by expert labelers.[^s1] It was designed to complement fixed-answer benchmarks such as **MMLU** and **TruthfulQA**.[^s1] Because the 80 questions are public and fixed, they are exposed to **benchmark contamination** and saturation, problems that the LMSYS team's **Arena-Hard** benchmark, built from fresh crowdsourced prompts, was created to address as a more separable alternative.[^s3] MT-Bench-101 is a finer-grained extension focused on multi-turn dialogue.[^s2]

## Sources

[^s1]: Zheng, Chiang, Sheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", NeurIPS 2023 Datasets and Benchmarks Track. https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract.html (accessed 2026-11-17)
[^s2]: Bai, Liu, Bu et al., "MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues", ACL 2024. https://aclanthology.org/2024.acl-long.401 (accessed 2026-11-17)
[^s3]: Li, Chiang, Frick et al., "From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline", arXiv 2406.11939v2 (ICML 2025). https://arxiv.org/html/2406.11939v2 (accessed 2026-11-17)
