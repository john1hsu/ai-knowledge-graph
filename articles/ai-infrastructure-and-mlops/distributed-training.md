---
id: kt:distributed-training
type: Paradigm
title: Distributed training
aliases: [distributed deep learning, parallel training, multi-GPU training, 3D parallelism]
domain: ai-infrastructure-and-mlops
summary: >-
  Training a single neural network across many accelerators or machines by partitioning the data,
  the layers or the individual weight matrices, and synchronizing gradients and activations over
  collective communication so the devices act as one larger computer.
maturity: established
broader: [kt:parallel-computing]
related: [kt:pretraining, kt:gpu-computing, kt:zero-redundancy-optimizer]
relations:
  - {predicate: hasPart, object: kt:data-parallelism}
  - {predicate: hasPart, object: kt:tensor-parallelism}
  - {predicate: hasPart, object: kt:pipeline-parallelism}
  - {predicate: dependsOn, object: kt:all-reduce}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: enables, object: kt:large-language-model}
sources:
  - id: s1
    title: "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism"
    publisher: arXiv:1909.08053 (Shoeybi, Patwary, Puri, LeGresley, Casper, Catanzaro), NVIDIA, 2019
    url: https://ar5iv.labs.arxiv.org/html/1909.08053
    type: primary
    accessed: 2026-11-13
  - id: s2
    title: "GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism"
    publisher: NeurIPS 2019 (Huang, Cheng, Bapna, Firat, Chen, Chen, Lee, Ngiam, Le, Wu, Chen)
    url: https://papers.nips.cc/paper/2019/file/093f65e080a295f8076b1c5722a46aa2-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM"
    publisher: SC '21 (Narayanan, Shoeybi, Casper, LeGresley, Patwary, Korthikanti, Vainbrand, Kashinkunti, Bernauer, Catanzaro, Phanishayee, Zaharia)
    url: https://ar5iv.labs.arxiv.org/html/2104.04473
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "PyTorch Distributed Overview"
    publisher: PyTorch tutorials (Will Constable)
    url: https://docs.pytorch.org/tutorials/_sources/beginner/dist_overview.rst.txt
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# Distributed training

Distributed training is the practice of spreading the work of training one model over many accelerators, often across many servers, so that the job finishes faster or so that a model too large for any single device can be trained at all. The work can be divided along three axes: the training examples (data parallelism), the layers of the network (pipeline parallelism), or the matrix multiplications inside each layer (tensor parallelism). PyTorch's own overview organizes its tooling the same way, offering replicated data parallelism, fully sharded data parallelism, and tensor and pipeline parallelism that split the model itself.[^s4] Modern large language models are trained by combining all three.[^s3]

## How it works

**Data parallelism** keeps a full copy of the model on each device and averages gradients after every step. It raises throughput but not capacity, because every replica must still hold the whole model; sharded variants remove that redundancy by partitioning model state across the data-parallel group.[^s4]

**Tensor (intra-layer) parallelism** splits individual weight matrices. In Megatron-LM, NVIDIA researchers partitioned a transformer's MLP block by splitting the first matrix multiply by columns and the second by rows, so the nonlinearity runs locally and the block needs just one all-reduce in the forward pass and one in the backward pass. Attention is split by heads in the same spirit, giving four all-reduces per transformer layer in total. The authors stress that the method needs no new compiler, only a few communication operations added in native PyTorch.[^s1]

**Pipeline (inter-layer) parallelism** assigns consecutive groups of layers to different devices. GPipe (Google, NeurIPS 2019) splits each minibatch into *M* micro-batches that flow through *K* pipeline stages, accumulating gradients and applying one synchronous update per minibatch. The price is a "bubble" of idle time of order (K−1)/(M+K−1), which the authors found negligible once M ≥ 4K. GPipe also recomputes activations during the backward pass instead of storing them, cutting activation memory.[^s2]

## Composing the axes

Narayanan et al. (SC '21) combined the three methods into what they call PTD-P. Their guidance follows the hardware: use tensor parallelism inside a server, where fast links can absorb its frequent all-reduces, use pipeline parallelism across servers, where its point-to-point traffic is cheaper, and replicate the resulting model with data parallelism to scale out. They also introduced an interleaved schedule in which each device holds several smaller chunks of layers, shrinking the bubble at the cost of more communication, and they report that poor combinations of tensor and pipeline degrees can cut throughput by up to half.[^s3] PyTorch offers a similar decision path: use replicated data parallelism if the model fits on one GPU, switch to fully sharded data parallelism if it does not, and add tensor or pipeline parallelism when sharding alone stops scaling.[^s4]

## Scale achieved

Megatron-LM trained an 8.3-billion-parameter transformer with 8-way tensor parallelism on 512 V100 GPUs, sustaining 15.1 petaFLOPs, with 76% scaling efficiency against a single-GPU baseline (2019).[^s1] GPipe trained a 6-billion-parameter, 128-layer multilingual transformer covering 103 languages.[^s2] The SC '21 system ran a 1-trillion-parameter GPT model on 3,072 A100 GPUs at 502 petaFLOP/s, 52% of theoretical peak per GPU, and its authors estimated roughly three months of end-to-end training for that model.[^s3] These are the authors' own measurements on their clusters, not general benchmarks.

## Limitations and open questions

Every axis trades memory for communication. Tensor parallelism needs high-bandwidth links and degrades when its all-reduces cross slower inter-server networks; pipeline parallelism wastes time in bubbles and needs many micro-batches to hide them; data parallelism inflates the global batch size.[^s2][^s3] Choosing the degree of each axis is a search problem that depends on model shape and cluster topology, and the wrong choice can halve throughput.[^s3] Underneath all of it sits the communication layer: PyTorch's parallelism modules are built on collective operations such as all-reduce and all-gather plus point-to-point sends, launched across machines with tools such as `torchrun`.[^s4]

## Connections

Distributed training is a branch of parallel computing applied to gradient-based learning.[^s3] It has three parts: data parallelism, tensor parallelism and pipeline parallelism, which Megatron-LM and GPipe introduced or popularized for large networks.[^s1][^s2] Its tensor-parallel and data-parallel forms depend on the all-reduce collective, and it is implemented in PyTorch through DDP, FSDP, and tensor- and pipeline-parallel APIs.[^s1][^s4] Sharded data parallelism, such as PyTorch's FSDP, removes the memory redundancy of plain replication by partitioning model state, the same idea behind ZeRO-style sharded optimizers.[^s4] It is what makes the pretraining of large language models possible, and it runs on clusters of GPUs connected by fast interconnects.[^s3]

## Sources
[^s1]: Shoeybi et al., "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism", arXiv:1909.08053, 2019. https://ar5iv.labs.arxiv.org/html/1909.08053 (accessed 2026-11-13)
[^s2]: Huang et al., "GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism", NeurIPS 2019. https://papers.nips.cc/paper/2019/file/093f65e080a295f8076b1c5722a46aa2-Paper.pdf (accessed 2026-11-13)
[^s3]: Narayanan et al., "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM", SC '21. https://ar5iv.labs.arxiv.org/html/2104.04473 (accessed 2026-11-13)
[^s4]: Constable, "PyTorch Distributed Overview", PyTorch tutorials. https://docs.pytorch.org/tutorials/_sources/beginner/dist_overview.rst.txt (accessed 2026-11-13)
