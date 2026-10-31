---
id: kt:rlhf
type: Technique
title: Reinforcement learning from human feedback
aliases: [RLHF, RL from human feedback, RL from human preferences, preference-based reinforcement learning]
domain: training-and-adaptation
summary: >-
  A training technique in which humans compare model outputs, a reward model is fitted to those preferences, and
  the model (policy) is then optimized with reinforcement learning to maximize the learned reward, usually under a
  penalty that keeps it close to its starting point.
maturity: established
broader: [kt:fine-tuning, kt:reinforcement-learning]
related: [kt:large-language-model, kt:red-teaming, kt:reward-hacking, kt:ai-alignment, kt:instruction-tuning]
relations:
  - {predicate: introducedIn, object: kt:deep-reinforcement-learning-from-human-preferences}
  - {predicate: dependsOn, object: kt:proximal-policy-optimization}
  - {predicate: alternativeTo, object: kt:direct-preference-optimization}
  - {predicate: implementedIn, object: kt:hugging-face-trl}
sources:
  - id: s1
    title: "Deep Reinforcement Learning from Human Preferences"
    publisher: NeurIPS 2017, Advances in Neural Information Processing Systems 30 (Christiano, Leike, Brown, Martic, Legg and Amodei)
    url: https://proceedings.neurips.cc/paper/2017/file/d5e2c0adad503c91f91df240d0cd4e49-Paper.pdf
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s2
    title: "Learning to summarize with human feedback"
    publisher: NeurIPS 2020, Advances in Neural Information Processing Systems 33 (Stiennon et al.)
    url: https://papers.nips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s3
    title: "Training language models to follow instructions with human feedback"
    publisher: Ouyang et al., arXiv 2203.02155 (published at NeurIPS 2022)
    url: https://arxiv.org/pdf/2203.02155v1
    type: primary
    accessed: 2026-10-31
  - id: s4
    title: "Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback"
    publisher: Casper et al., arXiv 2307.15217 (published in Transactions on Machine Learning Research, 2023)
    url: https://arxiv.org/pdf/2307.15217
    type: primary
    accessed: 2026-10-31
  - id: s5
    title: "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"
    publisher: NeurIPS 2023, Advances in Neural Information Processing Systems 36 (Rafailov, Sharma, Mitchell, Manning, Ermon and Finn)
    url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract.html
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s6
    title: "TRL - Transformer Reinforcement Learning"
    publisher: Hugging Face, TRL documentation (v0.12.0)
    url: https://huggingface.co/docs/trl/v0.12.0/en/index
    type: official-docs
    accessed: 2026-10-31
created: 2026-10-31
---

# Reinforcement learning from human feedback

**Reinforcement learning from human feedback (RLHF)** trains a model on what people prefer rather than on a hand-written reward function or a fixed set of target outputs. Humans compare candidate behaviours, a separate reward model learns to predict their judgements, and reinforcement learning then optimizes the model against that learned reward.[^s1][^s3] It became the standard final stage in turning a pretrained language model into an instruction-following assistant, and is also the most scrutinized one.[^s3][^s4]

## Origin

The modern recipe comes from Christiano, Leike, Brown, Martic, Legg and Amodei (OpenAI and DeepMind) at NeurIPS 2017. Humans watched pairs of short video clips of an agent and said which they preferred; a reward predictor was fitted to these choices and agents were trained on it with standard RL (A2C for Atari, TRPO for simulated robotics).[^s1] Feedback covered under 1% of the agent's interactions, roughly 30 minutes to 5 hours of human time per task, and was enough to approach true-reward performance on most MuJoCo tasks and to teach novel behaviours such as a Hopper backflip.[^s1] Results on Atari were mixed, and the authors found that fitting the reward model offline, rather than interleaving it with RL, could produce undesirable behaviour.[^s1]

The method moved to language with Stiennon et al. (NeurIPS 2020), who trained a reward model on human comparisons of summaries and used RL against it. On the Reddit TL;DR dataset their policies beat both the human reference summaries and much larger supervised models, and optimizing the learned reward gave summaries people preferred over those from optimizing ROUGE.[^s2] Ouyang et al. (InstructGPT, arXiv March 2022, NeurIPS 2022) then applied it to general instruction following with GPT-3.[^s3]

## How it works

The InstructGPT pipeline is the canonical three-stage form:[^s3]

1. **Supervised fine-tuning (SFT).** Fine-tune the pretrained model on labeller-written demonstrations (about 13k training prompts).
2. **Reward modelling.** Labellers rank 4 to 9 sampled responses per prompt (33k prompts); each ranking yields K-choose-2 pairwise comparisons. A reward model r(x, y) (6B parameters) is trained so that the preferred response scores higher, with a pairwise loss of the form −log σ(r(x, y_w) − r(x, y_l)). This is the Bradley–Terry preference model also used in the 2017 work.[^s1][^s3]
3. **RL fine-tuning.** Optimize the SFT policy with PPO on 31k unlabelled prompts to maximize r(x, y) minus β·KL(π ‖ π_SFT), a per-token KL penalty that limits over-optimization of the reward model. A variant, PPO-ptx, mixes in pretraining gradients to reduce the "alignment tax" (regressions on public NLP benchmarks).[^s3]

About 40 contractors produced the data. In human evaluations on the authors' prompt distribution, outputs of the 1.3B-parameter InstructGPT were preferred over those of the 175B GPT-3, though the model still made simple mistakes.[^s3]

## Limitations and open questions

Casper and 28 co-authors (TMLR 2023) organize RLHF's problems by stage and label each as tractable or fundamental.[^s4] On the **human feedback** side, evaluators can be biased, unrepresentative or flattered (sycophancy), and humans cannot reliably judge hard tasks or avoid being misled; they rate these oversight problems fundamental. On the **reward model** side, a single reward function cannot capture one person's values or a diverse society's, and reward models misgeneralize and can be hacked. On the **policy** side, RL can be adversarially exploitable and contribute to mode collapse.[^s4] Their remedy is to complement RLHF with other safety methods and to disclose details of how it was applied.[^s4]

The procedure is also costly and brittle in engineering terms. Rafailov et al. call it complex and often unstable, and show that the KL-constrained reward-maximization objective can be solved directly as a classification loss on preference pairs. This is **direct preference optimization (DPO)**, which needs no separate reward model and no sampling during training.[^s5]

## In practice

Open-source tooling exposes each stage. Hugging Face's TRL library describes itself as a full-stack toolkit spanning SFT, reward modelling and PPO, and as of its v0.12 documentation also ships trainers for DPO, KTO, RLOO, online DPO and other preference-optimization variants.[^s6] The growth of these alternatives shows the field treating the general idea (learn from human comparisons) as settled and the specific algorithm (reward model plus PPO) as one option among several.[^s5][^s6]

## Connections

RLHF is a form of **fine-tuning** that borrows its optimizer from **reinforcement learning**, most often **proximal policy optimization**.[^s1][^s3] It was introduced in *Deep Reinforcement Learning from Human Preferences* and is a standard post-training stage for **large language models**, typically after **instruction tuning** on demonstrations.[^s1][^s3] It is a central practical technique in **AI alignment**, and its failure modes include **reward hacking** of the learned reward model; **red teaming** probes behaviour that preference training missed.[^s4] **Direct preference optimization** is its main alternative, and **Hugging Face TRL** is a widely used implementation.[^s5][^s6]

## Sources

[^s1]: Christiano, Leike, Brown, Martic, Legg and Amodei, "Deep Reinforcement Learning from Human Preferences", NeurIPS 2017. https://proceedings.neurips.cc/paper/2017/file/d5e2c0adad503c91f91df240d0cd4e49-Paper.pdf (accessed 2026-10-31)
[^s2]: Stiennon et al., "Learning to summarize with human feedback", NeurIPS 2020. https://papers.nips.cc/paper/2020/hash/1f89885d556929e98d3ef9b86448f951-Abstract.html (accessed 2026-10-31)
[^s3]: Ouyang et al., "Training language models to follow instructions with human feedback", arXiv 2203.02155 (NeurIPS 2022). https://arxiv.org/pdf/2203.02155v1 (accessed 2026-10-31)
[^s4]: Casper et al., "Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback", arXiv 2307.15217 (TMLR 2023). https://arxiv.org/pdf/2307.15217 (accessed 2026-10-31)
[^s5]: Rafailov, Sharma, Mitchell, Manning, Ermon and Finn, "Direct Preference Optimization: Your Language Model is Secretly a Reward Model", NeurIPS 2023. https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract.html (accessed 2026-10-31)
[^s6]: Hugging Face, "TRL - Transformer Reinforcement Learning", TRL documentation v0.12.0. https://huggingface.co/docs/trl/v0.12.0/en/index (accessed 2026-10-31)
