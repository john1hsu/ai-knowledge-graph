---
id: kt:model-serving
type: Concept
title: "Model serving: deploying trained models behind inference APIs"
aliases: [model serving, inference serving, prediction serving, ML model serving, online inference]
domain: ai-infrastructure-and-mlops
summary: >-
  The systems practice of loading trained models into long-running servers that answer prediction requests
  over a network API, managing versions, batching, hardware placement and latency targets so that models can
  be used by applications in production.
maturity: established
broader: [kt:mlops]
related: [kt:batching-and-paged-attention, kt:quantization, kt:speculative-decoding, kt:llm-inference-optimization, kt:hugging-face-transformers]
relations:
  - {predicate: partOf, object: kt:mlops}
  - {predicate: implementedIn, object: kt:tensorflow-serving}
  - {predicate: implementedIn, object: kt:triton-inference-server}
  - {predicate: implementedIn, object: kt:vllm}
  - {predicate: influencedBy, object: kt:clipper-prediction-serving-system}
  - {predicate: influencedBy, object: kt:orca-serving-system}
  - {predicate: runsOn, object: kt:ai-accelerator}
sources:
  - id: s1
    title: "Clipper: A Low-Latency Online Prediction Serving System"
    publisher: NSDI 2017 (Crankshaw, Wang, Zhou, Franklin, Gonzalez, Stoica), USENIX
    url: https://usenix.org/conference/nsdi17/technical-sessions/presentation/crankshaw
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Clipper: A Low-Latency Online Prediction Serving System (full text)"
    publisher: Crankshaw et al., arXiv 1612.03079
    url: https://arxiv.org/pdf/1612.03079
    type: primary
    accessed: 2026-11-12
  - id: s3
    title: "TensorFlow-Serving: Flexible, High-Performance ML Serving"
    publisher: Olston et al., Google, NIPS 2017 workshop, arXiv 1712.06139
    url: https://arxiv.org/pdf/1712.06139
    type: primary
    accessed: 2026-11-12
  - id: s4
    title: "Dynamic Batching & Concurrent Model Execution (Triton Conceptual Guide, Part 2)"
    publisher: NVIDIA Triton Inference Server documentation
    url: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Conceptual_Guide/Part_2-improving_resource_utilization/README.html
    type: official-docs
    accessed: 2026-11-12
  - id: s5
    title: "Orca: A Distributed Serving System for Transformer-Based Generative Models"
    publisher: OSDI 2022 (Yu, Jeong, Kim, Kim, Chun), USENIX
    url: https://www.usenix.org/conference/osdi22/presentation/yu
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Model serving

**Model serving** (also called inference serving or prediction serving) is the part of the machine-learning lifecycle that takes a trained model and makes it answer requests in production: the model is loaded into a long-running server process, exposed through an RPC or HTTP API, and operated so that applications get predictions that are fast, accurate and available under load. The Berkeley authors of Clipper framed the gap in 2017: most ML frameworks and systems of the time addressed training, not deployment, even though applications need real-time predictions under heavy query load.[^s1]

## Why serving is its own problem

Google's TensorFlow-Serving paper explains why ad-hoc serving code tends to grow complicated. Teams soon need several model versions at once for A/B tests, careful RAM management, isolation so that loading one model does not cause latency spikes for others, asynchronous batching for accelerators, and request routing when a model is too large for one machine. The authors also argue that models differ from ordinary web objects: they contain logic as well as data, vary enormously in size and may be replaced every few minutes.[^s3]

## How serving systems work

- **Model abstraction.** Servers hide framework differences behind one prediction API. Clipper ran each model in its own container behind a common interface and reported that adding a framework (Spark MLlib, scikit-learn, Caffe, TensorFlow, HTK) took under 25 lines of code.[^s2] TensorFlow-Serving treats models as opaque "servables", so its core library is not tied to TensorFlow.[^s3]
- **Versioning and rollout.** TensorFlow-Serving watches storage for new versions and, by default, loads the latest. Canary releases load a new version beside the current one and send it a sample of traffic; rollback switches back to an older version. An availability-preserving policy loads the new version before unloading the old; a resource-preserving policy does the reverse when two copies will not fit in memory.[^s3]
- **Batching.** Accelerators are far more efficient on batches, so servers merge concurrent requests. Clipper's adaptive batching used an additive-increase, multiplicative-decrease rule to find the largest batch that still met a latency objective such as 20 ms.[^s2] NVIDIA's Triton enables a dynamic batcher per model, with a configurable maximum queue delay that trades a little waiting time for fuller batches.[^s4]
- **Concurrency and placement.** Triton can run several instances of one model on a GPU or across GPUs via an `instance_group` setting; its documentation notes that extra instances do not scale linearly.[^s4] In an NVIDIA tutorial example, dynamic batching raised throughput from about 975 to about 3,188 inferences per second while lowering p95 latency, and a second instance raised it to about 4,134.[^s4]
- **Model selection and robustness.** Clipper added a layer that combines or chooses among models using bandit algorithms and returns whatever predictions arrive before a deadline, trading some accuracy for bounded latency.[^s2]

## Serving generative models

Large language models changed the workload: each request runs many decoding iterations and produces a variable-length output. The Orca paper (OSDI 2022) observed that request-level batching makes early-finishing requests wait for the whole batch and makes new requests queue behind it. It proposed scheduling at the granularity of one model iteration, plus selective batching of only some operations, and reported a 36.9× throughput gain over NVIDIA FasterTransformer on GPT-3 175B at the same latency level.[^s5]

## Scale and practice

As of the 2017 paper, TensorFlow-Serving was used by hundreds of Google projects, and Google's total traffic was in the tens of millions of inferences per second; the authors estimated the serving library alone at about 100,000 requests per second per core.[^s3] Today's general-purpose servers such as Triton host many frameworks through backends, including PyTorch, ONNX Runtime, TensorRT, TensorRT-LLM and vLLM, and the right configuration depends on model, hardware, service-level agreements and cost.[^s4] Common open questions remain the trade-off between latency and throughput, multi-tenancy on shared accelerators, and cost control for very large models.[^s3][^s4]

## Connections

Model serving is the deployment stage of the broader **MLOps** lifecycle; TensorFlow-Serving's authors treat versioning, canarying and rollback as part of the serving system itself.[^s3] It is **implemented in** systems such as TensorFlow-Serving, NVIDIA Triton and vLLM, and was **influenced by** research systems like Clipper and Orca.[^s1][^s5] Inference techniques elsewhere in the graph exist largely to make serving cheaper: **continuous batching and PagedAttention**, **quantization** and **speculative decoding** each raise throughput or cut latency per request, and they sit under the umbrella of **LLM inference optimization**; Orca's iteration-level scheduling is the idea that the continuous-batching node builds on.[^s5] Servers **run on** GPUs and other AI accelerators, where batching matters most.[^s4]

## Sources

[^s1]: Crankshaw et al., "Clipper: A Low-Latency Online Prediction Serving System", NSDI 2017. https://usenix.org/conference/nsdi17/technical-sessions/presentation/crankshaw (accessed 2026-11-12)
[^s2]: Crankshaw et al., "Clipper: A Low-Latency Online Prediction Serving System", arXiv 1612.03079. https://arxiv.org/pdf/1612.03079 (accessed 2026-11-12)
[^s3]: Olston et al., "TensorFlow-Serving: Flexible, High-Performance ML Serving", arXiv 1712.06139, 2017. https://arxiv.org/pdf/1712.06139 (accessed 2026-11-12)
[^s4]: NVIDIA, "Dynamic Batching & Concurrent Model Execution", Triton Inference Server documentation. https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Conceptual_Guide/Part_2-improving_resource_utilization/README.html (accessed 2026-11-12)
[^s5]: Yu et al., "Orca: A Distributed Serving System for Transformer-Based Generative Models", OSDI 2022. https://www.usenix.org/conference/osdi22/presentation/yu (accessed 2026-11-12)
