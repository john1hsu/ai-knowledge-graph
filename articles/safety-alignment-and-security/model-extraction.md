---
id: kt:model-extraction
type: Risk
title: Model extraction
aliases: [model stealing, model extraction attack, model stealing attack]
domain: safety-alignment-and-security
summary: >-
  A privacy attack in which an adversary with query access to a deployed machine learning model uses its outputs
  to learn the model's parameters or architecture, or to train a substitute that reproduces its behaviour.
maturity: established
broader: [kt:adversarial-machine-learning]
related: [kt:data-poisoning, kt:adversarial-example, kt:membership-inference-attack, kt:large-language-model]
relations:
  - {predicate: basedOn, object: kt:knowledge-distillation}
  - {predicate: enables, object: kt:adversarial-example}
  - {predicate: introducedIn, object: kt:stealing-machine-learning-models-via-prediction-apis}
sources:
  - id: s1
    title: "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (NIST AI 100-2 E2025)"
    publisher: NIST (Vassilev, Oprea, Fordyce, Anderson, Davies, Hamin), March 2025
    url: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf
    type: government
    accessed: 2026-11-18
  - id: s2
    title: "Stealing Machine Learning Models via Prediction APIs"
    publisher: arXiv:1609.02943 (Tramèr, Zhang, Juels, Reiter, Ristenpart); USENIX Security 2016
    url: https://arxiv.org/abs/1609.02943v1
    type: primary
    accessed: 2026-11-18
  - id: s3
    title: "High Accuracy and High Fidelity Extraction of Neural Networks"
    publisher: USENIX Security 2020 (Jagielski, Carlini, Berthelot, Kurakin, Papernot)
    url: https://www.usenix.org/conference/usenixsecurity20/presentation/jagielski
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Knockoff Nets: Stealing Functionality of Black-Box Models"
    publisher: CVPR 2019 (Orekondy, Schiele, Fritz)
    url: https://openaccess.thecvf.com/content_CVPR_2019/html/Orekondy_Knockoff_Nets_Stealing_Functionality_of_Black-Box_Models_CVPR_2019_paper.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s5
    title: "Stealing Part of a Production Language Model"
    publisher: ICML 2024, PMLR vol. 235 (Carlini, Paleka, Dvijotham, Steinke, Hayase, Cooper, Lee, Jagielski, Nasr, Conmy, Wallace, Rolnick, Tramèr)
    url: https://proceedings.mlr.press/v235/carlini24a.html
    type: peer-reviewed
    accessed: 2026-11-18
created: 2026-11-18
---

# Model extraction

**Model extraction** (also called *model stealing*) is an attack on the confidentiality of a machine learning model rather than of its training data. An adversary who can send queries to a deployed model, typically through a machine-learning-as-a-service API, uses the returned predictions to learn information about the model: its architecture, its parameters, or simply enough of its behaviour to build a working copy.[^s1] NIST's adversarial machine learning taxonomy (AI 100-2 E2025) files it under privacy compromises and lists it among the attacks that need only query access, with no knowledge of the training data, architecture or weights.[^s1]

## Origin

The attack was put on the map by Tramèr, Zhang, Juels, Reiter and Ristenpart in "Stealing Machine Learning Models via Prediction APIs" (USENIX Security 2016). Working only through black-box queries, they extracted logistic regression models, neural networks and decision trees from the commercial prediction services of BigML and Amazon Machine Learning with what they called near-perfect fidelity.[^s2] They observed that APIs returning confidence scores, or accepting partial feature vectors, make extraction much easier, and that stripping confidence values from responses does not remove the threat.[^s2]

## How it works

Attacks are usually grouped by method:[^s1]

- **Direct (algebraic) extraction** treats the model's outputs as equations in its unknown weights and solves for them, exploiting the mathematical structure of the network.[^s1][^s2]
- **Learning-based extraction** labels a set of chosen inputs with the victim's predictions and trains a substitute on those pairs, often with active learning or reinforcement learning to cut the number of queries.[^s1]
- **Side-channel extraction** reads physical leakage such as electromagnetic emissions, or uses hardware faults such as Rowhammer, to recover networks running on a device.[^s1]

Learning-based extraction is essentially knowledge distillation carried out against someone else's model. Orekondy, Schiele and Fritz's *Knockoff Nets* (CVPR 2019) showed that querying an image classifier with natural images drawn from a different distribution than its training data, then training a "knockoff" on the returned predictions, yields a well-performing copy even when the knockoff uses a different architecture; the authors estimated that a reasonable knockoff of an image-analysis API could cost about $30 in queries.[^s4]

Jagielski, Carlini, Berthelot, Kurakin and Papernot (USENIX Security 2020) separated two goals. **Accuracy** asks how well the stolen model does on the underlying task; **fidelity** asks how closely it matches the victim's predictions on every input.[^s3] They argued that learning-based methods cannot reach truly high fidelity, and presented a practical attack that recovers weights directly, without training, to obtain a functionally equivalent model; their experiments included a production image classifier trained on a billion proprietary images.[^s3]

## Extraction of large language models

Carlini and colleagues (ICML 2024) showed that production LLM APIs leak precise architectural information. Using ordinary API access, they recovered the final embedding projection layer of a transformer up to symmetries. In their reported results, they extracted the full projection matrices of OpenAI's Ada and Babbage models for under $20, confirming hidden dimensions of 1,024 and 2,048, and recovered the exact hidden dimension of gpt-3.5-turbo; they estimated the full matrix for that model would cost under $2,000 in queries.[^s5] The authors described this as the first attack to pull precise, nontrivial parameters from black-box production language models.[^s5]

## Why it matters and limitations

Extraction harms in two ways. It lets an attacker free-ride on the cost of data collection and training, and it is often a stepping stone: once an attacker holds a close copy of the weights and architecture, stronger white-box or gray-box attacks such as crafting adversarial examples become possible against the original.[^s1]

There are also theoretical limits. NIST notes that exactly extracting deep models has been shown to be impossible, and that even building a functionally equivalent model is NP-hard in general, so practical attacks rely on structure, approximations or restricted model classes.[^s1]

## Defenses

NIST lists limiting the number of queries a user may make, detecting suspicious query patterns, and hardening architectures against side channels; it cautions that a well-resourced attacker can get around each of these.[^s1] Differential privacy does not help, because it protects individual training records rather than the model itself.[^s1] Coarsening outputs, such as returning labels without confidence scores, raises the cost but does not by itself prevent extraction.[^s2] The ICML 2024 paper also discusses defenses and mitigations specific to language-model APIs.[^s5]

## Connections

- **Broader:** model extraction is one of the main attack classes of adversarial machine learning, alongside evasion with adversarial examples and data poisoning.[^s1]
- **Based on:** learning-based extraction reuses the teacher-student logic of knowledge distillation, with the victim API as an unwilling teacher.[^s4]
- **Enables:** a stolen replica gives attackers white-box access for transfer attacks with adversarial examples.[^s1]
- **Related:** like membership inference attacks, it is a privacy compromise mounted through query access, but it targets the model instead of the data.[^s1] Recent work extends it to large language models.[^s5]
- **Introduced in:** Tramèr et al.'s 2016 USENIX Security paper.[^s2]

## Sources

[^s1]: NIST, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations" (NIST AI 100-2 E2025), March 2025. https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf (accessed 2026-11-18)
[^s2]: Tramèr, Zhang, Juels, Reiter, Ristenpart, "Stealing Machine Learning Models via Prediction APIs", USENIX Security 2016, arXiv:1609.02943. https://arxiv.org/abs/1609.02943v1 (accessed 2026-11-18)
[^s3]: Jagielski, Carlini, Berthelot, Kurakin, Papernot, "High Accuracy and High Fidelity Extraction of Neural Networks", USENIX Security 2020. https://www.usenix.org/conference/usenixsecurity20/presentation/jagielski (accessed 2026-11-18)
[^s4]: Orekondy, Schiele, Fritz, "Knockoff Nets: Stealing Functionality of Black-Box Models", CVPR 2019. https://openaccess.thecvf.com/content_CVPR_2019/html/Orekondy_Knockoff_Nets_Stealing_Functionality_of_Black-Box_Models_CVPR_2019_paper.html (accessed 2026-11-18)
[^s5]: Carlini et al., "Stealing Part of a Production Language Model", ICML 2024, PMLR 235:5680-5705. https://proceedings.mlr.press/v235/carlini24a.html (accessed 2026-11-18)
