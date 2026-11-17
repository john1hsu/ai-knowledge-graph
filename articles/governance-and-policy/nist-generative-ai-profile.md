---
id: kt:nist-generative-ai-profile
type: Policy
title: NIST Generative AI Profile
aliases: [NIST AI 600-1, Generative Artificial Intelligence Profile, GAI Profile, AI RMF Generative AI Profile]
domain: governance-and-policy
summary: >-
  NIST AI 600-1, a voluntary July 2024 companion to the NIST AI Risk Management Framework that names twelve risks
  unique to or worsened by generative AI and maps suggested risk-management actions onto the framework's Govern,
  Map, Measure and Manage functions.
maturity: established
broader: [kt:nist-ai-risk-management-framework, kt:ai-risk-management]
related: [kt:executive-orders-on-ai, kt:red-teaming, kt:generative-model, kt:content-provenance]
relations:
  - {predicate: createdBy, object: kt:nist}
  - {predicate: mitigates, object: kt:hallucination}
  - {predicate: mitigates, object: kt:prompt-injection}
sources:
  - id: s1
    title: "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)"
    publisher: National Institute of Standards and Technology, July 2024
    url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
    type: government
    accessed: 2026-11-17
  - id: s2
    title: "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (publication record)"
    publisher: National Institute of Standards and Technology
    url: https://www.nist.gov/node/1855536
    type: government
    accessed: 2026-11-17
  - id: s3
    title: "Biden-Harris Administration Announces New NIST Public Working Group on AI"
    publisher: National Institute of Standards and Technology, 22 June 2023
    url: https://www.nist.gov/news-events/news/2023/06/biden-harris-administration-announces-new-nist-public-working-group-ai
    type: government
    accessed: 2026-11-17
  - id: s4
    title: "Winning the Race: America's AI Action Plan"
    publisher: The White House, July 2025
    url: https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf
    type: government
    accessed: 2026-11-17
  - id: s5
    title: "Crosswalk between NIST AI 600-1 and IMDA AI Verify"
    publisher: NIST AI Resource Center (AIRC), May 2025
    url: https://airc.nist.gov/documents/1/20250527-Crosswalk_NIST_600-1_IMDA_AI_Verify.pdf
    type: government
    accessed: 2026-11-17
created: 2026-11-17
---

# NIST Generative AI Profile

The **NIST Generative AI Profile**, published as NIST AI 600-1 on 26 July 2024, is a cross-sectoral profile of the NIST AI Risk Management Framework (AI RMF 1.0) that applies the framework specifically to generative AI. Its authors include Chloe Autio, Reva Schwartz, Elham Tabassi and others. Like its parent framework, it is voluntary guidance rather than regulation: it helps organizations build trustworthiness into how they design, develop, deploy and evaluate generative systems.[^s2] The profile borrows the definition of generative AI from Executive Order 14110, meaning models that produce derived synthetic content such as text, images, audio or video, and in practice it focuses on generative foundation models.[^s1]

## Origin

NIST wrote the profile under Executive Order 14110 on safe, secure and trustworthy AI.[^s2] It started with a Public Working Group on Generative AI, which NIST announced on 22 June 2023. The group's short-term goal was to collect input on a profile showing how the AI RMF could support generative AI development. Its later goals covered testing and measurement work, including NIST's involvement in the DEF CON 2023 AI Village.[^s3] The final document also drew on public comments on a draft and on several requests for information.[^s1] The working group raised four main considerations that run through the profile: governance, content provenance, pre-deployment testing and incident disclosure.[^s1]

## The twelve risks

The core of the profile is a list of twelve risks that generative AI either creates or makes worse:[^s1]

1. **CBRN information or capabilities**: easier access to, or synthesis of, information that could help someone design chemical, biological, radiological or nuclear weapons.[^s1]
2. **Confabulation**: false content stated with confidence, often called hallucination.[^s1]
3. **Dangerous, violent or hateful content**.[^s1]
4. **Data privacy**: leakage or de-anonymization of personal data.[^s1]
5. **Environmental impacts** of compute-heavy training and inference.[^s1]
6. **Harmful bias or homogenization**: amplified bias and overly uniform outputs.[^s1]
7. **Human-AI configuration**: risks such as automation bias, over-reliance and emotional entanglement.[^s1]
8. **Information integrity**: content that blurs fact and fiction and helps disinformation spread at scale.[^s1]
9. **Information security**: lower barriers to offensive cyber operations, plus new attack surfaces such as prompt injection and data poisoning.[^s1]
10. **Intellectual property**: unauthorized reproduction of protected content.[^s1]
11. **Obscene, degrading or abusive content**, including synthetic sexual-abuse imagery and non-consensual intimate imagery.[^s1]
12. **Value chain and component integration**: poorly vetted third-party data, models and components that weaken transparency and accountability.[^s1]

The profile also classifies risks along several dimensions. These are the lifecycle stage (design through decommissioning), the scope (a single model, an application, or the wider ecosystem), the source (training, inputs, outputs or human behaviour) and the time scale (sudden onset or slow build-up).[^s1]

## How it works

The bulk of the document is a set of tables of **suggested actions**, grouped under AI RMF subcategories in the four functions Govern (GV), Map (MP), Measure (MS) and Manage (MG). Each action has an identifier that combines the function, the subcategory and a sequence number. For example, GV-1.1-001 is the first action under Govern 1.1. Each row also lists the generative AI risks the action addresses and the AI actor tasks involved. Not every AI RMF subcategory is covered. NIST says how much each action applies depends on the organization and on the actor's role.[^s1] In practice, teams use the risk list as a checklist when scoping a generative AI deployment and use the action IDs to show coverage. NIST's resource center has also published crosswalks that map the profile's actions to other frameworks. One example, dated May 2025, maps them to Singapore's AI Verify testing framework.[^s5]

## Limitations and open questions

Because the profile is voluntary, it relies on organizations choosing to adopt it, and its suggested actions are not pass/fail controls.[^s1] Its political basis has also changed. America's AI Action Plan of July 2025 told NIST to revise the AI RMF to remove references to misinformation, diversity, equity and inclusion, and climate change.[^s4] Those themes overlap with the profile's information-integrity, bias and environmental risks. NIST's publication page shows the record was updated in April 2026 but does not describe any change.[^s2] Readers should check whether a revised version has replaced the 2024 text.

## Connections

The profile is **part of** the **NIST AI Risk Management Framework** and is a concrete tool for **AI risk management** more broadly. It was **created by NIST** under one of the US **executive orders on AI**.[^s2] Several of its twelve risks are covered by their own nodes. Its suggested actions aim to **mitigate** confabulation (**hallucination**) and security threats such as **prompt injection**.[^s1] It names pre-deployment testing, including **red teaming**, and **content provenance** as main considerations, and it applies to **generative models** in general.[^s1] The 2025 Action Plan shows how US federal policy can reshape a voluntary framework.[^s4]

## Sources

[^s1]: NIST, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (NIST AI 600-1), July 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf (accessed 2026-11-17)
[^s2]: NIST, publication record for NIST AI 600-1 (Autio, Schwartz, Dunietz, Jain, Stanley, Tabassi, Hall, Roberts). https://www.nist.gov/node/1855536 (accessed 2026-11-17)
[^s3]: NIST, "Biden-Harris Administration Announces New NIST Public Working Group on AI", 22 June 2023. https://www.nist.gov/news-events/news/2023/06/biden-harris-administration-announces-new-nist-public-working-group-ai (accessed 2026-11-17)
[^s4]: The White House, "Winning the Race: America's AI Action Plan", July 2025. https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf (accessed 2026-11-17)
[^s5]: NIST AI Resource Center, "Crosswalk between NIST AI 600-1 and IMDA AI Verify", May 2025. https://airc.nist.gov/documents/1/20250527-Crosswalk_NIST_600-1_IMDA_AI_Verify.pdf (accessed 2026-11-17)
