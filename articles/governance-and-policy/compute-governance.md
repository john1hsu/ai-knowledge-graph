---
id: kt:compute-governance
type: Concept
title: Compute governance
aliases: [governance of computing power, compute-based AI governance, compute thresholds]
domain: governance-and-policy
summary: >-
  The use of computing power (the chips, data centres and processing used to train and run AI models) as a
  lever for AI policy: measuring, allocating or restricting compute to gain visibility into AI development,
  steer it toward beneficial uses, and enforce limits on risky or malicious work.
maturity: emerging
broader: [kt:ai-governance]
related: [kt:eu-ai-act, kt:executive-orders-on-ai, kt:ai-accelerator, kt:ai-safety-institutes, kt:computing-power-and-the-governance-of-artificial-intelligence]
relations:
  - {predicate: hasPart, object: kt:ai-chip-export-controls}
  - {predicate: dependsOn, object: kt:scaling-laws}
  - {predicate: influencedBy, object: kt:computing-power-and-the-governance-of-artificial-intelligence}
sources:
  - id: s1
    title: "Computing Power and the Governance of Artificial Intelligence (arXiv 2402.08797)"
    publisher: Sastry, Heim, Belfield, Anderljung, Brundage et al., authors' arXiv version, 13 February 2024
    url: https://arxiv.org/abs/2402.08797
    type: primary
    accessed: 2026-11-11
  - id: s2
    title: "Computing Power and the Governance of Artificial Intelligence (full text, HTML v1)"
    publisher: Sastry et al., arXiv HTML rendering of v1
    url: https://arxiv.org/html/2402.08797v1
    type: primary
    accessed: 2026-11-11
  - id: s3
    title: "Executive Order 14110: Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence"
    publisher: The White House; Federal Register 88(210), 1 November 2023
    url: https://www.govinfo.gov/content/pkg/FR-2023-11-01/html/2023-24283.htm
    type: government
    accessed: 2026-11-11
  - id: s4
    title: "Executive Order 14148: Initial Rescissions of Harmful Executive Orders and Actions"
    publisher: The American Presidency Project, University of California, Santa Barbara (order dated 20 January 2025)
    url: https://www.presidency.ucsb.edu/documents/executive-order-14148-initial-rescissions-harmful-executive-orders-and-actions
    type: academic
    accessed: 2026-11-11
  - id: s5
    title: "AI Act, Article 51: Classification of general-purpose AI models as general-purpose AI models with systemic risk"
    publisher: European Commission, AI Act Service Desk (based on Regulation (EU) 2024/1689, EUR-Lex consolidated text)
    url: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-51
    type: government
    accessed: 2026-11-11
  - id: s6
    title: "On the Limitations of Compute Thresholds as a Governance Strategy (arXiv 2407.05694, v2)"
    publisher: Sara Hooker, authors' arXiv version, July 2024
    url: https://arxiv.org/abs/2407.05694v2
    type: primary
    accessed: 2026-11-11
  - id: s7
    title: "SB 53 (Wiener): Artificial intelligence models: large developers — committee analysis"
    publisher: California State Assembly, Committee on Privacy and Consumer Protection (hearing of 11 September 2025)
    url: https://apcp.assembly.ca.gov/media/1019
    type: government
    accessed: 2026-11-11
created: 2026-11-11
---

# Compute governance

**Compute governance** is the idea of using computing power ("compute") as a point of control for AI policy. Training and running modern AI systems requires specialised chips housed in large data centres, so whoever can see, allocate or restrict that hardware has leverage over who builds which models and how. The concept was set out systematically in a February 2024 paper by Girish Sastry, Lennart Heim and 17 co-authors from academia, think tanks and AI labs (including Yoshua Bengio and Diane Coyle), which argued that governments were already using compute as a policy tool, through domestic investment, export restrictions and subsidised access, but had barely explored its potential.[^s1]

## Why compute is a governance lever

Sastry et al. contrast compute with the other two inputs to AI, data and algorithms, which are easy to copy and hard to observe. Compute, they argue, has four properties that make it governable: its use is **detectable**, access to it is **excludable**, it is **quantifiable**, and it comes from a highly **concentrated supply chain** with very few producers.[^s1] Its importance has grown with scale: the paper reports that training compute for notable ML systems has doubled roughly every six months, about a 350-million-fold rise over 13 years, while GPU price-performance doubles only every two to two-and-a-half years, so most of the growth comes from bigger clusters and more spending.[^s2] That spending makes large training runs visible and costly to hide.

## Three functions

The paper groups compute-based policies by what they let governments do.[^s1][^s2]

- **Visibility**: estimating actors' capabilities from compute data, mandatory reporting of large training runs by developers and cloud providers, an international chip registry, and privacy-preserving workload monitoring.[^s2]
- **Allocation**: directing compute toward beneficial research, redistributing access across and within countries, influencing the overall pace of progress, or pooling resources in a joint megaproject.[^s2]
- **Enforcement**: physical limits on chip-to-chip networking to cap cluster size, hardware-based remote enforcement, multiparty control over risky training runs, and digital norm enforcement.[^s2]

The authors stress that these options differ in readiness: some are already being piloted, while hardware-level mechanisms need foundational research.[^s1]

## Compute thresholds in law

The most widespread tool so far is a **training-compute threshold** that triggers obligations. US Executive Order 14110 (October 2023) required reports from anyone training a model with more than 10^26 integer or floating-point operations (10^23 for models trained mainly on biological sequence data) and from owners of clusters linked by networking above 100 Gbit/s with a theoretical peak of 10^20 operations per second; it also asked Commerce to make US cloud providers report large training runs by foreign customers and verify their identities.[^s3] That order was revoked on 20 January 2025 by Executive Order 14148.[^s4] The EU AI Act, by contrast, remains in force: Article 51 presumes a general-purpose AI model has high-impact capabilities, and so systemic risk, when its cumulative training compute exceeds 10^25 floating-point operations, and lets the Commission amend that threshold by delegated act as technology changes.[^s5] At the state level, California's SB 53, as analysed by the Assembly in September 2025, defined a "frontier model" as a foundation model trained with more than 10^26 operations and reserved its heaviest duties for developers with over $500 million in annual revenue.[^s7]

## Critiques and limitations

The approach is contested. Sara Hooker argues that compute thresholds as currently written are shortsighted, because the link between compute and risk is uncertain and shifting, and fixed cut-offs overstate how well anyone can predict which capabilities appear at which scale.[^s6] Sastry et al. acknowledge similar limits: algorithmic and hardware efficiency gains erode any fixed threshold; small, narrow models can still be dangerous; most compute is now spent on inference rather than training; and openly released models can run without centrally controlled hardware.[^s2] They also warn that poorly designed compute governance threatens privacy, leaks commercial secrets and concentrates power, and propose guardrails: exclude small-scale and non-AI compute, invest in privacy-preserving techniques, use ex ante compute controls only where justified, revisit controlled technologies regularly, and attach procedural safeguards.[^s2]

## Connections

Compute governance is a branch of **AI governance**, and **AI chip export controls** are its most developed real-world instrument, so that article sits beneath this one.[^s1] It **depends on** the empirical regularity captured by **scaling laws**: compute is a useful proxy only while capability rises predictably with training compute, which is exactly the assumption Hooker challenges.[^s6] The thresholds in **executive orders on AI** and the **EU AI Act** are its main legal expressions, and they target the **AI accelerators** whose concentrated supply makes the lever possible.[^s3][^s5] Government **AI safety institutes** are a related part of the same policy landscape. The 2024 paper *Computing Power and the Governance of Artificial Intelligence* is the framework most later debate builds on.[^s1]

## Sources

[^s1]: G. Sastry, L. Heim, H. Belfield et al., "Computing Power and the Governance of Artificial Intelligence", arXiv:2402.08797, 13 February 2024. https://arxiv.org/abs/2402.08797 (accessed 2026-11-11)
[^s2]: Sastry et al., full text (HTML v1). https://arxiv.org/html/2402.08797v1 (accessed 2026-11-11)
[^s3]: Executive Order 14110, "Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence", Federal Register, 1 November 2023. https://www.govinfo.gov/content/pkg/FR-2023-11-01/html/2023-24283.htm (accessed 2026-11-11)
[^s4]: Executive Order 14148, "Initial Rescissions of Harmful Executive Orders and Actions", 20 January 2025, The American Presidency Project. https://www.presidency.ucsb.edu/documents/executive-order-14148-initial-rescissions-harmful-executive-orders-and-actions (accessed 2026-11-11)
[^s5]: European Commission AI Act Service Desk, Article 51 of Regulation (EU) 2024/1689. https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-51 (accessed 2026-11-11)
[^s6]: S. Hooker, "On the Limitations of Compute Thresholds as a Governance Strategy", arXiv:2407.05694v2, July 2024. https://arxiv.org/abs/2407.05694v2 (accessed 2026-11-11)
[^s7]: California State Assembly Committee on Privacy and Consumer Protection, analysis of SB 53 (Wiener), September 2025. https://apcp.assembly.ca.gov/media/1019 (accessed 2026-11-11)
