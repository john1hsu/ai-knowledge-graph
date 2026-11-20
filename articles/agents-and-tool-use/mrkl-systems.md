---
id: kt:mrkl-systems
type: Architecture
title: MRKL systems
aliases: [MRKL, Modular Reasoning Knowledge and Language, MRKL architecture, Jurassic-X]
domain: agents-and-tool-use
summary: >-
  A modular neuro-symbolic architecture proposed by AI21 Labs in 2022 (pronounced "miracle") in which a router
  sends each natural-language input to the most suitable expert module, either a neural model or a discrete
  tool such as a calculator, API or database, with a general-purpose language model as the fallback.
maturity: historical
broader: [kt:neuro-symbolic-ai, kt:ai-agent]
related: [kt:tool-use, kt:toolformer, kt:react-prompting, kt:retrieval-augmented-generation, kt:catastrophic-forgetting]
relations:
  - {predicate: createdBy, object: kt:ai21-labs}
  - {predicate: basedOn, object: kt:jurassic-1}
  - {predicate: trainedWith, object: kt:prompt-tuning}
  - {predicate: mitigates, object: kt:hallucination}
  - {predicate: influencedBy, object: kt:symbolic-ai}
sources:
  - id: s1
    title: "MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning"
    publisher: arXiv 2205.00445 (Karpas et al., AI21 Labs; authors' version)
    url: https://arxiv.org/pdf/2205.00445
    type: primary
    accessed: 2026-11-20
  - id: s2
    title: "MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning"
    publisher: AI21 Labs research page
    url: https://ai21.com/research/mrkl-systems-a-modular-neuro-symbolic-architecture-that-combines-large-language-models-external-knowledge-sources-and-discrete-reasoning
    type: lab-research
    accessed: 2026-11-20
  - id: s3
    title: "Neural Nets + Rules = Truer Text: Jurassic-X can answer questions, check facts, solve math, and more"
    publisher: DeepLearning.AI, The Batch (April 20, 2022)
    url: https://www.deeplearning.ai/the-batch/neural-nets-rules-truer-text
    type: news
    accessed: 2026-11-20
  - id: s4
    title: "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques"
    publisher: arXiv 2406.06608v6 (Schulhoff et al., 2025)
    url: https://arxiv.org/pdf/2406.06608
    type: preprint
    accessed: 2026-11-20
created: 2026-11-20
---

# MRKL systems

A **MRKL system** (Modular Reasoning, Knowledge and Language, pronounced "miracle") is an architecture in which a large language model is one component among many rather than the whole system. An extendable set of "experts" sits behind a router; the router reads each natural-language input and hands it to the module best placed to deal with it, and that module's output either becomes the answer or is passed on to another module.[^s1][^s2] Experts may be neural, such as the big general-purpose model or smaller specialised ones, or symbolic, such as a calculator, a currency converter or a call to a database API.[^s1] AI21 Labs introduced the design in a May 2022 white paper by 17 of its researchers, including Ehud Karpas, Yoav Shoham, Kevin Leyton-Brown and Amnon Shashua, together with Jurassic-X, its own implementation.[^s1][^s2]

## Motivation

The paper framed language models as a textual gateway to knowledge and reasoning that, used alone, has four structural gaps. They cannot see information that changes after training (exchange rates, stock prices, today's date); they cannot see private data such as a company's customer records; they reason unreliably, with GPT-3 and Jurassic-1 handling two-digit addition but producing nonsense on four-digit sums; and fine-tuning one model per task leads to a "model explosion" that is costly to serve, while retraining a single multi-task model for every new task risks catastrophic forgetting.[^s1] The authors argued that scaling alone would not deliver the robustness of a pocket calculator, so discrete modules should do what they are good at.[^s1]

## How it works

The paper lists six advantages of routing to experts: a safe fallback to the general model when no expert fits; extensibility, because experts are built independently and only the comparatively light router must be retrained when one is added; interpretability, since an answer can be traced to the module that produced it; access to current information through external APIs; access to proprietary knowledge in private databases; and compositionality, by sending the parts of a multi-step question to different experts.[^s1]

Contemporary coverage of Jurassic-X gave more detail on the implementation. The router was itself a trained transformer, paired with a prompt generator that rephrased an input into a form suited to the chosen module. For open-domain questions, a passage retriever and reranker selected Wikipedia text that was supplied to Jurassic-1 with the question.[^s3] The system was described as being piloted with a few partners, with developer early access planned.[^s1]

The central technical problem the paper studies is crossing the "neuro-symbolic chasm": a symbolic module needs exact arguments, so the neural side must extract them from loosely worded text, where "twelve", "12" and "a dozen" mean the same thing.[^s1] In its arithmetic experiments, a 7-billion-parameter Jurassic-1 model was prompt-tuned (10 soft-prompt tokens) only to pull out operands and operators, and an actual calculator computed the result. Trained on one-digit problems, it kept essentially perfect accuracy on addition up to nine digits, whereas GPT-3's few-shot addition accuracy cited in the paper fell to about 25% at four digits.[^s1] Training on numbers written as words transferred to digits (about 99% accuracy) but not the other way round (about 16%), and some operation pairs generalised poorly; for example, a model trained on single operations scored about 1% on unseen addition-then-multiplication problems.[^s1] In an appendix comparison, prompt tuning was much more robust than few-shot prompting to numbers written as words and to unfamiliar phrasings.[^s1]

## Limitations and legacy

The evidence in the paper is narrow: it reports detailed results only for arithmetic, and leaves routing and model explosion to separate work.[^s1] Accuracy depends on the router choosing the right expert and extracting the right arguments, and the authors accept that this extraction step is not free; they describe the price as often affordable.[^s1] Jurassic-X itself was a proprietary product whose results were reported by its developer and the press rather than through independent benchmarks.[^s3]

MRKL's lasting influence is conceptual. The Prompt Report (2025) treats it as one of the simplest formulations of an LLM agent, a router with access to several tools that may call them repeatedly before composing a final answer, and lists Toolformer and Gorilla among later techniques that pursue similar goals, mostly with fine-tuning.[^s4] The same survey notes that tools are sometimes called experts or modules, terminology it traces to the MRKL paper.[^s4]

## Connections

MRKL is an instance of **neuro-symbolic AI**, combining learned models with discrete reasoning, and an early design for the **AI agent**; its symbolic experts reflect the older **symbolic AI** tradition it explicitly draws on.[^s1] It was **created by** **AI21 Labs** and **based on** the **Jurassic-1** model, whose argument extraction was trained with **prompt tuning**.[^s1] By grounding answers in tools and retrieved text, it aims to **mitigate** **hallucination**, and its Wikipedia pipeline anticipates **retrieval-augmented generation**.[^s1][^s3] Its modular design responds to **catastrophic forgetting** in multi-task models.[^s1] Later approaches to the same problem include **Toolformer**, in which the model learns when to call tools, and **ReAct**-style prompting; modern **tool use** (function calling) APIs carry forward the idea of a model handing structured calls to external programs.[^s4]

## Sources

[^s1]: Karpas et al., "MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning", AI21 Labs, arXiv 2205.00445, 2022. https://arxiv.org/pdf/2205.00445 (accessed 2026-11-20)
[^s2]: AI21 Labs, "MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning", research page. https://ai21.com/research/mrkl-systems-a-modular-neuro-symbolic-architecture-that-combines-large-language-models-external-knowledge-sources-and-discrete-reasoning (accessed 2026-11-20)
[^s3]: DeepLearning.AI, "Neural Nets + Rules = Truer Text", The Batch, April 20, 2022. https://www.deeplearning.ai/the-batch/neural-nets-rules-truer-text (accessed 2026-11-20)
[^s4]: Schulhoff et al., "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques", arXiv 2406.06608v6, 2025. https://arxiv.org/pdf/2406.06608 (accessed 2026-11-20)
