---
id: kt:nist-ai-risk-management-framework
type: Policy
title: NIST AI Risk Management Framework
aliases: [AI RMF, NIST AI RMF, AI RMF 1.0, NIST AI 100-1]
domain: governance-and-policy
summary: >-
  A voluntary, sector-neutral framework published by the US National Institute of Standards and Technology in
  January 2023 that helps organizations identify, assess and manage the risks of AI systems through four core
  functions (Govern, Map, Measure, Manage) and a set of trustworthiness characteristics.
maturity: established
broader: [kt:ai-governance, kt:ai-risk-management]
related: [kt:ai-evaluation, kt:red-teaming, kt:iso-iec-42001, kt:eu-ai-act, kt:executive-orders-on-ai]
relations:
  - {predicate: createdBy, object: kt:nist}
  - {predicate: hasPart, object: kt:nist-generative-ai-profile}
sources:
  - id: s1
    title: "Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1"
    publisher: National Institute of Standards and Technology (Tabassi), 26 January 2023
    url: https://www.nist.gov/node/1731741
    type: government
    accessed: 2026-10-31
  - id: s2
    title: "AI RMF 1.0 — Executive Summary"
    publisher: NIST Trustworthy and Responsible AI Resource Center (AIRC)
    url: https://airc.nist.gov/airmf-resources/airmf/0-ai-rmf-1-0
    type: government
    accessed: 2026-10-31
  - id: s3
    title: "AI RMF Core"
    publisher: NIST Trustworthy and Responsible AI Resource Center (AIRC)
    url: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
    type: government
    accessed: 2026-10-31
  - id: s4
    title: "AI Risks and Trustworthiness"
    publisher: NIST Trustworthy and Responsible AI Resource Center (AIRC)
    url: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/
    type: government
    accessed: 2026-10-31
  - id: s5
    title: "AI Risk Management Framework FAQs"
    publisher: National Institute of Standards and Technology (page updated 13 August 2026)
    url: https://www.nist.gov/artificial-intelligence/ai-risk-management-framework-faqs
    type: government
    accessed: 2026-10-31
  - id: s6
    title: "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)"
    publisher: National Institute of Standards and Technology, 26 July 2024
    url: https://www.nist.gov/node/1855536
    type: government
    accessed: 2026-10-31
created: 2026-10-31
---

# NIST AI Risk Management Framework

The **NIST AI Risk Management Framework** (AI RMF 1.0, published as NIST AI 100-1) is guidance from the US National Institute of Standards and Technology for organizations that design, develop, deploy or use AI systems. Its aim is to help them manage AI risks and promote trustworthy, responsible AI. It was released on 26 January 2023, with Elham Tabassi as the listed author, and was written at the direction of the National Artificial Intelligence Initiative Act of 2020.[^s1] The framework is voluntary. NIST describes it as rights-preserving, not specific to any sector, and agnostic about use case, so it can apply to organizations of any size.[^s1][^s2]

## Origin and development

Congress asked NIST for a voluntary framework, and NIST built it through a public, consensus-oriented process. A request for information went out in July 2021 and a concept paper followed in December 2021. A first draft appeared in March 2022 and a second in August 2022, with public workshops and comment periods in between. Version 1.0 was released in January 2023.[^s5] NIST calls the document a living one that it reviews periodically. Alongside the framework it maintains a Playbook of suggested actions. Organizations can adopt as many or as few of these as suit them, and NIST folds in public comments on the Playbook about twice a year.[^s5]

## Structure

The framework has two parts. Part 1 frames AI risk and describes what makes an AI system trustworthy. Part 2, the **Core**, organizes risk management into four functions.[^s2]

- **Govern** builds a risk-management culture. It sets policies, accountability structures and processes, including how third-party risk and stakeholder engagement are handled. It is cross-cutting: it informs and runs through the other three functions.[^s3]
- **Map** establishes context: intended uses, affected stakeholders and potential impacts. This supports an early go/no-go decision and grounds the later steps.[^s3]
- **Measure** uses quantitative, qualitative or mixed methods to assess, benchmark and monitor risks and trustworthiness, both before deployment and in operation.[^s3]
- **Manage** allocates resources to the risks that were mapped and measured. It prioritizes them and plans responses, recovery and communication.[^s3]

Each function breaks down into categories and subcategories (six, five, four and four categories respectively). NIST stresses that the suggested actions are not a checklist or a fixed sequence. A typical user sets up Govern, starts with Map, and then iterates between Measure and Manage.[^s3]

## Trustworthiness characteristics

The framework names seven characteristics of trustworthy AI: valid and reliable; safe; secure and resilient; accountable and transparent; explainable and interpretable; privacy-enhanced; and fair, with harmful bias managed.[^s4] Validity and reliability are treated as the necessary base for the others. Accountability and transparency are drawn as cutting across all of them.[^s4] The characteristics can pull against each other. Interpretability can trade off against privacy or predictive accuracy, and privacy-enhancing techniques can reduce accuracy in ways that affect fairness. NIST says analysis can expose these tensions but cannot settle them. The resolution depends on values in the specific context and should be documented and justifiable.[^s4]

## Limitations and open questions

Because the AI RMF is voluntary, it creates no legal obligations by itself. Public and private organizations are not required to use it.[^s5] Its outcome-oriented, non-prescriptive design makes it adaptable, but it leaves organizations to decide what counts as acceptable risk and how to resolve trade-offs.[^s3][^s4] The text is also being revised. America's AI Action Plan (23 July 2025) directed NIST to revise AI RMF 1.0, including removing references to misinformation, diversity, equity and inclusion, and climate change. As of October 2026, NIST's resource centre says a revised version is in progress but gives no timeline.[^s2][^s5]

## In practice

Organizations use the AI RMF mainly through **profiles**, which tailor the Core to a sector, technology or use case. NIST invites outside parties to contribute profiles.[^s5] The most prominent is NIST's own *Generative Artificial Intelligence Profile* (NIST AI 600-1), released on 26 July 2024 under Executive Order 14110. It is a cross-sectoral companion that applies the framework to generative AI and, like the parent framework, is voluntary.[^s6] NIST positions the AI RMF as complementary to its cybersecurity and privacy frameworks.[^s5]

## Connections

The AI RMF is a cornerstone of **AI governance** and **AI risk management**, the broader practices it operationalizes.[^s1] Its Measure function is where **evaluation of AI systems** and adversarial testing such as **red teaming** feed into risk decisions.[^s3] It was **created by NIST** and **has as a part** the **generative AI profile** (NIST AI 600-1).[^s1][^s6] It sits alongside other governance instruments that practitioners often map against it: the management-system standard **ISO/IEC 42001**, the binding **EU AI Act**, and US **executive orders on AI**, one of which (EO 14110) produced the generative AI profile.[^s6]

## Sources
[^s1]: NIST (Tabassi), "Artificial Intelligence Risk Management Framework (AI RMF 1.0)", NIST AI 100-1, 26 January 2023. https://www.nist.gov/node/1731741 (accessed 2026-10-31)
[^s2]: NIST AIRC, "AI RMF 1.0 — Executive Summary". https://airc.nist.gov/airmf-resources/airmf/0-ai-rmf-1-0 (accessed 2026-10-31)
[^s3]: NIST AIRC, "AI RMF Core". https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ (accessed 2026-10-31)
[^s4]: NIST AIRC, "AI Risks and Trustworthiness". https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ (accessed 2026-10-31)
[^s5]: NIST, "AI Risk Management Framework FAQs", updated 13 August 2026. https://www.nist.gov/artificial-intelligence/ai-risk-management-framework-faqs (accessed 2026-10-31)
[^s6]: NIST, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile", NIST AI 600-1, 26 July 2024. https://www.nist.gov/node/1855536 (accessed 2026-10-31)
