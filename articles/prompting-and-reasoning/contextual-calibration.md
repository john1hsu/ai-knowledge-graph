---
id: kt:contextual-calibration
type: Technique
title: Contextual calibration
aliases: [calibrate before use, content-free calibration]
domain: prompting-and-reasoning
summary: >-
  A training-free correction for few-shot and zero-shot prompting that measures a language model's
  built-in preference for certain answers by scoring a content-free input such as "N/A", then rescales
  the output probabilities so that this input would receive a uniform prediction over labels.
maturity: established
broader: [kt:in-context-learning, kt:prompt-engineering]
related: [kt:few-shot-prompting, kt:zero-shot-prompting, kt:batch-calibration]
relations:
  - {predicate: mitigates, object: kt:prompt-sensitivity}
  - {predicate: introducedIn, object: kt:calibrate-before-use-improving-few-shot-performance-of-language-models}
  - {predicate: basedOn, object: kt:language-models-are-few-shot-learners}
sources:
  - id: s1
    title: "Calibrate Before Use: Improving Few-shot Performance of Language Models"
    publisher: ICML 2021, PMLR vol. 139, pp. 12697-12706 (Zhao, Wallace, Feng, Klein, Singh)
    url: https://proceedings.mlr.press/v139/zhao21c.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "Calibrate Before Use: Improving Few-Shot Performance of Language Models (arXiv v2)"
    publisher: arXiv 2102.09690v2 (Zhao, Wallace, Feng, Klein, Singh)
    url: https://arxiv.org/abs/2102.09690v2
    type: primary
    accessed: 2026-11-18
  - id: s3
    title: "Calibrate Before Use (full text, ar5iv rendering of arXiv 2102.09690)"
    publisher: ar5iv / arXiv (Zhao et al.)
    url: https://ar5iv.labs.arxiv.org/html/2102.09690
    type: primary
    accessed: 2026-11-18
  - id: s4
    title: "Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering"
    publisher: ICLR 2024 (Zhou, Wan, Proleev, Mincu, Chen, Heller, Roy)
    url: https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s5
    title: "Batch calibration: Rethinking calibration for in-context learning and prompt engineering"
    publisher: Google Research blog (Han Zhou, Subhrajit Roy), October 2023
    url: https://research.google/blog/batch-calibration-rethinking-calibration-for-in-context-learning-and-prompt-engineering/
    type: lab-research
    accessed: 2026-11-18
  - id: s6
    title: "Mitigating Label Biases for In-context Learning"
    publisher: arXiv 2305.19148v3 (Fei, Hou, Chen, Bosselut); ACL 2023 main conference
    url: https://arxiv.org/abs/2305.19148v3
    type: primary
    accessed: 2026-11-18
created: 2026-11-18
---

# Contextual calibration

**Contextual calibration** is an inference-time fix for the instability of prompting large language models on classification-style tasks. It was introduced by Tony Z. Zhao, Eric Wallace, Shi Feng, Dan Klein and Sameer Singh in "Calibrate Before Use", first posted to arXiv in February 2021 and published at ICML 2021.[^s1][^s2] The method needs no labelled data and no gradient updates: it estimates which answers the model is predisposed to give in a particular prompt, then divides that predisposition out of every prediction.[^s2]

## The problem it targets

Zhao et al. studied few-shot prompting of GPT-3 and GPT-2 and found that accuracy swung widely with the prompt format, the choice of demonstrations and their order. On the SST-2 sentiment task, merely permuting the same examples moved GPT-3 from 54.3% to 93.4% accuracy.[^s3] They traced much of this to three biases in the model's output distribution:[^s3]

- **Majority label bias:** answers that appear more often among the demonstrations are favoured.[^s3]
- **Recency bias:** answers that appear near the end of the prompt are favoured.[^s3]
- **Common token bias:** answers that are frequent in pretraining text are favoured; on DBPedia the model chose "book" far more often than "artist".[^s3]

Because these biases mainly shift the output distribution rather than destroy the model's ability to discriminate, the authors argued that shifting it back should recover much of the lost accuracy.[^s3]

## How it works

The method has three steps.[^s3]

1. **Probe the bias.** Insert a *content-free* test input into the same prompt (the paper averages "N/A", "[MASK]" and the empty string) and record the probabilities $\hat{p}_{cf}$ the model gives each label word.[^s3]
2. **Fit the correction.** Apply an affine transform $\hat{q} = \mathrm{softmax}(W\hat{p} + b)$ with $W = \mathrm{diag}(\hat{p}_{cf})^{-1}$ and $b = 0$, chosen so that the content-free input would score uniformly across labels.[^s3]
3. **Predict.** For each real input, apply the same $W$ and $b$ to the model's label probabilities and take the argmax.[^s3]

As a toy example, if a sentiment prompt makes the model give "positive" 0.7 and "negative" 0.3 on "N/A", a later test input scored 0.6/0.4 is rescaled to roughly 0.86/1.33 before normalising, and the prediction flips to "negative". The paper works on probabilities rather than logits because the GPT-3 API exposed only probabilities. For open-ended generation it calibrates only the first output token with a diagonal $W$, and notes that an additive variant ($W = I$, $b = -\hat{p}_{cf}$) works better there.[^s3]

## Evidence

Across text classification (SST-2, TREC, CB, RTE, AGNews, DBPedia), fact retrieval (LAMA) and slot extraction (ATIS, MIT Movies), on GPT-3 at 2.7B, 13B and 175B parameters and on GPT-2, contextual calibration raised average accuracy by up to 30 absolute points and reduced the variance across prompt formats and example choices.[^s2][^s3] The cost is one or a few extra forward passes per prompt template.[^s3]

## Limitations and successors

The method rests on the assumption that a content-free string is neutral, and later work showed it often is not. Zhou et al. found that in two-sentence tasks such as natural language inference, the model can treat an "N/A" premise as matching an "N/A" hypothesis, skewing the estimate toward "entailment"; contextual calibration failed more often on paraphrase and NLI tasks in their PaLM 2 experiments.[^s4] Their *batch calibration* replaces the content-free probe with the mean label probabilities over a batch of unlabelled test inputs, and Google Research reported about 3% average improvement over contextual calibration on PaLM 2-L across 13 language tasks (as of the 2023 study).[^s4][^s5] Fei et al. identified a further *domain-label bias*, where the task's vocabulary itself pushes the model toward some labels, and proposed estimating bias from random in-domain words instead, reporting gains of up to 37% macro-F1 on GPT-J and GPT-3 for strongly affected tasks.[^s6] Contextual calibration also needs access to per-label probabilities, which some chat-model APIs do not expose, and the published evidence comes from 2021–2023 base models; how much it helps current instruction-tuned models should be measured rather than assumed.[^s3][^s4]

## Connections

Contextual calibration is a technique within **in-context learning** and **prompt engineering** (broader), since it changes how a prompted model's outputs are read rather than the model itself.[^s2] It **mitigates prompt sensitivity**, the brittleness to format and ordering that Zhao et al. documented.[^s1] It was **introduced in** "Calibrate Before Use" and was built for the **few-shot prompting** setting popularised by GPT-3 ("Language Models are Few-Shot Learners"); the same probe applies to **zero-shot prompting**, where the prompt has no demonstrations.[^s3] **Batch calibration** is a direct successor that keeps the idea of dividing out a contextual prior but estimates it from real inputs.[^s4][^s5] The word "calibration" here means correcting label bias, not matching confidence scores to empirical accuracy.[^s3]

## Sources
[^s1]: Zhao, Wallace, Feng, Klein and Singh, "Calibrate Before Use: Improving Few-shot Performance of Language Models", ICML 2021, PMLR 139:12697-12706. https://proceedings.mlr.press/v139/zhao21c.html (accessed 2026-11-18)
[^s2]: Zhao et al., "Calibrate Before Use", arXiv 2102.09690v2. https://arxiv.org/abs/2102.09690v2 (accessed 2026-11-18)
[^s3]: Zhao et al., "Calibrate Before Use", full text via ar5iv. https://ar5iv.labs.arxiv.org/html/2102.09690 (accessed 2026-11-18)
[^s4]: Zhou, Wan, Proleev, Mincu, Chen, Heller and Roy, "Batch Calibration: Rethinking Calibration for In-Context Learning and Prompt Engineering", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/file/003e438cf04e3caf0a5c908495e484fe-Paper-Conference.pdf (accessed 2026-11-18)
[^s5]: Zhou and Roy, "Batch calibration: Rethinking calibration for in-context learning and prompt engineering", Google Research blog, October 2023. https://research.google/blog/batch-calibration-rethinking-calibration-for-in-context-learning-and-prompt-engineering/ (accessed 2026-11-18)
[^s6]: Fei, Hou, Chen and Bosselut, "Mitigating Label Biases for In-context Learning", ACL 2023, arXiv 2305.19148v3. https://arxiv.org/abs/2305.19148v3 (accessed 2026-11-18)
