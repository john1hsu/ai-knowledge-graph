---
id: kt:ai-agent
type: Concept
title: AI agent
aliases: [intelligent agent, autonomous agent, LLM-based agent, LLM agent]
domain: agents-and-tool-use
summary: >-
  A system that perceives its environment and acts on it to achieve goals; in current usage, usually a
  large language model that decides its own sequence of steps and tool calls in a loop driven by
  feedback from the environment.
maturity: emerging
broader: [kt:artificial-intelligence]
related: [kt:agentic-workflow, kt:multi-agent-systems, kt:agent-memory, kt:planning-in-llms]
relations:
  - {predicate: basedOn, object: kt:large-language-model}
  - {predicate: dependsOn, object: kt:tool-use}
  - {predicate: implementedIn, object: kt:react-prompting}
  - {predicate: contrastsWith, object: kt:agentic-workflow}
sources:
  - id: s1
    title: "Chapter 2: Intelligent Agents (CMSC 421 lecture slides, after Russell & Norvig, AIMA)"
    publisher: University of Maryland, Department of Computer Science
    url: https://www.cs.umd.edu/~nau/cmsc421/chapter02.pdf
    type: academic
    accessed: 2026-10-30
  - id: s2
    title: "A Survey on Large Language Model based Autonomous Agents"
    publisher: Wang et al., arXiv 2308.11432 (authors' version)
    url: https://arxiv.org/html/2308.11432v7
    type: primary
    accessed: 2026-10-30
  - id: s3
    title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    publisher: ICLR 2023 (Yao et al.)
    url: https://iclr.cc/virtual/2023/poster/11003
    type: peer-reviewed
    accessed: 2026-10-30
  - id: s4
    title: "Building effective agents"
    publisher: Anthropic Engineering (Erik S. and Barry Zhang)
    url: https://www.anthropic.com/research/building-effective-agents
    type: lab-research
    accessed: 2026-10-30
created: 2026-10-30
---

# AI agent

An **AI agent** is anything that perceives its environment through sensors and acts upon that environment through actuators. This classical definition, from Russell and Norvig's textbook *Artificial Intelligence: A Modern Approach*, covers humans, robots, software "softbots" and even thermostats.[^s1] Since about 2023 the term has mostly meant something narrower: a system in which a large language model (LLM) chooses its own sequence of reasoning steps and tool calls to complete a task, observing the results of each action before deciding the next.[^s2][^s4]

## The classical view

In the textbook framing, an agent's behaviour is an *agent function* that maps the full history of percepts to an action. The *agent program* is the concrete implementation of that function running on some architecture.[^s1] A *rational* agent picks whichever action is expected to maximise its performance measure given what it has perceived so far. Rationality is not omniscience, and it implies exploration, learning and autonomy. Designers describe a task environment with PEAS (performance measure, environment, actuators, sensors). They classify environments along several axes: fully or partially observable, deterministic or stochastic, episodic or sequential, static or dynamic, discrete or continuous, and single- or multi-agent.[^s1] Agent designs range from simple reflex agents (condition–action rules) through reflex agents with internal state, goal-based agents and utility-based agents. Any of these can be extended into a learning agent that has a critic and a problem generator.[^s1]

## LLM-based agents

Earlier autonomous agents were usually trained with limited knowledge inside isolated environments. LLMs trained on web-scale data brought broad world knowledge to the problem, which set off a surge of research into LLM-based agents.[^s2] The survey by Wang et al. (first posted August 2023) proposes a unified architecture with four modules:[^s2]

- **Profile**: the agent's role, usually written into the prompt.
- **Memory**: a store of what the agent has perceived and experienced, used to guide later actions.
- **Planning**: breaking tasks into subtasks, with or without feedback from the environment, humans or the model itself.
- **Action**: turning decisions into concrete effects on the environment.

A key early technique was ReAct (Yao et al., ICLR 2023). ReAct prompts a model to interleave free-text reasoning with actions such as search-API calls or moves in a simulated environment. The reasoning steps help the model plan and recover from errors, and the observations ground it in external information.[^s3] With only one or two in-context examples, the authors report absolute success-rate gains of 34 and 10 points over imitation- and reinforcement-learning baselines on ALFWorld and WebShop. They also report less hallucination than chain-of-thought alone on HotpotQA and FEVER.[^s3]

## Agents versus workflows

Practitioners often separate *workflows*, which run LLM calls and tools along predefined code paths, from *agents*, which let the model control its own process and tool use. Anthropic's widely cited December 2024 guidance draws the line this way.[^s4] That guidance describes the building block as an "augmented LLM" with retrieval, tools and memory. It lists workflow patterns: prompt chaining, routing, parallelisation, orchestrator–workers and evaluator–optimiser. It reserves full agents for open-ended problems where the number of steps cannot be predicted in advance.[^s4]

## Limitations and open problems

Agents trade higher latency and cost for capability, and errors can compound over many turns. Anthropic therefore recommends trying the simplest solution first, testing extensively in sandboxes, and adding guardrails, human checkpoints and stopping conditions such as iteration caps.[^s4] It also argues that the agent–computer interface deserves as much engineering as the prompt. In its SWE-bench work, for example, requiring absolute file paths removed a class of errors that relative paths caused.[^s4] The Wang et al. survey lists open challenges: role-playing fidelity, generalised alignment with human values, prompt robustness, hallucination, knowledge-boundary effects, and efficiency.[^s2] How to evaluate agents also remains an active research question.[^s2]

## Connections

The concept sits under **artificial intelligence** broadly. It is **based on** **large language models** and **depends on** **tool use** to act beyond text.[^s2][^s4] **ReAct prompting** is one of the first and most influential ways to implement the reason–act loop.[^s3] Its modules correspond to neighbouring nodes: **agent memory** and **planning in LLMs** match the survey's memory and planning modules.[^s2] **Agentic workflows** are the predefined-path alternative it **contrasts with**.[^s4] **Multi-agent systems** compose several agents, a setting the classical environment taxonomy already anticipates as "multi-agent".[^s1]

## Sources
[^s1]: "Chapter 2: Intelligent Agents", CMSC 421 lecture slides (after Russell & Norvig, *AIMA*), University of Maryland. https://www.cs.umd.edu/~nau/cmsc421/chapter02.pdf (accessed 2026-10-30)
[^s2]: L. Wang et al., "A Survey on Large Language Model based Autonomous Agents", arXiv 2308.11432. https://arxiv.org/html/2308.11432v7 (accessed 2026-10-30)
[^s3]: S. Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", ICLR 2023. https://iclr.cc/virtual/2023/poster/11003 (accessed 2026-10-30)
[^s4]: Erik S. and Barry Zhang, "Building effective agents", Anthropic, 19 Dec 2024. https://www.anthropic.com/research/building-effective-agents (accessed 2026-10-30)
