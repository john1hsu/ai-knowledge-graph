---
id: kt:hugging-face-trl
type: Tool
title: Hugging Face TRL
aliases: [TRL, Transformer Reinforcement Learning, Transformers Reinforcement Learning, trl library]
domain: training-and-adaptation
summary: >-
  An open-source Python library from Hugging Face for post-training transformer language models, providing
  ready-made trainers for supervised fine-tuning, reward modeling, preference optimization (DPO, KTO) and online
  reinforcement learning (GRPO, RLOO), built on top of the Hugging Face Transformers library.
maturity: established
broader: [kt:post-training, kt:fine-tuning]
related: [kt:rlhf, kt:direct-preference-optimization, kt:instruction-tuning, kt:qlora, kt:knowledge-distillation, kt:reward-model, kt:parameter-efficient-fine-tuning]
relations:
  - {predicate: createdBy, object: kt:hugging-face}
  - {predicate: dependsOn, object: kt:hugging-face-transformers}
  - {predicate: basedOn, object: kt:proximal-policy-optimization}
sources:
  - id: s1
    title: "TRL documentation: TRL - Transformers Reinforcement Learning (main)"
    publisher: Hugging Face
    url: https://huggingface.co/docs/trl/main/index
    type: official-docs
    accessed: 2026-11-14
  - id: s2
    title: "TRL documentation (v1.9.0): Quickstart"
    publisher: Hugging Face
    url: https://huggingface.co/docs/trl/v1.9.0/quickstart
    type: official-docs
    accessed: 2026-11-14
  - id: s3
    title: "TRL v1.0: Post-Training Library Built to Move with the Field"
    publisher: Hugging Face blog, 31 March 2026 (Gallouédec, Liu, Cuenca and Paniego)
    url: https://huggingface.co/blog/trl-v1
    type: primary
    accessed: 2026-11-14
  - id: s4
    title: "Fine-tuning 20B LLMs with RLHF on a 24GB consumer GPU"
    publisher: Hugging Face blog, 9 March 2023 (Beeching, Younes B., von Werra, Mangrulkar, Tunstall and Rasul)
    url: https://huggingface.co/blog/trl-peft
    type: primary
    accessed: 2026-11-14
  - id: s5
    title: "Fine-Tuning Language Models from Human Preferences"
    publisher: arXiv:1909.08593 (Ziegler, Stiennon, Wu, Brown, Radford, Amodei, Christiano and Irving), 2019
    url: https://arxiv.org/abs/1909.08593
    type: primary
    accessed: 2026-11-14
  - id: s6
    title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
    publisher: arXiv:2402.03300 (Shao et al., DeepSeek-AI), 2024
    url: https://arxiv.org/abs/2402.03300
    type: primary
    accessed: 2026-11-14
created: 2026-11-14
---

# Hugging Face TRL

**TRL** (Transformers Reinforcement Learning) is Hugging Face's open-source library for *post-training* transformer language models: taking a pretrained checkpoint and adapting it with supervised fine-tuning (SFT), reward modeling, preference optimization such as Direct Preference Optimization (DPO), and online reinforcement learning such as Group Relative Policy Optimization (GRPO). The documentation describes it as a full-stack toolkit integrated with the Hugging Face Transformers library.[^s1] Despite the "reinforcement learning" in its name, most day-to-day use is SFT and offline preference training; RL is one family of methods among several.[^s1][^s3]

## Origin and evolution

According to the maintainers, TRL's first commit dates back more than six years before its v1.0 release, and it grew from a research codebase into a general library.[^s3] By early 2023 its focus was the reinforcement-learning step of the RLHF recipe: fine-tune a model on demonstrations, train a reward model on human comparisons, then optimize the policy against that reward with PPO.[^s4] That pipeline follows the reward-learning setup of Ziegler et al. (2019), who trained a reward model from human judgments and then tuned a pretrained language model against it with RL on stylistic continuation and summarization tasks.[^s5] A March 2023 Hugging Face post showed TRL's PPO combined with 8-bit loading and LoRA adapters fitting a 20-billion-parameter model's RL fine-tuning onto a 24 GB consumer GPU; because adapters can be switched off, the same weights double as the frozen reference model, avoiding a second model copy.[^s4]

TRL v1.0 was announced on 31 March 2026. The maintainers reported that the library then implemented more than 75 post-training methods, and split them into a **stable core** that follows semantic versioning (SFT, DPO, reward modeling, RLOO and GRPO plus close variants) and an **experimental** namespace (for example `trl.experimental.orpo`) with no stability guarantee; methods graduate based on usage relative to maintenance cost.[^s3] The same post cited about 3 million PyPI downloads per month and 17.8k GitHub stars, and noted that Unsloth and Axolotl build directly on TRL's trainers (figures as reported by Hugging Face, March 2026).[^s3]

## How it works

Each method is exposed as a `Trainer` subclass that takes a model (or a Hub model name) and a dataset and is launched with `trainer.train()`. The quickstart shows `SFTTrainer`, `GRPOTrainer` with a reward function, `DPOTrainer` and `RewardTrainer` following this pattern, and a command-line interface (`trl sft`, `trl dpo`, `trl reward`) runs the same recipes without writing code.[^s2] As of November 2026 the main-branch documentation groups trainers into online methods (GRPO, RLOO), reward modeling, offline methods (SFT, DPO, KTO) and knowledge distillation, with further experimental trainers such as ORPO, CPO, Online DPO and GKD.[^s1]

GRPO, now one of TRL's flagship trainers, was introduced in the DeepSeekMath paper as a variant of PPO that improves mathematical reasoning while reducing PPO's memory use.[^s6] TRL's design guidance favours explicit, local implementations over deep class hierarchies and accepts code duplication; the maintainers note that their RLOO and GRPO trainers are nearly line-for-line duplicates by design, and call an earlier generic `Judge` abstraction a mistake.[^s3]

## Scaling and integrations

The documentation lists PEFT integration for LoRA and QLoRA, DeepSpeed, vLLM for fast generation during online RL, and community integrations including Unsloth and Liger Kernel.[^s2] The v1.0 post says TRL supports multi-node DeepSpeed and FSDP training but lacks native tensor parallelism, a trade-off against heavier RL frameworks.[^s3] The main documentation also lists guides for training beyond one million tokens of context and for running on AMD Instinct GPUs and AWS Trainium (as of November 2026).[^s1]

## Limitations

TRL prioritises breadth and fast adoption of new methods, so many algorithms live in the experimental layer and may change between releases.[^s3] Large-scale online RL is bounded by generation throughput and by the lack of native tensor parallelism, which is why distributed setups pair it with vLLM and DeepSpeed or FSDP.[^s2][^s3]

## Connections

TRL is a toolkit for **post-training** and **fine-tuning** (`broader`). It is a common implementation of **RLHF**, **DPO** and **instruction tuning**, which is why those articles point to it via `implementedIn`.[^s4][^s1] It **depends on** Hugging Face Transformers for model definitions and is **created by** Hugging Face.[^s1] Its RLHF workflow was built around **PPO** (`basedOn`), and its GRPO trainer implements a PPO variant.[^s4][^s6] It is used together with **parameter-efficient fine-tuning** and **QLoRA** to cut memory,[^s2][^s4] trains **reward models**,[^s2] and includes **knowledge distillation** trainers.[^s1]

## Sources
[^s1]: Hugging Face, "TRL - Transformers Reinforcement Learning" documentation (main). https://huggingface.co/docs/trl/main/index (accessed 2026-11-14)
[^s2]: Hugging Face, TRL documentation v1.9.0, "Quickstart". https://huggingface.co/docs/trl/v1.9.0/quickstart (accessed 2026-11-14)
[^s3]: Gallouédec, Liu, Cuenca and Paniego, "TRL v1.0: Post-Training Library Built to Move with the Field", Hugging Face blog, 31 March 2026. https://huggingface.co/blog/trl-v1 (accessed 2026-11-14)
[^s4]: Beeching et al., "Fine-tuning 20B LLMs with RLHF on a 24GB consumer GPU", Hugging Face blog, 9 March 2023. https://huggingface.co/blog/trl-peft (accessed 2026-11-14)
[^s5]: Ziegler et al., "Fine-Tuning Language Models from Human Preferences", arXiv:1909.08593, 2019. https://arxiv.org/abs/1909.08593 (accessed 2026-11-14)
[^s6]: Shao et al., "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models", arXiv:2402.03300, 2024. https://arxiv.org/abs/2402.03300 (accessed 2026-11-14)
