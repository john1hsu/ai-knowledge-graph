---
id: kt:hotpotqa
type: Benchmark
title: HotpotQA
aliases: [Hotpot QA, HotpotQA dataset, hotpot_qa]
domain: evaluation-and-benchmarks
summary: >-
  A multi-hop question answering benchmark of about 113,000 crowd-written, Wikipedia-based questions, introduced at
  EMNLP 2018, in which answering requires combining evidence from two paragraphs and systems are also scored on
  identifying the sentence-level supporting facts behind each answer.
maturity: established
broader: [kt:ai-evaluation, kt:question-answering]
related: [kt:compositional-questions-do-not-necessitate-multi-hop-reasoning, kt:react-prompting, kt:reflexion, kt:retrieval-augmented-generation, kt:information-retrieval, kt:benchmark-contamination]
relations:
  - {predicate: introducedIn, object: kt:hotpotqa-a-dataset-for-diverse-explainable-multi-hop-question-answering}
  - {predicate: basedOn, object: kt:tf-idf}
  - {predicate: studiedIn, object: kt:natural-language-processing}
sources:
  - id: s1
    title: "HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering"
    publisher: Yang, Qi, Zhang, Bengio, Cohen, Salakhutdinov and Manning (CMU, Stanford, Mila, Google AI), arXiv 1809.09600
    url: https://arxiv.org/pdf/1809.09600
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering (anthology record)"
    publisher: EMNLP 2018, pp. 2369-2380, Association for Computational Linguistics, DOI 10.18653/v1/D18-1259
    url: https://aclanthology.org/D18-1259/
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "Compositional Questions Do Not Necessitate Multi-hop Reasoning"
    publisher: ACL 2019, pp. 4249-4257 (Min, Wallace, Singh, Gardner, Hajishirzi and Zettlemoyer), DOI 10.18653/v1/P19-1416
    url: https://aclanthology.org/P19-1416/
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    publisher: ICLR 2023 (Yao, Zhao, Yu, Du, Shafran, Narasimhan and Cao)
    url: https://iclr.cc/virtual/2023/poster/11003
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s5
    title: "hotpot_qa dataset card"
    publisher: Hugging Face Datasets
    url: https://huggingface.co/datasets/hotpot_qa?row=16
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# HotpotQA

**HotpotQA** is a question answering benchmark built so that a correct answer usually depends on linking facts found in two different Wikipedia paragraphs, a setup known as *multi-hop* question answering. It was introduced at EMNLP 2018 by Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William W. Cohen, Ruslan Salakhutdinov and Christopher D. Manning, a team spanning Carnegie Mellon University, Stanford, Mila and Google AI.[^s1][^s2] The authors framed it as a response to earlier reading-comprehension datasets, which they argued did not push systems toward complex reasoning or toward explaining their answers.[^s2]

## Design

The paper names four defining properties: questions need evidence from several supporting documents; they are written freely rather than generated from a fixed knowledge-base schema; every answer comes with sentence-level **supporting facts**; and a new class of **comparison questions** asks systems to contrast two entities, including yes/no variants.[^s1][^s2] The released dataset holds 112,779 valid examples.[^s1]

To collect it, the authors built a directed graph of hyperlinks among the first paragraphs of English Wikipedia articles and showed crowdworkers on Amazon Mechanical Turk pairs of linked paragraphs. A *bridge* question hinges on an entity that connects the two paragraphs; comparison questions were drawn from 42 curated lists of similar entities. Workers also marked which sentences were needed to reach the answer.[^s1] In a sample the authors analysed, bridge-entity chains made up about 42% of questions and comparisons about 27%, with the rest split among property-intersection and other patterns.[^s1]

Training data was divided by difficulty into train-easy (18,089), train-medium (56,814) and train-hard (15,661) examples, with dev, distractor-test and fullwiki-test sets of 7,405 each; the authors found that training on all three tiers worked best.[^s1] The public Hugging Face release exposes the same material as `distractor` and `fullwiki` configurations with 90,447 training and 7,405 validation examples, per-example `type` and `level` fields, and a CC BY-SA 4.0 licence.[^s5]

## Settings and metrics

HotpotQA is evaluated in two settings. In the **distractor** setting, each question comes with ten paragraphs: the two gold paragraphs plus eight distractors retrieved by bigram tf-idf. In the harder **fullwiki** setting, systems must find the evidence themselves among more than five million Wikipedia paragraphs.[^s1] Answers are scored with exact match (EM) and F1, supporting facts are scored the same way, and **joint** EM/F1 combine the two so that a system is rewarded only when it is right and can point to why.[^s1]

The 2018 baseline, trained with supporting-fact supervision, reached about 59 answer F1 in the distractor setting but only about 34 in fullwiki, with joint F1 of roughly 41 and 18 respectively; human annotators reached about 91 answer F1 and 83 joint F1 on a 1,000-question sample.[^s1] That gap, largest in the open-retrieval setting, is what made the benchmark a long-running target.

## Critiques

The most cited critique came from Min and colleagues at ACL 2019, who showed that many questions that look multi-hop can be answered from a single paragraph, because the question singles out a particular entity type or the evidence is redundant. Their single-hop BERT-based reader scored 67 F1, which they reported as comparable to multi-hop models of the time, and humans who were deliberately shown incomplete evidence still answered over 80% of questions correctly.[^s3] They argued that future benchmarks should pay more attention to evidence and move toward retrieval over larger, more varied collections.[^s3] The lesson generalises: a high HotpotQA score shows a system can answer these questions, not necessarily that it chains reasoning steps.

Because the questions are built from Wikipedia text and the dataset is openly redistributed under a permissive licence, scores from models pretrained on web text should also be read with benchmark contamination in mind.[^s1][^s5]

## Use in LLM and agent research

HotpotQA moved from reading-comprehension leaderboards into large-language-model research as a test of reasoning combined with retrieval. ReAct (ICLR 2023) used it, alongside the FEVER fact-verification task, to show a model interleaving reasoning traces with calls to a simple Wikipedia API; the authors report that this reduced the hallucination and error propagation seen with chain-of-thought alone.[^s4] Because a ReAct-style agent must decide what to look up, read the result and decide again, the benchmark now sits at the junction of question answering, retrieval and agent evaluation.[^s4][^s1]

## Connections

- **Broader:** HotpotQA is a dataset for **AI evaluation** within the wider task of question answering, specifically the multi-hop variety it helped define.[^s1]
- **Built with:** its distractor paragraphs come from bigram **tf-idf** retrieval, and the fullwiki setting turns it into an **information retrieval** problem.[^s1]
- **Used to evaluate:** **ReAct** reports results on it with a Wikipedia search tool, and the graph's **Reflexion** node also lists it as an evaluation target; its fullwiki setting is a natural test bed for **retrieval-augmented generation**, where a system must find and then combine evidence.[^s4][^s1]
- **Critiqued by:** *Compositional Questions Do Not Necessitate Multi-hop Reasoning* (ACL 2019), which quantified single-hop shortcuts in the data.[^s3]
- **Caveat:** results for web-pretrained models are subject to **benchmark contamination**.[^s5]

## Sources
[^s1]: Yang et al., "HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering", arXiv 1809.09600. https://arxiv.org/pdf/1809.09600 (accessed 2026-11-18)
[^s2]: Yang et al., EMNLP 2018 anthology record, DOI 10.18653/v1/D18-1259. https://aclanthology.org/D18-1259/ (accessed 2026-11-18)
[^s3]: Min et al., "Compositional Questions Do Not Necessitate Multi-hop Reasoning", ACL 2019. https://aclanthology.org/P19-1416/ (accessed 2026-11-18)
[^s4]: Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", ICLR 2023. https://iclr.cc/virtual/2023/poster/11003 (accessed 2026-11-18)
[^s5]: Hugging Face, "hotpot_qa" dataset card. https://huggingface.co/datasets/hotpot_qa?row=16 (accessed 2026-11-18)
