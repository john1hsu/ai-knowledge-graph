---
id: kt:gptq
type: Algorithm
title: GPTQ
aliases: [GPTQ quantization, GPTQ algorithm]
domain: inference-and-optimization
summary: >-
  A one-shot post-training weight-quantization algorithm for large transformer language models that rounds each
  layer's weights to 3 or 4 bits column by column while using approximate second-order (Hessian) information to
  update the not-yet-quantized weights and compensate for rounding error, using only a small calibration set.
maturity: established
broader: [kt:quantization, kt:post-training-quantization]
related: [kt:large-language-model, kt:awq, kt:model-serving, kt:model-compression]
relations:
  - {predicate: introducedIn, object: kt:gptq-accurate-post-training-quantization-for-generative-pre-trained-transformers}
  - {predicate: basedOn, object: kt:optimal-brain-compression}
  - {predicate: usedIn, object: kt:large-language-model}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: alternativeTo, object: kt:awq}
  - {predicate: enables, object: kt:model-serving}
sources:
  - id: s1
    title: "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"
    publisher: ICLR 2023 (Frantar, Ashkboos, Hoefler and Alistarh), authors' arXiv version 2210.17323
    url: https://arxiv.org/pdf/2210.17323
    type: primary
    accessed: 2026-11-10
  - id: s2
    title: "Optimal Brain Compression: A Framework for Accurate Post-Training Quantization and Pruning"
    publisher: NeurIPS 2022, Advances in Neural Information Processing Systems 35 (Frantar and Alistarh)
    url: https://proceedings.neurips.cc/paper_files/paper/2022/hash/1caf09c9f4e6b0150b06a07e77f2710c-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s3
    title: "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration"
    publisher: MLSys 2024 (Lin, Tang, Tang, Yang, Chen, Wang, Xiao, Dang, Gan and Han), authors' arXiv version 2306.00978
    url: https://arxiv.org/html/2306.00978
    type: primary
    accessed: 2026-11-10
  - id: s4
    title: "GPTQ"
    publisher: Hugging Face Transformers documentation
    url: https://huggingface.co/docs/transformers/en/quantization/gptq
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# GPTQ

**GPTQ** is a post-training quantization (PTQ) algorithm that compresses the weights of large generative transformers to 3 or 4 bits in a single pass, without retraining.[^s1] It was introduced by Elias Frantar (IST Austria), Saleh Ashkboos and Torsten Hoefler (ETH Zurich) and Dan Alistarh (IST Austria and Neural Magic), posted to arXiv in October 2022 and published at ICLR 2023.[^s1] Its headline result was that 175-billion-parameter models such as OPT-175B and BLOOM-176B could be quantized in about four GPU hours with only a small rise in perplexity, where simple round-to-nearest (RTN) quantization collapsed at 3 bits.[^s1] Pre-quantized GPTQ checkpoints are now commonly shared on the Hugging Face Hub, and the method is a standard option in the Transformers library.[^s4]

## Origin: from Optimal Brain Surgeon to OBQ

GPTQ descends from a line of second-order compression methods. Frantar and Alistarh's NeurIPS 2022 paper *Optimal Brain Compression* gave an exact, efficient realization of the classical Optimal Brain Surgeon pruning framework and extended it to weight quantization, treating pruning and quantization in one post-training setting that needs only a little calibration data.[^s2] Its quantization variant, Optimal Brain Quantization (OBQ), quantizes weights greedily one at a time and adjusts the remaining weights to compensate, but its cost grows cubically with a layer's input dimension, which made it impractical for billion-parameter models.[^s1]

## How it works

GPTQ solves a **layer-wise reconstruction** problem: for each linear layer with weights *W* and calibration inputs *X*, find quantized weights Ŵ on a fixed grid that minimize the squared output error ‖WX − ŴX‖².[^s1] The Hessian of this objective is proportional to XXᵀ, so it can be computed once per layer from the calibration activations.[^s1] Three changes make the OBQ idea scale:[^s1]

1. **Fixed column order.** The authors found that quantizing columns in a fixed order works about as well as OBQ's greedy order on large layers. Because every row then shares the same order, the inverse-Hessian updates are shared across rows, removing most of the cost.[^s1]
2. **Lazy batch updates.** Columns are processed in blocks of 128; updates inside a block are applied immediately, while the rest of the matrix is updated once per block, which uses GPU memory bandwidth far better.[^s1]
3. **Cholesky reformulation.** Repeated inverse updates became numerically unstable on large models, so GPTQ precomputes the needed inverse-Hessian rows with a Cholesky decomposition, plus mild dampening (about 1% of the mean diagonal added to the Hessian).[^s1]

In the paper, calibration used 128 random 2,048-token segments from the C4 corpus, and models were processed one transformer block at a time, feeding each block the outputs of the already-quantized blocks before it.[^s1] Weights can also be quantized in **groups** (for example, 128 consecutive weights sharing one scale), which improves accuracy at a small storage cost.[^s1]

## Results

On a single NVIDIA A100 80GB, quantizing OPT-175B took about 4.2 hours and BLOOM-176B about 3.8 hours.[^s1] On WikiText2, OPT-175B's perplexity went from 8.34 in FP16 to 8.37 at 4 bits with GPTQ, versus 10.54 with RTN; at 3 bits GPTQ reached 8.68 while RTN diverged.[^s1] The 3-bit OPT-175B fit on one 80GB A100, and with custom kernels that dequantize weights on the fly, per-token latency fell about 3.2x on A100s and 4.5x on A6000s relative to multi-GPU FP16.[^s1]

## Limitations and critiques

The authors note that the speedups come from moving fewer bytes, not from cheaper arithmetic: GPTQ quantizes weights only, activations stay in 16-bit, and mainstream hardware of the time lacked mixed FP16×INT4 matrix-multiply support.[^s1] Because it fits weights to reconstruct calibration outputs, later work argued it can overfit the calibration set. The MLSys 2024 AWQ paper reported that under mismatched calibration and evaluation domains, GPTQ's perplexity rose by 2.3–4.9 points versus 0.5–0.6 for AWQ, and that GPTQ needed a reordering trick for some models such as LLaMA-7B; the AWQ authors also describe the two methods as orthogonal and combinable.[^s3] These comparisons come from a competing method's authors and should be read as such.[^s3]

## In practice

As of November 2026, the Hugging Face Transformers documentation implements GPTQ through the GPT-QModel library, configured with a `GPTQConfig` that sets the bit width, a calibration dataset (C4 by default, or a custom list of strings) and a kernel backend such as Marlin; legacy AutoGPTQ is no longer supported and its checkpoints are not backward compatible with GPT-QModel.[^s4] The docs estimate about five minutes to quantize a 350M-parameter model on a free Colab GPU and about four hours for a 175B model on an A100, and suggest checking the Hub for an existing GPTQ checkpoint first.[^s4]

## Connections

GPTQ is a specific algorithm within **quantization** and, more narrowly, **post-training quantization**, since it needs no gradient-based retraining.[^s1] It was **introduced in** the Frantar et al. paper and is **based on** **Optimal Brain Compression**, whose OBQ procedure it makes tractable at LLM scale.[^s1][^s2] It is **used in** **large language models**, is **implemented in** **Hugging Face Transformers**, and **enables** cheaper **model serving** by fitting large models on fewer GPUs.[^s1][^s4] **AWQ** is its main **alternative** among weight-only LLM quantizers, and both belong to the wider family of **model-compression** methods alongside pruning, which Optimal Brain Compression also covers.[^s2][^s3]

## Sources

[^s1]: Frantar, Ashkboos, Hoefler and Alistarh, "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers", ICLR 2023, arXiv 2210.17323. https://arxiv.org/pdf/2210.17323 (accessed 2026-11-10)
[^s2]: Frantar and Alistarh, "Optimal Brain Compression: A Framework for Accurate Post-Training Quantization and Pruning", NeurIPS 2022. https://proceedings.neurips.cc/paper_files/paper/2022/hash/1caf09c9f4e6b0150b06a07e77f2710c-Abstract.html (accessed 2026-11-10)
[^s3]: Lin et al., "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration", MLSys 2024, arXiv 2306.00978. https://arxiv.org/html/2306.00978 (accessed 2026-11-10)
[^s4]: Hugging Face, "GPTQ", Transformers quantization documentation. https://huggingface.co/docs/transformers/en/quantization/gptq (accessed 2026-11-10)
