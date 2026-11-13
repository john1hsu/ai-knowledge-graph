---
id: kt:ai-safety
type: Field
title: AI safety
aliases: [ML safety, machine learning safety, safety of AI systems]
domain: safety-alignment-and-security
summary: >-
  The interdisciplinary field concerned with preventing AI systems from causing harm, whether through accidents and
  malfunctions, deliberate misuse or systemic effects of deployment, spanning robustness, monitoring, alignment and
  risk management.
maturity: emerging
broader: [kt:artificial-intelligence]
related: [kt:ai-governance, kt:ai-evaluation, kt:red-teaming, kt:adversarial-machine-learning, kt:ai-safety-institutes]
relations:
  - {predicate: hasPart, object: kt:ai-alignment}
  - {predicate: hasPart, object: kt:mechanistic-interpretability}
  - {predicate: influencedBy, object: kt:concrete-problems-in-ai-safety}
sources:
  - id: s1
    title: "Concrete Problems in AI Safety"
    publisher: Google Research (Amodei, Olah, Steinhardt, Christiano, Schulman, Mané), arXiv:1606.06565, 2016
    url: https://research.google/pubs/concrete-problems-in-ai-safety/
    type: primary
    accessed: 2026-11-13
  - id: s2
    title: "Unsolved Problems in ML Safety"
    publisher: arXiv:2109.13916v4 (Hendrycks, Carlini, Schulman, Steinhardt), first submitted September 2021
    url: https://arxiv.org/pdf/2109.13916v4
    type: primary
    accessed: 2026-11-13
  - id: s3
    title: "AI Risk Management Framework 1.0, Section 3: AI Risks and Trustworthiness"
    publisher: National Institute of Standards and Technology (NIST), Trustworthy and Responsible AI Resource Center
    url: https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/
    type: government
    accessed: 2026-11-13
  - id: s4
    title: "The Bletchley Declaration by Countries Attending the AI Safety Summit, 1-2 November 2023"
    publisher: UK Government (GOV.UK), published 1 November 2023
    url: https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration/the-bletchley-declaration-by-countries-attending-the-ai-safety-summit-1-2-november-2023.
    type: government
    accessed: 2026-11-13
  - id: s5
    title: "International AI Safety Report"
    publisher: arXiv:2501.17805 (Bengio et al., 100 contributing experts), January 2025
    url: https://arxiv.org/abs/2501.17805
    type: primary
    accessed: 2026-11-13
  - id: s6
    title: "International AI Safety Report (full text)"
    publisher: arXiv:2501.17805 PDF (Bengio et al.), January 2025
    url: https://arxiv.org/pdf/2501.17805
    type: primary
    accessed: 2026-11-13
created: 2026-11-13
---

# AI safety

**AI safety** is the field that studies how to keep AI systems from causing harm, and how to build, test, deploy and govern them so that they don't. It is broader than **AI alignment**: alignment asks whether a system pursues what its designers intend, while safety also covers systems that fail under unusual inputs, systems that are deliberately misused, and harms that emerge only once a technology is widely deployed. In engineering terms, NIST's AI Risk Management Framework lists "safe" as one of seven characteristics of trustworthy AI and, citing ISO/IEC TS 5723:2022, defines it as not leading, under defined conditions, to a state that endangers human life, health, property or the environment.[^s3]

## Origins: accidents in machine learning

Modern technical AI safety research is often dated to *Concrete Problems in AI Safety* (2016), by Amodei, Olah, Steinhardt, Christiano, Schulman and Mané. The paper framed the subject as preventing *accidents*: harmful behaviour that emerges from poor design of real-world ML systems and that no one intended.[^s1] It grouped five research problems by where accidents originate: a wrong objective (avoiding negative side effects, avoiding reward hacking), an objective too costly to check often (scalable supervision), and bad behaviour during learning (safe exploration, robustness to distributional shift).[^s1]

## A research map: robustness, monitoring, alignment, systemic safety

In 2021 Hendrycks, Carlini, Schulman and Steinhardt proposed an updated roadmap in *Unsolved Problems in ML Safety*, motivated by models that were growing in size, gaining new capabilities and moving into high-stakes settings.[^s2] They split the field into four problems framed around hazards:[^s2]

- **Robustness**: withstanding hazards, covering both adversarial robustness and robustness to black-swan, long-tail events.[^s2]
- **Monitoring**: identifying hazards, including anomaly detection, calibrated and honest outputs, and hidden functionality such as trojans or emergent hazardous capabilities.[^s2]
- **Alignment**: reducing hazards inherent to the model, such as objectives that are hard to specify or optimize and brittle proxies that get gamed.[^s2]
- **Systemic safety**: reducing hazards in the wider sociotechnical system, for example applying ML to cyber defence and to better forecasting and decision-making.[^s2]

This taxonomy treats alignment as one pillar among several and makes detection of hazards a research problem of its own.[^s2]

## Risk categories used in policy

Policy bodies tend to sort harms by cause rather than by research problem. The *International AI Safety Report*, published in January 2025 with Yoshua Bengio as chair and 100 contributing experts, was commissioned by the nations attending the 2023 Bletchley summit, which each nominated advisory-panel members alongside the UN, OECD and EU.[^s5] It groups general-purpose AI risks into three families: **malicious use** (for example fraud via voice impersonation, manipulation of public opinion, cyberattacks, and help with biological or chemical attacks); **malfunctions** (unreliable outputs, bias, and hypothetical *loss of control*); and **systemic risks** (labour-market disruption, market concentration, environmental costs, privacy and copyright harms).[^s6] On loss of control the report records broad agreement that current systems lack the capability to pose it, but real disagreement among experts about how likely it is over the next several years.[^s6]

The report also names an *evidence dilemma*: because capabilities can advance quickly and unpredictably, policymakers must choose between acting on thin evidence, which may prove unnecessary, and waiting, which may leave society unprepared.[^s6]

## Practice

In practice, safety work combines techniques from ML and from established safety engineering. NIST recommends planning for safety from the design stage, rigorous simulation and in-domain testing, real-time monitoring, and the ability to shut down, modify or override a system that deviates from expected behaviour, with risks of serious injury or death prioritised; it also points to safety practice in transportation and healthcare as models.[^s3] For frontier models, governments at the Bletchley summit in November 2023 agreed that developers of the most capable systems bear a particularly strong responsibility for safety, including through safety testing, evaluations and transparency about mitigations, and committed to support an international research network on frontier AI safety.[^s4] The Bletchley Declaration explicitly named both misuse and unintended loss of control as concerns, with cybersecurity, biotechnology and disinformation flagged as areas of particular risk.[^s4]

## Connections

AI safety sits under **artificial intelligence** as a cross-cutting field. **AI alignment** is one of its main parts, matching the alignment pillar in Hendrycks et al.'s roadmap, and **mechanistic interpretability** bears on its monitoring pillar, which includes uncovering hidden model functionality such as trojans.[^s2] Its modern research agenda was shaped by **Concrete Problems in AI Safety**.[^s1] **Adversarial machine learning** supplies much of the robustness pillar, while **red teaming** and **AI evaluation** are the main ways safety properties are tested before deployment, the practice the Bletchley signatories asked frontier developers to adopt.[^s2][^s4] **AI governance** turns safety findings into rules, and **AI safety institutes** are the public bodies created to carry out that testing and research.[^s4][^s5]

## Sources
[^s1]: Amodei, Olah, Steinhardt, Christiano, Schulman, Mané, "Concrete Problems in AI Safety", Google Research / arXiv:1606.06565, 2016. https://research.google/pubs/concrete-problems-in-ai-safety/ (accessed 2026-11-13)
[^s2]: Hendrycks, Carlini, Schulman, Steinhardt, "Unsolved Problems in ML Safety", arXiv:2109.13916v4. https://arxiv.org/pdf/2109.13916v4 (accessed 2026-11-13)
[^s3]: NIST, "AI RMF 1.0, Section 3: AI Risks and Trustworthiness". https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/ (accessed 2026-11-13)
[^s4]: UK Government, "The Bletchley Declaration by Countries Attending the AI Safety Summit, 1-2 November 2023". https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-declaration/the-bletchley-declaration-by-countries-attending-the-ai-safety-summit-1-2-november-2023. (accessed 2026-11-13)
[^s5]: Bengio et al., "International AI Safety Report", arXiv:2501.17805, January 2025. https://arxiv.org/abs/2501.17805 (accessed 2026-11-13)
[^s6]: Bengio et al., "International AI Safety Report" (full text), January 2025. https://arxiv.org/pdf/2501.17805 (accessed 2026-11-13)
