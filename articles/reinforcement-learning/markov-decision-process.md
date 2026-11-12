---
id: kt:markov-decision-process
type: Concept
title: Markov decision process
aliases: [MDP, Markovian decision process, finite MDP]
domain: reinforcement-learning
summary: >-
  The standard mathematical model of sequential decision-making under uncertainty: an agent in a state
  chooses an action, the environment returns a reward and a next state drawn from probabilities that depend
  only on the current state and action, and the goal is a policy that maximises expected (discounted) return.
maturity: foundational
broader: [kt:reinforcement-learning, kt:markov-chain]
related: [kt:q-learning, kt:policy-gradient, kt:exploration-exploitation, kt:hidden-markov-model, kt:deep-q-network]
relations:
  - {predicate: createdBy, object: kt:richard-bellman}
  - {predicate: extends, object: kt:markov-chain}
  - {predicate: enables, object: kt:value-iteration}
  - {predicate: enables, object: kt:policy-iteration}
  - {predicate: enables, object: kt:q-learning}
  - {predicate: contrastsWith, object: kt:partially-observable-markov-decision-process}
sources:
  - id: s1
    title: "A Markovian Decision Process"
    publisher: RAND Corporation paper P-1066 (Richard E. Bellman), 1957
    url: https://www.rand.org/pubs/papers/P1066.html
    type: primary
    accessed: 2026-11-12
  - id: s2
    title: "Chapter 3: The Reinforcement Learning Problem (lecture slides for Sutton and Barto)"
    publisher: University of Massachusetts Amherst, CS 687 course materials (Andrew G. Barto)
    url: https://people.cs.umass.edu/~barto/courses/cs687/Chapter%203.pdf
    type: academic
    accessed: 2026-11-12
  - id: s3
    title: "Lecture 10: Markov Decision Processes"
    publisher: MIT 6.390 Intro to Machine Learning (Shen Shen), April 2026
    url: https://introml.mit.edu/_static/spring26/lectures/lec10/lecture10.pdf
    type: academic
    accessed: 2026-11-12
  - id: s4
    title: "Lecture Note 3: Policy Iteration"
    publisher: MIT OpenCourseWare 2.997 Decision Making in Large Scale Systems (Daniela Pucci de Farias), Spring 2004
    url: https://ocw.mit.edu/courses/2-997-decision-making-in-large-scale-systems-spring-2004/fbd5a7941a8981776eb0f5bd81308790_lec_3_v3.pdf
    type: academic
    accessed: 2026-11-12
  - id: s5
    title: "Planning and acting in partially observable stochastic domains"
    publisher: Artificial Intelligence 101:99-134, 1998 (Kaelbling, Littman and Cassandra); course-hosted copy, University of Queensland
    url: https://people.smp.uq.edu.au/YoniNazarathy/Control4406_2014/resources/KaelblingLittmanCassandra1998.pdf
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Markov decision process

A **Markov decision process (MDP)** is the formal model underneath almost all of reinforcement learning. At each discrete time step an agent observes a state, picks an action, receives a numerical reward and finds itself in a new state; the agent's task is to choose actions so as to maximise the reward it accumulates over time.[^s2] What makes the process *Markov* is that the probability of the next state and reward depends only on the current state and action, not on the earlier history, so the state is assumed to summarise everything relevant about the past.[^s2] When the state and action sets are finite the model is called a finite MDP.[^s2]

## Definition

A common textbook formulation writes an MDP as a tuple (S, A, T, R, γ): a set of states S, a set of actions A, a transition model T(s, a, s′) giving the probability of landing in s′ after taking a in s, a reward function R(s, a), and a discount factor γ between 0 and 1 that shrinks the weight of later rewards.[^s3] Kaelbling, Littman and Cassandra use the same ingredients without γ in the tuple, treating discounting as part of the optimisation objective.[^s5] A **policy** π maps states to actions (or to probabilities over actions), and the object of study is the policy that maximises expected return.[^s2] MIT's 2026 lecture illustrates this with a 3×3 grid world in which a "move up" action succeeds with probability 0.8 and slips to a neighbouring cell with probability 0.2, showing how stochastic transitions enter the model.[^s3]

The return is either a plain sum of rewards up to a terminal step, for episodic tasks, or a discounted infinite sum Σ γ^k r_{t+k+1}, for continuing tasks; γ near 0 makes the agent short-sighted and γ near 1 far-sighted.[^s2] Choosing γ < 1 keeps infinite-horizon values finite.[^s3]

## Value functions and Bellman equations

Two functions organise the theory. The state-value V^π(s) is the expected return from s when following π, and the action-value Q^π(s, a) is the expected return from taking a in s and following π thereafter.[^s2] For a fixed policy, V^π satisfies a *Bellman expectation equation*, one linear equation per state, with V^π as the unique solution.[^s2] The optimal values satisfy the nonlinear *Bellman optimality equations*, for example

Q*(s, a) = Σ_{s′} P(s′ | s, a) [ R + γ · max_{a′} Q*(s′, a′) ].[^s2]

For finite MDPs at least one optimal policy exists, all optimal policies share the same V* and Q*, and acting greedily with respect to Q* (picking argmax_a Q*(s, a)) is optimal without any look-ahead search.[^s2] For discounted infinite-horizon problems a stationary optimal policy exists; Kaelbling and colleagues credit this result to Ronald Howard.[^s5]

## Solving an MDP

When the model is known, MDPs are solved by dynamic programming. **Value iteration** starts from zero values and repeatedly applies the Bellman optimality backup until successive estimates change by less than a small threshold, then reads off the greedy policy.[^s3][^s5] **Policy iteration** alternates exact policy evaluation (solving the linear system for the current policy) with greedy policy improvement; because each step is at least as good as the last and the set of stationary policies is finite, it terminates at an optimal policy after finitely many iterations.[^s4] Value iteration has cheap iterations but converges only in the limit, while policy iteration needs fewer but costlier iterations.[^s4]

## Origin

The name traces to operations research. Richard Bellman's 1957 RAND paper *A Markovian Decision Process* studied the long-run behaviour of a nonlinear recurrence that arose from an equipment-replacement problem treated by Stuart Dreyfus.[^s1] Howard's work on dynamic programming and Markov processes supplied the existence of stationary optimal policies cited above,[^s5] and AI researchers later adopted the framework as the foundation for planning and reinforcement learning.[^s5]

## Limitations

Exact solution assumes an accurate model of the dynamics, enough computation, and the Markov property. Dynamic programming is polynomial in the number of states, but real state spaces are vast (Barto's slides cite roughly 10^20 states for backgammon), so practical methods rely on approximation.[^s2] Many tasks also violate full observability. The **partially observable MDP (POMDP)** adds a set of observations and an observation function; the agent maintains a belief, a probability distribution over states, and planning becomes an MDP over continuous belief space. Exact POMDP algorithms have worst-case running time exponential in at least one problem parameter.[^s5] The framework is nonetheless abstract and flexible: time steps need not be fixed real-time intervals, and states and actions can be low-level sensor readings or high-level decisions.[^s2]

## Connections

An MDP `extends` a Markov chain by letting an agent's actions shape the transition probabilities and by attaching rewards to them,[^s2][^s5] which is why it is listed as related to the hidden Markov model, another Markov-chain-based model. It sits inside reinforcement learning as the problem definition that algorithms solve.[^s2] It `enables` value iteration and policy iteration when the model is known,[^s4] and model-free learners such as Q-learning, which estimate Q* directly from sampled transitions; deep Q-networks and policy-gradient methods scale those ideas with function approximation.[^s2] The term goes back to Bellman's 1957 paper of that title (`createdBy`),[^s1] and it `contrastsWith` the POMDP, its partially observable generalisation.[^s5] The tension between gathering information and exploiting current value estimates within an MDP is the exploration–exploitation trade-off.[^s2]

## Sources
[^s1]: Bellman, R. E., "A Markovian Decision Process", RAND Corporation P-1066, 1957. https://www.rand.org/pubs/papers/P1066.html (accessed 2026-11-12)
[^s2]: Barto, A. G., "Chapter 3: The Reinforcement Learning Problem", lecture slides for Sutton and Barto, *Reinforcement Learning: An Introduction*, UMass Amherst CS 687. https://people.cs.umass.edu/~barto/courses/cs687/Chapter%203.pdf (accessed 2026-11-12)
[^s3]: Shen, S., "Lecture 10: Markov Decision Processes", MIT 6.390 Intro to Machine Learning, April 2026. https://introml.mit.edu/_static/spring26/lectures/lec10/lecture10.pdf (accessed 2026-11-12)
[^s4]: Pucci de Farias, D., "Lecture Note 3: Policy Iteration", MIT 2.997 Decision Making in Large Scale Systems, Spring 2004, MIT OpenCourseWare. https://ocw.mit.edu/courses/2-997-decision-making-in-large-scale-systems-spring-2004/fbd5a7941a8981776eb0f5bd81308790_lec_3_v3.pdf (accessed 2026-11-12)
[^s5]: Kaelbling, L. P., Littman, M. L. and Cassandra, A. R., "Planning and acting in partially observable stochastic domains", *Artificial Intelligence* 101:99–134, 1998. https://people.smp.uq.edu.au/YoniNazarathy/Control4406_2014/resources/KaelblingLittmanCassandra1998.pdf (accessed 2026-11-12)
