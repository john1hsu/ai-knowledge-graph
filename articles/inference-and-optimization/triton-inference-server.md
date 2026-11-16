---
id: kt:triton-inference-server
type: Tool
title: Triton Inference Server
aliases: [NVIDIA Triton Inference Server, NVIDIA Dynamo-Triton, NVIDIA Dynamo Triton, TensorRT Inference Server]
domain: inference-and-optimization
summary: >-
  NVIDIA's open-source, framework-agnostic inference server, which loads models from a model repository and serves
  them over HTTP/REST, gRPC or an in-process C API, with server-side dynamic and sequence batching, concurrent model
  execution, and pipelines built from ensembles or Business Logic Scripting; renamed NVIDIA Dynamo-Triton in 2025.
maturity: established
broader: [kt:model-serving]
related: [kt:tensorrt-llm, kt:vllm, kt:batching-and-paged-attention, kt:mlops]
relations:
  - {predicate: createdBy, object: kt:nvidia}
  - {predicate: partOf, object: kt:nvidia-dynamo}
  - {predicate: runsOn, object: kt:gpu-computing}
  - {predicate: alternativeTo, object: kt:tensorflow-serving}
  - {predicate: contrastsWith, object: kt:orca-serving-system}
sources:
  - id: s1
    title: "NVIDIA Triton Inference Server (user guide overview)"
    publisher: NVIDIA Triton Inference Server documentation
    url: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs
    type: official-docs
    accessed: 2026-11-16
  - id: s2
    title: "Batchers"
    publisher: NVIDIA Triton Inference Server documentation (user guide, 2670 archive)
    url: https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2670/user-guide/docs/user_guide/batcher.html
    type: official-docs
    accessed: 2026-11-16
  - id: s3
    title: "Business Logic Scripting"
    publisher: NVIDIA Triton Inference Server documentation (user guide, 2670 archive)
    url: https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2670/user-guide/docs/user_guide/bls.html
    type: official-docs
    accessed: 2026-11-16
  - id: s4
    title: "Triton Inference Server Release 20.03"
    publisher: NVIDIA Triton Inference Server release notes
    url: https://docs.nvidia.com/deeplearning/triton-inference-server/release-notes/rel_20-03.html
    type: primary
    accessed: 2026-11-16
  - id: s5
    title: "Orca: A Distributed Serving System for Transformer-Based Generative Models"
    publisher: USENIX OSDI 2022 (Yu, Jeong, Kim, Kim and Chun)
    url: https://www.usenix.org/system/files/osdi22-yu.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s6
    title: "Optimize AI Inference Performance with NVIDIA Full-Stack Solutions"
    publisher: NVIDIA Technical Blog (Comly and Eassa), 24 January 2025, updated 2025
    url: https://developer.nvidia.com/blog/optimize-ai-inference-performance-with-nvidia-full-stack-solutions
    type: lab-research
    accessed: 2026-11-16
created: 2026-11-16
---

# Triton Inference Server

Triton Inference Server is open-source inference serving software from NVIDIA that puts trained models from many frameworks behind a common network interface. Its documentation lists support for models from TensorRT, PyTorch, ONNX, OpenVINO, Python and RAPIDS FIL, plus backends such as TensorRT-LLM and vLLM, and deployment on NVIDIA GPUs, x86 and ARM CPUs and AWS Inferentia, from cloud to edge.[^s1] The project began as the TensorRT Inference Server; release 20.03 (March 2020) states that it is now called Triton Inference Server.[^s4] On 18 March 2025 NVIDIA folded it into its Dynamo platform and renamed it NVIDIA Dynamo Triton, though the user guide still uses the Triton name.[^s6][^s1]

## How it works

Models live in a file-system **model repository**; each model has a configuration that names its backend, inputs and outputs, and a model-management API lets operators load and unload models over HTTP/REST, gRPC or the C API.[^s1] Clients call the server through HTTP/REST or gRPC endpoints that follow the community KServe inference protocol, while embedded or edge applications can link Triton in-process through C and Java APIs.[^s1] The server exports GPU-utilisation, throughput and latency metrics and readiness and liveness endpoints that orchestrators such as Kubernetes can poll.[^s1]

The core of the server is its schedulers. For stateless models the **dynamic batcher** merges requests that arrive separately into one batch: an empty `dynamic_batching { }` block simply forms the largest batch available up to the model's maximum, and `max_queue_delay_microseconds` lets the batcher wait a bounded time for more requests before sending a partial batch.[^s2] Priority levels give separate queues so urgent requests can overtake others, and queue policies can cap queue length or time out requests that wait too long.[^s2] Stateful models, whose requests must reach the same model instance in order, use the **sequence batcher** instead; a provisional "iterative sequence" mode lets the backend reschedule a request every iteration so finished requests can leave early, which the documentation pitches at continuous batching for LLMs.[^s2]

Multi-step workloads are composed in two ways. An **ensemble** wires several models into a pipeline, or more generally a directed acyclic graph, such as preprocessing, a network and postprocessing.[^s3] Because ensembles cannot express loops, conditionals or data-dependent control flow, Triton added **Business Logic Scripting (BLS)** in release 21.08: Python-backend code calls other served models with blocking or asynchronous requests inside its `execute` function.[^s3] The documentation warns that circular calls, such as a model calling itself with no free instance, can deadlock.[^s3]

## Limitations and the LLM shift

Triton's original design separates the serving layer, which queues and batches requests, from the execution engine that runs each batch. The authors of Orca (OSDI 2022) described Triton paired with NVIDIA FasterTransformer as a typical deployment for text generation, and argued that this request-level interface suits generative models poorly.[^s5] Under it, requests that finish early must wait for the whole batch, and new arrivals cannot join a batch already running; Orca's answer was iteration-level scheduling with the scheduler and engine tightly coupled.[^s5] Later backends and the iterative sequence mode move Triton toward that model, but per-iteration scheduling now lives largely inside LLM engines such as TensorRT-LLM and vLLM, which Triton hosts as backends.[^s1][^s2]

## In practice

Triton's breadth of backends makes it a fit when one service must host a mix of model types, such as vision, speech, tabular and language models, behind one protocol, metrics endpoint and batching configuration.[^s1] Since the 2025 rename, newer NVIDIA material refers to it as Dynamo Triton within the Dynamo platform, so practitioners meet both names.[^s6][^s1] Tuning usually centres on the batch-delay and instance-count settings, trading a little queueing latency for higher accelerator utilisation.[^s2]

## Connections

Triton is a concrete implementation of **model serving** and a stage in the broader **MLOps** lifecycle.[^s1] It was **created by** NVIDIA and is now **part of** the NVIDIA Dynamo platform.[^s6] It **runs on** GPU computing hardware above all, and plays the same role as **TensorFlow Serving**, which Orca's authors grouped with it as general-purpose serving systems.[^s1][^s5] It **contrasts with** the **Orca** serving system, whose iteration-level scheduling was a response to Triton-style request-level batching, and it is related to **continuous batching and PagedAttention**, the techniques that grew from that critique.[^s5] **TensorRT-LLM** and **vLLM** plug into Triton as backends for LLM workloads.[^s1]

## Sources
[^s1]: NVIDIA, "NVIDIA Triton Inference Server", user guide. https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs (accessed 2026-11-16)
[^s2]: NVIDIA, "Batchers", Triton user guide. https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2670/user-guide/docs/user_guide/batcher.html (accessed 2026-11-16)
[^s3]: NVIDIA, "Business Logic Scripting", Triton user guide. https://docs.nvidia.com/deeplearning/triton-inference-server/archives/triton-inference-server-2670/user-guide/docs/user_guide/bls.html (accessed 2026-11-16)
[^s4]: NVIDIA, "Triton Inference Server Release 20.03", release notes. https://docs.nvidia.com/deeplearning/triton-inference-server/release-notes/rel_20-03.html (accessed 2026-11-16)
[^s5]: Yu, Jeong, Kim, Kim and Chun, "Orca: A Distributed Serving System for Transformer-Based Generative Models", OSDI 2022. https://www.usenix.org/system/files/osdi22-yu.pdf (accessed 2026-11-16)
[^s6]: Comly and Eassa, "Optimize AI Inference Performance with NVIDIA Full-Stack Solutions", NVIDIA Technical Blog, 2025. https://developer.nvidia.com/blog/optimize-ai-inference-performance-with-nvidia-full-stack-solutions (accessed 2026-11-16)
