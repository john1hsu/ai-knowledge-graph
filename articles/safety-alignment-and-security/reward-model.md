---
id: kt:reward-model
type: Technique
title: Reward model
aliases: [reward modeling, learned reward model, preference model, RM]
domain: safety-alignment-and-security
summary: >-
  A learned function, usually a neural network trained on human comparisons between outputs, that assigns a scalar
  score standing in for human judgement, so that a policy can be optimized against it with reinforcement learning or
  used to rank and filter candidate outputs.
maturity: established
broader: [kt:ai-alignment, kt:reinforcement-learning]
related: [kt:reward-hacking, kt:goodharts-law, kt:scalable-oversight, kt:test-time-compute, kt:hugging-face-trl]
relations:
  - {predicate: partOf, object: kt:rlhf}
  - {predicate: introducedIn, object: kt:deep-reinforcement-learning-from-human-preferences}
  - {predicate: basedOn, object: kt:bradley-terry-model}
  - {predicate: usedIn, object: kt:proximal-policy-optimization}
  - {predicate: alternativeTo, object: kt:direct-preference-optimization}
  - {predicate: evaluatedOn, object: kt:rewardbench}
sources:
  - id: s1
    title: "Deep Reinforcement Learning from Human Preferences"
    publisher: NeurIPS 2017 (Christiano, Leike, Brown, Martic, Legg, Amodei)
    url: https://proceedings.neurips.cc/paper/2017/file/d5e2c0adad503c91f91df240d0cd4e49-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s2
    title: "Training language models to follow instructions with human feedback"
    publisher: NeurIPS 2022 (Ouyang et al., OpenAI)
    url: https://papers.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "Scalable agent alignment via reward modeling: a research direction"
    publisher: arXiv:1811.07871v1 (Leike, Krueger, Everitt, Martic, Maini, Legg), November 2018
    url: https://arxiv.org/abs/1811.07871v1
    type: primary
    accessed: 2026-11-15
  - id: s4
    title: "Scaling Laws for Reward Model Overoptimization"
    publisher: ICML 2023, PMLR 202 (Gao, Schulman, Hilton)
    url: https://proceedings.mlr.press/v202/gao23h.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "RewardBench: Evaluating Reward Models for Language Modeling"
    publisher: arXiv:2403.13787 (Lambert et al., Allen Institute for AI and University of Washington), March 2024
    url: https://arxiv.org/abs/2403.13787
    type: primary
    accessed: 2026-11-15
  - id: s6
    title: "Let's Verify Step by Step"
    publisher: ICLR 2024 (Lightman et al., OpenAI)
    url: https://proceedings.iclr.cc/paper_files/paper/2024/hash/aca97732e30bcf1303bc22ac3924fd16-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Reward model

A **reward model** (RM) is a learned scoring function that predicts how a human would judge an agent's behaviour or a language model's response. Instead of hand-writing a reward function, designers collect human feedback, usually comparisons between two or more outputs, fit a model to it, and then optimize a policy against the model's predicted reward.[^s1][^s3] Leike and colleagues at DeepMind framed this two-step recipe (learn a reward from user interaction, then optimize it with reinforcement learning) as a research direction for the agent alignment problem, motivated by the observation that people usually understand their goals only implicitly and cannot easily write them down.[^s3]

## Origin

The modern form comes from Christiano et al. (NeurIPS 2017). Their reward predictor maps observation–action pairs to a scalar, and is trained so that the summed reward of a trajectory segment predicts which of two short clips a human prefers.[^s1] Humans labelled fewer than 1% of the agent's interactions, yet this was enough to train MuJoCo agents close to the performance of RL on the true reward with about 700 labels, and to teach a simulated Hopper a backflip from 900 queries taking under an hour of human time.[^s1] The same paper gave the earliest clear warning about exploitation: when the reward predictor was trained offline rather than interleaved with policy training, a Pong agent learned to avoid conceding points without ever scoring, producing endless volleys.[^s1]

## How it works

Most reward models use a Bradley–Terry preference likelihood. If a model assigns scores r(x, y_w) and r(x, y_l) to a preferred and a dispreferred response to prompt x, the probability that the first is preferred is modelled as σ(r(x, y_w) − r(x, y_l)), and training minimizes the negative log of that probability over the comparison data.[^s1][^s2] Christiano et al. additionally trained an ensemble of predictors, assumed a 10% chance that a human answers at random, and used ensemble disagreement to choose which pairs to show labellers.[^s1]

InstructGPT (Ouyang et al., NeurIPS 2022) adapted the recipe to language models. A GPT-3 model fine-tuned to output a scalar for a prompt–response pair was trained on rankings of 4 to 9 responses per prompt, with every pairwise comparison from one prompt placed in a single batch element for efficiency; the RM dataset drew on about 33,000 training prompts.[^s2] OpenAI used a 6B-parameter RM rather than 175B, reporting that the larger model trained less stably and was less suitable as the PPO value function, which was initialized from the RM. A per-token KL penalty toward the supervised fine-tuned model was added during RL to discourage over-optimizing the reward model.[^s2] Labeller agreement in that work was roughly 73–77%, a reminder that the target the RM learns is itself noisy.[^s2]

Reward models are not only training signals. They can rerank samples at inference time (best-of-n), and *process* reward models score each intermediate reasoning step rather than only the final answer. Lightman et al. (ICLR 2024) found process supervision significantly outperformed outcome supervision on MATH, with their best process-supervised model solving 78% of a representative test subset, and released PRM800K, a set of 800,000 step-level human labels.[^s6]

## Limitations and open questions

Because an RM is only a proxy for human judgement, optimizing hard against it eventually degrades true quality, an instance of Goodhart's law. Gao, Schulman and Hilton (ICML 2023) studied this with a synthetic "gold" reward model labelling data for a smaller proxy: as optimization pressure rose, gold-standard reward followed a different functional form for RL than for best-of-n sampling, and the coefficients scaled smoothly with reward-model size.[^s4] Evaluating RMs directly is also hard. RewardBench (Lambert et al., 2024) scores models on prompt–chosen–rejected trios spanning chat, reasoning and safety, where the better answer is preferred for subtle but verifiable reasons, and its authors reported weaknesses around refusals, reasoning and instruction following across both classifier-style RMs and implicit rewards from DPO-trained models.[^s5] Scaling reward modelling to tasks humans cannot easily judge remains an open alignment problem.[^s3]

## Connections

The RM is the central component of **RLHF**, where it supplies the reward that **proximal policy optimization** maximizes.[^s2] It was introduced in its current form by *Deep Reinforcement Learning from Human Preferences* and rests on the **Bradley–Terry model** of paired comparisons.[^s1] Over-optimizing it is the textbook route to **reward hacking**, a concrete case of **Goodhart's law**.[^s4] **Direct Preference Optimization** is an alternative that skips the explicit RM, and **RewardBench** benchmarks both kinds.[^s5] Process reward models used to rerank or guide reasoning connect it to **test-time compute**, and the difficulty of supplying reliable feedback on hard tasks ties it to **scalable oversight** and **AI alignment** more broadly.[^s3][^s6]

## Sources

[^s1]: Christiano et al., "Deep Reinforcement Learning from Human Preferences", NeurIPS 2017. https://proceedings.neurips.cc/paper/2017/file/d5e2c0adad503c91f91df240d0cd4e49-Paper.pdf (accessed 2026-11-15)
[^s2]: Ouyang et al., "Training language models to follow instructions with human feedback", NeurIPS 2022. https://papers.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf (accessed 2026-11-15)
[^s3]: Leike et al., "Scalable agent alignment via reward modeling: a research direction", arXiv:1811.07871, 2018. https://arxiv.org/abs/1811.07871v1 (accessed 2026-11-15)
[^s4]: Gao, Schulman, Hilton, "Scaling Laws for Reward Model Overoptimization", ICML 2023. https://proceedings.mlr.press/v202/gao23h.html (accessed 2026-11-15)
[^s5]: Lambert et al., "RewardBench: Evaluating Reward Models for Language Modeling", arXiv:2403.13787, 2024. https://arxiv.org/abs/2403.13787 (accessed 2026-11-15)
[^s6]: Lightman et al., "Let's Verify Step by Step", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/aca97732e30bcf1303bc22ac3924fd16-Abstract-Conference.html (accessed 2026-11-15)
