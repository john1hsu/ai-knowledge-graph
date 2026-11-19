---
id: kt:big-bench
type: Benchmark
title: BIG-bench
aliases: [Beyond the Imitation Game Benchmark, BIG-Bench]
domain: evaluation-and-benchmarks
summary: >-
  A collaborative benchmark of more than 200 language tasks, contributed by over 400 researchers and
  published in 2022 (Srivastava et al.), built to probe abilities thought to be beyond language models and to
  study how their capabilities change with scale.
maturity: established
broader: [kt:ai-evaluation]
related: [kt:emergent-abilities, kt:scaling-laws, kt:benchmark-contamination, kt:mmlu, kt:chain-of-thought]
relations:
  - {predicate: introducedIn, object: kt:beyond-the-imitation-game-quantifying-and-extrapolating-the-capabilities-of-language-models}
  - {predicate: hasPart, object: kt:big-bench-hard}
  - {predicate: influencedBy, object: kt:turing-test}
sources:
  - id: s1
    title: "Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models (arXiv:2206.04615v3)"
    publisher: arXiv (Srivastava et al.)
    url: https://arxiv.org/pdf/2206.04615v3.pdf
    type: primary
    accessed: 2026-11-19
  - id: s2
    title: "Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models"
    publisher: Google Research publications
    url: https://research.google/pubs/beyond-the-imitation-game-quantifying-and-extrapolating-the-capabilities-of-language-models/
    type: lab-research
    accessed: 2026-11-19
  - id: s3
    title: "BIG-bench repository README"
    publisher: google/BIG-bench on GitHub
    url: https://raw.githubusercontent.com/google/BIG-bench/main/README.md
    type: primary
    accessed: 2026-11-19
  - id: s4
    title: "Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them"
    publisher: "Findings of ACL 2023, pp. 13003–13051 (Suzgun et al.)"
    url: https://aclanthology.org/2023.findings-acl.824
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s5
    title: "BIG-Bench Extra Hard"
    publisher: "ACL 2025, Volume 1 (Long Papers), pp. 26473–26501 (Kazemi et al.)"
    url: https://aclanthology.org/2025.acl-long.1285
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s6
    title: "Are Emergent Abilities of Large Language Models a Mirage?"
    publisher: NeurIPS 2023 (Schaeffer, Miranda, Koyejo)
    url: https://papers.neurips.cc/paper_files/paper/2023/file/adc98a266f45005c403b8311ca7e8bd7-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-11-19
created: 2026-11-19
---

# BIG-bench

**BIG-bench** (the Beyond the Imitation Game Benchmark) is a large, crowd-sourced suite of tasks for evaluating language models, released with the 2022 paper "Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models" by Aarohi Srivastava and several hundred co-authors.[^s1][^s2] Its name nods to Turing's imitation game: instead of asking whether a machine can pass for a human, it asks which concrete abilities models have, how those abilities grow with scale, and which remain out of reach.[^s1] The final paper describes 204 tasks from about 450 authors at 132 institutions (an earlier abstract cited 207 tasks), and the repository records publication in Transactions on Machine Learning Research (TMLR) in 2023.[^s1][^s2][^s3]

## Construction
Tasks were contributed through pull requests to a public GitHub repository and span linguistics, child development, mathematics, common-sense reasoning, biology, physics, social bias and software development, among other areas, chosen to target abilities believed to exceed models of the time.[^s2][^s3] About 80% are **JSON tasks**, defined by a file of input and target examples and scored with metrics such as multiple-choice grade or exact string match; the remaining 20% are **programmatic tasks** written in Python, which can query a model over several rounds and adapt later queries to earlier answers.[^s1][^s3] Because the full suite is costly to run, the authors defined **BIG-bench Lite**, a curated subset of 24 JSON tasks with its own leaderboard.[^s1][^s3] Every task file also carries a fixed canary string so that the data can be detected and filtered out of web-scraped training corpora.[^s1][^s3]

## Original findings
The paper evaluated Google's dense decoder-only BIG-G models, sparse mixture-of-experts variants with 32 experts per layer and top-2 routing, and eight OpenAI GPT-3-series models from 125M to 175B non-embedding parameters, with PaLM results added from a separate report; expert human raters supplied a comparison baseline.[^s1] Its main conclusions were:[^s1][^s2]
- Aggregate performance and calibration improve with model size and number of shots, but stay weak in absolute terms and far below expert raters.
- Model families perform similarly; sparse models matched dense ones with roughly twice the effective parameter count, and were better calibrated.
- Tasks that improve smoothly with scale tend to rely on knowledge or memorisation, while tasks with sudden "breakthrough" gains tend to need multi-step reasoning; about 5% of tasks showed breakthrough behaviour, and the choice of metric affected whether a curve looked gradual or sudden.
- Social bias usually grew with scale in ambiguous contexts, shrank in unambiguous ones, and could be reduced by prompting.

## Successors and critiques
BIG-bench's few-shot protocol turned out to understate models. Suzgun et al. selected 23 tasks on which earlier models had not beaten the average human rater, calling them **BIG-Bench Hard (BBH)**; with chain-of-thought prompting, PaLM surpassed the average rater on 10 of them and Codex (code-davinci-002) on 17.[^s4] By 2025 BBH had itself saturated, so Kazemi et al. replaced each BBH task with a harder one testing a similar skill in **BIG-Bench Extra Hard**, where, as reported in the ACL 2025 paper, the best general-purpose model scored 23.9% and the best reasoning-specialised model 54.2%.[^s5]

BIG-bench was also the main dataset behind claims of emergent abilities, and the same data fuelled a rebuttal. Schaeffer, Miranda and Koyejo found that two discontinuous or nonlinear metrics, multiple-choice grade and exact string match, accounted for more than 92% of claimed emergent abilities on BIG-bench, and that switching LaMDA's scoring to the continuous Brier score made the apparent jumps disappear.[^s6] Like any public test set, it is exposed to contamination; the canary string is a mitigation that works only if model developers actually filter on it.[^s1][^s3]

## Connections
BIG-bench is a large, collaborative instance of **AI evaluation**, introduced in the *Beyond the Imitation Game* paper and named in reference to the **Turing test**.[^s1] Its scaling curves underpin discussion of **emergent abilities** and of **scaling laws** applied to downstream tasks, and its breakthrough-versus-linear analysis is the empirical case that later critiques re-examined.[^s1][^s6] It contains the 23-task **BIG-Bench Hard** subset, a standard target for **chain-of-thought** studies.[^s4] Its canary string is an early, explicit defence against **benchmark contamination**.[^s3] It is a contemporary of **MMLU**: both are broad multi-domain suites, but MMLU is uniform multiple-choice while BIG-bench mixes formats, metrics and interactive tasks.[^s1][^s3]

## Sources
[^s1]: Srivastava et al., "Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models", arXiv:2206.04615v3. https://arxiv.org/pdf/2206.04615v3.pdf (accessed 2026-11-19)
[^s2]: Google Research, publication page for "Beyond the Imitation Game" (2022). https://research.google/pubs/beyond-the-imitation-game-quantifying-and-extrapolating-the-capabilities-of-language-models/ (accessed 2026-11-19)
[^s3]: google/BIG-bench repository README. https://raw.githubusercontent.com/google/BIG-bench/main/README.md (accessed 2026-11-19)
[^s4]: Suzgun et al., "Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them", Findings of ACL 2023, pp. 13003–13051. https://aclanthology.org/2023.findings-acl.824 (accessed 2026-11-19)
[^s5]: Kazemi et al., "BIG-Bench Extra Hard", ACL 2025 (Long Papers), pp. 26473–26501. https://aclanthology.org/2025.acl-long.1285 (accessed 2026-11-19)
[^s6]: Schaeffer, Miranda and Koyejo, "Are Emergent Abilities of Large Language Models a Mirage?", NeurIPS 2023. https://papers.neurips.cc/paper_files/paper/2023/file/adc98a266f45005c403b8311ca7e8bd7-Paper-Conference.pdf (accessed 2026-11-19)
