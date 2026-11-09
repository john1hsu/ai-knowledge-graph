---
id: kt:scaling-laws
type: Concept
title: Scaling laws
aliases: [neural scaling laws, LLM scaling laws, Kaplan scaling laws, Chinchilla scaling laws, compute-optimal scaling]
domain: transformers-and-llms
summary: >-
  Empirical power-law relationships that predict how a neural network's loss falls as its parameter count, training
  data and training compute grow, used to forecast model quality and to split a fixed compute budget between model
  size and data.
maturity: established
broader: [kt:deep-learning]
related: [kt:large-language-model, kt:pretraining, kt:test-time-compute, kt:transformer-architecture]
relations:
  - {predicate: introducedIn, object: kt:scaling-laws-for-neural-language-models}
  - {predicate: contrastsWith, object: kt:emergent-abilities}
  - {predicate: usedIn, object: kt:pretraining}
sources:
  - id: s1
    title: "Deep Learning Scaling is Predictable, Empirically"
    publisher: arXiv:1712.00409 (Hestness, Narang, Ardalani, Diamos, Jun, Kianinejad, Patwary, Yang, Zhou; Baidu Research), 2017
    url: https://arxiv.org/abs/1712.00409v1
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "Scaling Laws for Neural Language Models"
    publisher: arXiv:2001.08361 (Kaplan, McCandlish, Henighan, Brown, Chess, Child, Gray, Radford, Wu, Amodei; OpenAI), 2020
    url: https://arxiv.org/pdf/2001.08361
    type: primary
    accessed: 2026-11-09
  - id: s3
    title: "An Empirical Analysis of Compute-Optimal Large Language Model Training"
    publisher: NeurIPS 2022 (Hoffmann, Borgeaud, Mensch et al.; DeepMind); also arXiv:2203.15556 as "Training Compute-Optimal Large Language Models"
    url: https://mlanthology.org/neurips/2022/hoffmann2022neurips-empirical
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "Chinchilla Scaling: A replication attempt"
    publisher: arXiv:2404.10102v2 (Besiroglu, Erdil, Barnett, You; Epoch AI), 2024
    url: https://arxiv.org/html/2404.10102v2
    type: preprint
    accessed: 2026-11-09
  - id: s5
    title: "Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws"
    publisher: Proceedings of the 41st ICML, PMLR 235:43445-43460, 2024 (Sardana, Portes, Doubov, Frankle)
    url: https://proceedings.mlr.press/v235/sardana24a.html
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s6
    title: "Are Emergent Abilities of Large Language Models a Mirage?"
    publisher: NeurIPS 2023, oral (Schaeffer, Miranda, Koyejo)
    url: https://neurips.cc/virtual/2023/oral/73863
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# Scaling laws

**Scaling laws** (or *neural scaling laws*) are empirical regularities showing that a model's test loss falls smoothly and predictably, roughly as a power law, as one scales up the number of parameters N, the amount of training data D, or the training compute C. They let practitioners fit small, cheap training runs and extrapolate to much larger ones, and they underpin the decision of how large a language model to train and on how many tokens.[^s2][^s3]

## Origin

Hestness et al. at Baidu Research reported in 2017 that generalization error follows a power law in training-set size across machine translation, language modelling, image classification and speech recognition. They found that better architectures shift the curve but seem not to change its exponent, and that the required model size grows sublinearly with data.[^s1] Kaplan et al. at OpenAI then formalized the idea for Transformer language models in January 2020, showing power-law trends in cross-entropy loss spanning more than seven orders of magnitude and coining the framing most later work builds on.[^s2]

## How it works

Kaplan et al. fit separate laws for each resource while the others are not a bottleneck. With N counted as non-embedding parameters, loss behaves as L(N) = (N_c/N)^α_N with α_N ≈ 0.076; with data, L(D) = (D_c/D)^α_D with α_D ≈ 0.095; and with optimally allocated compute, L ∝ C^−0.050.[^s2] Excluding embedding parameters gave much cleaner trends, and shape details such as depth versus width mattered little at fixed parameter count.[^s2] The constants depend on the tokenizer and data, so only the exponents and the trends carry over.[^s2]

The practical payoff is **compute-optimal allocation**. Kaplan et al. concluded that optimal model size should grow as about C^0.73 while data grows only as about C^0.27, so the best use of a budget was a very large model trained on modest data and stopped well before convergence.[^s2]

Hoffmann et al. (DeepMind) revisited this in 2022 by training over 400 models, from 70 million to over 16 billion parameters on 5 to 500 billion tokens. They used three estimation methods (fixed model sizes with varying tokens, IsoFLOP profiles at fixed compute, and a fitted parametric loss L(N, D) = E + A/N^α + B/D^β) and concluded that parameters and tokens should scale in **equal proportion**, so that doubling the model means doubling the data.[^s3][^s4] To test the claim they trained **Chinchilla**, a 70B-parameter model given the same compute as the 280B Gopher but four times more data; Chinchilla outperformed Gopher, GPT-3 and Megatron-Turing NLG on a wide range of tasks and reached 67.5% average accuracy on MMLU, as reported by its authors in 2022.[^s3] The authors argued that many large models of the time were undertrained; Chinchilla itself was trained at roughly 20 tokens per parameter, a ratio often cited as the "Chinchilla-optimal" target.[^s3][^s4]

## Limitations and critiques

Scaling-law fits are fragile. An Epoch AI replication in 2024 reconstructed Hoffmann et al.'s data from a published figure and found that the paper's parametric fit matched the data poorly and had implausibly narrow confidence intervals. Its own refit implied roughly 20 tokens per parameter, consistent with the two other Chinchilla methods, whereas the originally reported parameters implied a different ratio.[^s4] The disagreement between Kaplan and Chinchilla exponents likewise shows that conclusions depend on experimental choices, not only on the underlying law.[^s2][^s3]

Compute-optimal is also not cost-optimal once a model is deployed. Sardana et al. (ICML 2024) added inference cost to the Chinchilla objective and found that teams expecting heavy demand (on the order of a billion requests) should train smaller models for longer. In their 47 trained models, quality kept improving at up to 10,000 tokens per parameter.[^s5] Finally, smooth loss curves do not guarantee smooth task metrics. Schaeffer et al. argued at NeurIPS 2023 that many apparently sudden "emergent" abilities come from nonlinear or discontinuous evaluation metrics, and largely disappear under continuous ones.[^s6]

## In practice

The method both papers model is to fit curves on many small, cheap runs before committing to a large pretraining run, then use them to choose model size and token budget and to forecast the final loss.[^s2][^s3] Inference-aware analyses give a principled reason to train compact, heavily used models far past the Chinchilla ratio, trading extra training compute for cheaper serving.[^s5]

## Connections

- **Broader:** scaling laws are an empirical property of **deep learning** systems, first documented across several deep-learning domains before language models.[^s1]
- **Introduced in:** the language-model formulation most work cites comes from Kaplan et al.'s *Scaling Laws for Neural Language Models*.[^s2]
- **Used in:** they guide **pretraining** budgets for **large language models** built on the **Transformer architecture**, the setting in which both the Kaplan and Chinchilla laws were measured.[^s2][^s3]
- **Related:** **test-time compute** extends the scaling question from training to inference, a direction foreshadowed by inference-aware laws.[^s5]
- **Contrasts with:** **emergent abilities**, the claim that capabilities appear abruptly with scale, which sits uneasily with smooth loss curves and has been attributed partly to metric choice.[^s6]

## Sources

[^s1]: Hestness et al., "Deep Learning Scaling is Predictable, Empirically", arXiv:1712.00409, 2017. https://arxiv.org/abs/1712.00409v1 (accessed 2026-11-09)
[^s2]: Kaplan et al., "Scaling Laws for Neural Language Models", arXiv:2001.08361, 2020. https://arxiv.org/pdf/2001.08361 (accessed 2026-11-09)
[^s3]: Hoffmann et al., "An Empirical Analysis of Compute-Optimal Large Language Model Training", NeurIPS 2022. https://mlanthology.org/neurips/2022/hoffmann2022neurips-empirical (accessed 2026-11-09)
[^s4]: Besiroglu, Erdil, Barnett, You, "Chinchilla Scaling: A replication attempt", arXiv:2404.10102v2, 2024. https://arxiv.org/html/2404.10102v2 (accessed 2026-11-09)
[^s5]: Sardana, Portes, Doubov, Frankle, "Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws", ICML 2024, PMLR 235. https://proceedings.mlr.press/v235/sardana24a.html (accessed 2026-11-09)
[^s6]: Schaeffer, Miranda, Koyejo, "Are Emergent Abilities of Large Language Models a Mirage?", NeurIPS 2023. https://neurips.cc/virtual/2023/oral/73863 (accessed 2026-11-09)
