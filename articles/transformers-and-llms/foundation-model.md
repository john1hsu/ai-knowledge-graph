---
id: kt:foundation-model
type: Paradigm
title: Foundation model
aliases: [foundation models, base model paradigm]
domain: transformers-and-llms
summary: >-
  A model trained on broad data, generally with self-supervision at scale, that can be adapted to a wide range of
  downstream tasks; the term was coined by Stanford researchers in 2021 and its regulatory counterpart in the EU
  is the "general-purpose AI model".
maturity: established
broader: [kt:deep-learning, kt:transfer-learning]
related: [kt:large-language-model, kt:bert, kt:clip, kt:emergent-abilities, kt:fine-tuning, kt:in-context-learning]
relations:
  - {predicate: introducedIn, object: kt:on-the-opportunities-and-risks-of-foundation-models}
  - {predicate: createdBy, object: kt:stanford-crfm}
  - {predicate: trainedWith, object: kt:self-supervised-learning}
  - {predicate: trainedWith, object: kt:pretraining}
  - {predicate: regulatedBy, object: kt:eu-ai-act}
  - {predicate: dependsOn, object: kt:scaling-laws}
sources:
  - id: s1
    title: "On the Opportunities and Risks of Foundation Models"
    publisher: arXiv:2108.07258 (Bommasani et al., Stanford CRFM)
    url: https://arxiv.org/abs/2108.07258
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "On the Opportunities and Risks of Foundation Models (report page)"
    publisher: Stanford Center for Research on Foundation Models
    url: https://crfm.stanford.edu/report.html
    type: academic
    accessed: 2026-11-18
  - id: s3
    title: "Dual-use foundation model (glossary entry, from NIST SP 800-218A)"
    publisher: NIST Computer Security Resource Center
    url: https://csrc.nist.gov/glossary/term/dual_use_foundation_model
    type: government
    accessed: 2026-11-18
  - id: s4
    title: "AI Act, Article 3: Definitions"
    publisher: European Commission AI Act Service Desk
    url: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-3
    type: government
    accessed: 2026-11-18
  - id: s5
    title: "AI Act, Article 51: Classification of general-purpose AI models as models with systemic risk"
    publisher: European Commission AI Act Service Desk
    url: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-51
    type: government
    accessed: 2026-11-18
  - id: s6
    title: "The Foundation Model Transparency Index (December 2025)"
    publisher: Stanford CRFM / HAI
    url: https://crfm.stanford.edu/fmti/December-2025
    type: academic
    accessed: 2026-11-18
created: 2026-11-18
---

# Foundation model

A **foundation model** is a model trained on broad data, usually through self-supervision at scale, that can then be adapted to many different downstream tasks.[^s2] The term was introduced in August 2021 by a team of more than a hundred researchers led by Rishi Bommasani at Stanford's Center for Research on Foundation Models (CRFM), in the report *On the Opportunities and Risks of Foundation Models*.[^s1] The authors chose the word "foundation" to stress that such models are central yet incomplete: they are intermediate assets meant to be built upon rather than finished products used directly.[^s2] BERT (2019), GPT-3 (2020) and CLIP (2021) were the report's canonical examples.[^s2]

## How it works

The paradigm has two stages. First, a large network is **pretrained** on broad, mostly unlabelled data with a self-supervised objective such as predicting masked or next tokens. Second, the pretrained model is **adapted** — by fine-tuning, by prompting, or by building it into a larger system — for a particular task.[^s2] The report stresses that none of the ingredients is new: deep networks, self-supervised learning and transfer learning had existed for years, and what changed was the scale and scope at which they were combined.[^s2] GPT-3, with 175 billion parameters, illustrated the point by performing many tasks it was never explicitly trained for when given natural-language prompts.[^s2]

Bommasani et al. single out two properties. **Emergence** means that capabilities arise implicitly from scale rather than being designed in, and are therefore hard to predict. **Homogenization** means that a small number of base models increasingly underlie a large number of applications.[^s1] Homogenization gives leverage, since an improvement to the base model benefits every adapted model, but it also means any defect or bias in the base is inherited by everything built on it.[^s1][^s2]

## Risks, critiques and open questions

The original report spans capabilities (language, vision, robotics, reasoning), technical foundations (architecture, data, systems, evaluation, theory), applications such as law, healthcare and education, and societal impacts including inequity, misuse, economic and environmental costs, and legal questions.[^s1] Its central caution is that the field still understands poorly how these models work, when they fail and what they can do, which it argues calls for interdisciplinary research.[^s1]

Transparency is a recurring concern. Stanford's Foundation Model Transparency Index scores developers on 100 indicators; in its December 2025 edition the mean score across 13 companies was 41, down 17 points from 2024, with IBM highest at 95 and xAI and Midjourney lowest at 14.[^s6] The index found training-data acquisition and properties to be the least disclosed areas, and reported that open-weight developers scored higher on average than closed-weight ones, though openness alone did not guarantee a high score.[^s6]

## In law and policy

Regulators have adopted versions of the concept. The EU AI Act defines a **general-purpose AI model** as one, including one trained on large data with self-supervision at scale, that shows significant generality, can competently perform a wide range of distinct tasks and can be integrated into many downstream systems; models used only for research or prototyping before release are excluded.[^s4] A general-purpose AI *system* is an AI system built on such a model.[^s4] Under Article 51, a model is presumed to have high-impact capabilities, and so to carry systemic risk, when its cumulative training compute exceeds 10^25 floating-point operations; the Commission can also designate models below that line.[^s5]

In the United States, NIST's glossary (drawing on SP 800-218A) defines a **dual-use foundation model** as a broadly trained, usually self-supervised model with at least tens of billions of parameters that performs, or could easily be modified to perform, at a level posing serious risks to security, economic security or public health and safety.[^s3] Under that definition, a model still qualifies even if it ships with technical safeguards against misuse.[^s3]

## Connections

Foundation models sit within **deep learning** and are the large-scale form of **transfer learning**: knowledge acquired in **pretraining** through **self-supervised learning** is carried to new tasks.[^s2] **Large language models** are the most prominent type, alongside encoders like **BERT** and image–text models like **CLIP**, the report's own examples.[^s2] **Fine-tuning** and **in-context learning** (prompting) are the main adaptation routes.[^s2] The emphasis on scale connects the paradigm to **scaling laws**, and the report's notion of emergence anticipates later work on **emergent abilities**.[^s1] Its regulatory form is governed by the **EU AI Act** through the general-purpose AI model provisions.[^s4][^s5]

## Sources
[^s1]: Bommasani et al., "On the Opportunities and Risks of Foundation Models", arXiv:2108.07258, 2021 (v3 2022). https://arxiv.org/abs/2108.07258 (accessed 2026-11-18)
[^s2]: Stanford CRFM, "On the Opportunities and Risks of Foundation Models" report page. https://crfm.stanford.edu/report.html (accessed 2026-11-18)
[^s3]: NIST CSRC Glossary, "dual-use foundation model" (source: NIST SP 800-218A). https://csrc.nist.gov/glossary/term/dual_use_foundation_model (accessed 2026-11-18)
[^s4]: European Commission AI Act Service Desk, Article 3: Definitions. https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-3 (accessed 2026-11-18)
[^s5]: European Commission AI Act Service Desk, Article 51. https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-51 (accessed 2026-11-18)
[^s6]: Stanford CRFM/HAI, "The Foundation Model Transparency Index", December 2025 edition. https://crfm.stanford.edu/fmti/December-2025 (accessed 2026-11-18)
