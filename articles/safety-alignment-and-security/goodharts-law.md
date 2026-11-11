---
id: kt:goodharts-law
type: Concept
title: Goodhart's law
aliases: [Goodharting, Goodhart effect]
domain: safety-alignment-and-security
summary: >-
  The principle that a statistical regularity or metric tends to stop tracking what it stood for once it is
  used as a target for control or optimisation; in AI it describes how optimising a proxy objective too hard
  can make performance on the true objective worse.
maturity: foundational
broader: [kt:ai-alignment, kt:ai-safety]
related: [kt:reward-hacking, kt:ai-evaluation, kt:benchmark-contamination, kt:rlhf, kt:reward-model, kt:campbells-law]
relations:
  - {predicate: createdBy, object: kt:charles-goodhart}
  - {predicate: causes, object: kt:reward-hacking}
sources:
  - id: s1
    title: "Categorizing Variants of Goodhart's Law"
    publisher: arXiv:1803.04585v4 (Manheim, Garrabrant), February 2019
    url: https://arxiv.org/pdf/1803.04585v4
    type: primary
    accessed: 2026-11-11
  - id: s2
    title: "RDP 9013: A Select Bibliography of Published Research by the Reserve Bank of Australia, 1969–1990 — Conference Volumes"
    publisher: Reserve Bank of Australia
    url: https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html
    type: government
    accessed: 2026-11-11
  - id: s3
    title: "Reliance on metrics is a fundamental challenge for AI"
    publisher: Patterns 3(5):100476, 2022 (Thomas, Uminsky)
    url: https://pmc.ncbi.nlm.nih.gov/articles/PMC9122957
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "Goodhart's Law in Reinforcement Learning"
    publisher: ICLR 2024 (Karwowski, Hayman, Bai, Kiendlhofer, Griffin, Skalse)
    url: https://proceedings.iclr.cc/paper_files/paper/2024/file/6ad68a54eaa8f9bf6ac698b02ec05048-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "Scaling Laws for Reward Model Overoptimization"
    publisher: ICML 2023, PMLR 202 (Gao, Schulman, Hilton)
    url: https://proceedings.mlr.press/v202/gao23h.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s6
    title: "Improving ratings: audit in the British University system"
    publisher: European Review 5(3):305–321, 1997 (Strathern)
    url: https://www.cambridge.org/core/journals/european-review/article/improving-ratings-audit-inthe-british-university-system/FC2EE640C0C44E3DB87C29FB666E9AAB
    type: peer-reviewed
    accessed: 2026-11-11
created: 2026-11-11
---

# Goodhart's law

**Goodhart's law** is the observation that a measure loses its value as a signal once people or systems are rewarded for moving it. Economist Charles Goodhart's original formulation held that an observed statistical regularity tends to collapse once pressure is placed on it for control purposes.[^s1] Machine learning inherits the problem directly: training minimises a loss or maximises a reward that is only a proxy for what designers actually want, so pushing hard on the proxy can pull the true objective down.[^s3]

## Origin and wording

Goodhart first proposed the idea in 1975, in the context of monetary policy targets.[^s3] The Reserve Bank of Australia's bibliography records his paper "Problems of Monetary Management: The U.K. Experience" in the RBA's 1976 *Papers in Monetary Economics* and notes that it contains the first reference to Goodhart's law.[^s2] The snappier phrasing most people quote, about a measure that becomes a target ceasing to be a good measure, is usually traced to anthropologist Marilyn Strathern's 1997 critique of audit culture in British universities.[^s3][^s6] Strathern argued that performance audit takes on a life of its own that can damage the activity it is meant to assess.[^s6] Related ideas include Campbell's law, on social indicators becoming corrupted when used for decisions, and the Lucas critique in macroeconomics; like Goodhart's law, both began as narrow claims and have since been read far more broadly.[^s1]

## Four mechanisms

Manheim and Garrabrant (2018–2019) argue that "Goodhart's law" lumps together distinct failure modes and separate four:[^s1]

- **Regressional:** selecting for a high proxy score also selects for noise, so the true goal in the tail is predictably lower than the proxy suggests.[^s1]
- **Extremal:** optimisation pushes the system into regions where the proxy–goal relationship observed in ordinary conditions no longer holds, either because the model was too simple or the regime changes.[^s1]
- **Causal:** the act of intervening changes the causal links between proxy and goal, for instance by teaching to the test or editing the metric directly.[^s1]
- **Adversarial:** other agents with different goals exploit the metric, including "cobra effect" cases where an incentive produces more of the problem it was meant to reduce.[^s1]

The authors stress that the damage grows with the optimisation power applied to the proxy, which is why they see the topic as especially important for capable AI systems.[^s1]

## Goodhart's law in machine learning

In reinforcement learning, Karwowski et al. (ICLR 2024) define "Goodharting" as the case where true reward first rises and then falls as a policy is optimised harder against a misspecified proxy reward. Across roughly 30,400 runs in four families of simple environments, they observed such a drop in 19.3% of cases, so it was common but not universal.[^s4] Their geometric account treats policies as points in a convex polytope of state-occupancy measures: steepest ascent on the proxy bends each time it hits a new face of the polytope, and after a bend the true reward can begin to decline, more likely when the angle between proxy and true reward is large.[^s4] For language models trained with human feedback, Gao, Schulman and Hilton (ICML 2023) found the same rise-then-fall pattern when optimising against a learned reward model and reported that the effect follows predictable trends with reward model size.[^s5]

Beyond training objectives, Thomas and Uminsky (2022) catalogue product-level cases: engagement metrics such as watch time standing in for user satisfaction, click-through rates crowding out long-term trust, and an automated essay grader that rewarded meaningless text packed with sophisticated vocabulary.[^s3]

## Mitigations and limits

No method removes the problem; the options trade some performance for robustness. Karwowski et al. propose an early-stopping rule that provably avoids Goodharting given a bound on the angle between proxy and true reward, but in their experiments it gave up on average about 10% to 44% of attainable true reward, and it needs that bound to be estimated well.[^s4] They also derive a pessimistic objective that maximises worst-case reward over plausible true rewards.[^s4] At the organisational level, Thomas and Uminsky recommend a slate of metrics rather than one number, external audits, qualitative evidence such as user research and model cards, and involving affected stakeholders in metric design.[^s3]

## Connections

Goodhart's law sits under **AI alignment** and **AI safety** (`broader`), because aligning a system means getting it to pursue an intended goal rather than a measurable stand-in.[^s1] It `causes` **reward hacking**, the RL and RLHF form in which an agent games a **reward model** or reward function; the RLHF case was quantified by Gao et al.[^s4][^s5] It also explains why **AI evaluation** results degrade when benchmarks become targets, a concern sharpened by **benchmark contamination**.[^s3] The law is `createdBy` **Charles Goodhart** and is closely related to **Campbell's law** on the corruption of social indicators.[^s1][^s2]

## Sources

[^s1]: Manheim and Garrabrant, "Categorizing Variants of Goodhart's Law", arXiv:1803.04585v4, 2019. https://arxiv.org/pdf/1803.04585v4 (accessed 2026-11-11)
[^s2]: Reserve Bank of Australia, RDP 9013 bibliography, Conference Volumes. https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html (accessed 2026-11-11)
[^s3]: Thomas and Uminsky, "Reliance on metrics is a fundamental challenge for AI", Patterns 3(5), 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9122957 (accessed 2026-11-11)
[^s4]: Karwowski et al., "Goodhart's Law in Reinforcement Learning", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/file/6ad68a54eaa8f9bf6ac698b02ec05048-Paper-Conference.pdf (accessed 2026-11-11)
[^s5]: Gao, Schulman and Hilton, "Scaling Laws for Reward Model Overoptimization", ICML 2023. https://proceedings.mlr.press/v202/gao23h.html (accessed 2026-11-11)
[^s6]: Strathern, "Improving ratings: audit in the British University system", European Review 5(3), 1997. https://www.cambridge.org/core/journals/european-review/article/improving-ratings-audit-inthe-british-university-system/FC2EE640C0C44E3DB87C29FB666E9AAB (accessed 2026-11-11)
