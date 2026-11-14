---
id: kt:llm-inference-optimization
type: Field
title: LLM inference optimization
aliases: [efficient LLM inference, LLM inference efficiency, LLM inference acceleration]
domain: inference-and-optimization
summary: >-
  The body of data-, model- and system-level techniques that cut the latency, memory footprint and cost of
  generating text with a trained large language model, chiefly by attacking the memory-bound, token-by-token
  decode phase, the growing KV cache and the sheer size of the weights.
maturity: established
broader: [kt:large-language-model, kt:machine-learning-systems]
related: [kt:kv-cache, kt:model-compression, kt:flash-attention]
relations:
  - {predicate: hasPart, object: kt:speculative-decoding}
  - {predicate: hasPart, object: kt:batching-and-paged-attention}
  - {predicate: enables, object: kt:model-serving}
sources:
  - id: s1
    title: "A Survey on Efficient Inference for Large Language Models"
    publisher: Zhou, Ning, Hong et al., arXiv 2404.14294 (2024)
    url: https://arxiv.org/html/2404.14294v2
    type: preprint
    accessed: 2026-11-14
  - id: s2
    title: "Efficiently Scaling Transformer Inference"
    publisher: Proceedings of Machine Learning and Systems 5 (MLSys 2023), pp. 606–624 (Pope et al., Google)
    url: https://proceedings.mlsys.org/paper_files/paper/2023/hash/c4be71ab8d24cdfb45e3d06dbfca2780-Abstract-mlsys2023.html
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "Orca: A Distributed Serving System for Transformer-Based Generative Models"
    publisher: USENIX OSDI '22, pp. 521–538 (Yu, Jeong, Kim, Kim and Chun)
    url: https://www.usenix.org/conference/osdi22/presentation/yu
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "Mastering LLM Techniques: Inference Optimization"
    publisher: NVIDIA Technical Blog (Verma and Vaidya, November 2023)
    url: https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization
    type: lab-research
    accessed: 2026-11-14
created: 2026-11-14
---

# LLM inference optimization

**LLM inference optimization** is the umbrella term for methods that make a trained large language model cheaper and faster to run, as opposed to cheaper to train. A 2024 survey by Zhou et al. traces the inefficiency of LLM inference to three root causes: very large parameter counts, attention whose cost grows quadratically with input length, and autoregressive decoding that emits one token per forward pass.[^s1] The scale of the problem is easy to state: holding LLaMA-2-70B's FP16 weights alone takes about 140 GB of accelerator memory, and the survey cites roughly 100 ms per generated token on two A100 GPUs, so a response of a few hundred tokens takes over ten seconds.[^s1]

## Prefill, decode and the metrics that matter

Generation has two phases. In **prefill**, the model processes the whole prompt in parallel, writes keys and values for every prompt token into the KV cache, and produces the first output token; in **decode**, it produces each further token one at a time, reusing and extending that cache.[^s1] NVIDIA's engineers describe prefill as a matrix-matrix workload that keeps the GPU busy, while decode is a matrix-vector workload whose latency is dominated by moving weights and cache from memory rather than by arithmetic.[^s4] Because the phases stress different resources, the field tracks separate metrics: first-token latency, per-output-token latency, whole-response latency, peak memory (weights plus KV cache), and throughput measured in tokens or completed requests per second.[^s1]

The KV cache is often the binding constraint. Per token it stores two vectors (key and value) per layer of width equal to the hidden size; for Llama 2 7B in 16-bit precision with a 4,096-token sequence that comes to about 2 GB for a single request, on top of roughly 14 GB of weights.[^s4] Cache size therefore caps how many requests can share a GPU, which ties memory management directly to throughput.[^s4]

## A taxonomy of techniques

Zhou et al. organise the literature into three levels.[^s1]

- **Data level** leaves the model untouched: compress the input (prompt pruning, summarisation, soft-prompt compression, retrieval) or reorganise the output so parts can be generated in parallel, as in Skeleton-of-Thought.[^s1]
- **Model level** changes the network, usually with some retraining and some accuracy risk: efficient structures such as mixture-of-experts layers and multi-query or grouped-query attention, and compression by quantization, sparsification, distillation or dynamic inference.[^s1]
- **System level** is typically lossless: faster kernels and graph optimisation, speculative decoding, and serving-layer work on memory management, batching, scheduling and distribution across devices.[^s1]

Several landmark results illustrate the system-level strand. Google's MLSys 2023 paper on serving PaLM 540B used an analytical model to choose how to partition weights and activations across TPU v4 chips, and showed that multi-query attention, with suitable partitioning, supports contexts up to 32 times longer; it reported 29 ms per token for low-batch generation with int8 weights and 76% model FLOPS utilisation when processing input tokens in large batches.[^s2] The Orca system (OSDI 2022) introduced iteration-level scheduling, letting finished requests leave and new ones join a running batch after every decoding step, and reported up to 36.9 times the throughput of NVIDIA FasterTransformer at equal latency on a GPT-3-sized 175B model.[^s3] This idea underlies what serving stacks now call continuous or in-flight batching, which NVIDIA contrasts with static batching where every request waits for the longest one.[^s4]

## Trade-offs and open questions

The levers interact and rarely compose for free. Model-level methods can degrade quality and often need fine-tuning: NVIDIA notes that multi-query attention generally requires training or up-training with it enabled, and that activations are harder to quantize than weights because of outliers.[^s4] Optimisations that raise throughput through bigger batches tend to raise per-token latency, and partitioning choices that minimise latency at small batch sizes differ from those that maximise utilisation at large ones, which is why Pope et al. frame the problem as a latency-versus-efficiency Pareto frontier rather than a single target.[^s2] The survey lists open directions including long-context inference, efficient alternatives to the transformer, and co-design with hardware.[^s1]

## Connections

LLM inference optimization is a subfield of **machine learning systems** applied to **large language models**, whose size and autoregressive decoding create its core problems.[^s1] Its central data structure is the **KV cache**, whose growth drives both memory management and attention-variant design.[^s4] **Model compression** (quantization, pruning, distillation) is its main model-level branch, and **FlashAttention** its best-known kernel-level example of reducing memory traffic without changing results.[^s1][^s4] It has as parts **speculative decoding**, which reduces the number of sequential target-model passes, and **batching and paged attention**, which descend from Orca-style iteration-level scheduling.[^s3][^s4] Together these techniques enable cost-effective **model serving**.[^s2][^s3]

## Sources

[^s1]: Zhou et al., "A Survey on Efficient Inference for Large Language Models", arXiv 2404.14294. https://arxiv.org/html/2404.14294v2 (accessed 2026-11-14)
[^s2]: Pope et al., "Efficiently Scaling Transformer Inference", MLSys 2023. https://proceedings.mlsys.org/paper_files/paper/2023/hash/c4be71ab8d24cdfb45e3d06dbfca2780-Abstract-mlsys2023.html (accessed 2026-11-14)
[^s3]: Yu et al., "Orca: A Distributed Serving System for Transformer-Based Generative Models", OSDI '22. https://www.usenix.org/conference/osdi22/presentation/yu (accessed 2026-11-14)
[^s4]: Verma and Vaidya, "Mastering LLM Techniques: Inference Optimization", NVIDIA Technical Blog, 2023. https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization (accessed 2026-11-14)
