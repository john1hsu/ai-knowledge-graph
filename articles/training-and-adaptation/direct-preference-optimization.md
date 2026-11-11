---
id: kt:direct-preference-optimization
type: Algorithm
title: "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"
aliases: [DPO, direct preference optimisation]
domain: training-and-adaptation
summary: >-
  A preference-alignment algorithm that fine-tunes a language model directly on pairs of preferred and rejected
  responses with a simple classification-style loss, solving the KL-constrained objective of RLHF without fitting a
  separate reward model or running reinforcement learning.
maturity: established
broader: [kt:fine-tuning]
related: [kt:ai-alignment, kt:large-language-model, kt:reward-hacking, kt:synthetic-data]
relations:
  - {predicate: alternativeTo, object: kt:rlhf}
  - {predicate: contrastsWith, object: kt:proximal-policy-optimization}
  - {predicate: dependsOn, object: kt:bradley-terry-model}
  - {predicate: implementedIn, object: kt:hugging-face-trl}
sources:
  - id: s1
    title: "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"
    publisher: NeurIPS 2023, Advances in Neural Information Processing Systems 36, pp. 53728–53741 (Rafailov, Sharma, Mitchell, Manning, Ermon and Finn)
    url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "Direct Preference Optimization: Your Language Model is Secretly a Reward Model (arXiv v2, HTML)"
    publisher: Rafailov et al., arXiv 2305.18290
    url: https://arxiv.org/html/2305.18290v2
    type: primary
    accessed: 2026-11-11
  - id: s3
    title: "A General Theoretical Paradigm to Understand Learning from Human Preferences"
    publisher: AISTATS 2024, PMLR 238:4447–4455 (Gheshlaghi Azar, Guo, Piot, Munos, Rowland, Valko and Calandriello)
    url: https://proceedings.mlr.press/v238/gheshlaghi-azar24a.html
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study"
    publisher: Xu et al., arXiv 2404.10719 (ICML 2024)
    url: https://arxiv.org/html/2404.10719v3
    type: primary
    accessed: 2026-11-11
  - id: s5
    title: "DPO Trainer"
    publisher: Hugging Face TRL documentation
    url: https://huggingface.co/docs/trl/en/dpo_trainer
    type: official-docs
    accessed: 2026-11-11
  - id: s6
    title: "Zephyr: Direct Distillation of LM Alignment"
    publisher: Tunstall et al., arXiv 2310.16944
    url: https://arxiv.org/abs/2310.16944
    type: primary
    accessed: 2026-11-11
created: 2026-11-11
---

# Direct Preference Optimization (DPO)

Direct Preference Optimization is a method for aligning a language model with human (or AI) preference judgments by training it directly on comparison data: for each prompt, one response labelled better and one labelled worse. It was introduced by Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher Manning, Stefano Ermon and Chelsea Finn in a NeurIPS 2023 paper, which framed it as a simpler, more stable replacement for the reward-model-plus-reinforcement-learning pipeline of RLHF.[^s1] The authors argue that the same KL-constrained objective RLHF optimizes can be solved exactly in a single supervised-style training stage that amounts to classification on preference pairs, with no sampling from the model during fine-tuning and little hyperparameter tuning.[^s1]

## How it works

RLHF maximizes a learned reward r(x, y) while penalizing, with weight β, the KL divergence between the trained policy π_θ and a frozen reference policy π_ref. The DPO paper notes that this objective has a closed-form optimum, π*(y|x) ∝ π_ref(y|x)·exp(r(x, y)/β). Rearranging gives the reward in terms of the policy: r(x, y) = β log[π(y|x)/π_ref(y|x)] + β log Z(x), where Z(x) is a partition function that is intractable to compute.[^s2] Under the Bradley–Terry model, the probability that one response beats another depends only on the difference of their rewards for the same prompt, so the β log Z(x) term cancels. The policy itself therefore defines an implicit reward model, which is the sense of the paper's subtitle.[^s2]

Substituting into the Bradley–Terry likelihood yields the DPO loss: the negative log-sigmoid of β times the gap between the chosen response's log-ratio log π_θ(y⁺|x)/π_ref(y⁺|x) and the rejected response's log-ratio.[^s2][^s5] Its gradient pushes up the likelihood of the preferred answer and down that of the rejected one, weighting each pair by how badly the implicit reward currently misorders it; the authors report that dropping this weighting can make the model degenerate.[^s2] In the paper's pipeline, a model is first supervised-fine-tuned, that SFT model serves as π_ref and as the initialization, and if no SFT model exists the reference can be fitted by maximum likelihood on the preferred completions.[^s2]

## Evidence and limitations

The original experiments covered sentiment control, summarization and single-turn dialogue with models up to about 6B parameters, using GPT-4-judged win rates for the latter two. The authors report that DPO controlled sentiment better than PPO-based RLHF and matched or improved response quality on summarization and dialogue.[^s1][^s2]

Later work qualified these results. Gheshlaghi Azar and colleagues showed that RLHF and DPO are special cases of a general preference objective (ΨPO) and argued that DPO still relies on approximating pairwise preferences with pointwise rewards; choosing an identity mapping in their framework gave an efficient alternative with performance guarantees.[^s3] Xu et al. (ICML 2024) found that DPO can favour responses outside the reference model's distribution, is sensitive to mismatch between the model's own outputs and the preference data, and failed to improve over SFT on competitive code generation, while a carefully tuned PPO beat it in all their tests. They report that extra SFT on preferred data and iterative DPO with freshly sampled, reward-labelled pairs narrow but do not close the gap.[^s4]

## In practice

DPO is widely implemented in open-source tooling. As of November 2026, Hugging Face's TRL `DPOTrainer` expects prompt/chosen/rejected records, uses β = 0.1 by default (higher values keep the model closer to the reference), defaults the reference to the initial policy, and offers many loss variants, including IPO, hinge, robust-DPO and length-normalized forms.[^s5] An early high-profile use was Zephyr-7B (October 2023), which applied a "distilled" DPO to preference rankings produced by a teacher model instead of humans; its authors report it surpassed Llama2-Chat-70B on MT-Bench after only a few hours of training.[^s6]

## Connections

DPO is a form of **fine-tuning** (broader) and an **alternative to RLHF**: it targets the same KL-regularized objective but removes the separate reward model and the reinforcement-learning loop.[^s1] It **contrasts with proximal policy optimization**, the on-policy RL algorithm that comparative studies still find stronger when tuned carefully.[^s4] It **depends on the Bradley–Terry model** of pairwise preferences, the assumption Azar et al. critique.[^s2][^s3] It is **implemented in Hugging Face TRL**.[^s5] It relates to **AI alignment** and **large language models** as a standard post-training step, to **synthetic data** because preference pairs are often generated and ranked by other models, as in Zephyr,[^s6] and to **reward hacking**, since an implicit reward can still be over-optimized away from what annotators intended.[^s3][^s4]

## Sources
[^s1]: Rafailov et al., "Direct Preference Optimization: Your Language Model is Secretly a Reward Model", NeurIPS 2023. https://proceedings.neurips.cc/paper_files/paper/2023/hash/a85b405ed65c6477a4fe8302b5e06ce7-Abstract.html (accessed 2026-11-11)
[^s2]: Rafailov et al., arXiv 2305.18290v2 (HTML full text). https://arxiv.org/html/2305.18290v2 (accessed 2026-11-11)
[^s3]: Gheshlaghi Azar et al., "A General Theoretical Paradigm to Understand Learning from Human Preferences", AISTATS 2024, PMLR 238. https://proceedings.mlr.press/v238/gheshlaghi-azar24a.html (accessed 2026-11-11)
[^s4]: Xu et al., "Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study", ICML 2024, arXiv 2404.10719. https://arxiv.org/html/2404.10719v3 (accessed 2026-11-11)
[^s5]: Hugging Face, "DPO Trainer", TRL documentation. https://huggingface.co/docs/trl/en/dpo_trainer (accessed 2026-11-11)
[^s6]: Tunstall et al., "Zephyr: Direct Distillation of LM Alignment", arXiv 2310.16944. https://arxiv.org/abs/2310.16944 (accessed 2026-11-11)
