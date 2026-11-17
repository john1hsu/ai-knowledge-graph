---
id: kt:swe-agent
type: Tool
title: SWE-agent
aliases: [SWE-agent (Princeton), "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering", agent-computer interface for software engineering]
domain: agents-and-tool-use
summary: >-
  An open-source language-model agent from Princeton and Stanford researchers (NeurIPS 2024) that resolves GitHub
  issues by working inside a repository through a purpose-built agent-computer interface (ACI) of search, file-viewing
  and linted editing commands, showing that interface design for LM agents strongly affects their performance.
maturity: established
broader: [kt:ai-agent, kt:tool-use]
related: [kt:computer-use-agents, kt:react-prompting, kt:context-window, kt:agentic-workflow, kt:mini-swe-agent]
relations:
  - {predicate: introducedIn, object: kt:swe-agent-agent-computer-interfaces-enable-automated-software-engineering}
  - {predicate: createdBy, object: kt:princeton-university}
  - {predicate: basedOn, object: kt:large-language-model}
  - {predicate: evaluatedOn, object: kt:swe-bench}
  - {predicate: evaluatedOn, object: kt:humanevalfix}
  - {predicate: supersededBy, object: kt:mini-swe-agent}
sources:
  - id: s1
    title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    publisher: Advances in Neural Information Processing Systems 37 (NeurIPS 2024), Yang et al.
    url: https://papers.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering (full paper)"
    publisher: arXiv 2405.15793 (Yang, Jimenez, Wettig, Lieret, Yao, Narasimhan, Press; authors' version)
    url: https://arxiv.org/pdf/2405.15793.pdf
    type: primary
    accessed: 2026-11-17
  - id: s3
    title: "SWE-agent repository and README"
    publisher: SWE-agent project (Princeton University and Stanford University), GitHub
    url: https://github.com/SWE-agent/SWE-agent
    type: official-docs
    accessed: 2026-11-17
  - id: s4
    title: "mini-swe-agent repository and README"
    publisher: SWE-agent project (Princeton University and Stanford University), GitHub
    url: https://github.com/SWE-agent/mini-swe-agent
    type: official-docs
    accessed: 2026-11-17
  - id: s5
    title: "EnIGMA: Interactive Tools Substantially Assist LM Agents in Finding Security Vulnerabilities"
    publisher: arXiv 2409.16165 (Abramovich et al.; v3, June 2025)
    url: https://arxiv.org/abs/2409.16165
    type: preprint
    accessed: 2026-11-17
  - id: s6
    title: "Building effective agents"
    publisher: Anthropic (Erik S. and Barry Zhang), 19 December 2024
    url: https://www.anthropic.com/research/building-effective-agents
    type: lab-research
    accessed: 2026-11-17
created: 2026-11-17
---

# SWE-agent

**SWE-agent** is an open-source system that lets a language model act as an autonomous software engineer: given a GitHub issue and a repository, the model navigates the code, edits files, runs tests and submits a patch. It was introduced by John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan and Ofir Press, and published at NeurIPS 2024.[^s1] The paper's central claim is that LM agents are a new kind of end user, and that they work better with interfaces built for them, which the authors call **agent-computer interfaces (ACIs)**, by analogy with human-computer interfaces.[^s1][^s2]

## How it works

SWE-agent runs a ReAct-style loop. At each step the model writes a thought and one command, and the environment returns an observation. The LM's weights are not changed; all gains come from the interface around it.[^s2] The paper derives four ACI design principles: keep actions simple, with few options and short documentation; make actions compact, so common operations such as navigating or editing take one step; give feedback that is informative but concise; and add guardrails that catch mistakes early.[^s2]

The concrete interface follows those principles:[^s2]

- Search commands (`find_file`, `search_file`, `search_dir`) return summaries capped at 50 hits, asking for a narrower query when exceeded.[^s2]
- A file viewer (`open`, `goto`, `scroll_up`, `scroll_down`) shows a 100-line window with line numbers and omitted-line counts.[^s2]
- An `edit n:m` command replaces a line range and immediately shows the updated region of the file.[^s2]
- A flake8 linter rejects edits that introduce syntax or indentation errors and shows the agent what went wrong.[^s2]
- Context management keeps only the last five observations in full and collapses older ones to a single line each.[^s2]

Commands that print nothing return an explicit success message, so the model never mistakes silence for failure.[^s2]

## Results and evidence

On the full SWE-bench test set, SWE-agent with GPT-4 Turbo resolved 12.47% of issues, versus 1.31% for a non-interactive retrieval-augmented baseline with the same model; with Claude 3 Opus it reached 10.46%. On HumanEvalFix it scored 87.7% pass@1. Both were reported as state of the art at publication (2024).[^s1][^s2] Runs were capped at a $4 budget per task.[^s2]

The ablations are the paper's main evidence that interface design matters. On SWE-bench Lite with GPT-4 Turbo, the full ACI resolved 18.0%, against 11.0% for an agent with only a plain Linux shell, a 64% relative gain. Removing the edit command dropped the score to 10.3%, and removing the linter dropped it to 15.0%. Showing whole files instead of a 100-line window lowered it to 12.7%, and a 30-line window gave 14.3%.[^s2] More information was not always better: iterative, one-result-at-a-time search underperformed both summarized search and no search tool at all.[^s2]

## Limitations

Failure analysis of unresolved Lite tasks found that about 52% stemmed from incorrect or overly specific fixes and about 23% from cascading failed edits. Recovery was hard: the chance an editing sequence eventually succeeded fell from 90.5% to 57.2% after a single failed edit.[^s2] The interface is hand-designed for Python repositories; its linter and commands do not transfer automatically to other languages or tasks.[^s2]

## In practice

The project is maintained under MIT licence by the Princeton and Stanford team, and is configured through a single YAML file. Its README news feed lists the SWE-agent 1.0 release and later state-of-the-art claims with newer models such as Claude 3.7, all self-reported. As of November 2026, the maintainers say most development has moved to **mini-swe-agent**, which they describe as superseding SWE-agent.[^s3] mini-swe-agent drops custom tools: it gives the model only bash, keeps a linear message history and runs each action as an independent subprocess. Its README claims above 74% on SWE-bench Verified, a figure from the project rather than an independent audit.[^s4] The ACI idea was also extended to security: EnIGMA adds interactive tools such as a debugger and a server-connection utility, and reports state-of-the-art results on capture-the-flag benchmarks.[^s5] Industry guidance adopted the term: Anthropic's December 2024 agent-building guide urges as much effort on ACIs as on human interfaces. It describes error-proofing tools, such as requiring absolute file paths, for its own SWE-bench agent.[^s6]

## Connections

SWE-agent is a specialised **AI agent** whose capability comes from **tool use** through a custom command set, and it follows the thought-action-observation loop of **ReAct prompting**.[^s2] It was introduced in the NeurIPS 2024 paper *SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering* by researchers at Princeton, and it wraps an unmodified **large language model**.[^s1] It was evaluated on **SWE-bench**, built by the same group, and on **HumanEvalFix**.[^s1][^s2] Its observation-collapsing scheme is a response to **context-window** limits, and it relates to **computer-use agents**, which control general GUIs rather than a code-specific interface.[^s2] It has been superseded in its maintainers' own recommendation by **mini-swe-agent**.[^s3][^s4] Its scaffold is an example of an **agentic workflow** for code repair.[^s6]

## Sources
[^s1]: Yang et al., "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering", NeurIPS 2024. https://papers.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html (accessed 2026-11-17)
[^s2]: Yang et al., "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering", arXiv 2405.15793. https://arxiv.org/pdf/2405.15793.pdf (accessed 2026-11-17)
[^s3]: SWE-agent project, SWE-agent repository README, GitHub. https://github.com/SWE-agent/SWE-agent (accessed 2026-11-17)
[^s4]: SWE-agent project, mini-swe-agent repository README, GitHub. https://github.com/SWE-agent/mini-swe-agent (accessed 2026-11-17)
[^s5]: Abramovich et al., "EnIGMA: Interactive Tools Substantially Assist LM Agents in Finding Security Vulnerabilities", arXiv 2409.16165. https://arxiv.org/abs/2409.16165 (accessed 2026-11-17)
[^s6]: Anthropic, "Building effective agents", 19 December 2024. https://www.anthropic.com/research/building-effective-agents (accessed 2026-11-17)
