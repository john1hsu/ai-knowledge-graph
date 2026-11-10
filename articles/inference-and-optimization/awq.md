---
id: kt:awq
type: Algorithm
title: AWQ
aliases: [activation-aware weight quantization, AWQ quantization]
domain: inference-and-optimization
summary: >-
  A post-training, weight-only quantization method for large language models that finds the small fraction of
  salient weight channels by looking at activation magnitudes and protects them with per-channel scaling before
  rounding, compressing weights to 4 or 3 bits without backpropagation or weight reconstruction.
maturity: established
broader: [kt:quantization, kt:post-training-quantization]
related: [kt:gptq, kt:large-language-model, kt:model-serving, kt:vllm, kt:vision-language-model]
relations:
  - {predicate: introducedIn, object: kt:awq-activation-aware-weight-quantization-for-llm-compression-and-acceleration}
  - {predicate: alternativeTo, object: kt:gptq}
  - {predicate: usedIn, object: kt:large-language-model}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: implementedIn, object: kt:vllm}
  - {predicate: enables, object: kt:model-serving}
sources:
  - id: s1
    title: "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration"
    publisher: Lin, Tang, Tang, Yang, Chen, Wang, Xiao, Dang, Gan and Han; authors' arXiv version 2306.00978v5
    url: https://arxiv.org/html/2306.00978v5
    type: primary
    accessed: 2026-11-10
  - id: s2
    title: "AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration"
    publisher: Proceedings of Machine Learning and Systems 6 (MLSys 2024), pp. 87-100
    url: https://proceedings.mlsys.org/paper_files/paper/2024/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s3
    title: "AWQ project page"
    publisher: MIT HAN Lab
    url: https://hanlab.mit.edu/projects/awq
    type: academic
    accessed: 2026-11-10
  - id: s4
    title: "AWQ"
    publisher: Hugging Face Transformers documentation (v5.13.0)
    url: https://huggingface.co/docs/transformers/v5.13.0/quantization/awq
    type: official-docs
    accessed: 2026-11-10
  - id: s5
    title: "AutoAWQ"
    publisher: vLLM documentation (v0.7.1)
    url: https://docs.vllm.ai/en/v0.7.1/features/quantization/auto_awq.html
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# AWQ

**AWQ (Activation-aware Weight Quantization)** is a low-bit, weight-only post-training quantization method for large language models (LLMs). It rests on the observation that weights are not equally important: protecting roughly 1% of the most salient weights sharply reduces quantization error, and those weights are best identified from the activations that flow into them rather than from the weights themselves.[^s2] Instead of keeping the salient weights in higher precision, AWQ scales their channels so that ordinary uniform rounding damages them less, and it does so without backpropagation or reconstruction.[^s2]

## Origin

AWQ was developed by Ji Lin, Jiaming Tang, Haotian Tang, Shang Yang, Wei-Ming Chen, Wei-Chen Wang, Guangxuan Xiao, Xingyu Dang, Chuang Gan and Song Han, with affiliations including MIT, Shanghai Jiao Tong University, NVIDIA, Tsinghua University, the MIT-IBM Watson AI Lab and UMass Amherst.[^s1] It first appeared on arXiv in June 2023 and was published in the proceedings of MLSys 2024, volume 6.[^s1][^s2] MIT HAN Lab reports that the paper received the MLSys 2024 Best Paper Award, announced in May 2024.[^s3]

## How it works

**Salient channels come from activations.** In the paper's experiments, keeping just 1% of weight channels in FP16 cut the 3-bit (group size 128) perplexity of OPT-1.3B from 119.00 with plain round-to-nearest (RTN) to 16.91, but only when those channels were chosen by input-activation magnitude; choosing them by weight norm barely beat random selection.[^s1] Channels that see large activations matter more because their errors are amplified downstream.[^s1]

**Scaling instead of mixed precision.** A mixed FP16/INT format is accurate but awkward for hardware kernels, so the authors looked for another way to protect the same channels.[^s1] With group-wise quantization, the step size Δ is set by the largest weight in a group. Multiplying a salient weight by a factor *s* > 1 and dividing its input activation by *s* leaves the layer's output mathematically unchanged and the group's Δ roughly the same, so the relative rounding error on that weight shrinks by about 1/*s*.[^s1] Too large an *s* backfires: on OPT-6.7B, *s* = 2 improved perplexity from 23.54 to 11.92, whereas at *s* = 4 more than a fifth of channels had their step size enlarged, hurting non-salient weights.[^s1]

**A tiny search.** AWQ therefore sets each channel's scale as *s* = *s_X*^α, where *s_X* is the channel's average activation magnitude measured on a small calibration set, and grid-searches the single exponent α in [0, 1] (20 points in the paper) to minimize the quantized layer's output error; weight clipping is also tuned to lower quantization error.[^s1] Because only average activation statistics are collected, there is no gradient step and no fitting of weights to the calibration data.[^s1]

## Evidence and limitations

The paper evaluates mainly INT4 and INT3 weight-only quantization with group size 128. For Llama-2-7B at INT3, it reports WikiText-2 perplexity of 6.24 for AWQ against 6.43 for GPTQ and 6.66 for RTN (FP16: 5.47); at INT4, Llama-2-70B reached 3.41 against an FP16 3.32.[^s1] It also reports near-lossless INT4 results on the Mixtral-8x7B mixture-of-experts model, on instruction-tuned Vicuna models, and on multimodal models such as OpenFlamingo and VILA, which the authors describe as the first quantization of multimodal LMs.[^s1][^s2] The authors argue that avoiding reconstruction makes AWQ less prone than GPTQ to overfitting the calibration set and to distorting other domains.[^s1][^s2]

Limits remain. AWQ compresses weights only, so activations and the KV cache stay in higher precision, and its gains are largest in memory-bound decoding rather than compute-bound prefill.[^s1] Speed depends on kernels: vLLM's documentation (as of v0.7.1) called its AWQ support under-optimized, with lower throughput than the unquantized model, and recommended it mainly when memory is the binding constraint and concurrency is low.[^s5] Hugging Face's guide notes that its fused AWQ modules cannot be combined with FlashAttention2 and that installing AutoAWQ may downgrade the Transformers version.[^s4]

## In practice

The authors paired AWQ with **TinyChat**, an inference engine that fuses on-the-fly dequantization into matrix-multiply kernels; they report more than 3× speedups over the Hugging Face FP16 implementation on desktop and mobile GPUs and running Llama-2-70B on a single 64 GB Jetson Orin.[^s1][^s2] HAN Lab lists adoption by NVIDIA TensorRT-LLM, AMD, Google Vertex AI, Amazon SageMaker, Intel Neural Compressor, FastChat, vLLM, Hugging Face TGI and LMDeploy, and reported over 6 million Hub downloads of AWQ models as of August 2024.[^s3] In Transformers, an AWQ checkpoint is identified by `"quant_method": "awq"` in its config, typically with 4 bits and group size 128, and loads directly with `from_pretrained`.[^s4] vLLM serves such checkpoints with `quantization="awq"`, and its guide shows producing them with the AutoAWQ library, which it says shrinks files by about 70% versus FP16.[^s5]

## Connections

AWQ is a form of **quantization**, specifically **post-training quantization**, applied to the weights of **large language models**.[^s1] It was **introduced in** the MLSys 2024 paper by Lin and colleagues.[^s2] It is a direct **alternative to GPTQ**: both quantize LLM weights to 3–4 bits from a small calibration set, but GPTQ compensates rounding error with second-order weight updates while AWQ rescales salient channels without reconstruction.[^s1] It is **implemented in** Hugging Face Transformers and **vLLM**, and so **enables** memory-efficient **model serving**.[^s4][^s5] Its evaluation on multimodal models links it to **vision-language models**.[^s1]

## Sources

[^s1]: Lin, Tang, Tang, Yang, Chen, Wang, Xiao, Dang, Gan and Han, "AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration", arXiv 2306.00978v5. https://arxiv.org/html/2306.00978v5 (accessed 2026-11-10)
[^s2]: Lin et al., "AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration", Proceedings of Machine Learning and Systems 6 (MLSys 2024), 87-100. https://proceedings.mlsys.org/paper_files/paper/2024/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html (accessed 2026-11-10)
[^s3]: MIT HAN Lab, "AWQ" project page. https://hanlab.mit.edu/projects/awq (accessed 2026-11-10)
[^s4]: Hugging Face Transformers documentation, "AWQ" (v5.13.0). https://huggingface.co/docs/transformers/v5.13.0/quantization/awq (accessed 2026-11-10)
[^s5]: vLLM documentation, "AutoAWQ" (v0.7.1). https://docs.vllm.ai/en/v0.7.1/features/quantization/auto_awq.html (accessed 2026-11-10)
