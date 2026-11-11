---
id: kt:fine-tuning
type: Technique
title: Fine-tuning
aliases: [finetuning, full fine-tuning, model fine-tuning]
domain: training-and-adaptation
summary: >-
  A transfer-learning technique that adapts a pretrained neural network to a new task or domain by continuing to
  train some or all of its weights on a smaller, task-specific dataset, instead of training a model from random
  initialization.
maturity: established
broader: [kt:transfer-learning, kt:deep-learning]
related: [kt:parameter-efficient-fine-tuning, kt:instruction-tuning, kt:rlhf, kt:qlora, kt:large-language-model]
relations:
  - {predicate: dependsOn, object: kt:pretraining}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: contrastsWith, object: kt:linear-probing}
  - {predicate: alternativeTo, object: kt:in-context-learning}
  - {predicate: causes, object: kt:catastrophic-forgetting}
  - {predicate: influencedBy, object: kt:universal-language-model-fine-tuning-for-text-classification}
sources:
  - id: s1
    title: "How transferable are features in deep neural networks?"
    publisher: NeurIPS 2014, Advances in Neural Information Processing Systems 27 (Yosinski, Clune, Bengio and Lipson)
    url: https://proceedings.nips.cc/paper_files/paper/2014/file/375c71349b295fbe2dcdca9206f20a06-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "Universal Language Model Fine-tuning for Text Classification"
    publisher: ACL 2018, Proceedings of the 56th Annual Meeting of the ACL, pp. 328–339 (Howard and Ruder)
    url: https://aclanthology.org/P18-1031/
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s3
    title: "14.2. Fine-Tuning"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), d2l.ai
    url: https://d2l.ai/chapter_computer-vision/fine-tuning.html
    type: textbook
    accessed: 2026-11-11
  - id: s4
    title: "Fine-tuning (Training guide)"
    publisher: Hugging Face Transformers documentation (main branch)
    url: https://huggingface.co/docs/transformers/training
    type: official-docs
    accessed: 2026-11-11
  - id: s5
    title: "Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution"
    publisher: ICLR 2022 (Kumar, Raghunathan, Jones, Ma and Liang)
    url: https://iclr.cc/virtual/2022/poster/5945
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s6
    title: "Overcoming catastrophic forgetting in neural networks"
    publisher: arXiv 1612.00796, Google DeepMind; PNAS 2017, doi:10.1073/pnas.1611835114 (Kirkpatrick et al.)
    url: https://arxiv.org/abs/1612.00796
    type: primary
    accessed: 2026-11-11
created: 2026-11-11
---

# Fine-tuning

**Fine-tuning** is the practice of taking a network that has already been trained on a large source dataset and continuing to train it on a smaller dataset for the task you actually care about. The pretrained weights act as the starting point, so the model inherits general-purpose features and only has to learn what is specific to the new task.[^s3] The Hugging Face Transformers guide describes it as the same procedure as pretraining except that training does not start from random weights, and notes that it needs far less compute, data and time.[^s4]

## Origin and evidence

Fine-tuning grew out of transfer learning in computer vision, where ImageNet-pretrained convolutional networks were reused for new image tasks. Yosinski, Clune, Bengio and Lipson (NeurIPS 2014) measured how transferable each layer is: early layers learn general, Gabor-like and colour-blob features, while the last layers are specific to the original task, and transferability falls as source and target tasks become less similar.[^s1] They also found that networks initialised with transferred features and then fine-tuned generalised better than networks trained only on the target data, a boost that persisted after long training.[^s1]

In NLP, Howard and Ruder's ULMFiT (ACL 2018) argued that transfer learning had lagged behind vision because methods still needed task-specific changes and training from scratch. They fine-tuned a pretrained language model for text classification, cutting error by 18–24% on most of six benchmark datasets, and with only 100 labelled examples matched training from scratch on 100 times more data.[^s2] This pretrain-then-fine-tune recipe became the default way to build task models from large pretrained language models.

## How it works

*Dive into Deep Learning* breaks the classic procedure into four steps: pretrain a source model; copy its architecture and parameters except the output layer; attach a new, randomly initialised output layer sized for the target classes; and train the whole target model on the target data.[^s3] Because the copied layers are already useful, they get a small learning rate, while the new head, starting from scratch, gets a larger one (ten times larger in the book's example).[^s3] In that worked example, an ImageNet-pretrained ResNet-18 fine-tuned on roughly 2,000 hot-dog/not-hot-dog training images reached about 94% test accuracy in five epochs, against about 85–86% for the same architecture trained from scratch.[^s3]

For large language models the mechanics are the same but the objective is usually next-token prediction on domain text or instruction data. The Transformers documentation walks through loading a causal language model in its saved precision, tokenising a dataset, and running the `Trainer` with options such as gradient accumulation, gradient checkpointing, bf16 mixed precision and a learning rate of 2e-5.[^s4]

## Limitations and open questions

- **Feature distortion under distribution shift.** Kumar et al. (ICLR 2022) found that, averaged over ten distribution-shift datasets, full fine-tuning gained about 2% in-distribution accuracy over linear probing but lost about 7% out-of-distribution.[^s5] Their explanation is that the lower layers drift while a random head is still being learned; fitting a linear probe first and then fine-tuning (LP-FT) recovered much of the gap.[^s5]
- **Catastrophic forgetting.** Training a network on a new task tends to erase what it learned earlier. Kirkpatrick et al. proposed elastic weight consolidation, which slows learning on weights important to earlier tasks, to reduce this effect.[^s6]
- **Cost and storage.** Updating every weight means storing a full copy of the model per task, which motivated parameter-efficient alternatives such as adapters and LoRA. Memory-saving flags in standard trainers address the same pressure.[^s4]

## In practice

Fine-tuning remains the standard way to specialise vision and language models, from swapping a classifier head on an image backbone to adapting an open-weight LLM to a domain corpus.[^s3][^s4] As of November 2026, the Hugging Face Transformers library ships a ready-made `Trainer` workflow for this, including pushing the result to the Hugging Face Hub.[^s4]

## Connections

Fine-tuning **depends on** **pretraining**, which supplies the general features it reuses, and sits under **transfer learning** and **deep learning**.[^s1][^s3] It **contrasts with** **linear probing**, which freezes the backbone, and it **causes** **catastrophic forgetting** when old capabilities are overwritten.[^s5][^s6] It was popularised for NLP by **ULMFiT (Howard and Ruder, 2018)** and is **implemented in** **Hugging Face Transformers**.[^s2][^s4] For LLMs it is an **alternative to** steering a frozen model through **in-context learning**, and it is the base on which **instruction tuning**, **RLHF**, **parameter-efficient fine-tuning** and **QLoRA** build.[^s4]

## Sources

[^s1]: Yosinski, Clune, Bengio and Lipson, "How transferable are features in deep neural networks?", NeurIPS 2014. https://proceedings.nips.cc/paper_files/paper/2014/file/375c71349b295fbe2dcdca9206f20a06-Paper.pdf (accessed 2026-11-11)
[^s2]: Howard and Ruder, "Universal Language Model Fine-tuning for Text Classification", ACL 2018. https://aclanthology.org/P18-1031/ (accessed 2026-11-11)
[^s3]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, §14.2 "Fine-Tuning". https://d2l.ai/chapter_computer-vision/fine-tuning.html (accessed 2026-11-11)
[^s4]: Hugging Face, "Fine-tuning", Transformers documentation. https://huggingface.co/docs/transformers/training (accessed 2026-11-11)
[^s5]: Kumar, Raghunathan, Jones, Ma and Liang, "Fine-Tuning can Distort Pretrained Features and Underperform Out-of-Distribution", ICLR 2022. https://iclr.cc/virtual/2022/poster/5945 (accessed 2026-11-11)
[^s6]: Kirkpatrick et al., "Overcoming catastrophic forgetting in neural networks", PNAS 2017 (arXiv 1612.00796). https://arxiv.org/abs/1612.00796 (accessed 2026-11-11)
