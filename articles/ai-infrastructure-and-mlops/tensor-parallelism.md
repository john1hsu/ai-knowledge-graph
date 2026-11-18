---
id: kt:tensor-parallelism
type: Technique
title: Tensor parallelism
aliases: [intra-layer model parallelism, tensor model parallelism, Megatron-style tensor parallelism]
domain: ai-infrastructure-and-mlops
summary: >-
  A form of model parallelism that splits the weight matrices inside each layer across several
  accelerators, so every device computes a slice of each matrix multiplication and the partial results
  are combined with collective communication such as all-reduce.
maturity: established
broader: [kt:model-parallelism, kt:distributed-training]
related: [kt:pipeline-parallelism, kt:data-parallelism, kt:sequence-parallelism, kt:activation-checkpointing, kt:zero-redundancy-optimizer]
relations:
  - {predicate: partOf, object: kt:distributed-training}
  - {predicate: introducedIn, object: kt:megatron-lm-training-multi-billion-parameter-language-models-using-model-parallelism}
  - {predicate: createdBy, object: kt:nvidia}
  - {predicate: dependsOn, object: kt:all-reduce}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: enables, object: kt:large-language-model}
sources:
  - id: s1
    title: "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism"
    publisher: arXiv:1909.08053 (Shoeybi, Patwary, Puri, LeGresley, Casper, Catanzaro), NVIDIA, 2019
    url: https://ar5iv.labs.arxiv.org/html/1909.08053
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM"
    publisher: SC '21 (Narayanan, Shoeybi, Casper, LeGresley, Patwary, Korthikanti, Vainbrand, Kashinkunti, Bernauer, Catanzaro, Phanishayee, Zaharia)
    url: https://ar5iv.labs.arxiv.org/html/2104.04473v4
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "Reducing Activation Recomputation in Large Transformer Models"
    publisher: MLSys 2023 (Korthikanti, Casper, Lym, McAfee, Andersch, Shoeybi, Catanzaro)
    url: https://proceedings.mlsys.org/paper_files/paper/2023/file/80083951326cf5b35e5100260d64ed81-Paper-mlsys2023.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Tensor Parallelism - torch.distributed.tensor.parallel, PyTorch 2.14"
    publisher: PyTorch documentation
    url: https://docs.pytorch.org/docs/2.14/distributed.tensor.parallel.html
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# Tensor parallelism

Tensor parallelism trains or serves a network whose layers are too large for one accelerator by splitting the weight matrices *inside* each layer across a group of devices. Each device holds a shard of every large matrix, computes its share of the matrix multiplication, and exchanges partial results with the others through collective communication. The approach was popularised for Transformers by NVIDIA's Megatron-LM (Shoeybi et al., 2019), which showed it could be written with a few communication primitives in native PyTorch, with no new compiler or library.[^s1] Because it partitions individual operations rather than whole layers, it is often called intra-layer model parallelism, in contrast to the inter-layer split of pipeline parallelism.[^s2]

## How it works

Megatron-LM's scheme exploits the structure of a Transformer block to keep communication to a minimum.[^s1]

- **MLP block:** the first linear layer's weight is split by columns, so each device produces a slice of the hidden activations and can apply GeLU locally with no synchronisation. The second linear layer is split by rows and consumes that slice directly, so only its output needs summing across devices.[^s1]
- **Self-attention block:** the query, key and value projections are split column-wise by attention head, so each device computes whole heads locally; the output projection is split row-wise, again leaving a single sum at the end.[^s1]
- **Embeddings and loss:** the input embedding is partitioned along the vocabulary, and the output projection is fused with the cross-entropy loss so devices exchange per-token scalar losses instead of full vocabulary-sized logits.[^s1]

Two conjugate operators handle the communication: one is an identity in the forward pass and an all-reduce in the backward pass, the other is the reverse. The result is two all-reduces in the forward pass and two in the backward pass per Transformer layer.[^s1] The later Megatron-LM analysis gives the per-device, per-layer volume as 8bsh(t−1)/t for micro-batch size *b*, sequence length *s*, hidden size *h* and tensor-parallel size *t*.[^s2]

## Results and limitations

In 2019 the original paper trained an 8.3-billion-parameter GPT-2-style model with 8-way tensor parallelism inside each server, combined with data parallelism, on 512 V100 GPUs. It sustained 15.1 petaFLOP/s, a scaling efficiency the authors report as 76% (74% in a later section) relative to a single-GPU baseline. That model reached 10.81 perplexity on WikiText-103 and 66.51% accuracy on LAMBADA, both state of the art at the time.[^s1]

The main cost is communication on the critical path: every layer waits on all-reduces, and splitting matrices yields smaller, less efficient matrix multiplications. Tensor parallelism is therefore usually confined to a small group of GPUs joined by high-bandwidth links such as NVLink inside one server.[^s3] Narayanan et al. (SC '21) recommend tensor parallelism up to the number of GPUs per server and pipeline parallelism beyond it. They warn that running it over slower inter-node links can be impractical, and that poor tensor/pipeline combinations can cut throughput by up to 2×.[^s2]

A second limitation concerns memory. Layer norms and dropout are not split by tensor parallelism, so every rank stores full copies of their activations. Korthikanti et al. (MLSys 2023) added *sequence parallelism*, which shards those regions along the sequence dimension and replaces each all-reduce with a reduce-scatter and an all-gather of the same bandwidth. Combined with selective activation recomputation, it cut activation memory by 5× and recomputation overhead by over 90%. They reported 54.2% model FLOPs utilisation for a 530-billion-parameter model on 2,240 A100 GPUs, against 42.1% with full recomputation.[^s3]

## In practice

Large language model training typically uses tensor parallelism as one axis of a "3D" layout. Tensor parallelism runs within a node, pipeline parallelism across nodes, and data parallelism on top to scale throughput.[^s2] PyTorch exposes it natively through `torch.distributed.tensor.parallel`, built on DTensor. As of PyTorch 2.14, `parallelize_module` applies a plan of `ColwiseParallel` and `RowwiseParallel` styles to linear and embedding layers over a one-dimensional device mesh. A `SequenceParallel` style covers LayerNorm, RMSNorm and dropout, and a `loss_parallel` context computes cross-entropy on class-sharded logits. The documentation still labels these APIs experimental.[^s4] A multi-dimensional mesh must be sliced to its tensor-parallel dimension before use, which is how tensor parallelism is composed with data-parallel sharding.[^s4]

## Connections

Tensor parallelism is a kind of model parallelism and one of the three axes of distributed training, alongside pipeline and data parallelism.[^s2] It was introduced for Transformers in the Megatron-LM paper by NVIDIA researchers.[^s1] It depends on the all-reduce collective, which carries every layer's partial sums.[^s1][^s2] It contrasts with data parallelism, which replicates the whole model, and is complemented by pipeline parallelism, which splits layers rather than matrices and tolerates slower links.[^s2] Sequence parallelism extends it to the layer-norm and dropout regions, and pairs with selective activation checkpointing to cut memory.[^s3] Like ZeRO-style sharding, it attacks the memory limit of a single device. It is implemented in PyTorch[^s4] and enables training of large language models whose layers exceed one accelerator's memory.[^s1][^s3]

## Sources
[^s1]: Shoeybi et al., "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism", arXiv:1909.08053, 2019. https://ar5iv.labs.arxiv.org/html/1909.08053 (accessed 2026-11-18)
[^s2]: Narayanan et al., "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM", SC '21. https://ar5iv.labs.arxiv.org/html/2104.04473v4 (accessed 2026-11-18)
[^s3]: Korthikanti et al., "Reducing Activation Recomputation in Large Transformer Models", MLSys 2023. https://proceedings.mlsys.org/paper_files/paper/2023/file/80083951326cf5b35e5100260d64ed81-Paper-mlsys2023.pdf (accessed 2026-11-18)
[^s4]: PyTorch documentation, "Tensor Parallelism - torch.distributed.tensor.parallel", PyTorch 2.14. https://docs.pytorch.org/docs/2.14/distributed.tensor.parallel.html (accessed 2026-11-18)
