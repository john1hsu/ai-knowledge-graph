---
id: kt:agentic-workflow
type: Technique
title: Agentic workflow
aliases: [LLM workflow, agentic design patterns, compound LLM workflow]
domain: agents-and-tool-use
summary: >-
  A way of building LLM applications in which several model calls and tool calls are orchestrated along
  code paths the developer defines in advance, such as chains, routers, parallel branches, orchestrator–worker
  splits and generate–critique loops, rather than leaving the overall control flow to the model.
maturity: emerging
broader: [kt:agentic-systems]
related: [kt:self-refine, kt:multi-agent-systems, kt:planning-in-llms, kt:ai-evaluation]
relations:
  - {predicate: contrastsWith, object: kt:ai-agent}
  - {predicate: basedOn, object: kt:large-language-model}
  - {predicate: dependsOn, object: kt:tool-use}
  - {predicate: implementedIn, object: kt:langgraph}
sources:
  - id: s1
    title: "Building effective agents"
    publisher: Anthropic Engineering (Erik S. and Barry Zhang)
    url: https://www.anthropic.com/research/building-effective-agents
    type: lab-research
    accessed: 2026-10-30
  - id: s2
    title: "Workflows and agents"
    publisher: LangChain, LangGraph documentation
    url: https://docs.langchain.com/oss/langgraph/workflows-agents
    type: official-docs
    accessed: 2026-10-30
  - id: s3
    title: "Self-Refine: Iterative Refinement with Self-Feedback"
    publisher: NeurIPS 2023 (Madaan et al.)
    url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract.html
    type: peer-reviewed
    accessed: 2026-10-30
  - id: s4
    title: "AFlow: Automating Agentic Workflow Generation"
    publisher: ICLR 2025 (Zhang et al.)
    url: https://proceedings.iclr.cc/paper_files/paper/2025/hash/5492ecbce4439401798dcd2c90be94cd-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-10-30
  - id: s5
    title: "Check Out Our Course on How to Build AI Agents"
    publisher: DeepLearning.AI, The Batch (Andrew Ng letter, 8 Oct 2025)
    url: https://www.deeplearning.ai/the-batch/check-out-our-course-on-how-to-build-ai-agents
    type: news
    accessed: 2026-10-30
created: 2026-10-30
---

# Agentic workflow

An **agentic workflow** is an LLM application whose steps are wired together by the developer: model calls, tool calls and checks run along predetermined code paths, and the model fills in each step rather than deciding the overall process.[^s1][^s2] The term is used most precisely in Anthropic's December 2024 engineering guidance. That guidance groups workflows and agents together as "agentic systems" and separates them by who controls the flow: in a workflow the code does, in an agent the model does.[^s1] LangGraph's documentation adopts the same split, describing workflows as predetermined paths and agents as systems that choose their own processes in feedback loops.[^s2] In looser usage, popularised by Andrew Ng's courses and newsletter, "agentic workflow" covers any multi-step LLM process built from patterns such as reflection, tool use, planning and multi-agent collaboration.[^s5]

## Core patterns

Anthropic's guidance names five recurring workflow patterns, and LangGraph documents the same set with runnable examples:[^s1][^s2]

- **Prompt chaining.** A task is split into fixed sequential steps, each consuming the previous output. Programmatic "gates" can check intermediate results and stop a bad chain early. Example: draft an outline, check it against criteria, then write the document.[^s1]
- **Routing.** An input is classified first and then sent to a specialised prompt or process. Example: sending easy questions to a smaller, cheaper model and hard ones to a more capable model.[^s1]
- **Parallelisation.** Several calls run at once and their outputs are aggregated in code. In *sectioning* the calls handle independent subtasks; in *voting* the same task is run several times to gain confidence, for instance several reviewers screening code for vulnerabilities.[^s1][^s2]
- **Orchestrator–workers.** A central model breaks a task down on the fly, hands subtasks to worker calls and merges their results. Unlike plain parallelisation, the subtasks are not known in advance; multi-file code edits are a typical case.[^s1] LangGraph supports this with a `Send` API that creates worker nodes dynamically.[^s2]
- **Evaluator–optimizer.** One call generates a response and another critiques it, looping until the output meets the criteria. It suits tasks with clear evaluation criteria, such as literary translation.[^s1]

## Evidence for the approach

The evaluator–optimizer loop has peer-reviewed support. Self-Refine (Madaan et al., NeurIPS 2023) has a single LLM produce an output, give feedback on it and revise it, with no extra training data, fine-tuning or reinforcement learning.[^s3] Across seven tasks, from dialogue responses to mathematical reasoning, and with GPT-3.5, ChatGPT and GPT-4, the authors report outputs preferred by humans and automatic metrics and an average gain of about 20 points absolute over one-shot generation (as reported in 2023).[^s3]

Designing workflows by hand is laborious, which has prompted work on generating them automatically. AFlow (Zhang et al., ICLR 2025) represents a workflow as code made of LLM-invoking nodes and searches over variants with Monte Carlo Tree Search, using execution feedback to keep improving.[^s4] On six benchmarks the authors report an average 5.7% improvement over prior state-of-the-art baselines, and say that workflows built around smaller models beat GPT-4o on some tasks at about 4.55% of its dollar inference cost.[^s4] These figures are the authors' own results on their chosen benchmarks.

## Trade-offs and practice

Workflows give predictability and consistency for well-defined tasks. Agents are better when flexibility and model-driven decisions are needed at scale.[^s1] Each extra step adds latency and cost, so Anthropic advises adding complexity only when it measurably improves results, and notes that chaining deliberately trades latency for accuracy.[^s1] Ng stresses a disciplined evaluation process: trace each step to find where a workflow breaks, then let error analysis decide what to fix rather than guessing at prompt changes.[^s5] Frameworks such as LangGraph add persistence, streaming, debugging and deployment support around these patterns.[^s2]

## Connections

Agentic workflows and **AI agents** sit together under the umbrella of **agentic systems** and are usually defined against each other, so the two nodes **contrast with** one another.[^s1][^s2] Both are **based on** **large language models** and **depend on** **tool use** to reach beyond text.[^s1][^s5] **LangGraph** is one framework that **implements** the patterns.[^s2] The evaluator–optimizer pattern is closely related to **Self-Refine**.[^s3] The orchestrator–workers pattern and Ng's multi-agent collaboration link to **multi-agent systems**, and his planning pattern to **planning in LLMs**.[^s1][^s5] Both AFlow's search and Ng's error-analysis advice depend on measurement, which connects workflows to **AI evaluation**.[^s4][^s5]

## Sources
[^s1]: Erik S. and Barry Zhang, "Building effective agents", Anthropic, 19 Dec 2024. https://www.anthropic.com/research/building-effective-agents (accessed 2026-10-30)
[^s2]: LangChain, "Workflows and agents", LangGraph documentation. https://docs.langchain.com/oss/langgraph/workflows-agents (accessed 2026-10-30)
[^s3]: A. Madaan et al., "Self-Refine: Iterative Refinement with Self-Feedback", NeurIPS 2023. https://proceedings.neurips.cc/paper_files/paper/2023/hash/91edff07232fb1b55a505a9e9f6c0ff3-Abstract.html (accessed 2026-10-30)
[^s4]: J. Zhang et al., "AFlow: Automating Agentic Workflow Generation", ICLR 2025. https://proceedings.iclr.cc/paper_files/paper/2025/hash/5492ecbce4439401798dcd2c90be94cd-Abstract-Conference.html (accessed 2026-10-30)
[^s5]: A. Ng, "Check Out Our Course on How to Build AI Agents", The Batch, DeepLearning.AI, 8 Oct 2025. https://www.deeplearning.ai/the-batch/check-out-our-course-on-how-to-build-ai-agents (accessed 2026-10-30)
