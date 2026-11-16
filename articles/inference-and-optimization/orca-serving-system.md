---
id: kt:orca-serving-system
type: Tool
title: Orca (LLM serving system)
aliases: [ORCA, Orca serving system, Orca inference engine]
domain: inference-and-optimization
summary: >-
  A distributed serving system for transformer-based generative models, presented by Yu et al. (Seoul National
  University and FriendliAI) at OSDI 2022, that pairs an iteration-level scheduler with selective batching and a
  multi-GPU engine, and became the reference design and baseline for later LLM serving engines.
maturity: established
broader: [kt:model-serving, kt:llm-inference-optimization]
related: [kt:batching-and-paged-attention, kt:vllm, kt:tensorrt-llm, kt:sarathi-serve]
relations:
  - {predicate: introducedIn, object: kt:orca-a-distributed-serving-system-for-transformer-based-generative-models}
  - {predicate: dependsOn, object: kt:kv-cache}
  - {predicate: dependsOn, object: kt:tensor-parallelism}
  - {predicate: dependsOn, object: kt:pipeline-parallelism}
  - {predicate: contrastsWith, object: kt:fastertransformer}
sources:
  - id: s1
    title: "Orca: A Distributed Serving System for Transformer-Based Generative Models (full paper)"
    publisher: USENIX OSDI 2022, pp. 521–538 (Yu, Jeong, Kim, Kim and Chun)
    url: https://www.usenix.org/system/files/osdi22-yu.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Orca: A Distributed Serving System for Transformer-Based Generative Models (presentation page)"
    publisher: USENIX OSDI 2022
    url: https://www.usenix.org/conference/osdi22/presentation/yu
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
    publisher: Kwon et al., SOSP 2023, arXiv 2309.06180
    url: https://arxiv.org/pdf/2309.06180
    type: primary
    accessed: 2026-11-16
  - id: s4
    title: "The Batch Manager in TensorRT-LLM"
    publisher: NVIDIA TensorRT-LLM documentation
    url: https://nvidia.github.io/TensorRT-LLM/advanced/batch-manager.html
    type: official-docs
    accessed: 2026-11-16
  - id: s5
    title: "Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve"
    publisher: USENIX OSDI 2024 (Agrawal et al., Georgia Tech and Microsoft Research India)
    url: https://www.usenix.org/conference/osdi24/presentation/agrawal
    type: peer-reviewed
    accessed: 2026-11-16
created: 2026-11-16
---

# Orca (LLM serving system)

**Orca** is a research serving system for GPT-style generative transformers, described by Gyeong-In Yu, Joo Seong Jeong, Geon-Woo Kim, Soojeong Kim and Byung-Gon Chun of Seoul National University and FriendliAI in a paper at the 16th USENIX Symposium on Operating Systems Design and Implementation (OSDI '22, July 2022).[^s2] It is best known as the origin of iteration-level scheduling, the idea now usually called continuous or in-flight batching, but the paper describes a full system: a scheduler, a batching scheme that makes that scheduler workable, and a distributed execution engine sized for models with hundreds of billions of parameters.[^s1][^s2]

## Design

**Scheduler.** Orca's scheduler hands the engine a batch for exactly one model iteration, collects the output tokens, and then picks the next batch, so a finished request can be returned at once and a newcomer waits at most one iteration.[^s1] Selection is first-come-first-served at iteration granularity, capped by an operator-chosen maximum batch size that trades throughput against latency.[^s1] Before a request first runs, the scheduler reserves key/value storage for its `max_tokens` budget out of a fixed pool of slots; if the pool is short, the request waits. The authors adopt this to rule out deadlock, in which every running request would need memory that nobody can free.[^s1]

**Selective batching.** Requests in one iteration sit at different token positions, so their tensors do not line up. Orca concatenates all tokens into one flattened matrix for the shape-agnostic layers (linear projections, layer normalization, residual adds, GeLU) and splits the batch only around attention, which runs per request and is merged back afterwards.[^s1] Cached keys and values live in an attention K/V manager, and the per-request attention kernels are fused into one launch.[^s1]

**Distributed engine.** Orca combines intra-layer (tensor) parallelism, which shards matrix multiplications across GPUs, with inter-layer (pipeline) parallelism, which assigns equal blocks of layers to each worker; the 175B configuration uses two pipeline stages of eight GPUs each.[^s1] Control messages travel over gRPC and tensors over NCCL, avoiding the per-iteration CPU–GPU synchronization the authors identify in NVIDIA FasterTransformer.[^s1] Because each iteration is already a self-contained batch, the scheduler can keep one batch in flight per pipeline stage without the micro-batch splitting FasterTransformer relies on.[^s1]

## Evaluation and limitations

Experiments used fp16 GPT-style models of 13B, 101B, 175B and 341B parameters on Azure VMs with eight 40 GB A100 GPUs each.[^s1] With the scheduler removed, the engine alone roughly matched FasterTransformer on the smaller models. End to end on GPT-3 175B, the authors report 36.9x the throughput of FasterTransformer at the same latency, as measured by Orca's authors in 2022.[^s1][^s2] The paper itself flags caveats: workloads were synthetic because no public trace existed, early termination was simulated rather than driven by real end-of-sequence tokens, FasterTransformer was the only end-to-end baseline, and FasterTransformer still did better for the 101B model at low load.[^s1]

## Influence

Orca's code was not released, so vLLM's authors re-created it as baselines named Orca (Oracle), Orca (Pow2) and Orca (Max), differing in how much KV space each over-reserves for outputs.[^s3] They argued that such contiguous per-request reservation leaves much cache memory idle or fragmented, and reported 2–4x higher throughput than Orca and FasterTransformer at similar latency (the vLLM authors' 2023 benchmarks).[^s3] NVIDIA's TensorRT-LLM batch manager treats in-flight batching, continuous batching and iteration-level batching as names for the same technique.[^s4] Sarathi-Serve (OSDI 2024) later targeted a side effect of mixing phases in one batch: admitting a prefill-heavy request can stall ongoing decodes, which it addresses with chunked prefills and stall-free scheduling.[^s5]

## Connections

Orca sits under **model serving** and **LLM inference optimization**, and was **introduced in** its OSDI 2022 paper.[^s1][^s2] Its scheduling idea is described in general form in **continuous batching and PagedAttention**; **vLLM** kept iteration-level scheduling but replaced Orca's reserved KV slots with paging, so the system **depends on** the **KV cache** whose management later work redesigned.[^s3] Its engine **depends on** **tensor parallelism** and **pipeline parallelism**, and the paper **contrasts** it **with** **FasterTransformer**, its main baseline.[^s1] **TensorRT-LLM** and **Sarathi-Serve** carry the batching approach forward in production and research respectively.[^s4][^s5]

## Sources
[^s1]: Yu, Jeong, Kim, Kim and Chun, "Orca: A Distributed Serving System for Transformer-Based Generative Models", OSDI 2022, pp. 521–538. https://www.usenix.org/system/files/osdi22-yu.pdf (accessed 2026-11-16)
[^s2]: USENIX, OSDI '22 presentation page for Orca. https://www.usenix.org/conference/osdi22/presentation/yu (accessed 2026-11-16)
[^s3]: Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention", SOSP 2023. https://arxiv.org/pdf/2309.06180 (accessed 2026-11-16)
[^s4]: NVIDIA, "The Batch Manager in TensorRT-LLM". https://nvidia.github.io/TensorRT-LLM/advanced/batch-manager.html (accessed 2026-11-16)
[^s5]: Agrawal et al., "Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve", OSDI 2024. https://www.usenix.org/conference/osdi24/presentation/agrawal (accessed 2026-11-16)
