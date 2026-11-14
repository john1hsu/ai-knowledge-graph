---
id: kt:model-cards
type: Technique
title: Model cards
aliases: [model card, model cards for model reporting]
domain: governance-and-policy
summary: >-
  Short, structured documents that accompany a trained machine learning model and report its intended use,
  training and evaluation data, performance disaggregated across groups and conditions, ethical considerations
  and known limitations; proposed by Mitchell et al. at FAT* 2019.
maturity: established
broader: [kt:ai-governance]
related: [kt:algorithmic-bias-and-fairness, kt:datasheets-for-datasets, kt:nist-ai-risk-management-framework, kt:eu-ai-act, kt:ai-evaluation, kt:omb-ai-memoranda]
relations:
  - {predicate: introducedIn, object: kt:model-cards-for-model-reporting}
  - {predicate: createdBy, object: kt:margaret-mitchell}
  - {predicate: implementedIn, object: kt:hugging-face-hub}
  - {predicate: studiedIn, object: kt:fairness-accountability-and-transparency}
sources:
  - id: s1
    title: "Model Cards for Model Reporting"
    publisher: FAT* 2019 (Mitchell, Wu, Zaldivar, Barnes, Vasserman, Hutchinson, Spitzer, Raji, Gebru); arXiv:1810.03993
    url: https://ar5iv.labs.arxiv.org/html/1810.03993
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s2
    title: "Model Cards — Hub documentation"
    publisher: Hugging Face
    url: https://huggingface.co/docs/hub/en/model-cards
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "AI RMF Playbook — Measure"
    publisher: NIST Trustworthy and Responsible AI Resource Center
    url: https://airc.nist.gov/airmf-resources/playbook/measure/
    type: government
    accessed: 2026-11-14
  - id: s4
    title: "Annex XI: Technical documentation referred to in Article 53(1)(a) — general-purpose AI models"
    publisher: European Commission AI Act Service Desk (Regulation (EU) 2024/1689)
    url: https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-11
    type: government
    accessed: 2026-11-14
  - id: s5
    title: "What's documented in AI? Systematic Analysis of 32K AI Model Cards"
    publisher: arXiv:2402.05160 (Liang, Rajani, Yang, Ozoani, Wu, Chen, Smith, Zou), February 2024
    url: https://arxiv.org/abs/2402.05160v1
    type: preprint
    accessed: 2026-11-14
created: 2026-11-14
---

# Model cards

A **model card** is a brief, standardized report that travels with a trained machine learning model and tells prospective users what the model is for, how it was built and evaluated, and where it is likely to fail. The idea was introduced by Margaret Mitchell, Timnit Gebru and colleagues, most of them at Google, in the paper "Model Cards for Model Reporting" at the FAT* 2019 conference on fairness, accountability and transparency.[^s1] The authors argued that models were increasingly used in high-stakes settings such as health care, hiring, education and policing, yet there was no standard way to communicate their performance characteristics, so biases often surfaced only after deployment. They proposed cards of roughly one to two pages so that a reader can judge whether a model suits their context.[^s1]

## Structure

The original paper proposes nine sections: Model Details, Intended Use, Factors, Metrics, Evaluation Data, Training Data, Quantitative Analyses, Ethical Considerations, and Caveats and Recommendations.[^s1] The distinctive element is **disaggregated evaluation**: results are reported separately for relevant groups (demographic, cultural or phenotypic), for environmental or instrumentation conditions, and for intersections of groups such as age combined with gender, because an aggregate score can hide poor performance on a subgroup. Cards are also expected to justify the chosen metrics and decision thresholds and to report uncertainty, for example confidence intervals.[^s1]

The paper illustrates this with two worked cards. For a smiling-detection classifier trained on CelebA, the breakdown showed a notably higher false discovery rate for older men. For two versions of a toxicity classifier, the card showed that the earlier version scored identity terms such as "gay" as toxic far more often than the later, bias-mitigated version, which the authors used to argue that cards must be updated with each release.[^s1]

## Model cards in practice

The format became the default documentation layer of open model hosting. On the Hugging Face Hub, a model card is simply the repository's `README.md`: a YAML metadata header (license, languages, training datasets, base model, task, and machine-readable evaluation results in a `model-index` block) followed by free-text sections on the model, intended uses and limitations, training details, datasets and evaluation. The Hub documentation points to Mitchell et al. for the limitations and ethics content and provides a template and an annotated guide.[^s2]

Model cards also appear in risk-management guidance. NIST's AI RMF Playbook names model cards, alongside datasheets for datasets, as an example of documentation best practice for measurement (MEASURE 2.1) and as a transparency tool for recording explanatory and validation information (MEASURE 2.9).[^s3] The EU AI Act does not mandate the "model card" label, but Annex XI requires providers of general-purpose AI models to keep technical documentation that overlaps heavily with one: intended tasks, acceptable use policies, architecture and parameter count, licence, training-data provenance and curation, training compute and energy use, and, for models with systemic risk, evaluation and adversarial-testing results.[^s4] Frontier labs' longer "system cards" extend the same idea to a deployed system rather than a single set of weights.

## Evidence and limitations

The original authors cautioned that a card is only as trustworthy as its author, that standardized fields do not by themselves prevent misleading reporting, and that cards should sit alongside third-party audits, adversarial testing and user feedback. Disaggregated evaluation also needs demographic labels, which raise privacy concerns and are often missing from available test sets.[^s1]

Empirical work bears out uneven practice. A 2024 study of 32,111 model cards on Hugging Face (Liang et al., a preprint) found that most heavily downloaded models had cards, but quality varied widely: training sections were the most consistently filled in, while environmental impact, limitations and evaluation sections were the least. In an intervention adding detailed cards to 42 popular models with sparse documentation, the authors reported a moderate association with higher weekly downloads.[^s5]

## Connections

Model cards sit under `kt:ai-governance` as a transparency mechanism and grew out of the `kt:fairness-accountability-and-transparency` research community; they are the model-side complement to `kt:datasheets-for-datasets`, which document the data a model is trained on.[^s1] Their disaggregated metrics are a primary tool for surfacing `kt:algorithmic-bias-and-fairness` problems and draw on `kt:ai-evaluation` practice.[^s1] They are implemented at scale on the `kt:hugging-face-hub`[^s2], recommended by the `kt:nist-ai-risk-management-framework` playbook[^s3], and echoed in the GPAI documentation duties of the `kt:eu-ai-act`.[^s4] The `kt:omb-ai-memoranda` node is linked as a neighbouring governance instrument that already points to this one.

## Sources
[^s1]: Mitchell et al., "Model Cards for Model Reporting", FAT* 2019 (arXiv:1810.03993). https://ar5iv.labs.arxiv.org/html/1810.03993 (accessed 2026-11-14)
[^s2]: Hugging Face, "Model Cards", Hub documentation. https://huggingface.co/docs/hub/en/model-cards (accessed 2026-11-14)
[^s3]: NIST, "AI RMF Playbook — Measure". https://airc.nist.gov/airmf-resources/playbook/measure/ (accessed 2026-11-14)
[^s4]: European Commission AI Act Service Desk, "Annex XI" of Regulation (EU) 2024/1689. https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-11 (accessed 2026-11-14)
[^s5]: Liang et al., "What's documented in AI? Systematic Analysis of 32K AI Model Cards", arXiv:2402.05160, 2024. https://arxiv.org/abs/2402.05160v1 (accessed 2026-11-14)
