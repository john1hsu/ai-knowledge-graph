---
id: kt:reflexion
type: Technique
title: Reflexion
aliases: [verbal reinforcement learning, "Reflexion: Language Agents with Verbal Reinforcement Learning", Shinn et al. 2023]
domain: prompting-and-reasoning
summary: >-
  A framework introduced by Shinn et al. (NeurIPS 2023) in which a language-model agent improves across
  repeated attempts at a task by writing natural-language reflections on its failures into an episodic
  memory that conditions later attempts, instead of updating model weights.
maturity: established
broader: [kt:self-correction, kt:ai-agent]
related: [kt:react-prompting, kt:chain-of-thought, kt:agent-memory, kt:test-time-compute, kt:self-refine-iterative-refinement-with-self-feedback]
relations:
  - {predicate: contrastsWith, object: kt:reinforcement-learning}
  - {predicate: extends, object: kt:react-prompting}
  - {predicate: evaluatedOn, object: kt:humaneval}
  - {predicate: evaluatedOn, object: kt:alfworld}
  - {predicate: evaluatedOn, object: kt:hotpotqa}
sources:
  - id: s1
    title: "Reflexion: Language Agents with Verbal Reinforcement Learning (abstract page)"
    publisher: NeurIPS 2023, Advances in Neural Information Processing Systems 36, pp. 8634-8652 (Shinn, Cassano, Gopinath, Narasimhan, Yao)
    url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Reflexion: Language Agents with Verbal Reinforcement Learning (full paper PDF)"
    publisher: NeurIPS 2023 proceedings (Shinn et al.)
    url: https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
    publisher: arXiv 2303.11366v4 (Shinn, Cassano, Berman, Gopinath, Narasimhan, Yao)
    url: https://arxiv.org/abs/2303.11366v4
    type: primary
    accessed: 2026-11-16
  - id: s4
    title: "Large Language Models Cannot Self-Correct Reasoning Yet"
    publisher: arXiv 2310.01798v2 (Huang, Chen, Mishra, Zheng, Yu, Song, Zhou; Google DeepMind and UIUC)
    url: https://arxiv.org/html/2310.01798v2
    type: primary
    accessed: 2026-11-16
  - id: s5
    title: "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs"
    publisher: TACL vol. 12, pp. 1417-1440, 2024 (Kamoi, Zhang, Zhang, Han, Zhang)
    url: https://aclanthology.org/2024.tacl-1.78
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s6
    title: "When Can LLMs Actually Correct Their Own Mistakes? (arXiv HTML version)"
    publisher: arXiv 2406.01297v2 (Kamoi et al.)
    url: https://arxiv.org/html/2406.01297v2
    type: primary
    accessed: 2026-11-16
created: 2026-11-16
---

# Reflexion

**Reflexion** is a framework for making language-model agents learn from trial and error without fine-tuning. After a failed attempt at a task, the agent writes a short natural-language reflection on what went wrong and stores it in an episodic memory buffer; on the next attempt that reflection is placed in the prompt so the agent can avoid the same mistake.[^s1] It was introduced by Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan and Shunyu Yao in "Reflexion: Language Agents with Verbal Reinforcement Learning", first posted to arXiv on 20 March 2023 and published at NeurIPS 2023.[^s1][^s3] The authors frame it as an alternative to conventional reinforcement learning, which needs many samples and costly weight updates to adapt an agent.[^s1]

## How it works

Reflexion combines three language-model roles with two kinds of memory.[^s2]

1. **Actor.** Generates text and actions from observations; the paper uses chain-of-thought and ReAct-style actors.[^s2]
2. **Evaluator.** Scores each trajectory. Depending on the task it is an exact-match check against the answer, hand-written heuristics or an LLM classifier for decision-making, or self-generated unit tests for code.[^s2]
3. **Self-reflection model.** Turns the sparse reward, the trajectory and existing memory into a specific verbal lesson, such as which action should have been taken differently.[^s2]

The trajectory acts as short-term memory, while the stored reflections form long-term memory. To fit the context window, long-term memory is capped at a few experiences, usually one to three: three reflections for AlfWorld and HotPotQA, one for programming.[^s2] The authors describe the reflection as a "semantic" gradient: a direction for improvement expressed in words rather than a numeric update to parameters.[^s2] Feedback can be scalar or free-form and can come from the environment or be simulated internally by the model.[^s1]

## Results

The paper evaluated Reflexion on sequential decision-making, multi-hop question answering and code generation.[^s1]

- **AlfWorld:** a ReAct agent with Reflexion completed 130 of 134 household tasks using a heuristic evaluator, an absolute gain of 22% over strong baselines across 12 trials.[^s2]
- **HotPotQA (100 questions):** Reflexion raised accuracy by about 20%; with GPT-4 a ReAct agent went from 0.39 to 0.51 and a chain-of-thought agent given ground-truth context from 0.68 to 0.80.[^s2]
- **Code:** on HumanEval (Python) Reflexion reported 91.0% pass@1 against 80.1% for GPT-4 alone, as reported by the authors in 2023; it also led on HumanEval and MBPP in Rust and on a set of 40 hard LeetCode problems, but trailed GPT-4 on MBPP Python (77.1 vs 80.1).[^s2]

Ablations showed both parts matter. On HotPotQA, adding self-reflection gave an 8-point absolute gain over replaying episodic memory alone; on the hardest 50 HumanEval Rust problems, removing either test generation or self-reflection erased the improvement (0.52 and 0.60 vs 0.68 for full Reflexion).[^s2]

## Limitations and critiques

The authors list several limits. Like other policy optimization, Reflexion can get stuck in local minima; its sliding-window memory is small; and on WebShop it did not clearly beat ReAct because the tasks need diverse exploration that reflections did not supply.[^s2] Self-generated tests are a weak evaluator for nondeterministic or impure code, and a 16.3% false-positive rate on MBPP Python explains the lower score there.[^s2] A smaller open model, starchat-beta, showed no gain (0.26 pass@1 before and after), which the authors read as evidence that self-correction emerges only in stronger models.[^s2]

Later work scrutinised the evaluation. Huang et al. noted that Reflexion's HotPotQA setup uses the correct label to decide when to stop retrying, and argued that gains of this kind vanish without such oracle labels; in their own tests GPT-4's HotPotQA score fell from 49 to 43 after two rounds of label-free self-correction.[^s4] A critical survey by Kamoi et al. in TACL classed the HotPotQA experiments as using oracle information that real applications lack, while treating the game and coding experiments, which use environment and interpreter feedback, as fairer.[^s6] Its broader conclusion is that self-correction works when reliable external feedback is available.[^s5]

## In practice

The evidence suggests Reflexion is most useful where an environment, test suite or other external check supplies an honest success signal between attempts, which is the setting of its AlfWorld and coding results.[^s2][^s5]

## Connections

Reflexion is a form of **self-correction** applied to **AI agents**, and its actor is a **ReAct**-style agent that it extends with reflection and memory.[^s2] It relies on **chain-of-thought** reasoning, stores lessons in a simple version of **agent memory**, and spends extra inference on repeated attempts, a kind of **test-time compute**.[^s2] It **contrasts with reinforcement learning** because it improves behaviour through text in context rather than weight updates.[^s1] It is concurrent with **Self-Refine**, which revises a single output within one attempt rather than across episodes.[^s2] Its experiments were run on **HumanEval**, **AlfWorld** and **HotPotQA**.[^s2]

## Sources
[^s1]: Shinn, Cassano, Gopinath, Narasimhan and Yao, "Reflexion: Language Agents with Verbal Reinforcement Learning", NeurIPS 2023 (abstract page). https://proceedings.neurips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract.html (accessed 2026-11-16)
[^s2]: Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning", NeurIPS 2023 (full paper). https://proceedings.neurips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf (accessed 2026-11-16)
[^s3]: Shinn et al., "Reflexion: Language Agents with Verbal Reinforcement Learning", arXiv 2303.11366v4. https://arxiv.org/abs/2303.11366v4 (accessed 2026-11-16)
[^s4]: Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet", arXiv 2310.01798v2. https://arxiv.org/html/2310.01798v2 (accessed 2026-11-16)
[^s5]: Kamoi, Zhang, Zhang, Han and Zhang, "When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs", TACL 12 (2024). https://aclanthology.org/2024.tacl-1.78 (accessed 2026-11-16)
[^s6]: Kamoi et al., "When Can LLMs Actually Correct Their Own Mistakes?", arXiv 2406.01297v2. https://arxiv.org/html/2406.01297v2 (accessed 2026-11-16)
