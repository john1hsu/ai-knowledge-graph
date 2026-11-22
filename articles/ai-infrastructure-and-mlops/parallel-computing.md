---
id: kt:parallel-computing
type: Paradigm
title: Parallel computing
aliases: [parallel processing, parallel programming, concurrent computation on multiple processors]
domain: ai-infrastructure-and-mlops
summary: >-
  The simultaneous use of multiple processors or compute resources to solve one computational
  problem, which is split into parts that run concurrently under a coordination mechanism; it is
  the computing paradigm on which GPU acceleration and distributed training of neural networks rest.
maturity: foundational
broader: [kt:computer-architecture]
related: [kt:gpu-computing, kt:ai-hardware, kt:cuda, kt:amdahls-law, kt:message-passing-interface]
relations:
  - {predicate: hasPart, object: kt:data-parallelism}
  - {predicate: hasPart, object: kt:model-parallelism}
  - {predicate: enables, object: kt:distributed-training}
  - {predicate: enables, object: kt:deep-learning}
  - {predicate: contrastsWith, object: kt:serial-computing}
sources:
  - id: s1
    title: "Introduction to Parallel Computing Tutorial"
    publisher: Lawrence Livermore National Laboratory, HPC @ LLNL (Livermore Computing Getting Started workshop series), June 2026 version
    url: https://hpc.llnl.gov/training/tutorials/introduction-parallel-computing-tutorial
    type: government
    accessed: 2026-11-22
  - id: s2
    title: "Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities"
    publisher: AFIPS Conference Proceedings vol. 30, Spring Joint Computer Conference 1967, pp. 483-485 (Gene M. Amdahl, IBM); 2007 IEEE SSCS News reprint hosted by Stony Brook University
    url: https://www3.cs.stonybrook.edu/~rezaul/Spring-2019/CSE613/reading/Amdahl-1967.pdf
    type: peer-reviewed
    accessed: 2026-11-22
  - id: s3
    title: "Reevaluating Amdahl's Law"
    publisher: Communications of the ACM 31(5), May 1988 (John L. Gustafson, Sandia National Laboratories); University of Utah course copy
    url: https://users.cs.utah.edu/~hari/teaching/paralg/Gustafson88.pdf
    type: peer-reviewed
    accessed: 2026-11-22
  - id: s4
    title: "Parallel processing"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/technology/parallel-processing
    type: encyclopedia
    accessed: 2026-11-22
created: 2026-11-22
---

# Parallel computing

**Parallel computing** is the use of several compute resources at the same time to solve a single computational problem. Lawrence Livermore National Laboratory's long-running tutorial contrasts it with serial computing, where a problem becomes one stream of instructions executed in order on one processor: in parallel computing the problem is broken into discrete parts that are solved concurrently, with an overall mechanism coordinating them.[^s1] Britannica distinguishes it from concurrency in general by the requirement that more than one processor actually executes the program, or set of programs, at the same moment.[^s4]

## Why parallelism

The LLNL tutorial lists the practical motives: shortening time to solution, tackling problems too large for one machine's memory, doing many things at once, drawing on remote or cloud resources, and not wasting the multiple cores now found even in laptops.[^s1] It also frames parallelism as the direction of the whole field, citing a rise in supercomputer performance of more than 500,000x over roughly two decades and an exascale era of 10^18 operations per second (as of its June 2026 version).[^s1] Britannica attributes renewed pressure for parallel execution to big data and very large numbers of simultaneous users.[^s4]

## Classifying parallel machines

**Flynn's taxonomy** (1966) sorts computers by whether they have single or multiple instruction streams and data streams.[^s1] SISD is the classic serial computer. SIMD machines apply one instruction to many data elements per cycle and suit regular workloads such as image processing; historical processor arrays like ILLIAC IV and vector machines like the Cray X-MP belong here, and modern CPUs' vector units and GPUs execute SIMD-style instructions.[^s1] MISD has few if any real examples, while MIMD, where independent processors run different instructions on different data, describes most clusters, multicore PCs and supercomputers, often with SIMD parts inside.[^s1]

Memory organization is the second axis. In **shared-memory** systems all processors see one global address space, either with uniform access times (UMA, as in symmetric multiprocessors) or with slower access to memory attached to other sockets (NUMA); in **distributed-memory** systems each processor has only local memory and data must move over a network.[^s1][^s4] Large modern systems are hybrids: networked nodes, each a shared-memory machine often carrying GPUs.[^s1] These map onto programming models: threads (Pthreads, OpenMP) for shared memory, message passing (MPI) for distributed memory, data-parallel models that partition one data structure among tasks, and SPMD or MPMD execution styles.[^s1]

## Limits: Amdahl and Gustafson

Gene Amdahl argued at the 1967 AFIPS conference that a large, apparently sequential share of real workloads, data-management "housekeeping" he put at about 40% of executed instructions, would cap the benefit of many parallel processors, so improving single-processor speed remained essential.[^s2] His paper states this verbally, without equations.[^s2] The standard formalization is speedup = 1 / (S + P/N) for serial fraction S, parallel fraction P and N processors; LLNL's table shows that 95%-parallel code tops out near 20x even with 100,000 processors.[^s1]

John Gustafson replied in 1988 that this fixed-size view misleads, because users grow the problem with the machine and hold run time roughly constant.[^s3] On a 1,024-processor hypercube at Sandia, three scientific applications with serial fractions of 0.4–0.8% reached speedups of 1,016–1,021, and he proposed **scaled speedup**, N + (1 − N)s, as the better measure.[^s3] The two views correspond to **strong scaling** (fixed total problem) and **weak scaling** (fixed work per processor).[^s1]

## Practical costs

Parallel programs pay overheads serial ones do not. Communication consumes cycles and bandwidth, and latency dominates when many small messages are sent, so batching messages and overlapping communication with computation help.[^s1] Synchronization primitives such as barriers and locks force tasks to wait; with barriers the slowest task sets the pace, which makes **load balancing** important.[^s1] **Granularity**, the ratio of computation to communication, trades easier balancing (fine grain) against lower overhead (coarse grain).[^s1]

## Connections

Parallel computing sits within **computer architecture** and contrasts with **serial computing**.[^s1] Its SIMD and hybrid-node ideas underlie **GPU computing**, **CUDA** and the wider **AI hardware** stack.[^s1] Its data-parallel model and the split of work across devices reappear as **data parallelism** and **model parallelism**, which together make **distributed training**, and thus large-scale **deep learning**, possible.[^s1] **Amdahl's law**, with Gustafson's scaled-speedup counterpoint, is the paradigm's central performance model, and the **Message Passing Interface** is its standard programming interface for distributed memory.[^s1][^s2][^s3]

## Sources
[^s1]: Lawrence Livermore National Laboratory, "Introduction to Parallel Computing Tutorial", HPC @ LLNL, June 2026 version. https://hpc.llnl.gov/training/tutorials/introduction-parallel-computing-tutorial (accessed 2026-11-22)
[^s2]: Gene M. Amdahl, "Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities", AFIPS Conference Proceedings 30, 1967 (2007 reprint). https://www3.cs.stonybrook.edu/~rezaul/Spring-2019/CSE613/reading/Amdahl-1967.pdf (accessed 2026-11-22)
[^s3]: John L. Gustafson, "Reevaluating Amdahl's Law", Communications of the ACM 31(5), 1988. https://users.cs.utah.edu/~hari/teaching/paralg/Gustafson88.pdf (accessed 2026-11-22)
[^s4]: Encyclopaedia Britannica, "Parallel processing". https://www.britannica.com/technology/parallel-processing (accessed 2026-11-22)
