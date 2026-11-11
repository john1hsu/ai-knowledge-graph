---
id: kt:high-bandwidth-memory
type: Hardware
title: High-bandwidth memory
aliases: [HBM, High Bandwidth Memory, stacked DRAM]
domain: ai-infrastructure-and-mlops
summary: >-
  A JEDEC-standardized form of DRAM in which several memory dies are stacked vertically, joined by
  through-silicon vias and placed beside the processor in the same package, giving a very wide, short
  interface; it is the main memory of modern AI accelerators and often the limiting resource for LLM serving.
maturity: established
broader: [kt:ai-hardware, kt:dram]
related: [kt:gpu-computing, kt:tpu, kt:large-language-model, kt:batching-and-paged-attention, kt:quantization]
relations:
  - {predicate: partOf, object: kt:ai-accelerator}
  - {predicate: basedOn, object: kt:through-silicon-via}
  - {predicate: createdBy, object: kt:jedec}
  - {predicate: alternativeTo, object: kt:gddr-memory}
  - {predicate: mitigates, object: kt:memory-wall}
sources:
  - id: s1
    title: "JEDEC Updates Groundbreaking High Bandwidth Memory (HBM) Standard"
    publisher: JEDEC Solid State Technology Association, press release, 17 Dec 2018
    url: https://www.jedec.org/news/pressreleases/jedec-updates-groundbreaking-high-bandwidth-memory-hbm-standard-0
    type: standards-body
    accessed: 2026-11-11
  - id: s2
    title: "JEDEC and Industry Leaders Collaborate to Release JESD270-4 HBM4 Standard Advancing Bandwidth, Efficiency, and Capacity for AI and HPC"
    publisher: JEDEC, press release via Business Wire, 16 Apr 2025
    url: https://businesswire.com/news/home/20250416843598/en/JEDEC-and-Industry-Leaders-Collaborate-to-Release-JESD270-4-HBM4-Standard-Advancing-Bandwidth-Efficiency-and-Capacity-for-AI-and-HPC
    type: standards-body
    accessed: 2026-11-11
  - id: s3
    title: "AMD Showcases Graphics, Energy Efficient Computing and Die-Stacking Innovation at Prestigious Hot Chips 27 Conference"
    publisher: AMD investor relations, press release, 24 Aug 2015
    url: https://ir.amd.com/news-events/press-releases/detail/629/amd-showcases-graphics-energy-efficient-computing-and-die-stacking-innovation-at-prestigious-hot-chips-27-conference
    type: primary
    accessed: 2026-11-11
  - id: s4
    title: "NVIDIA Hopper Architecture In-Depth"
    publisher: NVIDIA Technical Blog, 22 Mar 2022
    url: https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
    type: official-docs
    accessed: 2026-11-11
  - id: s5
    title: "AI and Memory Wall"
    publisher: Gholami, Yao, Kim, Hooper, Mahoney, Keutzer (UC Berkeley), authors' arXiv version 2403.14123, Mar 2024
    url: https://arxiv.org/abs/2403.14123
    type: primary
    accessed: 2026-11-11
created: 2026-11-11
---

# High-bandwidth memory

High-bandwidth memory (HBM) is a JEDEC standard for stacked DRAM. Instead of placing memory chips around a circuit board and driving a narrow, fast bus to each, HBM stacks several DRAM dies on top of one another, connects them vertically with through-silicon vias (TSVs), and exposes a very wide interface: 1,024 bits per stack in the original generations, split into independent channels.[^s1] The stack sits next to the GPU or accelerator inside the same package, usually on a silicon interposer, so the many short wires can run at modest per-pin speeds while still delivering very high total bandwidth.[^s3] HBM is now the standard main memory for data-centre AI accelerators, and how much of it a chip has, and how fast, often limits large-model performance more than arithmetic throughput does.[^s4][^s5]

## Origin and generations

AMD and its memory partner SK hynix brought HBM to market in AMD's Fiji graphics processors (Radeon R9 Fury family) in 2015. AMD described this as the graphics industry's first high-volume interposer with TSVs and micro-bumps, and claimed, from its own test setup, about four times the bandwidth per watt of the GDDR5 memory it replaced.[^s3] The standard has since been revised several times. JEDEC's December 2018 update (JESD235B) raised the per-pin rate to 2.4 Gb/s, or up to 307 GB/s per stack, and allowed stacks from 2-high to 12-high holding up to 24 GB each.[^s1]

The HBM4 standard, JESD270-4, was released in April 2025. It doubles the interface to 2,048 bits and the channel count to 32 per stack. At up to 8 Gb/s per pin it reaches up to 2 TB/s per stack, and 16-high stacks of 32 Gb dies give up to 64 GB per stack. Its interface stays compatible with HBM3 controllers, so one controller can drive either generation, and it adds Directed Refresh Management to defend against row-hammer errors.[^s2]

## Why it matters for AI

A transformer's weights and activations have to stream from memory into the compute units. When there is little arithmetic per byte moved, memory bandwidth sets the speed limit. Gholami and colleagues estimate that over the past two decades peak server FLOPS grew roughly 3.0x every two years, compared with about 1.6x for DRAM bandwidth and 1.4x for interconnect bandwidth. They call the resulting gap the "memory wall" and show that bandwidth can become the dominant bottleneck for decoder-style LLM inference.[^s5] At small batch sizes, autoregressive decoding reduces to matrix-vector products that read every weight for each generated token while doing little arithmetic per byte, so it is typically memory-bound rather than compute-bound.[^s5]

HBM is the hardware industry's main answer. NVIDIA's H100 SXM5 board, for example, carries 80 GB of HBM3 in five stacks behind ten 512-bit memory controllers and provides about 3 TB/s. That is roughly twice the bandwidth of the earlier A100, which used 40 GB of HBM2.[^s4] Capacity matters as much as bandwidth: models too large for one device's memory, such as GPT-3, must be split across several accelerators, and the traffic between chips then becomes a bottleneck of its own.[^s5]

## Limitations and trade-offs

HBM is a packaging technology as much as a memory type. It depends on die stacking, TSVs, micro-bumps and an interposer, which conventional board-mounted DRAM does not need, and it ties the memory permanently to the processor package.[^s3] The memory wall analysis finds that single-accelerator memory capacity has grown only about 2x every two years, and that bandwidth has trailed compute for two decades, so new HBM generations narrow the gap without closing it.[^s5] Each stack generation also adds reliability work: HBM4, for instance, builds row-hammer mitigation and reliability, availability and serviceability features into the standard.[^s2]

Because bandwidth is scarce, much LLM systems work aims to move fewer bytes. The memory wall authors point to low-precision formats (FP8 or FP16 for training, and inference quantized to INT4 with little accuracy loss), large-batch inference that turns matrix-vector work into matrix-matrix work, and keeping more of the working set in on-chip caches.[^s5] Paged KV-cache management and fused attention kernels follow the same logic: they treat HBM traffic and capacity as the resource to economize.

## Connections

HBM is a *part of* the AI accelerator: GPUs and TPUs pair their compute dies with HBM stacks in one package, so it sits under **AI hardware** and, as a memory technology, under **DRAM**.[^s4] It is *based on* through-silicon vias, which make vertical die stacking possible, and the specification is maintained by **JEDEC**.[^s1] It is the high-bandwidth *alternative to* board-mounted GDDR graphics memory, which it displaced first in AMD's Fiji GPUs.[^s3] It is the main hardware mitigation for the **memory wall**, the widening gap between compute and memory bandwidth.[^s5] That same bandwidth limit explains why **quantization** and **batching and paged attention** make **large language model** serving faster: both cut the bytes read from HBM for each generated token.[^s5]

## Sources
[^s1]: JEDEC, "JEDEC Updates Groundbreaking High Bandwidth Memory (HBM) Standard", 17 Dec 2018. https://www.jedec.org/news/pressreleases/jedec-updates-groundbreaking-high-bandwidth-memory-hbm-standard-0 (accessed 2026-11-11)
[^s2]: JEDEC, "JEDEC and Industry Leaders Collaborate to Release JESD270-4 HBM4 Standard…", Business Wire, 16 Apr 2025. https://businesswire.com/news/home/20250416843598/en/JEDEC-and-Industry-Leaders-Collaborate-to-Release-JESD270-4-HBM4-Standard-Advancing-Bandwidth-Efficiency-and-Capacity-for-AI-and-HPC (accessed 2026-11-11)
[^s3]: AMD, "AMD Showcases Graphics, Energy Efficient Computing and Die-Stacking Innovation at Prestigious Hot Chips 27 Conference", 24 Aug 2015. https://ir.amd.com/news-events/press-releases/detail/629/amd-showcases-graphics-energy-efficient-computing-and-die-stacking-innovation-at-prestigious-hot-chips-27-conference (accessed 2026-11-11)
[^s4]: NVIDIA, "NVIDIA Hopper Architecture In-Depth", NVIDIA Technical Blog, 22 Mar 2022. https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/ (accessed 2026-11-11)
[^s5]: Gholami et al., "AI and Memory Wall", arXiv:2403.14123, 2024. https://arxiv.org/abs/2403.14123 (accessed 2026-11-11)
