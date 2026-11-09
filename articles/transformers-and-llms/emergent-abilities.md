---
id: kt:emergent-abilities
type: Concept
title: Emergent abilities
aliases: [emergence in large language models, emergent capabilities, breakthrough behavior]
domain: transformers-and-llms
summary: >-
  Capabilities that are absent (near chance) in smaller language models but present in larger ones, so that they
  cannot be forecast by extrapolating the performance of smaller models; whether such jumps are real or an artifact
  of evaluation metrics is actively debated.
maturity: emerging
broader: [kt:large-language-model]
related: [kt:chain-of-thought, kt:in-context-learning, kt:ai-evaluation, kt:pretraining]
relations:
  - {predicate: introducedIn, object: kt:emergent-abilities-of-large-language-models}
  - {predicate: contrastsWith, object: kt:scaling-laws}
  - {predicate: evaluatedOn, object: kt:big-bench}
sources:
  - id: s1
    title: "Emergent Abilities of Large Language Models"
    publisher: Transactions on Machine Learning Research, 2022 (Wei, Tay, Bommasani, Raffel, Zoph, Borgeaud et al.); arXiv:2206.07682
    url: https://arxiv.org/abs/2206.07682
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s2
    title: "Emergent Abilities of Large Language Models (full text, HTML rendering)"
    publisher: ar5iv rendering of arXiv:2206.07682 (Wei et al.)
    url: https://ar5iv.labs.arxiv.org/html/2206.07682
    type: primary
    accessed: 2026-11-09
  - id: s3
    title: "Are Emergent Abilities of Large Language Models a Mirage?"
    publisher: NeurIPS 2023 (Schaeffer, Miranda, Koyejo)
    url: https://papers.neurips.cc/paper_files/paper/2023/file/adc98a266f45005c403b8311ca7e8bd7-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "Predictability and Surprise in Large Generative Models"
    publisher: ACM, DOI 10.1145/3531146.3533229 (Ganguli, Hernandez, Lovitt et al.), 2022; arXiv:2202.07785
    url: https://arxiv.org/abs/2202.07785
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s5
    title: "Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models"
    publisher: Transactions on Machine Learning Research, 2023 (Srivastava et al.)
    url: https://mlanthology.org/tmlr/2023/srivastava2023tmlr-beyond
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s6
    title: "Understanding Emergent Abilities of Language Models from the Loss Perspective"
    publisher: NeurIPS 2024 (Du, Zeng, Dong, Tang)
    url: https://proceedings.neurips.cc/paper_files/paper/2024/hash/5f1eee2509599faeeb3570a887016a64-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# Emergent abilities

An **emergent ability** of a language model is one that is not present in smaller models but is present in larger ones. Plotted against model scale, task performance sits near random chance up to some threshold and then rises well above it, which means the ability could not have been predicted by extrapolating from the smaller models.[^s1] The term frames a central question about **large language models**: does making them bigger merely make them better at what they already do, or does it unlock qualitatively new behaviour?[^s1][^s4]

## Origin

The concept was popularized by Wei et al. in a paper first posted in June 2022 and published in *Transactions on Machine Learning Research* that year.[^s1] They borrowed the idea from physicist Philip Anderson's 1972 essay "More Is Different", where quantitative change in a system produces qualitative change in behaviour.[^s2] Earlier the same year, Ganguli et al. had described the underlying tension: large generative models combine predictable loss on their training distribution with specific capabilities that are hard to anticipate, which complicates deployment decisions and policy.[^s4] The BIG-bench collaboration, with 204 tasks contributed by 450 authors, independently reported "breakthrough" tasks whose scores jump at a critical scale.[^s5]

## Evidence

Wei et al. surveyed published results and reported emergence on few-shot prompted tasks, measuring scale in training FLOPs and parameters. By their account, GPT-3 moved above chance on 3-digit addition at about 2.3×10^22 FLOPs (13B parameters); multi-task MMLU scores stayed near chance for models at or below roughly 10^22 FLOPs and rose for GPT-3 175B, Gopher and Chinchilla; and on the Word-in-Context benchmark only PaLM 540B, at about 2.5×10^24 FLOPs, exceeded random.[^s2] They also argued that some prompting methods are themselves emergent: **chain-of-thought** prompting beat standard prompting on math word problems only around 68B parameters, and instruction tuning hurt models of about 8B parameters or fewer while helping larger ones.[^s2]

BIG-bench found that tasks improving gradually tend to rely on knowledge or memorization, while breakthrough tasks tend to involve several steps or components, or brittle metrics.[^s5]

## Critiques

Schaeffer, Miranda and Koyejo (NeurIPS 2023) argued that many reported emergent abilities are a "mirage" created by the researcher's choice of metric.[^s3] Exact-match accuracy and multiple-choice grade are nonlinear or discontinuous, so a smooth per-token improvement can look like a sudden jump. Re-scoring InstructGPT/GPT-3 arithmetic with token edit distance produced smooth curves, and adding test data showed small models already performed above chance.[^s3] In a BIG-bench meta-analysis they found that over 92% of claimed emergent abilities appeared under just those two metrics, and they deliberately induced "emergence" in vision models by switching metrics.[^s3] They stressed, however, that their work does not show that language models cannot have emergent abilities.[^s3]

Wei et al. had themselves noted that metrics like exact match can hide incremental progress, and that abilities first seen at large scale sometimes later appear in much smaller models trained on better data or with different architectures.[^s2] Du et al. (NeurIPS 2024) proposed measuring emergence against **pretraining** loss rather than size: models with the same loss performed similarly regardless of parameter and data counts, and some tasks stayed near chance until loss crossed a threshold even under continuous metrics.[^s6]

## Why it matters

If capabilities appear abruptly, then evaluating a smaller model, or an earlier checkpoint, may not reveal what a larger one can do, including harmful behaviour.[^s4] Wei et al. noted that risks such as bias, toxicity and imitation of common falsehoods may also grow or appear with scale.[^s2] This is one reason developers and safety evaluators test frontier models directly instead of relying only on extrapolation.[^s4] As of 2026, the question is unresolved: the evidence suggests that the choice of scale variable and metric strongly shapes whether a capability looks emergent.[^s3][^s6]

## Connections

- **Broader:** emergence is a claimed property of **large language models** as they are scaled up.[^s1]
- **Introduced in:** Wei et al.'s *Emergent Abilities of Large Language Models* defined and catalogued the phenomenon.[^s1]
- **Contrasts with:** **scaling laws**, which describe smooth, predictable improvements in loss; the tension between smooth loss and abrupt task gains is the core of the debate.[^s4][^s3]
- **Evaluated on:** many cited examples come from **BIG-bench**.[^s5][^s3]
- **Related:** **chain-of-thought** prompting and **in-context learning** (few-shot prompting) are both cited as abilities that only pay off at sufficient scale;[^s2] **pretraining** loss is proposed as a better predictor of when they appear;[^s6] and the metric critique is a lesson for **AI evaluation** generally.[^s3]

## Sources

[^s1]: Wei et al., "Emergent Abilities of Large Language Models", TMLR 2022, arXiv:2206.07682. https://arxiv.org/abs/2206.07682 (accessed 2026-11-09)
[^s2]: Wei et al., "Emergent Abilities of Large Language Models", full text via ar5iv. https://ar5iv.labs.arxiv.org/html/2206.07682 (accessed 2026-11-09)
[^s3]: Schaeffer, Miranda, Koyejo, "Are Emergent Abilities of Large Language Models a Mirage?", NeurIPS 2023. https://papers.neurips.cc/paper_files/paper/2023/file/adc98a266f45005c403b8311ca7e8bd7-Paper-Conference.pdf (accessed 2026-11-09)
[^s4]: Ganguli et al., "Predictability and Surprise in Large Generative Models", ACM 2022, arXiv:2202.07785. https://arxiv.org/abs/2202.07785 (accessed 2026-11-09)
[^s5]: Srivastava et al., "Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models", TMLR 2023. https://mlanthology.org/tmlr/2023/srivastava2023tmlr-beyond (accessed 2026-11-09)
[^s6]: Du, Zeng, Dong, Tang, "Understanding Emergent Abilities of Language Models from the Loss Perspective", NeurIPS 2024. https://proceedings.neurips.cc/paper_files/paper/2024/hash/5f1eee2509599faeeb3570a887016a64-Abstract.html (accessed 2026-11-09)
