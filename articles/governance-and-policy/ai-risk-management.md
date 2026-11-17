---
id: kt:ai-risk-management
type: Concept
title: AI risk management
aliases: [artificial intelligence risk management, AI risk governance process]
domain: governance-and-policy
summary: >-
  The organizational discipline of identifying, analysing, evaluating, treating, monitoring and communicating the
  risks that AI systems pose across their lifecycle, usually built on general risk-management practice (ISO 31000)
  and codified for AI in standards, frameworks and laws such as ISO/IEC 23894, the NIST AI RMF and the EU AI Act.
maturity: emerging
broader: [kt:ai-governance]
related: [kt:ai-safety, kt:ai-evaluation, kt:red-teaming, kt:responsible-scaling-policy, kt:algorithmic-bias-and-fairness]
relations:
  - {predicate: hasPart, object: kt:iso-iec-23894}
  - {predicate: basedOn, object: kt:iso-31000}
  - {predicate: hasPart, object: kt:nist-ai-risk-management-framework}
  - {predicate: hasPart, object: kt:iso-iec-42001}
  - {predicate: regulatedBy, object: kt:eu-ai-act}
  - {predicate: influencedBy, object: kt:oecd-ai-principles}
sources:
  - id: s1
    title: "ISO/IEC 23894:2023 — Information technology — Artificial intelligence — Guidance on risk management"
    publisher: IEC Webstore (ISO/IEC JTC 1/SC 42), edition 1.0, 2023-02-06
    url: https://webstore.iec.ch/en/publication/82914
    type: standards-body
    accessed: 2026-11-17
  - id: s2
    title: "ISO/IEC 23894:2023 — Guidance on Risk Management for AI"
    publisher: American National Standards Institute (ANSI) Standards Blog
    url: https://blog.ansi.org/ansi/iso-iec-23894-2023-ai-risk-management/
    type: standards-body
    accessed: 2026-11-17
  - id: s3
    title: "AI RMF 1.0, Section 1: Framing Risk"
    publisher: NIST Trustworthy and Responsible AI Resource Center (AIRC)
    url: https://airc.nist.gov/airmf-resources/airmf/1-sec-risk/
    type: government
    accessed: 2026-11-17
  - id: s4
    title: "AI Act, Article 9: Risk management system"
    publisher: European Commission, AI Act Service Desk
    url: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9
    type: government
    accessed: 2026-11-17
  - id: s5
    title: "Advancing accountability in AI: Governing and managing risks throughout the lifecycle for trustworthy AI"
    publisher: OECD Digital Economy Papers, 23 February 2023
    url: https://oecd.ai/en/ai-publications/advancing-accountability
    type: intergovernmental
    accessed: 2026-11-17
  - id: s6
    title: "Three lines of defense against risks from AI"
    publisher: AI & Society 40:493–507 (Schuett), published online 2023-11-27
    url: https://link.springer.com/content/pdf/10.1007/s00146-023-01811-0.pdf
    type: peer-reviewed
    accessed: 2026-11-17
created: 2026-11-17
---

# AI risk management

**AI risk management** is the set of organizational processes by which developers, providers and users of AI systems find the ways those systems could cause harm (or fail to deliver benefit), judge how serious those possibilities are, decide what to do about them, and keep watching as the system and its context change. It is less a single framework than a shared practice that several frameworks express: the international guidance standard ISO/IEC 23894, the US NIST AI Risk Management Framework, the management-system standard ISO/IEC 42001, and the legally binding risk-management obligation in the EU AI Act all describe versions of it.[^s1][^s3][^s4]

## Origins

The discipline adapts generic enterprise risk management to AI rather than inventing something new. ISO/IEC 23894, published in February 2023 by the joint ISO/IEC subcommittee on AI (JTC 1/SC 42), offers guidance for any organization that develops, deploys or uses AI and is meant to be read together with ISO 31000:2018, the general risk-management guideline.[^s1][^s2] In the same month the OECD released a report that maps tools for defining, assessing, treating and governing risk onto each stage of the AI system lifecycle, explicitly drawing on ISO 31000, the NIST AI RMF and the OECD AI Principles.[^s5]

## How it works

Most formulations share the classic risk cycle. NIST frames risk as the combination of how likely an event is and how large its consequences would be, and notes that AI impacts can be positive as well as negative, so risk management covers maximizing benefit as well as limiting harm.[^s3] The EU AI Act turns the cycle into a legal duty for providers of high-risk systems: a documented, continuous and iterative process over the whole lifecycle that identifies known and foreseeable risks to health, safety and fundamental rights, estimates risks under intended use and reasonably foreseeable misuse, folds in data from post-market monitoring, and adopts targeted measures.[^s4]

Treatment follows a preference order in the Act: design risks out where technically feasible, then mitigate and control what remains, then inform and train deployers. The residual risk of each hazard, and of the system overall, must be judged acceptable, and testing against predefined metrics and probabilistic thresholds must happen before the system reaches the market.[^s4] NIST adds that eliminating all risk is unrealistic, so effort should be prioritized by assessed risk, with development or deployment halted safely when risks are unacceptable and residual risk documented for end users.[^s3]

AI-specific risk sources are what distinguish this from ordinary IT risk management. ISO/IEC 23894 directs organizations to consider factors such as environmental complexity, limited transparency and explainability, the level of automation, machine-learning-specific issues, hardware, lifecycle issues and technology readiness.[^s2]

## Organizational roles

Processes need owners. Schuett argues that the three lines of defense model, popularized by the Institute of Internal Auditors, can clarify who manages AI risk at a developer: product and research teams own their own risks (first line), risk, legal and compliance functions advise and challenge them (second line), and internal audit independently assures both and reports to the board (third line).[^s6] NIST similarly holds that AI risk should sit inside enterprise risk management alongside cybersecurity and privacy, and that it depends on leadership commitment, clear accountability and supportive incentives.[^s3]

## Limitations and open questions

Measurement is the weak point. NIST lists recurring obstacles: third-party components with undisclosed metrics, emergent risks, no consensus on robust and verifiable measures, metrics that can be gamed, risks that change between lifecycle stages, lab results that fail to predict field behaviour, inscrutable models, and the difficulty of comparing AI to a human baseline.[^s3] Risk tolerance is also left to context: NIST deliberately does not prescribe it, deferring to sector rules and organizational judgement.[^s3] Schuett notes that responsibility for AI risk is often unclear inside companies, which motivates structural fixes such as the three lines model.[^s6]

## In practice

As of 2026 an organization typically combines several of these instruments: ISO/IEC 23894 or the NIST AI RMF for the method, ISO/IEC 42001 for a certifiable management system, and Article 9 of the EU AI Act where it places high-risk systems on the EU market. The Act allows providers already subject to risk-management duties under other EU law to integrate the AI requirements into those existing procedures.[^s4] The OECD report's purpose is precisely to show how these frameworks can be combined along the AI lifecycle.[^s5]

## Connections

AI risk management is a core activity within **AI governance** (`broader`), which also covers policy, accountability and oversight beyond risk. It is **based on** ISO 31000, and its main codifications are **parts** of the practice: ISO/IEC 23894 (guidance), the NIST AI RMF (a voluntary framework) and ISO/IEC 42001 (a management system).[^s1][^s3] For high-risk systems in the EU it is **regulated by** the EU AI Act's Article 9.[^s4] The OECD AI Principles **influenced** the lifecycle framing used by the OECD's accountability work.[^s5] Its measurement step depends on **AI evaluation** and **red teaming**; the harms it manages range from **algorithmic bias** to the concerns of **AI safety**, and frontier developers' **responsible scaling policies** apply a capability-threshold version of the same idea.[^s3][^s4]

## Sources
[^s1]: ISO/IEC JTC 1/SC 42, "ISO/IEC 23894:2023 — Guidance on risk management", IEC Webstore. https://webstore.iec.ch/en/publication/82914 (accessed 2026-11-17)
[^s2]: ANSI, "ISO/IEC 23894:2023 — Guidance on Risk Management for AI". https://blog.ansi.org/ansi/iso-iec-23894-2023-ai-risk-management/ (accessed 2026-11-17)
[^s3]: NIST, "AI RMF 1.0, Section 1: Framing Risk". https://airc.nist.gov/airmf-resources/airmf/1-sec-risk/ (accessed 2026-11-17)
[^s4]: European Commission AI Act Service Desk, "Article 9: Risk management system". https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9 (accessed 2026-11-17)
[^s5]: OECD, "Advancing accountability in AI", OECD Digital Economy Papers, 2023. https://oecd.ai/en/ai-publications/advancing-accountability (accessed 2026-11-17)
[^s6]: J. Schuett, "Three lines of defense against risks from AI", AI & Society 40 (2025): 493–507. https://link.springer.com/content/pdf/10.1007/s00146-023-01811-0.pdf (accessed 2026-11-17)
