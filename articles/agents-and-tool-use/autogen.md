---
id: kt:autogen
type: Tool
title: "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
aliases: [AutoGen, Microsoft AutoGen, pyautogen]
domain: agents-and-tool-use
summary: >-
  An open-source Python framework and 2023 paper from Microsoft Research and academic collaborators in which
  LLM applications are built as conversations among customisable "conversable agents" (backed by LLMs, humans,
  tools or code execution) that reply to each other automatically; redesigned as an event-driven v0.4 in 2025 and
  later archived in favour of Microsoft Agent Framework.
maturity: established
broader: [kt:multi-agent-systems, kt:agentic-systems]
related: [kt:ai-agent, kt:tool-use, kt:react-prompting, kt:retrieval-augmented-generation, kt:agentic-workflow]
relations:
  - {predicate: createdBy, object: kt:microsoft-research}
  - {predicate: alternativeTo, object: kt:langgraph}
  - {predicate: dependsOn, object: kt:large-language-model}
  - {predicate: evaluatedOn, object: kt:alfworld}
  - {predicate: supersededBy, object: kt:microsoft-agent-framework}
sources:
  - id: s1
    title: "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
    publisher: arXiv 2308.08155v2 (Wu et al., Microsoft Research, Penn State, University of Washington, Xidian University; authors' version)
    url: https://arxiv.org/pdf/2308.08155.pdf
    type: primary
    accessed: 2026-11-11
  - id: s2
    title: "AutoGen: Enabling next-generation large language model applications"
    publisher: Microsoft Research Blog
    url: https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-generation-large-language-model-applications
    type: lab-research
    accessed: 2026-11-11
  - id: s3
    title: "AutoGen v0.4: Reimagining the foundation of agentic AI for scale, extensibility, and robustness"
    publisher: Microsoft Research
    url: https://www.microsoft.com/en-us/research/?p=1116288
    type: lab-research
    accessed: 2026-11-11
  - id: s4
    title: "AutoGen Reimagined: Launching AutoGen 0.4"
    publisher: Microsoft AutoGen developer blog
    url: https://devblogs.microsoft.com/autogen/autogen-reimagined-launching-autogen-0-4/
    type: official-docs
    accessed: 2026-11-11
  - id: s5
    title: "microsoft/autogen (README)"
    publisher: Microsoft, GitHub repository
    url: https://github.com/microsoft/autogen
    type: official-docs
    accessed: 2026-11-11
  - id: s6
    title: "Microsoft Agent Framework overview"
    publisher: Microsoft Learn
    url: https://learn.microsoft.com/en-us/agent-framework/overview/
    type: official-docs
    accessed: 2026-11-11
created: 2026-11-11
---

# AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

AutoGen is an open-source framework, and the paper that introduced it, for building large-language-model applications as conversations among several agents. Its central claim is that many complex tasks are easier to build, debug and extend when they are decomposed into agents with specialised roles that message one another, rather than written as a single long prompt or a hard-coded pipeline.[^s1] The paper was written by Qingyun Wu, Gagan Bansal, Chi Wang and colleagues at Microsoft Research, Pennsylvania State University, the University of Washington and Xidian University; the arXiv version 2 is dated October 2023.[^s1] Microsoft Research announced the framework in September 2023, describing it as a spinoff of FLAML, its automated machine-learning library, released as a free, community-driven Python package.[^s2]

## How it works

The basic abstraction is the **conversable agent**: anything that can send, receive and generate replies to messages through a common interface, whether it is backed by an LLM, a human, a tool, or a mix.[^s1] The base class can be configured into ready-made roles. An *AssistantAgent* is an LLM-backed assistant that writes plans and code; a *UserProxyAgent* stands in for the human, either asking a person for input or automatically executing the code and function calls the assistant proposes, with the level of human involvement adjustable.[^s1] This pairing turned an LLM into a loop that writes code, runs it, sees the errors and tries again, much like a code-interpreter chat but with each step exposed as messages.[^s2]

The authors call the resulting style **conversation programming**. A workflow is defined by what each agent computes when it receives a message and by control flow that emerges from the conversation itself: every agent auto-replies unless a termination condition is met, so a single opening message can drive a long multi-agent exchange.[^s1] Control can be expressed in natural language (system messages), in Python code (custom reply functions), or both, and a *GroupChatManager* agent supports dynamic group chats by choosing the next speaker and broadcasting messages to the group.[^s1][^s2]

## Results and limitations

The 2023 paper demonstrates six applications. On level-5 problems from the MATH dataset (120 problems), a GPT-4-based AutoGen setup solved 52.5%, against 30.0% for plain GPT-4 and 48.33% for ChatGPT with Code Interpreter; on ALFWorld household tasks, adding a third "grounding" agent that supplies commonsense hints raised average success to 69% from 54% for a ReAct baseline.[^s1] In a supply-chain coding application (OptiGuide), the core workflow shrank from over 430 lines of code to about 100, and a separate safeguard agent improved F1 for flagging unsafe code.[^s1] Microsoft's announcement summarised such case studies as cutting coding effort by more than 4x; these are the developers' own reported measurements.[^s2]

The authors frame the work as early-stage. They note that results depend heavily on the underlying model (GPT-4 followed instructions better than GPT-3.5-turbo), that choosing the number of agents, their roles and the conversation topology is an open design problem, that larger workflows become hard to log and debug, and that autonomous code execution can change the environment (for example by installing packages), which calls for human oversight and fail-safes.[^s1]

## Evolution and status

Feedback on the original release pointed to architectural constraints, an API that grew inefficient, and limited debugging and intervention.[^s3] In January 2025 Microsoft released **AutoGen v0.4**, a complete redesign in which agents exchange asynchronous messages, supporting both event-driven and request/response patterns.[^s4] It is layered into a Core API for message passing and local or distributed runtimes, a higher-level AgentChat API that replaced the v0.2 interface, and an Extensions API; it added OpenTelemetry tracing, Python and .NET interoperability, a rebuilt low-code AutoGen Studio, and the Magentic-One generalist multi-agent application.[^s3][^s4][^s5]

As of November 2026 the GitHub repository is archived: its README says Microsoft no longer provides bug fixes, security fixes or new features, and directs new users to Microsoft Agent Framework.[^s5] Microsoft Learn describes Agent Framework as the direct successor to both AutoGen and Semantic Kernel, built by the same teams, combining AutoGen's single- and multi-agent abstractions with Semantic Kernel's enterprise features and adding explicit workflows for controlling multi-agent execution paths.[^s6]

## Connections

AutoGen is an instance of **multi-agent systems** applied to LLMs and part of the broader family of **agentic systems**; it was **created by Microsoft Research** and **depends on large language models** for its assistant agents.[^s1][^s2] Its agents call functions and execute code, linking it to **tool use**, and its retrieval-augmented chat application ties it to **retrieval-augmented generation**.[^s1] It was **evaluated on ALFWorld**, where it was compared directly with **ReAct**, and it is an **alternative to LangGraph**, which models agent workflows as explicit state graphs rather than emergent conversations.[^s1] Within this graph it is the conversational counterpart to **agentic workflows** built from predefined steps, and it is **superseded by Microsoft Agent Framework**, which reintroduces explicit workflows alongside AutoGen-style agents.[^s6]

## Sources
[^s1]: Wu et al., "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation", arXiv 2308.08155v2. https://arxiv.org/pdf/2308.08155.pdf (accessed 2026-11-11)
[^s2]: Microsoft Research Blog, "AutoGen: Enabling next-generation large language model applications" (September 2023). https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-generation-large-language-model-applications (accessed 2026-11-11)
[^s3]: Microsoft Research, "AutoGen v0.4: Reimagining the foundation of agentic AI for scale, extensibility, and robustness". https://www.microsoft.com/en-us/research/?p=1116288 (accessed 2026-11-11)
[^s4]: Microsoft AutoGen blog, "AutoGen Reimagined: Launching AutoGen 0.4" (January 17, 2025). https://devblogs.microsoft.com/autogen/autogen-reimagined-launching-autogen-0-4/ (accessed 2026-11-11)
[^s5]: Microsoft, microsoft/autogen GitHub repository README. https://github.com/microsoft/autogen (accessed 2026-11-11)
[^s6]: Microsoft Learn, "Microsoft Agent Framework overview" (updated 2026-10-28). https://learn.microsoft.com/en-us/agent-framework/overview/ (accessed 2026-11-11)
