---
id: kt:langgraph
type: Tool
title: LangGraph
aliases: [LangGraph framework, langgraph library]
domain: agents-and-tool-use
summary: >-
  An open-source, low-level orchestration framework and runtime from LangChain for building long-running,
  stateful LLM agents and workflows as graphs of shared state, nodes and edges, with built-in checkpointing,
  human-in-the-loop interrupts and streaming; its execution model is adapted from Google's Pregel.
maturity: emerging
broader: [kt:agentic-systems]
related: [kt:agentic-workflow, kt:ai-agent, kt:multi-agent-systems, kt:agent-memory, kt:agent2agent-protocol]
relations:
  - {predicate: createdBy, object: kt:langchain}
  - {predicate: influencedBy, object: kt:pregel}
  - {predicate: alternativeTo, object: kt:autogen}
  - {predicate: dependsOn, object: kt:large-language-model}
sources:
  - id: s1
    title: "LangGraph overview"
    publisher: LangChain, LangGraph documentation (Python)
    url: https://docs.langchain.com/oss/python/langgraph/overview
    type: official-docs
    accessed: 2026-11-09
  - id: s2
    title: "Graph API overview"
    publisher: LangChain, LangGraph documentation (Python)
    url: https://docs.langchain.com/oss/python/langgraph/graph-api
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "Interrupts (human-in-the-loop)"
    publisher: LangChain, LangGraph documentation (Python)
    url: https://docs.langchain.com/oss/python/langgraph/human-in-the-loop
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "Persistence"
    publisher: LangChain, LangGraph documentation (Python)
    url: https://docs.langchain.com/oss/python/langgraph/persistence.md
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "LangChain and LangGraph Agent Frameworks Reach v1.0 Milestones"
    publisher: LangChain blog (Sydney Runkle and the LangChain OSS team), 22 October 2025
    url: https://www.langchain.com/blog/langchain-langgraph-1dot0
    type: primary
    accessed: 2026-11-09
  - id: s6
    title: "Pregel: A System for Large-Scale Graph Processing"
    publisher: SIGMOD 2010 (Malewicz et al., Google), author PDF hosted by Princeton COS 598F
    url: https://www.cs.princeton.edu/courses/archive/spring16/cos598F/pregel_paper.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s7
    title: "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
    publisher: COLM 2024 (Wu et al.), Microsoft Research publication page
    url: https://www.microsoft.com/en-us/research/publication/autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation-framework
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# LangGraph

**LangGraph** is an open-source orchestration framework and runtime, built by LangChain, for long-running, stateful agents. A developer describes an application as a graph: a shared **state**, **nodes** that do work and **edges** that decide what runs next. Deterministic code steps and LLM-driven steps can be mixed freely, and the framework does not prescribe prompts or an agent architecture.[^s1][^s2] It ships for Python and JavaScript/TypeScript.[^s5] LangChain positions it as the lowest layer of its stack: the LangChain library supplies model and tool integrations and ready-made agent loops on top of it, and LangSmith adds tracing, evaluation and hosted deployment.[^s1]

## How it works

A program is built with a `StateGraph`. Each state key has a **reducer** that merges node updates; without one, a new value overwrites the old, while a reducer such as list append lets parallel nodes add messages without clobbering each other.[^s2] Nodes are functions that read the state and return updates. Edges are either fixed or **conditional**, where a routing function picks the next node, ends the run, or fans out.[^s2] A `Send` object runs the same node once per item, which supports map-reduce and orchestrator–worker patterns where the number of subtasks is only known at runtime. A `Command` return value lets a node update state and choose the next node in one step.[^s2] The graph must be compiled before it runs; compilation checks the structure and attaches options such as a checkpointer.[^s2]

The runtime borrows its execution model from **Pregel**, Google's system for large-scale graph processing presented at SIGMOD 2010.[^s2][^s6] In Pregel, computation proceeds in synchronised **supersteps**, vertices communicate only by messages, and a vertex that votes to halt stays idle until a message wakes it; the job ends when every vertex is inactive and no messages are in flight.[^s6] LangGraph applies the same rules to LLM workflows: nodes running in parallel share a super-step, a node becomes active when input arrives on an incoming edge, and the run terminates when all nodes are inactive with no messages in transit.[^s2] A recursion limit caps the number of super-steps per run; the documentation gives a default of 10,007 from version 1.1.4 (as of November 2026).[^s2]

## Persistence and human-in-the-loop

The features LangChain stresses most are about surviving real-world runs.[^s5] A **checkpointer** saves graph state as checkpoints within a **thread**, identified by a `thread_id`; this gives conversation continuity, fault tolerance and the ability to revisit earlier states. Implementations range from an in-memory saver for experiments to SQLite for local development and PostgreSQL for production. A separate **store** holds long-term memory that is shared across threads, such as user preferences.[^s4]

Checkpointing makes **interrupts** possible. Calling `interrupt()` inside a node pauses the graph and surfaces a value to the caller; the run waits until it is resumed with `Command(resume=...)` on the same thread.[^s3] Typical uses are approving or rejecting a sensitive action, editing an LLM draft before it continues, and reviewing a tool call's arguments before it executes. One gotcha: on resume the node restarts from its beginning, so code before the interrupt must be idempotent.[^s3]

## Adoption and limitations

LangGraph 1.0 was released on 22 October 2025 alongside LangChain 1.0, with a commitment to no breaking changes until 2.0. The main deprecation was the `langgraph.prebuilt` module, whose agent helper moved to LangChain's `create_agent`, which itself runs on LangGraph.[^s5] LangChain names Uber, LinkedIn and Klarna among production users; these are the vendor's own claims.[^s5] The trade-off is abstraction level: because LangGraph is deliberately low-level, simple agents need more code than in higher-level libraries, and LangChain itself recommends starting from its agent API and dropping to LangGraph when more control is needed.[^s1][^s5]

## Connections

LangGraph is a framework for building **agentic systems**, so that is its broader node.[^s1] It is used both for predefined **agentic workflows** and for model-directed **AI agents**, and its `Send` fan-out supports **multi-agent systems**.[^s2] Its checkpointer and store implement short- and long-term **agent memory**.[^s4] It was **created by** **LangChain** and **influenced by** **Pregel**, whose superstep model it adapts.[^s2][^s6] It **depends on** **large language models** for its model-driven steps.[^s1] **AutoGen** (Wu et al., COLM 2024) is an **alternative** that structures applications as conversations between customisable agents rather than as an explicit state graph.[^s7] Finally, the **Agent2Agent protocol** node links here as one of the frameworks that implement that agent-to-agent standard.

## Sources
[^s1]: LangChain, "LangGraph overview", LangGraph documentation. https://docs.langchain.com/oss/python/langgraph/overview (accessed 2026-11-09)
[^s2]: LangChain, "Graph API overview", LangGraph documentation. https://docs.langchain.com/oss/python/langgraph/graph-api (accessed 2026-11-09)
[^s3]: LangChain, "Interrupts", LangGraph documentation. https://docs.langchain.com/oss/python/langgraph/human-in-the-loop (accessed 2026-11-09)
[^s4]: LangChain, "Persistence", LangGraph documentation. https://docs.langchain.com/oss/python/langgraph/persistence.md (accessed 2026-11-09)
[^s5]: S. Runkle and the LangChain OSS team, "LangChain and LangGraph Agent Frameworks Reach v1.0 Milestones", LangChain blog, 22 Oct 2025. https://www.langchain.com/blog/langchain-langgraph-1dot0 (accessed 2026-11-09)
[^s6]: G. Malewicz et al., "Pregel: A System for Large-Scale Graph Processing", SIGMOD 2010. https://www.cs.princeton.edu/courses/archive/spring16/cos598F/pregel_paper.pdf (accessed 2026-11-09)
[^s7]: Q. Wu et al., "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation", COLM 2024. https://www.microsoft.com/en-us/research/publication/autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation-framework (accessed 2026-11-09)
