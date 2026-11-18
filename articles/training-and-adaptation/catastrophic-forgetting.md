---
id: kt:catastrophic-forgetting
type: Risk
title: Catastrophic forgetting
aliases: [catastrophic interference, forgetting in sequential learning]
domain: training-and-adaptation
summary: >-
  The tendency of a neural network trained by gradient descent to abruptly lose previously learned knowledge or skills
  when it is trained on new tasks or data without continued access to the old ones; the central obstacle in continual
  learning and a known side effect of fine-tuning.
maturity: foundational
broader: [kt:continual-learning, kt:artificial-neural-network]
related: [kt:fine-tuning, kt:parameter-efficient-fine-tuning, kt:transfer-learning, kt:instruction-tuning, kt:regularization]
relations:
  - {predicate: mitigatedBy, object: kt:elastic-weight-consolidation}
  - {predicate: mitigatedBy, object: kt:experience-replay}
  - {predicate: partOf, object: kt:stability-plasticity-dilemma}
  - {predicate: contrastsWith, object: kt:overfitting}
sources:
  - id: s1
    title: "Overcoming catastrophic forgetting in neural networks"
    publisher: arXiv:1612.00796 (Kirkpatrick et al., DeepMind and Imperial College London; authors' version)
    url: https://arxiv.org/pdf/1612.00796
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "Pseudo-recurrent connectionist networks: An approach to the 'sensitivity–stability' dilemma"
    publisher: Connection Science 9(4), 353–379, 1997 (Robert M. French)
    url: https://itb.biologie.hu-berlin.de/~kempter/Teaching/2003_SS_Seminar/Literature/french97.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "Three types of incremental learning"
    publisher: Nature Machine Intelligence 4, 1185–1197, 2022 (van de Ven, Tuytelaars and Tolias)
    url: https://www.nature.com/articles/s42256-022-00568-3.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning"
    publisher: arXiv:2308.08747 (Luo, Yang, Meng, Li, Zhou and Zhang), v5 2025
    url: https://arxiv.org/abs/2308.08747v5
    type: preprint
    accessed: 2026-11-18
  - id: s5
    title: "LoRA Learns Less and Forgets Less"
    publisher: arXiv:2405.09673 (Biderman et al.), v2 2024
    url: https://arxiv.org/abs/2405.09673v2
    type: primary
    accessed: 2026-11-18
created: 2026-11-18
---

# Catastrophic forgetting

**Catastrophic forgetting** (also called **catastrophic interference**) is what happens when a neural network that has learned one task is trained on a second one and, in the process, loses much of its ability to perform the first. Unlike gradual human forgetting, the loss can be abrupt and nearly complete. The phenomenon was described for backpropagation networks by McCloskey and Cohen (1989) and Ratcliff (1990), and it remains the central obstacle for any system that must learn from a stream of tasks or data rather than from one fixed, shuffled dataset.[^s2][^s1]

## Why it happens

Standard networks store knowledge in **overlapping, distributed representations**: the same weights participate in many learned mappings. When gradient descent optimises only the loss of the new task, it freely moves weights that the old task depended on, because nothing in the objective says they matter. French summarised the cause directly: forgetting follows from the overlap of distributed representations.[^s2] Training on all tasks at once (multitask learning with interleaved data) avoids the problem because every update is checked against every task, but this is impractical when data arrive sequentially or old data are no longer available.[^s1]

The tension is often called the **stability–plasticity dilemma** (Carpenter and Grossberg) or the sensitivity–stability problem: a learner must stay plastic enough to absorb new information yet stable enough not to be overwritten by it. A lookup table is perfectly stable but cannot generalise; a backpropagation network generalises well but is highly sensitive to new input.[^s2]

## Mitigation strategies

Research has converged on three broad families of remedies:

- **Replay (rehearsal).** Interleave stored examples of earlier tasks with new training data, or generate stand-ins for them (*pseudo-rehearsal* or *generative replay*), so the old objectives keep shaping the gradients.[^s2][^s3]
- **Parameter regularisation.** Penalise changes to weights that were important for earlier tasks. The best-known example is **elastic weight consolidation** (EWC).[^s1]
- **Architectural separation.** Reduce representational overlap with sparse or orthogonalised codes, dual fast/slow memory systems inspired by the hippocampus and neocortex, or task-specific parameters added on top of a frozen network.[^s2]

EWC, introduced by Kirkpatrick and colleagues at DeepMind, takes a Bayesian view: the posterior over weights after task A becomes the prior for task B. Approximating that posterior as a Gaussian whose precision is the diagonal of the **Fisher information matrix**, the task-B loss gains a quadratic penalty, λ/2 · Σᵢ Fᵢ (θᵢ − θ\*ₐ,ᵢ)², which acts like a spring of importance-dependent stiffness pulling each weight back toward its task-A value. On permuted-MNIST sequences EWC learned new tasks without significant loss on old ones, whereas plain L2 regularisation constrained every weight equally and left too little capacity; on a sequence of Atari 2600 games it let one DQN agent retain several games, though not at the level of separately trained networks. The authors flagged the diagonal Fisher approximation as the method's main weakness.[^s1]

## How hard the problem is depends on the setting

Van de Ven, Tuytelaars and Tolias (2022) distinguish three continual-learning scenarios: **task-incremental** (the task identity is given at test time), **domain-incremental** (inputs shift but the output space is fixed) and **class-incremental** (the model must discriminate a growing set of classes that were never seen together). On Split MNIST and Split CIFAR-100, regularisation methods such as EWC and Synaptic Intelligence came close to the multitask upper bound in the task-incremental case but performed roughly as badly as naive sequential training in the class-incremental case. Replay was the only family that ranked among the top performers in all three scenarios, and simple experience replay often beat more elaborate methods.[^s3]

## Forgetting in large language models

The problem resurfaces when foundation models are adapted. Luo et al. continually fine-tuned LLMs from 1B to 7B parameters and observed catastrophic forgetting at every size; within that range, larger models forgot more, which the authors suggest may reflect their stronger starting performance. They also report that the decoder-only BLOOMZ forgot less than the encoder-decoder mT0, and that general instruction tuning beforehand reduced later forgetting (a 2023 preprint, revised 2025, not yet peer reviewed).[^s4]

Parameter-efficient methods change the trade-off. Biderman et al. (2024) compared LoRA with full fine-tuning on code and mathematics, in both instruction-tuning and continued-pretraining regimes. LoRA generally underperformed full fine-tuning on the target domain but preserved the base model's abilities outside it better, forgetting less than when weight decay or dropout were used as regularisers; the authors found that full fine-tuning learns weight perturbations of 10–100× higher rank than typical LoRA settings.[^s5] In practice, teams adapting LLMs combine these levers: mixing a share of general-purpose data into fine-tuning sets (replay), keeping base weights frozen behind adapters, and re-running broad evaluations after every adaptation step.[^s3][^s5]

## Connections

Catastrophic forgetting is the defining failure mode of **continual learning** and a property of **artificial neural networks** trained by gradient descent, so both are its broader concepts.[^s1][^s2] It is a recognised side effect of **fine-tuning** and **instruction tuning** of pretrained models, and the reason **parameter-efficient fine-tuning** methods such as LoRA are valued for preserving base capabilities.[^s4][^s5] It sits in tension with **transfer learning**, which aims to reuse prior knowledge rather than overwrite it.[^s1] It is **mitigated by** **elastic weight consolidation**, which borrows the logic of **regularisation** but weights each parameter by its importance, and by **experience replay**, the remedy that holds up best across scenarios.[^s1][^s3] It is one side of the **stability–plasticity dilemma**: forgetting is what too much plasticity costs.[^s2] It contrasts with **overfitting**: overfitting fits one dataset too closely, whereas forgetting erases a fit to an earlier one.[^s2]

## Sources
[^s1]: Kirkpatrick et al., "Overcoming catastrophic forgetting in neural networks", arXiv:1612.00796. https://arxiv.org/pdf/1612.00796 (accessed 2026-11-18)
[^s2]: R. M. French, "Pseudo-recurrent connectionist networks: An approach to the 'sensitivity–stability' dilemma", Connection Science 9(4), 1997. https://itb.biologie.hu-berlin.de/~kempter/Teaching/2003_SS_Seminar/Literature/french97.pdf (accessed 2026-11-18)
[^s3]: van de Ven, Tuytelaars and Tolias, "Three types of incremental learning", Nature Machine Intelligence 4, 2022. https://www.nature.com/articles/s42256-022-00568-3.pdf (accessed 2026-11-18)
[^s4]: Luo et al., "An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning", arXiv:2308.08747. https://arxiv.org/abs/2308.08747v5 (accessed 2026-11-18)
[^s5]: Biderman et al., "LoRA Learns Less and Forgets Less", arXiv:2405.09673. https://arxiv.org/abs/2405.09673v2 (accessed 2026-11-18)
