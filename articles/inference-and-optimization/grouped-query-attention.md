---
id: kt:grouped-query-attention
type: Architecture
title: Grouped-query attention
aliases: [GQA, grouped query attention, grouped-query self-attention]
domain: inference-and-optimization
summary: >-
  A transformer attention variant that partitions the query heads into G groups, each sharing a single key head and
  value head, so the KV cache shrinks by a factor of H/G; it interpolates between multi-head attention (G = H) and
  multi-query attention (G = 1) to get most of MQA's decoding speed at close to multi-head quality.
maturity: established
broader: [kt:self-attention, kt:llm-inference-optimization]
related: [kt:flash-attention, kt:batching-and-paged-attention, kt:llama-2, kt:mistral-7b]
relations:
  - {predicate: introducedIn, object: kt:gqa-training-generalized-multi-query-transformer-models-from-multi-head-checkpoints}
  - {predicate: extends, object: kt:multi-query-attention}
  - {predicate: dependsOn, object: kt:kv-cache}
  - {predicate: implementedIn, object: kt:pytorch}
sources:
  - id: s1
    title: "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints"
    publisher: Ainslie et al., Proceedings of EMNLP 2023, pp. 4895–4901 (ACL Anthology PDF)
    url: https://aclanthology.org/2023.emnlp-main.298.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "Llama 2: Open Foundation and Fine-Tuned Chat Models"
    publisher: Touvron et al., Meta, arXiv 2307.09288 (2023)
    url: https://arxiv.org/pdf/2307.09288
    type: primary
    accessed: 2026-11-18
  - id: s3
    title: "Mistral 7B"
    publisher: Jiang et al., Mistral AI, arXiv 2310.06825 (2023)
    url: https://arxiv.org/pdf/2310.06825
    type: primary
    accessed: 2026-11-18
  - id: s4
    title: "torch.nn.functional.scaled_dot_product_attention"
    publisher: PyTorch documentation (main, 2.16 pre-release)
    url: https://docs.pytorch.org/docs/main/generated/torch.nn.functional.scaled_dot_product_attention.html
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# Grouped-query attention

**Grouped-query attention (GQA)** is a way of wiring a transformer's attention layer so that several query heads read from the same key and value head. A layer with *H* query heads is split into *G* groups; every query head keeps its own projection, but the heads inside a group share one key projection and one value projection.[^s1] The two extremes are familiar designs: with one group (GQA-1) the layer becomes multi-query attention, and with as many groups as heads (GQA-H) it is ordinary multi-head attention.[^s1] GQA was proposed by Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebrón and Sumit Sanghai in a paper first posted on arXiv in May 2023 and published at EMNLP 2023.[^s1]

## Why it exists

During autoregressive generation, each new token must load the cached keys and values of every earlier token, so decoding is limited by memory bandwidth more than by arithmetic.[^s1] Collapsing all key-value heads into one (multi-query attention) removes most of that traffic, but the GQA authors report that it can cost quality, that MQA models trained from scratch were prone to loss spikes and diverged when fine-tuned on long inputs, and that training a separate model only to serve it faster is often unattractive.[^s1] GQA keeps an intermediate number of key-value heads to recover quality while retaining most of the speed.[^s1]

## How it works

For a model with *H* = 32 query heads and *G* = 8 key-value heads, each key-value head serves four query heads, and the per-token KV cache is one quarter the size of the multi-head version. Mistral 7B uses exactly this shape: 32 attention heads, 8 key-value heads, head dimension 128.[^s3] Computationally, the shared key and value tensors are simply broadcast to each query head in their group. PyTorch's reference implementation of `scaled_dot_product_attention` does this with `repeat_interleave` along the head dimension when the experimental `enable_gqa=True` flag is set, and requires the query head count to be divisible by the key-value head count.[^s4]

GQA also introduced a cheap way to obtain such models. Rather than training from scratch, an existing multi-head checkpoint is **uptrained**: the key and value projection matrices of the heads in each group are mean-pooled into one, and pre-training then continues for a fraction α of the original steps. The paper used α = 0.05, about 600 TPUv3 chip-days for T5-XXL, found mean pooling better than keeping one head or initialising randomly, and saw diminishing returns beyond roughly 10% uptraining.[^s1]

## Evidence

On T5 encoder-decoder models evaluated across summarisation, translation and question answering, Ainslie et al. report an average score of 47.1 for an uptrained GQA-8 XXL model versus 47.2 for multi-head XXL and 46.6 for MQA XXL, with inference time per sample of 0.28 s against 1.51 s (multi-head) and 0.24 s (MQA).[^s1] They chose eight groups as the middle ground between speed and quality.[^s1] The authors argue GQA suits larger models especially well: bigger models have more heads, so collapsing to one key-value head is a harsher cut, and standard model sharding wastefully replicates MQA's single head across partitions, which GQA avoids.[^s1]

Meta's Llama 2 report independently ablated the choice on 30B-parameter models trained on 150B tokens, widening the feed-forward layer (by 1.33× for MQA, 1.3× for GQA with 8 key-value projections) to keep parameter counts comparable. GQA scored close to multi-head attention on most benchmarks and better than MQA on average; in serving tests on eight 80 GiB A100s, multi-head attention ran out of memory at batch 1024 with 256-token contexts, while both reduced-head variants did not.[^s2]

## Limitations and open questions

The original experiments covered only encoder-decoder T5 models, applied GQA to decoder self- and cross-attention but not encoder self-attention, relied partly on ROUGE, and did not compare uptraining against training GQA from scratch at XXL scale.[^s1] GQA reduces KV-cache size and bandwidth but does not change attention's quadratic cost in sequence length; the PyTorch API labels its GQA support experimental and notes it does not work with nested tensors.[^s4]

## In practice

Prominent open-weight models adopted GQA in 2023. Llama 2 used it for its 34B and 70B models (but not 7B or 13B) for inference scalability, choosing it over MQA partly because it scales more easily across GPUs.[^s2] Mistral 7B, released in October 2023, paired GQA with sliding-window attention, citing faster inference and lower decoding memory that permits larger batches and higher throughput.[^s3] As of the PyTorch main-branch documentation in November 2026, the FlashAttention, cuDNN, memory-efficient and math backends of the fused attention kernel accept GQA inputs on CUDA.[^s4]

## Connections

GQA is a form of **self-attention** and a model-architecture lever within **LLM inference optimization**.[^s1] It was **introduced in** the EMNLP 2023 GQA paper and **extends multi-query attention**, which is its *G* = 1 special case.[^s1] Its benefit **depends on the KV cache**, whose size it divides by *H/G*, and it complements **FlashAttention** and **paged KV-cache batching**, which tackle attention's memory traffic and fragmentation without altering head structure.[^s4][^s1] It is **implemented in PyTorch**'s fused attention API and appears in **Llama 2** and **Mistral 7B**.[^s4][^s2][^s3]

## Sources

[^s1]: J. Ainslie, J. Lee-Thorp, M. de Jong, Y. Zemlyanskiy, F. Lebrón, S. Sanghai, "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints", EMNLP 2023. https://aclanthology.org/2023.emnlp-main.298.pdf (accessed 2026-11-18)
[^s2]: H. Touvron et al., "Llama 2: Open Foundation and Fine-Tuned Chat Models", arXiv 2307.09288, 2023. https://arxiv.org/pdf/2307.09288 (accessed 2026-11-18)
[^s3]: A. Q. Jiang et al., "Mistral 7B", arXiv 2310.06825, 2023. https://arxiv.org/pdf/2310.06825 (accessed 2026-11-18)
[^s4]: PyTorch, "torch.nn.functional.scaled_dot_product_attention" (main documentation). https://docs.pytorch.org/docs/main/generated/torch.nn.functional.scaled_dot_product_attention.html (accessed 2026-11-18)
