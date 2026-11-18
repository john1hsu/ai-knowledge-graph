---
id: kt:responsible-scaling-policy
type: Policy
title: Responsible scaling policy
aliases: [RSP, responsible scaling policies, frontier AI safety policy]
domain: safety-alignment-and-security
summary: >-
  A voluntary, published commitment framework in which a frontier AI developer ties specified dangerous-capability
  thresholds to the safety and security safeguards it must have in place before training or deploying more capable models.
maturity: emerging
broader: [kt:ai-safety, kt:ai-risk-management]
related: [kt:red-teaming, kt:jailbreak, kt:frontier-ai-safety-commitments, kt:ai-safety-institutes]
relations:
  - {predicate: createdBy, object: kt:anthropic}
  - {predicate: createdBy, object: kt:metr}
  - {predicate: influencedBy, object: kt:biosafety-level}
  - {predicate: dependsOn, object: kt:ai-evaluation}
  - {predicate: hasPart, object: kt:ai-safety-level}
sources:
  - id: s1
    title: "Responsible Scaling Policies (RSPs)"
    publisher: METR (Barnes, Wijk, Chan), 26 September 2023
    url: https://metr.org/blog/2023-09-26-rsp
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "Anthropic's Responsible Scaling Policy"
    publisher: Anthropic, 19 September 2023
    url: https://www.anthropic.com/news/anthropics-responsible-scaling-policy
    type: lab-research
    accessed: 2026-11-18
  - id: s3
    title: "Anthropic's Responsible Scaling Policy (policy page and version history, v3.4)"
    publisher: Anthropic, last updated 14 August 2026
    url: https://www.anthropic.com/rsp
    type: primary
    accessed: 2026-11-18
  - id: s4
    title: "Activating AI Safety Level 3 Protections"
    publisher: Anthropic, 22 May 2025
    url: https://anthropic.com/news/activating-asl3-protections
    type: lab-research
    accessed: 2026-11-18
  - id: s5
    title: "Frontier AI Safety Commitments, AI Seoul Summit 2024"
    publisher: UK Department for Science, Innovation and Technology (GOV.UK), 21 May 2024
    url: https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-safety-commitments-ai-seoul-summit-2024
    type: government
    accessed: 2026-11-18
  - id: s6
    title: "Common Elements of Frontier AI Safety Policies (December 2025 Update)"
    publisher: METR, 9 December 2025
    url: https://metr.org/blog/2025-12-09-common-elements-of-frontier-ai-safety-policies/
    type: community
    accessed: 2026-11-18
  - id: s7
    title: "Anthropic's RSP v3.0: How it Works, What's Changed, and Some Reflections"
    publisher: Centre for the Governance of AI (Williams, Freund), 5 March 2026
    url: https://www.governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections
    type: community
    accessed: 2026-11-18
created: 2026-11-18
---

# Responsible scaling policy

A **responsible scaling policy (RSP)** is a public, self-imposed framework in which an AI developer states which levels of dangerous capability it can safely handle with its current protections, and what it will do (strengthen safeguards, delay deployment or stop scaling) when its models approach capabilities that outrun those protections.[^s1] The term names both a general governance idea, set out by the evaluation nonprofit METR (then ARC Evals) in September 2023, and the specific policy Anthropic published under that name a week earlier.[^s1][^s2] Comparable documents from other labs go by other names, so the generic category is often called a "frontier AI safety policy."[^s6]

## Origin

METR's September 2023 note by Beth Barnes, Hjalmar Wijk and Lawrence Chan framed the RSP as a way to keep protective measures ahead of dangerous capabilities. It listed five elements a good policy needs: **limits** (capability observations that would make further scaling unsafe), **protections** (the measures that contain risk today), **evaluation** (procedures to catch early warning signs), **response** (a commitment to pause if protections cannot keep up) and **accountability** (how compliance is verified and how the policy itself changes).[^s1] Anthropic's first RSP, approved by its board on 19 September 2023, put this into practice through **AI Safety Levels (ASLs)**, loosely modelled on the biosafety levels used for handling dangerous pathogens.[^s2]

## How it works

The 2023 Anthropic policy defined ASL-1 as systems with no meaningful catastrophic risk, ASL-2 as systems showing early signs of dangerous capability that do not yet beat a search engine or textbook, and ASL-3 as systems that substantially raise catastrophic-misuse risk or show low-level autonomy. At the time Anthropic judged its Claude models to be ASL-2, and it committed to defining ASL-4 measures before reaching ASL-3.[^s2] The policy's logic is conditional: capability evaluations run during training and before deployment, and crossing a threshold triggers a required standard of deployment safeguards and model-weight security.[^s2][^s6]

The first real trigger came on 22 May 2025, when Anthropic launched Claude Opus 4 under the ASL-3 Deployment and Security Standards as a precaution. The company had not concluded that the model crossed the threshold, but it could no longer clearly rule this out for chemical, biological, radiological and nuclear (CBRN) risk.[^s4] The safeguards included real-time classifiers screening inputs and outputs for a narrow band of weapons-related content, a jailbreak bug bounty, more than 100 security controls such as two-party authorization for weight access, and egress-bandwidth limits meant to make weight exfiltration harder.[^s4]

## Evolution and critiques

Anthropic's policy has been revised often: v2.0 in October 2024, v2.1 and v2.2 in 2025, a full rewrite as v3.0 on 24 February 2026, and v3.4 effective 8 July 2026 (as of November 2026).[^s3] Version 3.0 added a non-binding **Frontier Safety Roadmap** of safety goals and periodic **Risk Reports** assessing models already deployed. Later versions let the Long-Term Benefit Trust request external review of those reports.[^s3] An analysis by the Centre for the Governance of AI found that v3.0 also dropped the earlier implied pause commitment. It now separates a few unilateral commitments, such as keeping ASL-3 protections, from "industry-wide recommendations" that Anthropic would adopt mainly if competitors do.[^s7] The authors welcomed the added transparency but noted critics' concern that the policy still relies largely on self-reporting.[^s7]

These concerns echo limits METR raised at the outset. Voluntary policies do not substitute for regulation, conditional pauses are weaker than a reliable global pause, and early-stage evaluations can miss warning signs or raise false alarms.[^s1] METR also argued that RSPs could appeal both to people who want caution and to people who think catastrophic risk is distant, and that they could serve as a testing ground for future evaluation-based standards and regulation.[^s1]

## Spread to the wider industry

At the AI Seoul Summit on 21 May 2024, 16 organisations, later joined by four more, signed the **Frontier AI Safety Commitments**. They pledged to publish safety frameworks with risk thresholds and, if mitigations could not keep risk below those thresholds, not to develop or deploy the model at all.[^s5] By METR's December 2025 count, twelve companies had published such policies, including Anthropic, OpenAI, Google DeepMind, Meta, Microsoft, Amazon, xAI and NVIDIA. Most share capability thresholds for biological weapons, cyberattacks, autonomous replication or automated AI R&D, along with evaluations, weight security, deployment mitigations, halting conditions and an update process.[^s6] METR's update also tracks how these policies relate to newer requirements such as the EU AI Act's General-Purpose AI Code of Practice and California's SB 53.[^s6]

## Connections

An RSP is a capability-threshold form of **AI risk management** and a practical tool of **AI safety** (`broader`).[^s1][^s6] It **depends on** **AI evaluation**, since dangerous-capability tests decide when thresholds are crossed. **Red teaming** and **jailbreak** resistance testing check whether deployment safeguards hold.[^s2][^s4] The concept was **created by** METR and **Anthropic**, whose **AI Safety Levels** are **part** of its policy and were **influenced by** biosafety levels.[^s1][^s2] The **Frontier AI Safety Commitments** extended the idea across the industry, and government **AI safety institutes** are among the "trusted actors" whose input the commitments call for when setting thresholds.[^s5]

## Sources
[^s1]: Barnes, Wijk & Chan, "Responsible Scaling Policies (RSPs)", METR, 26 Sep 2023. https://metr.org/blog/2023-09-26-rsp (accessed 2026-11-18)
[^s2]: Anthropic, "Anthropic's Responsible Scaling Policy", 19 Sep 2023. https://www.anthropic.com/news/anthropics-responsible-scaling-policy (accessed 2026-11-18)
[^s3]: Anthropic, "Anthropic's Responsible Scaling Policy" (v3.4 and version history). https://www.anthropic.com/rsp (accessed 2026-11-18)
[^s4]: Anthropic, "Activating AI Safety Level 3 Protections", 22 May 2025. https://anthropic.com/news/activating-asl3-protections (accessed 2026-11-18)
[^s5]: UK DSIT, "Frontier AI Safety Commitments, AI Seoul Summit 2024", 21 May 2024. https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-safety-commitments-ai-seoul-summit-2024 (accessed 2026-11-18)
[^s6]: METR, "Common Elements of Frontier AI Safety Policies (December 2025 Update)", 9 Dec 2025. https://metr.org/blog/2025-12-09-common-elements-of-frontier-ai-safety-policies/ (accessed 2026-11-18)
[^s7]: Williams & Freund, "Anthropic's RSP v3.0: How it Works, What's Changed, and Some Reflections", GovAI, 5 Mar 2026. https://www.governance.ai/analysis/anthropics-rsp-v3-0-how-it-works-whats-changed-and-some-reflections (accessed 2026-11-18)
