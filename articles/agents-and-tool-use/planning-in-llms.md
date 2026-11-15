---
id: kt:planning-in-llms
type: Concept
title: Planning in LLMs
aliases: [LLM planning, planning with large language models, LLM-based planning, LLM agent planning]
domain: agents-and-tool-use
summary: >-
  The use of large language models to turn a goal into an ordered sequence of subgoals or actions, either by
  generating plans directly (task decomposition, plan-then-execute prompting) or by working alongside classical
  planners and external verifiers that check and repair what the model proposes.
maturity: emerging
broader: [kt:ai-agent]
related: [kt:react-prompting, kt:tree-of-thoughts, kt:least-to-most-prompting, kt:agent-memory]
relations:
  - {predicate: influencedBy, object: kt:automated-planning}
  - {predicate: basedOn, object: kt:chain-of-thought}
sources:
  - id: s1
    title: "Understanding the planning of LLM agents: A survey"
    publisher: arXiv 2402.02716 (Huang et al., authors' version, Feb 2024)
    url: https://arxiv.org/abs/2402.02716v1
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents"
    publisher: ICML 2022 (Huang, Abbeel, Pathak, Mordatch; authors' arXiv version 2201.07207v2)
    url: https://arxiv.org/abs/2201.07207v2
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models"
    publisher: ACL 2023, Proceedings of the 61st Annual Meeting, pp. 2609–2634 (Wang et al.)
    url: https://aclanthology.org/2023.acl-long.147.xml
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "On the Planning Abilities of Large Language Models – A Critical Investigation"
    publisher: NeurIPS 2023 (Valmeekam, Marquez, Sreedharan, Kambhampati)
    url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/efb2072a358cefb75886a315a6fcf880-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "LLM+P: Empowering Large Language Models with Optimal Planning Proficiency"
    publisher: arXiv 2304.11477v3 (Liu, Jiang, Zhang, Liu, Zhang, Biswas, Stone; authors' version)
    url: https://arxiv.org/abs/2304.11477v3
    type: primary
    accessed: 2026-11-15
  - id: s6
    title: "Position: LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks"
    publisher: ICML 2024, PMLR 235 (Kambhampati et al.)
    url: https://proceedings.mlr.press/v235/kambhampati24a.html
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Planning in LLMs

Planning in LLMs refers to the family of methods in which a large language model works out what to do before (or while) doing it: breaking a goal into subgoals, ordering actions, choosing among candidate plans, and revising the plan when the world pushes back. It is one of the core capabilities attributed to LLM-based agents, alongside tool use and memory. A 2024 survey by Huang and colleagues sorts the literature into five overlapping strategies: task decomposition, plan selection, planning with external modules, reflection and refinement, and memory-augmented planning.[^s1]

## Origins and early results

An early demonstration came from Huang, Abbeel, Pathak and Mordatch at ICML 2022. They prompted large pretrained models to expand high-level household goals such as "make breakfast" into step-by-step action lists in the VirtualHome simulator, with no additional training. Sufficiently large models produced plausible decompositions, but many steps did not correspond to actions the environment could actually execute. The authors added a translation stage that mapped each free-form step onto the closest admissible action, conditioned on example demonstrations. Executability rose substantially, though human raters found a trade-off between executable plans and correct ones.[^s2] That tension between fluent plans and grounded, valid plans has run through the field since.

## Main approaches

**Plan-then-execute prompting.** Plan-and-Solve (PS) prompting, published at ACL 2023, targets the missing-step errors of zero-shot chain-of-thought. Instead of only asking the model to think step by step, the prompt first asks it to devise a plan that splits the problem into subtasks and then to carry those subtasks out. A variant, PS+, adds instructions aimed at reducing calculation errors. Using GPT-3, the authors reported that zero-shot PS beat zero-shot chain-of-thought on all ten reasoning datasets they tested and was roughly on par with 8-shot chain-of-thought on math problems.[^s3]

**Search over plans.** Rather than committing to one plan, some methods generate several candidates and select among them, for example by voting or by tree search with the model scoring partial plans; this is the survey's plan-selection category.[^s1]

**Hybrid planning with symbolic tools.** LLM+P (Liu et al., 2023) uses the model as a translator: it rewrites a natural-language problem as a Planning Domain Definition Language (PDDL) file, hands that file to a classical planner, and turns the planner's output back into natural language. On the authors' benchmark of common planning scenarios, LLM+P returned optimal plans for most problems, while the LLM on its own often failed to produce even a feasible plan.[^s5]

**Reflection and memory.** Agents can critique a failed plan, store lessons or past trajectories, and condition later planning on them.[^s1]

## Limitations and the critique

The most cited skeptical evidence comes from Kambhampati's group at Arizona State. At NeurIPS 2023, Valmeekam and colleagues generated test instances in domains like those of the International Planning Competition and measured whether models could produce valid plans on their own. The best model, GPT-4, averaged roughly 12% success across domains in that study, which the authors describe as a limited ability to generate executable plans autonomously. Results were better when LLM output was used as a heuristic to guide a sound planner, or when an external verifier sent feedback on failed plans and prompted the model to try again.[^s4]

A 2024 ICML position paper from the same group generalises this. It argues that autoregressive LLMs cannot, by themselves, plan or verify their own plans, and that self-verification is itself a form of reasoning that inherits the same limits. Its proposed alternative, the **LLM-Modulo** framework, keeps the LLM in a tight two-way loop with external, model-based verifiers. The LLM is treated as a broad but approximate source of knowledge, candidate plans and even draft domain models, while soundness comes from the verifiers.[^s6] Open questions include how far newer reasoning-focused models narrow the gap reported in 2023, and how to obtain reliable verifiers outside domains with formal models.[^s4][^s6]

## In practice

Production agent systems commonly combine an explicit planning step with execution and checking: a planner call writes a task list, executor steps call tools, and results feed back into re-planning. The survey's categories map directly onto such designs, with decomposition producing the task list, reflection handling failures, and memory carrying lessons forward.[^s1] Where a domain has a formal model (logistics, scheduling, robotics task specifications), the hybrid route of LLM translation plus a classical planner or validator offers correctness guarantees that free-form generation does not.[^s5][^s6]

## Connections

Planning is a component capability of an `kt:ai-agent`, so that node is its broader concept.[^s1] Plan-and-Solve is explicitly built on zero-shot `kt:chain-of-thought`, adding a plan stage before step-by-step reasoning.[^s3] It sits beside `kt:least-to-most-prompting`, another decomposition-first prompting method, and `kt:tree-of-thoughts`, an example of plan selection by search.[^s1] `kt:react-prompting` interleaves reasoning and acting step by step rather than planning up front, the reactive end of the same spectrum. Reflection-based and memory-based planning depend on `kt:agent-memory`.[^s1] Hybrid approaches such as LLM+P and LLM-Modulo draw on classical `kt:automated-planning` (PDDL and sound planners), which is where the field's validity standards come from.[^s5][^s6]

## Sources
[^s1]: Huang et al., "Understanding the planning of LLM agents: A survey", arXiv 2402.02716, 2024. https://arxiv.org/abs/2402.02716v1 (accessed 2026-11-15)
[^s2]: Huang, Abbeel, Pathak, Mordatch, "Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents", ICML 2022. https://arxiv.org/abs/2201.07207v2 (accessed 2026-11-15)
[^s3]: Wang et al., "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models", ACL 2023. https://aclanthology.org/2023.acl-long.147.xml (accessed 2026-11-15)
[^s4]: Valmeekam, Marquez, Sreedharan, Kambhampati, "On the Planning Abilities of Large Language Models – A Critical Investigation", NeurIPS 2023. https://proceedings.neurips.cc/paper_files/paper/2023/hash/efb2072a358cefb75886a315a6fcf880-Abstract.html (accessed 2026-11-15)
[^s5]: Liu et al., "LLM+P: Empowering Large Language Models with Optimal Planning Proficiency", arXiv 2304.11477, 2023. https://arxiv.org/abs/2304.11477v3 (accessed 2026-11-15)
[^s6]: Kambhampati et al., "Position: LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks", ICML 2024, PMLR 235. https://proceedings.mlr.press/v235/kambhampati24a.html (accessed 2026-11-15)
