---
id: kt:computer-use-agents
type: Technique
title: Computer-use agents
aliases: [computer use, computer-using agent, GUI agents, OS agents]
domain: agents-and-tool-use
summary: >-
  AI agents that operate a computer's graphical interface the way a person does: a multimodal model reads
  screenshots, decides on the next step, and issues mouse and keyboard actions in a loop until a task in
  ordinary desktop or web software is done.
maturity: emerging
broader: [kt:ai-agent, kt:tool-use]
related: [kt:vision-language-model, kt:prompt-injection, kt:react-prompting, kt:ai-evaluation]
relations:
  - {predicate: dependsOn, object: kt:vision-language-model}
  - {predicate: evaluatedOn, object: kt:osworld}
  - {predicate: evaluatedOn, object: kt:webarena}
  - {predicate: trainedWith, object: kt:reinforcement-learning}
sources:
  - id: s1
    title: "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments"
    publisher: NeurIPS 2024 Datasets and Benchmarks (Xie et al.)
    url: https://neurips.cc/virtual/2024/poster/97468
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "WebArena: A Realistic Web Environment for Building Autonomous Agents"
    publisher: ICLR 2024 (Zhou et al.)
    url: https://iclr.cc/virtual/2024/poster/17826
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "Developing a computer use model"
    publisher: Anthropic
    url: https://anthropic.com/news/developing-computer-use
    type: lab-research
    accessed: 2026-11-16
  - id: s4
    title: "Computer-Using Agent"
    publisher: OpenAI
    url: https://openai.com/index/computer-using-agent/
    type: lab-research
    accessed: 2026-11-16
  - id: s5
    title: "Computer use tool"
    publisher: Anthropic, Claude Platform documentation
    url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool
    type: official-docs
    accessed: 2026-11-16
created: 2026-11-16
---

# Computer-use agents

A computer-use agent is an AI agent whose actions are the same low-level inputs a human gives a computer: it looks at the screen, moves and clicks the pointer, scrolls and types. Rather than calling a purpose-built API for each application, the agent works through the existing graphical user interface (GUI), so in principle it can drive any desktop program or website a person could. The idea was framed in research benchmarks of 2023–2024 that placed multimodal models inside real web and operating-system environments,[^s1][^s2] and it became a product category when Anthropic released "computer use" for Claude 3.5 Sonnet as a public beta on 22 October 2024 and OpenAI described its Computer-Using Agent (CUA), the model behind Operator, on 23 January 2025.[^s3][^s4]

## How it works

The core is a perceive–reason–act loop. OpenAI describes CUA as receiving a screenshot, reasoning over current and earlier screenshots and actions with chain-of-thought, and then acting through a virtual mouse and keyboard, repeating until the task is finished or it needs the user's input; it attributes the capability to combining GPT-4o's vision with reasoning trained by reinforcement learning.[^s4] Anthropic says the hard skill was teaching the model to count pixels on a screenshot so it could work out how far to move the cursor, and that it trained on simple software such as a calculator and text editor without internet access, after which the skill generalised to other programs.[^s3]

In Anthropic's API the capability is exposed as a client-side toolset: the model emits tool calls such as `screenshot`, `left_click` at pixel coordinates, `type`, `key`, `scroll`, `zoom` and `wait`, and the developer's application executes each one in an environment it controls and returns the result, so the model never touches the machine directly.[^s5] As of November 2026 the documentation lists 17 such actions and notes that the model can batch several in one turn, with execution halted at the first failure.[^s5] Agents are usually paired with ordinary text tools (a shell or file editor) where those are faster than clicking.[^s5]

## Evaluation

Two benchmarks anchor the field. WebArena (ICLR 2024) builds self-hosted, functional websites for e-commerce, forums, collaborative software development and content management; its best GPT-4-based agent completed 14.41% of tasks end to end against 78.24% for humans.[^s2] OSWorld (NeurIPS 2024) runs 369 tasks on real Ubuntu, Windows and macOS machines, including file I/O and workflows that span several applications; at publication humans solved over 72% while the best model reached 12.24%, with failures traced mainly to GUI grounding and missing operational knowledge.[^s1] Reported progress since has been fast but comes from the labs themselves: Anthropic reported 14.9% on OSWorld in October 2024, and OpenAI reported 38.1% on OSWorld and 58.1% on WebArena for CUA in January 2025.[^s3][^s4]

## Limitations and risks

Developers' own documentation is candid about weak spots. Anthropic lists latency too slow for human-paced interaction, misplaced coordinates and hallucinated actions, lower reliability with niche or multiple applications, scrolling that sometimes fails, and difficulty with complex spreadsheet operations.[^s5] Its launch post likened the screenshot view to a flipbook that can miss short-lived notifications.[^s3]

Security is the larger concern. Because the agent reads whatever is on screen, text in a webpage or image can carry instructions that override the user's — a form of prompt injection.[^s3][^s5] Recommended mitigations include a dedicated virtual machine or container with minimal privileges, withholding credentials, allow-listing domains, requiring human confirmation for consequential steps such as payments, and classifiers that scan screenshots for injected instructions.[^s5] OpenAI describes similar layers: confirmations before actions with external effects, a supervised mode on sensitive sites such as email, refusals of some high-risk tasks like banking, and a monitor model that pauses execution on suspicious content.[^s4]

## Connections

Computer-use agents are a specialisation of the **AI agent** pattern and an extension of **tool use**, in which the "tool" is a whole computer driven through generic input actions.[^s5] They depend on a **vision-language model** to ground instructions in pixels, and OpenAI's account adds **reinforcement learning** to train the reasoning that selects actions.[^s4] Their loop of reasoning, acting and observing mirrors **ReAct prompting**, and their capabilities are measured on **OSWorld** and **WebArena** within the broader practice of **AI evaluation**.[^s1][^s2] Their chief security exposure is **prompt injection** delivered through on-screen content.[^s3][^s5]

## Sources
[^s1]: Xie et al., "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments", NeurIPS 2024. https://neurips.cc/virtual/2024/poster/97468 (accessed 2026-11-16)
[^s2]: Zhou et al., "WebArena: A Realistic Web Environment for Building Autonomous Agents", ICLR 2024. https://iclr.cc/virtual/2024/poster/17826 (accessed 2026-11-16)
[^s3]: Anthropic, "Developing a computer use model", 22 October 2024. https://anthropic.com/news/developing-computer-use (accessed 2026-11-16)
[^s4]: OpenAI, "Computer-Using Agent", 23 January 2025. https://openai.com/index/computer-using-agent/ (accessed 2026-11-16)
[^s5]: Anthropic, "Computer use tool", Claude Platform documentation. https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool (accessed 2026-11-16)
