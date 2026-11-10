---
id: kt:nvidia
type: Organization
title: NVIDIA
aliases: [NVIDIA Corporation, Nvidia, NVDA]
domain: ai-infrastructure-and-mlops
summary: >-
  An American semiconductor and computing company, founded in 1993, whose graphics processing units, CUDA
  software platform and data-centre systems became the dominant hardware and software stack for training and
  serving deep-learning models.
maturity: established
broader: [kt:ai-hardware]
related: [kt:gpu-computing, kt:cuda, kt:tensor-cores, kt:tpu, kt:imagenet-and-alexnet, kt:deep-learning]
relations:
  - {predicate: enables, object: kt:distributed-training}
  - {predicate: regulatedBy, object: kt:ai-chip-export-controls}
sources:
  - id: s1
    title: "NVIDIA Corporation Form 10-K for the fiscal year ended January 25, 2026"
    publisher: U.S. Securities and Exchange Commission (EDGAR), filed February 2026
    url: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm
    type: primary
    accessed: 2026-11-10
  - id: s2
    title: "NVIDIA Corporation"
    publisher: Encyclopaedia Britannica (Britannica Money)
    url: https://www.britannica.com/money/NVIDIA-Corporation
    type: encyclopedia
    accessed: 2026-11-10
  - id: s3
    title: "Large-scale Deep Unsupervised Learning using Graphics Processors"
    publisher: ICML 2009 (Raina, Madhavan, Ng)
    url: https://icml.cc/imls/conferences/2009/papers/218.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s4
    title: "NVIDIA Hopper Architecture In-Depth"
    publisher: NVIDIA Technical Blog, March 22, 2022
    url: https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
    type: lab-research
    accessed: 2026-11-10
created: 2026-11-10
---

# NVIDIA

NVIDIA is a semiconductor and computing company headquartered in Santa Clara, California, founded in April 1993 by Jensen Huang, Chris Malachowsky and Curtis Priem.[^s2] It began as a maker of PC graphics chips and, according to its own annual report, now describes itself as a data-centre-scale AI infrastructure company.[^s1] For practitioners, NVIDIA matters less as a business than as the supplier of the default stack on which most modern deep learning runs: GPUs with dedicated matrix units, the CUDA programming platform, high-bandwidth interconnects and the libraries layered on top of them.[^s1][^s4]

## History

NVIDIA's RIVA chips (from 1997) gave it a foothold in PC gaming, and the GeForce 256 of 1999 moved geometry transformation and lighting onto consumer graphics hardware; the company went public the same year.[^s2] Its 10-K dates the invention of the GPU to 1999 and the introduction of CUDA to 2006, the step that opened its chips to general-purpose parallel programming rather than graphics alone.[^s1][^s2] Britannica also records a failed attempt in 2020 to buy the chip designer Arm from SoftBank for about $40 billion, abandoned in 2022 after resistance from regulators in several jurisdictions.[^s2]

## How it became central to deep learning

Researchers discovered early that the massively parallel arithmetic of graphics cards suited neural-network training. In an ICML 2009 paper, Raina, Madhavan and Ng trained deep belief networks on an NVIDIA GeForce GTX 280 and reported speedups of up to about 70 times over a dual-core CPU, cutting training of a four-layer network with roughly 100 million parameters from several weeks to about a day.[^s3] The paper argued that such speedups made far larger unsupervised models practical, and NVIDIA's CUDA platform went on to attract a developer base it now counts in the millions.[^s3][^s1] Britannica notes that the public release of ChatGPT in late 2022, built on a supercomputer using some 10,000 NVIDIA GPUs, marked the company's commercial breakout in generative AI.[^s2]

NVIDIA then designed its data-centre chips specifically around neural-network workloads. The H100 (Hopper architecture), announced at GTC in March 2022, has 80 billion transistors on TSMC's customised 4N process, fourth-generation Tensor Cores, and a Transformer Engine that switches layers between FP8 and 16-bit precision; its fourth-generation NVLink gives 900 GB/s of GPU-to-GPU bandwidth.[^s4] NVIDIA claimed up to 9x faster training and 30x faster inference on large language models than its previous A100, figures it labelled preliminary.[^s4]

## Scale and constraints

NVIDIA's fiscal 2026, which ended on January 25, 2026, brought revenue of $215.9 billion, up 65% from $130.5 billion the previous year, with Data Center revenue up 68% and gross margin of 71.1%.[^s1] It reports two segments (Compute & Networking, and Graphics) and had about 42,000 employees and, by its own count, over 7.5 million CUDA developers at that date.[^s1] The same filing highlights concentration risks: two direct customers accounted for 22% and 14% of fiscal 2026 revenue, wafer production depends on outside foundries such as TSMC and Samsung, and U.S. export licensing requirements imposed in April 2025 on its H20 chip led to a $4.5 billion charge and left it, in its words, effectively shut out of China's data-centre compute market by year end.[^s1]

These figures show both the strength and the fragility of the position. CUDA's large developer base and software ecosystem give NVIDIA hardware a lock-in effect that rivals' accelerators, such as Google's TPUs, must overcome, while customer concentration, foundry dependence and export controls are external risks the company itself identifies.[^s1][^s2]

## Connections

NVIDIA sits under **AI hardware** as the leading vendor of accelerators for machine learning.[^s1] It created **CUDA**, the programming layer beneath **GPU computing**, and the **Tensor Cores** and NVLink interconnects in chips such as the H100 make large-scale **distributed training** practical.[^s4] Early GPU training results such as Raina et al.'s fed the rise of **deep learning**, of which the **ImageNet/AlexNet** breakthrough is the best-known milestone.[^s3] Google's **TPU** is the best-known alternative accelerator design, and **AI chip export controls** now shape where NVIDIA can sell its data-centre products.[^s1]

## Sources
[^s1]: NVIDIA Corporation, Form 10-K for fiscal year ended January 25, 2026, SEC EDGAR. https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm (accessed 2026-11-10)
[^s2]: "NVIDIA Corporation", Encyclopaedia Britannica. https://www.britannica.com/money/NVIDIA-Corporation (accessed 2026-11-10)
[^s3]: Raina, Madhavan, Ng, "Large-scale Deep Unsupervised Learning using Graphics Processors", ICML 2009. https://icml.cc/imls/conferences/2009/papers/218.pdf (accessed 2026-11-10)
[^s4]: "NVIDIA Hopper Architecture In-Depth", NVIDIA Technical Blog, 2022. https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/ (accessed 2026-11-10)
