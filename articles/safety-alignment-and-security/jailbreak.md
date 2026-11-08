---
id: kt:jailbreak
type: Risk
title: Jailbreak
aliases: [jailbreaking, LLM jailbreak, jailbreak attack, direct prompting attack]
domain: safety-alignment-and-security
summary: >-
  An attack in which a user crafts direct inputs to a safety-trained AI model so that it circumvents the
  restrictions its developer placed on its outputs, typically getting it to produce content it was trained to refuse.
maturity: emerging
broader: [kt:adversarial-machine-learning]
related: [kt:red-teaming, kt:rlhf, kt:large-language-model, kt:ai-alignment]
relations:
  - {predicate: contrastsWith, object: kt:prompt-injection}
  - {predicate: exploits, object: kt:in-context-learning}
sources:
  - id: s1
    title: "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (NIST AI 100-2 E2025)"
    publisher: NIST (Vassilev, Oprea, Fordyce, Anderson, Davies, Hamin), March 2025
    url: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf
    type: government
    accessed: 2026-11-08
  - id: s2
    title: "Jailbroken: How Does LLM Safety Training Fail?"
    publisher: NeurIPS 2023 (Wei, Haghtalab, Steinhardt)
    url: https://neurips.cc/virtual/2023/poster/70702
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s3
    title: "Universal and Transferable Adversarial Attacks on Aligned Language Models"
    publisher: arXiv:2307.15043 (Zou, Wang, Carlini, Nasr, Kolter, Fredrikson), 2023
    url: https://arxiv.org/abs/2307.15043
    type: primary
    accessed: 2026-11-08
  - id: s4
    title: "Many-shot jailbreaking"
    publisher: Anthropic, 2 April 2024
    url: https://www.anthropic.com/research/many-shot-jailbreaking
    type: lab-research
    accessed: 2026-11-08
  - id: s5
    title: "Constitutional Classifiers: Defending against universal jailbreaks"
    publisher: Anthropic, 3 February 2025 (updated 13 February 2025)
    url: https://www.anthropic.com/news/constitutional-classifiers
    type: lab-research
    accessed: 2026-11-08
created: 2026-11-08
---

# Jailbreak

A **jailbreak** is an attack on a generative AI model in which the user's own input is designed to get around the restrictions a developer has placed on the model's outputs, most often its trained tendency to refuse harmful requests. NIST's adversarial machine learning taxonomy (NIST AI 100-2 E2025) classifies jailbreaks as a kind of *direct prompting attack*: the attacker is the person typing to the model, and the goal is misuse that the model's safeguards were meant to block.[^s1] The term became widespread after early public chatbots such as ChatGPT were shown to be talked out of their safety behaviour, a pattern Wei, Haghtalab and Steinhardt studied systematically at NeurIPS 2023.[^s2]

## Why safety training fails

Wei et al. tested then-leading models, including GPT-4 and Claude v1.3, and proposed two root causes for jailbreak success.[^s2] **Competing objectives** arise when a model's helpfulness or instruction-following goals pull against its safety goals, so a request framed to reward compliance can outweigh the learned refusal. **Mismatched generalization** arises when pretraining gave the model a capability (for example, handling an unusual encoding or format) that safety training never covered, so refusals do not transfer to that input domain. Attacks designed around these two failure modes succeeded on every prompt in a set of unsafe requests drawn from the models' own red-teaming evaluations, despite extensive safety work. The authors argued that scaling alone will not fix this and called for "safety-capability parity", meaning safeguards as sophisticated as the model they protect.[^s2]

## Families of techniques

NIST groups jailbreak techniques into three broad families, described here only at the conceptual level.[^s1]

- **Optimization-based attacks** treat jailbreaking as a search problem, using gradients or search over tokens to find inputs that maximize the chance of a non-refusal. Zou et al. (2023) showed that an automatically found adversarial suffix, optimized on open models (Vicuna-7B and 13B), also transferred to other open models and to the public interfaces of commercial chatbots, which made such attacks cheap and *universal* rather than hand-crafted and fragile.[^s3]
- **Manual methods** exploit competing objectives (for instance, role-play or instructions that discourage refusing) or mismatched generalization (for instance, obfuscating a request through encodings or transformations).[^s1][^s2]
- **Automated model-based red teaming** uses an attacker model, the target model and a judge model in a loop to discover jailbreaks at scale, including multi-turn attacks that escalate gradually across a conversation.[^s1]

A notable long-context variant is **many-shot jailbreaking**, reported by Anthropic in April 2024: filling a very long prompt with many fabricated dialogue examples makes a model more likely to comply with a final harmful request. Anthropic found effectiveness rose with the number of examples following a power law similar to benign in-context learning, and that larger models were often more susceptible, so the growth of context windows from thousands to a million or more tokens widened this attack surface.[^s4]

## Defences and their limits

NIST lists mitigations at three stages: training (safety training and adversarial training), evaluation (automated vulnerability scans, expert red teaming, bug bounties and continuous post-deployment testing) and deployment (input and output classifiers, prompt modification, monitoring and usage restrictions).[^s1] It cautions that current models remain highly vulnerable to direct prompting attacks and that detection systems can themselves be attacked.[^s1]

Classifier-based defences have shown measurable gains in lab reports. Anthropic said in April 2024 that classifying and modifying prompts cut one many-shot attack's success rate from 61% to 2%, whereas fine-tuning the model to refuse only delayed the attack.[^s4] In February 2025 it described *Constitutional Classifiers*, input and output classifiers trained on synthetic data generated from a natural-language constitution of permitted and forbidden content. In Anthropic's automated tests on Claude 3.5 Sonnet, jailbreak success fell from 86% to 4.4%, with a 0.38% rise in refusals and 23.7% more compute.[^s5] These are the developer's own figures; in a subsequent public demo, one of 339 participants found a universal jailbreak, illustrating that defences raise attacker cost rather than eliminating the risk.[^s5]

## Connections

Jailbreaks are a subclass of **adversarial machine learning** attacks targeting generative models, as NIST's taxonomy places them.[^s1] They are the main thing **red teaming** of language models tries to find, and the failure they expose is in safety training such as **RLHF**, which shapes refusal behaviour that jailbreaks route around.[^s2] They contrast with **prompt injection**: NIST treats direct prompting (the user attacks the model) separately from indirect prompt injection (malicious instructions hidden in data the system retrieves), even though the techniques overlap.[^s1] Many-shot jailbreaking exploits **in-context learning**, linking jailbreak risk to the growth of **large language model** context windows.[^s4] More broadly, jailbreaks are evidence for the gap between a model's capabilities and its intended behaviour that **AI alignment** research seeks to close.[^s2]

## Sources
[^s1]: Vassilev et al., "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations", NIST AI 100-2 E2025, March 2025. https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf (accessed 2026-11-08)
[^s2]: Wei, Haghtalab and Steinhardt, "Jailbroken: How Does LLM Safety Training Fail?", NeurIPS 2023. https://neurips.cc/virtual/2023/poster/70702 (accessed 2026-11-08)
[^s3]: Zou et al., "Universal and Transferable Adversarial Attacks on Aligned Language Models", arXiv:2307.15043, 2023. https://arxiv.org/abs/2307.15043 (accessed 2026-11-08)
[^s4]: Anthropic, "Many-shot jailbreaking", 2 April 2024. https://www.anthropic.com/research/many-shot-jailbreaking (accessed 2026-11-08)
[^s5]: Anthropic, "Constitutional Classifiers: Defending against universal jailbreaks", February 2025. https://www.anthropic.com/news/constitutional-classifiers (accessed 2026-11-08)
