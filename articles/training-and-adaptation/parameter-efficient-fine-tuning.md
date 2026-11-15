---
id: kt:parameter-efficient-fine-tuning
type: Paradigm
title: Parameter-efficient fine-tuning
aliases: [PEFT, delta tuning, parameter-efficient transfer learning]
domain: training-and-adaptation
summary: >-
  A family of methods that adapt a pretrained model to a new task by training only a small set of added or selected
  parameters (adapters, soft prompts, low-rank updates) while keeping most or all of the original weights frozen,
  cutting the compute, memory and storage cost of fine-tuning.
maturity: established
broader: [kt:fine-tuning, kt:transfer-learning]
related: [kt:qlora, kt:large-language-model, kt:instruction-tuning, kt:hugging-face-trl, kt:prompt-engineering, kt:catastrophic-forgetting]
relations:
  - {predicate: hasPart, object: kt:lora}
  - {predicate: hasPart, object: kt:adapter-modules}
  - {predicate: hasPart, object: kt:prefix-tuning}
  - {predicate: hasPart, object: kt:prompt-tuning}
  - {predicate: introducedIn, object: kt:parameter-efficient-transfer-learning-for-nlp}
  - {predicate: implementedIn, object: kt:hugging-face-peft}
sources:
  - id: s1
    title: "Parameter-Efficient Transfer Learning for NLP"
    publisher: arXiv 1902.00751 (ICML 2019), Google Research (Houlsby et al.)
    url: https://arxiv.org/abs/1902.00751v2
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "Prefix-Tuning: Optimizing Continuous Prompts for Generation"
    publisher: ACL-IJCNLP 2021, Proceedings of the 59th Annual Meeting of the ACL (Li and Liang)
    url: https://aclanthology.org/2021.acl-long.353
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "The Power of Scale for Parameter-Efficient Prompt Tuning"
    publisher: EMNLP 2021 (Lester, Al-Rfou and Constant)
    url: https://aclanthology.org/2021.emnlp-main.243
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "LoRA: Low-Rank Adaptation of Large Language Models"
    publisher: arXiv 2106.09685, Microsoft; ICLR 2022 (Hu et al.)
    url: https://arxiv.org/html/2106.09685v1
    type: primary
    accessed: 2026-11-15
  - id: s5
    title: "Delta Tuning: A Comprehensive Study of Parameter Efficient Methods for Pre-trained Language Models"
    publisher: arXiv 2203.06904, Tsinghua University and collaborators (Ding et al.)
    url: https://arxiv.org/abs/2203.06904
    type: primary
    accessed: 2026-11-15
  - id: s6
    title: "PEFT"
    publisher: Hugging Face PEFT documentation (main branch; stable release v0.20.0)
    url: https://huggingface.co/docs/peft/main/en/index
    type: official-docs
    accessed: 2026-11-15
created: 2026-11-15
---

# Parameter-efficient fine-tuning

**Parameter-efficient fine-tuning (PEFT)**, also called *delta tuning*, is the practice of adapting a large pretrained model to a downstream task by training only a small number of parameters, either newly added ones or a chosen subset, while the bulk of the pretrained weights stays frozen.[^s5][^s6] The motivation is economic: full fine-tuning updates and stores a complete copy of every weight for every task, which becomes impractical as models grow to billions of parameters, whereas a PEFT method needs to store only a small task-specific delta on top of one shared base model.[^s1][^s3][^s6]

## Origin

The term traces to *Parameter-Efficient Transfer Learning for NLP* by Neil Houlsby and colleagues at Google, published at ICML 2019.[^s1] They inserted small trainable **adapter modules** into a frozen BERT model and reported results within 0.4% of full fine-tuning on the GLUE benchmark while adding only about 3.6% extra parameters per task, across 26 text-classification tasks in total.[^s1] Because the original network is untouched, new tasks can be added later without retraining or degrading earlier ones.[^s1]

## Main families

Ding et al.'s large empirical study groups the methods into three families according to how the trainable delta is defined.[^s5]

- **Addition-based** methods add new parameters. Adapters add small bottleneck layers inside each block.[^s1] **Prefix-tuning** (Li and Liang, ACL 2021) prepends learned continuous vectors to every layer, acting as virtual tokens that later tokens can attend to, and trains about 0.1% of the parameters of GPT-2 or BART.[^s2] **Prompt tuning** (Lester, Al-Rfou and Constant, EMNLP 2021) simplifies this to a learned soft prompt at the input only.[^s3]
- **Specification-based** methods leave the architecture alone and choose a small subset of existing parameters to train; the PEFT library's LayerNorm tuning, for instance, updates only normalization layers.[^s5][^s6]
- **Reparameterization-based** methods express the weight update in a compact form. **LoRA** (Hu et al., ICLR 2022) learns each update as a product of two low-rank matrices, giving a change of the form *ΔW = BA* added to a frozen weight *W₀*.[^s4][^s5]

## Evidence

Results across these papers suggest that, with enough model scale, training a tiny fraction of parameters can approach full fine-tuning. Prefix-tuning matched fine-tuning with full training data on table-to-text and summarization tasks, beat it in low-data settings, and generalized better to topics unseen in training.[^s2] Prompt tuning on T5 grew more competitive with model size and, beyond billions of parameters, matched tuning all weights; it also outperformed GPT-3's few-shot prompting by a large margin and improved robustness under domain shift.[^s3] For GPT-3 175B, the LoRA authors reported roughly 10,000 times fewer trainable parameters (4.7M versus about 175B), training memory falling from 1.2 TB to 350 GB, and checkpoints shrinking from 350 GB to 35 MB.[^s4] Ding et al., evaluating over 100 NLP tasks, found delta tuning can perform on a par with full fine-tuning depending on which parameters are tuned, while sharply reducing compute and storage.[^s5]

## Limitations and trade-offs

The methods are not interchangeable. The LoRA paper notes that sequential adapter layers add inference latency because they deepen the network, and that prefix-based methods consume part of the usable sequence length and degrade when too many special tokens are used (more than 256 for prefix-embedding tuning in its experiments).[^s4] LoRA avoids extra latency because its update can be merged into the base weights at deployment.[^s4] Prompt tuning's parity with full fine-tuning holds mainly for very large models; at smaller scales it lags.[^s3] Ding et al. stress that performance depends on the tuned parameter set and analyze combining methods, which remains an empirical design choice rather than a settled recipe.[^s5]

## In practice

As of November 2026, the most common entry point is Hugging Face's PEFT library, which describes its methods as training only a small number of extra parameters and claims performance comparable to full fine-tuning at much lower compute and storage cost.[^s6] It integrates with Transformers, Diffusers and Accelerate and implements soft-prompt methods (prompt tuning, prefix tuning, P-tuning), layer-tuning methods such as LayerNorm tuning, and many adapter methods including LoRA and its variants (DoRA, AdaLoRA and others) and IA3; the stable release was v0.20.0 when accessed.[^s6] Its documentation also positions PEFT as what makes training and storing LLMs feasible on consumer hardware.[^s6]

## Connections

PEFT is a narrower form of **fine-tuning** and, more broadly, of **transfer learning**: it reuses a pretrained model's knowledge while changing only a small delta.[^s1][^s5] Its member techniques include **adapter modules**, **prefix-tuning**, **prompt tuning** and **LoRA**; **QLoRA** extends LoRA by freezing the base model in 4-bit precision.[^s1][^s2][^s3][^s4] The paradigm was **introduced in** Houlsby et al.'s 2019 paper and is **implemented in** the Hugging Face PEFT library, which the **Hugging Face TRL** stack uses for **instruction tuning** of **large language models**.[^s1][^s6] Soft prompts relate it to **prompt engineering**: they replace hand-written discrete prompts with learned continuous ones.[^s3] Because the base weights are frozen, adding a task cannot overwrite earlier ones, which links PEFT to concerns about **catastrophic forgetting** in sequential fine-tuning.[^s1]

## Sources
[^s1]: Houlsby et al., "Parameter-Efficient Transfer Learning for NLP", arXiv 1902.00751 (ICML 2019). https://arxiv.org/abs/1902.00751v2 (accessed 2026-11-15)
[^s2]: Li and Liang, "Prefix-Tuning: Optimizing Continuous Prompts for Generation", ACL-IJCNLP 2021. https://aclanthology.org/2021.acl-long.353 (accessed 2026-11-15)
[^s3]: Lester, Al-Rfou and Constant, "The Power of Scale for Parameter-Efficient Prompt Tuning", EMNLP 2021. https://aclanthology.org/2021.emnlp-main.243 (accessed 2026-11-15)
[^s4]: Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", arXiv 2106.09685 (ICLR 2022). https://arxiv.org/html/2106.09685v1 (accessed 2026-11-15)
[^s5]: Ding et al., "Delta Tuning: A Comprehensive Study of Parameter Efficient Methods for Pre-trained Language Models", arXiv 2203.06904. https://arxiv.org/abs/2203.06904 (accessed 2026-11-15)
[^s6]: Hugging Face, "PEFT", PEFT documentation. https://huggingface.co/docs/peft/main/en/index (accessed 2026-11-15)
