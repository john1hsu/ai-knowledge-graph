---
id: kt:instruction-tuning
type: Technique
title: Instruction tuning
aliases: [instruction fine-tuning, instruction finetuning, supervised instruction tuning, multitask prompted training]
domain: training-and-adaptation
summary: >-
  A fine-tuning technique that trains a pretrained language model on many tasks phrased as natural-language
  instructions paired with target responses, so that it follows instructions and generalizes zero-shot to tasks it
  was never trained on.
maturity: established
broader: [kt:fine-tuning, kt:post-training]
related: [kt:rlhf, kt:synthetic-data, kt:large-language-model, kt:in-context-learning, kt:chain-of-thought, kt:zero-shot-learning]
relations:
  - {predicate: introducedIn, object: kt:finetuned-language-models-are-zero-shot-learners}
  - {predicate: dependsOn, object: kt:pretraining}
  - {predicate: followedBy, object: kt:rlhf}
  - {predicate: implementedIn, object: kt:hugging-face-trl}
  - {predicate: alternativeTo, object: kt:few-shot-prompting}
sources:
  - id: s1
    title: "Finetuned Language Models Are Zero-Shot Learners"
    publisher: ICLR 2022; arXiv 2109.01652v5, Google Research (Wei, Bosma, Zhao, Guu, Yu, Lester, Du, Dai and Le)
    url: https://arxiv.org/pdf/2109.01652
    type: primary
    accessed: 2026-11-12
  - id: s2
    title: "Multitask Prompted Training Enables Zero-Shot Task Generalization"
    publisher: ICLR 2022; arXiv 2110.08207, BigScience (Sanh, Webson, Raffel, Bach et al.)
    url: https://arxiv.org/pdf/2110.08207
    type: primary
    accessed: 2026-11-12
  - id: s3
    title: "Scaling Instruction-Finetuned Language Models"
    publisher: Journal of Machine Learning Research 25(70):1–53, 2024 (Chung, Hou, Longpre, Zoph et al.)
    url: https://www.jmlr.org/papers/v25/23-0870.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "LIMA: Less Is More for Alignment"
    publisher: NeurIPS 2023, Advances in Neural Information Processing Systems 36 (Zhou et al.)
    url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/ac662d74829e4407ce1d126477f4a03a-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s5
    title: "The False Promise of Imitating Proprietary LLMs"
    publisher: arXiv 2305.15717 (Gudibande, Wallace, Snell, Geng, Liu, Abbeel, Levine and Song), UC Berkeley
    url: https://arxiv.org/abs/2305.15717
    type: preprint
    accessed: 2026-11-12
  - id: s6
    title: "SFT Trainer"
    publisher: Hugging Face TRL documentation
    url: https://huggingface.co/docs/trl/sft_trainer
    type: official-docs
    accessed: 2026-11-12
created: 2026-11-12
---

# Instruction tuning

**Instruction tuning** is supervised fine-tuning of a pretrained language model on a large mixture of tasks, each
written as a natural-language instruction with a target answer. The goal is not to master the training tasks
themselves but to teach the model to respond to instructions in general, so that it handles new, unseen tasks
zero-shot.[^s1] The term was introduced by Wei et al. at Google Research (arXiv 2021, ICLR 2022), whose model FLAN
was the instruction-tuned version of a 137-billion-parameter decoder-only model, LaMDA-PT.[^s1] A concurrent
BigScience paper by Sanh et al. (ICLR 2022) called the same idea *multitask prompted training* and released the
T0 models.[^s2]

## How it works

Existing labelled datasets are rewritten into instruction form with templates. FLAN drew on 62 text datasets
grouped into twelve task clusters (inference, translation, sentiment and so on), with ten hand-written templates per
dataset plus up to three that reverse the task, such as writing a review of a given sentiment rather than
classifying one.[^s1] To measure generalization honestly, whole clusters are held out: when evaluating on natural
language inference, for instance, no inference dataset appears in training.[^s1] T0 used the same recipe with an
11-billion-parameter T5 encoder-decoder and prompts from the crowdsourced Public Pool of Prompts (P3), which then
held 2,073 prompts for 177 datasets; four task types, spanning 11 datasets, were never seen in training.[^s2]

Training itself is ordinary next-token cross-entropy on the target response. In practice libraries such as Hugging
Face TRL's `SFTTrainer` accept prompt–completion pairs or multi-turn `messages` conversations, apply the model's
chat template automatically, and by default compute the loss only on the completion for prompt–completion data;
an option restricts the loss to assistant turns in conversations.[^s6] A minimal example pairs the input
"Translate to French: The sky is blue." with the target "Le ciel est bleu.", and the gradient flows only through
the target tokens.[^s6]

## Evidence

FLAN beat zero-shot GPT-3 (175B) on 20 of 25 evaluated datasets, and even few-shot GPT-3 on 10, by Wei et al.'s
own report.[^s1] T0 matched or exceeded GPT-3 on 9 of 11 held-out datasets while being about 16 times smaller.[^s2]
Ablations in these papers established the main design rules. Held-out accuracy rose as more task clusters were
added; replacing instructions with bare dataset names, or no template at all, did substantially worse; and more
prompts per dataset raised median accuracy while reducing sensitivity to prompt wording.[^s1][^s2]

Chung et al. (JMLR 2024) scaled the recipe to 1.8K tasks across PaLM, T5 and U-PaLM models and added
chain-of-thought exemplars to the mix. Flan-PaLM 540B improved on PaLM 540B by 9.4% on average and scored 75.2% on
five-shot MMLU, state of the art when the work was released in 2022; the released Flan-T5 checkpoints performed
strongly against much larger models such as PaLM 62B.[^s3]

## Limitations and open questions

- **Scale dependence.** In FLAN's experiments instruction tuning helped the 68B and 137B models on unseen tasks
  but hurt held-out performance for models of 8B parameters or fewer.[^s1] Later work with more tasks reported
  gains at smaller scales too, so the threshold depends on the data mix.[^s3]
- **What the data teaches.** LIMA (NeurIPS 2023) fine-tuned a 65B LLaMa on only 1,000 curated prompt–response
  pairs, without reinforcement learning, and its answers were rated equal to or better than GPT-4's in 43% of
  cases.[^s4] The authors read this as evidence that knowledge comes almost entirely from pretraining, with
  instruction data mainly teaching format and style.[^s4]
- **Imitation is shallow.** Gudibande et al. (2023 preprint) fine-tuned 1.5B–13B models on ChatGPT outputs; crowd
  raters judged them competitive, yet targeted benchmarks showed they closed little of the capability gap.[^s5]
  They concluded that imitation copies style rather than factuality, and that stronger base models matter more.[^s5]
- **Open issues** include how to choose and weight task mixtures, contamination between instruction data and
  evaluation sets, and how much behaviour should be set by supervised data versus preference training.[^s3][^s4]

## In practice

Instruction tuning, often simply called supervised fine-tuning (SFT), is the usual first post-training stage that
turns a raw pretrained model into an assistant; preference optimization typically follows.[^s4][^s6] Instruction
data now ranges from templated academic datasets to small human-written sets and large model-generated
collections.[^s3][^s4][^s5] Open tooling such as TRL supports it directly, including packing several short examples
into one sequence for efficiency.[^s6]

## Connections

Instruction tuning is a specialization of **fine-tuning** and a core stage of **post-training**; it **depends on**
**pretraining**, since LIMA and the imitation study both locate the model's capability in the base model.[^s4][^s5]
It was **introduced in** *Finetuned Language Models Are Zero-Shot Learners*.[^s1] It is typically **followed by**
**RLHF** or related preference methods, and it draws heavily on **synthetic data**.[^s4][^s5] Its aim, strong
**zero-shot learning**, makes it an **alternative to** **few-shot prompting**: both FLAN and T0 were benchmarked
against few-shot GPT-3, the canonical case of **in-context learning**.[^s1][^s2] Adding **chain-of-thought**
exemplars to the mixture improved reasoning in Flan-PaLM.[^s3] It is **implemented in** **Hugging Face TRL**.[^s6]

## Sources

[^s1]: Wei et al., "Finetuned Language Models Are Zero-Shot Learners", ICLR 2022, arXiv 2109.01652. https://arxiv.org/pdf/2109.01652 (accessed 2026-11-12)
[^s2]: Sanh et al., "Multitask Prompted Training Enables Zero-Shot Task Generalization", ICLR 2022, arXiv 2110.08207. https://arxiv.org/pdf/2110.08207 (accessed 2026-11-12)
[^s3]: Chung et al., "Scaling Instruction-Finetuned Language Models", JMLR 25(70), 2024. https://www.jmlr.org/papers/v25/23-0870.html (accessed 2026-11-12)
[^s4]: Zhou et al., "LIMA: Less Is More for Alignment", NeurIPS 2023. https://proceedings.neurips.cc/paper_files/paper/2023/hash/ac662d74829e4407ce1d126477f4a03a-Abstract.html (accessed 2026-11-12)
[^s5]: Gudibande et al., "The False Promise of Imitating Proprietary LLMs", arXiv 2305.15717, 2023. https://arxiv.org/abs/2305.15717 (accessed 2026-11-12)
[^s6]: Hugging Face, "SFT Trainer", TRL documentation. https://huggingface.co/docs/trl/sft_trainer (accessed 2026-11-12)
