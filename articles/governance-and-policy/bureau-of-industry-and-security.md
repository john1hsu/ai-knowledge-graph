---
id: kt:bureau-of-industry-and-security
type: Organization
title: Bureau of Industry and Security
aliases: [BIS, US Bureau of Industry and Security, Commerce Department Bureau of Industry and Security, Bureau of Export Administration]
domain: governance-and-policy
summary: >-
  The US Department of Commerce agency that administers and enforces controls on exports of dual-use items under
  the Export Administration Regulations, and the body through which the US government restricts foreign access to
  advanced AI chips and has sought information from frontier AI developers.
maturity: established
broader: [kt:ai-governance]
related: [kt:ai-chip-export-controls, kt:compute-governance, kt:executive-orders-on-ai, kt:red-teaming, kt:ai-safety-institutes]
relations:
  - {predicate: partOf, object: kt:us-department-of-commerce}
  - {predicate: basedOn, object: kt:export-control-reform-act}
  - {predicate: enables, object: kt:ai-chip-export-controls}
  - {predicate: influencedBy, object: kt:executive-orders-on-ai}
sources:
  - id: s1
    title: "The U.S. Export Control System and the Export Control Reform Act of 2018 (R46814)"
    publisher: Congressional Research Service (Fergusson, Kerr and Casey), updated 7 June 2021
    url: https://www.congress.gov/crs_external_products/R/PDF/R46814/R46814.5.pdf
    type: government
    accessed: 2026-11-10
  - id: s2
    title: "Commerce Renames Agency Bureau of Industry and Security (press release, 2002)"
    publisher: US Department of Commerce, Bureau of Industry and Security; archived by the UNT End of Term Web Archive
    url: https://webarchive.library.unt.edu/eot2008/20080920162232/https:/www.bis.doc.gov/news/2002/commercerenamesagencybis.htm
    type: government
    accessed: 2026-11-10
  - id: s3
    title: "Industry and Security Programs; Change of Agency Name and Office Name (final rule)"
    publisher: US Department of Commerce, Bureau of Industry and Security; Federal Register, 10 July 2002
    url: https://www.govinfo.gov/content/pkg/FR-2002-07-10/pdf/02-17154.pdf
    type: government
    accessed: 2026-11-10
  - id: s4
    title: "Establishment of Reporting Requirements for the Development of Advanced Artificial Intelligence Models and Computing Clusters (proposed rule)"
    publisher: US Department of Commerce, Bureau of Industry and Security; Federal Register, 11 September 2024 (RIN 0694-AJ55)
    url: https://govinfo.gov/content/pkg/FR-2024-09-11/pdf/2024-20529.pdf
    type: government
    accessed: 2026-11-10
  - id: s5
    title: "Executive Order 14148: Initial Rescissions of Harmful Executive Orders and Actions"
    publisher: The White House; Federal Register 90(17), 28 January 2025
    url: https://www.federalregister.gov/documents/full_text/text/2025/01/28/2025-01901.txt
    type: government
    accessed: 2026-11-10
  - id: s6
    title: "Department of Commerce Announces Rescission of Biden-Era Artificial Intelligence Diffusion Rule, Strengthens Chip-Related Export Controls"
    publisher: US Department of Commerce, Bureau of Industry and Security (press release, 13 May 2025)
    url: https://www.bis.gov/press-release/department-commerce-announces-rescission-biden-era-artificial-intelligence-diffusion-rule-strengthens
    type: government
    accessed: 2026-11-10
created: 2026-11-10
---

# Bureau of Industry and Security

The **Bureau of Industry and Security (BIS)** is the agency inside the US Department of Commerce that runs the licensing and enforcement side of America's dual-use export control system: the rules governing commercial goods, software and technology that also have military or security uses. It also enforces US anti-boycott regulations.[^s1] For AI, BIS matters because it is the office that writes and polices the restrictions on shipping advanced accelerators and chipmaking tools abroad, and it was the agency chosen to collect information from frontier model developers in 2024.[^s1][^s4]

## History

Commerce's export licensing and enforcement functions were split off from the International Trade Administration in 1985 under the Reagan administration, to separate control from export promotion.[^s1] The agency later operated as the Bureau of Export Administration. On 18 April 2002 it was renamed the Bureau of Industry and Security, a change published in the Federal Register later that month and followed by conforming amendments to its regulations.[^s3] Under Secretary Kenneth Juster said the new name better reflected work spanning national, homeland, economic and cyber security; the announcement listed duties beyond export controls, including Chemical Weapons Convention compliance, critical-infrastructure outreach and monitoring the defense industrial base.[^s2]

## Legal authority and tools

For decades the system rested on the Export Administration Act of 1979, which last expired in 2001; from 1994 to 2018, apart from a ten-month reauthorization in 2000–2001, the controls were kept in force under emergency powers in the International Emergency Economic Powers Act. The **Export Control Reform Act of 2018 (ECRA)** gave BIS permanent statutory authority with no expiry date, and it was the first export control statute to treat economic security as part of national security.[^s1]

BIS implements ECRA through the **Export Administration Regulations (EAR)**. Nearly every US-origin item is subject to the EAR. Controlled items appear on the **Commerce Control List**, organised into nine categories, each item carrying an Export Control Classification Number. The **Entity List**, first published in 1997 and maintained by an interagency End User Review Committee, names foreign parties that need special licences; it held 1,644 entries in FY2020.[^s1] ECRA also directed Commerce to lead an interagency process to identify "emerging and foundational technologies" for new controls.[^s1]

Licence applications pass through interagency review with Defense, State and Energy, under statutory deadlines and a three-level escalation process for disputes. Enforcement falls to BIS's Office of Export Enforcement, which (as of 2021) had 23 US field offices and officers posted in seven foreign countries; ECRA set criminal penalties of up to $1 million and 20 years in prison per violation, and civil penalties of up to $300,000 or twice the transaction value.[^s1]

## Role in AI governance

**Chip export controls.** BIS issues the rules that restrict advanced AI chips, high-bandwidth memory and semiconductor equipment to China and other countries of concern. Its rules can also be reversed by new administrations: on 13 May 2025 BIS announced it would rescind the January 2025 AI Diffusion Rule before compliance began, while adding guidance on Huawei Ascend chips, on letting US chips train Chinese models, and on diversion through third countries.[^s6]

**Frontier model reporting.** In September 2024 BIS proposed quarterly reporting by US developers of AI models trained with more than 10^26 operations and by owners of large computing clusters, using information-collection powers in section 705 of the Defense Production Act to implement Executive Order 14110. Reports would cover training plans, model-weight security and the results of red-team testing.[^s4] Executive Order 14110 was revoked on 20 January 2025 by Executive Order 14148, removing the order that rule was written to implement.[^s5]

## Limitations and debates

BIS works on a dual mandate: keeping sensitive technology from adversaries while not unduly harming US exporters. ECRA builds this tension into licensing: it requires an assessment of each decision's impact on the US defense industrial base, and majority interagency approval for licences on emerging and foundational technologies.[^s1] Because most of its AI-relevant actions are interim rules and guidance, they can shift sharply with policy priorities, as the 2025 rescission showed.[^s6]

## Connections

BIS is **part of** the US Department of Commerce and its powers are **based on** the Export Control Reform Act.[^s1] It is the author of US **AI chip export controls**, the most visible instrument of **compute governance**, and sits within **AI governance** more broadly.[^s6] Its proposed frontier-model reporting rule was **influenced by** presidential **executive orders on AI** and required disclosure of **red-teaming** results, overlapping with the evaluation remit of **AI safety institutes**.[^s4][^s5]

## Sources

[^s1]: Fergusson, Kerr and Casey, "The U.S. Export Control System and the Export Control Reform Act of 2018", Congressional Research Service R46814, updated 7 June 2021. https://www.congress.gov/crs_external_products/R/PDF/R46814/R46814.5.pdf (accessed 2026-11-10)
[^s2]: US Department of Commerce, "Commerce Renames Agency Bureau of Industry and Security", press release (2002), UNT End of Term archive. https://webarchive.library.unt.edu/eot2008/20080920162232/https:/www.bis.doc.gov/news/2002/commercerenamesagencybis.htm (accessed 2026-11-10)
[^s3]: Bureau of Industry and Security, "Industry and Security Programs; Change of Agency Name and Office Name", Federal Register, 10 July 2002. https://www.govinfo.gov/content/pkg/FR-2002-07-10/pdf/02-17154.pdf (accessed 2026-11-10)
[^s4]: Bureau of Industry and Security, "Establishment of Reporting Requirements for the Development of Advanced Artificial Intelligence Models and Computing Clusters", proposed rule, Federal Register, 11 September 2024. https://govinfo.gov/content/pkg/FR-2024-09-11/pdf/2024-20529.pdf (accessed 2026-11-10)
[^s5]: Executive Order 14148, "Initial Rescissions of Harmful Executive Orders and Actions", Federal Register, 28 January 2025. https://www.federalregister.gov/documents/full_text/text/2025/01/28/2025-01901.txt (accessed 2026-11-10)
[^s6]: Bureau of Industry and Security, "Department of Commerce Announces Rescission of Biden-Era Artificial Intelligence Diffusion Rule, Strengthens Chip-Related Export Controls", press release, 13 May 2025. https://www.bis.gov/press-release/department-commerce-announces-rescission-biden-era-artificial-intelligence-diffusion-rule-strengthens (accessed 2026-11-10)
