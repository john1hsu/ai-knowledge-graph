---
id: kt:batching-and-paged-attention
type: Technique
title: Continuous batching and PagedAttention
aliases: [continuous batching, iteration-level scheduling, in-flight batching, PagedAttention, paged KV cache]
domain: inference-and-optimization
summary: >-
  A pair of LLM-serving techniques: continuous (iteration-level) batching reschedules the batch after every
  decoding step so finished requests leave and new ones join immediately, and PagedAttention stores each
  request's KV cache in small fixed-size blocks, like virtual-memory pages, so far more requests fit in GPU memory.
maturity: established
broader: [kt:llm-inference-optimization]
related: [kt:speculative-decoding, kt:quantization, kt:tensorrt-llm]
relations:
  - {predicate: introducedIn, object: kt:efficient-memory-management-for-large-language-model-serving-with-pagedattention}
  - {predicate: influencedBy, object: kt:orca-serving-system}
  - {predicate: dependsOn, object: kt:kv-cache}
  - {predicate: implementedIn, object: kt:vllm}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: enables, object: kt:model-serving}
sources:
  - id: s1
    title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
    publisher: Kwon et al., SOSP 2023, arXiv 2309.06180
    url: https://arxiv.org/abs/2309.06180
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "Efficient Memory Management for Large Language Model Serving with PagedAttention (full text)"
    publisher: Kwon et al., SOSP 2023 (copy hosted for Princeton COS 597, Fall 2024)
    url: https://www.cs.princeton.edu/~ravian/COS597_F24/papers/vllm.pdf
    type: primary
    accessed: 2026-11-09
  - id: s3
    title: "Orca: A Distributed Serving System for Transformer-Based Generative Models"
    publisher: USENIX OSDI 2022, pp. 521–538 (Yu, Jeong, Kim, Kim and Chun)
    url: https://www.usenix.org/conference/osdi22/presentation/yu
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "Orca: A Distributed Serving System for Transformer-Based Generative Models (full paper)"
    publisher: USENIX OSDI 2022
    url: https://www.usenix.org/system/files/osdi22-yu.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s5
    title: "Continuous batching"
    publisher: Hugging Face Transformers documentation
    url: https://huggingface.co/docs/transformers/continuous_batching
    type: official-docs
    accessed: 2026-11-09
  - id: s6
    title: "PagedAttention"
    publisher: Hugging Face Text Generation Inference documentation
    url: https://huggingface.co/docs/text-generation-inference/conceptual/paged_attention
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# Continuous batching and PagedAttention

**Continuous batching** and **PagedAttention** are the two ideas at the core of modern high-throughput serving of large language models. Generative models produce output one token per forward pass, and requests differ widely in prompt and output length, so serving systems built for fixed-shape batches waste both compute and memory.[^s3] Continuous batching, introduced as *iteration-level scheduling* in the Orca system (Yu et al., OSDI 2022), fixes the scheduling problem; PagedAttention, introduced with the vLLM engine by Kwon et al. at UC Berkeley (SOSP 2023), fixes the memory problem.[^s3][^s1] The two are usually deployed together, and some libraries now require a paged KV cache to run continuous batching at all.[^s5]

## Continuous batching

Traditional *request-level* batching keeps a batch fixed until every request in it finishes. A request that ends early cannot be returned and still occupies its slot, and a request that arrives mid-batch must wait for the whole batch to drain.[^s4] Orca instead runs the model one iteration at a time and lets the scheduler change the batch between iterations, so completed sequences exit and queued ones join at the next step.[^s3] Hugging Face describes the same idea as rescheduling the batch at every generation step.[^s5]

Mixing requests at different stages makes tensor shapes ragged. Orca's answer, **selective batching**, flattens the tokens of all requests into one matrix for operations that treat tokens independently (linear layers, layer norm, activations) and runs attention separately per request, since attention must only look at tokens of the same sequence.[^s4] The authors argue little is lost because attention has no weights whose reads batching would amortize.[^s4] On GPT-3 175B, Orca reported 36.9x the throughput of NVIDIA FasterTransformer at the same latency (2022 measurements by the Orca authors).[^s3]

## PagedAttention

Continuous batching raises the question of how many requests fit at once, and that is limited by the **KV cache**: the stored attention keys and values for every past token. For OPT-13B, Kwon et al. calculate roughly 800 KB per token, so one 2,048-token request can need up to 1.6 GB; on an A100 the cache took close to 30% of memory while weights took about 65%.[^s2] Earlier systems reserved one contiguous region per request sized for its maximum possible length; Orca, for example, reserves slots for a request's full `max_tokens` budget when admitting it.[^s4] Because the final length is unknown, much of that space sits reserved but unused or fragmented: Kwon et al. measured that only 20.4%–38.2% of KV-cache memory held actual token states in existing systems.[^s2]

PagedAttention borrows **paging** from operating-system virtual memory.[^s1] Each sequence's cache is split into fixed-size blocks (vLLM's default holds 16 tokens) that can live anywhere in GPU memory; a per-sequence block table maps logical to physical blocks, and a new block is allocated only when the last one fills.[^s2] The attention kernel gathers keys and values block by block through that table.[^s6] Waste is thus confined to the partly filled last block, and in the paper's measurements about 96% of the cache held token states.[^s2]

Blocks also make **sharing** cheap. Parallel samples of one prompt can point at the same prompt blocks, and beam-search candidates can share their common history, with reference counts and **copy-on-write** when a sequence must modify a shared block.[^s2] The authors report memory savings of 6.1%–9.8% for parallel sampling and 37.6%–55.2% for beam search on an Alpaca-based workload.[^s2] When memory runs out, vLLM preempts requests and either swaps their blocks to CPU memory or discards and later recomputes them.[^s2]

## Results and limitations

Kwon et al. report 2–4x higher throughput than FasterTransformer and Orca at similar latency, with larger gains for longer sequences, bigger models and more complex decoding.[^s1] Those figures come from the vLLM authors' own 2023 benchmarks. Paging adds an indirection inside the attention kernel, so it needs custom kernels rather than standard dense attention.[^s2][^s6] Block size is a trade-off: larger blocks waste more space in the last partly filled block, a caveat Hugging Face also notes for its own implementation.[^s5] Preemption choices matter too; in the paper, recomputation beat swapping at small block sizes, swapping won at large ones, and the two were comparable from 16 to 64 tokens per block.[^s2]

## In practice

As of November 2026 both techniques are standard in open-source serving. Hugging Face Text Generation Inference uses paged attention through CUDA kernels from the vLLM project, citing gains in memory efficiency, batch size and KV sharing for parallel sampling.[^s6] Hugging Face Transformers offers continuous batching through `generate_batch` and a background `ContinuousBatchingManager`, and it requires a paged attention backend such as `paged|flash_attention_2` or `paged|sdpa`; its default block size is 256 tokens.[^s5]

## Connections

These techniques belong to **LLM inference optimization**, and they **depend on** the **KV cache**, whose memory layout PagedAttention redesigns.[^s1][^s2] PagedAttention was **introduced in** Kwon et al.'s SOSP 2023 paper, which builds directly on the iteration-level scheduling of the **Orca** serving system.[^s1][^s3] Both are **implemented in** **vLLM** and **Hugging Face Transformers**, and together they **enable** efficient **model serving**.[^s1][^s5] They complement **speculative decoding** and **quantization**: batching and paging raise how many requests share a GPU, while those methods reduce the number or cost of forward passes per request.[^s1][^s5]

## Sources

[^s1]: Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention", SOSP 2023, arXiv 2309.06180. https://arxiv.org/abs/2309.06180 (accessed 2026-11-09)
[^s2]: Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention", full text. https://www.cs.princeton.edu/~ravian/COS597_F24/papers/vllm.pdf (accessed 2026-11-09)
[^s3]: Yu, Jeong, Kim, Kim and Chun, "Orca: A Distributed Serving System for Transformer-Based Generative Models", USENIX OSDI 2022. https://www.usenix.org/conference/osdi22/presentation/yu (accessed 2026-11-09)
[^s4]: Yu et al., "Orca", OSDI 2022, full paper. https://www.usenix.org/system/files/osdi22-yu.pdf (accessed 2026-11-09)
[^s5]: Hugging Face, "Continuous batching", Transformers documentation. https://huggingface.co/docs/transformers/continuous_batching (accessed 2026-11-09)
[^s6]: Hugging Face, "PagedAttention", Text Generation Inference documentation. https://huggingface.co/docs/text-generation-inference/conceptual/paged_attention (accessed 2026-11-09)
