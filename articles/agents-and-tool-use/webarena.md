---
id: kt:webarena
type: Benchmark
title: WebArena
aliases: [WebArena benchmark]
domain: agents-and-tool-use
summary: >-
  A self-hostable environment of fully functional websites and an accompanying set of 812 long-horizon
  tasks, introduced by Carnegie Mellon University researchers in 2023 and published at ICLR 2024, that
  evaluates autonomous web agents by checking whether each task was actually accomplished.
maturity: established
broader: [kt:ai-evaluation, kt:ai-agent]
related: [kt:osworld, kt:computer-use-agents, kt:visualwebarena, kt:llm-as-a-judge, kt:large-language-model]
relations:
  - {predicate: introducedIn, object: kt:webarena-a-realistic-web-environment-for-building-autonomous-agents}
  - {predicate: createdBy, object: kt:carnegie-mellon-university}
  - {predicate: alternativeTo, object: kt:osworld}
  - {predicate: followedBy, object: kt:webarena-verified}
sources:
  - id: s1
    title: "WebArena: A Realistic Web Environment for Building Autonomous Agents"
    publisher: arXiv 2307.13854 (Zhou, Xu et al.; authors' version)
    url: https://arxiv.org/pdf/2307.13854
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "WebArena: A Realistic Web Environment for Building Autonomous Agents (poster page)"
    publisher: ICLR 2024
    url: https://iclr.cc/virtual/2024/poster/17826
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks"
    publisher: Proceedings of ACL 2024 (Long Papers), pp. 881–905
    url: https://aclanthology.org/2024.acl-long.50
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "WebArena Verified: Reliable Evaluation for Web Agents"
    publisher: NeurIPS 2025 Workshop on Scaling Environments for Agents (El hattami, Thakkar, Chapados, Pal)
    url: https://neurips.cc/virtual/2025/124576
    type: primary
    accessed: 2026-11-18
created: 2026-11-18
---

# WebArena

WebArena is a benchmark and execution environment for agents that carry out tasks on the web. Rather than replaying cached pages or relying on live sites that change over time, it ships working copies of real web applications that anyone can host, reset and inspect, together with natural-language tasks whose success is judged by checking what the agent actually achieved. It was released in July 2023 by Shuyan Zhou, Frank F. Xu, Graham Neubig and colleagues at Carnegie Mellon University and published at ICLR 2024.[^s1][^s2]

## Environment

The environment reproduces four common kinds of website using open-source software populated with realistic data: an e-commerce store built on Adobe Magento with roughly 90,000 products, a Reddit-like forum running Postmill, a GitLab instance with about 300 repositories, and the Magento administration portal as a content-management system.[^s1] Agents can also use an OpenStreetMap-based map of the north-eastern United States, a calculator, a scratchpad, an offline copy of an encyclopedia, and the GitLab and Adobe Commerce user manuals, mirroring the way people consult tools and documentation while browsing.[^s1] Because every site runs in a container, the state can be reset between episodes, which makes runs reproducible.[^s1][^s2]

An agent observes the current URL, the open tabs and the page content, which can be rendered as raw HTML, a screenshot or an accessibility tree. It acts through 12 browser-level actions such as click, hover, type, press, scroll, opening and closing tabs, going back or forward, and visiting a URL, selecting elements either by coordinates or by element ID.[^s1]

## Tasks and scoring

The benchmark contains 812 task intents generated from 241 templates, spread across the shopping site, the admin portal, GitLab, the map, the forum and a small share of cross-site tasks.[^s1] Tasks fall into three groups: information seeking, site navigation, and creating content or changing configuration. Some are deliberately unachievable, and the agent is expected to report that rather than guess.[^s1]

Scoring targets functional correctness rather than imitation of a reference action sequence. Answers to information-seeking tasks are checked by exact match, by required substrings, or by a fuzzy match judged by GPT-4; the other tasks are checked programmatically by inspecting URLs, database records or page content after the episode, so any route that reaches the right end state counts.[^s1]

## Original findings

In the paper, human testers completed 78.24% of tasks, while the best GPT-4 agent using chain-of-thought reasoning reached 14.41%.[^s1][^s2] Adding a hint that some tasks might be impossible made GPT-4 worse: it then declared more than half of the feasible tasks unachievable. The authors also observed agents settling on the first plausible information they found, misreading earlier inputs and repeating actions until the step limit, and highly variable success among tasks drawn from the same template.[^s1]

## Extensions and limitations

WebArena spawned a family of follow-ups. VisualWebArena, published at ACL 2024 by an overlapping team, adds tasks that require understanding images on the page and found clear limits in both text-only and multimodal agents.[^s3] Heavy use also exposed weaknesses in the original checkers. In a 2025 NeurIPS workshop paper, El hattami and colleagues audited all 812 tasks, reporting ambiguous instructions, misaligned evaluations and brittle substring matching; their WebArena Verified release substitutes type-aware comparisons, verifies backend state for tasks that change data, reports confidence intervals, and offers a 137-task "Hard" subset that cuts evaluation cost by 83%.[^s4] As with other agent benchmarks, published scores depend on the checker version and run protocol, so comparisons are only meaningful under the same setup.[^s4]

## Connections

WebArena is an instrument of **AI evaluation** for **AI agents**, its two broader nodes.[^s1] It was **introduced in** the 2023 paper and **created by** **Carnegie Mellon University** researchers.[^s1][^s2] **OSWorld** is its closest **alternative**: WebArena confines agents to self-hosted websites, whereas OSWorld covers whole desktops, and both underpin the evaluation of **computer-use agents**. **VisualWebArena** extends it to visually grounded tasks, and **WebArena Verified** **follows** it as a corrected evaluation layer.[^s3][^s4] Its fuzzy-match grader is an early use of an **LLM as a judge**, and its tasks were built to stress-test **large language model** agents on long-horizon web work.[^s1]

## Sources
[^s1]: Zhou, Xu et al., "WebArena: A Realistic Web Environment for Building Autonomous Agents", arXiv 2307.13854, 2023. https://arxiv.org/pdf/2307.13854 (accessed 2026-11-18)
[^s2]: Zhou, Xu et al., "WebArena: A Realistic Web Environment for Building Autonomous Agents", ICLR 2024 poster page. https://iclr.cc/virtual/2024/poster/17826 (accessed 2026-11-18)
[^s3]: Koh et al., "VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks", ACL 2024. https://aclanthology.org/2024.acl-long.50 (accessed 2026-11-18)
[^s4]: El hattami, Thakkar, Chapados and Pal, "WebArena Verified: Reliable Evaluation for Web Agents", NeurIPS 2025 Workshop on Scaling Environments for Agents. https://neurips.cc/virtual/2025/124576 (accessed 2026-11-18)
