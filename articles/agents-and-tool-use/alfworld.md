---
id: kt:alfworld
type: Benchmark
title: ALFWorld
aliases: [ALFWorld benchmark, ALFWorld environment]
domain: agents-and-tool-use
summary: >-
  An interactive simulator, introduced at ICLR 2021 by researchers from the University of Washington,
  Microsoft Research and Carnegie Mellon, that pairs text-adventure versions of household tasks with
  their visually embodied counterparts from the ALFRED benchmark; its text games became a standard
  testbed for LLM agents such as ReAct and Reflexion.
maturity: established
broader: [kt:ai-evaluation, kt:ai-agent]
related: [kt:planning-in-llms, kt:swe-bench, kt:embodied-ai]
relations:
  - {predicate: introducedIn, object: kt:alfworld-aligning-text-and-embodied-environments-for-interactive-learning}
  - {predicate: createdBy, object: kt:microsoft-research}
  - {predicate: basedOn, object: kt:alfred-benchmark}
  - {predicate: basedOn, object: kt:textworld}
  - {predicate: usedIn, object: kt:react-prompting}
  - {predicate: usedIn, object: kt:reflexion}
  - {predicate: partOf, object: kt:agentbench}
sources:
  - id: s1
    title: "ALFWorld: Aligning Text and Embodied Environments for Interactive Learning (v2)"
    publisher: arXiv 2010.03768 (Shridhar, Yuan, Côté, Bisk, Trischler, Hausknecht; authors' version)
    url: https://arxiv.org/pdf/2010.03768v2.pdf
    type: primary
    accessed: 2026-11-17
  - id: s2
    title: "ALFWorld: Aligning Text and Embodied Environments for Interactive Learning (poster)"
    publisher: ICLR 2021
    url: https://iclr.cc/virtual/2021/poster/2973
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s3
    title: "ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks"
    publisher: CVPR 2020 (Shridhar et al.), CVF Open Access
    url: https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "ReAct: Synergizing Reasoning and Acting in Language Models"
    publisher: arXiv 2210.03629 (Yao et al.; authors' version, ICLR 2023)
    url: https://arxiv.org/pdf/2210.03629
    type: primary
    accessed: 2026-11-17
  - id: s5
    title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    publisher: arXiv 2303.11366 (Shinn et al.; authors' version, NeurIPS 2023)
    url: https://arxiv.org/pdf/2303.11366
    type: primary
    accessed: 2026-11-17
  - id: s6
    title: "AgentBench: Evaluating LLMs as Agents"
    publisher: arXiv 2308.03688 (Liu et al.; authors' version, ICLR 2024)
    url: https://arxiv.org/pdf/2308.03688
    type: primary
    accessed: 2026-11-17
created: 2026-11-17
---

# ALFWorld

**ALFWorld** is a simulator that aligns two views of the same household tasks: an abstract, text-only game built with Microsoft's TextWorld engine, and a visually rendered, physically embodied version taken from the ALFRED benchmark.[^s1] It was introduced by Mohit Shridhar, Xingdi (Eric) Yuan, Marc-Alexandre Côté, Yonatan Bisk, Adam Trischler and Matthew Hausknecht, and presented at ICLR 2021.[^s2] The authors' goal was to let an agent learn high-level policies cheaply in text and then carry them out in the visual world. They described it as the first interactive, parallel environment linking text commands with embodied robotic simulation.[^s1] Since 2022 its text games have mainly served as a benchmark for agents built on large language models.[^s4]

## Origins in ALFRED

ALFRED, presented at CVPR 2020 by largely the same group, maps natural-language instructions and egocentric vision to action sequences for everyday household tasks. It has about 25,000 directives, each backed by expert demonstrations in an interactive 3D environment.[^s3] Its tasks are long and compositional and include state changes that cannot be undone, and the authors' baseline model performed poorly on it.[^s3] ALFWorld keeps ALFRED's goal descriptions but drops its step-by-step instructions, so the agent must plan the steps itself.[^s1]

## How it works

Each ALFRED scene is described in the Planning Domain Definition Language (PDDL), and the TextWorld engine generates an equivalent text game. A classical planner (Fast Downward) tracks the game state as logical predicates, and template grammars turn that state into text observations.[^s1] The text agent issues high-level commands such as *go to*, *take*, *open*, *heat*, *cool* and *clean*. The embodied side uses low-level actions in the THOR simulator: move, rotate, pick up, toggle and so on.[^s1]

The benchmark covers six task types: pick and place, examine in light, clean and place, heat and place, cool and place, and pick two and place. They are spread over 120 rooms: kitchens, bedrooms, bathrooms and living rooms.[^s1] There are 3,553 training tasks, 140 "seen" test tasks (familiar rooms, new instances) and 134 "unseen" test tasks set in new rooms and layouts.[^s1]

The paper's reference agent, BUTLER, has three modules. A Transformer sequence-to-sequence "brain" is trained in text with DAgger imitation learning from a rule-based expert. A Mask R-CNN "vision" module converts frames into text-like observations. A "body" controller uses an A* navigator and the ALFRED manipulation API.[^s1] Pretraining in text ran about seven times faster than embodied training: 6.1 episodes per second versus 0.9. It also transferred better to unseen embodied tasks, with 34.3% success against 23.1% for embodied-only training.[^s1] Absolute numbers were still low. Zero-shot, BUTLER succeeded on 19% of seen and 10% of unseen embodied tasks.[^s1]

## Use as an LLM-agent benchmark

ALFWorld became widely known when the ReAct paper (Yao et al., ICLR 2023) used its 134 unseen text games to test few-shot prompted agents. Each prompt held two example trajectories of the same task type.[^s4] With PaLM-540B, the best ReAct prompt reached 71% success. The best action-only prompt reached 45%, and BUTLER, trained by imitation on 10^5 expert trajectories per task type, reached 37%.[^s4] In the same paper's appendix, GPT-3 (text-davinci-002) reached 78.4%.[^s4] Reflexion (Shinn et al., NeurIPS 2023) added verbal self-reflection between attempts. It reported completing 130 of 134 tasks, an absolute 22-point gain over ReAct across 12 trials.[^s5] The authors traced most baseline failures to the agent wrongly believing it held an object and then never backtracking.[^s5] AgentBench (ICLR 2024) turned ALFWorld into its "house-holding" environment with 50 test problems. There, GPT-4 (0613) scored 78% success, while most open-source models scored between 0% and 8%. Invalid actions caused most failures.[^s6]

## Limitations

ALFWorld's text side is a simplification. The authors note that the text-to-embodied transfer loses accuracy through object-detection errors, navigation collisions and physical constraints, and that their navigator relies on a pre-built map, which is a strong prior.[^s1] Results with human-written goals were preliminary and much weaker: 8% seen and 3% unseen.[^s1] For LLM work, the small, fixed test set and the exemplar-based prompting mean that scores depend heavily on prompt design. Most LLM papers also use only the text games, so high scores say little about perception or motor control.[^s4][^s5]

## Connections

ALFWorld is a benchmark under **AI evaluation** and a standard testbed for **AI agents**. It was **introduced in** the 2021 ALFWorld paper and **co-created by Microsoft Research** with university partners.[^s1][^s2] It is **based on** the **ALFRED** embodied benchmark and the **TextWorld** text-game engine.[^s1][^s3] Its tasks need multi-step **planning**, which ties it to work on **planning in LLMs**, and its embodied half links it to **embodied AI**.[^s1] It was **used in** **ReAct** and **Reflexion**, and it is **part of AgentBench**.[^s4][^s5][^s6] Like **SWE-bench**, it scores agents by whether an interactive task ends in success rather than by matching text.[^s6]

## Sources
[^s1]: Shridhar et al., "ALFWorld: Aligning Text and Embodied Environments for Interactive Learning", arXiv 2010.03768v2. https://arxiv.org/pdf/2010.03768v2.pdf (accessed 2026-11-17)
[^s2]: ICLR 2021 poster page, "ALFWorld: Aligning Text and Embodied Environments for Interactive Learning". https://iclr.cc/virtual/2021/poster/2973 (accessed 2026-11-17)
[^s3]: Shridhar et al., "ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks", CVPR 2020. https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html (accessed 2026-11-17)
[^s4]: Yao et al., "ReAct: Synergizing Reasoning and Acting in Language Models", arXiv 2210.03629. https://arxiv.org/pdf/2210.03629 (accessed 2026-11-17)
[^s5]: Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning", arXiv 2303.11366. https://arxiv.org/pdf/2303.11366 (accessed 2026-11-17)
[^s6]: Liu et al., "AgentBench: Evaluating LLMs as Agents", arXiv 2308.03688. https://arxiv.org/pdf/2308.03688 (accessed 2026-11-17)
