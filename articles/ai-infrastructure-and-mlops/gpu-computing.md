---
id: kt:gpu-computing
type: Paradigm
title: GPU computing
aliases: [GPGPU, general-purpose computing on graphics processing units, general-purpose GPU computing, GPU acceleration]
domain: ai-infrastructure-and-mlops
summary: >-
  The use of graphics processing units, throughput-oriented processors with thousands of parallel
  lanes and high-bandwidth memory, for general computation rather than rendering; since the late
  2000s it has been the dominant hardware substrate for training and serving neural networks.
maturity: established
broader: [kt:parallel-computing, kt:ai-hardware]
related: [kt:cuda, kt:high-bandwidth-memory, kt:data-parallelism, kt:roofline-model]
relations:
  - {predicate: enables, object: kt:deep-learning}
  - {predicate: usedIn, object: kt:imagenet-and-alexnet}
  - {predicate: hasPart, object: kt:tensor-cores}
  - {predicate: alternativeTo, object: kt:tpu}
  - {predicate: dependsOn, object: kt:arithmetic-intensity}
sources:
  - id: s1
    title: "A Survey of General-Purpose Computation on Graphics Hardware"
    publisher: Eurographics 2005 State of the Art Reports (Owens, Luebke, Govindaraju, Harris, Krüger, Lefohn, Purcell); NVIDIA Research page
    url: https://research.nvidia.com/publication/2005-08_survey-general-purpose-computation-graphics-hardware
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "GPU Computing"
    publisher: Proceedings of the IEEE 96(5), May 2008 (Owens, Houston, Luebke, Green, Stone, Phillips); UC eScholarship copy
    url: https://escholarship.org/content/qt0cv1p1nc/qt0cv1p1nc.pdf?t=owljow
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s3
    title: "Large-scale Deep Unsupervised Learning using Graphics Processors"
    publisher: ICML 2009 (Raina, Madhavan, Ng)
    url: https://icml.cc/imls/conferences/2009/papers/218.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "GPU Performance Background User's Guide"
    publisher: NVIDIA Deep Learning Performance documentation
    url: https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html
    type: official-docs
    accessed: 2026-11-12
  - id: s5
    title: "Understanding GPU performance"
    publisher: AMD ROCm HIP documentation
    url: https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html
    type: official-docs
    accessed: 2026-11-12
created: 2026-11-12
---

# GPU computing

**GPU computing**, also called **GPGPU** (general-purpose computation on graphics processing units), is the practice of running non-graphics workloads on graphics processors. A 2005 Eurographics survey by Owens and colleagues described the field as a response to graphics hardware becoming both much faster and programmable enough to be an attractive platform for demanding computation, and it catalogued techniques for mapping general algorithms onto that hardware.[^s1] Today the paradigm underlies nearly all large-scale neural-network training and inference.

## Origin: from shaders to compute APIs

GPUs began as fixed-function rendering pipelines. Programmable vertex and fragment stages replaced the fixed units, shader models added 32-bit integer and floating-point arithmetic and dynamic control flow, and unified shader architectures (AMD's Xenos in the Xbox 360, 2005, then flagship AMD and NVIDIA parts) merged the programmable stages into one pool of data-parallel processors.[^s2] Early GPGPU work had to disguise computation as graphics: arrays were stored as textures and kernels written as fragment shaders, which imposed 2D layout limits and made scattered writes awkward.[^s2] Stream languages such as BrookGPU and Sh hid some of this, and in 2006–2007 vendors shipped compute-oriented interfaces, AMD's CTM and NVIDIA's CUDA, with direct memory access, pointers, shared memory and thread synchronization.[^s2] The 2008 *Proceedings of the IEEE* review by Owens et al. reported that a GeForce 8800 GTX of 2006 could sustain over 330 GFLOPS and more than 80 GB/s of memory bandwidth, and cited application speedups such as a roughly 20x gain for molecular-dynamics force calculations over one CPU core.[^s2]

## How it works

The defining design choice is throughput over latency. Owens et al. contrast CPUs, optimized for low latency on a few threads, with GPUs that devote most of their resources to arithmetic and keep many operations in flight at once.[^s2] Programs follow a single-program, multiple-data style: many threads run the same kernel, grouped into blocks, and branches that diverge within a group force both paths to execute, so coherent control flow performs best.[^s2] A modern NVIDIA GPU is organized as many streaming multiprocessors (SMs) fed from high-bandwidth DRAM through a shared L2 cache; NVIDIA's guide cites the A100 with 108 SMs, a 40 MB L2, 80 GB of HBM2 at up to 2039 GB/s, and dense Tensor Core peaks of 312 FP16 TFLOPS.[^s4] AMD's equivalent units are compute units executing 64-thread wavefronts on its CDNA GPUs.[^s5]

Whether a kernel benefits depends on **arithmetic intensity**, the ratio of operations to bytes moved. An operation whose intensity exceeds the processor's ops-per-byte ratio is math-limited; below it, memory-limited.[^s4] NVIDIA's examples show a linear layer at batch size 512 reaching about 315 FLOPS per byte, while the same layer at batch size 1, a ReLU (0.25) or layer normalization (under 10) are memory-limited.[^s4] AMD's documentation frames the same trade-off as a roofline plot, with a compute roof, a slanted bandwidth roof and a ridge point between them.[^s5] GPUs hide memory latency by switching among many resident warps, which is why a launch needs far more threads than there are cores; NVIDIA suggests roughly four times as many thread blocks as SMs, and warns of a "tail effect" when the last wave of blocks leaves most SMs idle.[^s4][^s5]

## Adoption in machine learning

Raina, Madhavan and Ng argued at ICML 2009 that GPUs suit neural-network training because its stochastic, sequential updates resist coarse map-reduce parallelism but expose fine-grained parallelism within each update.[^s3] On a GeForce GTX 280 they reported deep-belief-network training up to about 70x faster than a dual-core CPU, cutting a 100-million-parameter, four-layer model from weeks to about a day, and 5–15x speedups for sparse coding.[^s3] They also identified host-to-device transfer as the main bottleneck and kept parameters resident in GPU memory, moving examples in large batches, a pattern still standard.[^s3] Three years later AlexNet's two-GPU ImageNet result made the approach mainstream.

## Limitations and practical gotchas

Peak FLOPS figures are rarely reached: many common layers are memory-bound, and AMD notes that few kernels hit either roof because of overhead, latency and divergence.[^s5] Small batches, as in single-request LLM decoding, push work toward the memory-limited regime.[^s4] Raising occupancy helps latency hiding only up to a point, after which register and local-memory pressure can hurt.[^s5] Hardware figures above are vendor-published specifications for particular products and change with each generation.[^s4]

## Connections

GPU computing is a branch of **parallel computing** and a core part of **AI hardware**.[^s2] It rose with compute platforms such as **CUDA**[^s2] and relies on **high-bandwidth memory** to feed its arithmetic units.[^s4] It **enables deep learning** at scale,[^s3] was **used in AlexNet's ImageNet** breakthrough, and modern GPUs include **tensor cores** for matrix math.[^s4] Performance analysis rests on **arithmetic intensity** and the **roofline model**.[^s4][^s5] Multi-GPU training extends it through **data parallelism**, and Google's **TPU** is a purpose-built alternative accelerator.

## Sources
[^s1]: Owens, Luebke, Govindaraju, Harris, Krüger, Lefohn, Purcell, "A Survey of General-Purpose Computation on Graphics Hardware", Eurographics 2005 STAR. https://research.nvidia.com/publication/2005-08_survey-general-purpose-computation-graphics-hardware (accessed 2026-11-12)
[^s2]: Owens, Houston, Luebke, Green, Stone, Phillips, "GPU Computing", Proceedings of the IEEE 96(5), 2008. https://escholarship.org/content/qt0cv1p1nc/qt0cv1p1nc.pdf?t=owljow (accessed 2026-11-12)
[^s3]: Raina, Madhavan, Ng, "Large-scale Deep Unsupervised Learning using Graphics Processors", ICML 2009. https://icml.cc/imls/conferences/2009/papers/218.pdf (accessed 2026-11-12)
[^s4]: NVIDIA, "GPU Performance Background User's Guide". https://docs.nvidia.com/deeplearning/performance/dl-performance-gpu-background/index.html (accessed 2026-11-12)
[^s5]: AMD, "Understanding GPU performance", ROCm HIP documentation. https://rocm.docs.amd.com/projects/HIP/en/latest/understand/performance_optimization.html (accessed 2026-11-12)
