---
id: kt:proximal-policy-optimization
type: Algorithm
title: Proximal policy optimization
aliases: [PPO, PPO-Clip, PPO-Penalty, clipped surrogate objective]
domain: reinforcement-learning
summary: >-
  An on-policy, actor-critic policy-gradient algorithm that reuses each batch of experience for several epochs of
  minibatch updates while a clipped probability-ratio objective keeps each new policy close to the one that
  collected the data.
maturity: established
broader: [kt:policy-gradient, kt:actor-critic]
related: [kt:direct-preference-optimization]
relations:
  - {predicate: introducedIn, object: kt:proximal-policy-optimization-algorithms}
  - {predicate: createdBy, object: kt:openai}
  - {predicate: alternativeTo, object: kt:trust-region-policy-optimization}
  - {predicate: dependsOn, object: kt:generalized-advantage-estimation}
  - {predicate: usedIn, object: kt:rlhf}
sources:
  - id: s1
    title: "Proximal Policy Optimization Algorithms"
    publisher: Schulman, Wolski, Dhariwal, Radford and Klimov (OpenAI), arXiv 1707.06347, 2017
    url: https://arxiv.org/abs/1707.06347
    type: primary
    accessed: 2026-11-13
  - id: s2
    title: "Proximal Policy Optimization Algorithms (v1 full text)"
    publisher: Schulman et al., arXiv 1707.06347v1 PDF
    url: https://arxiv.org/pdf/1707.06347v1
    type: primary
    accessed: 2026-11-13
  - id: s3
    title: "Spinning Up in Deep RL: Proximal Policy Optimization"
    publisher: OpenAI
    url: https://spinningup.openai.com/en/latest/algorithms/ppo.html
    type: lab-research
    accessed: 2026-11-13
  - id: s4
    title: "Implementation Matters in Deep RL: A Case Study on PPO and TRPO"
    publisher: ICLR 2020 (Engstrom, Ilyas, Santurkar, Tsipras, Janoos, Rudolph and Madry)
    url: https://iclr.cc/virtual/2020/poster/1752
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s5
    title: "Training language models to follow instructions with human feedback"
    publisher: NeurIPS 2022 (Ouyang et al., OpenAI)
    url: https://papers.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s6
    title: "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models"
    publisher: Shao et al. (DeepSeek), arXiv 2402.03300, 2024
    url: https://arxiv.org/html/2402.03300v3
    type: primary
    accessed: 2026-11-13
created: 2026-11-13
---

# Proximal policy optimization

Proximal policy optimization (PPO) is a reinforcement learning algorithm that alternates between gathering experience with the current policy and improving that policy by stochastic gradient ascent on a *surrogate* objective. Its key departure from earlier online policy-gradient methods is that the surrogate can be optimized for several passes of minibatch updates over the same batch, instead of one gradient step per sample.[^s1] PPO was proposed in July 2017 by John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford and Oleg Klimov at OpenAI, who presented it as keeping much of the stability of trust region policy optimization (TRPO) while being simpler to implement and more general.[^s1]

## How it works

Let r_t(θ) = π_θ(a_t|s_t) / π_θold(a_t|s_t) be the probability ratio between the policy being trained and the policy that collected the data, and let Â_t be an advantage estimate. The clipped objective, used by the variant usually called PPO-Clip, is:[^s2][^s3]

L^CLIP(θ) = Ê_t[ min( r_t(θ)·Â_t , clip(r_t(θ), 1−ε, 1+ε)·Â_t ) ]

Taking the minimum makes this a pessimistic bound: once the ratio has moved past 1+ε for a good action, or below 1−ε for a bad one, the term stops improving, so the optimizer gains nothing by pushing the new policy further from the old one.[^s2][^s3] OpenAI's reference documentation describes ε as a small hyperparameter, roughly 0.1 to 0.3, and its implementation also stops the gradient steps early when the mean KL divergence from the old policy exceeds a target.[^s3]

A second variant, PPO-Penalty, subtracts a KL-divergence penalty β·KL[π_old, π_θ] instead of clipping, and adapts β after each update: it is halved when the measured KL falls well below a target and doubled when it overshoots.[^s2] When the policy and value function share a network, the full loss adds a squared-error value term and an entropy bonus that encourages exploration, L^CLIP − c₁L^VF + c₂S.[^s2] Each iteration runs N parallel actors for T timesteps, computes advantages, then optimizes the loss for K epochs with minibatches drawn from the NT samples, typically with Adam.[^s2] OpenAI's implementation estimates advantages with generalized advantage estimation and supports both discrete and continuous action spaces.[^s3]

## Evidence

In the original paper's continuous-control comparison over seven MuJoCo tasks, clipping with ε = 0.2 achieved the best average normalized score (0.82), ahead of the best adaptive-KL setting (0.74), while dropping both clipping and the penalty scored −0.39.[^s2] On 49 Atari games, PPO won 30 when scored by average reward across all of training, against 18 for ACER and 1 for A2C; scored by the final 100 episodes, ACER led with 28 to PPO's 19, so PPO's advantage was mainly in learning speed.[^s2] Compared with TRPO, which enforces a hard KL constraint using a conjugate-gradient, second-order-style solver, PPO needs only first-order optimizers.[^s2]

## Limitations

PPO is on-policy: data must come from the current policy, so old experience cannot be replayed as in off-policy methods, and the stochastic policy tends to become more deterministic over training, which can trap it in local optima.[^s3] Its reported performance also depends heavily on details outside the core objective. An ICLR 2020 study by Engstrom et al. found that "code-level optimizations" omitted from the algorithm's description accounted for most of PPO's reward gain over TRPO and changed how the method behaves.[^s4] Results therefore need careful attribution between the clipping idea and the implementation around it.[^s4]

## In practice

PPO became the standard optimizer for reinforcement learning from human feedback on language models. In OpenAI's InstructGPT work (NeurIPS 2022), a supervised policy was fine-tuned with PPO against a learned reward model, with a per-token KL penalty toward the supervised model to limit reward over-optimization; a "PPO-ptx" variant mixed in pretraining gradients to reduce regressions on public NLP datasets.[^s5] The authors reported that labelers preferred outputs of the 1.3B-parameter InstructGPT model over those of the 175B GPT-3.[^s5] Later work modified PPO for LLMs: DeepSeek's group relative policy optimization (GRPO, 2024) drops the separate value model, which the authors note is typically comparable in size to the policy, and instead uses the mean and standard deviation of rewards across a group of sampled answers as the baseline.[^s6]

## Connections

PPO is a **policy-gradient** method with **actor-critic** structure: the policy is updated from advantage estimates supplied by a learned value function, and it **depends on generalized advantage estimation** in common implementations.[^s2][^s3] It was **introduced in** *Proximal Policy Optimization Algorithms* and **created by OpenAI** researchers.[^s1] It is an **alternative to trust region policy optimization**, aiming for similar stability with first-order updates.[^s1][^s2] It is **used in** **RLHF**, where it optimizes a language model against a reward model under a KL penalty.[^s5] **Direct preference optimization** is related as the main reward-model-free alternative for preference tuning, and GRPO shows how the PPO objective has been adapted to reduce memory cost in LLM training.[^s6]

## Sources

[^s1]: Schulman, Wolski, Dhariwal, Radford and Klimov, "Proximal Policy Optimization Algorithms", arXiv 1707.06347, 2017. https://arxiv.org/abs/1707.06347 (accessed 2026-11-13)
[^s2]: Schulman et al., "Proximal Policy Optimization Algorithms", full text v1. https://arxiv.org/pdf/1707.06347v1 (accessed 2026-11-13)
[^s3]: OpenAI, "Spinning Up in Deep RL: Proximal Policy Optimization". https://spinningup.openai.com/en/latest/algorithms/ppo.html (accessed 2026-11-13)
[^s4]: Engstrom, Ilyas, Santurkar, Tsipras, Janoos, Rudolph and Madry, "Implementation Matters in Deep RL: A Case Study on PPO and TRPO", ICLR 2020. https://iclr.cc/virtual/2020/poster/1752 (accessed 2026-11-13)
[^s5]: Ouyang et al., "Training language models to follow instructions with human feedback", NeurIPS 2022. https://papers.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf (accessed 2026-11-13)
[^s6]: Shao et al., "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models", arXiv 2402.03300, 2024. https://arxiv.org/html/2402.03300v3 (accessed 2026-11-13)
