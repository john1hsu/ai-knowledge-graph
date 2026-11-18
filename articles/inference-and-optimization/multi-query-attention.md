---
id: kt:multi-query-attention
type: Architecture
title: Multi-query attention
aliases: [MQA, multiquery attention, multi-query self-attention, single key-value head attention]
domain: inference-and-optimization
summary: >-
  A variant of transformer multi-head attention in which every query head keeps its own projection but all heads
  share one key projection and one value projection, shrinking the KV cache and the memory traffic of each
  autoregressive decoding step at a small cost in model quality.
maturity: established
broader: [kt:self-attention, kt:llm-inference-optimization]
related: [kt:kv-cache, kt:transformer-architecture, kt:flash-attention, kt:batching-and-paged-attention, kt:palm]
relations:
  - {predicate: introducedIn, object: kt:fast-transformer-decoding-one-write-head-is-all-you-need}
  - {predicate: createdBy, object: kt:noam-shazeer}
  - {predicate: alternativeTo, object: kt:grouped-query-attention}
  - {predicate: dependsOn, object: kt:kv-cache}
  - {predicate: enables, object: kt:context-window}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
sources:
  - id: s1
    title: "Fast Transformer Decoding: One Write-Head is All You Need"
    publisher: Noam Shazeer (Google), arXiv 1911.02150 (2019)
    url: https://arxiv.org/pdf/1911.02150
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints"
    publisher: Ainslie et al., Proceedings of EMNLP 2023, pp. 4895–4901
    url: https://aclanthology.org/2023.emnlp-main.298
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "Efficiently Scaling Transformer Inference"
    publisher: Pope et al., Proceedings of Machine Learning and Systems 5 (MLSys 2023), pp. 606–624
    url: https://proceedings.mlsys.org/paper_files/paper/2023/hash/c4be71ab8d24cdfb45e3d06dbfca2780-Abstract-mlsys2023.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "PaLM: Scaling Language Modeling with Pathways"
    publisher: Chowdhery et al., Journal of Machine Learning Research 24 (2023)
    url: https://jmlr.org/papers/volume24/22-1144/22-1144.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s5
    title: "Optimizing LLMs for Speed and Memory"
    publisher: Hugging Face Transformers documentation
    url: https://huggingface.co/docs/transformers/llm_tutorial_optimization
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# Multi-query attention

**Multi-query attention (MQA)** is a modification of the transformer's multi-head attention layer. Standard multi-head attention gives each of its *h* heads separate query, key and value projections. MQA keeps *h* distinct query heads but replaces the per-head keys and values with a single shared key projection and a single shared value projection, so every head attends over the same keys and values with its own query.[^s1] Noam Shazeer of Google proposed it in a November 2019 arXiv paper titled "Fast Transformer Decoding: One Write-Head is All You Need", motivated by the cost of generating text one token at a time rather than by training speed.[^s1]

## How it works

Shazeer's argument is a memory-bandwidth analysis. In batched training, memory access is small relative to arithmetic, so multi-head attention runs efficiently. In incremental (autoregressive) decoding, however, each step must reload the cached keys and values of all previous positions, and he derives that the ratio of memory access to arithmetic for multi-head attention is on the order of *n/d + 1/b*, where *n* is the sequence length, *d* the model dimension and *b* the batch size. When the sequence is as long as the model is wide, or the batch is tiny, reloading those tensors dominates. Sharing one key head and one value head divides the *n/d* term by *h*.[^s1]

Concretely, the KV cache stores one key and one value vector per layer per token instead of *h* of each. Hugging Face's optimisation guide illustrates this with a code model whose standard cache for a 16,000-token input is about 15 GB in float16; with a single key-value head the guide puts it below 400 MB.[^s5] The same guide stresses that the saving exists only when a KV cache is used: a single uncached forward pass still forms a different query-key product for every query head, so its peak memory does not change.[^s5]

## Evidence and limitations

In Shazeer's 2019 experiments on WMT14 English-German translation, the multi-query model scored 26.5 dev BLEU with greedy decoding against 26.7 for the multi-head baseline, while amortised decoder time per token on TPUv2 fell from 46 to 3.8 microseconds for greedy search and from 203 to 32 microseconds with beam size 4. Training cost was roughly unchanged. On the Billion-Word language-modelling benchmark the dev perplexity rose slightly, from 29.9 to 30.2, but this beat simply cutting the number of heads or shrinking the key and value dimensions, which degraded quality more.[^s1] The paper also found MQA orthogonal to local attention, and combining the two gave the fastest decoders it tested.[^s1]

The quality cost is the main criticism. Ainslie et al. note that MQA can degrade quality, and that training a separate model purely for faster inference may be unattractive. Their EMNLP 2023 paper shows that existing multi-head checkpoints can be uptrained into MQA with about 5% of the original pre-training compute, and introduces grouped-query attention, which uses an intermediate number of key-value heads to recover most of the quality while keeping speed close to MQA.[^s2] Hugging Face's guide reports that choosing a small number of groups, such as 2, 4 or 8, keeps nearly all of MQA's memory and speed gains.[^s5]

## In practice

Google's PaLM adopted MQA for its 540B-parameter model; its authors, citing Shazeer, report a neutral effect on quality and training speed and significant savings in autoregressive decoding, which is where standard multi-head attention runs inefficiently on accelerators.[^s4] Pope et al.'s MLSys 2023 work on serving PaLM attributes much of its long-context scaling to MQA, stating that its lower memory needs, with suitable partitioning across TPU v4 chips, allow contexts up to 32 times longer.[^s3] Hugging Face's documentation lists Falcon, PaLM, MPT and BLOOM among models using MQA and, as of its writing, strongly recommends MQA or GQA for chat-style deployments with long inputs.[^s5] Many later open models chose GQA instead, the guide citing Llama 2 70B as the most notable early example.[^s5]

## Connections

MQA is a restricted form of **self-attention** and a model-level lever within **LLM inference optimization**, introduced in Shazeer's 2019 paper.[^s1] Its benefit **depends on the KV cache**, whose per-token size it cuts by the number of heads, and so it **enables** longer **context windows** at serving time.[^s5][^s3] **Grouped-query attention** is the main **alternative**, interpolating between MQA and full multi-head attention.[^s2] It complements **FlashAttention** and **paged KV-cache batching**, which reduce attention's memory traffic and fragmentation without changing the architecture, and it is part of the **PaLM** design.[^s4] Model support is implemented in **Hugging Face Transformers**.[^s5]

## Sources

[^s1]: N. Shazeer, "Fast Transformer Decoding: One Write-Head is All You Need", arXiv 1911.02150, 2019. https://arxiv.org/pdf/1911.02150 (accessed 2026-11-18)
[^s2]: J. Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints", EMNLP 2023. https://aclanthology.org/2023.emnlp-main.298 (accessed 2026-11-18)
[^s3]: R. Pope et al., "Efficiently Scaling Transformer Inference", MLSys 2023. https://proceedings.mlsys.org/paper_files/paper/2023/hash/c4be71ab8d24cdfb45e3d06dbfca2780-Abstract-mlsys2023.html (accessed 2026-11-18)
[^s4]: A. Chowdhery et al., "PaLM: Scaling Language Modeling with Pathways", JMLR 24, 2023. https://jmlr.org/papers/volume24/22-1144/22-1144.pdf (accessed 2026-11-18)
[^s5]: Hugging Face, "Optimizing LLMs for Speed and Memory", Transformers documentation. https://huggingface.co/docs/transformers/llm_tutorial_optimization (accessed 2026-11-18)
