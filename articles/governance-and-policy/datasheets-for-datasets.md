---
id: kt:datasheets-for-datasets
type: Technique
title: Datasheets for datasets
aliases: [datasheet for datasets, dataset datasheet, dataset documentation datasheets]
domain: governance-and-policy
summary: >-
  A dataset-documentation framework proposed by Gebru et al. (arXiv 2018; Communications of the ACM 2021) in which
  every machine learning dataset ships with a datasheet answering structured questions about its motivation,
  composition, collection process, preprocessing, uses, distribution and maintenance.
maturity: established
broader: [kt:ai-governance]
related: [kt:model-cards, kt:data-cards, kt:dataset-cards]
relations:
  - {predicate: introducedIn, object: kt:datasheets-for-datasets-paper}
  - {predicate: createdBy, object: kt:timnit-gebru}
  - {predicate: implementedIn, object: kt:hugging-face-hub}
  - {predicate: mitigates, object: kt:algorithmic-bias-and-fairness}
  - {predicate: studiedIn, object: kt:fairness-accountability-and-transparency}
sources:
  - id: s1
    title: "Datasheets for Datasets (arXiv:1803.09010v5)"
    publisher: arXiv (Gebru, Morgenstern, Vecchione, Wortman Vaughan, Wallach, Daumé III, Crawford)
    url: https://arxiv.org/pdf/1803.09010v5
    type: primary
    accessed: 2026-11-16
  - id: s2
    title: "Datasheets for Datasets — Communications of the ACM 64(12):86–92"
    publisher: Microsoft Research publication page
    url: https://www.microsoft.com/en-us/research/publication/datasheets-for-datasets/
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "Data Cards: Purposeful and Transparent Dataset Documentation for Responsible AI"
    publisher: arXiv:2204.01075 (Pushkarna, Zaldivar, Kjartansson; Google Research)
    url: https://arxiv.org/pdf/2204.01075.pdf
    type: primary
    accessed: 2026-11-16
  - id: s4
    title: "Dataset Cards — Hub documentation"
    publisher: Hugging Face
    url: https://huggingface.co/docs/hub/en/datasets-cards
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "Navigating Dataset Documentations in AI: A Large-Scale Analysis of Dataset Cards on HuggingFace"
    publisher: ICLR 2024 poster (Yang, Liang, Zou)
    url: https://iclr.cc/virtual/2024/poster/17463
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s6
    title: "Navigating Dataset Documentations in AI (arXiv:2401.13822v1, full text)"
    publisher: arXiv (Yang, Liang, Zou)
    url: https://arxiv.org/html/2401.13822v1
    type: primary
    accessed: 2026-11-16
created: 2026-11-16
---

# Datasheets for datasets

**Datasheets for datasets** is a documentation practice for machine learning data: the people who build a dataset write a structured account of why it exists, what is in it, how it was gathered and processed, what it should and should not be used for, how it is distributed and who maintains it. The idea was introduced by Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III and Kate Crawford, first as an arXiv preprint in March 2018 and later in *Communications of the ACM* (vol. 64, no. 12, December 2021).[^s1][^s2] The authors' starting point was that machine learning had no standard way to document datasets, even though a dataset's characteristics strongly shape the behaviour of models trained on it and can carry unwanted biases into high-stakes uses.[^s1][^s2]

## Origin and analogy

The name comes from electronics, where every component is sold with a datasheet listing its operating characteristics, test results and recommended uses. Gebru et al. argued by analogy that every dataset should come with one too, and they also pointed to medicine, where clinical-trial reporting standards require attention to subpopulations and consent.[^s1] The goal is to improve communication between dataset **creators** and dataset **consumers**, and to promote transparency and accountability.[^s2]

## How it works

A datasheet is a set of open-ended questions grouped into seven sections that follow the dataset lifecycle:[^s1]

1. **Motivation** — why the dataset was created and who funded it.[^s1]
2. **Composition** — what the instances represent, how many there are, how they were sampled, labels, missing data, and whether sensitive or identifying information is present.[^s1]
3. **Collection process** — how and over what timeframe data were acquired, by whom, and whether the people involved were notified or consented.[^s1]
4. **Preprocessing, cleaning and labeling** — what transformations were applied and whether the raw data and software are available.[^s1]
5. **Uses** — tasks the dataset has been or could be used for, and tasks it should not be used for.[^s1]
6. **Distribution** — how it is shared and under which licence, terms or regulatory restrictions.[^s1]
7. **Maintenance** — who maintains it, how to report errata, and how updates and older versions are handled.[^s1]

The questions are phrased to discourage yes/no answers and are explicitly not a checklist; creators are advised to read them before collecting any data and to answer each section at the matching stage. The authors stress that the process is deliberately manual, because reflection by the creators is part of the point.[^s1] Besides creators and consumers, the intended readers include policymakers, advocates, data subjects and researchers trying to reproduce results.[^s1]

## Evidence, adoption and limitations

According to the final paper version, academic researchers began releasing datasets with datasheets and Microsoft, Google and IBM piloted them internally.[^s1] The framework also spawned derivatives. Google Research's **Data Cards** (Pushkarna et al., 2022) present themselves as a modular, scalable complement to longer frameworks such as datasheets, organised around 31 themes; in their development, 12 Google teams produced 22 cards, and the authors found that producers often copied old cards (spreading errors) and that writing a card after a dataset is finished costs far more than writing it during creation.[^s3] On the Hugging Face Hub, the **dataset card** is a `README.md` with YAML metadata (licence, language, task categories) that the Hub renders and uses for search filters, plus prose on contents, biases and appropriate use.[^s4]

Empirical work shows uneven uptake. A study presented at ICLR 2024 analysed 7,433 non-empty dataset cards from 24,065 Hugging Face dataset repositories (snapshot of March 2023): only 30.9% of repositories had a non-empty card, though those repositories accounted for 95.0% of downloads; and the sections on dataset creation and on considerations for using the data were consistently the least completed.[^s5][^s6]

Gebru et al. themselves list limits: the questions need adapting to each organisation and domain; streaming or continually changing datasets need different treatment; writing datasheets adds overhead and may raise legal or proprietary concerns; creators cannot foresee every use; and datasets assembled from third-party sources limit what can be documented.[^s1] A datasheet improves transparency but does not by itself remove bias or harm.[^s1]

## Connections

Datasheets sit under `kt:ai-governance` as a documentation control. They are the data-side counterpart of `kt:model-cards`, which grew out of the same research community and which the datasheets paper cites as a related effort.[^s1] Their composition and collection questions target the dataset-level causes of `kt:algorithmic-bias-and-fairness` problems, which is why they are recorded as mitigating it, and they are a recurring subject in `kt:fairness-accountability-and-transparency` research.[^s1][^s5] `kt:data-cards` and Hugging Face `kt:dataset-cards` are later formats that adapt the idea for production teams and an open model hub, and the `kt:hugging-face-hub` is the most widely used place where such cards are implemented.[^s3][^s4]

## Sources
[^s1]: Gebru et al., "Datasheets for Datasets", arXiv:1803.09010v5. https://arxiv.org/pdf/1803.09010v5 (accessed 2026-11-16)
[^s2]: Gebru et al., "Datasheets for Datasets", Communications of the ACM 64(12):86–92, 2021 (Microsoft Research page). https://www.microsoft.com/en-us/research/publication/datasheets-for-datasets/ (accessed 2026-11-16)
[^s3]: Pushkarna, Zaldivar, Kjartansson, "Data Cards: Purposeful and Transparent Dataset Documentation for Responsible AI", arXiv:2204.01075. https://arxiv.org/pdf/2204.01075.pdf (accessed 2026-11-16)
[^s4]: Hugging Face, "Dataset Cards", Hub documentation. https://huggingface.co/docs/hub/en/datasets-cards (accessed 2026-11-16)
[^s5]: Yang, Liang, Zou, "Navigating Dataset Documentations in AI", ICLR 2024 poster. https://iclr.cc/virtual/2024/poster/17463 (accessed 2026-11-16)
[^s6]: Yang, Liang, Zou, arXiv:2401.13822v1 full text. https://arxiv.org/html/2401.13822v1 (accessed 2026-11-16)
