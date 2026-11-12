---
id: kt:tensorrt-llm
type: Tool
title: TensorRT-LLM
aliases: [TensorRT LLM, TRT-LLM]
domain: inference-and-optimization
summary: >-
  NVIDIA's open-source library for optimizing and serving large language model inference on NVIDIA GPUs,
  combining fused attention kernels, in-flight batching, a paged KV cache, low-precision quantization,
  speculative decoding and multi-GPU parallelism behind a Python LLM API.
maturity: established
broader: [kt:llm-inference-optimization, kt:model-serving]
related: [kt:batching-and-paged-attention, kt:quantization, kt:speculative-decoding, kt:flash-attention, kt:triton-inference-server]
relations:
  - {predicate: createdBy, object: kt:nvidia}
  - {predicate: basedOn, object: kt:pytorch}
  - {predicate: influencedBy, object: kt:orca-serving-system}
  - {predicate: runsOn, object: kt:tensor-cores}
  - {predicate: alternativeTo, object: kt:vllm}
  - {predicate: dependsOn, object: kt:cuda}
sources:
  - id: s1
    title: "Overview — TensorRT LLM documentation (1.4.0rc3)"
    publisher: NVIDIA TensorRT-LLM documentation
    url: https://nvidia.github.io/TensorRT-LLM/latest/overview.html
    type: official-docs
    accessed: 2026-11-12
  - id: s2
    title: "NVIDIA TensorRT-LLM Supercharges Large Language Model Inference on NVIDIA H100 GPUs"
    publisher: NVIDIA Technical Blog (Vaidya, Comly, DeLaere, Patel and Oh), 9 September 2023
    url: https://developer.nvidia.com/blog/nvidia-tensorrt-llm-supercharges-large-language-model-inference-on-nvidia-h100-gpus/
    type: lab-research
    accessed: 2026-11-12
  - id: s3
    title: "Optimizing Inference on Large Language Models with NVIDIA TensorRT-LLM, Now Publicly Available"
    publisher: NVIDIA Technical Blog, 19 October 2023
    url: https://developer.nvidia.com/blog/optimizing-inference-on-llms-with-tensorrt-llm-now-publicly-available/
    type: lab-research
    accessed: 2026-11-12
  - id: s4
    title: "Orca: A Distributed Serving System for Transformer-Based Generative Models"
    publisher: OSDI '22, USENIX, pp. 521–538 (Yu, Jeong, Kim, Kim and Chun)
    url: https://www.usenix.org/conference/osdi22/presentation/yu
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s5
    title: "Migration Guide: TensorRT Backend Removed"
    publisher: NVIDIA TensorRT-LLM documentation
    url: https://nvidia.github.io/TensorRT-LLM/latest/legacy/tensorrt-backend-removal.html
    type: official-docs
    accessed: 2026-11-12
  - id: s6
    title: "PyTorch Backend"
    publisher: NVIDIA TensorRT-LLM documentation
    url: https://nvidia.github.io/TensorRT-LLM/latest/legacy/torch.html
    type: official-docs
    accessed: 2026-11-12
created: 2026-11-12
---

# TensorRT-LLM

TensorRT-LLM is an open-source library from NVIDIA for accelerating large language model (LLM) inference on NVIDIA GPUs. It packages the serving-side optimizations that matter most for autoregressive decoding (fused attention kernels, continuous batching, paged key-value cache management, low-precision arithmetic, speculative decoding and model parallelism) behind a high-level Python LLM API that scales from one GPU to multi-node clusters.[^s1] NVIDIA announced it in September 2023 and made it publicly available on GitHub and inside the NeMo framework on 19 October 2023.[^s2][^s3]

## Origin and evolution

At launch, NVIDIA described TensorRT-LLM as the TensorRT deep learning compiler combined with optimized kernels, pre- and post-processing steps and multi-GPU, multi-node communication primitives, exposed through a modular Python API so that developers could add models without deep C++ or CUDA expertise.[^s2] The original workflow had three stages: define the network in the Python API (or use a predefined architecture such as Llama), compile it into a TensorRT engine in which the compiler picks kernels and fuses operations, and execute that engine with a C++ runtime that handles sampling, KV-cache management and request batching, either standalone or behind a Triton Inference Server backend.[^s3]

The project has since moved away from ahead-of-time engines. A PyTorch backend appeared as a beta in version 0.17, and popular models are now defined in native PyTorch code that users can customize.[^s6][^s1] By late 2026 the documentation states that PyTorch is the sole execution backend: the `trtllm-build` engine compiler and checkpoint-conversion scripts were removed, Hugging Face checkpoints load directly, and requesting the old TensorRT backend raises an error.[^s5] Despite the name, then, current TensorRT-LLM no longer depends on building a TensorRT engine; readers of older tutorials should expect the engine-build step to be gone.[^s5]

## How it works

The core runtime idea is **in-flight batching**, NVIDIA's name for iteration-level scheduling. Finished sequences leave the batch and newly arrived requests join it between decoding steps, rather than waiting for the whole batch to complete.[^s2] The technique was formalized in the Orca serving system, which scheduled work per model iteration and applied batching selectively to the operations that tolerate it; on GPT-3 175B its authors reported a 36.9× throughput gain over FasterTransformer at equal latency.[^s4] TensorRT-LLM processes prefill (context) and generation phases together under this scheduler and stores attention keys and values in a **paged KV cache** with block reuse, so memory is allocated in pages rather than one contiguous buffer per request.[^s1][^s3]

On top of scheduling, the library supplies the other standard levers of LLM inference optimization:[^s1]

- **Kernels:** fused attention kernels covering multi-head, multi-query and grouped-query attention, including FlashAttention-style fusions.[^s1][^s2]
- **Quantization:** FP8 on H100-class and later GPUs, which the documentation says can roughly halve memory and double throughput versus 16-bit formats with minimal accuracy loss, and FP4 on Blackwell B200 GPUs.[^s1]
- **Speculative decoding:** EAGLE, multi-token prediction (MTP) and n-gram drafting methods.[^s1]
- **Parallelism:** tensor, pipeline and expert parallelism across GPUs and nodes, plus LoRA adapters, guided decoding, chunked prefill and a beta disaggregated-serving mode.[^s1]

## Performance claims and limitations

Performance figures for TensorRT-LLM come mostly from NVIDIA itself and should be read as vendor benchmarks. In September 2023 NVIDIA reported that, on a CNN/DailyMail summarization workload, H100 GPUs with TensorRT-LLM and in-flight batching delivered up to 8× the GPT-J-6B throughput of A100 GPUs, and up to 4.6× for Llama 2 70B.[^s2] As of the November 2026 documentation, NVIDIA additionally claims record DeepSeek-R1 inference on Blackwell and more than 1,000 tokens per second per user for Llama 4 Maverick on B200, without publishing the full methodology on that page.[^s1] Such numbers mix hardware generations with software gains, so they do not isolate what the library contributes.[^s2]

The main practical constraint is vendor lock-in: the library targets NVIDIA GPUs, and its newest precision formats require specific generations (FP8 on Hopper or later, FP4 on Blackwell).[^s1] Its rapid release cadence also means APIs change; the PyTorch backend was launched with an explicit warning that its interface might change, and the engine-based workflow was later removed outright.[^s6][^s5]

## Connections

TensorRT-LLM is a concrete **model-serving** system and an implementation of **LLM inference optimization** techniques, which places it under both broader nodes.[^s1] It was **created by NVIDIA**, now **builds on PyTorch** as its sole execution backend, and **depends on CUDA** and runs on GPU **tensor cores** for its low-precision kernels.[^s5][^s1] Its in-flight batching was **influenced by the Orca serving system**, and its paged KV cache relates it closely to **batching and paged attention**.[^s4][^s3] It packages **quantization**, **speculative decoding** and **FlashAttention**-style kernels, is commonly served through **Triton Inference Server**, and is an **alternative to vLLM**, the main open-source engine built around the same continuous-batching and paged-cache ideas.[^s1][^s3]

## Sources

[^s1]: NVIDIA, "Overview", TensorRT-LLM documentation (1.4.0rc3, updated 2026-11-03). https://nvidia.github.io/TensorRT-LLM/latest/overview.html (accessed 2026-11-12)
[^s2]: Vaidya et al., "NVIDIA TensorRT-LLM Supercharges Large Language Model Inference on NVIDIA H100 GPUs", NVIDIA Technical Blog, 2023-09-09. https://developer.nvidia.com/blog/nvidia-tensorrt-llm-supercharges-large-language-model-inference-on-nvidia-h100-gpus/ (accessed 2026-11-12)
[^s3]: NVIDIA, "Optimizing Inference on Large Language Models with NVIDIA TensorRT-LLM, Now Publicly Available", NVIDIA Technical Blog, 2023-10-19. https://developer.nvidia.com/blog/optimizing-inference-on-llms-with-tensorrt-llm-now-publicly-available/ (accessed 2026-11-12)
[^s4]: Yu, Jeong, Kim, Kim and Chun, "Orca: A Distributed Serving System for Transformer-Based Generative Models", OSDI '22. https://www.usenix.org/conference/osdi22/presentation/yu (accessed 2026-11-12)
[^s5]: NVIDIA, "Migration Guide: TensorRT Backend Removed", TensorRT-LLM documentation. https://nvidia.github.io/TensorRT-LLM/latest/legacy/tensorrt-backend-removal.html (accessed 2026-11-12)
[^s6]: NVIDIA, "PyTorch Backend", TensorRT-LLM documentation. https://nvidia.github.io/TensorRT-LLM/latest/legacy/torch.html (accessed 2026-11-12)
