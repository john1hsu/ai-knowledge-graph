---
id: kt:ai-hardware
type: Hardware
title: AI hardware
aliases: [machine learning hardware, ML hardware, deep learning hardware, AI compute hardware]
domain: ai-infrastructure-and-mlops
summary: >-
  The full physical stack used to train and serve AI models: processors (CPUs, GPUs and other accelerators),
  the memory hierarchy, interconnects and networks, storage and the datacenter systems that tie them together,
  whose balance increasingly decides AI performance more than peak arithmetic does.
maturity: established
broader: [kt:computer-architecture, kt:parallel-computing]
related: [kt:gpu-computing, kt:tpu, kt:compute-governance]
relations:
  - {predicate: hasPart, object: kt:ai-accelerator}
  - {predicate: hasPart, object: kt:high-bandwidth-memory}
  - {predicate: enables, object: kt:distributed-training}
sources:
  - id: s1
    title: "13.4. Hardware"
    publisher: "Dive into Deep Learning (Zhang, Lipton, Li, Smola), d2l.ai"
    url: https://d2l.ai/chapter_computational-performance/hardware.html
    type: textbook
    accessed: 2026-11-18
  - id: s2
    title: "AI and Memory Wall"
    publisher: "Gholami, Yao, Kim, Hooper, Mahoney, Keutzer (UC Berkeley / ICSI / LBNL), arXiv:2403.14123, March 2024"
    url: https://arxiv.org/html/2403.14123v1
    type: primary
    accessed: 2026-11-18
  - id: s3
    title: "Trends in Machine Learning Hardware"
    publisher: "Epoch AI (Hobbhahn, Heim, Aydos), November 2023"
    url: https://epoch.ai/blog/trends-in-machine-learning-hardware
    type: primary
    accessed: 2026-11-18
  - id: s4
    title: "TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings"
    publisher: "Jouppi et al. (Google), ISCA 2023; authors' arXiv version 2304.01433"
    url: https://arxiv.org/abs/2304.01433
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s5
    title: "A New Golden Age for Computer Architecture (Turing Lecture, ISCA 2018)"
    publisher: "Association for Computing Machinery"
    url: https://www.acm.org/hennessy-patterson-turing-lecture
    type: primary
    accessed: 2026-11-18
created: 2026-11-18
---

# AI hardware

**AI hardware** is the physical stack on which machine-learning models are trained and served. It is broader than any single chip: a deep-learning server combines a host CPU, one or more accelerators attached over PCIe, system and device memory, local storage for data and checkpoints, and a network link to other machines.[^s1] Accelerators such as GPUs and TPUs supply most of the arithmetic, but whether that arithmetic is usable depends on how fast data can reach it from memory, from other chips and from storage.[^s1][^s2] The field therefore treats AI hardware as a balance problem across compute, memory, interconnect and system design rather than a race for peak FLOP/s.

## Origin

GPUs outpace CPUs on deep learning because they offer thousands of parallel lanes for dense matrix arithmetic.[^s1] The turn toward purpose-built AI systems is part of a wider shift in computer architecture: in their 2018 ACM Turing Lecture at ISCA, John Hennessy and David Patterson framed domain-specific hardware and software co-design as a central direction for the field's "new golden age".[^s5] Google's TPU line is one result; by 2023 its fourth generation was described not as a chip but as a supercomputer of up to 4,096 chips.[^s4]

## The layers of the stack

- **Compute.** CPUs offer a few cores with wide vector units and deep caches; GPUs and other accelerators offer thousands of simpler lanes plus matrix units, but handle sparse data and interrupts poorly.[^s1] The trade-offs inside accelerators are covered in the AI accelerator article.
- **Memory hierarchy.** Latency rises by orders of magnitude from on-chip caches (about 1.5 ns for an L1 hit) to GPU global memory (about 200 ns), so the textbook advice is to keep working sets close to the processor and to favour large burst transfers over random access.[^s1]
- **Interconnect.** Within a server, accelerators talk over PCIe or faster links such as NVIDIA's NVLink; between servers, over Ethernet or specialised fabrics. Moving 1 MB to a GPU takes about 30 μs over NVLink and about 80 μs over PCIe in d2l's reference table.[^s1] Epoch AI singles out interconnect bandwidth as a key metric for large-scale training.[^s3]
- **Storage and I/O.** SSDs, often NVMe on PCIe, feed training data and hold checkpoints; their random-write behaviour and wear matter for data pipelines.[^s1]
- **Systems.** At the top, chips are assembled into pods and clusters. TPU v4 links its chips with optical circuit switches that can reconfigure the network topology; Google reports these switches cost under 5% of system cost and under 3% of system power.[^s4]

## Trends and the memory wall

Epoch AI's 2023 dataset of 47 ML accelerators found that FP32 peak performance doubled about every 2.3 years, while memory capacity and bandwidth doubled only about every 4 years; switching to tensor-core and low-precision formats added large further gains on top of FP32 (on average roughly 13× for INT8, by their estimate).[^s3] Gholami and colleagues at UC Berkeley put the gap more starkly for server hardware over roughly 20 years: peak FLOPS grew about 3.0× every two years, DRAM bandwidth about 1.6× and interconnect bandwidth about 1.4×.[^s2] They call the result the **memory wall** and argue it now binds many AI workloads, especially autoregressive decoding in LLMs, whose matrix-vector operations move far more bytes per FLOP than encoder models do at small batch sizes.[^s2]

## Limitations and open questions

Because compute outruns data movement, headline FLOP/s overstate real throughput; Gholami et al. propose shifting design effort toward better caches and higher-capacity memory, and pairing it with software methods such as quantization, pruning and rematerialization.[^s2] Vendor comparisons are also contested: Google reports that TPU v4 ran 1.2–1.7× faster than NVIDIA's A100 while using less power, a lab's own benchmark claim rather than an independent result.[^s4] Epoch notes its low-precision multipliers are rough estimates from limited data.[^s3] Energy and siting matter too: Google attributes much of TPU v4's lower emissions to running in efficient cloud datacenters rather than on-premise.[^s4]

## Connections

AI hardware sits under **computer architecture** and **parallel computing**.[^s5][^s1] Its main *parts* are **AI accelerators**, including **GPU computing** platforms and Google's **TPU**, and the **high-bandwidth memory** that feeds them, the component the memory-wall argument is about.[^s1][^s2][^s4] Fast interconnects and pod-scale systems are what *enable* **distributed training** across thousands of chips.[^s3][^s4] Since frontier training runs consume pod-scale hardware whose performance trends can be tracked, this stack is also the object that **compute governance** proposals aim to measure and steer.[^s3][^s4]

## Sources
[^s1]: Zhang, Lipton, Li and Smola, "13.4. Hardware", Dive into Deep Learning. https://d2l.ai/chapter_computational-performance/hardware.html (accessed 2026-11-18)
[^s2]: Gholami et al., "AI and Memory Wall", arXiv:2403.14123, 2024. https://arxiv.org/html/2403.14123v1 (accessed 2026-11-18)
[^s3]: Hobbhahn, Heim and Aydos, "Trends in Machine Learning Hardware", Epoch AI, 2023. https://epoch.ai/blog/trends-in-machine-learning-hardware (accessed 2026-11-18)
[^s4]: Jouppi et al., "TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings", ISCA 2023, arXiv:2304.01433. https://arxiv.org/abs/2304.01433 (accessed 2026-11-18)
[^s5]: ACM, "John Hennessy and David Patterson Deliver Turing Lecture at ISCA 2018". https://www.acm.org/hennessy-patterson-turing-lecture (accessed 2026-11-18)
