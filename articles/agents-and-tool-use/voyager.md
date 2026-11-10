---
id: kt:voyager
type: Model
title: Voyager (embodied LLM agent)
aliases: [VOYAGER, Voyager agent, MineDojo Voyager]
domain: agents-and-tool-use
summary: >-
  An LLM-powered lifelong-learning agent for Minecraft, introduced in 2023 by researchers at NVIDIA and partner
  universities, that proposes its own tasks, writes executable code to accomplish them, and stores verified
  programs in a growing skill library it can retrieve and reuse, all through black-box GPT-4 calls with no fine-tuning.
maturity: emerging
broader: [kt:ai-agent]
related: [kt:agent-memory, kt:planning-in-llms, kt:self-refine, kt:agentic-workflow]
relations:
  - {predicate: basedOn, object: kt:large-language-model}
  - {predicate: dependsOn, object: kt:tool-use}
  - {predicate: createdBy, object: kt:nvidia}
  - {predicate: introducedIn, object: kt:voyager-an-open-ended-embodied-agent-with-large-language-models}
sources:
  - id: s1
    title: "Voyager: An Open-Ended Embodied Agent with Large Language Models (v2)"
    publisher: arXiv 2305.16291 (Wang et al., authors' version)
    url: https://arxiv.org/html/2305.16291v2
    type: primary
    accessed: 2026-11-10
  - id: s2
    title: "Voyager: An Open-Ended Embodied Agent with Large Language Models (spotlight)"
    publisher: NeurIPS 2023 Agent Learning in Open-Endedness Workshop
    url: https://neurips.cc/virtual/2023/79179
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s3
    title: "A Survey on Large Language Model based Autonomous Agents"
    publisher: Wang et al., arXiv 2308.11432 (authors' version)
    url: https://arxiv.org/html/2308.11432v7
    type: primary
    accessed: 2026-11-10
  - id: s4
    title: "MineDojo/Voyager: An Open-Ended Embodied Agent with Large Language Models"
    publisher: GitHub (official code release)
    url: https://github.com/minedojo/voyager
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# Voyager (embodied LLM agent)

**Voyager** is a large language model (LLM) agent that plays Minecraft open-endedly: it keeps exploring, picks up new skills and makes discoveries with no human in the loop.[^s1] It was introduced in May 2023 by Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan and Anima Anandkumar, with affiliations at NVIDIA, Caltech, UT Austin, Stanford and UW–Madison.[^s1] The paper was presented as a spotlight at the NeurIPS 2023 Agent Learning in Open-Endedness workshop, where the authors billed it as the first LLM-powered embodied lifelong-learning agent.[^s2] Voyager calls GPT-4 as a black box and never updates model weights. Everything it learns lives outside the model, in prompts and a library of code.[^s1]

## How it works

Voyager has three components that run in a loop.[^s1][^s2]

- **Automatic curriculum.** GPT-4 proposes the next task, aiming at "discovering as many diverse things as possible." It sees the agent's state (inventory, nearby blocks and entities, biome, health, position) and lists of completed and failed tasks.[^s1]
- **Skill library.** Actions are written as executable JavaScript against the Mineflayer bot API rather than as low-level motor commands. Once a program is verified, GPT-3.5 writes a description of it, and the description's embedding becomes the program's index. For a new task, the agent retrieves the top five matching skills and can compose them into more complex behaviour.[^s1]
- **Iterative prompting.** Each generated program is refined using three kinds of feedback: progress messages from the game, execution errors from the interpreter, and a self-verification step. In that step a separate GPT-4 "critic" judges whether the task succeeded and suggests fixes if it did not. The agent gets up to four rounds per task. Successful programs are added to the library; a task that still fails is set aside for later.[^s1]

The released implementation uses the MineDojo environment and Minecraft 1.19 with Fabric mods. It runs on Python and Node.js, needs an OpenAI API key, and is MIT-licensed.[^s1][^s4] Saved skill libraries can be loaded into a fresh agent, which can then break a new task into sub-goals and solve them with the stored skills.[^s4]

## Results

The authors compared Voyager with LLM-agent baselines (ReAct, Reflexion and AutoGPT) and reported, in the October 2023 revision, about 3.3 times as many unique items, 2.3 times the distance travelled, and tech-tree milestones reached up to 15.3 times faster than prior methods.[^s1] The workshop abstract gives the item gain as 3.1 times, so the headline figure differs between versions.[^s2] Voyager was the only method to reach diamond tools, and it did so in one of three trials. ReAct and Reflexion made little progress, and AutoGPT got through the early tech tree but stalled before diamond.[^s1] In a new world with an empty inventory, Voyager solved four unseen tasks within 50 iterations by drawing on its library. AutoGPT solved some of them only when it was given Voyager's skill library.[^s1]

The ablations show how much each part matters. A random curriculum cut discovered items by 93%, and removing self-verification cut them by 73%. Without the skill library, progress plateaued late in a run. Swapping GPT-4 for GPT-3.5 as the code writer reduced unique items by a factor of 5.7.[^s1] All of these are the authors' own results in a single game environment, and they have not been independently replicated at scale.

## Limitations

The authors list three main weaknesses.[^s1] GPT-4 cost about 15 times as much as GPT-3.5 at the time. The agent sometimes gets stuck, and the critic can miss successes. The curriculum also hallucinates, for example proposing items that do not exist in the game, and generated code can call functions that do not exist. More broadly, Voyager depends on a rich, scriptable API. Its "actions" are high-level bot calls, so its results say little about low-level sensorimotor control.[^s1]

## Connections

Voyager is a specific instance of an **AI agent** and is **based on** a **large language model** used without fine-tuning.[^s1] Writing code against a game API is a form of **tool use**, which the design **depends on**.[^s1][^s4] It was **created by** a team centred at **NVIDIA** and **introduced in** the 2023 Voyager paper.[^s1] Wang et al.'s survey of LLM-based agents uses Voyager as a reference example for several design dimensions. It cites the skill library as **agent memory** stored as natural-language descriptions and code, and as experience accumulation in capability acquisition. It also cites Voyager's feedback-driven loop as an example of **planning in LLMs** with environment feedback.[^s3] The iterative critique-and-revise loop resembles **Self-Refine** and the evaluator–optimizer pattern of **agentic workflows**, though Voyager adds external execution signals to the model's self-assessment.[^s1][^s3]

## Sources
[^s1]: G. Wang et al., "Voyager: An Open-Ended Embodied Agent with Large Language Models", arXiv 2305.16291v2, Oct 2023. https://arxiv.org/html/2305.16291v2 (accessed 2026-11-10)
[^s2]: G. Wang et al., "Voyager: An Open-Ended Embodied Agent with Large Language Models", spotlight, NeurIPS 2023 Agent Learning in Open-Endedness Workshop. https://neurips.cc/virtual/2023/79179 (accessed 2026-11-10)
[^s3]: L. Wang et al., "A Survey on Large Language Model based Autonomous Agents", arXiv 2308.11432v7. https://arxiv.org/html/2308.11432v7 (accessed 2026-11-10)
[^s4]: MineDojo, "Voyager" code repository, GitHub. https://github.com/minedojo/voyager (accessed 2026-11-10)
