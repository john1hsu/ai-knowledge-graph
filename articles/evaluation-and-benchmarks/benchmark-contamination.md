---
id: kt:benchmark-contamination
type: Risk
title: Benchmark contamination
aliases: [data contamination, test set contamination, test-set leakage, evaluation data contamination]
domain: evaluation-and-benchmarks
summary: >-
  The presence of a benchmark's test data (or closely related material) in a model's training data, which
  inflates its measured score and can make evaluation results and the conclusions drawn from them invalid.
maturity: emerging
broader: [kt:ai-evaluation]
related: [kt:gsm8k, kt:mmlu, kt:goodharts-law, kt:overfitting, kt:membership-inference-attack, kt:livebench]
relations:
  - {predicate: dependsOn, object: kt:pretraining}
  - {predicate: contrastsWith, object: kt:data-poisoning}
sources:
  - id: s1
    title: "NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark"
    publisher: Findings of EMNLP 2023 (Sainz, Campos, García-Ferrero, Etxaniz, Lopez de Lacalle, Agirre)
    url: https://aclanthology.org/2023.findings-emnlp.722.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus"
    publisher: EMNLP 2021 (Dodge, Sap, Marasović, Agnew, Ilharco, Groeneveld, Mitchell, Gardner)
    url: https://aclanthology.org/2021.emnlp-main.98/
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s3
    title: "Proving Test Set Contamination in Black-Box Language Models"
    publisher: ICLR 2024 (Oren, Meister, Chatterji, Ladhak, Hashimoto)
    url: https://proceedings.iclr.cc/paper_files/paper/2024/hash/46e624c244cff669223d488defd4e835-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "Detecting Pretraining Data from Large Language Models"
    publisher: ICLR 2024 (Shi, Ajith, Xia, Huang, Liu, Blevins, Chen, Zettlemoyer)
    url: https://proceedings.iclr.cc/paper_files/paper/2024/hash/e32ad85fa27be4a9868d55703f01323e-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s5
    title: "A Careful Examination of Large Language Model Performance on Grade School Arithmetic"
    publisher: NeurIPS 2024 Datasets and Benchmarks Track (Zhang, Da, Lee et al.; Scale AI)
    url: https://proceedings.neurips.cc/paper_files/paper/2024/hash/53384f2090c6a5cac952c598fd67992f-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s6
    title: "LiveBench: A Challenging, Contamination-Limited LLM Benchmark"
    publisher: ICLR 2025 poster (White, Dooley, Roberts, Pal et al.)
    url: https://iclr.cc/virtual/2025/poster/28134
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Benchmark contamination

Benchmark contamination (also called data or test set contamination) occurs when material from an evaluation benchmark, most seriously its labelled test split, ends up in the data a model was trained on. The model is then partly graded on questions it has already seen, so its score overstates how well it handles genuinely new inputs.[^s1] Sainz and colleagues argued at EMNLP 2023 that the problem puts NLP evaluation "in trouble": contaminated models look better than clean ones, which can lead to wrong conclusions being published and valid ones being dismissed, and the true scale of the problem is unknown because it is hard to measure.[^s1]

## Why it happens

Large language models are pretrained on web-scale crawls, and public benchmarks live on the same web: in papers, GitHub repositories, dataset hubs and blog posts. An audit of the Colossal Clean Crawled Corpus (C4) found evaluation examples from other NLP benchmark datasets inside the training text (EMNLP 2021).[^s2] Because model developers rarely release full pretraining corpora, outside researchers usually cannot check directly whether a given benchmark was included.[^s3] Sainz et al. showed the practical consequence by prompting ChatGPT for the opening examples of the CoNLL-2003 training split, which it reproduced almost verbatim; they attributed this to the dataset having been uploaded to GitHub many times.[^s1]

## Kinds of contamination

Sainz et al. distinguish three levels.[^s1]

- **Guideline contamination:** the model saw the annotation guidelines, which matters mainly for zero- and few-shot claims.[^s1]
- **Raw-text contamination:** the model saw the source text a dataset was built from (for example the original web pages), but not the labels.[^s1]
- **Annotation contamination:** the model saw the labelled examples. Exposure of the test split invalidates the experiment; exposure of train or dev splits leaves supervised comparisons intact but undermines zero- and few-shot claims.[^s1]

A related, softer form arises when a model is tuned heavily on data resembling a benchmark, so it fits the benchmark's style rather than its items; the GSM8K case below shows both effects are hard to separate.[^s5]

## Detecting it

With access to the training corpus, the direct method is string or n-gram matching between benchmark items and pretraining text, reported as the share of a benchmark found in the data.[^s1] For closed models, detection has to work from outputs or probabilities:

- **Extraction probes:** prompt the model with some benchmark examples and check whether it regenerates the next ones; the extractable fraction serves as a contamination estimate. Failure to extract does not prove the data was unseen.[^s1]
- **Ordering tests:** Oren et al. note that an uncontaminated model should find every ordering of a benchmark's examples equally likely. A model that assigns markedly higher likelihood to the canonical published order than to shuffled orders has probably memorised it. Their test gives exact false-positive guarantees and worked with models as small as 1.4 billion parameters and test sets of 1,000 examples (ICLR 2024).[^s3]
- **Membership inference:** Shi et al.'s Min-K% Prob scores a text by its least likely tokens, on the idea that unseen text tends to contain a few low-probability outliers while seen text rarely does. It needs no reference model, improved on earlier methods by 7.4% on their WikiMIA benchmark, and was applied to flagging contaminated benchmark examples (ICLR 2024).[^s4]

## Evidence of impact

The clearest measurement of impact is to rebuild a benchmark from scratch and compare. Scale AI researchers wrote GSM1k, a 1,000-problem set matched to GSM8K on human solve rate, step count and answer size. Some leading models scored up to 8% lower on it, several model families showed systematic overfitting across sizes, and a model's probability of generating GSM8K examples correlated with its score gap (Spearman r² of 0.36). Many frontier models, however, showed little sign of overfitting (as reported at NeurIPS 2024).[^s5]

## Mitigations

Sainz et al. call for automatic detection tools, a shared registry of known contamination cases, and treatment of contamination during peer review.[^s1] Benchmark designers increasingly use freshness instead: LiveBench draws questions from recent maths competitions, arXiv papers and news, refreshes them monthly, and scores against objective answers rather than LLM judges or crowdsourcing. Its ICLR 2025 version reported top models below 70% accuracy, and its authors softened the title's claim from "contamination-free" to "contamination-limited".[^s6] Private held-out test sets and post-cutoff data are other common defences, though none gives a guarantee once a benchmark is public.[^s1][^s6]

## Connections

Benchmark contamination is a failure mode of **AI evaluation** (`broader`) and a concrete case of **Goodhart's law**: once a public score becomes the target, training data drifts toward it.[^s1][^s5] It **depends on** web-scale **pretraining**, whose undocumented corpora make leakage likely.[^s2] **GSM8K** and **MMLU** are widely studied examples, and the GSM1k results tie it to **overfitting**.[^s5] Its detection methods are forms of **membership inference**.[^s4] It **contrasts with** **data poisoning**: both concern what enters training data, but contamination is usually accidental and inflates scores, whereas poisoning is deliberate manipulation. **LiveBench** is a benchmark designed to limit it.[^s6]

## Sources

[^s1]: Sainz et al., "NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark", Findings of EMNLP 2023. https://aclanthology.org/2023.findings-emnlp.722.pdf (accessed 2026-11-12)
[^s2]: Dodge et al., "Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus", EMNLP 2021. https://aclanthology.org/2021.emnlp-main.98/ (accessed 2026-11-12)
[^s3]: Oren et al., "Proving Test Set Contamination in Black-Box Language Models", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/46e624c244cff669223d488defd4e835-Abstract-Conference.html (accessed 2026-11-12)
[^s4]: Shi et al., "Detecting Pretraining Data from Large Language Models", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/e32ad85fa27be4a9868d55703f01323e-Abstract-Conference.html (accessed 2026-11-12)
[^s5]: Zhang et al., "A Careful Examination of Large Language Model Performance on Grade School Arithmetic", NeurIPS 2024 Datasets and Benchmarks Track. https://proceedings.neurips.cc/paper_files/paper/2024/hash/53384f2090c6a5cac952c598fd67992f-Abstract.html (accessed 2026-11-12)
[^s6]: White et al., "LiveBench: A Challenging, Contamination-Limited LLM Benchmark", ICLR 2025. https://iclr.cc/virtual/2025/poster/28134 (accessed 2026-11-12)
