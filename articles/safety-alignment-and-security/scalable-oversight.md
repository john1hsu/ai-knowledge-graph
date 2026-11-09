---
id: kt:scalable-oversight
type: Concept
title: Scalable oversight
aliases: [scalable supervision, superhuman oversight problem]
domain: safety-alignment-and-security
summary: >-
  The alignment research problem of supervising AI systems reliably when a full human evaluation of their
  behaviour is too costly, or when the systems may come to exceed human skill at the task being judged.
maturity: emerging
broader: [kt:ai-alignment]
related: [kt:rlhf, kt:reward-hacking]
relations:
  - {predicate: introducedIn, object: kt:concrete-problems-in-ai-safety}
  - {predicate: hasPart, object: kt:ai-safety-via-debate}
  - {predicate: hasPart, object: kt:iterated-amplification}
  - {predicate: hasPart, object: kt:weak-to-strong-generalization}
sources:
  - id: s1
    title: "Concrete Problems in AI Safety"
    publisher: arXiv:1606.06565 (Amodei, Olah, Steinhardt, Christiano, Schulman, Mané), v2 July 2016
    url: https://arxiv.org/abs/1606.06565v2
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "AI safety via debate"
    publisher: arXiv:1805.00899 (Irving, Christiano, Amodei), May 2018, revised October 2018
    url: https://www.arxiv.org/abs/1805.00899
    type: primary
    accessed: 2026-11-09
  - id: s3
    title: "Supervising strong learners by amplifying weak experts"
    publisher: arXiv:1810.08575 (Christiano, Shlegeris, Amodei), October 2018
    url: https://arxiv.org/abs/1810.08575v1
    type: primary
    accessed: 2026-11-09
  - id: s4
    title: "Measuring Progress on Scalable Oversight for Large Language Models"
    publisher: arXiv:2211.03540 (Bowman, Hyun, Perez et al., Anthropic), November 2022
    url: https://arxiv.org/abs/2211.03540v2
    type: primary
    accessed: 2026-11-09
  - id: s5
    title: "Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision"
    publisher: arXiv:2312.09390 (Burns, Izmailov, Kirchner et al., OpenAI), December 2023
    url: https://arxiv.org/abs/2312.09390v1
    type: primary
    accessed: 2026-11-09
  - id: s6
    title: "Debating with More Persuasive LLMs Leads to More Truthful Answers"
    publisher: ICML 2024 (Khan, Hughes, Valentine, Ruis, Sachan, Radhakrishnan, Grefenstette, Bowman, Rocktäschel, Perez)
    url: https://icml.cc/virtual/2024/poster/33360
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# Scalable oversight

Scalable oversight is the problem of giving an AI system a trustworthy training and evaluation signal when checking its work properly is expensive, slow, or beyond the competence of the people doing the checking. The term entered the safety literature through *Concrete Problems in AI Safety* (Amodei, Olah, Steinhardt, Christiano, Schulman and Mané, 2016), which listed it as one of five practical accident-risk problems. There it describes a true objective that is too costly to evaluate often, so that training must lean on cheaper proxies and spend a limited budget of careful evaluation wisely.[^s1] Later work widened the framing: Bowman and colleagues at Anthropic defined it as supervising systems that may outperform humans on most skills relevant to the task at hand.[^s4]

## Why it is hard

Most current alignment methods assume a person can tell good behaviour from bad. Burns and colleagues at OpenAI point out that techniques such as RLHF depend on humans evaluating model outputs, and that future superhuman models may behave in ways too complex for people to judge reliably, leaving humans as only weak supervisors.[^s5] Irving, Christiano and Amodei make the same point for direct human judging: it fails once a task is too complicated for a person to assess.[^s2] When the overseer cannot see the difference between a good answer and a convincing-looking one, optimisation pressure can reward the latter, which links the problem to reward hacking.

The 2016 paper illustrated the cheaper-proxy version with a cleaning robot whose real reward would be a thorough human inspection. The robot might learn that asking whether the room is clean, or looking for visible dirt, approximates that inspection; sweeping mess under a rug breaks the link between proxy and truth, and a good learner should notice.[^s1] The authors proposed semi-supervised reinforcement learning, where reward is observed on only a small fraction of episodes, plus distant supervision and hierarchical RL, and suggested starting with reward on about 10% of episodes in simple control tasks.[^s1]

## Main approaches

**Debate.** Irving, Christiano and Amodei (2018) proposed training two agents by self-play in a zero-sum game: they alternate short statements about a question and a human judges which side gave the most true, useful information. By analogy to complexity theory they argued that debate with optimal play could answer any PSPACE question with polynomial-time judges, versus NP for direct judging. In a toy MNIST experiment, debating agents raised a sparse classifier's accuracy from 59.4% to 88.9% with six revealed pixels.[^s2] An ICML 2024 best-paper study by Khan and colleagues tested debate with LLMs: non-expert judges choosing between two expert models' arguments reached 76% accuracy for model judges and 88% for human judges, against naive baselines of 48% and 60%. Making debaters more persuasive also helped judges find the truth.[^s6]

**Iterated amplification.** Christiano, Shlegeris and Amodei (2018) proposed building a training signal for hard problems step by step, combining a model's solutions to easier subproblems so that an amplified human-plus-model team can supervise the next model. It resembles Expert Iteration but uses no external reward function, and learned complex behaviours efficiently in algorithmic environments.[^s3]

**Weak-to-strong generalization.** Burns and colleagues (2023) studied an analogy: can a weak model elicit the full capabilities of a much stronger one? Fine-tuning GPT-4-family models on labels from much weaker supervisors consistently beat the supervisor but fell well short of the strong model's ceiling. Adding an auxiliary confidence loss let a GPT-2-level supervisor recover close to GPT-3.5-level performance on NLP tasks, as reported by the authors.[^s5]

## Measuring progress

Because no current model broadly exceeds human ability, scalable oversight is hard to test directly. Bowman et al. (2022) proposed an experimental design using tasks that specialists can solve but that unaided non-experts and current models cannot, so that a method succeeds if it lets non-experts approach specialist accuracy. In a proof-of-concept on MMLU and a time-limited version of QuALITY, participants who simply chatted with an unreliable LLM assistant substantially outperformed both the model alone and their own unaided answers.[^s4] The authors read this as evidence that the problem can already be studied empirically.[^s4]

## Limitations and open questions

Each proposal rests on untested assumptions. Debate's authors stress that its practical value depends on empirical questions about human judges and tasks, and on what alignment should mean.[^s2] Weak-to-strong results suggest naive RLHF may scale poorly to superhuman models.[^s5] The positive debate results so far come from question-answering settings with known correct answers, which the ICML 2024 authors present as encouraging rather than conclusive evidence that debate can align models without ground-truth labels.[^s6] Bowman et al. likewise describe their experiment as a proof of concept using a deliberately simple assistant baseline.[^s4]

## Connections

Scalable oversight is a named sub-problem of **AI alignment** (`broader`), introduced in *Concrete Problems in AI Safety*.[^s1] It is the main known weakness of **RLHF**, whose signal is only as good as the human evaluator.[^s5] Failures of oversight let **reward hacking** go undetected, since proxies replace the true objective.[^s1] **Debate**, **iterated amplification** and **weak-to-strong generalization** are three research programmes for tackling it (`hasPart`).[^s2][^s3][^s5]

## Sources
[^s1]: Amodei et al., "Concrete Problems in AI Safety", arXiv:1606.06565 (2016). https://arxiv.org/abs/1606.06565v2 (accessed 2026-11-09)
[^s2]: Irving, Christiano and Amodei, "AI safety via debate", arXiv:1805.00899 (2018). https://www.arxiv.org/abs/1805.00899 (accessed 2026-11-09)
[^s3]: Christiano, Shlegeris and Amodei, "Supervising strong learners by amplifying weak experts", arXiv:1810.08575 (2018). https://arxiv.org/abs/1810.08575v1 (accessed 2026-11-09)
[^s4]: Bowman et al., "Measuring Progress on Scalable Oversight for Large Language Models", arXiv:2211.03540 (2022). https://arxiv.org/abs/2211.03540v2 (accessed 2026-11-09)
[^s5]: Burns et al., "Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision", arXiv:2312.09390 (2023). https://arxiv.org/abs/2312.09390v1 (accessed 2026-11-09)
[^s6]: Khan et al., "Debating with More Persuasive LLMs Leads to More Truthful Answers", ICML 2024. https://icml.cc/virtual/2024/poster/33360 (accessed 2026-11-09)
