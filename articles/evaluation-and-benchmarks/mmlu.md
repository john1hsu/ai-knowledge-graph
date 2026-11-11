---
id: kt:mmlu
type: Benchmark
title: "MMLU: Measuring Massive Multitask Language Understanding"
aliases: [MMLU, Massive Multitask Language Understanding, MMLU benchmark, Hendrycks Test]
domain: evaluation-and-benchmarks
summary: >-
  A multiple-choice benchmark of 57 subjects, from elementary mathematics to professional law, introduced by
  Hendrycks et al. at ICLR 2021 to measure the breadth of knowledge and problem solving a language model picks up in pretraining.
maturity: established
broader: [kt:ai-evaluation]
related: [kt:large-language-model, kt:benchmark-contamination, kt:prompt-sensitivity, kt:emergent-abilities, kt:truthfulqa]
relations:
  - {predicate: createdBy, object: kt:dan-hendrycks}
  - {predicate: supersededBy, object: kt:mmlu-pro}
sources:
  - id: s1
    title: "Measuring Massive Multitask Language Understanding (ICLR 2021 poster)"
    publisher: ICLR 2021 (Hendrycks, Burns, Basart, Zou, Mazeika, Song, Steinhardt)
    url: https://iclr.cc/virtual/2021/poster/2962
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "Measuring Massive Multitask Language Understanding (arXiv:2009.03300, HTML version)"
    publisher: arXiv / ar5iv (Hendrycks et al.)
    url: https://ar5iv.labs.arxiv.org/html/2009.03300
    type: primary
    accessed: 2026-11-11
  - id: s3
    title: "Are We Done with MMLU?"
    publisher: "NAACL 2025, Volume 1 (Long Papers), pp. 5069–5096 (Gema et al.)"
    url: https://aclanthology.org/2025.naacl-long.262
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark"
    publisher: NeurIPS 2024 Datasets and Benchmarks Track (Wang et al.)
    url: https://neurips.cc/virtual/2024/poster/97435
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "MMLU-Pro (arXiv:2406.01574v4, HTML version)"
    publisher: arXiv (Wang et al.; Waterloo, Toronto, CMU)
    url: https://arxiv.org/html/2406.01574v4
    type: primary
    accessed: 2026-11-11
  - id: s6
    title: "AI Index Report 2025, Chapter 2: Technical Performance"
    publisher: Stanford Institute for Human-Centered AI (HAI)
    url: https://hai-production.s3.amazonaws.com/files/hai_ai-index-report-2025_chapter2_final.pdf
    type: academic
    accessed: 2026-11-11
created: 2026-11-11
---

# MMLU: Measuring Massive Multitask Language Understanding

**MMLU** (Massive Multitask Language Understanding) is a benchmark that tests how much academic and professional knowledge a text model can apply, using four-option multiple-choice questions across 57 subjects such as elementary mathematics, US history, computer science and law. It was introduced by Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song and Jacob Steinhardt in a 2020 preprint and presented at ICLR 2021.[^s1][^s2] Its premise was that a model which has absorbed broad world knowledge in pretraining should be able to answer exam-style questions without task-specific training, so it is scored in zero-shot and few-shot settings rather than after fine-tuning.[^s2]

## Construction and format
The 57 tasks are grouped into four areas: humanities, social sciences, STEM and "other" (for example professional medicine, business and global facts).[^s2] The 15,908 questions are split into a few-shot development set of five questions per subject, a validation set of 1,540 questions and a test set of 14,079, with at least 100 test questions per subject.[^s2] Random guessing scores 25%. The standard protocol shows the model up to five worked examples from the development set and then asks it to pick A, B, C or D; the headline metric is accuracy averaged across subjects.[^s2]

## Original results
In the 2020 paper, most models scored close to chance. The largest GPT-3 model (175B parameters) averaged 43.9% few-shot and about 37.7% zero-shot, while smaller GPT-3 variants stayed near 25%; UnifiedQA, an 11B model transferred from other QA data, reached 48.9%.[^s2] The authors estimated that non-expert crowd workers scored 34.5% and that expert-level accuracy would be about 89.8%.[^s2] They highlighted three weaknesses: performance was lopsided (GPT-3 scored roughly 69% on US foreign policy but 26% on college chemistry), calculation-heavy STEM subjects and socially important areas such as morality and law were near chance, and the model's confidence was poorly calibrated, differing from its accuracy by up to 24 points zero-shot.[^s1][^s2]

## Role in the LLM era
Broad, cheap to run and summarised as one number, MMLU became a standard headline score for new language models, and its scores rose quickly: GPT-4 reached 86.4% in March 2023, and the Stanford AI Index reports that the highest recorded score, 92.3%, came from OpenAI's o1-preview in September 2024, as claimed by the developer.[^s6] The same report notes that the gap between leading US and Chinese models on MMLU shrank from 17.5 points at the end of 2023 to 0.3 points at the end of 2024, and lists MMLU among the "traditional" benchmarks whose saturation pushed researchers toward harder tests.[^s6]

## Critiques and limitations
- **Label errors.** Gema et al. manually re-annotated questions and built MMLU-Redux, 5,700 checked questions across all 57 subjects; they found that 57% of the analysed Virology questions contained errors, and that re-scoring on corrected items can change model rankings.[^s3]
- **Saturation.** The MMLU-Pro authors argued that progress had plateaued after GPT-4, with frontier models of early to mid 2024 clustered around 86–87%, leaving little room to separate them.[^s5]
- **Prompt sensitivity.** The same study measured score swings of about 4–5% on MMLU across 24 prompt styles, with a peak near 11%, which is comparable to the gaps between competing models.[^s4][^s5]
- **Format limits.** Four-option questions reward elimination and recognition more than multi-step reasoning; chain-of-thought prompting barely changed GPT-4-class scores on MMLU but added 15–19 points on the harder MMLU-Pro.[^s5]

## Successors
**MMLU-Pro** (NeurIPS 2024 Datasets and Benchmarks Track) merges the subjects into 14 disciplines, raises the options from four to ten, removes trivial and noisy items and adds reasoning-heavy questions; models scored 16–33% lower than on MMLU, and score variation across prompts fell to about 2%.[^s4] By the 2025 AI Index, DeepSeek-R1 held the top reported MMLU-Pro score at 84.0%, while harder evaluations such as GPQA and Humanity's Last Exam had taken over as frontier knowledge tests.[^s6]

## Connections
MMLU sits under **AI evaluation** as one of its canonical static benchmarks, and is built to probe what **large language models** learn in pretraining.[^s2] Its original results, with smaller GPT-3 models near chance and only the largest well above it, are an early example of the scale-dependent jumps discussed under **emergent abilities**.[^s2] It is a standard case study for label noise and for **prompt sensitivity**, since small template changes move its scores, and as a long-public test set it is a natural target for **benchmark contamination** checks.[^s3][^s5] It is a sibling of **TruthfulQA**, another multiple-choice knowledge benchmark from the same period, and appears alongside GSM8K and HumanEval in the AI Index's list of saturated benchmarks.[^s6] It was **created by** Dan Hendrycks and colleagues and has been **superseded** for frontier comparisons by **MMLU-Pro**.[^s1][^s4]

## Sources
[^s1]: Hendrycks et al., "Measuring Massive Multitask Language Understanding", ICLR 2021 poster page. https://iclr.cc/virtual/2021/poster/2962 (accessed 2026-11-11)
[^s2]: Hendrycks et al., "Measuring Massive Multitask Language Understanding", arXiv:2009.03300. https://ar5iv.labs.arxiv.org/html/2009.03300 (accessed 2026-11-11)
[^s3]: Gema et al., "Are We Done with MMLU?", NAACL 2025, pp. 5069–5096. https://aclanthology.org/2025.naacl-long.262 (accessed 2026-11-11)
[^s4]: Wang et al., "MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark", NeurIPS 2024 Datasets and Benchmarks Track. https://neurips.cc/virtual/2024/poster/97435 (accessed 2026-11-11)
[^s5]: Wang et al., "MMLU-Pro", arXiv:2406.01574v4. https://arxiv.org/html/2406.01574v4 (accessed 2026-11-11)
[^s6]: Stanford HAI, "AI Index Report 2025", Chapter 2: Technical Performance. https://hai-production.s3.amazonaws.com/files/hai_ai-index-report-2025_chapter2_final.pdf (accessed 2026-11-11)
