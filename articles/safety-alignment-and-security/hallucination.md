---
id: kt:hallucination
type: Risk
title: Hallucination
aliases: [AI hallucination, LLM hallucination, confabulation, model hallucination]
domain: safety-alignment-and-security
summary: >-
  The generation by a language model or other generative AI system of fluent, confident content that is false,
  unsupported by its input, or nonsensical, such as invented facts, citations or quotations.
maturity: established
broader: [kt:ai-safety]
related: [kt:large-language-model, kt:pretraining, kt:sampling-temperature-and-top-p, kt:retrieval-augmented-generation]
relations:
  - {predicate: contrastsWith, object: kt:sycophancy}
  - {predicate: evaluatedOn, object: kt:truthfulqa}
  - {predicate: regulatedBy, object: kt:nist-ai-risk-management-framework}
sources:
  - id: s1
    title: "Survey of Hallucination in Natural Language Generation"
    publisher: ACM Computing Surveys (Ji, Lee, Frieske, Yu, Su, Xu, Ishii, Bang, Madotto, Fung et al.), DOI 10.1145/3571730; arXiv:2202.03629
    url: https://arxiv.org/pdf/2202.03629v5
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Why Language Models Hallucinate"
    publisher: arXiv:2509.04664 (Kalai, Nachum, Vempala, Zhang), September 2025
    url: https://arxiv.org/html/2509.04664v1
    type: primary
    accessed: 2026-11-12
  - id: s3
    title: "Why language models hallucinate"
    publisher: OpenAI, 5 September 2025
    url: https://openai.com/index/why-language-models-hallucinate/
    type: lab-research
    accessed: 2026-11-12
  - id: s4
    title: "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)"
    publisher: National Institute of Standards and Technology, July 2024
    url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
    type: government
    accessed: 2026-11-12
  - id: s5
    title: "Detecting hallucinations in large language models using semantic entropy"
    publisher: Nature, 2024 (Farquhar, Kossen, Kuhn, Gal), OATML Oxford publication page
    url: https://oatml.cs.ox.ac.uk/publications/202406_FarquharKossenKuhn_HallucinatingLLMs.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s6
    title: "Detecting hallucinations in large language models using semantic entropy (explainer)"
    publisher: OATML, University of Oxford, 19 June 2024
    url: https://oatml.cs.ox.ac.uk/blog/2024/06/19/detecting_hallucinations_2024.html
    type: academic
    accessed: 2026-11-12
created: 2026-11-12
---

# Hallucination

In AI, **hallucination** is when a generative model produces fluent, confident output that is false, unsupported by its input, or nonsensical. Examples include an invented citation or a summary that contradicts its document. In their survey of natural language generation, Ji and colleagues define it as generated content that is nonsensical or unfaithful to the source content.[^s1] OpenAI's 2025 framing is similar: plausible statements that are nonetheless false.[^s3] NIST's Generative AI Profile prefers the term **confabulation**. It describes systems that confidently present erroneous or false content, and notes that some commenters find "hallucination" anthropomorphising.[^s4]

## Origin of the term and taxonomy

The word came into machine learning from computer vision. There it first had a positive sense, as in "hallucinating" detail for image super-resolution. Later vision work used it negatively for captions or detections of objects that are not in the image, and natural language generation adopted that negative sense.[^s1] Ji et al.'s survey (ACM Computing Surveys) set out the taxonomy most papers still use:[^s1]

- **Intrinsic hallucination:** the output contradicts the source, such as a summary giving the wrong year for an event the article dates.[^s1]
- **Extrinsic hallucination:** the output can be neither supported nor refuted by the source. It may happen to be true, but it cannot be verified from the input.[^s1]

Open-ended chatbots often have no source document, so the test becomes factuality against world knowledge, as NIST and OpenAI frame it.[^s3][^s4] NIST's definition also counts outputs that contradict earlier statements in the same conversation.[^s4]

## Why models hallucinate

The survey traces causes to both data and modelling.[^s1] On the data side, training pairs often diverge: a reference text contains facts absent from its source, so the model learns to add unsupported content. On the modelling side it lists weak input representations, decoders that attend to the wrong part of the input, and **exposure bias**. A model trained on gold prefixes but generating from its own outputs compounds its errors over long texts. Diversity-promoting decoding such as top-k sampling is associated with more hallucination. Models may also prefer knowledge memorised in pretraining over what the input says.[^s1]

A 2025 paper by Kalai, Nachum, Vempala and Zhang gives a statistical account for pretrained language models.[^s2] It reduces generation to a binary "Is-It-Valid" classification problem. Roughly, a base model's rate of generating errors is at least about twice its rate of misclassifying valid versus invalid strings. Errors are therefore expected wherever facts cannot be told apart from plausible falsehoods.[^s2] For arbitrary facts such as birthdays, the authors tie this to the **singleton rate**, the share of facts seen only once in training. If 20% of birthday facts appear exactly once, a base model should hallucinate on at least about 20% of them.[^s2]

The same authors argue that hallucinations persist after post-training because benchmarks grade like multiple-choice tests with no penalty for guessing.[^s2][^s3] An "I don't know" scores zero while a guess sometimes scores, so models are rewarded for confident guessing. OpenAI illustrated this with SimpleQA figures from its GPT-5 system card (2025). gpt-5-thinking-mini abstained on 52% of questions, got 22% right and 26% wrong; o4-mini abstained on 1%, got 24% right and 75% wrong.[^s3] These are OpenAI's figures for its own models.

## Detection, mitigation and open problems

Mitigations fall into data methods, such as cleaner and more faithful training sets or adding external evidence to the input, and modelling and inference methods, such as architectural changes, training objectives and post-editing of outputs.[^s1] Supplying retrieved evidence alongside the prompt, as in retrieval-augmented generation, belongs to the first group.[^s1] Kalai et al. and OpenAI propose an incentive fix: penalise confident errors more than abstentions and give credit for appropriate uncertainty in mainstream benchmarks, rather than adding a few separate hallucination tests.[^s2][^s3]

Detection at run time is an active research area. Farquhar and colleagues (Nature, 2024) proposed **semantic entropy** for a subset of hallucinations they call confabulations: arbitrary, incorrect answers that change when the question is re-asked.[^s5] The method samples several answers, often about five, groups them by meaning using an entailment model or an LLM, and computes entropy over the meaning groups. High entropy flags a likely confabulation.[^s6] The authors note it costs roughly ten times a single query. It cannot catch errors a model makes consistently, such as facts it learned wrongly, or deliberate deception.[^s6]

The stakes are practical. NIST lists confabulation among the main risks of generative AI. Its examples include a confabulated summary of patient records leading doctors to a wrong diagnosis, and it notes that legal confabulations are pervasive in state-of-the-art LLMs.[^s4] NIST's suggested actions include verifying sources and citations in outputs before deployment and during monitoring.[^s4]

## Connections

Hallucination is a core reliability risk studied under **AI safety** (`broader`).[^s4] It is most discussed for the **large language model** and arises from the statistics of next-token **pretraining**, per Kalai et al.[^s2][^s4] Decoding choices covered under **sampling: temperature and top-p** affect it, since more random sampling is linked to more hallucination.[^s1] **Retrieval-augmented generation** grounds outputs in retrieved evidence to reduce it.[^s1] It is often confused with **sycophancy** (`contrastsWith`): a hallucinating model invents content it has no basis for, while a sycophantic model may know the right answer and defer to the user. Benchmarks such as **TruthfulQA** measure one form of it (`evaluatedOn`). The **NIST AI Risk Management Framework** covers it through the confabulation risk in its Generative AI Profile (`regulatedBy`).[^s4]

## Sources
[^s1]: Ji et al., "Survey of Hallucination in Natural Language Generation", ACM Computing Surveys, DOI 10.1145/3571730; arXiv:2202.03629v5. https://arxiv.org/pdf/2202.03629v5 (accessed 2026-11-12)
[^s2]: Kalai, Nachum, Vempala and Zhang, "Why Language Models Hallucinate", arXiv:2509.04664, September 2025. https://arxiv.org/html/2509.04664v1 (accessed 2026-11-12)
[^s3]: OpenAI, "Why language models hallucinate", 5 September 2025. https://openai.com/index/why-language-models-hallucinate/ (accessed 2026-11-12)
[^s4]: NIST, "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile" (NIST AI 600-1), July 2024. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf (accessed 2026-11-12)
[^s5]: Farquhar, Kossen, Kuhn and Gal, "Detecting hallucinations in large language models using semantic entropy", Nature, 2024. https://oatml.cs.ox.ac.uk/publications/202406_FarquharKossenKuhn_HallucinatingLLMs.html (accessed 2026-11-12)
[^s6]: OATML (University of Oxford), "Detecting hallucinations in large language models using semantic entropy", 19 June 2024. https://oatml.cs.ox.ac.uk/blog/2024/06/19/detecting_hallucinations_2024.html (accessed 2026-11-12)
