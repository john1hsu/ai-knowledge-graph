---
id: kt:cuda
type: Tool
title: CUDA
aliases: [Compute Unified Device Architecture, CUDA Toolkit, CUDA platform]
domain: ai-infrastructure-and-mlops
summary: >-
  NVIDIA's parallel computing platform and programming model for general-purpose computation on its GPUs,
  in which a host program launches kernels executed by a hierarchy of thousands of lightweight threads;
  it is the software layer beneath most deep-learning training and inference.
maturity: established
broader: [kt:gpu-computing, kt:parallel-computing]
related: [kt:deep-learning, kt:distributed-training]
relations:
  - {predicate: createdBy, object: kt:nvidia}
  - {predicate: introducedIn, object: kt:scalable-parallel-programming-with-cuda}
  - {predicate: hasPart, object: kt:cudnn}
  - {predicate: usedIn, object: kt:imagenet-and-alexnet}
sources:
  - id: s1
    title: "CUDA Programming Guide, 1.2 Programming Model (v13.4.2)"
    publisher: NVIDIA CUDA documentation
    url: https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html
    type: official-docs
    accessed: 2026-11-08
  - id: s2
    title: "Scalable Parallel Programming with CUDA"
    publisher: ACM Queue 6(2), March 2008 (Nickolls, Buck, Garland, Skadron); course copy
    url: https://grothoff.org/christian/teaching/2008/4704/scalable_cuda.pdf
    type: primary
    accessed: 2026-11-08
  - id: s3
    title: "cuDNN: Efficient Primitives for Deep Learning"
    publisher: arXiv:1410.0759 (Chetlur et al., NVIDIA / UC Berkeley), 2014
    url: https://arxiv.org/abs/1410.0759
    type: primary
    accessed: 2026-11-08
  - id: s4
    title: "ImageNet Classification with Deep Convolutional Neural Networks"
    publisher: NIPS 2012 (Krizhevsky, Sutskever, Hinton); Duke course copy
    url: https://courses.cs.duke.edu/fall16/compsci527/papers/Krizhevsky%20et%20al%20DNN%20ImageNet%202012.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s5
    title: "CUDA semantics"
    publisher: PyTorch documentation (v2.3)
    url: https://docs.pytorch.org/docs/2.3/notes/cuda.html
    type: official-docs
    accessed: 2026-11-08
  - id: s6
    title: "CUDA Zone"
    publisher: NVIDIA Developer
    url: https://developer.nvidia.com/cuda-zone
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# CUDA

**CUDA** is NVIDIA's platform and programming model for running general-purpose code on its graphics processors. NVIDIA describes it as its platform for accelerated computing, and the CUDA Toolkit bundles a C++ compiler, a runtime library, GPU-accelerated libraries, and debugging and profiling tools; developers can work in C++, Python or Fortran, or indirectly through frameworks such as PyTorch.[^s6] Almost every mainstream deep-learning stack ultimately dispatches its tensor operations to CUDA kernels, which is why the platform sits at the base of the AI infrastructure layer.

## Origin

CUDA was presented to the research community by John Nickolls, Ian Buck, Michael Garland and Kevin Skadron in a 2008 *ACM Queue* article. They framed it as a minimal extension of C and C++ in which a programmer writes a serial host program that calls parallel kernels, and they stated that NVIDIA released CUDA in 2007 for GPUs built on its Tesla architecture, introduced in November 2006 with the GeForce 8800.[^s2] The article argued that mainstream software needed to scale automatically as core counts grew, and it reported application speedups ranging from tens to over a hundred times versus serial CPU code, including a 263x faster MRI reconstruction.[^s2] Those figures were the authors' own 2008 measurements on contemporary hardware.

## How it works

The 2008 design rested on three abstractions: a hierarchy of thread groups, shared memories, and barrier synchronization (the `__syncthreads()` intrinsic).[^s2] The current guide (v13.4.2, September 2026) keeps that model. The CPU and its memory are the *host*, the GPU and its memory the *device*; the host copies data and launches a *kernel*, a function that many threads execute in parallel, each using built-in index variables to pick the data it handles.[^s1] Threads are grouped into *blocks* that run on a single streaming multiprocessor (SM) and can share fast on-chip memory, and blocks form a *grid*; GPUs of compute capability 9.0 and later add optional *clusters* of blocks that can read each other's shared memory.[^s1]

Execution follows SIMT (single instruction, multiple threads): threads run in *warps* of 32, and when threads in a warp take different branches the inactive ones are masked, lowering utilization, so block sizes are recommended in multiples of 32.[^s1] The memory hierarchy runs from per-thread registers through per-block shared memory and per-SM L1 caches to a device-wide L2 and global DRAM.[^s1] Because blocks carry no ordering guarantees and must not depend on one another, the same grid can run on a GPU with one SM or thousands, which is how CUDA programs scale across hardware generations.[^s1]

## Role in deep learning

CUDA became central to AI when researchers began hand-writing GPU kernels for neural networks. The 2012 AlexNet paper trained its network on two NVIDIA GTX 580 3 GB GPUs for five to six days, splitting the kernels of each layer across the two cards, and the authors released their optimized GPU convolution code as cuda-convnet.[^s4] To spare every research group from re-tuning such kernels for each new chip, NVIDIA introduced cuDNN in 2014, a BLAS-like library of deep-learning primitives; its authors reported that integrating it into the Caffe framework sped up a standard model by 36% while cutting memory use.[^s3]

Frameworks now hide most CUDA details. In PyTorch, GPU work is queued asynchronously so the CPU need not wait, operations within a CUDA stream run in order while separate streams may overlap, a caching allocator reuses freed memory, and CUDA graphs replay captured sequences of kernels with far less CPU launch overhead.[^s5]

## Limitations and gotchas

CUDA runs only on NVIDIA GPUs, so code written directly against it is tied to one vendor's hardware. Practitioners hit recurring pitfalls: asynchronous launches make naive timing misleading unless the device is synchronized, errors surface at a later call unless launches are forced to block (`CUDA_LAUNCH_BLOCKING=1`), and memory reported by `nvidia-smi` exceeds what live tensors use because of allocator caching.[^s5] Precision shortcuts also matter: PyTorch's documentation shows TF32 tensor-core math on an A100 giving roughly 7x faster matrix multiplication at the cost of about two orders of magnitude more error than full FP32.[^s5] Branch divergence within a warp and launches whose register demand exceeds an SM's register file are further performance or launch failures at the kernel level.[^s1]

## Connections

CUDA is a specific platform within **GPU computing** and the broader practice of **parallel computing**.[^s2] It was created by **NVIDIA** and introduced to the research literature in *Scalable Parallel Programming with CUDA*.[^s2] **cuDNN** is part of the CUDA library ecosystem that supplies deep-learning primitives,[^s3] and the platform was used in **AlexNet**, the ImageNet result that helped launch modern **deep learning**.[^s4] Frameworks such as **PyTorch** use CUDA as their GPU backend,[^s5] and its matrix math reaches **tensor cores** on recent GPUs.[^s5] Multi-GPU **distributed training** builds on CUDA devices and streams, and the toolkit underpins NVIDIA's LLM training and inference software.[^s6]

## Sources
[^s1]: NVIDIA, "CUDA Programming Guide, 1.2 Programming Model", v13.4.2. https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html (accessed 2026-11-08)
[^s2]: Nickolls, Buck, Garland, Skadron, "Scalable Parallel Programming with CUDA", ACM Queue 6(2), 2008. https://grothoff.org/christian/teaching/2008/4704/scalable_cuda.pdf (accessed 2026-11-08)
[^s3]: Chetlur et al., "cuDNN: Efficient Primitives for Deep Learning", arXiv:1410.0759, 2014. https://arxiv.org/abs/1410.0759 (accessed 2026-11-08)
[^s4]: Krizhevsky, Sutskever, Hinton, "ImageNet Classification with Deep Convolutional Neural Networks", NIPS 2012. https://courses.cs.duke.edu/fall16/compsci527/papers/Krizhevsky%20et%20al%20DNN%20ImageNet%202012.pdf (accessed 2026-11-08)
[^s5]: PyTorch, "CUDA semantics", documentation v2.3. https://docs.pytorch.org/docs/2.3/notes/cuda.html (accessed 2026-11-08)
[^s6]: NVIDIA Developer, "CUDA Zone". https://developer.nvidia.com/cuda-zone (accessed 2026-11-08)
