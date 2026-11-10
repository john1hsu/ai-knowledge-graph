---
id: kt:ai-chip-export-controls
type: Policy
title: AI chip export controls
aliases: [US AI chip export controls, advanced computing export controls, semiconductor export controls on China, October 7 export controls]
domain: governance-and-policy
summary: >-
  The US export rules, administered by the Commerce Department's Bureau of Industry and Security since October
  2022, that restrict which advanced AI accelerators, high-bandwidth memory, chipmaking tools and related
  services may go to China and other countries of concern, as a way to limit adversaries' access to AI compute.
maturity: emerging
broader: [kt:ai-governance, kt:compute-governance]
related: [kt:nvidia, kt:ai-accelerator, kt:gpu-computing, kt:tpu, kt:scaling-laws, kt:executive-orders-on-ai]
relations:
  - {predicate: createdBy, object: kt:bureau-of-industry-and-security}
  - {predicate: basedOn, object: kt:export-control-reform-act}
sources:
  - id: s1
    title: "The United States Announces Export Controls to Restrict China's Ability to Purchase and Manufacture High-End Chips"
    publisher: American Journal of International Law 117(1):144–150, 2023 (Contemporary Practice of the United States), doi:10.1017/ajil.2022.89
    url: https://www.cambridge.org/core/product/A5295D4E8C992F024040F84EB1B471C5/core-reader
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s2
    title: "Commerce Strengthens Restrictions on Advanced Computing Semiconductors, Semiconductor Manufacturing Equipment, and Supercomputing Items to Countries of Concern"
    publisher: US Department of Commerce, Bureau of Industry and Security (press release, 17 October 2023)
    url: https://www.bis.gov/press-release/commerce-strengthens-restrictions-advanced-computing-semiconductors-semiconductor-manufacturing-equipment
    type: government
    accessed: 2026-11-10
  - id: s3
    title: "Understanding the Biden Administration's Updated Export Controls"
    publisher: Center for Strategic and International Studies (Gregory C. Allen), 11 December 2024
    url: https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls
    type: community
    accessed: 2026-11-10
  - id: s4
    title: "Framework for Artificial Intelligence Diffusion (interim final rule)"
    publisher: US Department of Commerce, Bureau of Industry and Security; Federal Register, 15 January 2025
    url: https://www.govinfo.gov/content/pkg/FR-2025-01-15/html/2025-00636.htm
    type: government
    accessed: 2026-11-10
  - id: s5
    title: "Department of Commerce Announces Rescission of Biden-Era Artificial Intelligence Diffusion Rule, Strengthens Chip-Related Export Controls"
    publisher: US Department of Commerce, Bureau of Industry and Security (press release, 13 May 2025)
    url: https://www.bis.gov/press-release/department-commerce-announces-rescission-biden-era-artificial-intelligence-diffusion-rule-strengthens
    type: government
    accessed: 2026-11-10
  - id: s6
    title: "Revision to License Review Policy for Advanced Computing Commodities (final rule, 91 FR 1684)"
    publisher: US Department of Commerce, Bureau of Industry and Security; Federal Register, 15 January 2026
    url: https://www.govinfo.gov/content/pkg/FR-2026-01-15/html/2026-00789.htm
    type: government
    accessed: 2026-11-10
created: 2026-11-10
---

# AI chip export controls

**AI chip export controls** are the rules under the US Export Administration Regulations (EAR) that limit the sale of advanced AI accelerators, the memory and manufacturing tools needed to build them, and some related services to China and other countries of concern. They are written and enforced by the Commerce Department's Bureau of Industry and Security (BIS). The regime began with an interim final rule issued on 7 October 2022, which created new control classifications for high-end chips, chipmaking equipment and supercomputers, set a presumption of denial for licences, and justified the move on national-security grounds: advanced computing could improve military decision-making, weapons design and surveillance.[^s1] Because frontier AI capability depends heavily on training compute, the controls are the most direct lever any government has used to shape who can build large models.

## How the controls work

The 2022 rule combined several instruments. It placed advanced chips and the computers containing them on the Commerce Control List; extended US jurisdiction to some foreign-made chips and tools through **foreign direct product rules** (one aimed at 28 Chinese parties on the Entity List); and barred US persons from "supporting" the development or production of certain chips in China without a licence.[^s1] The Netherlands and Japan, home to key lithography and equipment makers, were singled out as essential partners, and reportedly agreed to adopt parallel controls.[^s1]

Chips are caught by technical thresholds rather than by product name. The October 2023 update dropped interconnect bandwidth as a criterion and added a **performance density** test alongside the existing performance test, so a chip exceeding either is controlled; BIS described the change as closing loopholes and heading off future workarounds.[^s2] It also required licences for sales to companies headquartered in, or with a parent in, arms-embargoed countries or Macau wherever they are located; extended presumption-of-denial licensing to 22 arms-embargoed destinations; and created a notification exception for chips just below the limit.[^s2] A December 2024 package added country-wide controls on advanced **high-bandwidth memory** (HBM2e and newer, set by a memory-bandwidth-density threshold of 3.3 GB/s per mm²), more chipmaking tools, two new foreign direct product rules, and 140 Entity List additions, while leaving the chip performance thresholds as set in 2023.[^s3]

## The diffusion framework and its reversal

In January 2025 BIS published the **Framework for Artificial Intelligence Diffusion**, which would have turned the China-focused regime into a global one. Nineteen destinations (the US and 18 close partners) were exempt; everyone else faced licence requirements or per-country compute allocations, and validated data-centre operators were capped on how much of their AI compute could sit outside trusted countries. It also controlled, for the first time, the weights of closed models trained with more than 10^26 operations, while leaving open-weight models uncontrolled.[^s4] Compliance was due on 15 May 2025, but on 13 May 2025 BIS rescinded the rule, told enforcement staff not to enforce it, promised an unspecified replacement, and instead issued guidance warning about Huawei Ascend chips, the use of US chips to train Chinese models, and diversion schemes.[^s5]

## Recent developments (as of January 2026)

Policy then moved toward conditional sales. A final rule effective 15 January 2026 switched licence review for exports to China and Macau from a presumption of denial to **case-by-case review** for chips below a total processing performance of 21,000 and a DRAM bandwidth of 6,500 GB/s, naming NVIDIA's H200 and AMD's MI325X as examples.[^s6] Approval is conditional: aggregate exports to China may not exceed 50% of the compute the vendor shipped to US customers, every shipment must be checked by an independent US testing lab, buyers need know-your-customer controls against unauthorised remote access, and military end users remain barred.[^s6] Chips above those thresholds, and sales to entities headquartered in arms-embargoed countries but located elsewhere, stay under a presumption of denial.[^s6]

## Debates and limitations

Analysts disagree about effectiveness. Successive updates have had to close workarounds, including purchases through overseas subsidiaries and diversion via third countries, and each widened the regime's scope.[^s2][^s3][^s5] Unilateral controls also depend on allies: equipment from the Netherlands and Japan matters as much as US chips, and the December 2024 rules exempted only countries with equivalent controls from new foreign direct product rules.[^s1][^s3] Remote access to cloud compute, and the policy swing between the 2025 diffusion framework and the 2026 conditional-sales rule, show that the regime is still being redesigned.[^s4][^s6]

## Connections

The controls are an instrument of national **AI governance** and the leading real-world case of **compute governance**: they treat chips as a chokepoint, and the 2025 framework even used a training-compute threshold (10^26 operations) to decide which model weights to control, echoing the compute-capability link described by **scaling laws**.[^s4] They apply directly to **NVIDIA** and other makers of **AI accelerators** and **GPU computing** hardware; the 2026 rule names NVIDIA's H200 and AMD's MI325X, and its thresholds cover any accelerator, including custom chips such as the **TPU**.[^s6] They are **created by** BIS and **based on** the Export Control Reform Act of 2018, which the 2026 rule cites as its authority.[^s6] They sit alongside **executive orders on AI** in the US policy mix, and their direction has shifted with each administration, as the 2025 rescission shows.[^s5]

## Sources

[^s1]: "The United States Announces Export Controls to Restrict China's Ability to Purchase and Manufacture High-End Chips", *American Journal of International Law* 117(1), 2023. https://www.cambridge.org/core/product/A5295D4E8C992F024040F84EB1B471C5/core-reader (accessed 2026-11-10)
[^s2]: Bureau of Industry and Security, "Commerce Strengthens Restrictions on Advanced Computing Semiconductors…", 17 October 2023. https://www.bis.gov/press-release/commerce-strengthens-restrictions-advanced-computing-semiconductors-semiconductor-manufacturing-equipment (accessed 2026-11-10)
[^s3]: G. C. Allen, "Understanding the Biden Administration's Updated Export Controls", CSIS, 11 December 2024. https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls (accessed 2026-11-10)
[^s4]: Bureau of Industry and Security, "Framework for Artificial Intelligence Diffusion", Federal Register, 15 January 2025. https://www.govinfo.gov/content/pkg/FR-2025-01-15/html/2025-00636.htm (accessed 2026-11-10)
[^s5]: Bureau of Industry and Security, rescission of the AI Diffusion Rule, 13 May 2025. https://www.bis.gov/press-release/department-commerce-announces-rescission-biden-era-artificial-intelligence-diffusion-rule-strengthens (accessed 2026-11-10)
[^s6]: Bureau of Industry and Security, "Revision to License Review Policy for Advanced Computing Commodities", Federal Register, 15 January 2026. https://www.govinfo.gov/content/pkg/FR-2026-01-15/html/2026-00789.htm (accessed 2026-11-10)
