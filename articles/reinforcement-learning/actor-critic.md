---
id: kt:actor-critic
type: Technique
title: Actor-critic
aliases: [actor-critic algorithms, actor-critic architecture]
domain: reinforcement-learning
summary: >-
  A reinforcement learning design that trains two coupled function approximators: an actor, which is the
  parameterized policy that chooses actions, and a critic, which learns value estimates used to score and
  correct the actor's updates.
maturity: established
broader: [kt:policy-gradient, kt:reinforcement-learning]
related: [kt:q-learning, kt:markov-decision-process, kt:deep-learning]
relations:
  - {predicate: dependsOn, object: kt:temporal-difference-learning}
  - {predicate: enables, object: kt:asynchronous-advantage-actor-critic}
  - {predicate: enables, object: kt:soft-actor-critic}
  - {predicate: alternativeTo, object: kt:q-learning}
sources:
  - id: s1
    title: "Actor-Critic Algorithms"
    publisher: Advances in Neural Information Processing Systems 12 (NIPS 1999) (Konda and Tsitsiklis)
    url: https://papers.nips.cc/paper/1786-actor-critic-algorithms
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s2
    title: "Asynchronous Methods for Deep Reinforcement Learning"
    publisher: Proceedings of the 33rd ICML, PMLR 48:1928-1937, 2016 (Mnih et al.)
    url: https://proceedings.mlr.press/v48/mniha16.html
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s3
    title: "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor"
    publisher: Proceedings of the 35th ICML, PMLR 80:1861-1870, 2018 (Haarnoja, Zhou, Abbeel and Levine)
    url: https://proceedings.mlr.press/v80/haarnoja18b.html
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s4
    title: "Deep RL Course, Unit 6: Advantage Actor-Critic (A2C)"
    publisher: Hugging Face
    url: https://huggingface.co/learn/deep-rl-course/unit6/advantage-actor-critic
    type: official-docs
    accessed: 2026-11-08
  - id: s5
    title: "Spinning Up in Deep RL: Soft Actor-Critic"
    publisher: OpenAI
    url: https://spinningup.openai.com/en/latest/algorithms/sac.html
    type: lab-research
    accessed: 2026-11-08
created: 2026-11-08
---

# Actor-critic

Actor-critic is a way of organizing a reinforcement learning agent around two learned components instead of one. The **actor** is a parameterized policy π_θ that decides which action to take in each state. The **critic** is a value function with its own parameters w that judges how good those actions turned out to be.[^s4] The critic's judgement is fed back to the actor, which shifts its parameters in an approximate gradient direction so that well-rated actions become more likely.[^s1] The design sits between two older families: methods that learn only a policy, and methods that learn only values and act greedily on them.[^s4]

## Origin

Konda and Tsitsiklis gave one of the standard formal treatments at NIPS 1999. They studied actor-critic algorithms for simulation-based optimization of a Markov decision process, with randomized stationary policies drawn from a parameterized family.[^s1] In their scheme the critic runs temporal-difference (TD) learning with a linear approximation architecture, while the actor follows the approximate gradient the critic supplies. They described the algorithms as two-time-scale, meaning both parts learn together but at different rates.[^s1] A key structural finding was that the critic does not need to represent everything about the environment. Its features only need to span a subspace determined by how the actor's policy is parameterized.[^s1]

## How it works

A single interaction step makes the division of labour concrete. The agent observes state S_t, the actor proposes action A_t, and the critic scores that state-action pair. Acting yields reward R_{t+1} and the next state S_{t+1}. The actor then updates its policy parameters using the critic's score, and the critic updates its own parameters before the cycle repeats.[^s4]

Most modern variants score actions with an **advantage**, A(s, a) = Q(s, a) − V(s), rather than a raw action value. A positive advantage means the action beat the state's average and should be reinforced; a negative one means it should be suppressed.[^s4] Computing the advantage exactly would require two value functions. In practice the one-step TD error, δ = r + γV(s′) − V(s), is used as an estimate of it, so the critic only has to learn V.[^s4] Hugging Face's course presents this advantage actor-critic (A2C) form as a fix for the high variance of REINFORCE-style updates, which otherwise weight every action by a noisy whole-episode return.[^s4]

## Notable algorithms

**Asynchronous actor-critic (A3C).** Mnih and colleagues at DeepMind (ICML 2016) ran several actor-learners in parallel, each updating shared network parameters asynchronously. They reported that this parallelism stabilized training of deep neural network controllers without a replay buffer.[^s2] The authors claimed their asynchronous actor-critic variant surpassed the then state of the art on Atari while training for half the time on a single multi-core CPU instead of a GPU. They also reported success on continuous motor control and on navigating random 3D mazes from pixels.[^s2]

**Soft actor-critic (SAC).** Haarnoja, Zhou, Abbeel and Levine (ICML 2018) targeted two weaknesses of model-free deep RL: high sample complexity and brittle convergence that needs careful tuning.[^s3] SAC is off-policy, reusing past transitions from a replay buffer, and its actor maximizes expected reward plus policy entropy, so it aims to succeed while acting as randomly as possible.[^s3][^s5] The authors reported state-of-the-art results on continuous-control benchmarks and similar performance across random seeds, in contrast with other off-policy methods of the time.[^s3] OpenAI's Spinning Up implementation trains two Q-function critics and takes the minimum of their estimates, uses polyak-averaged target networks, and weights the entropy bonus with a temperature α that trades exploration against exploitation.[^s5]

## Limitations and practical notes

Actor-critic methods inherit a bias-variance trade-off: a learned critic reduces the variance of the actor's gradient signal, but its errors bias that signal, which is why the theory places conditions on the critic's features.[^s1] Coupled training also means the critic chases a moving target as the policy changes; the two-time-scale analysis exists to make that interaction tractable.[^s1] Deep variants add their own fixes for instability, such as parallel actor-learners in A3C or clipped double-Q critics and target networks in SAC.[^s2][^s5] Implementation details matter: Spinning Up's SAC supports only continuous action spaces, and discrete actions require a changed policy update.[^s5]

## Connections

Actor-critic is a refinement within **policy gradient** methods and, more broadly, a core design in **reinforcement learning** over **Markov decision processes**: the actor is the policy-gradient learner and the critic supplies its gradient signal.[^s1] It **depends on** **temporal-difference learning**, which the critic uses to estimate values and whose error doubles as the advantage estimate.[^s1][^s4] It is an **alternative to** purely value-based methods such as **Q-learning**, though SAC's critics are trained with a Q-learning-style regression to a shared target, showing how the two lines merge.[^s5] The design **enables** later algorithms, notably **asynchronous advantage actor-critic** and **soft actor-critic**, both of which use **deep learning** networks for actor and critic.[^s2][^s3]

## Sources

[^s1]: V. R. Konda and J. N. Tsitsiklis, "Actor-Critic Algorithms", Advances in Neural Information Processing Systems 12 (NIPS 1999). https://papers.nips.cc/paper/1786-actor-critic-algorithms (accessed 2026-11-08)
[^s2]: V. Mnih et al., "Asynchronous Methods for Deep Reinforcement Learning", Proceedings of the 33rd International Conference on Machine Learning, PMLR 48:1928-1937, 2016. https://proceedings.mlr.press/v48/mniha16.html (accessed 2026-11-08)
[^s3]: T. Haarnoja, A. Zhou, P. Abbeel and S. Levine, "Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor", Proceedings of the 35th International Conference on Machine Learning, PMLR 80:1861-1870, 2018. https://proceedings.mlr.press/v80/haarnoja18b.html (accessed 2026-11-08)
[^s4]: Hugging Face, "Deep RL Course, Unit 6: Advantage Actor-Critic (A2C)". https://huggingface.co/learn/deep-rl-course/unit6/advantage-actor-critic (accessed 2026-11-08)
[^s5]: OpenAI, "Spinning Up in Deep RL: Soft Actor-Critic". https://spinningup.openai.com/en/latest/algorithms/sac.html (accessed 2026-11-08)
