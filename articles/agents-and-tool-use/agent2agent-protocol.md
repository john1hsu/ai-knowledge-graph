---
id: kt:agent2agent-protocol
type: Tool
title: Agent2Agent protocol
aliases: [A2A, A2A protocol, Agent-to-Agent protocol]
domain: agents-and-tool-use
summary: >-
  An open protocol, launched by Google in April 2025 and now governed under the Linux Foundation, that lets
  independent AI agents built on different frameworks discover one another through published Agent Cards and
  delegate, track and complete tasks as peers without sharing their internal memory, tools or prompts.
maturity: emerging
broader: [kt:multi-agent-systems]
related: [kt:ai-agent, kt:agentic-workflow, kt:tool-use, kt:prompt-injection]
relations:
  - {predicate: createdBy, object: kt:google}
  - {predicate: contrastsWith, object: kt:model-context-protocol}
  - {predicate: implementedIn, object: kt:langgraph}
sources:
  - id: s1
    title: "Announcing the Agent2Agent Protocol (A2A)"
    publisher: Google Developers Blog (Surapaneni, Jha, Vakoc, Segal), 9 April 2025
    url: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "Agent2Agent (A2A) Protocol Specification"
    publisher: A2A Protocol Working Group, The Linux Foundation (v1.0)
    url: https://a2a-protocol.org/latest/specification/
    type: official-docs
    accessed: 2026-11-09
  - id: s3
    title: "Linux Foundation Launches the Agent2Agent Protocol Project to Enable Secure, Intelligent Communication Between AI Agents"
    publisher: The Linux Foundation press release, 23 June 2025
    url: https://linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents
    type: news
    accessed: 2026-11-09
  - id: s4
    title: "A2A Protocol Surpasses 150 Organizations, Lands in Major Cloud Platforms, and Sees Enterprise Production Use in First Year"
    publisher: The Linux Foundation press release, 9 April 2026
    url: https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year
    type: news
    accessed: 2026-11-09
  - id: s5
    title: "A New Chapter for A2A: Joining the Agentic AI Foundation"
    publisher: A2A Protocol project blog, 27 August 2026
    url: https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/
    type: official-docs
    accessed: 2026-11-09
  - id: s6
    title: "Building A Secure Agentic AI Application Leveraging A2A Protocol"
    publisher: arXiv 2504.16902v1 (Habler, Huang, Narajala, Kulkarni), 2025
    url: https://arxiv.org/html/2504.16902v1
    type: preprint
    accessed: 2026-11-09
created: 2026-11-09
---

# Agent2Agent protocol

The **Agent2Agent protocol (A2A)** is an open standard for communication between AI agents. It lets an agent built by one vendor or framework find another agent, hand it a task, follow the task's progress and receive its results, even though neither side can see the other's memory, tools or reasoning.[^s1][^s2] Google announced A2A on 9 April 2025 with more than 50 technology partners and several consulting firms behind it.[^s1] On 23 June 2025 the Linux Foundation took the project over, saying it would keep the protocol vendor neutral; Google Cloud, SAP, ServiceNow and Cisco's Outshift were named as founding contributors.[^s3] The specification is now maintained by an A2A Protocol Working Group under the Linux Foundation and published under the Apache 2.0 licence.[^s2]

## How it works

A2A treats every agent as an opaque service. A **client agent** formulates a task and a **remote agent** carries it out.[^s1] The specification lists five design principles: reuse existing web standards, be ready for enterprise use, work asynchronously so tasks can run for hours or wait on humans, carry any content modality, and keep each agent's execution opaque.[^s2]

- **Discovery.** Each A2A server publishes an **Agent Card**, a JSON document giving the agent's identity, skills, service endpoint and required authentication. Clients can fetch it from a well-known path, `/.well-known/agent-card.json`, on the server's domain.[^s2]
- **Tasks.** Work is organised as a stateful **Task** with its own ID. A task moves through states such as working, input-required, auth-required, completed, failed, canceled or rejected, so a client can tell a finished job from one waiting for more input.[^s2]
- **Messages, parts and artifacts.** Agents exchange **Messages** (turns with the role "user" or "agent") made of **Parts**: text, file references or structured data. A task's outputs are returned as **Artifacts**, also built from parts.[^s2] Typed parts let agents agree on formats the user's interface can show, such as forms or video.[^s1]
- **Updates.** Besides simple request–response, clients can stream task events over Server-Sent Events or register a webhook for push notifications, which suits long-running work.[^s2]

Version 1.0 defines one data model, written in Protocol Buffers, and three interchangeable bindings: JSON-RPC 2.0, gRPC and HTTP+JSON/REST.[^s2] The Linux Foundation describes v1.0 as the first stable release. It added signed Agent Cards for cryptographic identity, multi-tenancy, updated security flows and a migration path from earlier drafts.[^s4]

## Relationship to MCP

A2A is usually presented alongside the **Model Context Protocol (MCP)**. The specification calls the two complementary. MCP covers how a model or agent connects to tools, APIs and data sources, while A2A covers how independent agents discover each other and share or delegate work.[^s2] A typical design uses both. A client asks a remote agent over A2A to handle a complex request, and that agent uses MCP to reach the tools it needs.[^s2] The project describes MCP as the "vertical" layer and A2A as the "horizontal" layer between peers.[^s5]

## Adoption

By April 2026 the Linux Foundation counted more than 150 supporting organisations, including AWS, Cisco, IBM, Microsoft, Salesforce, SAP and ServiceNow. It also reported production SDKs in Python, JavaScript, Java, Go and .NET.[^s4] Microsoft added A2A to Azure AI Foundry and Copilot Studio, and AWS supports it through Amazon Bedrock AgentCore Runtime.[^s4] On 27 August 2026, A2A was accepted as a Growth Stage project of the Agentic AI Foundation (AAIF), a Linux Foundation body that also hosts MCP.[^s5] The project lists agent frameworks that support it, including LangGraph, CrewAI, Pydantic AI, AG2 and IBM BeeAI.[^s5] These figures come from the project and its foundation and are not independent measurements.

## Limitations and security

Connecting agents from different owners creates new trust problems. An independent threat model by Habler et al. (2025, preprint) uses the MAESTRO framework to find risks for A2A deployments. They include spoofed or "poisoned" Agent Cards whose fields carry injected instructions, replayed task requests, impersonated servers, cross-agent privilege escalation and tampered artifacts.[^s6] The mitigations they propose are conceptual: sign and verify Agent Cards, use mutual TLS and short-lived tokens, protect against replay, enforce strict schema validation and least privilege, and keep audit logs that resist tampering.[^s6] The specification itself requires servers to reject missing or invalid credentials and to avoid revealing resources a client is not allowed to see. It also puts extended Agent Cards behind authentication.[^s2] Because the specification changed substantially between early drafts and v1.0, adopters have had to migrate between versions.[^s4]

## Connections

A2A is an infrastructure layer for **multi-agent systems**, its broader topic, and it was **created by** **Google** before moving to the Linux Foundation.[^s1][^s3] Each endpoint is an **AI agent**, and an orchestrator–worker **agentic workflow** can span agents run by different organisations once they speak A2A.[^s1][^s2] The protocol **contrasts with** the **Model Context Protocol**: MCP handles **tool use** within one agent, while A2A connects agents to each other.[^s2][^s5] Agent frameworks such as **LangGraph** **implement** it.[^s5] Poisoned Agent Cards are a form of **prompt injection**, which links A2A security to that risk.[^s6]

## Sources
[^s1]: R. Surapaneni, M. Jha, M. Vakoc and T. Segal, "Announcing the Agent2Agent Protocol (A2A)", Google Developers Blog, 9 April 2025. https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ (accessed 2026-11-09)
[^s2]: A2A Protocol Working Group, "Agent2Agent (A2A) Protocol Specification", v1.0, The Linux Foundation. https://a2a-protocol.org/latest/specification/ (accessed 2026-11-09)
[^s3]: The Linux Foundation, "Linux Foundation Launches the Agent2Agent Protocol Project to Enable Secure, Intelligent Communication Between AI Agents", 23 June 2025. https://linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents (accessed 2026-11-09)
[^s4]: The Linux Foundation, "A2A Protocol Surpasses 150 Organizations, Lands in Major Cloud Platforms, and Sees Enterprise Production Use in First Year", 9 April 2026. https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year (accessed 2026-11-09)
[^s5]: A2A Protocol project, "A New Chapter for A2A: Joining the Agentic AI Foundation", 27 August 2026. https://a2a-protocol.org/latest/blog/2026/08/27/a-new-chapter-for-a2a-joining-the-agentic-ai-foundation/ (accessed 2026-11-09)
[^s6]: I. Habler, K. Huang, V. S. Narajala and P. Kulkarni, "Building A Secure Agentic AI Application Leveraging A2A Protocol", arXiv 2504.16902v1, 2025. https://arxiv.org/html/2504.16902v1 (accessed 2026-11-09)
