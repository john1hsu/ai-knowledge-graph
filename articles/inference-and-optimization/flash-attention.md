---
id: kt:flash-attention
type: Algorithm
title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
aliases: [FlashAttention, flash attention, FlashAttention-2, FlashAttention-3, FlashAttention-4]
domain: inference-and-optimization
summary: >-
  A family of IO-aware GPU kernels that compute exact softmax attention by tiling queries, keys and values
  through fast on-chip SRAM with an online softmax, so the full sequence-by-sequence attention matrix is never
  written to slow high-bandwidth memory; it cuts attention memory to linear in sequence length and speeds up
  both training and inference.
maturity: established
broader: [kt:self-attention, kt:llm-inference-optimization]
related: [kt:transformer-architecture, kt:batching-and-paged-attention]
relations:
  - {predicate: createdBy, object: kt:tri-dao}
  - {predicate: dependsOn, object: kt:high-bandwidth-memory}
  - {predicate: enables, object: kt:context-window}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
sources:
  - id: s1
    title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
    publisher: NeurIPS 2022, Advances in Neural Information Processing Systems 35 (Dao, Fu, Ermon, Rudra and Ré)
    url: https://proceedings.neurips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness (authors' arXiv version)"
    publisher: Dao, Fu, Ermon, Rudra and Ré, arXiv 2205.14135
    url: https://arxiv.org/pdf/2205.14135
    type: primary
    accessed: 2026-11-11
  - id: s3
    title: "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning"
    publisher: Tri Dao, arXiv 2307.08691 (2023)
    url: https://arxiv.org/abs/2307.08691
    type: primary
    accessed: 2026-11-11
  - id: s4
    title: "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision"
    publisher: NeurIPS 2024 (Shah, Bikshandi, Zhang, Thakkar, Ramani and Dao)
    url: https://proceedings.neurips.cc/paper_files/paper/2024/hash/7ede97c3e082c6df10a8d6103a2eebd2-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s5
    title: "FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling"
    publisher: Zadouri, Hoehnerbach, Shah, Liu, Thakkar and Dao, arXiv 2603.05451 (March 2026)
    url: https://arxiv.org/html/2603.05451
    type: primary
    accessed: 2026-11-11
  - id: s6
    title: "Attention backends (AttentionInterface)"
    publisher: Hugging Face Transformers documentation
    url: https://huggingface.co/docs/transformers/main/en/attention_interface
    type: official-docs
    accessed: 2026-11-11
created: 2026-11-11
---

# FlashAttention

FlashAttention is an algorithm for computing exact scaled dot-product attention on GPUs while minimising traffic between the GPU's large but slow high-bandwidth memory (HBM) and its small, fast on-chip SRAM. It was introduced by Tri Dao, Dan Fu, Stefano Ermon, Atri Rudra and Christopher Ré at NeurIPS 2022, who argued that attention research had overlooked "IO-awareness" and that cutting memory reads and writes, not arithmetic, was the route to real wall-clock speedups.[^s1] Unlike sparse or low-rank approximations, it returns the same result as standard attention, so it is a drop-in replacement rather than a modelling change.[^s1][^s2]

## Why standard attention is slow

A naive implementation computes the N×N score matrix S = QKᵀ, writes it to HBM, reads it back to apply softmax, writes the probability matrix P, and reads it again to multiply by V. For long sequences this traffic dominates, because the operation is memory-bound rather than compute-bound.[^s2] The paper illustrates the gap with the NVIDIA A100: 40–80 GB of HBM at roughly 1.5–2.0 TB/s, against 192 KB of SRAM in each of 108 streaming multiprocessors with an estimated 19 TB/s of bandwidth.[^s2]

## How it works

FlashAttention splits Q, K and V into blocks sized to fit in SRAM and fuses the whole attention computation into one kernel. Each K/V block is loaded once while the matching Q blocks are processed against it.[^s2] Softmax normally needs a full row before normalising, so the algorithm keeps two running statistics per row, the maximum m and the sum of shifted exponentials ℓ, and rescales the partial output whenever a new block changes them. This "online softmax" yields exactly softmax(QKᵀ)V without materialising S or P.[^s2]

The backward pass avoids storing the N×N matrices too. Only the output, the statistics m and ℓ, and the dropout random-number state are saved; the needed blocks of S and P are recomputed on-chip. Recomputation adds FLOPs but removes enough HBM traffic that the backward pass still runs faster, and extra memory falls to O(N).[^s2] The authors show standard attention needs Θ(Nd + N²) HBM accesses while FlashAttention needs Θ(N²d²/M) for SRAM size M, and prove that no exact algorithm can do asymptotically better across all SRAM sizes.[^s2] A block-sparse variant skips blocks that a sparsity mask marks as zero, which the paper reports as 2–4× faster than dense FlashAttention.[^s2]

## Results

The original paper reported a 3× speedup training GPT-2 at sequence length 1K, 2.4× on Long-Range Arena (1K–4K), 0.7 lower perplexity on GPT-2, and 6.4 points of lift on long-document classification.[^s1] Because memory no longer grew quadratically, it produced what the authors describe as the first Transformers to beat chance on Path-X (16K tokens, 61.4%) and, with the block-sparse variant, Path-256 (64K tokens, 63.1%).[^s1][^s2]

## Later versions

- **FlashAttention-2 (2023)** cut non-matmul FLOPs, parallelised over sequence length as well as batch and heads, and split work across warps to reduce shared-memory traffic.[^s3]
- It roughly doubled speed, reaching 50–73% of the A100's peak FLOPs/s versus 25–40% for the original, and up to 225 TFLOPs/s per A100 in GPT-style training.[^s3]
- **FlashAttention-3 (NeurIPS 2024)** targeted Hopper GPUs, where FlashAttention-2 used only about 35% of an H100.[^s4]
- It added warp specialisation, interleaved matmul and softmax, and FP8 block quantisation, reporting up to 840 TFLOPs/s in BF16 and 1.3 PFLOPs/s in FP8.[^s4]
- **FlashAttention-4 (arXiv, March 2026)** targets Blackwell GPUs such as the B200, where tensor-core throughput grew faster than shared-memory bandwidth and exponential units.[^s5]
- The authors report up to 1613 TFLOPs/s in BF16 on a B200 (about 71% utilisation), up to 1.3× faster than cuDNN 9.13, using a kernel written entirely in the Python-embedded CuTe-DSL.[^s5]

## Limitations

Each new attention variant has historically needed a hand-written low-level kernel, which takes substantial engineering and may not port across GPU generations; the original authors flagged this and suggested higher-level compilers as future work.[^s2] Each major version has been tuned to a specific NVIDIA architecture, which is why the series has had to be redesigned for Hopper and again for Blackwell.[^s4][^s5] The IO-optimality proof covers a single GPU; multi-GPU IO analysis was left open.[^s2] Speed figures above are the authors' own benchmarks on specific hardware and dates.[^s3][^s4][^s5]

## In practice

As of November 2026, Hugging Face Transformers exposes `flash_attention_2` and `flash_attention_3` as selectable backends alongside PyTorch's built-in scaled dot-product attention, chosen with the `attn_implementation` argument, and offers paged variants of each for serving.[^s6]

## Connections

FlashAttention is an implementation of **self-attention** and a core **LLM inference optimization**, though it speeds up training as well.[^s1] It was created by **Tri Dao** and colleagues and is used inside the **Transformer architecture** without changing the model.[^s1] Its whole design depends on the gap between on-chip SRAM and **high-bandwidth memory**.[^s2] By making memory linear in sequence length it enables longer **context window** lengths.[^s1] It complements **continuous batching and PagedAttention**: paged attention manages the KV cache across requests, and Transformers combines the two as paged FlashAttention backends.[^s6] It is implemented in **Hugging Face Transformers**.[^s6]

## Sources
[^s1]: Dao, Fu, Ermon, Rudra and Ré, "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness", NeurIPS 2022. https://proceedings.neurips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html (accessed 2026-11-11)
[^s2]: Dao et al., "FlashAttention", arXiv 2205.14135. https://arxiv.org/pdf/2205.14135 (accessed 2026-11-11)
[^s3]: Tri Dao, "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning", arXiv 2307.08691. https://arxiv.org/abs/2307.08691 (accessed 2026-11-11)
[^s4]: Shah et al., "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision", NeurIPS 2024. https://proceedings.neurips.cc/paper_files/paper/2024/hash/7ede97c3e082c6df10a8d6103a2eebd2-Abstract.html (accessed 2026-11-11)
[^s5]: Zadouri et al., "FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling", arXiv 2603.05451. https://arxiv.org/html/2603.05451 (accessed 2026-11-11)
[^s6]: Hugging Face, "Attention backends", Transformers documentation. https://huggingface.co/docs/transformers/main/en/attention_interface (accessed 2026-11-11)
