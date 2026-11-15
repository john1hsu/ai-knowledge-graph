---
id: kt:sarsa
type: Algorithm
title: SARSA
aliases: [Sarsa, State-Action-Reward-State-Action, Modified Connectionist Q-Learning, MCQ-L, on-policy TD control]
domain: reinforcement-learning
summary: >-
  An on-policy temporal-difference control algorithm that learns action values by updating each
  state-action estimate toward the reward plus the discounted value of the next action the agent
  actually takes, so the values it learns reflect the agent's own exploratory behaviour.
maturity: foundational
broader: [kt:temporal-difference-learning, kt:reinforcement-learning]
related: [kt:exploration-exploitation, kt:markov-decision-process, kt:actor-critic, kt:expected-sarsa, kt:function-approximation]
relations:
  - {predicate: contrastsWith, object: kt:q-learning}
  - {predicate: dependsOn, object: kt:markov-decision-process}
  - {predicate: introducedIn, object: kt:on-line-q-learning-using-connectionist-systems}
  - {predicate: influencedBy, object: kt:q-learning}
  - {predicate: enables, object: kt:expected-sarsa}
sources:
  - id: s1
    title: "Reinforcement Learning: An Introduction (2nd ed.), sections 6.4-6.6 and bibliographical remarks"
    publisher: MIT Press, 2018 (Sutton and Barto), course copy hosted by Texas A&M CSCE 421
    url: https://people.engr.tamu.edu/guni/csce421/files/RLbook2018.pdf
    type: textbook
    accessed: 2026-11-15
  - id: s2
    title: "On-line Q-learning using connectionist systems (CUED/F-INFENG/TR166), abstract"
    publisher: Cambridge University Engineering Department, 1994 (Rummery and Niranjan)
    url: https://mi.eng.cam.ac.uk/reports/abstracts/rummery_tr166.html
    type: primary
    accessed: 2026-11-15
  - id: s3
    title: "Generalization in Reinforcement Learning: Successful Examples Using Sparse Coarse Coding"
    publisher: Advances in Neural Information Processing Systems 8 (NIPS 1995), Sutton
    url: https://papers.neurips.cc/paper_files/paper/1995/file/8f1d43620bc6bb580df6e80b0dc05c48-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "Convergence Results for Single-Step On-Policy Reinforcement-Learning Algorithms"
    publisher: Machine Learning 39:287-308, 2000 (Singh, Jaakkola, Littman and Szepesvari), author copy
    url: https://sites.ualberta.ca/~szepesva/papers/singh98convergence.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "A Theoretical and Empirical Analysis of Expected Sarsa"
    publisher: IEEE ADPRL 2009, pp. 177-184 (van Seijen, van Hasselt, Whiteson and Wiering), Utrecht University research portal
    url: https://research-portal.uu.nl/en/publications/a-theoretical-and-empirical-analysis-of-expected-sarsa/
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# SARSA

SARSA is a model-free reinforcement learning algorithm that learns an action-value function Q(s, a) by temporal-difference (TD) updates and uses it to choose actions. It is the standard example of **on-policy** TD control: the values it estimates are those of the very policy the agent is following, exploration included.[^s1] Its name lists the five quantities each update consumes: the current state S_t, action A_t, reward R_{t+1}, next state S_{t+1} and next action A_{t+1}.[^s1]

## Origin

Gavin Rummery and Mahesan Niranjan introduced the method in a 1994 Cambridge University Engineering Department technical report, calling it "Modified Connectionist Q-Learning" (MCQ-L).[^s1][^s2] Their goal was to make Q-learning-style methods work with neural-network function approximators on continuous, high-dimensional problems, and they argued for updating on-line during each trial rather than replaying a trial backwards once it ended; on a simulated mobile-robot navigation task they found on-line updating less sensitive to training parameters.[^s2] Richard Sutton gave the algorithm its now-standard name in a NIPS paper presented in 1995 and published in 1996, which used "variations of the sarsa algorithm" with sparse coarse-coded (CMAC) approximators to solve gridworld, puddle-world, mountain-car and acrobot control tasks, countering earlier negative reports about combining value learning with function approximation.[^s1][^s3]

## How it works

After every transition from a non-terminal state, SARSA applies[^s1]

Q(S_t, A_t) ← Q(S_t, A_t) + α [ R_{t+1} + γ Q(S_{t+1}, A_{t+1}) − Q(S_t, A_t) ]

where α is the step size and γ the discount factor; the value of a terminal state is taken as zero. In the control loop the agent picks A_{t+1} from its current policy (typically ε-greedy with respect to Q), uses that action in the update, and then actually executes it, so policy evaluation and policy improvement are interleaved step by step.[^s1]

The key contrast is with Q-learning, whose target uses the maximum next-state action value regardless of what the agent will do. Q-learning is therefore off-policy, learning about the greedy policy while behaving differently, whereas SARSA learns the value of its behaviour policy.[^s1][^s4]

## Convergence

In the tabular case SARSA converges with probability 1 to an optimal policy and action-value function, given standard step-size conditions, provided every state-action pair is visited infinitely often and the policy becomes greedy in the limit; ε-greedy with ε = 1/t is one way to meet the second condition.[^s1] Singh, Jaakkola, Littman and Szepesvári proved this in 2000 for one-step SARSA under policies that are "greedy in the limit with infinite exploration" (GLIE), giving decaying ε-greedy and suitably scheduled Boltzmann exploration as GLIE examples. They also showed that under persistent exploration SARSA converges to the best policy within a restricted class, and stressed that because on-policy methods cannot separate exploration from learning, their guarantees depend on the exploration schedule. The results cover lookup tables only, not function approximation.[^s4]

## Behaviour and trade-offs

Sutton and Barto's cliff-walking example shows the practical consequence. With rewards of −1 per step, −100 for stepping off a cliff, and ε-greedy exploration at ε = 0.1, Q-learning learns the shortest path along the cliff edge but occasionally falls off while exploring, while SARSA learns a longer, safer route and earns more reward online. Both would reach the optimal policy if ε were reduced gradually.[^s1] SARSA is thus a reasonable choice when the agent's mistakes during learning are costly, while off-policy methods suit learning a greedy target from exploratory or logged data.[^s1][^s4]

Because it learns during an episode, SARSA also copes with tasks where some policies never terminate: in the windy-gridworld example Monte Carlo methods are hard to apply, but SARSA quickly learns that looping policies are poor.[^s1] Its main weakness is the variance introduced by sampling A_{t+1}. **Expected SARSA** replaces Q(S_{t+1}, A_{t+1}) with the expected value of Q(S_{t+1}, ·) under the policy, removing that variance at extra computational cost.[^s1] Van Seijen and colleagues showed in 2009 that it converges under the same conditions as SARSA, permits larger learning rates (a rate of 1 in deterministic environments), and often outperformed both SARSA and Q-learning in their experiments.[^s5] Multi-step (n-step SARSA) and eligibility-trace (SARSA(λ)) versions bridge one-step TD and Monte Carlo targets.[^s1]

## Connections

SARSA is a control method built on temporal-difference learning and sits within reinforcement learning; it assumes the task is framed as a Markov decision process (`dependsOn kt:markov-decision-process`).[^s1] It is most often taught by contrast with Q-learning (`contrastsWith kt:q-learning`), from which its original name derives (`influencedBy kt:q-learning`), the difference being on-policy versus off-policy targets.[^s1][^s2] It was introduced in Rummery and Niranjan's 1994 report (`introducedIn kt:on-line-q-learning-using-connectionist-systems`).[^s2] Its on-policy character ties it directly to the exploration-exploitation dilemma, since the exploration schedule shapes both what it learns and whether it converges.[^s4] It `enables` Expected SARSA, its lower-variance successor, and Sutton's 1996 results made it an early showcase for value learning with function approximation.[^s3][^s5] Actor-critic methods are a related family that also learn on-policy from TD errors but keep a separate policy.[^s1]

## Sources
[^s1]: Sutton and Barto, *Reinforcement Learning: An Introduction*, 2nd ed., MIT Press, 2018, §6.4–6.6 and Chapter 6 bibliographical remarks. https://people.engr.tamu.edu/guni/csce421/files/RLbook2018.pdf (accessed 2026-11-15)
[^s2]: Rummery and Niranjan, "On-line Q-learning using connectionist systems", Cambridge University Engineering Department TR166, 1994 (abstract). https://mi.eng.cam.ac.uk/reports/abstracts/rummery_tr166.html (accessed 2026-11-15)
[^s3]: Sutton, "Generalization in Reinforcement Learning: Successful Examples Using Sparse Coarse Coding", NIPS 8, 1996. https://papers.neurips.cc/paper_files/paper/1995/file/8f1d43620bc6bb580df6e80b0dc05c48-Paper.pdf (accessed 2026-11-15)
[^s4]: Singh, Jaakkola, Littman and Szepesvári, "Convergence Results for Single-Step On-Policy Reinforcement-Learning Algorithms", Machine Learning 39, 2000. https://sites.ualberta.ca/~szepesva/papers/singh98convergence.pdf (accessed 2026-11-15)
[^s5]: van Seijen, van Hasselt, Whiteson and Wiering, "A Theoretical and Empirical Analysis of Expected Sarsa", IEEE ADPRL 2009. https://research-portal.uu.nl/en/publications/a-theoretical-and-empirical-analysis-of-expected-sarsa/ (accessed 2026-11-15)
