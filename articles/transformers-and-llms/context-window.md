---
id: kt:context-window
type: Concept
title: Context window
aliases: [context length, context size, maximum context length, long-context window]
domain: transformers-and-llms
summary: >-
  The maximum span of tokens a language model can attend to in a single request, covering the prompt, any
  documents, tool results and conversation history, and the output it generates; it acts as the model's working
  memory, distinct from what it learned in training.
maturity: established
broader: [kt:large-language-model, kt:transformer-architecture]
related: [kt:in-context-learning, kt:retrieval-augmented-generation, kt:batching-and-paged-attention, kt:scaling-laws]
relations:
  - {predicate: dependsOn, object: kt:self-attention}
  - {predicate: dependsOn, object: kt:positional-encoding}
  - {predicate: evaluatedOn, object: kt:ruler}
  - {predicate: enables, object: kt:in-context-learning}
sources:
  - id: s1
    title: "Attention is All you Need"
    publisher: NeurIPS 2017, Advances in Neural Information Processing Systems 30 (Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin)
    url: https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s2
    title: "Extending Context Window of Large Language Models via Positional Interpolation"
    publisher: arXiv:2306.15595v2 (Chen, Wong, Chen, Tian), 2023
    url: https://arxiv.org/abs/2306.15595v2
    type: primary
    accessed: 2026-11-10
  - id: s3
    title: "Lost in the Middle: How Language Models Use Long Contexts"
    publisher: Transactions of the Association for Computational Linguistics 12:157–173, 2024 (Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang)
    url: https://aclanthology.org/2024.tacl-1.9/
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s4
    title: "RULER: What's the Real Context Size of Your Long-Context Language Models?"
    publisher: arXiv:2404.06654v2 (Hsieh, Sun, Kriman, Acharya, Rekesh, Jia, Zhang, Ginsburg), 2024
    url: https://arxiv.org/abs/2404.06654v2
    type: primary
    accessed: 2026-11-10
  - id: s5
    title: "Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context"
    publisher: Gemini Team, Google — technical report, arXiv:2403.05530v2, April 2024
    url: https://arxiv.org/html/2403.05530v2
    type: primary
    accessed: 2026-11-10
  - id: s6
    title: "Context windows"
    publisher: Anthropic, Claude Platform documentation
    url: https://platform.claude.com/docs/es/build-with-claude/context-windows
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# Context window

A **context window** (or *context length*) is the largest amount of text, measured in tokens, that a language model can reference at once when producing a response. Anthropic's API documentation describes it as the model's working memory, separate from the data it was trained on, and counts everything in a request against it: the system prompt, every message and tool result, attached images and documents, tool definitions, and the tokens the model generates in reply, including any extended "thinking" tokens.[^s6] Whatever falls outside the window simply does not exist for that request, which makes the window one of the most consequential numbers in a model's specification.[^s6]

## Why the window is finite

In the Transformer, every position attends to every other position. Vaswani et al.'s 2017 analysis gives self-attention a per-layer cost of O(n²·d) for sequence length n and representation size d, against O(n·d²) for a recurrent layer, in exchange for connecting any two positions in a constant number of steps.[^s1] That quadratic term is why longer contexts become expensive in compute and memory. The same paper already noted that restricting attention to a neighbourhood of size r cuts the cost to O(r·n·d), at the price of a longer path between distant positions.[^s1]

The second constraint is position. Because attention by itself is order-blind, Transformers add positional information to token embeddings; the original model used fixed sinusoids, chosen partly in the hope that they would let the model extrapolate to sequences longer than any seen in training.[^s1] In practice, models trained at one length generalise poorly beyond it. Chen et al. (2023) showed that naively running a model that uses rotary position embeddings (RoPE), such as LLaMA, past its trained length can yield extremely large attention scores that break self-attention.[^s2]

## Extending the window

Chen et al.'s **Position Interpolation** rescales position indices so that a longer input is squeezed into the range the model was trained on, rather than extrapolating beyond it. With fine-tuning of at most 1,000 steps, they extended LLaMA models from 7B to 65B parameters to windows of up to 32,768 tokens, largely preserving quality on short inputs; their analysis bounded interpolation's error at roughly 600 times smaller than extrapolation's.[^s2] Since the architecture is unchanged, existing training and serving infrastructure can be reused.[^s2]

Advertised windows have since grown by orders of magnitude. Google's Gemini 1.5 report (April 2024) tested inputs up to 10 million tokens and reported, by its own measurements, above 99% needle-in-a-haystack recall up to 1 million tokens across text, video and audio.[^s5] As of November 2026, Anthropic documents a 1-million-token window as the default for its current Claude models, with older models at 200,000 tokens and a cap of 128,000 output tokens per request on the 1M models.[^s6]

## Advertised versus effective context

A large window does not mean the model uses all of it well. Liu et al. (TACL 2024) found a U-shaped pattern on multi-document question answering and key-value retrieval: accuracy was highest when the relevant information sat at the start or end of the input and dropped markedly when it sat in the middle, even for models built for long contexts.[^s3] The RULER benchmark of Hsieh et al. (2024) argued that the simple needle test measures only shallow retrieval, adding multi-needle, multi-hop tracing and aggregation tasks. Of 17 models that all claimed at least 32K tokens, only about half performed satisfactorily at 32K, and models that nearly aced the basic needle test still degraded as length and task difficulty grew.[^s4] Anthropic's documentation calls the same phenomenon "context rot" and advises curating what enters the window rather than filling it.[^s6]

## In practice

Operationally, the window is a hard budget. In Anthropic's API, an input that alone exceeds the window is rejected with an error, while on newer models a request whose input plus maximum output would exceed it is accepted but stops generating when the limit is reached.[^s6] Prompt caching changes cost but not occupancy: cached prefixes still count against the window.[^s6] For long-running agents and conversations, vendors therefore offer context-management tools such as server-side compaction, which summarises earlier turns, and clearing of old tool results.[^s6] Long windows also unlock new uses: Gemini 1.5, given a grammar book, a word list and about 400 parallel sentences in its prompt, learned to translate English into Kalamang, a language with under 200 speakers, at a level close to a human who studied the same material.[^s5]

## Connections

- **Broader:** the context window is a defining property of every **large language model** and a direct consequence of the **Transformer architecture**, whose attention cost grows quadratically with sequence length.[^s1][^s6]
- **Depends on:** **self-attention**, which sets the cost of long inputs, and **positional encoding**, which determines whether a model can handle positions beyond its training length.[^s1][^s2]
- **Enables:** **in-context learning** at scale, from few-shot examples to whole reference books supplied in the prompt.[^s5]
- **Evaluated on:** **RULER** and needle-in-a-haystack tests, which separate advertised from effective context length.[^s4][^s5]
- **Related:** **retrieval-augmented generation** and similar pipelines decide what to put in the window, and the lost-in-the-middle effect shows that where retrieved passages are placed matters.[^s3] Because attention work grows with sequence length, long contexts raise serving cost, the problem that inference techniques such as **continuous batching and PagedAttention** address, while **scaling laws** govern the pretraining these models build on.[^s1]

## Sources

[^s1]: Vaswani et al., "Attention is All you Need", NeurIPS 2017. https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf (accessed 2026-11-10)
[^s2]: Chen, Wong, Chen, Tian, "Extending Context Window of Large Language Models via Positional Interpolation", arXiv:2306.15595, 2023. https://arxiv.org/abs/2306.15595v2 (accessed 2026-11-10)
[^s3]: Liu et al., "Lost in the Middle: How Language Models Use Long Contexts", TACL 12, 2024. https://aclanthology.org/2024.tacl-1.9/ (accessed 2026-11-10)
[^s4]: Hsieh et al., "RULER: What's the Real Context Size of Your Long-Context Language Models?", arXiv:2404.06654, 2024. https://arxiv.org/abs/2404.06654v2 (accessed 2026-11-10)
[^s5]: Gemini Team, Google, "Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context", arXiv:2403.05530v2, 2024. https://arxiv.org/html/2403.05530v2 (accessed 2026-11-10)
[^s6]: Anthropic, "Context windows", Claude Platform documentation. https://platform.claude.com/docs/es/build-with-claude/context-windows (accessed 2026-11-10)
