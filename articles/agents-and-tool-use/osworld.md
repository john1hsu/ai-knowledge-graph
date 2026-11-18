---
id: kt:osworld
type: Benchmark
title: OSWorld
aliases: [OSWorld benchmark, OSWorld-Verified]
domain: agents-and-tool-use
summary: >-
  A benchmark and executable environment, presented at NeurIPS 2024, that tests multimodal agents on
  369 open-ended tasks inside real virtual machines running desktop software, scoring each attempt with
  a task-specific script that inspects the final machine state; its 2025 OSWorld-Verified revision is
  the standard yardstick for computer-use agents.
maturity: emerging
broader: [kt:ai-evaluation, kt:computer-use-agents]
related: [kt:alfworld, kt:swe-bench, kt:vision-language-model, kt:ai-agent]
relations:
  - {predicate: introducedIn, object: kt:osworld-benchmarking-multimodal-agents-for-open-ended-tasks-in-real-computer-environments}
  - {predicate: createdBy, object: kt:university-of-hong-kong}
  - {predicate: createdBy, object: kt:salesforce-research}
  - {predicate: alternativeTo, object: kt:webarena}
sources:
  - id: s1
    title: "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments"
    publisher: arXiv 2404.07972 (Xie, Zhang et al.; authors' version)
    url: https://arxiv.org/pdf/2404.07972
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments (proceedings)"
    publisher: NeurIPS 2024 Datasets and Benchmarks Track
    url: https://proceedings.neurips.cc/paper_files/paper/2024/hash/5d413e48f84dc61244b6be550f1cd8f5-Abstract-Datasets_and_Benchmarks_Track.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "xlang-ai/OSWorld repository README"
    publisher: XLANG Lab, GitHub
    url: https://github.com/xlang-ai/OSWorld
    type: official-docs
    accessed: 2026-11-18
  - id: s4
    title: "Introducing OSWorld-Verified"
    publisher: XLANG Lab (University of Hong Kong) blog, 28 July 2025
    url: https://xlang.ai/blog/osworld-verified
    type: academic
    accessed: 2026-11-18
  - id: s5
    title: "Introducing Claude Sonnet 4.5"
    publisher: Anthropic, 29 September 2025
    url: https://www.anthropic.com/news/claude-sonnet-4-5
    type: lab-research
    accessed: 2026-11-18
  - id: s6
    title: "Introducing Claude Sonnet 4.6"
    publisher: Anthropic, 17 February 2026
    url: https://www.anthropic.com/news/claude-sonnet-4-6
    type: lab-research
    accessed: 2026-11-18
created: 2026-11-18
---

# OSWorld

OSWorld is a benchmark for agents that use computers through their graphical interfaces. Instead of simulating a website or a text game, it boots real virtual machines, loads a prepared starting state, hands the agent a natural-language instruction, and afterwards runs a checking script against the files, settings and application state the agent left behind. It was released in April 2024 by Tianbao Xie, Tao Yu and colleagues at the University of Hong Kong, with collaborators from Carnegie Mellon and Salesforce Research, and was published in the NeurIPS 2024 Datasets and Benchmarks Track.[^s1][^s2][^s3]

## Design

The core set has 369 tasks built on Ubuntu, plus 43 supplementary Windows tasks that need a licensed system image; the environment itself can also host macOS.[^s1] Each task bundles three pieces: the instruction, a configuration that sets up the initial state (opening files, launching apps, downloading inputs), and an execution-based evaluator. Across the suite the authors wrote 302 distinct initial states and 134 evaluation functions, so success is judged by outcome rather than by matching a reference action sequence — any route that produces the correct end state counts.[^s1]

Tasks span everyday and professional software: Chrome, VLC, Thunderbird, VS Code, GIMP, the LibreOffice Calc, Writer and Impress suite, and basic operating-system tools such as the terminal and file manager. About 27% (101 tasks) are workflows that cross several applications, and 30 tasks (about 8%) are deliberately infeasible, rewarding an agent that recognises an impossible request and declines instead of improvising.[^s1]

Agents can observe raw screenshots, the accessibility (a11y) tree, both together, or a Set-of-Mark view in which interactive elements are boxed and numbered on the screenshot. Actions are mostly Python `pyautogui` calls, with special `WAIT`, `FAIL` and `DONE` tokens.[^s1] The open-source harness (Apache-2.0) runs the machines on VMware, VirtualBox, Docker or cloud hosts such as AWS, and supports parallel runs.[^s3]

## Original findings

In the paper, human testers completed 72.36% of tasks, while the best model configuration — GPT-4 given the accessibility tree — reached 12.24%.[^s1][^s2] The authors' error analysis found that inaccurate mouse clicks appeared in over three-quarters of failed GPT-4V episodes, often after a sensible plan; agents also lacked knowledge of specialised software and were thrown off by moved or resized windows and cluttered screens. Higher screenshot resolution generally helped screenshot-only agents, and adding text-based history of earlier steps helped more than adding past screenshots.[^s1]

## OSWorld-Verified

Heavy use exposed reliability problems. In July 2025 the maintainers released OSWorld-Verified after roughly ten people spent about two months addressing around 300 reported issues: websites that blocked bots or changed layout, setup steps that ran before apps finished loading, ambiguous instructions, and evaluators that rejected valid alternative solutions such as an equivalent spreadsheet formula.[^s4] Most fixes loosened or repaired the checkers; the team also moved evaluation to AWS, where up to 50 environments run at once, cutting a full run from more than ten hours to minutes.[^s4] The maintainers note that scores depend strongly on the step budget — one model ranged from 9.1% to 23.0% across settings — so results are only comparable under the same protocol.[^s4]

## Results and limitations

Reported scores have risen quickly but come largely from developers' own runs. At the Verified launch the maintainers listed an agentic system, CoACT-1, as best at 60.76%.[^s4] Anthropic reported 61.4% for Claude Sonnet 4.5 in September 2025, using the official framework with a 100-step limit averaged over four runs.[^s5] Anthropic itself cautions that the benchmark is a strong but incomplete measure of real-world computer use.[^s6] Other open issues follow from the design: a fixed task set invites overfitting, live websites drift, and outcome checkers can still misjudge unusual but correct solutions.[^s4]

## Connections

OSWorld is an instrument of **AI evaluation** and the reference benchmark for **computer-use agents**, which is why both are its broader nodes.[^s1] It was **introduced in** the NeurIPS 2024 paper and **created by** the University of Hong Kong's XLANG Lab with **Salesforce Research**.[^s2][^s3] It complements **WebArena**, which confines agents to self-hosted websites, whereas OSWorld covers whole desktops, and it sits beside **ALFWorld** and **SWE-bench** as execution-checked agent benchmarks. Its tasks demand a **vision-language model** that can ground instructions in pixels, and **Anthropic** has used it to track successive Claude models.[^s5][^s6]

## Sources
[^s1]: Xie et al., "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments", arXiv 2404.07972, 2024. https://arxiv.org/pdf/2404.07972 (accessed 2026-11-18)
[^s2]: Xie et al., "OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments", NeurIPS 2024 Datasets and Benchmarks Track. https://proceedings.neurips.cc/paper_files/paper/2024/hash/5d413e48f84dc61244b6be550f1cd8f5-Abstract-Datasets_and_Benchmarks_Track.html (accessed 2026-11-18)
[^s3]: XLANG Lab, "OSWorld" repository README, GitHub. https://github.com/xlang-ai/OSWorld (accessed 2026-11-18)
[^s4]: XLANG Lab, "Introducing OSWorld-Verified", 28 July 2025. https://xlang.ai/blog/osworld-verified (accessed 2026-11-18)
[^s5]: Anthropic, "Introducing Claude Sonnet 4.5", 29 September 2025. https://www.anthropic.com/news/claude-sonnet-4-5 (accessed 2026-11-18)
[^s6]: Anthropic, "Introducing Claude Sonnet 4.6", 17 February 2026. https://www.anthropic.com/news/claude-sonnet-4-6 (accessed 2026-11-18)
