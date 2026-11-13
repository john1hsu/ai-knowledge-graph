---
id: kt:prompt-injection
type: Risk
title: Prompt injection
aliases: [prompt injection attack, indirect prompt injection, direct prompt injection, LLM01]
domain: safety-alignment-and-security
summary: >-
  A class of attacks on applications built around language models in which text supplied by a user or embedded
  in content the model reads is interpreted as instructions, overriding or subverting what the developer intended.
maturity: emerging
broader: [kt:adversarial-machine-learning]
related: [kt:ai-agent, kt:red-teaming, kt:retrieval-augmented-generation, kt:instruction-hierarchy]
relations:
  - {predicate: contrastsWith, object: kt:jailbreak}
  - {predicate: exploits, object: kt:tool-use}
sources:
  - id: s1
    title: "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (NIST AI 100-2 E2025)"
    publisher: NIST (Vassilev, Oprea, Fordyce, Anderson, Davies, Hamin), March 2025
    url: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf
    type: government
    accessed: 2026-11-13
  - id: s2
    title: "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection"
    publisher: arXiv:2302.12173 (Greshake, Abdelnabi, Mishra, Endres, Holz, Fritz), 2023
    url: https://arxiv.org/abs/2302.12173v2
    type: primary
    accessed: 2026-11-13
  - id: s3
    title: "Formalizing and Benchmarking Prompt Injection Attacks and Defenses"
    publisher: USENIX Security 2024 (Liu, Jia, Geng, Jia, Gong)
    url: https://www.usenix.org/conference/usenixsecurity24/presentation/liu-yupei
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions"
    publisher: arXiv:2404.13208 (Wallace, Xiao, Leike, Weng, Heidecke, Beutel), 2024
    url: https://arxiv.org/abs/2404.13208v1
    type: primary
    accessed: 2026-11-13
  - id: s5
    title: "LLM01:2025 Prompt Injection"
    publisher: OWASP Gen AI Security Project, Top 10 for LLM Applications 2025
    url: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
    type: community
    accessed: 2026-11-13
  - id: s6
    title: "What's Old Is New Again: GPT-3 Prompt Injection Attack Affects AI"
    publisher: Hackaday, 16 September 2022
    url: https://hackaday.com/2022/09/16/whats-old-is-new-again-gpt-3-prompt-injection-attack-affects-ai
    type: news
    accessed: 2026-11-13
created: 2026-11-13
---

# Prompt injection

**Prompt injection** is an attack on systems that wrap a large language model in an application: input text is crafted so the model treats it as instructions, changing the application's behaviour or output in ways its developer did not intend.[^s5] The root cause is that a language model receives the developer's instructions, the user's request and any retrieved data as one stream of tokens, with no hard boundary between "code" and "data".[^s2] OWASP ranks it first (LLM01) in its 2025 Top 10 for LLM applications, and notes the injected text need not be visible to a human as long as the model parses it.[^s5]

## Origin

The problem came to public attention in September 2022, when Riley Goodside showed that a GPT-3 translation prompt could be told to disregard its task and print attacker-chosen text instead.[^s6] Simon Willison named the behaviour "prompt injection" and argued it was a genuine security flaw rather than a curiosity, by analogy to SQL injection, where user-supplied data ends up executed as commands.[^s6] In February 2023, Greshake and colleagues extended the idea to **indirect prompt injection**: an attacker who never talks to the application plants instructions in content it will later retrieve, such as a web page or document. They demonstrated practical attacks on Bing's GPT-4-powered chat and on code-completion tools, and catalogued impacts including data theft, worm-like propagation and contamination of the information ecosystem.[^s2]

## Direct and indirect forms

NIST's 2025 adversarial machine learning taxonomy separates the two settings by who the attacker is.[^s1] In **direct prompting attacks** the attacker is the primary user with query access; direct prompt injection is the subset where the user's text is appended to higher-trust instructions such as a system prompt. Goals include enabling misuse, extracting the system prompt or other private context, and manipulating tool or API calls.[^s1] In **indirect prompt injection** a third party controls a resource the system ingests. NIST groups the consequences into availability attacks (for example, triggering slow background tasks or disabling an API), integrity attacks (such as poisoning a retrieval knowledge base or self-propagating injections) and privacy compromises (leaking data from connected resources to the attacker).[^s1] OWASP adds that multimodal systems widen the attack surface, since instructions can be hidden in an image that accompanies harmless text.[^s5]

## Relation to jailbreaking

The terms are often used interchangeably. OWASP treats jailbreaking as a form of prompt injection whose aim is to make the model drop its safety rules altogether, whereas prompt injection more broadly is about steering an application's behaviour.[^s5] NIST draws the line by threat model instead: direct prompting by the user versus injection through third-party data, while acknowledging that the techniques overlap.[^s1]

## Defences and their limits

Liu et al. formalized prompt injection as a general framework in which earlier attacks are special cases, and benchmarked 5 attacks against 10 defences across 10 LLMs and 7 tasks (USENIX Security 2024), releasing an open platform for further evaluation.[^s3] Model-level defences train the model to weigh instructions by source. Wallace et al. observed that models tend to give a developer's system prompt the same weight as text from users or third parties, and proposed an **instruction hierarchy** specifying which instructions win when priorities conflict; they generated training data teaching GPT-3.5 to ignore conflicting lower-privilege instructions; the authors report substantially better robustness, including on attack types not seen in training, with minimal capability loss (2024).[^s4] Deployment-level measures listed by NIST include delimiting or "spotlighting" untrusted content, LLM-based detectors, and designing systems on the assumption that injection will succeed, for example by splitting work across models with different permissions.[^s1] OWASP's guidance stresses least privilege, deterministic validation of output formats, human approval for high-risk actions, and regular adversarial testing.[^s5] Neither source treats the problem as solved: NIST states that current mitigations do not fully protect against all attacker techniques, and OWASP notes that retrieval augmentation and fine-tuning do not fully mitigate it.[^s1][^s5]

## Connections

Prompt injection is a branch of **adversarial machine learning**, which is why NIST's taxonomy is the main framing here.[^s1] It **contrasts with** **jailbreak**: both use crafted text, but they differ in attacker and goal.[^s1][^s5] It **exploits** **tool use**, because model-chosen API calls are what turn injected text into real actions, and severity grows with the agency granted to an **AI agent**.[^s2][^s5] Indirect injection targets **retrieval-augmented generation** pipelines, whose retrieved passages are a natural carrier for planted instructions.[^s1] The **instruction hierarchy** is a model-side mitigation, and **red teaming** is the main way practitioners probe for these weaknesses before deployment.[^s4][^s5]

## Sources
[^s1]: NIST, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations" (NIST AI 100-2 E2025), March 2025. https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf (accessed 2026-11-13)
[^s2]: Greshake et al., "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection", arXiv:2302.12173, 2023. https://arxiv.org/abs/2302.12173v2 (accessed 2026-11-13)
[^s3]: Liu et al., "Formalizing and Benchmarking Prompt Injection Attacks and Defenses", USENIX Security 2024. https://www.usenix.org/conference/usenixsecurity24/presentation/liu-yupei (accessed 2026-11-13)
[^s4]: Wallace et al., "The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions", arXiv:2404.13208, 2024. https://arxiv.org/abs/2404.13208v1 (accessed 2026-11-13)
[^s5]: OWASP Gen AI Security Project, "LLM01:2025 Prompt Injection". https://genai.owasp.org/llmrisk/llm01-prompt-injection/ (accessed 2026-11-13)
[^s6]: Hackaday, "What's Old Is New Again: GPT-3 Prompt Injection Attack Affects AI", 16 September 2022. https://hackaday.com/2022/09/16/whats-old-is-new-again-gpt-3-prompt-injection-attack-affects-ai (accessed 2026-11-13)
