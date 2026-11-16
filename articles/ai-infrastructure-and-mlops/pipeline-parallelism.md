---
id: kt:pipeline-parallelism
type: Technique
title: Pipeline parallelism
aliases: [inter-layer parallelism, pipeline model parallelism, pipelined model parallelism]
domain: ai-infrastructure-and-mlops
summary: >-
  A form of model parallelism that partitions a network's layers into sequential stages on different
  accelerators and streams micro-batches through them, so every stage works on a different slice of the
  batch at once and only boundary activations travel between devices.
maturity: established
broader: [kt:model-parallelism, kt:distributed-training]
related: [kt:tensor-parallelism, kt:zero-redundancy-optimizer, kt:activation-checkpointing, kt:large-language-model]
relations:
  - {predicate: partOf, object: kt:distributed-training}
  - {predicate: introducedIn, object: kt:gpipe}
  - {predicate: contrastsWith, object: kt:data-parallelism}
  - {predicate: dependsOn, object: kt:backpropagation}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: enables, object: kt:large-language-model}
sources:
  - id: s1
    title: "GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism"
    publisher: arXiv:1811.06965v5 (Huang, Cheng, Bapna, Firat, Chen, Chen, Lee, Ngiam, Le, Wu, Chen), Google, 2019
    url: https://arxiv.org/abs/1811.06965v5
    type: primary
    accessed: 2026-11-16
  - id: s2
    title: "PipeDream: Generalized Pipeline Parallelism for DNN Training"
    publisher: SOSP 2019 (Narayanan, Harlap, Phanishayee, Seshadri, Devanur, Ganger, Gibbons, Zaharia); copy hosted by UW CSE 550
    url: https://courses.cs.washington.edu/courses/cse550/21au/papers/CSE550.pipedream.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM"
    publisher: SC '21 (Narayanan, Shoeybi, Casper, LeGresley, Patwary, Korthikanti, Vainbrand, Kashinkunti, Bernauer, Catanzaro, Phanishayee, Zaharia)
    url: https://ar5iv.labs.arxiv.org/html/2104.04473
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s4
    title: "Zero Bubble (Almost) Pipeline Parallelism"
    publisher: ICLR 2024 (Qi, Wan, Huang, Lin)
    url: https://proceedings.iclr.cc/paper_files/paper/2024/hash/d5a8e37f38a08c68162452dcba89ae9c-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "Pipeline Parallelism (torch.distributed.pipelining), PyTorch 2.8"
    publisher: PyTorch documentation
    url: https://docs.pytorch.org/docs/2.8/_sources/distributed.pipelining.md.txt
    type: official-docs
    accessed: 2026-11-16
created: 2026-11-16
---

# Pipeline parallelism

Pipeline parallelism trains a network that is too large for one accelerator by cutting its sequence of layers into contiguous *stages*, placing each stage on its own device, and feeding the stages a stream of small micro-batches like an assembly line. Google's GPipe library (Huang et al., 2018–2019) framed it as a task-independent way to scale any model expressible as a sequence of layers, and used it to train a 557-million-parameter AmoebaNet to 84.4% ImageNet top-1 accuracy and a 6-billion-parameter, 128-layer multilingual Transformer.[^s1] Unlike splitting each matrix multiplication across devices, the only traffic between stages is the activation tensor at each partition boundary, which GPipe's authors argued keeps bandwidth from being a bottleneck even without fast interconnects.[^s1]

## How it works

Naively assigning layers to devices leaves all but one device idle at any moment. GPipe fixes this by splitting a mini-batch of size *N* into *M* micro-batches: while stage 2 processes micro-batch 1, stage 1 can already start micro-batch 2. Gradients from all *M* micro-batches are accumulated and applied in one synchronous step, so the update is the same however many partitions are used.[^s1] The idle time while the pipeline fills and drains is the *bubble*. GPipe gives it as O((K−1)/(M+K−1)) for *K* stages and found it negligible once M ≥ 4K.[^s1] Megatron-LM's later analysis expresses the same cost as a bubble fraction of (p−1)/m for *p* stages and *m* micro-batches, so the batch must hold many more micro-batches than there are stages.[^s3]

GPipe also stores only boundary activations and recomputes each stage's forward pass during backpropagation, reducing peak activation memory from O(N×L) to O(N + (L/K)×(N/M)) for an *L*-layer network.[^s1] Batch normalization is computed per micro-batch, with a moving average over the full mini-batch kept for evaluation.[^s1] On a Transformer with 32 micro-batches, GPipe reported normalized throughput of 1.8, 3.4 and 6.3 on 2, 4 and 8 TPU partitions.[^s1]

## Schedules

The order in which stages run forward and backward passes is the main design lever.

- **GPipe (all-forward, all-backward):** runs every micro-batch forward, then every one backward, so activations for all *m* micro-batches must be held at once.[^s3]
- **1F1B (one forward, one backward):** introduced by PipeDream (Microsoft Research, SOSP 2019), each worker alternates one forward and one backward pass in steady state after a warm-up phase.[^s2]
- **PipeDream-Flush:** Megatron-LM's synchronous 1F1B variant keeps GPipe's bubble size but limits in-flight micro-batches to *p*, cutting stored activations.[^s3]
- **Interleaved 1F1B:** each device holds *v* small chunks of layers, shrinking the bubble by a factor of *v* at the cost of roughly *v* times more communication.[^s3]
- **Zero bubble:** Qi et al. (ICLR 2024) split backward into input-gradient and weight-gradient parts to fill idle slots.[^s4]

PipeDream itself was asynchronous: it never flushed the pipeline and used *weight stashing*, keeping the weight version each micro-batch saw in its forward pass so its backward pass computes a valid gradient. That gives bounded staleness, which the authors found reached target accuracy in about as many epochs as data parallelism on their workloads. PipeDream reported up to 5.3× faster time-to-accuracy than data parallelism, for VGG-16 on a cluster with 10 Gbps Ethernet between servers. It also used a profiler and dynamic-programming optimizer to balance stage times, since the slowest stage caps throughput.[^s2] Megatron-LM chose synchronous flushes instead to keep strict optimizer semantics, and its interleaved schedule improved throughput by more than 10% at comparable memory.[^s3] The zero-bubble authors report up to 15% higher throughput than 1F1B at a similar memory limit, and up to 30% with the limit relaxed.[^s4]

## Limitations and practice

The approach has three recurring costs: the bubble, which needs many micro-batches to hide; load imbalance, since stages must take similar time (AmoebaNet scaled sub-linearly in GPipe because its compute was unevenly spread across layers); and engineering effort.[^s1][^s3] PyTorch's documentation notes that pipelining partitions a model's *execution*, not just its weights, which often requires intrusive changes to model code.[^s5] Its `torch.distributed.pipelining` package, still labelled alpha in PyTorch 2.8, offers a manual `PipelineStage` frontend and a tracing frontend that splits a model at marked points. It ships GPipe, 1F1B, interleaved 1F1B, looped-BFS and two zero-bubble schedules.[^s5]

In large language model training, pipeline parallelism is usually one axis of three. Megatron-LM recommends tensor parallelism within a server and pipeline parallelism across servers, where point-to-point traffic is cheaper. With data parallelism on top, it trained a 1-trillion-parameter model on 3,072 GPUs at 502 petaFLOP/s, 52% of theoretical peak (reported in 2021).[^s3]

## Connections

Pipeline parallelism is a kind of model parallelism and one of the three parts of distributed training, alongside tensor parallelism, with which it is combined in Megatron-LM.[^s3] It was introduced for giant networks by GPipe.[^s1] It contrasts with data parallelism, which replicates the whole model rather than splitting it, though PipeDream and Megatron-LM both add data-parallel replicas on top of a pipeline.[^s2][^s3] It depends on backpropagation's layer-by-layer structure, which the zero-bubble schedules split into separate gradient computations.[^s4] GPipe's recomputation of stage activations is a form of activation checkpointing, and like ZeRO-style sharding it targets the memory wall of a single device.[^s1] It is implemented in PyTorch through `torch.distributed.pipelining`, and it enables the training of large language models too big for any one accelerator.[^s3][^s5]

## Sources
[^s1]: Huang et al., "GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism", arXiv:1811.06965v5, 2019. https://arxiv.org/abs/1811.06965v5 (accessed 2026-11-16)
[^s2]: Narayanan et al., "PipeDream: Generalized Pipeline Parallelism for DNN Training", SOSP 2019. https://courses.cs.washington.edu/courses/cse550/21au/papers/CSE550.pipedream.pdf (accessed 2026-11-16)
[^s3]: Narayanan et al., "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM", SC '21. https://ar5iv.labs.arxiv.org/html/2104.04473 (accessed 2026-11-16)
[^s4]: Qi, Wan, Huang and Lin, "Zero Bubble (Almost) Pipeline Parallelism", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/d5a8e37f38a08c68162452dcba89ae9c-Abstract-Conference.html (accessed 2026-11-16)
[^s5]: PyTorch documentation, "Pipeline Parallelism" (`torch.distributed.pipelining`), PyTorch 2.8. https://docs.pytorch.org/docs/2.8/_sources/distributed.pipelining.md.txt (accessed 2026-11-16)
