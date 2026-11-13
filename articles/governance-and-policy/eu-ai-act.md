---
id: kt:eu-ai-act
type: Policy
title: EU AI Act
aliases: [Artificial Intelligence Act, AI Act, Regulation (EU) 2024/1689, European Union Artificial Intelligence Act]
domain: governance-and-policy
summary: >-
  Regulation (EU) 2024/1689, the European Union's horizontal law on artificial intelligence, which sorts AI
  systems into risk tiers (prohibited, high-risk, transparency, minimal), sets separate duties for providers of
  general-purpose AI models, and is enforced by national authorities and the Commission's AI Office.
maturity: emerging
broader: [kt:ai-governance]
related: [kt:nist-ai-risk-management-framework, kt:compute-governance, kt:algorithmic-bias-and-fairness, kt:large-language-model, kt:general-purpose-ai-model, kt:digital-omnibus-on-ai]
relations:
  - {predicate: createdBy, object: kt:european-union}
  - {predicate: contrastsWith, object: kt:executive-orders-on-ai}
  - {predicate: influencedBy, object: kt:new-legislative-framework}
sources:
  - id: s1
    title: "Regulation (EU) 2024/1689 (Artificial Intelligence Act), consolidated text of 27 July 2026"
    publisher: EUR-Lex, Publications Office of the European Union
    url: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng/pdf
    type: government
    accessed: 2026-11-13
  - id: s2
    title: "AI Act — Shaping Europe's digital future (regulatory framework for AI)"
    publisher: European Commission, last updated 19 October 2026
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    type: government
    accessed: 2026-11-13
  - id: s3
    title: "EU agrees to simplify AI rules to boost innovation and ban 'nudification' apps to protect citizens"
    publisher: European Commission press release, 7 May 2026
    url: https://digital-strategy.ec.europa.eu/en/news/eu-agrees-simplify-ai-rules-boost-innovation-and-ban-nudification-apps-protect-citizens
    type: government
    accessed: 2026-11-13
  - id: s4
    title: "Demystifying the Draft EU Artificial Intelligence Act"
    publisher: Computer Law Review International 22(4), 2021 (Veale & Zuiderveen Borgesius; authors' arXiv version)
    url: https://arxiv.org/pdf/2107.03721.pdf
    type: peer-reviewed
    accessed: 2026-11-13
created: 2026-11-13
---

# EU AI Act

The EU AI Act is Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024, which lays down harmonised rules on artificial intelligence across the European Union's single market.[^s1] It entered into force on 1 August 2024 and is widely described as the first comprehensive, horizontal AI law: rather than regulating one sector, it attaches obligations to AI systems according to the risk their intended use poses to health, safety and fundamental rights.[^s2] The Act defines an AI system broadly, as a machine-based system that operates with varying autonomy, may adapt after deployment, and infers from its inputs how to produce outputs such as predictions, content, recommendations or decisions that can influence physical or virtual environments.[^s1]

## How it works: four risk tiers

- **Unacceptable risk (prohibited).** As of late 2026 the Commission lists nine banned practices, including harmful manipulation, social scoring, untargeted scraping of facial images, and emotion recognition in workplaces and schools.[^s2]
- **High risk.** Uses such as CV screening, credit scoring, exam scoring and AI safety components of regulated products must meet requirements on risk management, data quality, logging, documentation, human oversight and robustness.[^s2]
- **Transparency risk.** People must be told when they are dealing with a chatbot, and generated or manipulated content such as deepfakes must be identifiable or labelled.[^s2]
- **Minimal risk.** Most AI systems, such as spam filters or game AI, carry no specific obligations under the Act.[^s2]

Separately from these tiers, the Act regulates **general-purpose AI (GPAI) models**, the category that covers today's large language models. Every GPAI provider must keep technical documentation, inform downstream integrators about capabilities and limits, maintain an EU copyright-compliance policy, and publish a summary of training content using an AI Office template; open-source models with public weights are exempt from the documentation duties unless they pose systemic risk.[^s1] A model is presumed to have high-impact capabilities, and hence systemic risk, when its cumulative training compute exceeds 10^25 floating-point operations, which triggers additional evaluation and risk-mitigation duties.[^s1]

## Enforcement and penalties

Enforcement is split between Member State market-surveillance authorities and the Commission's AI Office, which has direct powers over GPAI models: it can request documentation, evaluate models, order corrective measures and fine providers.[^s2] Maximum fines are EUR 35 million or 7% of worldwide annual turnover (whichever is higher) for prohibited practices, EUR 15 million or 3% for most other operator obligations, and EUR 7.5 million or 1% for supplying misleading information; SMEs face the lower of the two amounts.[^s1] GPAI providers can be fined up to 3% of turnover or EUR 15 million by the Commission.[^s1]

## Timeline and the 2026 AI Omnibus

The Act phases in over several years. Prohibitions and AI-literacy duties applied from 2 February 2025, governance and GPAI rules from 2 August 2025, and the Act became generally applicable on 2 August 2026.[^s2] In November 2025 the Commission proposed a "Digital Omnibus on AI" to simplify implementation; Parliament and Council reached political agreement on 7 May 2026, and the amending regulation entered into force on 27 July 2026.[^s3][^s2] It pushed high-risk obligations for Annex III use cases (such as employment, education, biometrics and border control) to 2 December 2027 and for AI embedded in regulated products to 2 August 2028, so that harmonised standards can be ready first.[^s3][^s1] It also added a ninth prohibition, on AI that generates non-consensual intimate imagery or child sexual abuse material, applying from 2 December 2026, and extended simplified rules to small mid-cap companies.[^s2][^s1]

## Critiques and open questions

Legal scholars Michael Veale and Frederik Zuiderveen Borgesius, analysing the Commission's 2021 draft, credited the risk-tiered approach but argued the Act grafts fundamental-rights protection onto the EU's product-safety "New Legislative Framework", designed for goods like lifts and toys.[^s4] They warned that much real rule-making would move into harmonised technical standards written by private standards bodies with limited democratic oversight, that most high-risk systems could be certified by provider self-assessment, and that maximum harmonisation could stop Member States from regulating AI below the high-risk threshold.[^s4] The repeated deadline extensions tied to standards readiness show that dependence on standardisation remains a practical bottleneck.[^s3]

## Connections

The Act is the EU's central instrument within **AI governance**, and it is the main binding counterpart to voluntary frameworks such as the **NIST AI Risk Management Framework**, and it is often contrasted with US **executive orders on AI**.[^s2] Its 10^25 FLOP presumption links it to **compute governance**, and its GPAI chapter is what applies to **large language model** providers.[^s1] High-risk data-quality and oversight duties address concerns studied under **algorithmic bias and fairness**, and its design draws on the **New Legislative Framework** for product regulation.[^s2][^s4]

## Sources
[^s1]: Regulation (EU) 2024/1689 (Artificial Intelligence Act), consolidated text of 27 July 2026, EUR-Lex. https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng/pdf (accessed 2026-11-13)
[^s2]: European Commission, "AI Act", Shaping Europe's digital future, last updated 19 October 2026. https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai (accessed 2026-11-13)
[^s3]: European Commission, "EU agrees to simplify AI rules to boost innovation and ban 'nudification' apps to protect citizens", 7 May 2026. https://digital-strategy.ec.europa.eu/en/news/eu-agrees-simplify-ai-rules-boost-innovation-and-ban-nudification-apps-protect-citizens (accessed 2026-11-13)
[^s4]: M. Veale and F. Zuiderveen Borgesius, "Demystifying the Draft EU Artificial Intelligence Act", Computer Law Review International 22(4), 2021. https://arxiv.org/pdf/2107.03721.pdf (accessed 2026-11-13)
