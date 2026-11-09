---
id: kt:prompt-sensitivity
type: Concept
title: Prompt sensitivity
aliases: [prompt brittleness, prompt format sensitivity, prompt fragility, few-shot instability]
domain: prompting-and-reasoning
summary: >-
  The tendency of language models to give substantially different outputs and accuracy when a prompt is
  changed in ways that should not matter, such as its formatting, instruction wording, choice of
  demonstrations, or the order of those demonstrations.
maturity: established
broader: [kt:prompt-engineering]
related: [kt:few-shot-prompting, kt:in-context-learning, kt:large-language-model, kt:self-consistency, kt:contextual-calibration]
relations:
  - {predicate: studiedIn, object: kt:ai-evaluation}
sources:
  - id: s1
    title: "Calibrate Before Use: Improving Few-shot Performance of Language Models"
    publisher: ICML 2021, PMLR vol. 139, pp. 12697-12706 (Zhao, Wallace, Feng, Klein, Singh)
    url: https://proceedings.mlr.press/v139/zhao21c.html
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s2
    title: "Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity"
    publisher: ACL 2022, pp. 8086-8098 (Lu, Bartolo, Moore, Riedel, Stenetorp), via UCL Discovery
    url: https://discovery.ucl.ac.uk/id/eprint/10154329/
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s3
    title: "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design"
    publisher: arXiv 2310.11324v2 (Sclar, Choi, Tsvetkov, Suhr)
    url: https://arxiv.org/abs/2310.11324v2
    type: primary
    accessed: 2026-11-09
  - id: s4
    title: "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design (ICLR 2024 poster)"
    publisher: ICLR 2024
    url: https://iclr.cc/virtual/2024/poster/18650
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s5
    title: "State of What Art? A Call for Multi-Prompt LLM Evaluation"
    publisher: TACL vol. 12, pp. 933-949, 2024 (Mizrahi, Kaplan, Malkin, Dror, Shahaf, Stanovsky)
    url: https://aclanthology.org/2024.tacl-1.52
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# Prompt sensitivity

**Prompt sensitivity** (also called prompt brittleness) is the observation that a language model's behaviour can change sharply when a prompt is altered in ways a human would consider irrelevant: a different separator or casing, a reworded but equivalent instruction, a different set of worked examples, or the same examples in another order. It became a recognised problem with few-shot prompting of GPT-3, where Zhao et al. reported that such choices alone could move accuracy from roughly chance level to near the state of the art.[^s1] Later work extended the finding to instruction-tuned and open-weight models and to how benchmarks are run.[^s3][^s5]

## How it shows up

Researchers usually separate several sources of variation, all of which leave the task's meaning unchanged.[^s1]

- **Demonstration order.** Lu et al. showed that permuting the same few-shot examples can separate strong results from random-guess performance; good orderings were not tied to a particular subset of examples and did not transfer from one model to another, and the effect appeared at every model size they tested.[^s2]
- **Demonstration choice and label balance.** Zhao et al. traced much of the instability to the model favouring certain answers, in particular labels that appear near the end of the prompt and labels that are frequent in pretraining text.[^s1]
- **Surface formatting.** Sclar et al. varied only "spurious" features such as separators, spacing and casing. On several open-source models they measured accuracy gaps of up to 76 points with LLaMA-2-13B, and the sensitivity persisted with larger models, more examples, and instruction tuning.[^s3][^s4]
- **Instruction wording.** Mizrahi et al. evaluated 20 LLMs on 39 tasks from three benchmarks with many paraphrases of each instruction (6.5 million instances in total). Both absolute scores and model rankings shifted with the template.[^s5]

## Mitigations

*Contextual calibration* first measures the model's bias by giving it the prompt with a content-free input such as "N/A", then fits an affine correction so that this input gets a uniform prediction over labels. On GPT-2 and GPT-3 it raised accuracy by up to 30 absolute points and narrowed the spread across prompt choices.[^s1] To choose example orders without a labelled development set, Lu et al. let the model generate an artificial probing set and ranked permutations with entropy statistics, reporting a 13% relative gain across eleven text-classification tasks for GPT-family models.[^s2] Averaging over several sampled outputs, as in self-consistency, reduces decoding variance, but it does not remove variance that comes from how the prompt is built.

## Consequences for evaluation

Sensitivity matters most for evaluation. When a benchmark scores each model with one arbitrarily chosen template, a reported difference between models may come from the template rather than from capability.[^s5] Sclar et al. proposed FormatSpread, which samples plausible formats and reports the expected range of performance. It needs no access to model weights, and the authors found that the best format correlates only weakly across models.[^s3] Mizrahi et al. likewise recommend metrics computed over many instruction paraphrases, chosen for the goal at hand, such as comparing models versus picking a prompt for a product.[^s5]

## Open questions

These studies measure sensitivity but do not fully explain it. Proposed causes include label and recency biases learned in pretraining[^s1] and differences in how models represent formats internally, which Sclar et al. began to probe.[^s3] Most of the quantitative evidence above comes from classification-style tasks and models released between 2020 and 2024, so the size of the effect on newer chat and reasoning models should be measured rather than assumed.[^s3][^s5]

## Connections

Prompt sensitivity is a property of **prompt engineering** (broader): it is the reason prompt design has an empirical, trial-and-error side.[^s3] It was first documented for **few-shot prompting** and **in-context learning** in **large language models**, where the demonstrations are part of the prompt.[^s1][^s2] **Contextual calibration** is the best-known targeted fix.[^s1] **Self-consistency** is related but addresses sampling variance rather than prompt construction. The phenomenon is **studied in AI evaluation**, where multi-prompt reporting is proposed as the remedy for brittle single-template leaderboards.[^s5]

## Sources
[^s1]: Zhao, Wallace, Feng, Klein and Singh, "Calibrate Before Use: Improving Few-shot Performance of Language Models", ICML 2021, PMLR 139. https://proceedings.mlr.press/v139/zhao21c.html (accessed 2026-11-09)
[^s2]: Lu, Bartolo, Moore, Riedel and Stenetorp, "Fantastically Ordered Prompts and Where to Find Them: Overcoming Few-Shot Prompt Order Sensitivity", ACL 2022. https://discovery.ucl.ac.uk/id/eprint/10154329/ (accessed 2026-11-09)
[^s3]: Sclar, Choi, Tsvetkov and Suhr, "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design", arXiv 2310.11324v2. https://arxiv.org/abs/2310.11324v2 (accessed 2026-11-09)
[^s4]: ICLR 2024 poster page for Sclar et al. https://iclr.cc/virtual/2024/poster/18650 (accessed 2026-11-09)
[^s5]: Mizrahi, Kaplan, Malkin, Dror, Shahaf and Stanovsky, "State of What Art? A Call for Multi-Prompt LLM Evaluation", TACL 12 (2024). https://aclanthology.org/2024.tacl-1.52 (accessed 2026-11-09)
