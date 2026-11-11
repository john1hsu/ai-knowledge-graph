---
id: kt:program-induction-by-rationale-generation
type: Work
title: "Program Induction by Rationale Generation: Learning to Solve and Explain Algebraic Word Problems"
aliases: [Ling et al. 2017, AQuA paper, rationale generation for algebra word problems]
domain: prompting-and-reasoning
summary: >-
  The ACL 2017 paper by Wang Ling, Dani Yogatama, Chris Dyer and Phil Blunsom that released AQuA, a dataset of
  about 100,000 multiple-choice algebra word problems with step-by-step natural-language rationales, and trained a
  sequence-to-program model that uses those rationales to guide the search for the arithmetic program behind each answer.
maturity: historical
broader: [kt:mathematical-reasoning, kt:program-induction]
related: [kt:scratchpad, kt:chain-of-thought, kt:gsm8k, kt:long-short-term-memory]
relations:
  - {predicate: hasPart, object: kt:aqua-rat}
  - {predicate: extends, object: kt:sequence-to-sequence-learning}
  - {predicate: basedOn, object: kt:long-short-term-memory}
  - {predicate: followedBy, object: kt:chain-of-thought}
sources:
  - id: s1
    title: "Program Induction by Rationale Generation: Learning to Solve and Explain Algebraic Word Problems"
    publisher: Proceedings of ACL 2017 (Volume 1, Long Papers), pp. 158-167, DOI 10.18653/v1/P17-1015
    url: https://aclanthology.org/P17-1015/
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "Program Induction by Rationale Generation: Learning to Solve and Explain Algebraic Word Problems (arXiv 1705.04146)"
    publisher: arXiv (Ling, Yogatama, Dyer, Blunsom)
    url: https://arxiv.org/pdf/1705.04146
    type: primary
    accessed: 2026-11-11
  - id: s3
    title: "AQuA-RAT dataset card (aqua_rat)"
    publisher: Hugging Face Datasets
    url: https://huggingface.co/datasets/aqua_rat/blob/main/README.md
    type: official-docs
    accessed: 2026-11-11
  - id: s4
    title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    publisher: arXiv 2201.11903 (Wei et al.; NeurIPS 2022)
    url: https://arxiv.org/pdf/2201.11903
    type: primary
    accessed: 2026-11-11
created: 2026-11-11
---

# Program Induction by Rationale Generation

**"Program Induction by Rationale Generation: Learning to Solve and Explain Algebraic Word Problems"** is a 2017 paper by Wang Ling, Dani Yogatama, Chris Dyer and Phil Blunsom, published in the long-paper track of ACL 2017 in Vancouver.[^s1] It made two contributions: **AQuA** (often called AQuA-RAT), a dataset of algebra word problems paired with worked, step-by-step solutions called *rationales*; and a neural model that solves a problem by generating such a rationale while inducing the arithmetic program that produces it.[^s1][^s2] It is now best known as an early demonstration that natural-language intermediate steps can guide a model toward a correct answer, an idea later central to chain-of-thought prompting.[^s4]

## The problem and the idea

Solving an algebra word problem means carrying out a sequence of arithmetic operations, in effect a small program. Learning such programs directly from question–answer pairs is hard because the space of possible programs is enormous.[^s1] The authors proposed to supervise the model with rationales instead: text that mixes natural language with mathematical expressions and reaches the answer in small steps. A rationale is not a program, but its intermediate milestones constrain what the program can be.[^s2] They also argued that because the rationale is generated *before* the answer and causes it, it is a more faithful account of the computation than an explanation produced after the fact.[^s2]

## The AQuA dataset

The authors gathered 34,202 seed problems from multiple-choice exam material such as GMAT and GRE questions with solutions found online, then had crowd workers write new problems similar to a chosen seed, with different answers and rationales. Copying web problems was forbidden; the authors detected copies with nearest-neighbour checks and spot-checked workers manually. This added 70,318 questions.[^s2] After holding out 250 development and 250 test problems and removing near-duplicates of them, the training set contained 100,949 examples.[^s2] Each item has a question, five answer options (A–E), a rationale and the correct letter.[^s2][^s3] Rationales average about 106 tokens, longer than the questions at about 77.[^s2] The version distributed on Hugging Face lists 97,467 training, 254 validation and 254 test examples, under the Apache 2.0 licence, with the repository hosted in DeepMind's GitHub organization.[^s3]

## How the model works

The model reads the question and options and outputs a rationale followed by the chosen letter. Behind this output is a latent program: a sequence of instructions, each with an operation, its arguments, a result, and a destination that is either the output text or a memory buffer.[^s2] There are 22 operations, including basic arithmetic, powers, roots, logs, trigonometric functions, factorial and combinations, type conversions, and a `Check` operation that matches a computed value to an answer option. A predictor chooses whether each argument is a newly generated word, a pointer into the question, or a pointer into earlier output or memory.[^s2] The networks are two-layer LSTMs with 200-dimensional hidden states.[^s2]

Since the program is never observed, training marginalizes over programs that could produce the rationale. Random sampling almost never finds a valid one, so at each step the search keeps only instructions that can emit the next rationale token, allowing at most one intermediate memory value. The authors report that without the rationale the search is too unconstrained to learn.[^s2]

## Results and limitations

On the test set the model reached 36.4% accuracy, against 20.8% for an attention-based sequence-to-sequence baseline and a 20% chance rate for five options. It also produced better rationales by automatic metrics: BLEU 27.2 versus 8.57 and perplexity 28.5 versus 524.7.[^s2] The paper describes this as roughly doubling the baseline, though the reported figures amount to about 1.75 times.[^s2] The authors note that most correctly solved problems need only one or two operations, that multi-step problems remain hard, and that long rationales, often over 200 tokens, strain attention and copy mechanisms. Rationale quality was judged only with automatic metrics, with no human evaluation.[^s2]

## Connections

The paper **extends sequence-to-sequence learning** with copy mechanisms and a latent program, and is **based on long short-term memory** networks.[^s2] **AQuA** is **part of** the work and became a standard benchmark for **mathematical reasoning**, alongside the later **GSM8K**.[^s3][^s4] Like the later **scratchpad** approach, it trains a model to write intermediate steps before answering, and it was **followed by chain-of-thought prompting**: Wei et al. credit Ling et al. with pioneering natural-language rationales for math word problems, and evaluated on AQuA using four training-set exemplars, where PaLM 540B rose from 25.2% with standard prompting to 35.8% with chain-of-thought prompting (as reported in 2022).[^s4] Where Ling et al. needed about 100,000 annotated rationales to train a dedicated model, chain-of-thought showed that a few written examples could elicit similar reasoning from a large pretrained model.[^s2][^s4] The model is also an instance of **program induction**: the program is the target, and the rationale is the supervision that makes it learnable.[^s1]

## Sources
[^s1]: Ling, Yogatama, Dyer and Blunsom, "Program Induction by Rationale Generation: Learning to Solve and Explain Algebraic Word Problems", ACL 2017, pp. 158-167. https://aclanthology.org/P17-1015/ (accessed 2026-11-11)
[^s2]: Ling, Yogatama, Dyer and Blunsom, arXiv 1705.04146 (full paper). https://arxiv.org/pdf/1705.04146 (accessed 2026-11-11)
[^s3]: "aqua_rat" dataset card, Hugging Face Datasets. https://huggingface.co/datasets/aqua_rat/blob/main/README.md (accessed 2026-11-11)
[^s4]: Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", arXiv 2201.11903 (NeurIPS 2022). https://arxiv.org/pdf/2201.11903 (accessed 2026-11-11)
