---
id: kt:red-teaming
type: Technique
title: Red teaming
aliases: [AI red teaming, AI red-teaming, red-teaming, adversarial testing of AI systems]
domain: evaluation-and-benchmarks
summary: >-
  A structured, adversarial testing practice in which people (and increasingly other models) deliberately try to
  make an AI system fail or behave harmfully, so that its flaws and vulnerabilities can be found, measured and
  mitigated before or after deployment.
maturity: emerging
broader: [kt:ai-evaluation]
related: [kt:large-language-model, kt:nist-ai-risk-management-framework, kt:rlhf, kt:jailbreak, kt:prompt-injection]
relations:
  - {predicate: regulatedBy, object: kt:executive-orders-on-ai}
  - {predicate: contrastsWith, object: kt:penetration-testing}
sources:
  - id: s1
    title: "Red Teaming Language Models with Language Models"
    publisher: Proceedings of EMNLP 2022, pp. 3419–3448 (Perez et al.), ACL Anthology
    url: https://aclanthology.org/2022.emnlp-main.225
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s2
    title: "Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned"
    publisher: arXiv:2209.07858 (Ganguli et al., Anthropic), 2022
    url: https://arxiv.org/abs/2209.07858v1
    type: primary
    accessed: 2026-10-31
  - id: s3
    title: "Red-Teaming for Generative AI: Silver Bullet or Security Theater?"
    publisher: arXiv:2401.15897v3 (Feffer, Sinha, Deng, Lipton and Heidari, Carnegie Mellon University)
    url: https://arxiv.org/html/2401.15897v3
    type: preprint
    accessed: 2026-10-31
  - id: s4
    title: "Executive Order 14110: Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence"
    publisher: Code of Federal Regulations, Title 3 (2024 edition), U.S. Government Publishing Office
    url: https://govinfo.gov/content/pkg/CFR-2024-title3-vol1/pdf/CFR-2024-title3-vol1-eo14110.pdf
    type: government
    accessed: 2026-10-31
  - id: s5
    title: "Executive Order 14148: Initial Rescissions of Harmful Executive Orders and Actions"
    publisher: Daily Compilation of Presidential Documents, U.S. Government Publishing Office, January 20, 2025
    url: https://www.govinfo.gov/content/pkg/DCPD-202500115/html/DCPD-202500115.htm
    type: government
    accessed: 2026-10-31
created: 2026-10-31
---

# Red teaming

**Red teaming** of AI systems is the practice of deliberately attacking a model or AI-enabled product, playing the role of an adversary or a misusing user, in order to surface harmful, unsafe or insecure behaviour that ordinary testing misses. US Executive Order 14110 (October 30, 2023) defined AI red-teaming as a structured testing effort to find flaws and vulnerabilities in an AI system, often in a controlled environment and in collaboration with the system's developers.[^s4] In the context of large language models, red teams look for outputs such as offensive or discriminatory text, leaked private or training data, dangerous assistance, and failures that only appear over multi-turn conversations.[^s1][^s2]

## Origins

The term predates AI. Feffer and colleagues trace it to military practice, where the US military used "red teams" in the 1960s to model the Soviet Union as an opponent, and to computer security, where a red team emulates an adversary to map an organisation's weaknesses.[^s3] They stress that security red teaming differs from both penetration testing and auditing: it is open-ended adversary emulation rather than a checklist of known controls.[^s3] For language models, two 2022 papers set much of the vocabulary. Perez et al. (DeepMind, EMNLP 2022) proposed using one language model to generate test cases that elicit harmful replies from another,[^s1] and Ganguli et al. (Anthropic) published a large human red-teaming study with its full instructions and data.[^s2]

## How it works

A red-teaming exercise defines a target (a base model, a fine-tuned assistant, or a full application), a threat model (which harms and which adversaries are in scope), and a team, which can be domain experts, crowdworkers, or other models.[^s3] Testers then probe the system, record the attempts that succeed, and hand those findings to developers, who use them to retrain, filter or otherwise mitigate the behaviour.[^s2][^s3]

- **Manual red teaming.** Ganguli et al. had human testers hold open-ended conversations with models of three sizes (2.7B, 13B and 52B parameters) and four kinds: a plain language model, a prompted helpful-honest-harmless model, a rejection-sampling model, and a model trained with RLHF. They released 38,961 red-team attacks as a dataset.[^s2]
- **Automated (model-based) red teaming.** Perez et al. had a "red" language model write test inputs and used a classifier to flag offensive replies from a 280-billion-parameter target chatbot, comparing methods from zero-shot generation to reinforcement learning.[^s1] Automation scales coverage cheaply, but the classifier and the red model limit which failures can be found.[^s1][^s3]

## Evidence, limitations and open questions

The empirical results are mixed but informative. Ganguli et al. found that RLHF-trained models became harder to red team as they grew, while the other model types showed roughly flat trends with scale.[^s2] Perez et al. found that model-generated tests uncovered many harmful replies that hand-written tests would be too costly to find, and the authors present the method as one tool among several rather than a complete solution.[^s1]

Critics argue the practice is poorly defined. Reviewing six public exercises, mostly run by industry, and 104 research papers, Feffer et al. found wide variation in purpose, threat model, team composition, resources and disclosure. Only half of the exercises shared examples of harmful outputs, and none reported full costs.[^s3] They argue that treating red teaming as a catch-all answer to safety and regulation risks becoming "security theater". Instead they call for standardised reporting of resources, goals met and mitigations taken, and for red teaming to sit inside a broader evaluation toolkit.[^s3] Who should red team, whose values define harm, and how strong an adversary to assume all remain open questions.[^s3]

## In practice and policy

Red teaming has become a standard pre-release step for frontier language models, and it moved into US policy in 2023. Executive Order 14110 directed NIST to develop red-teaming guidelines. It also required developers of potential dual-use foundation models to report red-team results to the federal government, including tests related to biological-weapons uplift, software vulnerability discovery, influence operations and self-replication.[^s4] EO 14110 was revoked on January 20, 2025, by Executive Order 14148, so as of 2026 those reporting requirements no longer apply under that order.[^s5] Security topics are covered here at the level of concepts and mitigations only.

## Connections

Red teaming is a method within **evaluation of AI systems**, supplying the adversarial, open-ended complement to static benchmarks.[^s3] Most published work targets **large language models**, and Ganguli et al.'s scaling result directly concerns **RLHF**-trained models.[^s2] Red teams commonly hunt for **jailbreaks** and **prompt injection**, and the practice feeds the measurement activities of the **NIST AI Risk Management Framework**.[^s1][^s3] It was **regulated by** US **executive orders on AI**, notably EO 14110 and its revocation.[^s4][^s5] It **contrasts with penetration testing**, which checks known controls rather than emulating an open-ended adversary.[^s3]

## Sources

[^s1]: Perez, Huang, Song, Cai, Ring, Aslanides, Glaese, McAleese and Irving, "Red Teaming Language Models with Language Models", EMNLP 2022. https://aclanthology.org/2022.emnlp-main.225 (accessed 2026-10-31)
[^s2]: Ganguli et al., "Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned", arXiv:2209.07858, 2022. https://arxiv.org/abs/2209.07858v1 (accessed 2026-10-31)
[^s3]: Feffer, Sinha, Deng, Lipton and Heidari, "Red-Teaming for Generative AI: Silver Bullet or Security Theater?", arXiv:2401.15897v3. https://arxiv.org/html/2401.15897v3 (accessed 2026-10-31)
[^s4]: Executive Order 14110, "Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence", October 30, 2023, 3 CFR (2024). https://govinfo.gov/content/pkg/CFR-2024-title3-vol1/pdf/CFR-2024-title3-vol1-eo14110.pdf (accessed 2026-10-31)
[^s5]: Executive Order 14148, "Initial Rescissions of Harmful Executive Orders and Actions", January 20, 2025. https://www.govinfo.gov/content/pkg/DCPD-202500115/html/DCPD-202500115.htm (accessed 2026-10-31)
