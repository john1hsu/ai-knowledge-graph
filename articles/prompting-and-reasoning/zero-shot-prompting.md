---
id: kt:zero-shot-prompting
type: Technique
title: Zero-shot prompting
aliases: [zero-shot prompt, instruction-only prompting, zero-shot in-context learning]
domain: prompting-and-reasoning
summary: >-
  Prompting a language model to carry out a task from a natural-language instruction (and the input) alone,
  with no worked demonstrations in the prompt and no weight updates, relying on what the model learned in
  pretraining and instruction tuning.
maturity: established
broader: [kt:prompt-engineering]
related: [kt:instruction-tuning, kt:chain-of-thought, kt:prompt-sensitivity, kt:zero-shot-learning, kt:large-language-model]
relations:
  - {predicate: introducedIn, object: kt:language-models-are-few-shot-learners}
  - {predicate: contrastsWith, object: kt:few-shot-prompting}
  - {predicate: dependsOn, object: kt:in-context-learning}
  - {predicate: influencedBy, object: kt:finetuned-language-models-are-zero-shot-learners}
sources:
  - id: s1
    title: "Language Models are Few-Shot Learners"
    publisher: arXiv 2005.14165 via ar5iv (Brown, Mann, Ryder, Subbiah, Kaplan, Dhariwal, et al.; NeurIPS 2020)
    url: https://ar5iv.arxiv.org/html/2005.14165
    type: primary
    accessed: 2026-11-16
  - id: s2
    title: "Finetuned Language Models Are Zero-Shot Learners"
    publisher: arXiv 2109.01652, authors' version of the ICLR 2022 paper (Wei, Bosma, Zhao, Guu, Yu, Lester, Du, Dai, Le)
    url: https://arxiv.org/pdf/2109.01652
    type: primary
    accessed: 2026-11-16
  - id: s3
    title: "Multitask Prompted Training Enables Zero-Shot Task Generalization"
    publisher: arXiv 2110.08207, authors' version of the ICLR 2022 paper (Sanh, Webson, Raffel, Bach, et al.; BigScience)
    url: https://arxiv.org/pdf/2110.08207
    type: primary
    accessed: 2026-11-16
  - id: s4
    title: "Large Language Models are Zero-Shot Reasoners"
    publisher: NeurIPS 2022, Advances in Neural Information Processing Systems 35 (Kojima, Gu, Reid, Matsuo, Iwasawa)
    url: https://proceedings.neurips.cc/paper/2022/hash/8bb0d291acd4acf06ef112099c16f326-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "Prompting best practices: be clear and direct"
    publisher: Anthropic, Claude Platform documentation
    url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/be-clear-and-direct
    type: official-docs
    accessed: 2026-11-16
created: 2026-11-16
---

# Zero-shot prompting

**Zero-shot prompting** asks a language model to perform a task using only a natural-language description of that task plus the input to work on. The prompt contains no solved examples, and the model's weights are not changed. The GPT-3 paper (Brown et al., 2020) gave the setting its now-standard name, placing it at one end of a spectrum: zero-shot (instruction only), one-shot (a single demonstration) and few-shot (typically 10 to 100 demonstrations), all without gradient updates.[^s1]

## How it works

A zero-shot prompt is simply an instruction followed by the input, for example "Translate the following sentence into French:" and then the sentence. The model must infer the task, the expected output format and any implicit constraints from the wording alone, drawing on patterns it absorbed during pretraining.[^s1] Because nothing in the context window shows what a correct answer looks like, the instruction carries all of the task specification. Vendor guidance therefore stresses explicit, specific instructions and the reasons behind them: Anthropic's documentation compares the model to a capable new employee who lacks context on your norms, and suggests testing a prompt by checking whether a colleague with little background could follow it.[^s5]

## Why it matters and its limitations

Brown et al. describe the zero-shot setting as offering maximum convenience, potential robustness and avoidance of spurious correlations from examples, but also as the hardest setting, and at times "unfairly hard" because an instruction can be ambiguous about format.[^s1] They also argue it is closest to how people are asked to do many tasks. In their experiments, zero-shot accuracy rose steadily with model size, but few-shot accuracy rose faster, so the gap between the two settings tended to widen as models grew (results reported in 2020).[^s1]

Raw zero-shot ability in base models proved weak on many tasks, which motivated **instruction tuning**. Google's FLAN work (Wei et al., ICLR 2022) fine-tuned a 137B-parameter model on more than 60 datasets phrased as instructions; the tuned model beat zero-shot GPT-3 175B on 20 of 25 evaluated datasets. The same study found that instruction tuning helped only at large scale and hurt held-out performance for models of 8B parameters or smaller, and that removing the instructions from the training data sharply reduced the benefit.[^s2] In parallel, the BigScience T0 model (Sanh et al., ICLR 2022) trained an 11B-parameter T5 variant on a large pool of crowd-written prompts and matched or beat GPT-3 on 9 of 11 held-out datasets despite being about 16 times smaller. Training on more prompts per dataset also raised median performance and reduced variance across paraphrased prompts.[^s3] That variance is the main practical weakness of zero-shot prompting: small changes to wording can move results, which is one face of the broader prompt-sensitivity problem.[^s3]

## Zero-shot reasoning

Zero-shot prompts were long thought to be poor at multi-step reasoning, where chain-of-thought methods relied on hand-written worked examples. Kojima et al. (NeurIPS 2022) showed that appending one trigger phrase, "Let's think step by step", before the answer elicits step-by-step reasoning without any demonstrations. With InstructGPT (text-davinci-002), accuracy rose from 17.7% to 78.7% on MultiArith and from 10.4% to 40.7% on GSM8K, with gains of similar size reported for the 540B-parameter PaLM.[^s4] The authors present this "zero-shot chain-of-thought" as a strong baseline that should be checked before building fine-tuning datasets or few-shot exemplars.[^s4]

## In practice

For instruction-tuned chat models, zero-shot prompting is the default way most tasks are posed: a system prompt and a clear user instruction. Practitioners usually start zero-shot and add demonstrations only when the output format, tone or edge cases need to be pinned down; Anthropic's guide, for instance, recommends adding three to five well-chosen examples when examples are needed to steer structure.[^s5] Zero-shot prompts are cheaper (fewer tokens), avoid biasing the model toward the surface features of particular examples, and are easier to maintain, at the cost of less control over format.[^s1][^s5]

## Connections

Zero-shot prompting is a technique within **prompt engineering** and one setting of **in-context learning**, the case where the context holds an instruction but no demonstrations.[^s1] It **contrasts with few-shot prompting**, its neighbour on the GPT-3 spectrum, and its name and framing were **introduced in** "Language Models are Few-Shot Learners".[^s1] Its effectiveness on modern models owes much to **instruction tuning**, whose FLAN paper, "Finetuned Language Models Are Zero-Shot Learners", **influenced** how the technique is used.[^s2] Its sensitivity to wording links it to **prompt sensitivity**,[^s3] and the zero-shot reasoning trigger connects it to **chain-of-thought** prompting.[^s4] It shares a name, but not a subject, with the broader **zero-shot learning** node; here the "zero" counts demonstrations placed in a **large language model**'s prompt, not training examples.[^s1]

## Sources
[^s1]: Brown et al., "Language Models are Few-Shot Learners", NeurIPS 2020 (arXiv 2005.14165). https://ar5iv.arxiv.org/html/2005.14165 (accessed 2026-11-16)
[^s2]: Wei et al., "Finetuned Language Models Are Zero-Shot Learners", ICLR 2022 (arXiv 2109.01652). https://arxiv.org/pdf/2109.01652 (accessed 2026-11-16)
[^s3]: Sanh et al., "Multitask Prompted Training Enables Zero-Shot Task Generalization", ICLR 2022 (arXiv 2110.08207). https://arxiv.org/pdf/2110.08207 (accessed 2026-11-16)
[^s4]: Kojima et al., "Large Language Models are Zero-Shot Reasoners", NeurIPS 2022. https://proceedings.neurips.cc/paper/2022/hash/8bb0d291acd4acf06ef112099c16f326-Abstract-Conference.html (accessed 2026-11-16)
[^s5]: Anthropic, "Prompting best practices: be clear and direct", Claude Platform docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/be-clear-and-direct (accessed 2026-11-16)
