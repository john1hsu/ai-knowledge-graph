---
id: kt:chain-of-thought
type: Technique
title: Chain-of-thought prompting
aliases: [chain of thought, CoT, CoT prompting, step-by-step prompting]
domain: prompting-and-reasoning
summary: >-
  A prompting technique in which a language model is led to write out a sequence of intermediate
  natural-language reasoning steps before giving its final answer, which improves accuracy on multi-step
  arithmetic, commonsense and symbolic reasoning tasks in sufficiently large models.
maturity: established
broader: [kt:prompt-engineering]
related: [kt:in-context-learning, kt:self-consistency, kt:reasoning-models, kt:react-prompting, kt:few-shot-prompting]
relations:
  - {predicate: introducedIn, object: kt:chain-of-thought-prompting-elicits-reasoning-in-large-language-models}
  - {predicate: basedOn, object: kt:large-language-model}
  - {predicate: evaluatedOn, object: kt:gsm8k}
  - {predicate: enables, object: kt:test-time-compute}
sources:
  - id: s1
    title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    publisher: NeurIPS 2022 (Wei, Wang, Schuurmans, Bosma, Ichter, Xia, Chi, Le, Zhou)
    url: https://proceedings.nips.cc/paper_files/paper/2022/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s2
    title: "Large Language Models are Zero-Shot Reasoners"
    publisher: NeurIPS 2022 (Kojima, Gu, Reid, Matsuo, Iwasawa)
    url: https://proceedings.neurips.cc/paper/2022/hash/8bb0d291acd4acf06ef112099c16f326-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s3
    title: "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
    publisher: arXiv 2203.11171 (Wang, Wei, Schuurmans, Le, Chi, Narang, Chowdhery, Zhou; ICLR 2023)
    url: https://arxiv.org/abs/2203.11171v4
    type: primary
    accessed: 2026-10-31
  - id: s4
    title: "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting"
    publisher: arXiv 2305.04388 (Turpin, Michael, Perez, Bowman; NeurIPS 2023)
    url: https://arxiv.org/abs/2305.04388v2
    type: primary
    accessed: 2026-10-31
  - id: s5
    title: "Prompting best practices (chain of thought)"
    publisher: Anthropic, Claude Platform documentation
    url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-of-thought
    type: official-docs
    accessed: 2026-10-31
created: 2026-10-31
---

# Chain-of-thought prompting

Chain-of-thought (CoT) prompting asks a large language model to produce a series of intermediate reasoning steps, written in natural language, on the way to its final answer. The technique was introduced by Jason Wei and colleagues at Google in a paper presented at NeurIPS 2022. They defined a chain of thought as intermediate reasoning steps "that lead to the final output" and showed that prompting for them improved results on arithmetic, commonsense and symbolic reasoning benchmarks.[^s1]

## How it works

In the original few-shot form, the prompt contains a handful of exemplars, each a triple of *input, chain of thought, output*. A maths exemplar might pose a word problem about tennis balls and answer with a one-line worked sum followed by the answer. The test question follows, and the model imitates the pattern by writing its own working before the answer.[^s1] No weights change: the method relies entirely on the model's ability to learn a format from examples in its context.[^s1]

Kojima and colleagues then showed that exemplars are not strictly needed. Adding a single trigger phrase, "Let's think step by step", before each answer turned the model into what they called a zero-shot reasoner.[^s2] With OpenAI's InstructGPT model text-davinci-002, this raised accuracy on MultiArith from 17.7% to 78.7% and on GSM8K from 10.4% to 40.7%, and similar gains appeared with the 540-billion-parameter PaLM model.[^s2]

A widely used extension is self-consistency. Instead of decoding one chain greedily, the model samples several diverse reasoning paths and the most frequent final answer is selected by majority vote.[^s3] Wang and colleagues reported that this improved on standard chain-of-thought prompting by 17.9% on GSM8K, 11.0% on SVAMP, 12.2% on AQuA, 6.4% on StrategyQA and 3.9% on ARC-challenge.[^s3]

## Evidence and limitations

The headline result in the original paper came from PaLM 540B prompted with eight chain-of-thought exemplars. It reached state-of-the-art accuracy on GSM8K at the time, beating a fine-tuned GPT-3 model that used a separate verifier. The paper's Figure 2 shows the solve rate rising from roughly 18% with standard prompting to roughly 57% with CoT.[^s1]

The gains depended strongly on scale. The authors found that CoT helped only for models of about 100 billion parameters or more; smaller models wrote fluent but illogical chains and did worse than with standard prompting.[^s1] They also flagged that a generated chain carries no guarantee of correct reasoning, and left open whether the network is truly reasoning in any deeper sense.[^s1]

A further concern is *faithfulness*: whether the written chain reflects what actually drove the answer. Turpin and colleagues biased few-shot prompts, for example by reordering multiple-choice options so the correct answer was always "(A)". Models followed the bias but their explanations did not mention it, instead rationalising the biased answer. Across 13 BIG-Bench Hard tasks, accuracy fell by as much as 36% for GPT-3.5 and Claude 1.0.[^s4] The study concluded that CoT explanations can be plausible yet misleading, so they should not be treated as a reliable window into model computation.[^s4]

## In practice

As of 2026, explicit CoT prompting has partly moved inside the models. Anthropic's Claude documentation describes manual CoT, such as asking the model to work through a problem and put the result in answer tags, as a fallback for when built-in thinking is turned off.[^s5] For its newest models the same page advises relying on the model's own thinking mode, tuned by an effort setting, and notes that prompts asking for written-out reasoning may be declined on some of them.[^s5] The documentation also warns that extended thinking adds tokens and latency, and suggests lowering effort or capping output length when that matters.[^s5]

## Connections

CoT is a technique within **prompt engineering** (`broader`) and builds on the few-shot, **in-context learning** abilities of **large language models**, since the original method teaches the reasoning format purely through exemplars in the prompt.[^s1] Its zero-shot variant shows the same behaviour can be elicited without **few-shot prompting**.[^s2] **Self-consistency** extends CoT by sampling many chains and voting, an early example of spending extra **test-time compute** for accuracy.[^s3] The arithmetic benchmark **GSM8K** was the main showcase for both papers.[^s1][^s2] **ReAct prompting** interleaves CoT-style reasoning with tool actions, and today's **reasoning models** internalise long reasoning traces that developers steer through settings rather than prompt wording.[^s5] Research on unfaithful explanations links CoT to interpretability and safety debates about whether visible reasoning can be trusted.[^s4]

## Sources
[^s1]: Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", NeurIPS 2022. https://proceedings.nips.cc/paper_files/paper/2022/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf (accessed 2026-10-31)
[^s2]: Kojima et al., "Large Language Models are Zero-Shot Reasoners", NeurIPS 2022. https://proceedings.neurips.cc/paper/2022/hash/8bb0d291acd4acf06ef112099c16f326-Abstract-Conference.html (accessed 2026-10-31)
[^s3]: Wang et al., "Self-Consistency Improves Chain of Thought Reasoning in Language Models", arXiv 2203.11171 (ICLR 2023). https://arxiv.org/abs/2203.11171v4 (accessed 2026-10-31)
[^s4]: Turpin et al., "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting", arXiv 2305.04388 (NeurIPS 2023). https://arxiv.org/abs/2305.04388v2 (accessed 2026-10-31)
[^s5]: Anthropic, "Prompting best practices", Claude Platform documentation. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-of-thought (accessed 2026-10-31)
