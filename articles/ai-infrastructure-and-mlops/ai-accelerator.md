---
id: kt:ai-accelerator
type: Hardware
title: AI accelerator
aliases: [AI chip, machine learning accelerator, deep learning accelerator, DNN accelerator]
domain: ai-infrastructure-and-mlops
summary: >-
  A processor specialized for neural-network workloads, such as a GPU, an AI-specific ASIC like the TPU, or an
  FPGA, that gains speed and energy efficiency over general-purpose CPUs through massive parallelism, low-precision
  arithmetic, local memory and reduced instruction overhead.
maturity: established
broader: [kt:ai-hardware]
related: [kt:gpu-computing, kt:tpu, kt:application-specific-integrated-circuit, kt:quantization, kt:compute-governance]
relations:
  - {predicate: dependsOn, object: kt:high-bandwidth-memory}
  - {predicate: enables, object: kt:deep-learning}
  - {predicate: regulatedBy, object: kt:ai-chip-export-controls}
sources:
  - id: s1
    title: "Efficient Processing of Deep Neural Networks: A Tutorial and Survey"
    publisher: Proceedings of the IEEE, December 2017 (Sze, Chen, Yang, Emer); authors' arXiv version 1703.09039
    url: https://arxiv.org/abs/1703.09039v2
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s2
    title: "Domain-Specific Hardware Accelerators"
    publisher: Communications of the ACM 63(7), 2020 (Dally, Turakhia, Han; DOI 10.1145/3361682), copy hosted for Imperial College London course reading
    url: https://www.doc.ic.ac.uk/~wl/teachlocal/arch/papers/cacm20dsa.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "AI Chips: What They Are and Why They Matter"
    publisher: Georgetown University Center for Security and Emerging Technology (Khan and Mann), April 2020
    url: https://cset.georgetown.edu/publication/ai-chips-what-they-are-and-why-they-matter/
    type: academic
    accessed: 2026-11-15
  - id: s4
    title: "Lincoln AI Computing Survey (LAICS) Update"
    publisher: MIT Lincoln Laboratory Supercomputing Center (Reuther et al.), 2023; arXiv 2310.09145
    url: https://arxiv.org/pdf/2310.09145.pdf
    type: academic
    accessed: 2026-11-15
  - id: s5
    title: "AI Acceleration"
    publisher: Machine Learning Systems (open textbook, mlsysbook.ai)
    url: https://mlsysbook.ai/contents/hw_acceleration/hw_acceleration.html
    type: textbook
    accessed: 2026-11-15
created: 2026-11-15
---

# AI accelerator

An **AI accelerator** (also called an AI chip) is a processor built or adapted to run neural-network computations far more efficiently than a general-purpose CPU. The category spans graphics processing units (GPUs), field-programmable gate arrays (FPGAs) and application-specific integrated circuits (ASICs) designed for AI, such as Google's TPU.[^s3][^s5] A 2020 Georgetown CSET report estimated that such chips can be tens to thousands of times faster and more energy-efficient than CPUs on AI workloads, and argued that state-of-the-art chips are a prerequisite for training and running large models at a reasonable cost.[^s3]

## Origin

Offloading arithmetic from the CPU is an old idea. Floating-point coprocessors such as Intel's 8087 (1980) took math off the 8086, and GPUs, built for graphics in the 1990s, became general-purpose parallel processors in the 2000s; their use to train AlexNet in 2012 marked a breakthrough for deep learning.[^s5] As Dennard scaling ended and Moore's-law gains slowed, architects turned to **domain-specific accelerators** as one of the few remaining routes to better performance per watt, a case argued by Bill Dally, Yatish Turakhia and Song Han in *Communications of the ACM* in 2020.[^s2][^s5] Google's TPU is a prominent example of such an AI-specific ASIC.[^s5]

## How it works

Dally and colleagues attribute accelerator gains to four mechanisms whose effects multiply.[^s2]

- **Specialized data types and operations** do in one step what takes a CPU many instructions.[^s2]
- **Massive parallelism** puts thousands of multiply-accumulate (MAC) units to work at once, provided each has local data.[^s2]
- **Local, optimized memory** keeps operands in small on-chip buffers, because data movement rather than arithmetic dominates energy.[^s1][^s2]
- **Reduced overhead** strips out instruction fetch, decode and speculation; the authors estimate a 32-bit add costs about 63 fJ in 28 nm silicon versus over 250 pJ for an add instruction on a mobile CPU core.[^s2]

The memory point is central. Sze, Chen, Yang and Emer's survey in *Proceedings of the IEEE* (2017) notes that a DRAM access can cost orders of magnitude more energy than the computation it feeds, so accelerator designs are judged largely by their **dataflow**: which values (weights, activations or partial sums) stay put in each processing element. Their taxonomy names weight-stationary, output-stationary, no-local-reuse and row-stationary dataflows, and reports that row-stationary used about 1.4–2.5× less energy on AlexNet convolution layers in their comparison.[^s1] The survey also contrasts *temporal* architectures (CPUs and GPUs, where a central controller drives many ALUs that fetch from a shared memory hierarchy) with *spatial* ones (common in ASICs and FPGAs, where processing elements pass data directly to neighbours, as in a systolic array).[^s1]

**Low precision** is the other lever. The same survey reports that an 8-bit fixed-point multiply uses about 15.5× less energy than a 32-bit fixed-point one and about 18.5× less than 32-bit floating point, and that inference tolerates reduced precision better than training.[^s1] Accordingly, most accelerators in MIT Lincoln Laboratory's 2023 survey reach peak inference throughput at int8 or fp16/bf16.[^s4]

## Types and landscape

Each class trades efficiency against flexibility. ASICs give the highest efficiency but carry long design cycles and high up-front cost; FPGAs are reconfigurable but slower and harder to program; GPUs offer mature software and broad availability at some efficiency cost.[^s5] Dally et al. estimate that FPGAs give up 10–100× in efficiency for their flexibility, and that GPUs with specialized matrix instructions come within roughly 13–23% of a dedicated ASIC on matrix multiplication.[^s2] CSET's 2020 report described GPUs as used mainly for training, FPGAs mainly for inference, and ASICs for either.[^s3] The Lincoln Laboratory survey, reflecting the market as of summer 2023, classifies chips by technology (GPU, CPU, dataflow, tensor, FPGA, processing-in-memory, manycore) and by segment, from sub-watt embedded parts to datacenter systems; it notes that frontier foundation models are trained on the same kinds of accelerators as smaller jobs, just many more of them linked by high-bandwidth networks.[^s4]

## Limitations

Specialization only pays if software can exploit it: accelerators depend on compilers, kernel libraries and runtimes (CUDA, cuDNN, TensorRT, TVM, ONNX) to map models onto hardware.[^s5] Dally et al. stress that algorithms tuned for CPUs often run poorly on accelerators and must be co-designed with the hardware, and that once arithmetic is nearly free, memory bandwidth caps the speedup.[^s2] Peak figures quoted by vendors are measured on chosen workloads and precisions and are not directly comparable across products.[^s4]

## Connections

AI accelerators are a subclass of **AI hardware**. **GPU computing** and Google's **TPU**, an **application-specific integrated circuit**, are the dominant instances.[^s3][^s5] Their efficiency **depends on** feeding compute from fast memory such as **high-bandwidth memory**,[^s1][^s5] and their reliance on low-precision arithmetic ties them to **quantization**.[^s1][^s4] They **enabled** modern **deep learning**, from AlexNet onward.[^s5] Because the advanced chip supply chain is concentrated in a few countries, CSET argued that AI chips are a natural lever for policy, the logic behind **AI chip export controls** and **compute governance**.[^s3]

## Sources
[^s1]: Sze, Chen, Yang and Emer, "Efficient Processing of Deep Neural Networks: A Tutorial and Survey", Proceedings of the IEEE, 2017, arXiv:1703.09039. https://arxiv.org/abs/1703.09039v2 (accessed 2026-11-15)
[^s2]: Dally, Turakhia and Han, "Domain-Specific Hardware Accelerators", Communications of the ACM 63(7), 2020. https://www.doc.ic.ac.uk/~wl/teachlocal/arch/papers/cacm20dsa.pdf (accessed 2026-11-15)
[^s3]: Khan and Mann, "AI Chips: What They Are and Why They Matter", Georgetown CSET, April 2020. https://cset.georgetown.edu/publication/ai-chips-what-they-are-and-why-they-matter/ (accessed 2026-11-15)
[^s4]: Reuther et al., "Lincoln AI Computing Survey (LAICS) Update", MIT Lincoln Laboratory, 2023, arXiv:2310.09145. https://arxiv.org/pdf/2310.09145.pdf (accessed 2026-11-15)
[^s5]: "AI Acceleration", Machine Learning Systems (open textbook). https://mlsysbook.ai/contents/hw_acceleration/hw_acceleration.html (accessed 2026-11-15)
