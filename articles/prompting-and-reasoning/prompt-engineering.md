---
id: kt:prompt-engineering
type: Technique
title: Prompt engineering
aliases: [prompt design, prompting techniques, prompt-based learning]
domain: prompting-and-reasoning
summary: >-
  The practice of designing, testing and iterating on the text given to a pretrained language model
  (instructions, context, examples and output format) so that it reliably performs a task without
  changing the model's weights.
maturity: established
broader: [kt:natural-language-processing]
related: [kt:chain-of-thought, kt:prompt-sensitivity, kt:few-shot-prompting, kt:large-language-model]
relations:
  - {predicate: dependsOn, object: kt:in-context-learning}
  - {predicate: alternativeTo, object: kt:fine-tuning}
sources:
  - id: s1
    title: "Language Models are Few-Shot Learners"
    publisher: NeurIPS 2020 (Brown et al.)
    url: https://papers.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing"
    publisher: arXiv 2107.13586v1 (Liu, Yuan, Fu, Jiang, Hayashi, Neubig)
    url: https://arxiv.org/abs/2107.13586v1
    type: primary
    accessed: 2026-11-12
  - id: s3
    title: "The Prompt Report: A Systematic Survey of Prompting Techniques"
    publisher: arXiv 2406.06608v6 (Schulhoff et al.)
    url: https://arxiv.org/abs/2406.06608v6
    type: primary
    accessed: 2026-11-12
  - id: s4
    title: "Large Language Models Are Human-Level Prompt Engineers"
    publisher: ICLR 2023, authors' arXiv version 2211.01910 (Zhou, Muresanu, Han, Paster, Pitis, Chan, Ba)
    url: https://arxiv.org/pdf/2211.01910
    type: primary
    accessed: 2026-11-12
  - id: s5
    title: "Prompt engineering overview"
    publisher: Anthropic, Claude Platform documentation
    url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
    type: official-docs
    accessed: 2026-11-12
  - id: s6
    title: "Prompt engineering"
    publisher: OpenAI API documentation
    url: https://developers.openai.com/api/docs/guides/prompt-engineering
    type: official-docs
    accessed: 2026-11-12
created: 2026-11-12
---

# Prompt engineering

**Prompt engineering** is the practice of shaping the input text a pretrained language model receives (its instructions, background context, worked examples and requested output format) so that the model consistently produces what an application needs. OpenAI's API guide frames it as writing instructions so a model reliably meets your requirements, while noting that model output is non-deterministic, which makes the work part craft and part empirical science.[^s6] Unlike **fine-tuning**, it leaves the model's weights untouched: all adaptation happens through the context.[^s1][^s2]

## Origin

The discipline grew out of the observation that large pretrained models can be steered by text alone. Brown et al.'s 2020 GPT-3 paper showed that a 175-billion-parameter autoregressive model could perform new tasks when the task description and a few demonstrations were supplied purely as text, with no gradient updates or fine-tuning.[^s1] In 2021, Liu et al. named this shift the "pre-train, prompt, and predict" paradigm: instead of training a separate supervised model for each task, an input is wrapped in a textual template with unfilled slots, the language model fills them, and the answer is read off the completed string.[^s2] Their survey organized early work by choice of pretrained model, prompt design and tuning strategy, and much of the later vocabulary (templates, zero-shot and few-shot prompting) traces to this period.[^s2]

## How it works

A modern prompt typically combines several components, and each has become a lever with its own techniques:[^s5][^s6]

- **Instructions and roles.** Chat APIs separate developer or system instructions from end-user input; OpenAI documents that developer messages take priority over user messages, likening them to a function definition and user input to its arguments.[^s6]
- **Examples (few-shot prompting).** A handful of diverse input-output pairs in the prompt lets the model pick up a pattern without fine-tuning.[^s1][^s6]
- **Structure.** Vendors recommend delimiting sections such as instructions, examples and reference context with Markdown headers or XML tags; Anthropic lists XML structuring, role prompting, extended thinking and prompt chaining among its core techniques.[^s5][^s6]
- **Reasoning elicitation.** Asking for intermediate steps, as in chain-of-thought prompting, is one of the most cited families of techniques.[^s3][^s4]

The field has grown large enough to need its own taxonomy. The Prompt Report (Schulhoff et al., v6, February 2025) catalogued 58 text prompting techniques and 40 techniques for other modalities, and defined 33 vocabulary terms, arguing that the literature suffered from conflicting terminology.[^s3]

## Automatic prompt engineering

Because hand-tuning prompts is laborious, researchers have used models to write prompts. Zhou et al.'s Automatic Prompt Engineer (APE, ICLR 2023) treats the instruction as a program: an LLM proposes candidate instructions, each is scored (for example by accuracy on training examples), and the best is selected, optionally after rounds of resampling around top candidates.[^s4] Across 24 NLP tasks, the authors report that APE's instructions matched or beat human-written ones on 21.[^s4] APE also found a zero-shot reasoning trigger that outscored the classic "Let's think step by step" on MultiArith (78.7 to 82.0) and GSM8K (40.7 to 43.0) in their experiments.[^s4]

## Limitations and practice

Prompt engineering is empirical and model-specific. Anthropic advises defining success criteria and building tests before iterating on a prompt, and notes that some goals, such as latency or cost, are usually better addressed by choosing a different model than by rewording.[^s5] OpenAI recommends pinning production applications to specific model snapshots and maintaining evaluation suites, because prompt behaviour can shift when the model changes.[^s6] Guidance also diverges by model family: as of 2026, OpenAI advises giving reasoning models high-level goals but giving its GPT models precise, explicit instructions.[^s6] The sheer number of overlapping techniques, and the terminology confusion the Prompt Report documents, mean many published "tricks" are hard to compare or reproduce across models.[^s3] Automated search methods such as APE partly reframe the task as optimization rather than craft.[^s4]

## Connections

Prompt engineering sits within **natural language processing** (`broader`) as the main way practitioners adapt pretrained models without training.[^s2] It `dependsOn` **in-context learning**, the capability that GPT-3 demonstrated, and **few-shot prompting** is its most basic technique.[^s1] It is an `alternativeTo` **fine-tuning**: vendor guides suggest examples in the prompt as a substitute for weight updates.[^s6] **Chain-of-thought** prompting is one of its best-known techniques, and APE showed such reasoning triggers can themselves be optimized automatically.[^s4] **Prompt sensitivity**, the brittleness of model outputs to small wording and formatting changes, is the reason the discipline leans so heavily on evaluation.[^s5][^s6] All of this applies to **large language models**, whose scale made text-only task specification practical.[^s1]

## Sources
[^s1]: Brown et al., "Language Models are Few-Shot Learners", NeurIPS 2020. https://papers.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html (accessed 2026-11-12)
[^s2]: Liu et al., "Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing", arXiv 2107.13586v1, 2021. https://arxiv.org/abs/2107.13586v1 (accessed 2026-11-12)
[^s3]: Schulhoff et al., "The Prompt Report: A Systematic Survey of Prompting Techniques", arXiv 2406.06608v6, 2025. https://arxiv.org/abs/2406.06608v6 (accessed 2026-11-12)
[^s4]: Zhou et al., "Large Language Models Are Human-Level Prompt Engineers", ICLR 2023 (arXiv 2211.01910). https://arxiv.org/pdf/2211.01910 (accessed 2026-11-12)
[^s5]: Anthropic, "Prompt engineering overview", Claude Platform documentation. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview (accessed 2026-11-12)
[^s6]: OpenAI, "Prompt engineering", OpenAI API documentation. https://developers.openai.com/api/docs/guides/prompt-engineering (accessed 2026-11-12)
