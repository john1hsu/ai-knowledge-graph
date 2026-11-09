---
id: kt:algorithmic-bias-and-fairness
type: Risk
title: Algorithmic bias and fairness
aliases: [algorithmic bias, AI bias, fairness in machine learning, ML fairness, algorithmic fairness]
domain: governance-and-policy
summary: >-
  Algorithmic bias is systematic, unjustified disparity in how an automated or machine-learning system treats or
  performs for different groups of people; algorithmic fairness is the study of formal criteria, measurements and
  interventions for detecting and reducing such disparities, together with the trade-offs between them.
maturity: established
broader: [kt:ai-governance, kt:ai-ethics]
related: [kt:nist-ai-risk-management-framework, kt:ai-evaluation, kt:model-cards, kt:facial-recognition, kt:bias-variance-tradeoff]
relations:
  - {predicate: regulatedBy, object: kt:eu-ai-act}
  - {predicate: studiedIn, object: kt:fairness-accountability-and-transparency}
sources:
  - id: s1
    title: "Fairness and Machine Learning: Limitations and Opportunities — Chapter 3, Classification"
    publisher: MIT Press, 2023 (Barocas, Hardt, Narayanan); online edition at fairmlbook.org
    url: https://fairmlbook.org/classification.html
    type: textbook
    accessed: 2026-11-09
  - id: s2
    title: "Equality of Opportunity in Supervised Learning"
    publisher: NeurIPS 2016 (Hardt, Price, Srebro)
    url: https://papers.nips.cc/paper/2016/file/9d2682367c3935defcb1f9e247a97c0d-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s3
    title: "Inherent Trade-Offs in the Fair Determination of Risk Scores"
    publisher: ITCS 2017, LIPIcs vol. 67 (Kleinberg, Mullainathan, Raghavan)
    url: https://drops.dagstuhl.de/opus/volltexte/2017/8156/pdf/LIPIcs-ITCS-2017-43.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification"
    publisher: Proceedings of the 1st Conference on Fairness, Accountability and Transparency, PMLR 81 (Buolamwini, Gebru), 2018
    url: https://proceedings.mlr.press/v81/buolamwini18a.html
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s5
    title: "Towards a Standard for Identifying and Managing Bias in Artificial Intelligence (NIST SP 1270)"
    publisher: National Institute of Standards and Technology (Schwartz et al.), March 2022
    url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.Sp.1270.pdf
    type: government
    accessed: 2026-11-09
created: 2026-11-09
---

# Algorithmic bias and fairness

**Algorithmic bias** refers to systematic disparities in the decisions, scores or error rates that an automated system produces for different groups of people, typically groups defined by a sensitive attribute such as race, sex or age. **Algorithmic fairness** is the research and engineering field that formalizes what "fair" treatment by a predictor could mean, measures departures from it and designs interventions to reduce them.[^s1] NIST's SP 1270 stresses that such biases can cause harm whether or not anyone intended them, and that unmanaged bias undermines public trust in AI.[^s5]

The term is distinct from the *statistical* bias of an estimator studied in the bias-variance tradeoff, although statistical and computational errors are one of the sources of algorithmic bias described below.[^s5]

## Where bias comes from

NIST SP 1270 (March 2022) groups AI bias into three categories. **Systemic** bias is embedded in institutional procedures, norms and historical datasets that advantage some groups over others. **Statistical and computational** bias arises from unrepresentative samples and flawed modelling choices. **Human** bias comes from the cognition of the people who design, deploy and rely on systems, including anchoring, confirmation bias and over-reliance on automation. NIST argues for a socio-technical view: technical fixes alone cannot remove bias, and zero bias risk is not an achievable goal.[^s5]

A common naive remedy, dropping the sensitive attribute ("fairness through unawareness"), does not work in general. Other features often encode the attribute redundantly, so a model can effectively reconstruct it, and deleting it can also throw away legitimately useful information.[^s1]

## Formal fairness criteria

Barocas, Hardt and Narayanan organize most group-fairness definitions around three conditional-independence properties of a score *R*, sensitive attribute *A* and outcome *Y*:[^s1]

- **Independence** (*R* ⊥ *A*): acceptance rates are equal across groups, also called demographic parity.[^s1]
- **Separation** (*R* ⊥ *A* | *Y*): true-positive and false-positive rates are equal across groups.[^s1]
- **Sufficiency** (*Y* ⊥ *A* | *R*): a given score means the same thing in every group, closely related to calibration by group.[^s1]

Hardt, Price and Srebro (NeurIPS 2016) introduced separation for classifiers as **equalized odds** and its relaxation **equal opportunity**, which only requires equal true-positive rates. They criticized demographic parity because it can be met by accepting qualified people in one group and random people in another, and because it rules out a perfect predictor when outcomes differ between groups. They also showed that any trained predictor can be adjusted after training to satisfy their criteria. In a FICO credit-score case study, race-blind thresholds retained 99.3% of maximum profit, equal opportunity 92.8%, equalized odds 80.2% and demographic parity 69.8%.[^s2]

## Impossibility results

These criteria conflict. Kleinberg, Mullainathan and Raghavan (ITCS 2017) proved that calibration within groups and balance of average scores for both the positive and negative class can all hold only in two special cases: perfect prediction or equal base rates between groups.[^s3] The textbook treatment generalizes this: independence and sufficiency are incompatible whenever *A* and *Y* are dependent, and separation and sufficiency are likewise incompatible in that setting for any classifier that makes errors. So choosing a fairness metric is a value judgment about which errors matter, not a purely technical step.[^s1]

## Evidence: Gender Shades

Buolamwini and Gebru's *Gender Shades* (FAT* 2018) became a reference case for measuring bias. Two widely used face benchmarks, IJB-A and Adience, were 79.6% and 86.2% lighter-skinned. The authors built a new benchmark balanced by gender and Fitzpatrick skin type and audited three commercial gender classifiers. Darker-skinned women had error rates of up to 34.7%, while lighter-skinned men had a maximum error rate of 0.8%.[^s4] The study showed why disaggregated, intersectional evaluation matters: aggregate accuracy hid large subgroup gaps.

## In practice

Practitioner guidance stresses process over any single metric. NIST recommends checking that datasets represent the affected population and documenting their limits. It also calls for evaluating performance stratified by group under realistic conditions, monitoring deployed systems continuously and involving affected stakeholders. It warns that putting a human in the loop does not reliably remove bias.[^s5] Post-processing such as group-specific thresholds is one of several technical levers, alongside pre-processing of data and in-training constraints, and each shifts costs among groups and the decision maker.[^s1][^s2]

## Connections

Algorithmic bias is a core risk within **AI governance** and **AI ethics** (broader). NIST positions SP 1270 alongside its AI Series, the family that includes the **NIST AI Risk Management Framework**, which treats bias management as part of trustworthy AI.[^s5] Bias audits are a form of **AI evaluation** and are natural content for **model cards**; *Gender Shades* audited face-analysis systems of the kind used in **facial recognition**.[^s4] The study appeared at the first **Fairness, Accountability and Transparency** conference, the field's main interdisciplinary venue.[^s4] Regulation such as the **EU AI Act** is the policy-side counterpart to the technical criteria above. The **bias-variance tradeoff** is linked by name only: it concerns estimator error, which is just one contributor to group disparities.[^s1][^s5]

## Sources
[^s1]: Barocas, Hardt, Narayanan, *Fairness and Machine Learning: Limitations and Opportunities*, MIT Press, 2023, ch. 3 "Classification". https://fairmlbook.org/classification.html (accessed 2026-11-09)
[^s2]: Hardt, Price, Srebro, "Equality of Opportunity in Supervised Learning", NeurIPS 2016. https://papers.nips.cc/paper/2016/file/9d2682367c3935defcb1f9e247a97c0d-Paper.pdf (accessed 2026-11-09)
[^s3]: Kleinberg, Mullainathan, Raghavan, "Inherent Trade-Offs in the Fair Determination of Risk Scores", ITCS 2017, LIPIcs 67. https://drops.dagstuhl.de/opus/volltexte/2017/8156/pdf/LIPIcs-ITCS-2017-43.pdf (accessed 2026-11-09)
[^s4]: Buolamwini, Gebru, "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification", PMLR 81 (FAT* 2018). https://proceedings.mlr.press/v81/buolamwini18a.html (accessed 2026-11-09)
[^s5]: Schwartz et al., "Towards a Standard for Identifying and Managing Bias in Artificial Intelligence", NIST SP 1270, March 2022. https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.Sp.1270.pdf (accessed 2026-11-09)
