---
id: kt:model-pruning
type: Technique
title: Model pruning
aliases: [neural network pruning, weight pruning, network pruning, parameter pruning]
domain: inference-and-optimization
summary: >-
  A model-compression technique that removes weights, neurons, channels or other structures judged unimportant
  from a trained neural network, producing a sparser or smaller model that ideally keeps the original accuracy
  while needing less memory and, when the sparsity pattern suits the hardware, less compute.
maturity: established
broader: [kt:model-compression]
related: [kt:knowledge-distillation, kt:lottery-ticket-hypothesis, kt:regularization, kt:gptq]
relations:
  - {predicate: introducedIn, object: kt:optimal-brain-damage}
  - {predicate: alternativeTo, object: kt:quantization}
  - {predicate: usedIn, object: kt:large-language-model}
  - {predicate: runsOn, object: kt:tensor-cores}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: enables, object: kt:model-serving}
sources:
  - id: s1
    title: "Optimal Brain Damage"
    publisher: NeurIPS 1989 (Advances in Neural Information Processing Systems 2; LeCun, Denker and Solla)
    url: https://papers.nips.cc/paper/1989/hash/6c9882bbac1c7093bd25041881277658-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Learning both Weights and Connections for Efficient Neural Networks"
    publisher: Han, Pool, Tran and Dally, authors' arXiv version 1506.02626 (2015)
    url: https://arxiv.org/abs/1506.02626v3
    type: primary
    accessed: 2026-11-12
  - id: s3
    title: "The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks"
    publisher: Frankle and Carbin, authors' arXiv version 1803.03635 (2018, revised 2019)
    url: https://arxiv.org/html/1803.03635v5
    type: primary
    accessed: 2026-11-12
  - id: s4
    title: "SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot"
    publisher: ICML 2023 (Frantar and Alistarh), authors' arXiv version 2301.00774
    url: https://arxiv.org/abs/2301.00774
    type: primary
    accessed: 2026-11-12
  - id: s5
    title: "What is the State of Neural Network Pruning?"
    publisher: MLSys 2020 (Blalock, Gonzalez Ortiz, Frankle and Guttag)
    url: https://proceedings.mlsys.org/paper_files/paper/2020/hash/6c44dc73014d66ba49b28d483a8f8b0d-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s6
    title: "Accelerating Inference with Sparsity Using the NVIDIA Ampere Architecture and NVIDIA TensorRT"
    publisher: NVIDIA Technical Blog (Pool, Sawarkar and Rodge), July 2021
    url: https://developer.nvidia.com/blog/accelerating-inference-with-sparsity-using-ampere-and-tensorrt/
    type: lab-research
    accessed: 2026-11-12
created: 2026-11-12
---

# Model pruning

**Model pruning** removes parts of a trained neural network (individual weights, neurons, attention heads, convolutional channels or whole layers) that contribute little to its output, leaving a smaller or sparser model. The goal is to keep accuracy close to the dense original while cutting storage, memory traffic and, where the hardware can exploit it, arithmetic. The idea dates to at least 1989, when LeCun, Denker and Solla's *Optimal Brain Damage* proposed deleting unimportant weights to trade network complexity against training error, arguing that smaller networks could generalize better, need fewer training examples and run faster.[^s1]

## How it works

A pruning method answers three questions: what to remove, how to score importance, and how to recover lost accuracy.[^s5]

- **Scoring.** Optimal Brain Damage ranked weights by a saliency derived from second-derivative (Hessian) information about the loss.[^s1] A simpler and common criterion is weight magnitude: the weights closest to zero are assumed least important.[^s3][^s6]
- **Recovery.** Han, Pool, Tran and Dally popularized a train, prune, retrain loop: train the dense network to learn which connections matter, delete the unimportant ones, then fine-tune the survivors. They reported shrinking AlexNet from 61 million to 6.7 million parameters (9x) and VGG-16 from 138 million to 10.3 million (13x) on ImageNet with no loss of accuracy.[^s2]
- **Schedule.** Pruning can be done once (one-shot) or iteratively, removing a fraction of the remaining weights in each round; in the lottery-ticket experiments, iterative pruning found smaller well-performing subnetworks than one-shot pruning.[^s3]

## Unstructured versus structured sparsity

Removing arbitrary individual weights (*unstructured* pruning) gives the highest sparsity for a given accuracy, but the resulting irregular zero pattern is hard to accelerate: it cannot use the vector and matrix instructions of efficient hardware, and standard sparse formats only pay off at very high sparsity.[^s6] *Structured* pruning removes whole channels, heads or blocks, so the remaining model is simply a smaller dense network that ordinary dense kernels can run; the trade-off between pattern regularity and accuracy is a central design choice across pruning methods.[^s5][^s6]

A middle ground is NVIDIA's **2:4 semi-structured sparsity**, introduced with Ampere-generation (A100) Sparse Tensor Cores: in every contiguous group of four weights, two must be zero, giving 50% sparsity with a compact index. NVIDIA lists sparse peak throughput at twice dense (for example 624 versus 312 TOPS for FP16 with FP32 accumulation on A100), but its own measured gain for a sparse ResNeXt-101 in TensorRT 8.0 was up to about 20% in throughput, with up to 36% better performance per watt, as of its 2021 post. The recommended recipe is to prune a converged dense model to the 2:4 pattern by magnitude and retrain with the original schedule; NVIDIA reported matching dense accuracy on ResNet-50, BERT-Large and other models.[^s6]

## Pruning large language models

Retraining a model with hundreds of billions of parameters after pruning is expensive, which motivated one-shot, post-training methods. SparseGPT (Frantar and Alistarh, ICML 2023) prunes OPT-175B and BLOOM-176B to at least 50% sparsity in under 4.5 hours without any retraining, reports only a negligible perplexity increase at 60% unstructured sparsity, extends to 2:4 and 4:8 patterns, and composes with weight quantization.[^s4]

## Evidence, critiques and open questions

The **lottery ticket hypothesis** reframed what pruning reveals. Frankle and Carbin found that dense networks contain subnetworks, often under 10-20% of the original size on MNIST and CIFAR-10, that train in isolation to comparable accuracy when reset to their *original* initial weights; with fresh random initialization the same sparse structures no longer match the dense network.[^s3] This suggests pruning identifies favorable initializations, not only redundant weights.

Evaluation is a persistent weakness. A 2020 meta-analysis of 81 pruning papers concluded that the field lacks standardized benchmarks and metrics, making it hard to tell how much three decades of methods have improved; the authors released ShrinkBench to standardize comparisons.[^s5] Reported parameter-count reductions also often overstate real speedups, because unstructured zeros do not translate into faster kernels.[^s6]

## Connections

Pruning is one branch of **model compression**, alongside **quantization**, which lowers numeric precision rather than removing parameters and can be stacked with it, and **knowledge distillation**, which trains a smaller student instead of cutting the teacher; quantization's compatibility with pruning is shown by SparseGPT.[^s4] It originated in **Optimal Brain Damage**[^s1] and connects to the **lottery ticket hypothesis** about trainable sparse subnetworks.[^s3] Its early motivation of better generalization ties it to **regularization**.[^s1] Hardware support for 2:4 sparsity runs on NVIDIA **Tensor Cores**, with the ASP training library built for **PyTorch**, and smaller models ease **model serving**.[^s6] SparseGPT applies it to **large language models** as a one-shot, post-training method, the same setting as the **GPTQ** quantizer.[^s4]

## Sources
[^s1]: LeCun, Denker and Solla, "Optimal Brain Damage", NeurIPS 1989. https://papers.nips.cc/paper/1989/hash/6c9882bbac1c7093bd25041881277658-Abstract.html (accessed 2026-11-12)
[^s2]: Han, Pool, Tran and Dally, "Learning both Weights and Connections for Efficient Neural Networks", arXiv 1506.02626 (2015). https://arxiv.org/abs/1506.02626v3 (accessed 2026-11-12)
[^s3]: Frankle and Carbin, "The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks", arXiv 1803.03635. https://arxiv.org/html/1803.03635v5 (accessed 2026-11-12)
[^s4]: Frantar and Alistarh, "SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot", ICML 2023, arXiv 2301.00774. https://arxiv.org/abs/2301.00774 (accessed 2026-11-12)
[^s5]: Blalock, Gonzalez Ortiz, Frankle and Guttag, "What is the State of Neural Network Pruning?", MLSys 2020. https://proceedings.mlsys.org/paper_files/paper/2020/hash/6c44dc73014d66ba49b28d483a8f8b0d-Abstract.html (accessed 2026-11-12)
[^s6]: Pool, Sawarkar and Rodge, "Accelerating Inference with Sparsity Using the NVIDIA Ampere Architecture and NVIDIA TensorRT", NVIDIA Technical Blog, 2021. https://developer.nvidia.com/blog/accelerating-inference-with-sparsity-using-ampere-and-tensorrt/ (accessed 2026-11-12)
