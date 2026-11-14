---
id: kt:human-evaluation
type: Technique
title: Human evaluation
aliases: [human judgment evaluation, human assessment of model outputs, human preference evaluation]
domain: evaluation-and-benchmarks
summary: >-
  Assessing the outputs of AI systems, especially generated text, by collecting judgments from human raters
  through ratings, pairwise preferences or annotation tasks, typically treated as the reference standard
  against which automatic metrics and model judges are validated.
maturity: established
broader: [kt:ai-evaluation]
related: [kt:llm-as-a-judge, kt:chatbot-arena, kt:red-teaming, kt:inter-annotator-agreement]
relations:
  - {predicate: usedIn, object: kt:rlhf}
  - {predicate: usedIn, object: kt:chatbot-arena}
  - {predicate: dependsOn, object: kt:bradley-terry-model}
  - {predicate: alternativeTo, object: kt:llm-as-a-judge}
  - {predicate: contrastsWith, object: kt:perplexity}
sources:
  - id: s1
    title: "Best practices for the human evaluation of automatically generated text"
    publisher: Proceedings of INLG 2019, pp. 355–368 (van der Lee, Gatt, van Miltenburg, Wubben, Krahmer)
    url: https://aclanthology.org/W19-8643/
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s2
    title: "Twenty Years of Confusion in Human Evaluation: NLG Needs Evaluation Sheets and Standardised Definitions"
    publisher: Proceedings of INLG 2020, pp. 169–182 (Howcroft, Belz, Clinciu et al.)
    url: https://aclanthology.org/2020.inlg-1.23
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "All That's 'Human' Is Not Gold: Evaluating Human Evaluation of Generated Text"
    publisher: Proceedings of ACL-IJCNLP 2021 (Volume 1), pp. 7282–7296 (Clark, August, Serrano, Haduong, Gururangan, Smith)
    url: https://aclanthology.org/2021.acl-long.565
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "The Perils of Using Mechanical Turk to Evaluate Open-Ended Text Generation"
    publisher: Proceedings of EMNLP 2021, pp. 1265–1285 (Karpinska, Akoury, Iyyer)
    url: https://aclanthology.org/2021.emnlp-main.97
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference"
    publisher: Proceedings of ICML 2024, PMLR 235:8359–8388 (Chiang, Zheng, Sheng et al.)
    url: https://proceedings.mlr.press/v235/chiang24b.html
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s6
    title: "Training language models to follow instructions with human feedback"
    publisher: NeurIPS 2022 (Ouyang, Wu, Jiang et al.)
    url: https://neurips.cc/virtual/2022/poster/52886
    type: peer-reviewed
    accessed: 2026-11-14
created: 2026-11-14
---

# Human evaluation

**Human evaluation** is the practice of judging an AI system's outputs by asking people to rate, rank, compare or annotate them. It is the default way to assess qualities that automatic metrics capture poorly, such as fluency, helpfulness, coherence or factual adequacy of open-ended text, and it serves as the yardstick against which automatic metrics and model-based judges are calibrated. In natural language generation (NLG), researchers have long relied on it even while observing that the way it is carried out varies widely from study to study.[^s1]

## How it works

A human evaluation study fixes several design choices: which **quality criteria** to judge (for example fluency or relevance), what **response format** raters use, who the **raters** are, how many items and judgments are collected, and how results are analysed statistically. Van der Lee and colleagues surveyed how NLG papers make these choices and proposed literature-grounded best practices covering them, aimed at making evaluations more consistent and comparable.[^s1]

Common response formats include:

- **Absolute ratings**, where each output is scored on a scale (often a Likert scale) for one or more criteria.[^s1]
- **Pairwise preference**, where a rater sees two outputs for the same input and picks the better one, or declares a tie.[^s5]
- **Ranking**, where several outputs are ordered from best to worst; InstructGPT's labelers ranked model outputs, and those rankings trained a reward model.[^s6]

Pairwise judgments can be aggregated into a leaderboard with a statistical model. Chatbot Arena shows a user two anonymous models' answers to the user's own prompt, reveals the identities only after the vote, and fits a Bradley–Terry (logistic) model to the win records, preferring its coefficients to Elo ratings for statistical estimation and reporting confidence intervals.[^s5]

## Reliability problems

Human judgments are not automatically a gold standard. Howcroft and colleagues analysed 165 NLG papers with human evaluations and found more than 200 different terms used for the quality aspects being assessed, often with unclear definitions, and concluded that the field's practice was badly confused as of 2020. They called for standard terminology and evaluation sheets that document each study's design.[^s2]

Rater expertise matters. Clark and colleagues found that untrained evaluators distinguished GPT-3 text from human-written stories, news and recipes at about chance level; quick training with instructions or examples raised accuracy to at most 55%, without significant gains across domains.[^s3] Karpinska, Akoury and Iyyer reviewed 45 open-ended generation papers, found most omitted key details of their crowdsourcing setup, and showed that Amazon Mechanical Turk workers, even after qualification filters, could not separate model output from human references, whereas English teachers could.[^s4]

Agreement between raters is itself a measured quantity. In the Chatbot Arena study (data from April 2023 to January 2024), crowd votes matched expert labels on 72.8% to 83.1% of sampled comparisons, while two experts agreed with each other 79.4% to 89.8% of the time.[^s5] The authors also note that their volunteer user base likely skews toward LLM hobbyists and researchers and that the study measured helpfulness rather than safety.[^s5]

## In practice

Human evaluation underpins how chat models are built and compared. InstructGPT combined labeler-written demonstrations with human rankings of outputs, and in human evaluations labelers preferred outputs of a 1.3-billion-parameter InstructGPT model over those of the 175-billion-parameter GPT-3 (as reported by OpenAI researchers in 2022).[^s6] Public preference leaderboards scale the same idea through crowdsourcing: by January 2024 Chatbot Arena had gathered about 240,000 votes from more than 90,000 users across over 50 models.[^s5] Because such studies are slow and costly, teams increasingly use model-based judges for routine checks and reserve human raters for validation and high-stakes decisions; the reporting guidance from the NLG literature still applies to either.[^s1][^s2]

## Connections

Human evaluation is a method within **AI evaluation**, the broader field of measuring AI systems.[^s1] It is the main alternative to **LLM-as-a-judge**, whose value is usually established by measuring agreement with human raters.[^s5] Human rankings are the training signal in **RLHF**,[^s6] and **Chatbot Arena** is the best-known crowdsourced preference platform, which aggregates votes with the **Bradley–Terry model**.[^s5] It contrasts with intrinsic automatic metrics such as **perplexity**, which need no raters but say little directly about perceived quality of open-ended output.[^s1] Its reliability is quantified through **inter-annotator agreement**,[^s5] and adversarial human probing for failures is the related practice of **red teaming**.

## Sources

[^s1]: van der Lee et al., "Best practices for the human evaluation of automatically generated text", INLG 2019. https://aclanthology.org/W19-8643/ (accessed 2026-11-14)
[^s2]: Howcroft et al., "Twenty Years of Confusion in Human Evaluation: NLG Needs Evaluation Sheets and Standardised Definitions", INLG 2020. https://aclanthology.org/2020.inlg-1.23 (accessed 2026-11-14)
[^s3]: Clark et al., "All That's 'Human' Is Not Gold: Evaluating Human Evaluation of Generated Text", ACL-IJCNLP 2021. https://aclanthology.org/2021.acl-long.565 (accessed 2026-11-14)
[^s4]: Karpinska, Akoury & Iyyer, "The Perils of Using Mechanical Turk to Evaluate Open-Ended Text Generation", EMNLP 2021. https://aclanthology.org/2021.emnlp-main.97 (accessed 2026-11-14)
[^s5]: Chiang et al., "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference", ICML 2024. https://proceedings.mlr.press/v235/chiang24b.html (accessed 2026-11-14)
[^s6]: Ouyang et al., "Training language models to follow instructions with human feedback", NeurIPS 2022. https://neurips.cc/virtual/2022/poster/52886 (accessed 2026-11-14)
