---
id: kt:omb-ai-memoranda
type: Policy
title: OMB AI memoranda
aliases: [OMB AI guidance, OMB M-24-10, OMB M-25-21, OMB M-25-22, OMB M-26-04]
domain: governance-and-policy
summary: >-
  The series of memoranda from the US Office of Management and Budget that set binding, government-wide rules
  for how federal executive agencies govern, use and buy AI, from M-24-10 and M-24-18 (2024) to their 2025
  replacements M-25-21 and M-25-22 and the December 2025 LLM procurement memo M-26-04.
maturity: emerging
broader: [kt:ai-governance]
related: [kt:nist-ai-risk-management-framework, kt:executive-orders-on-ai, kt:algorithmic-bias-and-fairness, kt:red-teaming, kt:large-language-model, kt:model-cards]
relations:
  - {predicate: createdBy, object: kt:office-of-management-and-budget}
  - {predicate: basedOn, object: kt:executive-orders-on-ai}
  - {predicate: contrastsWith, object: kt:eu-ai-act}
sources:
  - id: s1
    title: "M-24-10: Advancing Governance, Innovation, and Risk Management for Agency Use of Artificial Intelligence"
    publisher: Office of Management and Budget (Young), 28 March 2024
    url: https://www.whitehouse.gov/wp-content/uploads/2024/03/M-24-10-Advancing-Governance-Innovation-and-Risk-Management-for-Agency-Use-of-Artificial-Intelligence.pdf
    type: government
    accessed: 2026-11-09
  - id: s2
    title: "M-24-18: Advancing the Responsible Acquisition of Artificial Intelligence in Government"
    publisher: Office of Management and Budget (Young), 24 September 2024
    url: https://www.whitehouse.gov/wp-content/uploads/2024/10/M-24-18-AI-Acquisition-Memorandum.pdf
    type: government
    accessed: 2026-11-09
  - id: s3
    title: "M-25-21: Accelerating Federal Use of AI through Innovation, Governance, and Public Trust"
    publisher: Office of Management and Budget (Vought), 3 April 2025
    url: https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf
    type: government
    accessed: 2026-11-09
  - id: s4
    title: "M-25-22: Driving Efficient Acquisition of Artificial Intelligence in Government (copy of the OMB memo)"
    publisher: Office of Management and Budget (Vought), 3 April 2025; hosted by Digital Government Hub
    url: https://digitalgovernmenthub.org/wp-content/uploads/2025/04/M-25-22-Driving-Efficient-Acquisition-of-Artificial-Intelligence-in-Government.pdf
    type: government
    accessed: 2026-11-09
  - id: s5
    title: "Fact Sheet: Eliminating Barriers for Federal Artificial Intelligence Use and Procurement"
    publisher: The White House, 7 April 2025
    url: https://www.whitehouse.gov/fact-sheets/2025/04/fact-sheet-eliminating-barriers-for-federal-artificial-intelligence-use-and-procurement/
    type: government
    accessed: 2026-11-09
  - id: s6
    title: "M-26-04: Increasing Public Trust in Artificial Intelligence Through Unbiased AI Principles"
    publisher: Office of Management and Budget (Vought), 11 December 2025
    url: https://www.whitehouse.gov/wp-content/uploads/2025/12/M-26-04-Increasing-Public-Trust-in-Artificial-Intelligence-Through-Unbiased-AI-Principles-1.pdf
    type: government
    accessed: 2026-11-09
created: 2026-11-09
---

# OMB AI memoranda

The **OMB AI memoranda** are policy directives issued by the US Office of Management and Budget (OMB) that tell federal executive agencies how to organize for, govern, use and acquire artificial intelligence. Unlike voluntary frameworks, they bind agencies directly: they set deadlines, assign named officials, and can require an agency to stop using a non-compliant system. The series has been rewritten once already with a change of administration, so the most recent memos are M-25-21 for use and M-25-22 for acquisition (both April 2025) and M-26-04 for large language model procurement (December 2025).[^s1][^s3][^s4][^s6]

## The 2024 memos: M-24-10 and M-24-18

M-24-10, signed by OMB Director Shalanda Young on 28 March 2024, drew on the AI in Government Act of 2020, the Advancing American AI Act and Executive Order 14110. It required every agency to designate a Chief AI Officer (CAIO) within 60 days, had the larger CFO Act agencies stand up an AI Governance Board chaired at Deputy Secretary level, and required public compliance plans and annual AI use-case inventories.[^s1] Its core was a pair of risk categories, **safety-impacting** and **rights-impacting** AI, with an appendix of uses presumed to fall into them (for example certain law-enforcement, immigration and housing decisions). By 1 December 2024 agencies had to apply minimum practices to such systems, including impact assessments, real-world testing, independent evaluation, ongoing monitoring, operator training, human oversight and public notice, or stop using them; CAIOs could grant documented, system-specific waivers.[^s1]

M-24-18 (24 September 2024) extended this to procurement. It asked agencies to avoid vendor lock-in through data and model portability and knowledge transfer, to define who owns data and IP when agency data trains or fine-tunes a model, and to bar vendors from training commercial models on agency data without consent. It added specific expectations for enterprise generative AI (such as labelling synthetic media and documenting red-teaming) and for AI-enabled biometrics.[^s2]

## The 2025 rewrite: M-25-21 and M-25-22

On 3 April 2025 OMB Director Russell Vought issued M-25-21, implementing Executive Order 14179, and it explicitly rescinded M-24-10.[^s3] The structure survived: agencies still need a CAIO within 60 days, CFO Act agencies still need a governance board (within 90 days), and compliance plans and inventories continue. The two risk categories were merged into a single **high-impact AI** category, meaning AI whose output is a principal basis for decisions with legal, material, binding or significant effects on rights or safety. Agencies got 365 days to document minimum practices for high-impact uses, including pre-deployment testing, impact assessments, monitoring, human oversight and remedies, and must discontinue non-compliant systems. New elements included agency AI strategies, a preference for American-made AI, and a push to share custom AI code and model weights across government and, where practicable, as open source.[^s3]

M-25-22, issued the same day, rescinded and replaced M-24-18. It kept the anti-lock-in and data-rights themes, including a permanent bar on training commercial or public models on non-public agency data without consent, and applies to contracts under solicitations issued 180 days or more after issuance. It also tasked GSA with an acquisition guide and an agencies-only repository of AI procurement practices.[^s4] The White House framed both memos as replacing a "risk-averse" approach with one aimed at faster, more competitive adoption, while keeping privacy and civil-liberties protections.[^s5]

## M-26-04 and LLM procurement

M-26-04 (11 December 2025) implements Executive Order 14319. It requires any LLM an agency procures to follow two "Unbiased AI Principles", truth-seeking and ideological neutrality, and requires vendors to supply at least an acceptable use policy, model, system or data cards, end-user resources and a channel for reporting violating outputs. Agencies had until 11 March 2026 to update procurement policies; the memo sunsets after two years unless extended.[^s6]

## Scope, limits and critiques

Every memo in the series excludes AI used as a component of a National Security System, and the Intelligence Community is excluded or only encouraged to comply, so a large share of high-stakes government AI falls outside them.[^s1][^s3][^s4][^s6] Waivers granted by CAIOs give agencies discretion that outsiders see only in public summaries.[^s3] Because each memo rests on an executive order, the rules can change quickly with a new administration, as the 2025 rescissions showed.[^s3][^s4]

## Connections

The memoranda are an instance of national **AI governance** and are **based on** successive **executive orders on AI** (EO 14110, then EO 14179 and EO 14319).[^s1][^s3][^s6] They are **created by** OMB and lean on practices also found in the **NIST AI Risk Management Framework**, such as impact assessment, testing and monitoring.[^s1] Their handling of bias links to **algorithmic bias and fairness**, while M-24-18's red-teaming documentation and M-26-04's LLM rules connect them to **red teaming**, **large language models** and **model cards**.[^s2][^s6] They **contrast with** the **EU AI Act**: the OMB rules govern only the US government's own use and purchasing, not the private market.[^s3]

## Sources
[^s1]: OMB, M-24-10, "Advancing Governance, Innovation, and Risk Management for Agency Use of Artificial Intelligence", 28 March 2024. https://www.whitehouse.gov/wp-content/uploads/2024/03/M-24-10-Advancing-Governance-Innovation-and-Risk-Management-for-Agency-Use-of-Artificial-Intelligence.pdf (accessed 2026-11-09)
[^s2]: OMB, M-24-18, "Advancing the Responsible Acquisition of Artificial Intelligence in Government", 24 September 2024. https://www.whitehouse.gov/wp-content/uploads/2024/10/M-24-18-AI-Acquisition-Memorandum.pdf (accessed 2026-11-09)
[^s3]: OMB, M-25-21, "Accelerating Federal Use of AI through Innovation, Governance, and Public Trust", 3 April 2025. https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf (accessed 2026-11-09)
[^s4]: OMB, M-25-22, "Driving Efficient Acquisition of Artificial Intelligence in Government", 3 April 2025 (copy hosted by Digital Government Hub). https://digitalgovernmenthub.org/wp-content/uploads/2025/04/M-25-22-Driving-Efficient-Acquisition-of-Artificial-Intelligence-in-Government.pdf (accessed 2026-11-09)
[^s5]: The White House, "Fact Sheet: Eliminating Barriers for Federal Artificial Intelligence Use and Procurement", 7 April 2025. https://www.whitehouse.gov/fact-sheets/2025/04/fact-sheet-eliminating-barriers-for-federal-artificial-intelligence-use-and-procurement/ (accessed 2026-11-09)
[^s6]: OMB, M-26-04, "Increasing Public Trust in Artificial Intelligence Through Unbiased AI Principles", 11 December 2025. https://www.whitehouse.gov/wp-content/uploads/2025/12/M-26-04-Increasing-Public-Trust-in-Artificial-Intelligence-Through-Unbiased-AI-Principles-1.pdf (accessed 2026-11-09)
