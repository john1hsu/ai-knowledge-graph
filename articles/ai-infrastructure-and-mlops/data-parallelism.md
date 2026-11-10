---
id: kt:data-parallelism
type: Technique
title: Data parallelism
aliases: [data-parallel training, distributed data parallel, DDP]
domain: ai-infrastructure-and-mlops
summary: >-
  A way to scale neural-network training in which every device holds a full replica of the model,
  processes a different slice of each minibatch, and averages gradients with its peers (typically via
  all-reduce) so that all replicas take the same optimizer step.
maturity: established
broader: [kt:distributed-training, kt:parallel-computing]
related: [kt:gpu-computing, kt:cuda, kt:batch-normalization, kt:zero-redundancy-optimizer]
relations:
  - {predicate: contrastsWith, object: kt:model-parallelism}
  - {predicate: basedOn, object: kt:stochastic-gradient-descent}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: dependsOn, object: kt:all-reduce}
sources:
  - id: s1
    title: "13.5. Training on Multiple GPUs"
    publisher: Dive into Deep Learning (d2l.ai), v1.0.3
    url: https://www.d2l.ai/chapter_computational-performance/multiple-gpus.html
    type: textbook
    accessed: 2026-11-10
  - id: s2
    title: "Large Scale Distributed Deep Networks"
    publisher: NIPS 2012 (Dean, Corrado, Monga, Chen, Devin, Mao, Ranzato, Senior, Tucker, Yang, Le, Ng)
    url: https://papers.nips.cc/paper/2012/hash/6aca97005c68f1206823815f66102863-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s3
    title: "Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour"
    publisher: arXiv:1706.02677 (Goyal, Dollár, Girshick, Noordhuis, Wesolowski, Kyrola, Tulloch, Jia, He), 2017
    url: https://arxiv.org/abs/1706.02677
    type: primary
    accessed: 2026-11-10
  - id: s4
    title: "PyTorch Distributed: Experiences on Accelerating Data Parallel Training"
    publisher: arXiv:2006.15704 (Li et al.), VLDB 2020
    url: https://arxiv.org/abs/2006.15704v1
    type: primary
    accessed: 2026-11-10
  - id: s5
    title: "torch.nn.parallel.DistributedDataParallel (PyTorch 2.2)"
    publisher: PyTorch documentation
    url: https://docs.pytorch.org/docs/2.2/generated/torch.nn.parallel.DistributedDataParallel.html
    type: official-docs
    accessed: 2026-11-10
  - id: s6
    title: "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models"
    publisher: arXiv:1910.02054 (Rajbhandari, Rasley, Ruwase, He), Microsoft
    url: https://ar5iv.labs.arxiv.org/html/1910.02054
    type: primary
    accessed: 2026-11-10
created: 2026-11-10
---

# Data parallelism

Data parallelism is the most common way to spread the training of a neural network over several accelerators. Every device keeps a complete copy of the model; each minibatch is cut into shards, one per device; each device computes the loss and gradients on its own shard; and the gradients are combined so every replica applies the identical update. *Dive into Deep Learning* contrasts it with splitting the network by layers or splitting each layer's work across devices, and calls the data-partitioning approach the simplest one, usable in any situation, because devices need to synchronize only once per minibatch.[^s1]

## How it works

One synchronous data-parallel step on *k* devices runs as follows: split the minibatch into *k* parts, run forward and backward passes locally, sum the per-device gradients with an all-reduce, and let each device update its own parameters with the aggregated gradient.[^s1] Because the gradient of a sum of per-example losses is the sum of per-shard gradients, the result matches what one device would compute on the whole minibatch, so the method changes how fast training runs rather than what it computes. The textbook notes two practical consequences: the global minibatch usually grows *k*-fold so each device stays busy, and batch normalization needs care because its statistics are computed per device.[^s1]

An early, asynchronous variant came from Google's DistBelief system. Its Downpour SGD ran many model replicas in parallel and exchanged updates through a central parameter server, which let the team train networks with billions of parameters on tens of thousands of CPU cores.[^s2] Modern GPU training mostly uses the synchronous all-reduce form described above, which avoids the stale gradients that asynchrony introduces.[^s1][^s4]

## Scaling the batch

Larger global batches raise an optimization question: does training still converge to the same accuracy? Goyal et al. (Facebook, 2017) proposed a *linear scaling rule*, raising the learning rate in proportion to the minibatch size, plus a warmup phase for the unstable early iterations. With these, they trained ResNet-50 on ImageNet with minibatches of 8,192 images on 256 GPUs in about an hour, matched small-batch accuracy, and reported roughly 90% scaling efficiency going from 8 to 256 GPUs.[^s3]

## Engineering: overlapping communication

The naive approach waits for the entire backward pass to finish before communicating. PyTorch's DistributedDataParallel (DDP) instead groups gradients into buckets and launches an all-reduce for each bucket as soon as its gradients are ready, overlapping communication with the rest of the backward pass; it can also skip synchronization on some iterations to accumulate gradients locally. Li et al. report near-linear scaling on 256 GPUs when DDP is configured appropriately (VLDB 2020, PyTorch v1.5).[^s4] The documentation recommends one process per GPU, sets the default bucket size to 25 MB, exposes a `no_sync()` context manager for gradient accumulation, and describes DDP as significantly faster than the older single-process `DataParallel` wrapper.[^s5]

## Limitations

Adding devices to plain data parallelism adds throughput, not capacity: every replica still has to fit the whole model in its own memory.[^s1] Rajbhandari et al. quantify the waste. With mixed-precision Adam, model states cost about 16 bytes per parameter, so a 7.5-billion-parameter model needs roughly 120 GB on every data-parallel device. Their ZeRO method partitions optimizer states, gradients and finally parameters across the data-parallel group. In their analysis the first two stages keep the same communication volume as ordinary data parallelism, while full parameter partitioning costs about 1.5 times as much.[^s6] Large batches also need learning-rate and warmup adjustments to keep accuracy, and the all-reduce becomes a bottleneck when interconnect bandwidth is low relative to compute.[^s3][^s4]

## Connections

Data parallelism is the simplest form of distributed training and a case of general parallel computing.[^s1] It contrasts with model parallelism, which splits the network itself across devices and is the option to reach for when the model no longer fits on one device.[^s1] It is built on minibatch stochastic gradient descent, since the gradient being averaged is the minibatch gradient.[^s3] In practice it is implemented in PyTorch's DDP and depends on an efficient all-reduce collective.[^s4][^s5] ZeRO keeps the data-parallel programming model while removing its memory redundancy, and batch normalization is the layer most directly affected by per-device sharding.[^s1][^s6] It runs mostly on GPUs programmed through CUDA.[^s4]

## Sources
[^s1]: *Dive into Deep Learning*, §13.5 "Training on Multiple GPUs". https://www.d2l.ai/chapter_computational-performance/multiple-gpus.html (accessed 2026-11-10)
[^s2]: Dean et al., "Large Scale Distributed Deep Networks", NIPS 2012. https://papers.nips.cc/paper/2012/hash/6aca97005c68f1206823815f66102863-Abstract.html (accessed 2026-11-10)
[^s3]: Goyal et al., "Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour", 2017. https://arxiv.org/abs/1706.02677 (accessed 2026-11-10)
[^s4]: Li et al., "PyTorch Distributed: Experiences on Accelerating Data Parallel Training", VLDB 2020. https://arxiv.org/abs/2006.15704v1 (accessed 2026-11-10)
[^s5]: PyTorch documentation, `torch.nn.parallel.DistributedDataParallel` (2.2). https://docs.pytorch.org/docs/2.2/generated/torch.nn.parallel.DistributedDataParallel.html (accessed 2026-11-10)
[^s6]: Rajbhandari et al., "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models", arXiv:1910.02054. https://ar5iv.labs.arxiv.org/html/1910.02054 (accessed 2026-11-10)
