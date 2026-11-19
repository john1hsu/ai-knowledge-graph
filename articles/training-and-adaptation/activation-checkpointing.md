---
id: kt:activation-checkpointing
type: Technique
title: Activation checkpointing
aliases: [gradient checkpointing, activation recomputation, rematerialization, sublinear memory training]
domain: training-and-adaptation
summary: >-
  A training memory optimization that keeps only a subset of a network's intermediate activations during the forward
  pass and recomputes the discarded ones during backpropagation, trading extra computation for a much smaller
  activation-memory footprint.
maturity: established
broader: [kt:backpropagation, kt:distributed-training]
related: [kt:pipeline-parallelism, kt:tensor-parallelism, kt:sequence-parallelism, kt:zero-redundancy-optimizer, kt:fine-tuning, kt:qlora]
relations:
  - {predicate: introducedIn, object: kt:training-deep-nets-with-sublinear-memory-cost}
  - {predicate: basedOn, object: kt:automatic-differentiation}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: createdBy, object: kt:tianqi-chen}
sources:
  - id: s1
    title: "Training Deep Nets with Sublinear Memory Cost"
    publisher: arXiv 1604.06174 (Chen, Xu, Zhang and Guestrin), 2016
    url: https://arxiv.org/abs/1604.06174v2
    type: primary
    accessed: 2026-11-19
  - id: s2
    title: "Training Deep Nets with Sublinear Memory Cost (full text)"
    publisher: arXiv 1604.06174 (Chen, Xu, Zhang and Guestrin), 2016
    url: https://www.arxiv.org/pdf/1604.06174
    type: primary
    accessed: 2026-11-19
  - id: s3
    title: "Reducing Activation Recomputation in Large Transformer Models"
    publisher: MLSys 2023 (Korthikanti, Casper, Lym, McAfee, Andersch, Shoeybi and Catanzaro; NVIDIA)
    url: https://proceedings.mlsys.org/paper_files/paper/2023/hash/80083951326cf5b35e5100260d64ed81-Abstract-mlsys2023.html
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s4
    title: "torch.utils.checkpoint (PyTorch 2.3 documentation)"
    publisher: PyTorch
    url: https://docs.pytorch.org/docs/2.3/checkpoint.html
    type: official-docs
    accessed: 2026-11-19
  - id: s5
    title: "torch.utils.checkpoint (PyTorch 2.9 documentation source)"
    publisher: PyTorch
    url: https://docs.pytorch.org/docs/2.9/_sources/checkpoint.md.txt
    type: official-docs
    accessed: 2026-11-19
created: 2026-11-19
---

# Activation checkpointing

**Activation checkpointing** (also called gradient checkpointing or activation recomputation) is a way to train deep networks with less memory. Instead of keeping every intermediate activation from the forward pass until backpropagation needs it, the training system stores only selected "checkpoint" tensors and reruns parts of the forward computation during the backward pass to rebuild the rest. The cost is extra compute; the gain is that activation memory, often the dominant memory term when training with long sequences or large batches, can shrink dramatically.[^s1][^s4]

## Origin

The idea predates deep learning. Chen, Xu, Zhang and Guestrin, who brought it to neural network training in 2016, note that dropping intermediate results is known in the automatic differentiation literature as checkpointing, and they cite Griewank and Walther's Revolve algorithm as prior work. Their contribution was to apply the idea systematically to general neural-network computation graphs, both convolutional and recurrent, implemented on top of MXNet.[^s2] Their paper, "Training Deep Nets with Sublinear Memory Cost", showed that an n-layer network can be trained with O(√n) memory at the price of roughly one extra forward pass per mini-batch.[^s1]

## How it works

Backpropagation needs the activations of each layer to compute gradients. Naively these are all held in memory, so memory grows linearly with depth (and with sequence length and batch size). Chen et al. split an n-layer network into k segments, keep only each segment's boundary output, and discard the activations inside segments. During the backward pass each segment is rerun from its stored input to regenerate its internals, then backpropagated. Memory then scales as O(n/k) + O(k); choosing k = √n gives O(√n). Applying the same trick recursively inside segments drives memory down to O(log n), at the cost of O(n log n) extra forward computation.[^s2]

Not every operation needs to be recomputed. Chen et al. keep expensive results such as convolutions and drop cheap ones such as batch normalization, activations and pooling, so the recomputation overhead stays small.[^s2] In their experiments, memory for a 1,000-layer residual network on ImageNet fell from 48 GB to 7 GB with about 30% more running time, and a four-layer LSTM over long unrolled sequences saw more than a fourfold memory reduction.[^s1][^s2]

## Selective recomputation for transformers

For large transformer language models, Korthikanti et al. at NVIDIA (MLSys 2023) argued that recomputing whole layers wastes compute. They proposed **selective activation recomputation**, which recomputes only the parts of each layer that use a lot of memory but little compute, and combined it with sequence parallelism and tensor parallelism. They report that this reduces activation memory by about 5x and cuts the execution-time overhead of recomputation by over 90%; training a 530-billion-parameter GPT-3-style model on 2,240 A100 GPUs reached 54.2% model FLOPs utilization, versus 42.1% with full recomputation (the authors' figures, 2022–2023).[^s3]

## In practice

PyTorch exposes the technique as `torch.utils.checkpoint`. The `checkpoint` function reruns a wrapped segment during backward instead of saving its intermediates, and `checkpoint_sequential` splits a sequential model into a chosen number of segments, saving only each segment's inputs.[^s4] PyTorch offers reentrant and non-reentrant implementations and recommends `use_reentrant=False`; the non-reentrant variant records the autograd graph, supports `torch.autograd.grad`, handles nested inputs and can stop recomputation early once the needed tensors exist.[^s4] Recent versions also expose policies for selective checkpointing, letting users choose which operations to save and which to recompute.[^s5]

One gotcha is randomness: operations such as dropout must produce the same values when recomputed. PyTorch saves and restores RNG state by default, which adds some overhead; turning that off with `preserve_rng_state=False` can make outputs and gradients differ from an uncheckpointed run.[^s5] Moving tensors to a new device inside a checkpointed function can also break determinism, because the RNG bookkeeping cannot anticipate it.[^s5]

## Limitations

Checkpointing does not reduce the memory used by parameters, gradients or optimizer state, only activations, so it is usually combined with other techniques. The extra forward work is a real throughput cost (around 30% in Chen et al.'s experiments), and choosing which tensors to keep is a scheduling problem whose best answer depends on the model and hardware.[^s2][^s3]

## Connections

Activation checkpointing is a refinement of **backpropagation** and is rooted in checkpointing from **automatic differentiation**, which Chen et al. explicitly cite.[^s2] It is a standard ingredient of **distributed training** for large models alongside **tensor parallelism**, **sequence parallelism** and **pipeline parallelism**; Korthikanti et al. show how these parallel schemes reduce the need for recomputation.[^s3] It complements the **Zero Redundancy Optimizer**, which shards parameter and optimizer memory rather than activation memory. It is implemented in **PyTorch**[^s4], and because it trades compute for memory it is a natural companion to memory-constrained **fine-tuning** methods such as **QLoRA**.

## Sources

[^s1]: Chen, Xu, Zhang and Guestrin, "Training Deep Nets with Sublinear Memory Cost", arXiv 1604.06174, 2016. https://arxiv.org/abs/1604.06174v2 (accessed 2026-11-19)
[^s2]: Chen, Xu, Zhang and Guestrin, "Training Deep Nets with Sublinear Memory Cost" (full text), arXiv 1604.06174. https://www.arxiv.org/pdf/1604.06174 (accessed 2026-11-19)
[^s3]: Korthikanti et al., "Reducing Activation Recomputation in Large Transformer Models", MLSys 2023. https://proceedings.mlsys.org/paper_files/paper/2023/hash/80083951326cf5b35e5100260d64ed81-Abstract-mlsys2023.html (accessed 2026-11-19)
[^s4]: PyTorch, "torch.utils.checkpoint", PyTorch 2.3 documentation. https://docs.pytorch.org/docs/2.3/checkpoint.html (accessed 2026-11-19)
[^s5]: PyTorch, "torch.utils.checkpoint", PyTorch 2.9 documentation source. https://docs.pytorch.org/docs/2.9/_sources/checkpoint.md.txt (accessed 2026-11-19)
