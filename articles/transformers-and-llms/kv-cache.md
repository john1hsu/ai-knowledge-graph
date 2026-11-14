---
id: kt:kv-cache
type: Technique
title: KV cache
aliases: [key-value cache, KV caching, past key values, attention KV cache]
domain: transformers-and-llms
summary: >-
  An inference technique for autoregressive transformers that stores the attention key and value vectors of every
  token already processed, so each new decoding step computes keys and values only for the newest token and reuses
  the rest, trading GPU memory for much faster generation.
maturity: established
broader: [kt:llm-inference-optimization]
related: [kt:batching-and-paged-attention, kt:context-window, kt:multi-query-attention, kt:grouped-query-attention, kt:speculative-decoding, kt:quantization]
relations:
  - {predicate: dependsOn, object: kt:self-attention}
  - {predicate: partOf, object: kt:transformer-architecture}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: implementedIn, object: kt:vllm}
  - {predicate: enables, object: kt:prefix-caching}
sources:
  - id: s1
    title: "Cache strategies (KV cache)"
    publisher: Hugging Face Transformers documentation
    url: https://huggingface.co/docs/transformers/kv_cache
    type: official-docs
    accessed: 2026-11-14
  - id: s2
    title: "Fast Transformer Decoding: One Write-Head is All You Need"
    publisher: Noam Shazeer, arXiv 1911.02150 (2019)
    url: https://arxiv.org/abs/1911.02150v1
    type: primary
    accessed: 2026-11-14
  - id: s3
    title: "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints"
    publisher: Ainslie et al., EMNLP 2023 (ACL Anthology)
    url: https://aclanthology.org/2023.emnlp-main.298
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "Efficiently Scaling Transformer Inference"
    publisher: Pope et al., Proceedings of MLSys 2023
    url: https://proceedings.mlsys.org/paper_files/paper/2023/hash/c4be71ab8d24cdfb45e3d06dbfca2780-Abstract-mlsys2023.html
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
    publisher: Kwon et al., SOSP 2023, arXiv 2309.06180
    url: https://arxiv.org/pdf/2309.06180
    type: primary
    accessed: 2026-11-14
created: 2026-11-14
---

# KV cache

A **KV cache** (key-value cache) is the store of attention keys and values that a decoder-only transformer keeps while it generates text one token at a time. In self-attention every token is projected into a query, a key and a value; when a model generates autoregressively, each new token must attend to all earlier tokens, so without a cache the model would recompute identical key and value vectors for the whole prefix at every step. Caching them means each step only computes the newest token's projections and appends them, which cuts per-step computation and is the main knob for trading memory against speed during generation.[^s1]

## How it works

Generation splits into two phases. In the **prefill** phase the prompt is processed in parallel and the keys and values for every prompt token, in every layer, are written to the cache. In the **decode** phase the model runs one token at a time: it computes that token's query, key and value, appends the new key and value to each layer's cache, and attends from the new query over the cached keys and values.[^s1][^s4] Attention cost per step therefore grows linearly with the length of the sequence so far rather than requiring the whole prefix to be re-encoded.

The price is memory. For standard multi-head attention the cache holds, per token, one key and one value vector for every head in every layer, so its size scales as roughly 2 × layers × KV heads × head dimension × bytes per element, multiplied by sequence length and batch size. The PagedAttention paper works this out for OPT-13B as 2 × 5120 (hidden size) × 40 (layers) × 2 bytes, about 800 KB per token, and reports that on a 40 GB A100 serving a 13B model, close to 30% of GPU memory goes to such per-request state while parameters take about 65%.[^s5]

## Why it matters and limitations

Shazeer observed in 2019 that incremental decoding is slow not because of arithmetic but because every step must reload the large key and value tensors, making decoding bound by memory bandwidth.[^s2] That observation shaped later architecture choices. **Multi-query attention (MQA)** lets all query heads share one key-value head, shrinking the cache and the bandwidth needed per step at a small cost in quality.[^s2] **Grouped-query attention (GQA)**, published at EMNLP 2023, uses an intermediate number of key-value heads; its authors report that uptraining existing multi-head checkpoints with about 5% of the original pre-training compute yields quality close to multi-head attention at speeds comparable to MQA.[^s3] Google's PaLM inference work reported in 2023 that multiquery attention, combined with suitable partitioning across TPU v4 chips, enabled context lengths up to 32 times larger.[^s4]

Cache management is itself a systems problem. Kwon et al. measured that in earlier serving systems only 20.4%–38.2% of KV-cache memory actually held token states, with the rest lost to slots reserved for future tokens and to internal and external fragmentation.[^s5] Their paged allocation scheme (PagedAttention, in vLLM) stores the cache in fixed-size blocks and reported 2–4× higher throughput than FasterTransformer and Orca at the same latency.[^s5] Long contexts amplify all of this: the cache grows with every token, so it, not the weights, often limits batch size and maximum context.[^s1][^s5]

## In practice

Every major inference stack keeps a KV cache by default. Hugging Face Transformers, for example, uses a growing `DynamicCache` unless configured otherwise; a pre-allocated `StaticCache` works with `torch.compile` but wastes compute on masked slots; offloaded caches keep only the current layer on the GPU; and quantized caches store keys and values at low bit widths (int2 to int8, depending on backend) to save memory at some latency cost.[^s1] Sliding-window models cap cache growth at the window size, and state-space models such as Mamba have no keys or values and need their own cache type.[^s1] The same docs describe reusing a cache across chat turns and copying a prefilled cache so that a shared prompt prefix is computed only once, the idea behind prefix caching.[^s1]

## Connections

The KV cache is a direct consequence of **self-attention**, whose keys and values it stores, and it sits inside the decoder stack of the **transformer architecture**.[^s1] It falls under **LLM inference optimization**: **continuous batching and PagedAttention** and **vLLM** exist largely to allocate it efficiently, and **quantization** is applied to it as well as to weights.[^s5][^s1] **Multi-query** and **grouped-query attention** are architectural responses to its memory cost, which is also what makes a long **context window** expensive to serve.[^s2][^s3][^s4] **Speculative decoding** relies on rolling the cache back when draft tokens are rejected, which Transformers supports by cropping the cache, and the cache's reusability **enables prefix caching**.[^s1] It is implemented in **Hugging Face Transformers**.[^s1]

## Sources

[^s1]: Hugging Face, "Cache strategies" (Transformers documentation). https://huggingface.co/docs/transformers/kv_cache (accessed 2026-11-14)
[^s2]: N. Shazeer, "Fast Transformer Decoding: One Write-Head is All You Need", arXiv 1911.02150, 2019. https://arxiv.org/abs/1911.02150v1 (accessed 2026-11-14)
[^s3]: J. Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints", EMNLP 2023. https://aclanthology.org/2023.emnlp-main.298 (accessed 2026-11-14)
[^s4]: R. Pope et al., "Efficiently Scaling Transformer Inference", MLSys 2023. https://proceedings.mlsys.org/paper_files/paper/2023/hash/c4be71ab8d24cdfb45e3d06dbfca2780-Abstract-mlsys2023.html (accessed 2026-11-14)
[^s5]: W. Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention", SOSP 2023, arXiv 2309.06180. https://arxiv.org/pdf/2309.06180 (accessed 2026-11-14)
