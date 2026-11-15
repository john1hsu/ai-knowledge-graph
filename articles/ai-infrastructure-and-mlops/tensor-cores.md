---
id: kt:tensor-cores
type: Hardware
title: Tensor Cores
aliases: [Tensor Core, NVIDIA Tensor Cores, sparse Tensor Cores]
domain: ai-infrastructure-and-mlops
summary: >-
  Specialized matrix multiply-accumulate units inside NVIDIA GPU streaming multiprocessors, introduced with the
  Volta architecture in 2017, that compute small fused matrix products (D = A×B + C) in reduced precision and
  supply most of a modern data-centre GPU's deep-learning throughput.
maturity: established
broader: [kt:ai-accelerator]
related: [kt:cuda, kt:quantization, kt:model-pruning, kt:high-bandwidth-memory, kt:tpu, kt:tensorrt-llm]
relations:
  - {predicate: partOf, object: kt:gpu-computing}
  - {predicate: createdBy, object: kt:nvidia}
  - {predicate: enables, object: kt:mixed-precision-training}
  - {predicate: implementedIn, object: kt:cutlass}
  - {predicate: implementedIn, object: kt:transformer-engine}
sources:
  - id: s1
    title: "Tuning CUDA Applications for Volta (Volta Tuning Guide)"
    publisher: NVIDIA CUDA Toolkit documentation (archive 12.3.2)
    url: https://docs.nvidia.com/cuda/archive/12.3.2/volta-tuning-guide/index.html
    type: official-docs
    accessed: 2026-11-15
  - id: s2
    title: "NVIDIA Tensor Core Programmability, Performance & Precision"
    publisher: Markidis, Chien, Laure, Peng, Vetter; IPDPS Workshops 2018, authors' arXiv version 1803.04014
    url: https://arxiv.org/abs/1803.04014v1
    type: primary
    accessed: 2026-11-15
  - id: s3
    title: "Mixed Precision Training"
    publisher: Micikevicius et al. (NVIDIA, Baidu Research), ICLR 2018, authors' arXiv version 1710.03740
    url: https://arxiv.org/abs/1710.03740
    type: primary
    accessed: 2026-11-15
  - id: s4
    title: "NVIDIA Ampere Architecture In-Depth"
    publisher: NVIDIA Technical Blog (Krashinsky, Giroux, Jones, Stam, Ramaswamy), 14 May 2020
    url: https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Dissecting the NVIDIA Hopper Architecture through Microbenchmarking and Multiple Level Analysis"
    publisher: Luo, Fan, Li, Du, Liu, Wang, Chu; extended version of IPDPS 2024 paper, authors' arXiv version 2501.12084v2
    url: https://arxiv.org/html/2501.12084v2
    type: primary
    accessed: 2026-11-15
created: 2026-11-15
---

# Tensor Cores

Tensor Cores are dedicated matrix-math units built into the streaming multiprocessors (SMs) of NVIDIA GPUs. NVIDIA introduced them with the Volta architecture (GV100, compute capability 7.x), where each Tensor Core performs a fused multiply-add on 4×4 matrices, D = A×B + C, and larger matrix operations are assembled from many such steps.[^s1] Because neural-network training and inference are dominated by dense matrix multiplication, in convolutions, fully connected layers and transformer attention and feed-forward blocks, moving that work from general-purpose CUDA cores onto Tensor Cores is the main source of modern GPUs' deep-learning speed.[^s2][^s4]

## How it works

On Volta, the inputs A and B are FP16 matrices, while the accumulators C and D may be FP16 or FP32. When accumulating in FP32, the FP16 products are kept at full precision and summed with single-precision addition, which limits rounding error in long dot products.[^s1] Each GV100 SM contains eight Tensor Cores. Programmers reach them through warp-level matrix operations in the CUDA 9 C++ API: the 32 threads of a warp cooperatively load, multiply-accumulate and store 16×16 matrix tiles.[^s1] Markidis and colleagues at KTH and Oak Ridge describe three programming routes: the CUDA WMMA API, NVIDIA's CUTLASS template library built on WMMA, and cuBLAS GEMM calls. They note that the Tesla V100's 640 Tensor Cores have a theoretical peak of 125 TFLOPS in mixed precision.[^s2] In their 2018 benchmarks the units reached up to 83 TFLOPS, about seven times single-precision and three times half-precision throughput on the same chip. A naive WMMA batched GEMM, by contrast, managed only about 4 TFLOPS, so achieved speed depends heavily on the software path.[^s2]

## Generations

Later architectures widened both the data types and the work per unit. On the Ampere A100 (2020), each third-generation Tensor Core performs 256 FP16/FP32 fused multiply-adds per clock, and an SM's four Tensor Cores together do twice the per-SM work of Volta's eight. They also support BF16, TF32, FP64, INT8, INT4 and binary formats.[^s4] TF32 keeps FP32's 8-bit exponent with a 10-bit mantissa; NVIDIA made it the default for AI training on A100 so that unmodified FP32 code runs on Tensor Cores. NVIDIA lists A100 peaks of 156 TFLOPS for TF32 and 312 TFLOPS for FP16 or BF16 with FP32 accumulation (vendor figures at boost clock, 2020).[^s4] Ampere also added *fine-grained structured sparsity*. If weights are pruned to a 2:4 pattern, with at most two non-zeros in every group of four, sparse Tensor Core instructions skip the zeros and double peak throughput. NVIDIA reports virtually no inference accuracy loss with a train, prune, fine-tune recipe.[^s4]

Hopper's fourth-generation units add FP8 and new asynchronous warp-group `wgmma` instructions. Microbenchmarks by Luo and colleagues (published in 2025, extending their IPDPS 2024 paper) find that only `wgmma` reaches the hardware's full potential: over 95% of peak in dense tests, against about 63% for the older synchronous `mma` path. FP8 roughly doubles FP16 matrix throughput in their tests.[^s5]

## Limitations and open questions

Reduced-precision inputs lose information. Markidis et al. show that the error can be cut substantially, but only by doing extra computation, which matters for scientific HPC codes.[^s2] Deep learning tolerates FP16 largely because of the recipe in Micikevicius et al. (ICLR 2018): keep an FP32 master copy of the weights and scale the loss so that small gradients survive in half precision. The authors report this roughly halves memory use across CNNs, RNNs and GANs.[^s3] Peak numbers also overstate real gains. Luo et al. observe that an H800 hits its power limit and lowers its clock under random inputs. Its sparse `mma` delivered only about 1.42× over dense rather than 2×. In their tests FP8 helped only for large matrices: full transformer layers gained less than 2× and short-sequence Llama inference showed no clear gain over BF16, because softmax, activations and attention stay outside FP8.[^s5] Finally, when Tensor Cores are fast, the bottleneck often moves to feeding them data from memory.[^s5]

## In practice

Most practitioners never write Tensor Core code directly. Matrix multiplies are routed to library kernels, such as cuBLAS GEMM or CUTLASS templates, that use them when data types and shapes allow.[^s2] Turning on mixed precision (FP16 or BF16 with FP32 accumulation) is the standard way to engage them in training; NVIDIA states that this gives up to twice TF32 throughput on A100.[^s4] Inference stacks go further with INT8, FP8 and 2:4-sparse kernels.[^s4][^s5]

## Connections

Tensor Cores are a *part of* the SMs that make up NVIDIA's **GPU computing** platform, which places them under **AI accelerators**; Google's **TPU** is a related design that builds a whole chip around matrix hardware.[^s1][^s4] They are *created by* **NVIDIA** and programmed through **CUDA**, with **CUTLASS** as a key implementation library.[^s2] Their low-precision arithmetic *enables* **mixed-precision training**[^s3] and makes **quantization** to INT8, INT4 and FP8 pay off at inference time, while 2:4 structured sparsity rewards **model pruning**.[^s4] Inference engines such as **TensorRT-LLM** run on them, and Hopper's FP8 path is *implemented in* NVIDIA's **Transformer Engine** library, whose FP8 linear layers Luo et al. benchmark.[^s5] Because fast matrix units shift the bottleneck to data movement, memory bandwidth, the problem **high-bandwidth memory** addresses, decides how much of their peak is usable.[^s5]

## Sources
[^s1]: NVIDIA, "Tuning CUDA Applications for Volta", CUDA Toolkit documentation. https://docs.nvidia.com/cuda/archive/12.3.2/volta-tuning-guide/index.html (accessed 2026-11-15)
[^s2]: Markidis, Chien, Laure, Peng, Vetter, "NVIDIA Tensor Core Programmability, Performance & Precision", IPDPS Workshops 2018, arXiv:1803.04014. https://arxiv.org/abs/1803.04014v1 (accessed 2026-11-15)
[^s3]: Micikevicius et al., "Mixed Precision Training", ICLR 2018, arXiv:1710.03740. https://arxiv.org/abs/1710.03740 (accessed 2026-11-15)
[^s4]: Krashinsky et al., "NVIDIA Ampere Architecture In-Depth", NVIDIA Technical Blog, 14 May 2020. https://developer.nvidia.com/blog/nvidia-ampere-architecture-in-depth (accessed 2026-11-15)
[^s5]: Luo et al., "Dissecting the NVIDIA Hopper Architecture through Microbenchmarking and Multiple Level Analysis", arXiv:2501.12084v2. https://arxiv.org/html/2501.12084v2 (accessed 2026-11-15)
