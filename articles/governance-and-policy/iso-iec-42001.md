---
id: kt:iso-iec-42001
type: Policy
title: ISO/IEC 42001
aliases: [ISO/IEC 42001:2023, ISO 42001, AI management system standard, AIMS standard]
domain: governance-and-policy
summary: >-
  The international standard, published by ISO and IEC in December 2023, that specifies requirements and guidance
  for establishing, implementing, maintaining and continually improving an artificial intelligence management
  system (AIMS) in any organization that develops, provides or uses AI systems.
maturity: emerging
broader: [kt:ai-governance, kt:ai-risk-management]
related: [kt:nist-ai-risk-management-framework, kt:eu-ai-act, kt:iso-iec-42006, kt:iso-iec-27001, kt:algorithmic-bias-and-fairness]
relations:
  - {predicate: createdBy, object: kt:iso-iec-jtc-1-sc-42}
  - {predicate: influencedBy, object: kt:iso-iec-27001}
sources:
  - id: s1
    title: "ISO/IEC 42001:2023 — Information technology — Artificial intelligence — Management system"
    publisher: IEC Webstore (ISO/IEC JTC 1/SC 42), edition 1.0, 2023-12-18
    url: https://webstore.iec.ch/publication/90574
    type: standards-body
    accessed: 2026-11-14
  - id: s2
    title: "ISO/IEC 42001:2023 — table of contents"
    publisher: DIN (German Institute for Standardization)
    url: https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:376160445/toc-3516210/download
    type: standards-body
    accessed: 2026-11-14
  - id: s3
    title: "AI management systems: What businesses need to know"
    publisher: ISO, 31 January 2024
    url: https://committee.iso.org/artificial-intelligence/ai-management-systems
    type: standards-body
    accessed: 2026-11-14
  - id: s4
    title: "ISO/IEC 42006 — Requirements for bodies providing audit and certification of artificial intelligence management systems"
    publisher: ISO, July 2025
    url: https://www.iso.org/standard/42006
    type: standards-body
    accessed: 2026-11-14
  - id: s5
    title: "NIST AI RMF to ISO/IEC FDIS 42001 AI Management System Crosswalk"
    publisher: NIST Trustworthy and Responsible AI Resource Center (AIRC)
    url: https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf
    type: government
    accessed: 2026-11-14
  - id: s6
    title: "Standardisation of the AI Act"
    publisher: European Commission, Shaping Europe's digital future (updated 19 October 2026)
    url: https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation
    type: government
    accessed: 2026-11-14
created: 2026-11-14
---

# ISO/IEC 42001

**ISO/IEC 42001** is the international standard for an *artificial intelligence management system* (AIMS): the set of policies, roles, processes and controls an organization uses to govern how it builds, supplies or uses AI. It was developed by the joint ISO/IEC committee on AI, JTC 1/SC 42, and published as edition 1.0 on 18 December 2023 (51 pages).[^s1] Its scope is deliberately broad: it applies to any organization, whatever its size, type or sector, that provides or uses products or services built on AI systems, and its stated aim is to help them develop, provide or use AI responsibly while meeting obligations to interested parties.[^s1] ISO has promoted it as the world's first AI management system standard.[^s3]

## Origin and purpose

ISO frames 42001 as the AI counterpart of its widely certified management system standards, predicting it will become as integral to organizations as ISO 9001 (quality), ISO 14001 (environment) and ISO/IEC 27001 (information security).[^s3] Rather than prescribing technical properties of models, it asks organizations to manage AI-specific concerns such as ethics, accountability, transparency and data privacy through a repeatable governance cycle that runs from risk assessment to risk treatment.[^s3] The intended benefits ISO lists include more traceable, transparent and reliable AI applications, more efficient risk assessment and easier regulatory compliance, though it offers no quantified evidence for them.[^s3]

## How it works

The standard follows the common layout of ISO management system standards. Clauses 1–3 cover scope, references and terms; clauses 4–10 hold the auditable requirements, organised as context of the organization, leadership, planning, support, operation, performance evaluation and improvement.[^s2] These map onto a Plan-Do-Check-Act loop: the organization sets an AI policy and objectives, assesses and treats AI risks, runs and monitors its AI processes, and corrects and improves them at planned intervals, so that the system can adapt as the technology changes.[^s3]

Four annexes add AI-specific content.[^s2]

- **Annex A** (normative) lists reference control objectives and controls that an organization selects from when treating its AI risks.[^s2]
- **Annex B** (normative) gives implementation guidance for each of those controls.[^s2]
- **Annex C** (informative) catalogues potential AI-related organizational objectives and sources of risk.[^s2]
- **Annex D** (informative) discusses using the management system across different domains and sectors.[^s2]

NIST's crosswalk gives a sense of what the clauses and annex guidance cover in practice. It maps the AI RMF's analysis of a system's intended purposes and impacts to planning clause 6.1.4, risk-management processes to clauses 6.1 and 8.2–8.4, and roles and training to clauses 5 and 7; it maps system inventories, documentation, data, testing, third-party risk and post-deployment incident handling mainly to the annex guidance.[^s5]

## Certification

Because clauses 4–10 and Annex A are written as requirements, organizations can be audited and certified against 42001, much as they are against ISO/IEC 27001.[^s2][^s3] To make those audits consistent, SC 42 published **ISO/IEC 42006** in July 2025, which extends the general certification-body standard ISO/IEC 17021-1 with AI-specific requirements for the competence and conduct of bodies that audit and certify AI management systems.[^s4]

## Limitations and open questions

A 42001 certificate attests that an organization runs a management system meeting the standard's requirements; the standard itself specifies requirements for that system, not performance, robustness or safety thresholds for any particular model.[^s1][^s2] Its regulatory weight also varies by jurisdiction. Under the EU AI Act, only harmonised standards developed by CEN and CENELEC's JTC 21 and referenced in the EU's Official Journal give a legal presumption of conformity; the European Commission's AI Act quality management standard is a separate document, prEN 18286, which entered public enquiry on 30 October 2025.[^s6] The Commission says it prefers adopting international standards where they align with EU requirements, which leaves room for, but does not guarantee, a role for SC 42 work such as 42001.[^s6] Finally, ISO's own promotional material lists benefits without published evidence, so the effect of certification on real-world AI harms remains an open empirical question.[^s3]

## Connections

42001 is a voluntary instrument of `kt:ai-governance` and a concrete method for `kt:ai-risk-management`, which is why both are its `broader` nodes. Its closest relative is the `kt:nist-ai-risk-management-framework`: both are voluntary and risk-based, and NIST's AI Resource Center hosts a crosswalk mapping each AI RMF Govern, Map, Measure and Manage subcategory to 42001 clauses and annex guidance; the crosswalk was drafted against the final-draft (FDIS) text.[^s5] It relates to the `kt:eu-ai-act` through the Act's standardisation process, where harmonised standards, not 42001 itself, carry presumption of conformity.[^s6] It was created by `kt:iso-iec-jtc-1-sc-42`, borrows the management-system pattern of ISO/IEC 27001 (`kt:iso-iec-27001`), and is paired with ISO/IEC 42006 (`kt:iso-iec-42006`) for certification.[^s3][^s4] Its concerns with accountability and transparency overlap with work on `kt:algorithmic-bias-and-fairness`.[^s3]

## Sources
[^s1]: IEC Webstore, "ISO/IEC 42001:2023 Information technology — Artificial intelligence — Management system", ed. 1.0, 2023-12-18. https://webstore.iec.ch/publication/90574 (accessed 2026-11-14)
[^s2]: DIN, "ISO/IEC 42001:2023 — table of contents". https://www.din.de/de/mitwirken/normenausschuesse/nia/veroeffentlichungen/wdc-beuth:din21:376160445/toc-3516210/download (accessed 2026-11-14)
[^s3]: ISO, "AI management systems: What businesses need to know", 31 January 2024. https://committee.iso.org/artificial-intelligence/ai-management-systems (accessed 2026-11-14)
[^s4]: ISO, "ISO/IEC 42006 — Requirements for bodies providing audit and certification of artificial intelligence management systems", 2025. https://www.iso.org/standard/42006 (accessed 2026-11-14)
[^s5]: NIST AIRC, "NIST AI RMF to ISO/IEC FDIS 42001 AI Management System Crosswalk". https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf (accessed 2026-11-14)
[^s6]: European Commission, "Standardisation of the AI Act", updated 19 October 2026. https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation (accessed 2026-11-14)
