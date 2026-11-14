---
id: kt:agent-memory
type: Concept
title: Agent memory
aliases: [LLM agent memory, memory for language agents, agentic memory, long-term agent memory]
domain: agents-and-tool-use
summary: >-
  The mechanisms that let an LLM-based agent keep, organize and recall information beyond a single model call,
  spanning short-term working context and long-term episodic, semantic and procedural stores that the agent
  writes to, manages and retrieves from as it acts.
maturity: emerging
broader: [kt:ai-agent]
related: [kt:retrieval-augmented-generation, kt:context-window, kt:memgpt, kt:generative-agents-interactive-simulacra-of-human-behavior]
relations:
  - {predicate: dependsOn, object: kt:vector-database}
  - {predicate: implementedIn, object: kt:langgraph}
sources:
  - id: s1
    title: "Cognitive Architectures for Language Agents"
    publisher: Transactions on Machine Learning Research, 2024 (Sumers, Yao, Narasimhan, Griffiths; authors' arXiv version 2309.02427)
    url: https://arxiv.org/pdf/2309.02427
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s2
    title: "MemGPT: Towards LLMs as Operating Systems"
    publisher: arXiv 2310.08560 (Packer et al., authors' version)
    url: https://arxiv.org/pdf/2310.08560
    type: primary
    accessed: 2026-11-14
  - id: s3
    title: "A Survey on the Memory Mechanism of Large Language Model based Agents"
    publisher: arXiv 2404.13501 (Zhang et al., authors' version)
    url: https://arxiv.org/pdf/2404.13501
    type: primary
    accessed: 2026-11-14
  - id: s4
    title: "Generative Agents: Interactive Simulacra of Human Behavior"
    publisher: UIST 2023 (Park et al.; authors' arXiv version 2304.03442v2)
    url: https://arxiv.org/pdf/2304.03442v2
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "Memory overview (LangGraph / LangChain docs)"
    publisher: LangChain
    url: https://docs.langchain.com/oss/python/concepts/memory
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# Agent memory

**Agent memory** is the set of mechanisms by which an LLM-based agent retains information across the steps of a task and across separate tasks or sessions, then brings the relevant parts back into the model's prompt when it decides what to do next. A model call is stateless and bounded by its context window, so anything an agent "remembers" must either be re-inserted as text, kept in an external store, or encoded in weights.[^s1][^s3] Zhang et al.'s 2024 survey distinguishes a narrow view, where memory is only the history of earlier steps in the current trial, from a broad view that also includes experience from earlier trials and external knowledge.[^s3]

## Taxonomy

The most widely cited framework is CoALA (Cognitive Architectures for Language Agents) by Sumers, Yao, Narasimhan and Griffiths, published in TMLR in 2024, which borrows categories from cognitive science.[^s1]

- **Working memory** holds the information active in the current decision cycle (observations, goals, intermediate reasoning) and persists across LLM calls.[^s1]
- **Episodic memory** stores past experience such as event histories or trajectories; **semantic memory** stores knowledge about the world and the agent itself.[^s1]
- **Procedural memory** is split between implicit knowledge in the LLM's weights and explicit knowledge in the agent's code and prompts.[^s1]

In CoALA, *retrieval* actions read from long-term memory into working memory, *reasoning* reads and writes working memory, and *learning* writes from working memory into a long-term store.[^s1] The survey by Zhang et al. adds an orthogonal axis: memory can be **textual** (natural language or structured records in the prompt or a database) or **parametric** (written into weights by fine-tuning or knowledge editing). Textual memory is interpretable and cheap to write but limited by prompt length; parametric memory escapes that limit at the cost of expensive writes and possible information loss.[^s3]

## How it works

Implementations usually decompose memory into three operations: *writing* raw observations into a stored form, *managing* the store by merging duplicates, reflecting into higher-level summaries and forgetting irrelevant entries, and *reading* the items relevant to the next action, often by embedding similarity.[^s3]

The Generative Agents system (Park et al., UIST 2023) is an early, influential design. Each agent keeps a "memory stream" of natural-language records and ranks them for retrieval by the sum of three normalized scores: recency (exponential decay with factor 0.995 per game hour), importance (an LLM rating from 1 to 10 assigned at creation), and relevance (cosine similarity between embeddings of the record and the current query).[^s4] When accumulated importance passes a threshold, the agent writes *reflections*, higher-level inferences that cite their supporting memories. In the paper's ablation, removing memory, reflection and planning lowered human-judged believability from a TrueSkill score of 29.89 to 21.21.[^s4]

MemGPT (Packer et al., 2023) instead treats the context window like an operating system's main memory. The prompt holds read-only system instructions, a small editable working context, and a FIFO message queue headed by a recursive summary of evicted messages; older content lives in searchable *recall* and *archival* storage outside the window.[^s2] The model itself moves data between tiers through function calls, and a queue manager warns it of "memory pressure" near a token threshold before evicting messages. On the authors' deep-memory-retrieval task over prior chat sessions, GPT-4 accuracy rose from 32.1% with a fixed summary-based context to 92.5% with MemGPT, as reported in the paper.[^s2]

## In practice

Agent frameworks now expose memory as a first-class component. LangGraph, for example, separates thread-scoped short-term memory, persisted via checkpoints, from long-term memory kept as JSON documents in a store organized by namespaces, and it maps semantic, episodic and procedural memory onto user profiles, few-shot examples and self-revised instructions respectively.[^s5] Its documentation contrasts writing memories "in the hot path", which makes them available immediately but adds latency, with writing them in a background task, which avoids latency but can leave other threads briefly without fresh context.[^s5]

## Limitations and open questions

Long prompts are costly and suffer position bias, recency-based truncation can drop distant but critical facts, and retrieval quality caps what the agent can recall.[^s3] Parametric memory risks overfitting and catastrophic forgetting, and the survey noted that, as of 2024, there were no open benchmarks dedicated to memory modules.[^s3] CoALA flags memory modification and deletion ("unlearning") and adaptive retrieval as understudied, and warns that letting agents rewrite their own procedural memory can introduce bugs or subvert designer intent.[^s1]

## Connections

Agent memory is a core component of an **AI agent**, its broader concept, and is the main way agents work around the fixed **context window**.[^s1][^s2] Reading from a long-term textual store is essentially **retrieval-augmented generation** applied to the agent's own history, and such stores commonly **depend on** a **vector database** for similarity search.[^s3] **MemGPT** and **Generative Agents** are the two canonical reference designs described above.[^s2][^s4] Long-term stores and checkpointed short-term state are **implemented in** **LangGraph**.[^s5]

## Sources
[^s1]: T. R. Sumers, S. Yao, K. Narasimhan, T. L. Griffiths, "Cognitive Architectures for Language Agents", Transactions on Machine Learning Research, 2024 (arXiv 2309.02427). https://arxiv.org/pdf/2309.02427 (accessed 2026-11-14)
[^s2]: C. Packer et al., "MemGPT: Towards LLMs as Operating Systems", arXiv 2310.08560, 2023. https://arxiv.org/pdf/2310.08560 (accessed 2026-11-14)
[^s3]: Zhang et al., "A Survey on the Memory Mechanism of Large Language Model based Agents", arXiv 2404.13501, 2024. https://arxiv.org/pdf/2404.13501 (accessed 2026-11-14)
[^s4]: J. S. Park et al., "Generative Agents: Interactive Simulacra of Human Behavior", UIST 2023 (arXiv 2304.03442v2). https://arxiv.org/pdf/2304.03442v2 (accessed 2026-11-14)
[^s5]: LangChain, "Memory overview", LangGraph documentation. https://docs.langchain.com/oss/python/concepts/memory (accessed 2026-11-14)
