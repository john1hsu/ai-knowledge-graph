---
id: kt:vllm
type: Tool
title: vLLM
aliases: [vLLM inference engine, vLLM serving engine]
domain: inference-and-optimization
summary: >-
  An open-source, high-throughput and memory-efficient inference and serving engine for large language models,
  created at UC Berkeley around PagedAttention and now a PyTorch Foundation-hosted project that exposes
  OpenAI-compatible APIs across many hardware backends.
maturity: established
broader: [kt:llm-inference-optimization, kt:model-serving]
related: [kt:batching-and-paged-attention, kt:speculative-decoding, kt:quantization, kt:hugging-face-transformers, kt:chatbot-arena]
relations:
  - {predicate: introducedIn, object: kt:efficient-memory-management-for-large-language-model-serving-with-pagedattention}
  - {predicate: createdBy, object: kt:uc-berkeley}
  - {predicate: basedOn, object: kt:pytorch}
  - {predicate: dependsOn, object: kt:kv-cache}
  - {predicate: alternativeTo, object: kt:tensorrt-llm}
  - {predicate: runsOn, object: kt:gpu-computing}
sources:
  - id: s1
    title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
    publisher: Kwon, Li, Zhuang, Sheng, Zheng, Yu, Gonzalez, Zhang and Stoica, SOSP 2023, arXiv 2309.06180
    url: https://arxiv.org/abs/2309.06180
    type: primary
    accessed: 2026-11-13
  - id: s2
    title: "vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention"
    publisher: vLLM project blog (UC Berkeley), 20 June 2023
    url: https://vllm.ai/blog/2023-06-20-vllm
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "vLLM V1: A Major Upgrade to vLLM's Core Architecture"
    publisher: vLLM project blog, 27 January 2025
    url: https://vllm.ai/blog/2025-01-27-v1-alpha-release
    type: official-docs
    accessed: 2026-11-13
  - id: s4
    title: "PyTorch Foundation Welcomes vLLM"
    publisher: PyTorch Foundation blog, 7 May 2025
    url: https://pytorch.org/blog/pytorch-foundation-welcomes-vllm/
    type: official-docs
    accessed: 2026-11-13
  - id: s5
    title: "vLLM V1 guide"
    publisher: vLLM documentation (latest, November 2026)
    url: https://docs.vllm.ai/en/latest/usage/v1_guide/
    type: official-docs
    accessed: 2026-11-13
  - id: s6
    title: "Online serving (OpenAI-compatible server)"
    publisher: vLLM documentation (stable, October 2026)
    url: https://docs.vllm.ai/en/stable/serving/online_serving/
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# vLLM

vLLM is an open-source engine for running large language model (LLM) inference and serving at high throughput with efficient GPU memory use.[^s4] It was built at UC Berkeley by Woosuk Kwon, Zhuohan Li, Ion Stoica, Joseph Gonzalez, Hao Zhang and colleagues, and launched publicly on 20 June 2023 with the slogan "easy, fast, and cheap LLM serving".[^s2] Its founding idea, PagedAttention, was described in a paper presented at SOSP 2023, and the project has since grown into one of the most widely used open serving stacks; in May 2025 it became a hosted project of the PyTorch Foundation.[^s1][^s4]

## Origin

The Berkeley team started from the observation that the key-value (KV) cache, which stores attention keys and values for every token a request has seen, is large, grows unpredictably, and was being badly managed. Their launch post estimated that existing systems wasted 60–80% of KV-cache memory through fragmentation and over-reservation, whereas paging the cache into fixed-size, non-contiguous blocks limited waste to under 4%.[^s2] The accompanying paper reported 2–4× higher throughput than FasterTransformer and Orca at the same latency, with larger gains for longer sequences, bigger models and complex decoding such as beam search.[^s1]

Before the paper, vLLM had already been running in production for LMSYS. The team integrated it into FastChat to serve Vicuna in Chatbot Arena, where, according to the launch post, it handled more than half of requests between April and May 2023, averaged about 30,000 requests a day with peaks of 60,000, and let LMSYS halve the GPUs used for that traffic.[^s2] The same post claimed up to 24× the throughput of Hugging Face Transformers and up to 3.5× that of Text Generation Inference on LLaMA-7B and LLaMA-13B; these are the developers' own 2023 benchmarks on a ShareGPT-derived workload, not independent measurements.[^s2]

## How it works

A vLLM server combines a scheduler, a KV-cache block manager and a model executor. Requests are batched continuously, so new ones join and finished ones leave between decoding steps, and each sequence's cache is addressed through a block table that maps logical blocks to physical GPU blocks allocated on demand.[^s2] Blocks can be shared across sequences with reference counting and copy-on-write, which the 2023 post said cut memory for parallel sampling and beam search by up to 55%.[^s2]

The **V1 engine**, released as an alpha on 27 January 2025, reorganized this core.[^s3] Its scheduler no longer distinguishes prefill from decode: each step simply assigns a number of tokens to each request, which makes chunked prefill, prefix caching and speculative decoding fit one mechanism. Prefix caching became hash-based and on by default, with the authors reporting under 1% throughput loss when nothing is reused. An isolated `EngineCore` process runs only scheduling and model execution, while tokenization, multimodal preprocessing, detokenization and streaming overlap with it in other processes. V1 also leans on `torch.compile` and piecewise CUDA graphs instead of hand-written kernels; the team claimed up to 1.7× higher throughput than the previous engine, mainly from lower CPU overhead.[^s3] By November 2026 the documentation describes the old V0 engine as fully deprecated.[^s5]

## In practice

Users typically launch a model with `vllm serve <model>`, which starts an HTTP server implementing OpenAI-style completions, chat completions and responses endpoints, plus embeddings, reranking, scoring, audio transcription and an Anthropic-style messages route, as of the October 2026 stable documentation.[^s6] A common gotcha is that chat endpoints need a chat template in the model's tokenizer configuration; without one every chat request errors unless a template is supplied with `--chat-template`.[^s6]

The PyTorch Foundation's 2025 announcement listed support for NVIDIA GPUs through Blackwell, AMD GPUs, Google Cloud TPUs, Intel GPUs, CPUs and Gaudi accelerators, AWS Neuron and ARM, with further accelerators added through a plugin system. It also cited pipeline parallelism, chunked prefill, speculative decoding, disaggregated serving, quantization and more than 100 model architectures, and counted over 46,500 GitHub stars and 1,000 contributors as of May 2025.[^s4]

## Limitations

V1 simplified the engine partly by dropping features: the `best_of` sampling parameter, per-request logits processors and GPU-to-CPU KV-cache swapping were removed, most encoder-decoder models other than Whisper moved to plugins, and prefix caching for Mamba-style and hybrid models was still unsupported as of November 2026.[^s5] V1's CUDA graphs also use more GPU memory than V0's, and returned log-probabilities are by default computed before logit post-processing, so they may not match the final sampling distribution.[^s5] Fast release cycles mean flags and endpoints change often, so version-pinned documentation matters.[^s5][^s6]

## Connections

vLLM is a concrete **model-serving** system and a reference implementation of **LLM inference optimization**, its two broader nodes.[^s4] It was **introduced in** the SOSP 2023 PagedAttention paper and **created by** researchers at **UC Berkeley**, and it is the main open implementation of **continuous batching and PagedAttention**, which in turn **depends on** careful management of the **KV cache**.[^s1][^s2] It is **based on PyTorch**, which the Foundation describes as its unified interface across hardware, and it mostly **runs on GPUs** while supporting other accelerators.[^s4] Its features overlap with **speculative decoding** and **quantization**, it loads models from the **Hugging Face Transformers** ecosystem, it first proved itself serving **Chatbot Arena**, and it is the leading open-source **alternative to TensorRT-LLM**.[^s3][^s4][^s2]

## Sources

[^s1]: Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention", SOSP 2023, arXiv:2309.06180. https://arxiv.org/abs/2309.06180 (accessed 2026-11-13)
[^s2]: Kwon et al., "vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention", vLLM blog, 2023-06-20. https://vllm.ai/blog/2023-06-20-vllm (accessed 2026-11-13)
[^s3]: vLLM Team, "vLLM V1: A Major Upgrade to vLLM's Core Architecture", vLLM blog, 2025-01-27. https://vllm.ai/blog/2025-01-27-v1-alpha-release (accessed 2026-11-13)
[^s4]: PyTorch Foundation, "PyTorch Foundation Welcomes vLLM", 2025-05-07. https://pytorch.org/blog/pytorch-foundation-welcomes-vllm/ (accessed 2026-11-13)
[^s5]: vLLM documentation, "V1 guide" (latest, updated 2026-11-02). https://docs.vllm.ai/en/latest/usage/v1_guide/ (accessed 2026-11-13)
[^s6]: vLLM documentation, "Online serving" (stable, updated 2026-10-24). https://docs.vllm.ai/en/stable/serving/online_serving/ (accessed 2026-11-13)
