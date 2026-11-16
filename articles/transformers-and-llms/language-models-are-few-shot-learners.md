---
id: kt:language-models-are-few-shot-learners
type: Work
title: Language Models are Few-Shot Learners
aliases: [Brown et al. 2020, the GPT-3 paper]
domain: transformers-and-llms
summary: >-
  The 2020 NeurIPS paper by Brown and 30 OpenAI colleagues that introduced GPT-3, a 175-billion-parameter
  autoregressive Transformer, and showed that a large enough language model can perform many tasks from a
  text prompt and a handful of examples, with no gradient updates or fine-tuning.
maturity: foundational
broader: [kt:large-language-model, kt:pretraining]
related: [kt:in-context-learning, kt:few-shot-prompting, kt:zero-shot-prompting, kt:scaling-laws, kt:benchmark-contamination, kt:attention-is-all-you-need]
relations:
  - {predicate: createdBy, object: kt:openai}
  - {predicate: basedOn, object: kt:transformer-architecture}
  - {predicate: influencedBy, object: kt:sparse-transformer}
  - {predicate: enables, object: kt:in-context-learning}
  - {predicate: evaluatedOn, object: kt:triviaqa}
sources:
  - id: s1
    title: "Language Models are Few-Shot Learners"
    publisher: Brown et al., Advances in Neural Information Processing Systems 33 (NeurIPS 2020), pp. 1877–1901, proceedings abstract page
    url: https://papers.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Language Models are Few-Shot Learners (arXiv 2005.14165, v4)"
    publisher: Brown et al., OpenAI, authors' arXiv version (v1 28 May 2020; v4 22 July 2020)
    url: https://arxiv.org/pdf/2005.14165
    type: primary
    accessed: 2026-11-16
  - id: s3
    title: "Dive into Deep Learning, 11.9: Large-Scale Pretraining with Transformers"
    publisher: Zhang, Lipton, Li and Smola, d2l.ai
    url: https://d2l.ai/chapter_attention-mechanisms-and-transformers/large-pretraining-transformers.html
    type: textbook
    accessed: 2026-11-16
  - id: s4
    title: "CS324 Large Language Models: Capabilities"
    publisher: Stanford University, CS324 lecture notes (Winter 2022)
    url: https://stanford-cs324.github.io/winter2022/lectures/capabilities
    type: academic
    accessed: 2026-11-16
  - id: s5
    title: "OpenAI API"
    publisher: OpenAI blog, 11 June 2020 (updated 18 September 2020)
    url: https://openai.com/index/openai-api/
    type: lab-research
    accessed: 2026-11-16
created: 2026-11-16
---

# Language Models are Few-Shot Learners

*Language Models are Few-Shot Learners* is the paper that introduced **GPT-3**. Its 31 authors, led by Tom Brown and including Jared Kaplan, Alec Radford, Ilya Sutskever and Dario Amodei, published it in *Advances in Neural Information Processing Systems 33* (NeurIPS 2020).[^s1] The central claim is that scaling up a language model greatly improves task-agnostic few-shot performance, sometimes to the point of rivalling prior fine-tuned state-of-the-art systems.[^s1] The first arXiv version appeared on 28 May 2020 and the fourth and final revision on 22 July 2020; it runs to 40 pages plus 32 pages of appendices.[^s2]

## Background and motivation

By 2020 the standard recipe in NLP was to pretrain a Transformer and then fine-tune it on thousands of labelled task examples. The authors argued that this need for task-specific datasets was a practical burden and contrasted it with people, who can usually pick up a new language task from a short instruction or a few examples.[^s2] GPT-2 had already shown that a 1.5-billion-parameter decoder-only model could do some tasks without parameter updates; GPT-3 kept that design and made it roughly two orders of magnitude larger.[^s3]

## What the paper did

GPT-3 reuses GPT-2's architecture, including pre-normalization, modified initialization and reversible tokenization, with one change: layers alternate between dense and locally banded sparse attention, in the style of the Sparse Transformer.[^s2] The authors trained eight models, from 125 million to 175 billion parameters, all with a 2,048-token context window and all on 300 billion tokens.[^s2] The largest has 96 layers, a model width of 12,288 and 96 attention heads.[^s2] Its training mix weighted filtered Common Crawl at 60%, WebText2 at 22%, two book corpora at 8% each and English Wikipedia at 3%, deliberately sampling the smaller, higher-quality sets more often than their size alone would dictate.[^s2] Appendix D puts training compute for the 175B model at about 3.64 × 10³ petaflop/s-days, or 3.14 × 10²³ floating-point operations.[^s2]

The paper's key methodological move was to evaluate the model purely through its prompt. It defines three settings: **zero-shot** (a natural-language instruction only), **one-shot** (an instruction plus one demonstration) and **few-shot** (typically 10 to 100 demonstrations, as many as fit in the context window), with no weight updates in any of them.[^s2] The authors call this ability to adapt from the context *in-context learning*, and textbooks now use the same zero/one/few-shot vocabulary.[^s3]

## Results

Results were strong but uneven. Stanford's CS324 notes summarise the paper's figures: few-shot GPT-3 reached 71.2% on TriviaQA, above a retrieval-augmented baseline at 68.0%, and 40.6 BLEU on German-to-English translation without supervised translation data, but it trailed fine-tuned systems on HellaSwag and retrieval-based systems on Natural Questions.[^s4] The paper itself reports competence on on-the-fly tasks such as word unscrambling and three-digit arithmetic, and found that human raters identified its roughly 200-word generated news articles only about 52% of the time, near chance.[^s2] Across tasks, few-shot accuracy rose with model size and grew fastest for the largest models, a pattern d2l links to the power-law scaling of loss with compute.[^s3]

## Limitations and critiques

The authors listed weaknesses candidly: long generations could repeat, lose coherence or contradict themselves; one- and few-shot performance was near chance on comparison tasks such as WiC and ANLI; and a left-to-right model may be disadvantaged where bidirectional context helps.[^s2] They also noted that it was unclear whether few-shot prompting teaches genuinely new tasks or merely helps the model recognise tasks it absorbed in training.[^s2] A filtering bug left some benchmark test data in the training set; retraining was too expensive, so the authors measured performance on "clean" subsets instead, finding little effect for most benchmarks but flagging PIQA and Winograd.[^s2] The broader-impacts section examined misuse, gender, race and religion biases in model outputs, and energy use.[^s2]

## Influence

Rather than releasing the weights, OpenAI exposed GPT-3-family models through a private-beta "text in, text out" API announced on 11 June 2020, citing research funding, the cost of running such large models, and the ability to respond to misuse.[^s5] The paper's prompting-based evaluation helped turn prompting into a primary way of adapting language models, although the CS324 notes stress that why in-context learning works remained poorly understood.[^s4]

## Connections

The paper is a landmark in the **large language model** and **pretraining** lineage. It was **created by** **OpenAI**, is **based on** the decoder-only **Transformer architecture** that grew out of *Attention Is All You Need*, and was **influenced by** the **Sparse Transformer**'s attention pattern.[^s2][^s3] It popularised the term **in-context learning**, with its **zero-shot** and **few-shot prompting** settings.[^s2][^s3] Its scale-driven results fed the study of **scaling laws**, it was **evaluated on** benchmarks such as **TriviaQA**, and its candid contamination analysis made it an early case study in **benchmark contamination**.[^s2][^s4]

## Sources
[^s1]: Brown et al., "Language Models are Few-Shot Learners", NeurIPS 2020 proceedings. https://papers.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html (accessed 2026-11-16)
[^s2]: Brown et al., "Language Models are Few-Shot Learners", arXiv 2005.14165 (v4). https://arxiv.org/pdf/2005.14165 (accessed 2026-11-16)
[^s3]: Zhang et al., Dive into Deep Learning, section 11.9. https://d2l.ai/chapter_attention-mechanisms-and-transformers/large-pretraining-transformers.html (accessed 2026-11-16)
[^s4]: Stanford CS324, "Capabilities" lecture notes (Winter 2022). https://stanford-cs324.github.io/winter2022/lectures/capabilities (accessed 2026-11-16)
[^s5]: OpenAI, "OpenAI API", 11 June 2020. https://openai.com/index/openai-api/ (accessed 2026-11-16)
