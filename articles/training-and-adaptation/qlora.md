---
id: kt:qlora
type: Technique
title: QLoRA
aliases: [quantized low-rank adaptation, quantized LoRA, 4-bit LoRA fine-tuning]
domain: training-and-adaptation
summary: >-
  A memory-efficient fine-tuning method that freezes a pretrained language model in 4-bit precision and trains only
  small low-rank adapter (LoRA) weights by backpropagating through the quantized model, so that models with tens of
  billions of parameters can be fine-tuned on a single GPU.
maturity: established
broader: [kt:parameter-efficient-fine-tuning, kt:fine-tuning]
related: [kt:quantization, kt:large-language-model, kt:llm-as-a-judge, kt:loftq, kt:instruction-tuning]
relations:
  - {predicate: extends, object: kt:lora}
  - {predicate: basedOn, object: kt:quantization}
  - {predicate: introducedIn, object: kt:qlora-efficient-finetuning-of-quantized-llms}
  - {predicate: createdBy, object: kt:tim-dettmers}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: implementedIn, object: kt:hugging-face-peft}
sources:
  - id: s1
    title: "QLoRA: Efficient Finetuning of Quantized LLMs"
    publisher: NeurIPS 2023, Advances in Neural Information Processing Systems 36 (Dettmers, Pagnoni, Holtzman and Zettlemoyer)
    url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s2
    title: "QLoRA: Efficient Finetuning of Quantized LLMs (full text)"
    publisher: arXiv 2305.14314, University of Washington (Dettmers, Pagnoni, Holtzman and Zettlemoyer)
    url: https://arxiv.org/pdf/2305.14314
    type: primary
    accessed: 2026-11-09
  - id: s3
    title: "LoRA: Low-Rank Adaptation of Large Language Models"
    publisher: arXiv 2106.09685, Microsoft; ICLR 2022 (Hu, Shen, Wallis, Allen-Zhu, Li, Wang and Chen)
    url: https://arxiv.org/html/2106.09685v1
    type: primary
    accessed: 2026-11-09
  - id: s4
    title: "Bitsandbytes (quantization guide)"
    publisher: Hugging Face Transformers documentation, v5.13.0
    url: https://huggingface.co/docs/transformers/v5.13.0/quantization/bitsandbytes
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "Quantization (PEFT developer guide)"
    publisher: Hugging Face PEFT documentation, v0.7.1
    url: https://huggingface.co/docs/peft/v0.7.1/developer_guides/quantization
    type: official-docs
    accessed: 2026-11-09
  - id: s6
    title: "LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models"
    publisher: ICLR 2024 (Li, Yu, Liang, Karampatziakis, He, Chen and Zhao)
    url: https://proceedings.iclr.cc/paper_files/paper/2024/hash/39ec972afab01e0d8ddc6834a9d12ac1-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# QLoRA

**QLoRA** (quantized low-rank adaptation) is a fine-tuning method that keeps a pretrained language model frozen in 4-bit precision and trains only small low-rank adapters attached to it, with gradients flowing back through the quantized weights into the adapters.[^s1][^s2] It was introduced by Tim Dettmers, Artidoro Pagnoni, Ari Holtzman and Luke Zettlemoyer of the University of Washington and published at NeurIPS 2023.[^s1] Its headline result was that a 65-billion-parameter model could be fine-tuned on a single 48 GB GPU, where ordinary 16-bit fine-tuning of the same model needs more than 780 GB of GPU memory.[^s2]

## Background: LoRA

QLoRA builds on LoRA (Hu et al., Microsoft, 2021), which freezes a pretrained weight matrix *W₀* and learns its update as a product of two thin matrices, so a layer computes *W₀x + BAx* with *B* of size *d×r*, *A* of size *r×k*, and a rank *r* much smaller than *d* or *k*.[^s3] *B* starts at zero, so training begins from the unchanged pretrained model, and after training *BA* can be merged into *W₀*, adding no inference latency. For GPT-3 175B the LoRA authors reported about 10,000 times fewer trainable parameters than full fine-tuning and roughly a threefold cut in hardware requirements.[^s3] LoRA still keeps the frozen base weights in 16-bit precision, however, and those weights dominate memory for large models.[^s2]

## How it works

QLoRA stores the frozen base weights in 4 bits and adds three techniques to keep quality and memory under control.[^s2]

- **4-bit NormalFloat (NF4).** Pretrained weights are roughly normally distributed, so NF4 places its 16 quantization levels at quantiles of a normal distribution scaled to [−1, 1], giving each level about the same number of weights and including an exact zero. The paper reports NF4 outperforming 4-bit integer and 4-bit float formats.[^s2]
- **Double quantization.** Block-wise quantization stores one scaling constant per block. QLoRA quantizes those constants again with 8-bit floats; with a block size of 64 this cuts their overhead from 0.5 to about 0.127 bits per parameter, roughly 3 GB on a 65B model.[^s2]
- **Paged optimizers.** Optimizer states use NVIDIA unified memory, so they can be moved to CPU memory during memory spikes (for example with gradient checkpointing on long sequences) instead of causing out-of-memory errors.[^s2]

During the forward and backward passes, each NF4 weight block is dequantized to bfloat16 for computation; only the adapter weights, also held in bfloat16, receive gradient updates.[^s2] The authors found that adapters must be placed on every linear layer of the transformer to match 16-bit fine-tuning, whereas adapting only the attention query and value projections, as in the original LoRA experiments, fell short.[^s2][^s3]

## Results and limitations

The authors fine-tuned more than 1,000 models across 8 instruction datasets and model sizes from 80M to 65B parameters.[^s1][^s2] Their Guanaco 65B model, trained on the small OASST1 dataset in about 24 hours on one GPU, scored 99.3% of ChatGPT's level on the Vicuna benchmark as judged by GPT-4, a figure the authors themselves attribute to model-based evaluation.[^s1][^s2] They also found that a 9k-example high-quality dataset beat a 450k-example subsample of FLAN v2 for chatbot quality, suggesting data quality matters more than size.[^s2]

The paper is candid about its limits. The authors could not fully confirm that QLoRA matches 16-bit fine-tuning at 33B and 65B scale, evaluated on a narrow set of benchmarks, and did not test 3-bit models or adapters other than LoRA.[^s2] They also documented weaknesses in chatbot evaluation itself: human raters agreed only moderately (Fleiss κ = 0.42), and GPT-4 as a judge showed order bias and favoured its own outputs.[^s2] Later work argues that quantizing then attaching LoRA consistently trails full fine-tuning; LoftQ (ICLR 2024) jointly computes the quantized weights and a low-rank initialization to shrink that gap, with the largest gains at 2-bit precision.[^s6]

## In practice

QLoRA is implemented through the bitsandbytes library in Hugging Face Transformers, where a `BitsAndBytesConfig` with `load_in_4bit`, `bnb_4bit_quant_type="nf4"`, `bnb_4bit_use_double_quant` and a bfloat16 compute dtype reproduces the paper's setup.[^s4][^s5] The Transformers documentation recommends NF4 for training 4-bit base models and states that 4-bit training only updates extra parameters such as adapters.[^s4] The PEFT library adds the adapters on top of the quantized model and also offers LoftQ initialization as an option.[^s5]

## Connections

QLoRA is a form of **parameter-efficient fine-tuning** and therefore of **fine-tuning** generally: it adapts a pretrained **large language model** while updating only a sliver of its parameters.[^s1] It **extends LoRA** by moving the frozen base model to 4 bits, and it is **based on quantization**, reusing block-wise weight quantization but for training rather than for inference alone.[^s2][^s3] It was **introduced in** the NeurIPS 2023 paper by **Tim Dettmers** and colleagues and is **implemented in** Hugging Face Transformers and PEFT.[^s1][^s4][^s5] Its Guanaco experiments applied it to **instruction tuning** on a single GPU, and its analysis of GPT-4 judging connects it to **LLM-as-a-judge** evaluation.[^s2] **LoftQ** is a successor technique aimed at its quantization error.[^s6]

## Sources
[^s1]: Dettmers, Pagnoni, Holtzman and Zettlemoyer, "QLoRA: Efficient Finetuning of Quantized LLMs", NeurIPS 2023. https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract.html (accessed 2026-11-09)
[^s2]: Dettmers, Pagnoni, Holtzman and Zettlemoyer, "QLoRA: Efficient Finetuning of Quantized LLMs", arXiv 2305.14314. https://arxiv.org/pdf/2305.14314 (accessed 2026-11-09)
[^s3]: Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", arXiv 2106.09685 (ICLR 2022). https://arxiv.org/html/2106.09685v1 (accessed 2026-11-09)
[^s4]: Hugging Face, "Bitsandbytes", Transformers documentation v5.13.0. https://huggingface.co/docs/transformers/v5.13.0/quantization/bitsandbytes (accessed 2026-11-09)
[^s5]: Hugging Face, "Quantization", PEFT developer guide v0.7.1. https://huggingface.co/docs/peft/v0.7.1/developer_guides/quantization (accessed 2026-11-09)
[^s6]: Li et al., "LoftQ: LoRA-Fine-Tuning-aware Quantization for Large Language Models", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/39ec972afab01e0d8ddc6834a9d12ac1-Abstract-Conference.html (accessed 2026-11-09)
