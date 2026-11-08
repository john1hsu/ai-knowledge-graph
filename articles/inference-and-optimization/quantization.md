---
id: kt:quantization
type: Technique
title: Quantization
aliases: [model quantization, neural network quantization, low-precision inference, weight quantization]
domain: inference-and-optimization
summary: >-
  A model-compression technique that represents a neural network's weights (and often its activations) with
  low-precision numbers such as 8-bit or 4-bit integers or 8/4-bit floats instead of 16- or 32-bit floats,
  cutting memory and bandwidth and enabling faster integer or low-precision arithmetic at a small cost in accuracy.
maturity: established
broader: [kt:model-compression]
related: [kt:model-pruning, kt:knowledge-distillation, kt:qlora, kt:large-language-model, kt:speculative-decoding]
relations:
  - {predicate: usedIn, object: kt:large-language-model}
  - {predicate: enables, object: kt:model-serving}
  - {predicate: implementedIn, object: kt:tensorrt-llm}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: alternativeTo, object: kt:model-pruning}
sources:
  - id: s1
    title: "Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference"
    publisher: CVPR 2018 (Jacob, Kligys, Chen, Zhu, Tang, Howard, Adam and Kalenichenko), authors' arXiv version 1712.05877
    url: https://arxiv.org/pdf/1712.05877
    type: primary
    accessed: 2026-10-31
  - id: s2
    title: "LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale"
    publisher: Dettmers, Lewis, Belkada and Zettlemoyer, arXiv 2208.07339 (2022)
    url: https://arxiv.org/abs/2208.07339v2
    type: primary
    accessed: 2026-10-31
  - id: s3
    title: "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers"
    publisher: Frantar, Ashkboos, Hoefler and Alistarh, arXiv 2210.17323 (2022, revised 2023)
    url: https://arxiv.org/abs/2210.17323v2
    type: primary
    accessed: 2026-10-31
  - id: s4
    title: "Selecting a quantization method"
    publisher: Hugging Face Transformers documentation
    url: https://huggingface.co/docs/transformers/quantization/selecting
    type: official-docs
    accessed: 2026-10-31
  - id: s5
    title: "Optimizing LLMs for Performance and Accuracy with Post-training Quantization"
    publisher: NVIDIA Technical Blog (Alvarez, Mao, Chen and Almog), August 2025, updated March 2026
    url: https://developer.nvidia.com/blog/optimizing-llms-for-performance-and-accuracy-with-post-training-quantization
    type: lab-research
    accessed: 2026-10-31
created: 2026-10-31
---

# Quantization

**Quantization** is the practice of storing and computing a trained neural network with fewer bits per number than the 32-bit or 16-bit floating point used in training. Weights, and often activations, are mapped onto a small grid of values such as 8-bit integers, so the model occupies less memory, moves less data, and can use cheaper integer or low-precision hardware arithmetic.[^s1] For 8-bit weights and activations, Jacob et al. report close to a fourfold memory reduction relative to 32-bit floats.[^s1] It has become one of the main levers for deploying large language models on limited hardware.[^s2][^s4]

## How it works

The most common scheme is *affine* (uniform) quantization. A real value *r* is represented by an integer *q* through r = S(q − Z), where the scale *S* is a positive real number and the zero-point *Z* is the integer that stands for real zero.[^s1] Because *Z* is itself a quantized value, real zero is represented exactly, which the authors note matters for operations like zero-padding.[^s1] In Jacob et al.'s design, one (S, Z) pair is shared across each weight or activation array, while biases are kept as 32-bit integers whose scale is the product of the weight and input scales.[^s1]

A simpler symmetric variant drops the zero-point and sets the scale from the largest absolute value α in the data, so that α maps to the top of the b-bit signed range, 2^(b−1) − 1; values are then multiplied by the scale and rounded.[^s5] **Granularity** governs how many values share one scale: a single scale per tensor, one per output channel, or one per small block of weights. Finer granularity tracks local ranges better at some bookkeeping cost; formats such as NVIDIA's NVFP4 and 4-bit AWQ weights use per-block scales.[^s5]

There are two broad ways to obtain a quantized model:

- **Quantization-aware training (QAT).** Training proceeds in floating point, but the forward pass simulates the rounding that inference will apply ("fake quantization"), so the network learns weights that survive it. Jacob et al. fold batch-norm parameters into the weights before quantizing, track activation ranges with moving averages, and delay activation quantization early in training to keep ranges stable.[^s1]
- **Post-training quantization (PTQ).** A finished model is converted directly, usually after running a small calibration set (NVIDIA cites 128–512 samples as typical) to measure activation ranges.[^s5] PTQ dominates for LLMs because retraining billion-parameter models is expensive.[^s3]

## Quantizing large language models

Naive 8-bit quantization breaks down in large transformers. Dettmers et al. found that models develop systematic *outlier features*—a few hidden dimensions with very large magnitudes that dominate attention and prediction quality.[^s2] Their LLM.int8() method uses vector-wise scales for most of the matrix multiplication and routes the outlier dimensions to a 16-bit multiplication, so more than 99.9% of values are still multiplied in 8-bit; it roughly halves inference memory versus 16-bit while preserving accuracy on models up to 175B parameters.[^s2]

Going below 8 bits requires smarter rounding. GPTQ quantizes weights one layer at a time using approximate second-order (Hessian) information to compensate for rounding error, reaching 3 or 4 bits per weight on 175B-parameter models in about four GPU hours.[^s3] The authors report end-to-end speedups over FP16 of about 3.25x on an NVIDIA A100 and 4.5x on an A6000, and that a quantized 175B model fits on a single GPU for generation.[^s3] Related methods include SmoothQuant, which migrates activation outliers into the weights through a mathematically equivalent rescaling, and AWQ, which picks per-channel scales that protect the weights most important to the activations.[^s5]

## Limitations and trade-offs

Quantization is lossy. Jacob et al. measured ImageNet top-1 drops of roughly 1.5–2 points for 8-bit ResNets, in exchange for up to about 50% lower latency on mobile ARM cores for detection models.[^s1] Hugging Face's comparison on Llama 3.1 8B and 70B summarizes the regime as of 2026: 8-bit methods save about 2x memory with accuracy very close to bf16, 4-bit methods about 4x with relatively high accuracy, and sub-4-bit methods show noticeable degradation, especially at 2 bits.[^s4] Calibration-based methods can overfit their calibration data, and memory savings do not automatically produce speedups—that requires kernels and hardware that support the format.[^s4] Practitioners are advised to benchmark accuracy and speed on their own task before deploying.[^s4]

## In practice

As of 2026, the Hugging Face Transformers library exposes several back ends: bitsandbytes for easy on-the-fly 8-bit and 4-bit loading and for QLoRA fine-tuning, GPTQ and AWQ for calibrated 4-bit weights, and torchao, HQQ and others for flexible or calibration-free schemes.[^s4] NVIDIA's Model Optimizer and TensorRT-LLM stack supports FP8, INT8 SmoothQuant, INT4 AWQ and the Blackwell-oriented NVFP4 format; NVIDIA claims NVFP4 delivers up to 2–3x token-generation throughput on several large models while retaining nearly all accuracy—a vendor figure rather than an independent benchmark.[^s5]

## Connections

Quantization is a form of **model compression**, alongside **model pruning** (removing weights rather than shrinking their precision) and **knowledge distillation** (training a smaller student model).[^s1][^s4] It is used heavily for **large language models**, where outlier features make the problem distinctive.[^s2] It enables cheaper **model serving** and is implemented in inference stacks such as **TensorRT-LLM** and the **Hugging Face Transformers** library.[^s4][^s5] It also reaches into training: **QLoRA** fine-tuning, which Hugging Face supports through bitsandbytes, works on a quantized base model so large models can be fine-tuned on consumer GPUs.[^s4]

## Sources

[^s1]: Jacob et al., "Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference", CVPR 2018 (arXiv 1712.05877). https://arxiv.org/pdf/1712.05877 (accessed 2026-10-31)
[^s2]: Dettmers, Lewis, Belkada and Zettlemoyer, "LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale", arXiv 2208.07339. https://arxiv.org/abs/2208.07339v2 (accessed 2026-10-31)
[^s3]: Frantar, Ashkboos, Hoefler and Alistarh, "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers", arXiv 2210.17323. https://arxiv.org/abs/2210.17323v2 (accessed 2026-10-31)
[^s4]: Hugging Face, "Selecting a quantization method", Transformers documentation. https://huggingface.co/docs/transformers/quantization/selecting (accessed 2026-10-31)
[^s5]: Alvarez, Mao, Chen and Almog, "Optimizing LLMs for Performance and Accuracy with Post-training Quantization", NVIDIA Technical Blog, 2025 (updated 2026). https://developer.nvidia.com/blog/optimizing-llms-for-performance-and-accuracy-with-post-training-quantization (accessed 2026-10-31)
