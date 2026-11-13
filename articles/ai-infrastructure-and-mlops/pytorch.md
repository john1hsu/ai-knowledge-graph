---
id: kt:pytorch
type: Tool
title: PyTorch
aliases: [torch]
domain: ai-infrastructure-and-mlops
summary: >-
  An open-source deep learning framework, begun at Meta (then Facebook) AI in 2016 and governed since 2022 by the
  PyTorch Foundation under the Linux Foundation, that pairs GPU-accelerated tensors with an imperative,
  define-by-run programming model and reverse-mode automatic differentiation, plus the torch.compile graph compiler.
maturity: established
broader: [kt:deep-learning-framework]
related: [kt:automatic-differentiation, kt:hugging-face-transformers, kt:data-parallelism, kt:distributed-training, kt:backpropagation, kt:gpu-computing]
relations:
  - {predicate: createdBy, object: kt:meta-ai}
  - {predicate: introducedIn, object: kt:pytorch-an-imperative-style-high-performance-deep-learning-library}
  - {predicate: dependsOn, object: kt:cuda}
sources:
  - id: s1
    title: "PyTorch: An Imperative Style, High-Performance Deep Learning Library"
    publisher: Advances in Neural Information Processing Systems 32 (NeurIPS 2019), Paszke et al.
    url: https://papers.nips.cc/paper/9015-pytorch
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s2
    title: "Autograd mechanics (PyTorch 2.2 documentation)"
    publisher: PyTorch documentation
    url: https://docs.pytorch.org/docs/2.2/notes/autograd.html
    type: official-docs
    accessed: 2026-11-13
  - id: s3
    title: "PyTorch 2 paper and tutorial @ ASPLOS 2024"
    publisher: PyTorch blog, 6 February 2024
    url: https://pytorch.org/blog/pytorch-2-paper-tutorial/
    type: primary
    accessed: 2026-11-13
  - id: s4
    title: "Meta Transitions PyTorch to the Linux Foundation, Further Accelerating AI/ML Open Source Collaboration"
    publisher: The Linux Foundation, press release, 12 September 2022
    url: https://linuxfoundation.org/press-release/meta-transitions-pytorch-to-the-linux-foundation/
    type: primary
    accessed: 2026-11-13
  - id: s5
    title: "PyTorch Foundation (announcement of PyTorch's move to the Linux Foundation)"
    publisher: Meta AI blog, 12 September 2022
    url: https://ai.meta.com/blog/pytorch-foundation/
    type: lab-research
    accessed: 2026-11-13
  - id: s6
    title: "PyTorch 2.14 Release Blog"
    publisher: PyTorch blog, 2 September 2026
    url: https://pytorch.org/blog/pytorch-2-14-release-blog/
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# PyTorch

PyTorch is an open-source library for building and training neural networks in Python. Its core objects are multidimensional tensors that can live on CPUs or GPUs, a library of differentiable operations over them, and an automatic differentiation engine that computes gradients of arbitrary Python programs. Its defining design choice is an imperative style: a model is ordinary Python code that executes line by line, which its authors argued makes it easy to debug and to combine with the wider scientific Python ecosystem without giving up speed.[^s1]

## Origin

Work on PyTorch began in 2016 at Meta AI (then Facebook AI Research). According to Meta, the team experimented with Theano and Torch and borrowed ideas from Lua Torch, Chainer and HIPS Autograd, putting usability first.[^s5] The framework was publicly released in 2016.[^s4] Meta announced PyTorch 1.0 in 2018, pitching it as a dynamic framework that could also switch to graph-based modes for deployment.[^s5] The design was described in a peer-reviewed paper by Paszke, Gross, Massa, Chintala and colleagues at NeurIPS 2019, which argued that usability and performance need not be traded off against each other.[^s1]

## How it works

The heart of PyTorch is **autograd**, a reverse-mode automatic differentiation system. As tensor operations run, autograd records them as a directed acyclic graph of `Function` objects whose leaves are input tensors and whose roots are outputs; each result's `grad_fn` points into this graph. Calling `.backward()` walks the graph from outputs to inputs, applying the chain rule, which is exactly the computation performed by backpropagation.[^s2] Operations that need forward-pass values for their gradient, such as squaring, save those tensors for the backward pass.[^s2]

Crucially, the graph is rebuilt from scratch on every iteration. Ordinary Python `if` statements and loops can therefore change the graph's shape from one step to the next, and the code that runs is the code that gets differentiated. This "define-by-run" approach contrasts with earlier static-graph frameworks that required the whole computation to be declared before execution.[^s2][^s1]

## PyTorch 2 and torch.compile

Eager execution makes whole-program optimization hard, because no complete graph exists ahead of time. PyTorch 2 addressed this with `torch.compile`, described in an ASPLOS 2024 paper. **TorchDynamo** is a Python-level just-in-time compiler that rewrites Python bytecode before execution and extracts runs of PyTorch operations into an FX graph, keeping Python's flexibility. **TorchInductor**, its default backend, compiles that graph into OpenAI Triton kernels for GPUs and C++ for CPUs.[^s3] The PyTorch team reported geometric-mean speedups of 2.27× for inference and 1.41× for training on an NVIDIA A100 across more than 180 real-world models, outperforming six other compilers; these are the authors' own benchmarks.[^s3]

## Limitations and open questions

The imperative model that makes PyTorch pleasant for research also complicates deployment and compilation: graph capture must cope with arbitrary Python, data-dependent control flow and dynamic shapes, which is why successive releases keep adding control-flow operators and dynamic-shape tooling.[^s3][^s6] Performance on new accelerators also depends on vendor backends and kernels, so feature parity across CUDA, ROCm, Apple Silicon and other platforms arrives unevenly.[^s6]

## In practice

In September 2022 Meta moved PyTorch to the newly formed PyTorch Foundation under the Linux Foundation, with AMD, AWS, Google Cloud, Meta, Microsoft Azure and NVIDIA as founding members on its governing board.[^s4] At that time Meta claimed over 2,400 contributors, more than 150,000 projects built on PyTorch, and use by more than 80 percent of researchers submitting to major ML conferences; these figures come from Meta and were not independently verified.[^s5] Development remains rapid: PyTorch 2.14, released on 2 September 2026, comprised 2,995 commits from 487 contributors since 2.13 and added Inductor kernel backends, a rewritten NCCL communication backend in preview, fault-tolerance features for distributed training and native Metal linear algebra on Apple Silicon.[^s6]

## Connections

PyTorch is a **deep learning framework** (broader). It was **created by Meta AI** and **introduced in** the NeurIPS 2019 paper.[^s1][^s5] Its autograd engine is an implementation of **automatic differentiation** that performs **backpropagation** over dynamically built graphs.[^s2] It is a workhorse of **GPU computing** and **depends on CUDA** for NVIDIA GPUs, with Inductor generating GPU kernels.[^s3][^s6] Higher-level libraries such as **Hugging Face Transformers** build on it, and its c10d collective-communication layer underpins **data parallelism** and wider **distributed training**.[^s6]

## Sources
[^s1]: Paszke et al., "PyTorch: An Imperative Style, High-Performance Deep Learning Library", NeurIPS 2019. https://papers.nips.cc/paper/9015-pytorch (accessed 2026-11-13)
[^s2]: PyTorch documentation, "Autograd mechanics" (2.2). https://docs.pytorch.org/docs/2.2/notes/autograd.html (accessed 2026-11-13)
[^s3]: PyTorch blog, "PyTorch 2 paper and tutorial @ ASPLOS 2024", 6 February 2024. https://pytorch.org/blog/pytorch-2-paper-tutorial/ (accessed 2026-11-13)
[^s4]: The Linux Foundation, "Meta Transitions PyTorch to the Linux Foundation", 12 September 2022. https://linuxfoundation.org/press-release/meta-transitions-pytorch-to-the-linux-foundation/ (accessed 2026-11-13)
[^s5]: Meta AI blog, "PyTorch Foundation" announcement, 12 September 2022. https://ai.meta.com/blog/pytorch-foundation/ (accessed 2026-11-13)
[^s6]: PyTorch blog, "PyTorch 2.14 Release Blog", 2 September 2026. https://pytorch.org/blog/pytorch-2-14-release-blog/ (accessed 2026-11-13)
