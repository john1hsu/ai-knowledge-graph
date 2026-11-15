---
id: kt:model-context-protocol
type: Tool
title: Model Context Protocol
aliases: [MCP, MCP protocol]
domain: agents-and-tool-use
summary: >-
  An open protocol, introduced by Anthropic in November 2024 and donated to the Linux Foundation's Agentic AI
  Foundation in December 2025, that standardizes how LLM applications connect to external tools, data and prompt
  templates through JSON-RPC 2.0 messages exchanged between host-side clients and MCP servers.
maturity: emerging
broader: [kt:tool-use]
related: [kt:ai-agent, kt:retrieval-augmented-generation, kt:prompt-injection]
relations:
  - {predicate: createdBy, object: kt:anthropic}
  - {predicate: influencedBy, object: kt:language-server-protocol}
  - {predicate: contrastsWith, object: kt:agent2agent-protocol}
sources:
  - id: s1
    title: "Introducing the Model Context Protocol"
    publisher: Anthropic, 25 November 2024
    url: https://www.anthropic.com/news/model-context-protocol?so=1
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "Specification (Model Context Protocol), latest revision 2026-07-28"
    publisher: Model Context Protocol project
    url: https://modelcontextprotocol.io/specification/latest
    type: official-docs
    accessed: 2026-11-15
  - id: s3
    title: "Architecture overview"
    publisher: Model Context Protocol documentation (protocol version 2026-07-28)
    url: https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "MCP joins the Agentic AI Foundation"
    publisher: Model Context Protocol blog, 9 December 2025
    url: https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/
    type: official-docs
    accessed: 2026-11-15
  - id: s5
    title: "Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions"
    publisher: arXiv 2503.23278v3 (Hou, Zhao, Wang and Wang), 2025
    url: https://arxiv.org/html/2503.23278v3
    type: preprint
    accessed: 2026-11-15
created: 2026-11-15
---

# Model Context Protocol

The **Model Context Protocol (MCP)** is an open standard for connecting AI applications to the systems where data and capabilities live: file stores, business tools, databases and development environments. Anthropic released it on 25 November 2024. The stated problem was that every new data source needed its own custom connector, so integrations were fragmented and hard to scale; MCP replaces them with one protocol.[^s1] The launch included the specification and SDKs, local MCP server support in the Claude Desktop apps, and an open-source repository of reference servers for Google Drive, Slack, GitHub, Git, Postgres and Puppeteer. Block and Apollo were named as early adopters, with Zed, Replit, Codeium and Sourcegraph building support.[^s1]

## How it works

MCP uses a client–server design with three roles. A **host** is the AI application, such as an IDE or chat assistant. For every **server** it connects to, the host creates a dedicated **client** that holds that one connection. A server is any program that provides context, whether it runs locally or remotely.[^s3] The specification says it borrows the idea of the **Language Server Protocol**, which lets one language integration work across many editors; MCP aims to do the same for context and tools across AI applications.[^s2]

The protocol has two layers.[^s3]

- **Data layer.** Messages follow JSON-RPC 2.0. Servers expose three primitives: **tools** (functions the model can call), **resources** (data used as context) and **prompts** (reusable templates for users).[^s2][^s3]
- **Discovery and calls.** Clients find primitives with `*/list` methods and run a tool with `tools/call`, passing arguments that match the tool's JSON Schema `inputSchema`. Servers can push change notifications, such as an updated tool list.[^s3]
- **Transport layer.** Local servers usually run over **stdio** as a child process. Remote servers use **Streamable HTTP**, which takes HTTP POST plus optional Server-Sent Events, and the docs recommend OAuth for obtaining access tokens.[^s3]

A database server, for example, might offer a query tool, a resource holding the schema and a prompt with few-shot examples. The host merges tools from all its servers into one registry the model can choose from.[^s3] MCP only defines how context is exchanged; it does not dictate how the application prompts the model or manages that context.[^s3]

The protocol is versioned by date. In the 2026-07-28 revision, every request carries the protocol version and capabilities in a `_meta` field, so a server can handle each request on its own, and servers must answer a `server/discover` request.[^s3] The same revision deprecated **sampling** (servers asking the host's model for completions) and protocol-level logging. It kept **elicitation**, which lets a server ask the user for input or confirmation.[^s3] Optional extensions, such as Tasks for long-running work and MCP Apps for interactive UI, are negotiated separately.[^s2]

## Adoption and governance

On 9 December 2025 Anthropic donated MCP to the **Agentic AI Foundation (AAIF)**, a directed fund under the Linux Foundation co-founded by Anthropic, Block and OpenAI. Google, Microsoft, AWS, Cloudflare and Bloomberg joined as supporters.[^s4] The project reported more than 97 million monthly SDK downloads and about 10,000 active servers at that time, along with client support in ChatGPT, Claude, Cursor, Gemini, Microsoft Copilot and Visual Studio Code. These are the project's own figures, not independent measurements.[^s4] The existing maintainers kept technical control, and changes still go through Specification Enhancement Proposals (SEPs).[^s4]

## Security and limitations

MCP opens paths to arbitrary data access and code execution, and the specification says the protocol cannot enforce safety by itself. It asks implementers to get explicit user consent before exposing data or invoking any tool. It also says tool descriptions and annotations should be treated as untrusted unless they come from a trusted server.[^s2] A threat survey by Hou et al. (2025, preprint) splits a server's life into creation, deployment, operation and maintenance phases. It lists 16 threat scenarios across four attacker types, including typosquatted server names, tool-name collisions, **tool poisoning** through hidden instructions in metadata, "rug pulls" where a trusted server later changes behaviour, installer spoofing and indirect prompt injection.[^s5] Their suggested defences are conceptual. They include signed manifests and verified publishers, namespaced tool names, auditing tool metadata before it reaches the model, version pinning, least-privilege credentials and runtime anomaly monitoring.[^s5] The authors showed that each threat is feasible with proof-of-concept servers but did not measure attack success rates.[^s5]

## Connections

MCP is a standard way to do **tool use**, its broader topic: it gives an **AI agent** a uniform way to find and call external functions.[^s2][^s3] Resources let applications pull documents into context, the same need **retrieval-augmented generation** meets, although MCP specifies only the transport and not the retrieval method.[^s3] It was **created by** **Anthropic**[^s1] and **influenced by** the **Language Server Protocol**.[^s2] It **contrasts with** the **Agent2Agent protocol**, which also sits under the AAIF but connects agents to each other rather than to tools.[^s4] Tool poisoning and malicious servers make **prompt injection** the main security risk in MCP deployments.[^s2][^s5]

## Sources
[^s1]: Anthropic, "Introducing the Model Context Protocol", 25 November 2024. https://www.anthropic.com/news/model-context-protocol?so=1 (accessed 2026-11-15)
[^s2]: Model Context Protocol project, "Specification", latest revision 2026-07-28. https://modelcontextprotocol.io/specification/latest (accessed 2026-11-15)
[^s3]: Model Context Protocol project, "Architecture overview", documentation for protocol version 2026-07-28. https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture (accessed 2026-11-15)
[^s4]: Model Context Protocol blog, "MCP joins the Agentic AI Foundation", 9 December 2025. https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/ (accessed 2026-11-15)
[^s5]: X. Hou, Y. Zhao, S. Wang and H. Wang, "Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions", arXiv 2503.23278v3, 2025. https://arxiv.org/html/2503.23278v3 (accessed 2026-11-15)
