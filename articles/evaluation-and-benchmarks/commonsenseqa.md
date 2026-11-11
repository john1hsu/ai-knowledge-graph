---
id: kt:commonsenseqa
type: Benchmark
title: CommonsenseQA
aliases: [CSQA, Commonsense QA, CommonsenseQA 1.0]
domain: evaluation-and-benchmarks
summary: >-
  A five-way multiple-choice question answering benchmark of 12,247 crowd-written questions built from
  ConceptNet relations, introduced at NAACL 2019 to test whether models can answer questions that require
  everyday commonsense knowledge rather than facts stated in a given passage.
maturity: established
broader: [kt:ai-evaluation, kt:commonsense-reasoning]
related: [kt:chain-of-thought, kt:star-self-taught-reasoner, kt:gsm8k, kt:benchmark-contamination, kt:large-language-model]
relations:
  - {predicate: introducedIn, object: kt:commonsenseqa-a-question-answering-challenge-targeting-commonsense-knowledge}
  - {predicate: createdBy, object: kt:allen-institute-for-ai}
  - {predicate: basedOn, object: kt:conceptnet}
  - {predicate: followedBy, object: kt:commonsenseqa-2-0}
sources:
  - id: s1
    title: "CommonsenseQA: A Question Answering Challenge Targeting Commonsense Knowledge"
    publisher: NAACL-HLT 2019, pp. 4149-4158 (Talmor, Herzig, Lourie and Berant; Tel Aviv University and Allen Institute for AI), ACL Anthology N19-1421
    url: https://aclanthology.org/N19-1421.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "CommonsenseQA: A Question Answering Challenge Targeting Commonsense Knowledge (anthology record)"
    publisher: Association for Computational Linguistics, DOI 10.18653/v1/N19-1421
    url: https://aclanthology.org/N19-1421/
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "tau/commonsense_qa dataset card"
    publisher: Hugging Face Datasets
    url: https://huggingface.co/datasets/tau/commonsense_qa/blob/refs%2Fpr%2F2/README.md
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    publisher: Wei, Wang, Schuurmans, Bosma, Ichter, Xia, Chi, Le and Zhou (Google Research), arXiv 2201.11903
    url: https://arxiv.org/pdf/2201.11903
    type: primary
    accessed: 2026-11-11
  - id: s5
    title: "CommonsenseQA 2.0: Exposing the Limits of AI through Gamification"
    publisher: NeurIPS 2021 Datasets and Benchmarks Track (Talmor, Yoran, Le Bras, Bhagavatula, Goldberg, Choi and Berant)
    url: https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/3ef815416f775098fe977004015c6193-Abstract-round1.html
    type: peer-reviewed
    accessed: 2026-11-11
created: 2026-11-11
---

# CommonsenseQA

**CommonsenseQA** (often abbreviated **CSQA**) is a multiple-choice question answering benchmark designed to measure whether a model can draw on background commonsense knowledge, the kind of everyday understanding people rarely state explicitly. It was introduced by Alon Talmor, Jonathan Herzig, Nicholas Lourie and Jonathan Berant of Tel Aviv University and the Allen Institute for AI in a paper at NAACL-HLT 2019.[^s1][^s2] Unlike reading-comprehension datasets, its questions come with no supporting passage: the answer has to be inferred from what the model already knows about the world.[^s1]

## How it was built

The dataset is grounded in **ConceptNet**, a large graph of commonsense relations between concepts. The authors started from about 32 million ConceptNet triplets and filtered them to 236,208 triplets over 22 relations, discarding overly general relations, non-English concepts and concepts longer than four words.[^s1] They then grouped triplets that share a source concept and relation into sets of three target concepts, yielding roughly 43,000 sets.[^s1]

Crowdworkers on Amazon Mechanical Turk received one such set and wrote three questions, each with a different target concept as its answer. Because all three targets relate to the same source concept in the same way, the other targets serve as hard distractors that a shallow association with the source concept cannot rule out. Each question also gained one extra distractor drawn from ConceptNet and one written by the worker, for five answer choices in total.[^s1] Two further workers verified every question, and questions that neither answered correctly were dropped, which removed about 15%: of 16,242 questions written, 12,247 were kept, at a cost of about $0.33 per question.[^s1]

The released data follows an 80/10/10 split. In the Hugging Face release, each example carries the question text, the ConceptNet `question_concept`, five labelled choices (A to E) and an `answerKey`, with 9,741 training, 1,221 validation and 1,140 test examples; the card lists an MIT licence.[^s3] The authors also provided a second "question concept" split in which concepts do not overlap between train and test.[^s1]

## What the questions test

In an analysis of 100 development questions, the authors found an average of 1.75 commonsense skills per question. Spatial knowledge was the most common (41%), followed by cause and effect and part-whole knowledge (23% each), purpose (18%), category membership (17%) and social conventions (15%).[^s1] The ConceptNet relation behind the questions was dominated by *AtLocation* (47.3%), with *Causes* (17.3%) and *CapableOf* (9.4%) next.[^s1]

## Results and evidence

At release the benchmark was hard for state-of-the-art models. On the main random split, BERT-large reached 55.9% test accuracy and the original GPT 45.5%, against 20% chance and 88.9% for humans, measured by a majority vote of five workers on 100 sampled questions.[^s1] A "sanity" variant that replaced the hard distractors with random ones let BERT-large score above 92%, showing that the difficulty came mainly from the carefully chosen distractors.[^s1] Error analysis found BERT did well when surface cues gave the answer away (77.7%) but poorly on negation (42.8%) and on questions requiring a conjunction of conditions (23.8%).[^s1]

The benchmark then became a standard commonsense test for large language models. In the 2022 chain-of-thought paper from Google Research, PaLM 540B scored 78.1% on CSQA with standard few-shot prompting and 79.9% with chain-of-thought prompting; the authors characterised the gain on CSQA as minimal, and reported that chain-of-thought did not help GPT-3 on this task.[^s4]

## Limitations and critiques

The original authors noted that more than 85% of questions came from 10 of the 122 question writers and that the human-performance estimate rested on only 100 questions.[^s1] More broadly, members of the same team argued in 2021 that pretrained models reach human-level scores by exploiting dataset artifacts while still failing adversarial, commonsense-probing examples. Their successor, **CommonsenseQA 2.0**, gathered 14,343 yes/no questions through a game in which players tried to fool an AI; the best baseline (an 11-billion-parameter T5-based model) reached 70.2%, few-shot GPT-3 52.9%, and humans 94.1%.[^s5] Because the test set is small and the data has circulated publicly since 2019, high scores on CSQA say little on their own about a model's commonsense abilities.[^s3][^s5]

## Connections

CommonsenseQA is a benchmark within **AI evaluation** that targets **commonsense reasoning**.[^s1] It is **introduced in** the NAACL 2019 paper by Talmor and colleagues, **created by** a team including the **Allen Institute for AI**, and **based on** the **ConceptNet** knowledge graph.[^s1][^s2] It was **followed by** **CommonsenseQA 2.0**, built to resist the artifact exploitation that inflated scores on the original.[^s5] It appears alongside **GSM8K** in the evaluation of **chain-of-thought** prompting with **large language models**,[^s4] and **STaR (self-taught reasoner)** was evaluated on it. Its public, long-circulated data makes it a natural concern for **benchmark contamination**.[^s3]

## Sources

[^s1]: Talmor, Herzig, Lourie and Berant, "CommonsenseQA: A Question Answering Challenge Targeting Commonsense Knowledge", NAACL-HLT 2019, pp. 4149-4158. https://aclanthology.org/N19-1421.pdf (accessed 2026-11-11)
[^s2]: ACL Anthology record N19-1421, DOI 10.18653/v1/N19-1421. https://aclanthology.org/N19-1421/ (accessed 2026-11-11)
[^s3]: Hugging Face Datasets, "tau/commonsense_qa" dataset card. https://huggingface.co/datasets/tau/commonsense_qa/blob/refs%2Fpr%2F2/README.md (accessed 2026-11-11)
[^s4]: Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", arXiv 2201.11903. https://arxiv.org/pdf/2201.11903 (accessed 2026-11-11)
[^s5]: Talmor, Yoran, Le Bras, Bhagavatula, Goldberg, Choi and Berant, "CommonsenseQA 2.0: Exposing the Limits of AI through Gamification", NeurIPS 2021 Datasets and Benchmarks Track. https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/3ef815416f775098fe977004015c6193-Abstract-round1.html (accessed 2026-11-11)
