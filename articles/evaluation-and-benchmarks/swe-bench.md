---
id: kt:swe-bench
type: Benchmark
title: SWE-bench
aliases: [SWE-Bench, SWE-bench Verified, SWE-bench Lite, Software Engineering Benchmark]
domain: evaluation-and-benchmarks
summary: >-
  A benchmark of 2,294 real GitHub issues from 12 popular Python repositories in which a model must edit
  the codebase to resolve each issue, graded by running the repository's own unit tests; introduced by
  Princeton researchers at ICLR 2024 and now a standard yardstick for coding agents.
maturity: established
broader: [kt:ai-evaluation]
related: [kt:large-language-model, kt:ai-agent, kt:tool-use, kt:benchmark-contamination, kt:test-time-compute, kt:swe-agent]
relations:
  - {predicate: introducedIn, object: kt:swe-bench-can-language-models-resolve-real-world-github-issues}
  - {predicate: createdBy, object: kt:princeton-university}
sources:
  - id: s1
    title: "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
    publisher: arXiv:2310.06770 (Jimenez, Yang, Wettig, Yao, Pei, Press, Narasimhan), v2 April 2024
    url: https://arxiv.org/abs/2310.06770v2
    type: primary
    accessed: 2026-11-13
  - id: s2
    title: "SWE-Bench: Can Language Models Resolve Real-World GitHub Issues? (ICLR 2024)"
    publisher: ML Anthology, ICLR 2024 proceedings record
    url: https://mlanthology.org/iclr/2024/jimenez2024iclr-swebench
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "Introducing SWE-bench Verified"
    publisher: OpenAI, 13 August 2024 (updated 24 February 2025)
    url: https://openai.com/index/introducing-swe-bench-verified/
    type: lab-research
    accessed: 2026-11-13
  - id: s4
    title: "SWE-bench/SWE-bench (benchmark and evaluation harness repository)"
    publisher: SWE-bench maintainers on GitHub
    url: https://github.com/SWE-bench/SWE-bench
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "princeton-nlp/SWE-bench_Lite dataset card"
    publisher: Hugging Face Datasets
    url: https://huggingface.co/datasets/princeton-nlp/SWE-bench_Lite/blob/main/README.md
    type: official-docs
    accessed: 2026-11-13
  - id: s6
    title: "SWE-Bench+: Enhanced Coding Benchmark for LLMs"
    publisher: arXiv:2410.06992 (Aleithan, Xue, Mohajer, Nnorom, Uddin, Wang), October 2024
    url: https://arxiv.org/abs/2410.06992v2
    type: preprint
    accessed: 2026-11-13
created: 2026-11-13
---

# SWE-bench

SWE-bench is a benchmark that asks a language model to act like a software engineer: given a real code repository and a GitHub issue describing a bug or feature request, it must produce an edit to the codebase that resolves the issue.[^s1] The original test set contains 2,294 problems drawn from 12 popular open-source Python repositories.[^s1] It was introduced by Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press and Karthik Narasimhan, first posted in October 2023 and published at ICLR 2024.[^s1][^s2]

## How it works

Each task instance pairs an issue with the repository snapshot just before the pull request that fixed it. The Hugging Face dataset card lists the fields: the `problem_statement` (issue title and body), the `base_commit`, the gold `patch` from the merged PR with test code removed, and a separate `test_patch` holding the tests that PR added.[^s5] Grading is execution-based. `FAIL_TO_PASS` lists tests tied to the issue that should fail before the fix and pass after it. `PASS_TO_PASS` lists tests that must pass both before and after, so a fix that breaks other behaviour is rejected.[^s5] A task counts as resolved only if the model's patch applies cleanly and both sets of tests pass. The headline metric is the percentage of instances resolved.[^s1]

The official harness runs each evaluation in Docker containers so environments are reproducible. A `swebench eval` command takes a file of predicted patches and reports per-instance results. The maintainers recommend an x86_64 machine with about 120 GB of free disk, 16 GB of RAM and 8 cores, and cloud evaluation through Modal is also offered.[^s4]

## Variants

- **SWE-bench (full):** the original 2,294-instance test set.[^s1]
- **SWE-bench Lite:** a 300-instance test split plus a 23-instance dev split, built to make evaluation cheaper.[^s5]
- **SWE-bench Verified:** 500 instances screened by human engineers, released with OpenAI in August 2024.[^s3]
- **SWE-bench Multimodal:** issues from visual software domains, accepted at ICLR 2025; its version 2 offers 480 tasks for local evaluation.[^s4]

## Results and limitations

The benchmark was hard when it launched. The best model in the paper, Claude 2, resolved only 1.96% of issues, and models solved mainly the simplest ones.[^s1] Scores rose quickly once agent scaffolds arrived. In April 2024 the same group released SWE-agent, which they described as state of the art on the full test set.[^s4]

Data quality soon became the main critique. OpenAI's Preparedness team had 93 Python developers label 1,699 random samples three times each. They found underspecified issues, unit tests too specific or unrelated to the issue, and environments that could fail regardless of the fix. They filtered out 68.3% of the samples, a cut OpenAI itself calls likely overly strict.[^s3] The 500 surviving tasks became SWE-bench Verified. On Verified, GPT-4o with the Agentless scaffold resolved 33.2%, compared with 16% on the original set (as reported by OpenAI in August 2024).[^s3]

An independent audit by Aleithan et al. (October 2024) studied passing patches from SWE-agent with GPT-4. In 32.67% of them, the solution already appeared in the issue report or its comments. Another 31.08% passed because the tests were too weak to catch incorrect fixes.[^s6] Filtering those cases cut the reported resolution rate from 12.47% to 3.97%. The authors also found that over 94% of issues predate the models' knowledge cutoffs, which raises contamination concerns.[^s6] Because every task is Python and drawn from a few repositories, scores also say little about other languages or about engineering work beyond issue-sized fixes.[^s1][^s6]

## In practice

SWE-bench Verified is now a standard yardstick for coding models and agents. AI labs and agent builders report scores on it, and the maintainers keep a public leaderboard with official submissions in a separate experiments repository.[^s3][^s4] The repository also ships tooling to collect new task instances from other repositories.[^s4] Comparisons depend heavily on the scaffold, retrieval method and number of attempts, so a score describes a whole system, not a bare model.[^s3]

## Connections

SWE-bench is a benchmark within **AI evaluation**, and it tests **large language models** acting as **AI agents**, which rely on **tool use** to navigate, edit and test a repository.[^s1][^s4] It was introduced in the ICLR 2024 paper *SWE-bench: Can Language Models Resolve Real-World GitHub Issues?* by Jimenez et al., with the dataset released under Princeton NLP, and its authors later built **SWE-agent** on top of it.[^s2][^s4] Its public, pre-cutoff GitHub data makes it a case study in **benchmark contamination** and solution leakage.[^s6] Because grading runs each repository's own tests automatically, the benchmark also suits **test-time compute** methods that sample many candidate patches and check them.[^s5]

## Sources

[^s1]: Jimenez et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", arXiv:2310.06770v2. https://arxiv.org/abs/2310.06770v2 (accessed 2026-11-13)
[^s2]: ML Anthology, ICLR 2024 record for SWE-Bench. https://mlanthology.org/iclr/2024/jimenez2024iclr-swebench (accessed 2026-11-13)
[^s3]: OpenAI, "Introducing SWE-bench Verified", 2024 (updated 2025). https://openai.com/index/introducing-swe-bench-verified/ (accessed 2026-11-13)
[^s4]: SWE-bench maintainers, SWE-bench GitHub repository. https://github.com/SWE-bench/SWE-bench (accessed 2026-11-13)
[^s5]: Hugging Face, princeton-nlp/SWE-bench_Lite dataset card. https://huggingface.co/datasets/princeton-nlp/SWE-bench_Lite/blob/main/README.md (accessed 2026-11-13)
[^s6]: Aleithan et al., "SWE-Bench+: Enhanced Coding Benchmark for LLMs", arXiv:2410.06992v2. https://arxiv.org/abs/2410.06992v2 (accessed 2026-11-13)
