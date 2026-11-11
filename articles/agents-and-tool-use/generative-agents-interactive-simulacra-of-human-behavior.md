---
id: kt:generative-agents-interactive-simulacra-of-human-behavior
type: Work
title: "Generative Agents: Interactive Simulacra of Human Behavior"
aliases: [Generative Agents paper, Park et al. 2023, Smallville simulation]
domain: agents-and-tool-use
summary: >-
  A UIST 2023 paper by Park et al. (Stanford and Google) that wraps a large language model in a memory stream,
  reflection and recursive planning so that 25 simulated characters in a Sims-like town called Smallville
  behave believably, remember, form relationships and coordinate without scripting.
maturity: established
broader: [kt:ai-agent]
related: [kt:agent-memory, kt:planning-in-llms, kt:multi-agent-systems, kt:voyager]
relations:
  - {predicate: basedOn, object: kt:large-language-model}
  - {predicate: dependsOn, object: kt:embeddings}
sources:
  - id: s1
    title: "Generative Agents: Interactive Simulacra of Human Behavior (v2)"
    publisher: arXiv 2304.03442 (Park et al., authors' version of the UIST 2023 paper)
    url: https://arxiv.org/pdf/2304.03442v2
    type: primary
    accessed: 2026-11-11
  - id: s2
    title: "Generative Agents: Interactive Simulacra of Human Behavior"
    publisher: Google Research publication page (Proceedings of UIST 2023, ACM)
    url: https://research.google/pubs/generative-agents-interactive-simulacra-of-human-behavior/
    type: lab-research
    accessed: 2026-11-11
  - id: s3
    title: "Computational Agents Exhibit Believable Humanlike Behavior"
    publisher: Stanford HAI (news, September 2023)
    url: https://hai.stanford.edu/news/computational-agents-exhibit-believable-humanlike-behavior
    type: academic
    accessed: 2026-11-11
  - id: s4
    title: "Simulating Human Behavior with AI Agents (policy brief)"
    publisher: Stanford HAI (May 2025)
    url: https://hai.stanford.edu/policy/simulating-human-behavior-with-ai-agents
    type: academic
    accessed: 2026-11-11
created: 2026-11-11
---

# Generative Agents: Interactive Simulacra of Human Behavior

**"Generative Agents: Interactive Simulacra of Human Behavior"** is a 2023 paper by Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang and Michael S. Bernstein, from Stanford University and Google. It was first posted to arXiv in April 2023 and published at the ACM Symposium on User Interface Software and Technology (UIST '23), held from October 29 to November 1, 2023, in San Francisco.[^s1][^s2] The paper defines *generative agents* as software characters that simulate believable human behaviour. Each agent is a large language model wrapped in an architecture that stores the agent's experiences as natural-language memories, condenses them into higher-level reflections, and retrieves them to plan.[^s2] The paper became a common reference design for memory and reflection in LLM agents.

## How it works

The architecture has three parts around a frozen model. The paper used gpt-3.5-turbo, and no model weights are trained.[^s1]

- **Memory stream.** Every observation, plan and reflection is appended to a list of records. Each record holds a text description, a creation time and a last-access time.[^s1]
- **Retrieval.** When an agent must act, candidate memories are ranked by the sum of three normalized scores. *Recency* decays exponentially by a factor of 0.995 per game hour since last access. *Importance* is a 1–10 rating the model assigns when the memory is created, from mundane to poignant. *Relevance* is the cosine similarity between the embeddings of the memory and the current query. In the paper's implementation all three are weighted equally.[^s1]
- **Reflection.** When the summed importance of recent events passes a threshold of 150, which happened about two or three times per simulated day, the agent asks itself salient questions about its 100 most recent records. It then writes insights that cite the memories supporting them. Reflections are stored back in the stream and can build on earlier reflections, forming trees of increasingly abstract beliefs.[^s1]
- **Planning.** Each agent drafts a coarse plan for the day in five to eight chunks. It recursively breaks each chunk into hour-long blocks and then into actions of 5–15 minutes. New observations can trigger a decision to react and re-plan.[^s1]

## The Smallville experiment

The authors placed 25 agents, each seeded with a one-paragraph biography, in Smallville. Smallville is a sandbox town inspired by *The Sims* and built with the Phaser game framework. Users could watch the agents, talk to them in natural language, or change the world.[^s1][^s2] Over two simulated days with no user intervention, social behaviour emerged that nobody had scripted.[^s1][^s3]

- The only setup was telling one agent, Isabella, that she wanted to host a Valentine's Day party. Knowledge of the party grew from 1 agent (4%) to 13 (52%) by the paper's text (a figure caption gives 12), and 5 of the 12 invited agents turned up at the right time and place.[^s1]
- News of another agent's mayoral candidacy spread from 1 agent to 8 (32%), and the town's relationship-network density rose from 0.167 to 0.74.[^s1]

Believability was measured with "interviews" in five areas: self-knowledge, memory, plans, reactions and reflections. One hundred human evaluators ranked the answers produced by the full architecture, by three ablated versions, and by human crowdworkers role-playing each agent. The full architecture ranked highest, with a TrueSkill μ of 29.89. Removing reflection lowered it to 26.88, and removing reflection and planning lowered it to 25.64. The crowdworkers scored 22.95, and the fully ablated version, with no memory, reflection or planning, scored lowest at 21.21.[^s1] Stanford HAI reported that removing observation, planning or reflection each made the agents less believable.[^s3]

## Limitations and critiques

The authors list several failure modes. Agents sometimes failed to retrieve relevant memories, recalled them incompletely, or embellished them with invented details. Their speech was overly formal and cooperative, which the authors attribute to instruction tuning. As memory grew, they chose odd locations and misread social norms, for example several agents using a one-person bathroom at once or going into shops after closing.[^s1][^s3] The simulation ran over only two game days. The crowdworker baseline was not meant to represent expert human performance. Running it cost thousands of dollars in API credits and took several days.[^s1] The paper also discusses ethical risks: parasocial attachment, persuasive misinformation, and over-reliance that replaces real human input in design. The mitigations it proposes include disclosing that agents are computational and keeping audit logs of their outputs.[^s1][^s3]

## Influence

The same group later grounded generative agents in two-hour interviews with 1,052 people. In that follow-up, which a Stanford HAI policy brief summarized in May 2025, the agents reproduced participants' General Social Survey answers 85% as accurately as the participants reproduced their own answers two weeks later. These are the authors' own results; the brief also flags privacy, consent and over-reliance risks and says the architectures need further development before reliable use.[^s4] In Stanford HAI's 2023 coverage, Park pointed to prototyping social systems and building game characters that remember players as practical uses.[^s3]

## Connections

Generative agents are a specific design for an **AI agent** and are **based on** a **large language model** used without fine-tuning.[^s1][^s2] Its memory stream with a scored retriever is a widely cited template for **agent memory**, and its relevance score **depends on** **embeddings**.[^s1] Recursive daily planning with reactive re-planning is an example of **planning in LLMs**, and Smallville's 25 interacting characters make it an early large-scale **multi-agent system** of LLM agents.[^s1][^s2] **Voyager**, also from 2023, offers a contrasting design: instead of reflecting on episodic memories to stay socially consistent, it stores verified code skills to master a game.

## Sources
[^s1]: J. S. Park, J. C. O'Brien, C. J. Cai, M. R. Morris, P. Liang, M. S. Bernstein, "Generative Agents: Interactive Simulacra of Human Behavior", UIST '23 (DOI 10.1145/3586183.3606763), arXiv 2304.03442v2. https://arxiv.org/pdf/2304.03442v2 (accessed 2026-11-11)
[^s2]: Google Research, "Generative Agents: Interactive Simulacra of Human Behavior", publication page, Proceedings of UIST 2023. https://research.google/pubs/generative-agents-interactive-simulacra-of-human-behavior/ (accessed 2026-11-11)
[^s3]: Stanford HAI, "Computational Agents Exhibit Believable Humanlike Behavior", September 21, 2023. https://hai.stanford.edu/news/computational-agents-exhibit-believable-humanlike-behavior (accessed 2026-11-11)
[^s4]: J. S. Park et al., "Simulating Human Behavior with AI Agents", Stanford HAI policy brief, May 2025. https://hai.stanford.edu/policy/simulating-human-behavior-with-ai-agents (accessed 2026-11-11)
