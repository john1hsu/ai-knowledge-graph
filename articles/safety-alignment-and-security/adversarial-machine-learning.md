---
id: kt:adversarial-machine-learning
type: Field
title: Adversarial machine learning
aliases: [AML, adversarial ML, machine learning security]
domain: safety-alignment-and-security
summary: >-
  The study of how attackers can manipulate machine learning systems through crafted inputs, corrupted training
  data or probing queries, and of the defenses that make models robust to such manipulation.
maturity: established
broader: [kt:ai-safety, kt:machine-learning]
related: [kt:red-teaming, kt:jailbreak, kt:adversarial-example, kt:adversarial-training]
relations:
  - {predicate: hasPart, object: kt:prompt-injection}
  - {predicate: hasPart, object: kt:data-poisoning}
  - {predicate: hasPart, object: kt:model-extraction}
  - {predicate: contrastsWith, object: kt:generative-adversarial-network}
sources:
  - id: s1
    title: "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (NIST AI 100-2 E2025)"
    publisher: NIST CSRC publication page (Vassilev, Oprea, Fordyce, Anderson, Davies, Hamin), March 2025
    url: https://csrc.nist.gov/pubs/ai/100/2/e2025/final
    type: government
    accessed: 2026-11-14
  - id: s2
    title: "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (NIST AI 100-2 E2025), full report"
    publisher: NIST, March 2025
    url: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf
    type: government
    accessed: 2026-11-14
  - id: s3
    title: "Wild Patterns: Ten Years After the Rise of Adversarial Machine Learning"
    publisher: Pattern Recognition 84 (2018), arXiv:1712.03141 (Biggio, Roli)
    url: https://ar5iv.labs.arxiv.org/html/1712.03141
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "Explaining and Harnessing Adversarial Examples"
    publisher: ICLR 2015, arXiv:1412.6572 (Goodfellow, Shlens, Szegedy)
    url: https://arxiv.org/abs/1412.6572
    type: primary
    accessed: 2026-11-14
  - id: s5
    title: "Explaining and Harnessing Adversarial Examples (publication record)"
    publisher: Google Research
    url: https://research.google/pubs/explaining-and-harnessing-adversarial-examples/
    type: lab-research
    accessed: 2026-11-14
  - id: s6
    title: "Towards Deep Learning Models Resistant to Adversarial Attacks"
    publisher: arXiv:1706.06083 (Madry, Makelov, Schmidt, Tsipras, Vladu), 2017
    url: https://arxiv.org/abs/1706.06083v4
    type: primary
    accessed: 2026-11-14
created: 2026-11-14
---

# Adversarial machine learning

Adversarial machine learning (AML) studies machine learning systems as targets: how an adversary can make a model misbehave, leak information or become unavailable, and how designers can anticipate and mitigate those attacks. NIST's AI 100-2 E2025 report, published in March 2025, organizes the field as a taxonomy of attacker goals, capabilities and knowledge across the stages of the ML lifecycle, and offers a glossary intended as a common vocabulary for standards bodies and practitioners.[^s1]

## Origins

The field is often dated to the discovery of adversarial examples in deep networks around 2014, but Biggio and Roli argue that it is roughly a decade older. Work in 2004–2005 by Dalvi et al. and by Lowd and Meek showed that linear spam filters could be evaded by small, targeted edits to email content, and Barreno et al. (2006) categorized attacks by whether they act at training or test time.[^s3] In 2013 Biggio and colleagues showed gradient-based evasion of nonlinear classifiers, including neural networks, and the transferability of such attacks; the authors describe Szegedy et al.'s 2014 adversarial-example paper as a parallel discovery from different premises.[^s3]

Goodfellow, Shlens and Szegedy's paper, presented at ICLR 2015, brought the topic to the deep learning mainstream.[^s5] It argued that vulnerability to small, worst-case input perturbations stems mainly from models behaving too linearly in high-dimensional input spaces, rather than from nonlinearity or overfitting, and it introduced a fast way to generate such perturbations and use them for adversarial training.[^s4]

## Threat model

AML analyses start by specifying the adversary. Biggio and Roli describe three axes. The **goal** is to violate integrity (evading detection or forcing a chosen output), availability (degrading service) or privacy (extracting information), and may be targeted or indiscriminate. The attacker's **knowledge** ranges from full white-box access to gray-box knowledge with surrogate data or models to black-box query access. Their **capability** is causative if they can influence training data, or exploratory if they can only shape test-time inputs.[^s3] NIST adds a fourth objective for generative systems, misuse, meaning circumventing a model's safety restrictions.[^s2]

## Attack classes

For predictive AI, NIST groups attacks into three classes.[^s2]

- **Evasion:** test-time inputs perturbed to change a model's prediction, typically posed as an optimization under a perturbation budget.[^s2][^s3]
- **Poisoning:** corrupting training data or model parameters; variants include availability, targeted, backdoor and model poisoning.[^s2]
- **Privacy:** membership inference, data reconstruction, property inference and model extraction.[^s2]

For generative AI, NIST adds supply-chain attacks through poisoned data or third-party models, direct prompting attacks such as jailbreaks, indirect prompt injection through content the model processes, and attacks on AI agents that act on a user's behalf.[^s2] The underlying logic is unchanged: untrusted inputs, untrusted training data and an exposed query interface are each attack surfaces.

## Defenses and their limits

The best-known defense against evasion is adversarial training. Madry et al. framed robustness as a robust-optimization problem, training against the strongest perturbation a first-order (gradient-based) adversary can find, and reported markedly improved resistance on MNIST and CIFAR-10.[^s6] Other mitigations include randomized smoothing, formal verification, data sanitization and differential privacy.[^s2]

NIST's assessment is sober. It notes an inherent trade-off between robustness and accuracy, that verification struggles to scale, that widely used algorithms lack information-theoretic security proofs, and that many published defenses were later broken by adaptive attacks; it therefore recommends evaluating defenses against attackers who know the defense.[^s2] Biggio and Roli similarly frame the field as an arms race and urge proactive design: model the adversary, simulate attacks before deployment, and test under worst-case assumptions rather than against weak attacks.[^s3]

## In practice

AML concepts underpin security testing of deployed models, from malware and fraud classifiers to LLM applications. In 2025 NIST explicitly extended its taxonomy to large language models and chatbots, reflecting a shift of attention from perturbed images toward prompt-level and supply-chain attacks on generative systems.[^s1][^s2]

## Connections

AML is a security-focused branch of **AI safety** that applies to any **machine learning** system. Its central object is the **adversarial example**, and its most studied defense is **adversarial training**.[^s4][^s6] It encompasses **data poisoning** and **model extraction** as attack classes, and NIST places **prompt injection** and **jailbreak**-style direct prompting inside the same taxonomy for generative AI.[^s2] **Red teaming** is the practice that operationalizes its threat models. Despite the shared word, it contrasts with the **generative adversarial network**, where the "adversary" is a cooperative training component rather than an attacker.

## Sources
[^s1]: NIST, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations" (NIST AI 100-2 E2025), publication page, March 2025. https://csrc.nist.gov/pubs/ai/100/2/e2025/final (accessed 2026-11-14)
[^s2]: NIST AI 100-2 E2025, full report, March 2025. https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf (accessed 2026-11-14)
[^s3]: Biggio & Roli, "Wild Patterns: Ten Years After the Rise of Adversarial Machine Learning", Pattern Recognition 84, 2018. https://ar5iv.labs.arxiv.org/html/1712.03141 (accessed 2026-11-14)
[^s4]: Goodfellow, Shlens & Szegedy, "Explaining and Harnessing Adversarial Examples", arXiv:1412.6572. https://arxiv.org/abs/1412.6572 (accessed 2026-11-14)
[^s5]: Google Research publication record for "Explaining and Harnessing Adversarial Examples" (ICLR 2015). https://research.google/pubs/explaining-and-harnessing-adversarial-examples/ (accessed 2026-11-14)
[^s6]: Madry et al., "Towards Deep Learning Models Resistant to Adversarial Attacks", arXiv:1706.06083. https://arxiv.org/abs/1706.06083v4 (accessed 2026-11-14)
