---
id: kt:executive-orders-on-ai
type: Policy
title: Executive orders on AI
aliases: [US executive orders on artificial intelligence, AI executive orders, presidential AI executive orders]
domain: governance-and-policy
summary: >-
  Directives signed by the US President that set federal policy on artificial intelligence by instructing
  executive agencies, from the 2019 American AI Initiative (EO 13859) through EO 14110 on safe and trustworthy
  AI (2023), its 2025 replacement EO 14179, and later orders on LLM procurement, state-law preemption and
  frontier-model security.
maturity: emerging
broader: [kt:ai-governance]
related: [kt:omb-ai-memoranda, kt:nist-ai-risk-management-framework, kt:compute-governance, kt:red-teaming, kt:ai-safety-institutes, kt:large-language-model]
relations:
  - {predicate: enables, object: kt:omb-ai-memoranda}
  - {predicate: contrastsWith, object: kt:eu-ai-act}
  - {predicate: influencedBy, object: kt:nist-ai-risk-management-framework}
sources:
  - id: s1
    title: "Executive Order 13859—Maintaining American Leadership in Artificial Intelligence"
    publisher: The American Presidency Project, UC Santa Barbara (order signed 11 February 2019)
    url: https://www.presidency.ucsb.edu/documents/executive-order-13859-maintaining-american-leadership-artificial-intelligence
    type: primary
    accessed: 2026-11-12
  - id: s2
    title: "Executive Order 14110: Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence"
    publisher: Federal Register Vol. 88 No. 210, 1 November 2023 (GovInfo)
    url: https://www.govinfo.gov/content/pkg/FR-2023-11-01/html/2023-24283.htm
    type: government
    accessed: 2026-11-12
  - id: s3
    title: "Executive Order 14179: Removing Barriers to American Leadership in Artificial Intelligence"
    publisher: Federal Register Vol. 90 No. 20, 31 January 2025 (GovInfo)
    url: https://www.govinfo.gov/content/pkg/FR-2025-01-31/html/2025-02172.htm
    type: government
    accessed: 2026-11-12
  - id: s4
    title: "Executive Order 14319: Preventing Woke AI in the Federal Government"
    publisher: Federal Register Vol. 90 No. 142, 28 July 2025 (GovInfo)
    url: https://www.govinfo.gov/content/pkg/FR-2025-07-28/html/2025-14217.htm
    type: government
    accessed: 2026-11-12
  - id: s5
    title: "Ensuring a National Policy Framework for Artificial Intelligence (EO 14365)"
    publisher: The White House, 11 December 2025
    url: https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence/
    type: government
    accessed: 2026-11-12
  - id: s6
    title: "Promoting Advanced Artificial Intelligence Innovation and Security (EO 14409)"
    publisher: The White House, 2 June 2026
    url: https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/
    type: government
    accessed: 2026-11-12
created: 2026-11-12
---

# Executive orders on AI

**Executive orders on AI** are directives signed by the President of the United States that set national policy on artificial intelligence by telling federal agencies what to do. They are the main instrument of US federal AI policy in the absence of a comprehensive AI statute: they assign tasks and deadlines to bodies such as the Office of Management and Budget (OMB), the Department of Commerce and NIST, but they bind only the executive branch, cannot override statutes, and can be revoked by the next President. The orders typically end with a standard clause saying they create no enforceable rights.[^s3][^s5]

## From the American AI Initiative to EO 14110

An early AI-focused order, **EO 13859** (11 February 2019), launched the American AI Initiative, coordinated by a National Science and Technology Council select committee. It set five guiding principles (research breakthroughs, technical standards, workforce training, public trust with civil-liberties protection, and protecting US technological advantages) and directed agencies to prioritize AI research funding from fiscal year 2020. It also gave OMB 180 days to issue guidance on regulating AI applications and NIST 180 days to plan federal engagement in AI technical standards.[^s1]

**EO 14110** (30 October 2023), on "safe, secure, and trustworthy" AI, was far broader, with eight guiding principles and tasks spread across dozens of agencies.[^s2] Its best-known provision used the Defense Production Act to make developers of potential dual-use foundation models report training plans, model-weight security and red-team results to Commerce. Until Commerce set its own criteria, reporting applied to models trained with more than 10^26 operations (10^23 if trained mainly on biological sequence data) and to computing clusters with a theoretical peak above 10^20 operations per second.[^s2] It also gave NIST 270 days to write red-teaming guidelines and a generative-AI companion to its AI Risk Management Framework, proposed know-your-customer rules for cloud providers serving foreign customers, and called for standards on watermarking and detecting synthetic content.[^s2]

## The 2025 reversal

EO 14110 was revoked when the administration changed in January 2025. **EO 14179** (23 January 2025) declared a policy to "sustain and enhance America's global AI dominance," ordered an immediate review of everything agencies had done under the revoked order so that conflicting actions could be suspended or rescinded, required an AI action plan within 180 days, and gave OMB 60 days to revise its 2024 memoranda on federal use and purchase of AI.[^s3]

Later orders filled in the new approach. **EO 14319** (23 July 2025) allows agencies to buy only large language models that follow two "Unbiased AI Principles", truth-seeking and ideological neutrality, gave OMB 120 days to issue guidance, and exempts national security systems as appropriate.[^s4] **EO 14365** (11 December 2025) targets state AI laws: it created a Justice Department AI Litigation Task Force to challenge state laws on grounds such as interstate commerce and preemption, asked Commerce to list "onerous" state laws within 90 days, tied some broadband grant funds to state AI policy, and called for draft federal legislation that would preempt state law while sparing areas such as child safety and state procurement.[^s5]

**EO 14409** (2 June 2026) turned to frontier-model security. It has the NSA designate "covered frontier models" through a classified benchmarking process for advanced cyber capabilities, and it creates a voluntary framework in which developers may give the government access to such models for up to 30 days before other trusted partners. The order states that it does not create a mandatory licensing or pre-clearance requirement.[^s6]

## Limits and critiques

Because orders bind only agencies, much of their effect depends on follow-on rules, guidance and procurement terms, and they can be undone quickly: EO 14179 began unwinding EO 14110 within days of taking office.[^s3] Several orders exclude national security systems or leave key definitions, such as which models count as frontier, to later agency processes, which limits transparency.[^s4][^s6] Measures aimed at states rely on litigation, grant conditions and requests to Congress rather than direct preemption, since an executive order cannot itself displace state law.[^s5] The orders also swing between approaches: EO 14110 imposed mandatory reporting keyed to fixed compute thresholds, while EO 14409 relies on voluntary access and a classified capability test, leaving open which yardstick for frontier risk will last.[^s2][^s6]

## Connections

The orders are the top layer of US **AI governance** and **enable** the **OMB AI memoranda**, which EO 14179 directed OMB to rewrite and EO 14319 to supplement for LLM procurement.[^s3][^s4] EO 14110 drew on and extended the **NIST AI Risk Management Framework**, required **red teaming** results, and set the training-compute thresholds that made it a landmark of **compute governance**.[^s2] Its tasks on capability evaluation and auditing parallel the work of **AI safety institutes**, and EO 14409 continues the theme of government pre-release access to frontier models.[^s2][^s6] EO 14319 applies specifically to **large language models**.[^s4] The orders **contrast with** the **EU AI Act**, a statute that regulates the private market directly, whereas US orders steer federal agencies and leave private obligations to existing law.[^s3][^s5]

## Sources
[^s1]: Executive Order 13859, "Maintaining American Leadership in Artificial Intelligence", 11 February 2019, via The American Presidency Project. https://www.presidency.ucsb.edu/documents/executive-order-13859-maintaining-american-leadership-artificial-intelligence (accessed 2026-11-12)
[^s2]: Executive Order 14110, "Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence", 30 October 2023, 88 FR 75191. https://www.govinfo.gov/content/pkg/FR-2023-11-01/html/2023-24283.htm (accessed 2026-11-12)
[^s3]: Executive Order 14179, "Removing Barriers to American Leadership in Artificial Intelligence", 23 January 2025, 90 FR 8741. https://www.govinfo.gov/content/pkg/FR-2025-01-31/html/2025-02172.htm (accessed 2026-11-12)
[^s4]: Executive Order 14319, "Preventing Woke AI in the Federal Government", 23 July 2025, 90 FR 35389. https://www.govinfo.gov/content/pkg/FR-2025-07-28/html/2025-14217.htm (accessed 2026-11-12)
[^s5]: The White House, "Ensuring a National Policy Framework for Artificial Intelligence" (EO 14365), 11 December 2025. https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence/ (accessed 2026-11-12)
[^s6]: The White House, "Promoting Advanced Artificial Intelligence Innovation and Security" (EO 14409), 2 June 2026. https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/ (accessed 2026-11-12)
