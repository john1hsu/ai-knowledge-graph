---
id: kt:gpqa
type: Benchmark
title: "GPQA: A Graduate-Level Google-Proof Q&A Benchmark"
aliases: [GPQA, GPQA Diamond, Google-Proof Q&A, Graduate-Level Google-Proof Q&A]
domain: evaluation-and-benchmarks
summary: >-
  A benchmark of 448 expert-written, four-option multiple-choice questions in biology, physics and chemistry,
  released by Rein et al. in 2023, designed so that PhD-level domain experts mostly answer correctly while skilled
  non-experts with unrestricted web access mostly fail; its 198-question Diamond subset became a standard test of
  frontier model reasoning.
maturity: established
broader: [kt:ai-evaluation]
related: [kt:scalable-oversight, kt:mmlu, kt:benchmark-contamination, kt:reasoning-models, kt:big-bench]
relations:
  - {predicate: introducedIn, object: kt:gpqa-a-graduate-level-google-proof-q-a-benchmark}
  - {predicate: createdBy, object: kt:david-rein}
  - {predicate: createdBy, object: kt:samuel-bowman}
  - {predicate: usedIn, object: kt:scalable-oversight}
sources:
  - id: s1
    title: "GPQA: A Graduate-Level Google-Proof Q&A Benchmark (arXiv:2311.12022 abstract page)"
    publisher: arXiv (Rein, Hou, Stickland, Petty, Pang, Dirani, Michael, Bowman; NYU, Cohere, Anthropic), November 2023
    url: https://arxiv.org/abs/2311.12022
    type: primary
    accessed: 2026-11-25
  - id: s2
    title: "GPQA: A Graduate-Level Google-Proof Q&A Benchmark (full paper PDF)"
    publisher: arXiv (Rein et al.), published at the First Conference on Language Modeling (COLM) 2024
    url: https://arxiv.org/pdf/2311.12022
    type: primary
    accessed: 2026-11-25
  - id: s3
    title: "idavidrein/gpqa: baselines, analysis code and dataset release"
    publisher: GitHub (David Rein)
    url: https://github.com/idavidrein/gpqa
    type: official-docs
    accessed: 2026-11-25
  - id: s4
    title: "GPQA Diamond (benchmark description and methodology)"
    publisher: Epoch AI Benchmarking Hub
    url: https://epoch.ai/benchmarks/gpqa-diamond
    type: primary
    accessed: 2026-11-25
  - id: s5
    title: "GPQA Diamond: What's left?"
    publisher: Epoch AI Gradient Updates (Greg Burnham), May 30, 2025
    url: https://epoch.ai/gradient-updates/gpqa-diamond-whats-left
    type: community
    accessed: 2026-11-25
  - id: s6
    title: "Independent AI Testing Authority Turns From Saturated Knowledge Benchmarks to Harder Business Tests"
    publisher: The Batch, DeepLearning.AI, January 30, 2026
    url: https://www.deeplearning.ai/the-batch/independent-ai-testing-authority-turns-from-saturated-knowledge-benchmarks-to-harder-business-tests
    type: news
    accessed: 2026-11-25
created: 2026-11-25
---

# GPQA: A Graduate-Level Google-Proof Q&A Benchmark

**GPQA** is a question-answering benchmark of 448 multiple-choice questions in biology, physics and chemistry, written and checked by people who hold or are pursuing PhDs in those fields.[^s1] It was introduced in November 2023 by David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael and Samuel R. Bowman, with affiliations at NYU, Cohere and Anthropic, and later appeared at the first Conference on Language Modeling (COLM 2024).[^s1][^s3] "Google-proof" names its central design goal: the questions should be hard to answer by searching the web. In the original study, experts reached 65% accuracy (74% after discounting mistakes they later acknowledged), while highly skilled non-experts managed only 34% despite averaging more than 30 minutes per question with unrestricted web access.[^s1]

## Motivation: a testbed for scalable oversight

The authors built GPQA less as a leaderboard than as an instrument for **scalable oversight** research. If future AI systems help answer questions that people cannot easily check, humans will need methods to supervise those answers reliably; GPQA supplies questions where ground truth is known to specialists but out of reach for capable non-experts, so oversight protocols can be tested realistically.[^s1] At release, the strongest GPT-4-based baseline scored 39%, close to the non-expert level and far below the experts.[^s1]

## How the dataset was built

Questions came from 61 contractors recruited through Upwork, each with a completed or in-progress PhD. Each item passed through four stages: writing, a first expert validation, revision by the writer, and a second expert validation, after which three non-expert validators (experts from *other* domains) attempted it with web access but no language-model assistants.[^s2] Non-experts had to spend at least 15 minutes per question and averaged about 37 minutes.[^s2] Pay was structured to reward the property the benchmark wants: writers earned bonuses when experts got their question right and when non-experts got it wrong, and validators were paid more for correct answers, giving an estimated average of about $95 per hour.[^s2]

The release has three nested subsets. **GPQA Extended** has 546 questions; the **main** set of 448 keeps items where experts largely agreed with the intended answer and non-experts mostly failed; and **GPQA Diamond**, 198 questions, keeps only items that both experts answered correctly (or where an expert's error was clearly a slip) and that at most one of the three non-experts got right.[^s2] Organic chemistry is the largest subdomain, followed by molecular biology and quantum mechanics.[^s2] On the paper's own figures, expert validators scored about 81% on Diamond against about 22% for non-experts, although those numbers are inflated and deflated respectively by the selection rule itself.[^s2]

## Guarding against contamination

Because a public benchmark can leak into pretraining data, the authors asked users not to post examples in plain text or images online, distributed the data as a password-protected archive, and embedded a canary string (a superset of the BIG-bench canary) so that model developers can filter it from training corpora.[^s2][^s3] The repository is MIT-licensed and includes zero-shot, few-shot, chain-of-thought and retrieval-augmented baselines for GPT-3.5 and GPT-4, plus a form for reporting erroneous questions.[^s3]

## Use, saturation and critiques

GPQA Diamond quickly became a headline reasoning metric for frontier models. Epoch AI's benchmarking hub runs it with a standard step-by-step prompt that requires a final answer letter, scores unformatted answers as wrong (so some results fall below the 25% chance rate), and notes OpenAI's report that recruited PhD experts scored 69.7% on Diamond.[^s4] Scores rose quickly: by May 2025 Epoch's Greg Burnham observed that state-of-the-art results clustered around 83%, and Epoch's own evaluation of Grok 4 in July 2025 reported 87% (±2%).[^s5][^s4] Burnham examined the questions that strong models still missed and found they were concentrated in organic chemistry; he estimated that at least 90% of Diamond is valid, with a rough extrapolation putting flawed items near 8%, and argued that future science benchmarks should move beyond multiple choice.[^s5] As of January 2026, Artificial Analysis kept GPQA Diamond in version 4.0 of its Intelligence Index while dropping other knowledge and coding tests it judged saturated.[^s6]

The main limitations are visible in the design: the set is small, so a single question moves Diamond scores by about half a percentage point; the four-option format allows elimination strategies and guessing; and expert validators recruited through a freelance platform are an imperfect stand-in for the questions a superhuman system might face.[^s2][^s5]

## Connections

GPQA is a specific instrument within **AI evaluation** (`broader`). It was introduced in the paper *GPQA: A Graduate-Level Google-Proof Q&A Benchmark* (`introducedIn`) by a team led by David Rein with Samuel R. Bowman as a senior author (`createdBy`).[^s1] Its stated purpose ties it to **scalable oversight** (`usedIn`), where expert-vs-non-expert gaps let researchers test whether a supervision method lets non-experts approach specialist accuracy.[^s1] It is often reported alongside **MMLU**, which tests breadth across 57 subjects rather than depth in three sciences, and it became a standard benchmark for **reasoning models**.[^s4][^s5] Its password-protected release and canary string, borrowed from **BIG-bench**, are responses to **benchmark contamination**.[^s2][^s3]

## Sources
[^s1]: Rein et al., "GPQA: A Graduate-Level Google-Proof Q&A Benchmark", arXiv:2311.12022, November 2023. https://arxiv.org/abs/2311.12022 (accessed 2026-11-25)
[^s2]: Rein et al., "GPQA: A Graduate-Level Google-Proof Q&A Benchmark" (full paper), COLM 2024. https://arxiv.org/pdf/2311.12022 (accessed 2026-11-25)
[^s3]: David Rein, "idavidrein/gpqa", GitHub. https://github.com/idavidrein/gpqa (accessed 2026-11-25)
[^s4]: Epoch AI, "GPQA Diamond", Benchmarking Hub. https://epoch.ai/benchmarks/gpqa-diamond (accessed 2026-11-25)
[^s5]: Greg Burnham, "GPQA Diamond: What's left?", Epoch AI Gradient Updates, May 30, 2025. https://epoch.ai/gradient-updates/gpqa-diamond-whats-left (accessed 2026-11-25)
[^s6]: "Independent AI Testing Authority Turns From Saturated Knowledge Benchmarks to Harder Business Tests", The Batch, DeepLearning.AI, January 30, 2026. https://www.deeplearning.ai/the-batch/independent-ai-testing-authority-turns-from-saturated-knowledge-benchmarks-to-harder-business-tests (accessed 2026-11-25)
