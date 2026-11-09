---
id: kt:tpu
type: Hardware
title: Tensor Processing Unit
aliases: [TPU, Cloud TPU, Google TPU]
domain: ai-infrastructure-and-mlops
summary: >-
  Google's family of custom application-specific chips for neural-network workloads, built around large
  systolic-array matrix-multiply units; first deployed for inference in Google's datacenters in 2015 and
  later scaled into optically interconnected pods for both training and serving.
maturity: established
broader: [kt:ai-accelerator, kt:application-specific-integrated-circuit]
related: [kt:cuda, kt:quantization, kt:distributed-training, kt:embeddings, kt:large-language-model]
relations:
  - {predicate: createdBy, object: kt:google}
  - {predicate: introducedIn, object: kt:in-datacenter-performance-analysis-of-a-tensor-processing-unit}
  - {predicate: basedOn, object: kt:systolic-array}
  - {predicate: alternativeTo, object: kt:gpu-computing}
sources:
  - id: s1
    title: "In-Datacenter Performance Analysis of a Tensor Processing Unit"
    publisher: ISCA 2017 (Jouppi, Young, Patil, Patterson et al., Google); authors' arXiv version 1704.04760
    url: https://arxiv.org/abs/1704.04760
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings"
    publisher: ISCA 2023 (Jouppi, Patterson et al., Google); authors' arXiv version 2304.01433
    url: https://arxiv.org/abs/2304.01433
    type: primary
    accessed: 2026-11-09
  - id: s3
    title: "TPU architecture"
    publisher: Google Cloud TPU documentation (last updated 2026-11-06)
    url: https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "TPU7x (Ironwood)"
    publisher: Google Cloud TPU documentation (page dated 2026-10-29)
    url: https://docs.cloud.google.com/tpu/docs/tpu7x
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "TPU v2"
    publisher: Google Cloud TPU documentation
    url: https://docs.cloud.google.com/tpu/docs/v2
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# Tensor Processing Unit

A **Tensor Processing Unit (TPU)** is a custom application-specific integrated circuit (ASIC) that Google designs to accelerate neural networks. Rather than a general-purpose processor with many independent cores, a TPU devotes most of its silicon to a few very large matrix-multiply units, on the bet that dense linear algebra dominates deep-learning workloads.[^s1][^s3] TPUs power Google's own products and are rented to outside users through Google Cloud, where they are the main commercial alternative to NVIDIA GPUs for large-scale training and serving.[^s3]

## Origin

The first TPU was described by Norman Jouppi, Cliff Young, Nishant Patil, David Patterson and roughly 70 Google colleagues at the 2017 International Symposium on Computer Architecture (ISCA). The chip had been running in Google's datacenters since 2015 and, by the authors' account, went from design to deployment in about 15 months.[^s1] It targeted *inference* only. The team measured six production applications (multilayer perceptrons, LSTMs and CNNs) that together made up about 95% of Google's datacenter inference demand at the time; CNNs were only around 5% of that mix, a reminder that the workload driving the chip was not mainly image models.[^s1]

## How it works

The original TPU's heart was a 256×256 grid of 65,536 8-bit multiply-accumulate (MAC) units clocked at 700 MHz, giving a peak of 92 tera-operations per second. It had 28 MiB of software-managed on-chip memory and 8 GiB of off-chip DRAM for weights.[^s1] The matrix unit is a **systolic array**: operands enter at the edges and pass from neighbour to neighbour each cycle, so each value fetched from memory is reused across many multiplications, cutting reads and writes and the energy they cost.[^s1] Because inference is user-facing, the design was deliberately simple and deterministic so that it could meet 99th-percentile latency limits rather than chase average throughput.[^s1]

Later generations kept the systolic idea but broadened the chip. Google's current documentation (updated November 2026) describes each **TensorCore** as one or more matrix-multiply units (MXUs) plus a vector unit for operations such as activations and softmax and a scalar unit for control flow. MXUs are 128×128 arrays on TPU v5p and earlier and 256×256 on v6e and TPU7x; they take bfloat16 inputs with FP32 accumulation, with int8 or FP8 available on some generations.[^s3] Data moves from the host into on-package high-bandwidth memory (HBM) and from there into the MXUs.[^s3]

## Scaling into pods

From the second generation onward TPUs were built to train as well as serve, and they were wired together. Chips connect through a dedicated inter-chip interconnect (ICI) into a **pod**; users rent a **slice** of chips within a pod, and *Multislice* joins slices over the ordinary datacenter network.[^s3] A full TPU v2 pod held up to 256 chips with two TensorCores each.[^s5] TPU v4, in service since 2020, grew the system to 4,096 chips and added optical circuit switches that reconfigure the network topology; the authors reported these cost under 5% of system cost and under 3% of power.[^s2] TPU v4 also added *SparseCores*, small dataflow units that the paper says speed embedding-heavy models such as recommenders by 5–7× for about 5% of die area and power.[^s2] The newest generation in Google's documentation, TPU7x (Ironwood), lists 9,216 chips per pod, 192 GiB of HBM per chip, and peak per-chip throughput of 2,307 BF16 TFLOPS (4,614 FP8), with two TensorCores and four SparseCores per chip, as of October 2026.[^s4]

## Evidence and limitations

The performance claims come mostly from Google itself. The 2017 paper reported the TPU running its workloads 15–30× faster than a contemporary NVIDIA K80 GPU or Intel Haswell CPU, with 30–80× better performance per watt.[^s1] The 2023 TPU v4 paper reported 2.1× the speed and 2.7× the performance per watt of TPU v3, and 1.2–1.7× the speed of an NVIDIA A100 at 1.3–1.9× lower power for similarly sized systems.[^s2] These are vendor measurements on chosen workloads and hardware generations, and newer GPUs have since moved the baseline. Practical limits include availability only through Google's cloud, programming through a compiler stack (frameworks such as JAX and PyTorch) rather than hand-written kernels, and a design that rewards large, regular matrix shapes; older generations are also retired on a schedule, as with TPU v2, which now receives only bug and security fixes.[^s3][^s5]

## Connections

The TPU is an instance of an **AI accelerator** and of an **application-specific integrated circuit**, created by **Google** and introduced to the literature in *In-Datacenter Performance Analysis of a Tensor Processing Unit*.[^s1] It is **based on** the **systolic array** structure,[^s1][^s3] and it is the chief **alternative to GPU computing** and the **CUDA** software stack for deep learning.[^s2][^s3] The first chip's 8-bit arithmetic is an early large-scale use of **quantization** for inference,[^s1] while pods, ICI and Multislice make TPUs a platform for **distributed training**.[^s3] SparseCores tie the hardware to **embeddings**,[^s2] and the latest generation is pitched at pre-training and serving **large language models**, including mixture-of-experts models.[^s4]

## Sources
[^s1]: Jouppi et al., "In-Datacenter Performance Analysis of a Tensor Processing Unit", ISCA 2017, arXiv:1704.04760. https://arxiv.org/abs/1704.04760 (accessed 2026-11-09)
[^s2]: Jouppi et al., "TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings", ISCA 2023, arXiv:2304.01433. https://arxiv.org/abs/2304.01433 (accessed 2026-11-09)
[^s3]: Google Cloud, "TPU architecture", Cloud TPU documentation. https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm (accessed 2026-11-09)
[^s4]: Google Cloud, "TPU7x (Ironwood)", Cloud TPU documentation. https://docs.cloud.google.com/tpu/docs/tpu7x (accessed 2026-11-09)
[^s5]: Google Cloud, "TPU v2", Cloud TPU documentation. https://docs.cloud.google.com/tpu/docs/v2 (accessed 2026-11-09)
