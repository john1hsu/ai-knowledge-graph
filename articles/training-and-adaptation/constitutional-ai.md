---
id: kt:constitutional-ai
type: Technique
title: Constitutional AI
aliases: [CAI, constitutional AI training]
domain: training-and-adaptation
summary: >-
  An alignment training method, introduced by Anthropic in 2022, in which a short written list of natural-language
  principles (a "constitution") replaces human harmlessness labels: the model critiques and revises its own outputs
  against those principles, then is refined with reinforcement learning from AI-generated preference labels.
maturity: established
broader: [kt:ai-alignment, kt:fine-tuning]
related: [kt:red-teaming, kt:synthetic-data, kt:scalable-oversight, kt:self-refine-iterative-refinement-with-self-feedback]
relations:
  - {predicate: introducedIn, object: kt:constitutional-ai-harmlessness-from-ai-feedback}
  - {predicate: createdBy, object: kt:anthropic}
  - {predicate: extends, object: kt:rlhf}
  - {predicate: basedOn, object: kt:reinforcement-learning-from-ai-feedback}
  - {predicate: usedIn, object: kt:claude}
  - {predicate: dependsOn, object: kt:chain-of-thought}
sources:
  - id: s1
    title: "Constitutional AI: Harmlessness from AI Feedback"
    publisher: Bai et al. (Anthropic), arXiv 2212.08073, December 2022 (ar5iv HTML rendering)
    url: https://ar5iv.labs.arxiv.org/html/2212.08073
    type: primary
    accessed: 2026-11-13
  - id: s2
    title: "Claude's new constitution"
    publisher: Anthropic, 22 January 2026
    url: https://www.anthropic.com/research/claude-new-constitution
    type: lab-research
    accessed: 2026-11-13
  - id: s3
    title: "RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback"
    publisher: ICML 2024, PMLR 235:26874–26901 (Lee, Phatale, Mansoor, Mesnard, Ferret, Lu, Bishop, Hall, Carbune, Rastogi and Prakash)
    url: https://proceedings.mlr.press/v235/lee24t.html
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "Collective Constitutional AI: Aligning a Language Model with Public Input"
    publisher: Huang, Siddarth, Lovitt, Liao, Durmus, Tamkin and Ganguli, arXiv 2406.07814 (2024)
    url: https://arxiv.org/abs/2406.07814
    type: primary
    accessed: 2026-11-13
created: 2026-11-13
---

# Constitutional AI

Constitutional AI (CAI) is a method for training a language-model assistant to be harmless without collecting human labels that say which outputs are harmful. Human oversight is instead concentrated in a short list of natural-language principles, the "constitution", plus a handful of examples. The method was introduced by an Anthropic team led by Yuntao Bai and Jared Kaplan in the December 2022 paper *Constitutional AI: Harmlessness from AI Feedback*, which also popularised the term reinforcement learning from AI feedback (RLAIF).[^s1]

## How it works

CAI has two stages, both starting from a model that has already been trained to be helpful.[^s1]

1. **Supervised critique and revision (SL-CAI).** The helpful-only model answers red-team prompts designed to elicit harmful content. It is then asked to critique its own answer against a principle sampled at random from the constitution and to rewrite it; this can be repeated several times. The pretrained model is fine-tuned on the final revisions, mixed with ordinary helpfulness samples.[^s1]
2. **Reinforcement learning from AI feedback (RL-CAI).** The SL-CAI model produces pairs of responses, and a feedback model is asked, in multiple-choice form and guided by a sampled principle, which response is less harmful. Its normalised probabilities become soft preference labels. A preference model is trained on these AI labels together with human helpfulness labels, and the policy is then optimised against it with reinforcement learning, as in RLHF.[^s1]

The paper's constitution had 16 harmlessness principles, which the authors describe as chosen ad hoc for research; varying the number of principles did not noticeably change harmlessness, but sampling across them made the preference model more robust. The dataset mixed roughly 183,000 AI-labelled harmlessness comparisons with about 135,000 human helpfulness comparisons, and most reported results use 52-billion-parameter models.[^s1]

Asking the feedback model to reason step by step before choosing improved its judgments, but made its probabilities overconfident, so the authors clamped chain-of-thought labels to the 40–60% range.[^s1]

## Results and limitations

In crowdworker comparisons, RL-CAI models were judged markedly more harmless than RLHF models of similar helpfulness, and they rarely gave evasive refusals, typically explaining their objection instead. The authors partly attribute earlier evasiveness to labelling instructions that rewarded harmless-but-unhelpful answers.[^s1]

The paper lists several caveats: over-training produced Goodhart-style failures such as harsh or boilerplate reassurances; preference-model scores were poorly calibrated at the high end; self-critiques were sometimes wrong; helpfulness still depended on human labels; and the principles themselves lacked input from wider stakeholders. The authors also note that cheaper oversight could let developers ship systems with unforeseen failure modes, and the same technique could train a harmful model.[^s1]

Independent work supports the core RLAIF idea. Google researchers reported at ICML 2024 that RLAIF reached performance comparable to RLHF on summarisation and on helpful and harmless dialogue, that it beat a supervised baseline even when the AI labeller was the same size as the policy, and that a "direct" variant scoring outputs with an off-the-shelf LLM, without a separate reward model, did better still.[^s3]

## In practice

Who writes the constitution is an open question. In *Collective Constitutional AI* (2024), Anthropic researchers sourced principles from a sample of the public; the resulting model showed lower bias across nine social dimensions with equivalent language, maths and helpful-harmless performance, and tended to reframe contentious topics rather than refuse them.[^s4]

Anthropic has trained Claude models with CAI since 2023. On 22 January 2026 it published a rewritten constitution that, instead of a list of standalone rules, explains the reasoning behind desired behaviour, keeps a small set of hard constraints, and orders priorities as broadly safe, broadly ethical, compliant with Anthropic's guidelines, then helpful. Anthropic states that the document is used at several stages of training, including for the model to generate synthetic conversations and rank candidate responses, and released it under a CC0 public-domain dedication. These are the lab's own descriptions of its practice.[^s2]

## Connections

CAI extends **RLHF** by swapping human harmlessness labels for model-generated ones, and is built on **reinforcement learning from AI feedback**, a family of methods later studied independently of Anthropic.[^s1][^s3] It sits under **AI alignment** and **fine-tuning**, as a way to instil values through post-training.[^s1] Its training prompts come from **red teaming**, its revisions and labels are a form of **synthetic data**, and its critique-and-revise loop parallels **Self-Refine**.[^s1][^s2] Using AI to supervise AI is an early instance of **scalable oversight**, and the labelling step relies on **chain-of-thought** reasoning.[^s1] It was introduced in *Constitutional AI: Harmlessness from AI Feedback*, created by **Anthropic**, and is used in training **Claude**.[^s1][^s2]

## Sources
[^s1]: Bai et al., "Constitutional AI: Harmlessness from AI Feedback", Anthropic, arXiv 2212.08073, 2022. https://ar5iv.labs.arxiv.org/html/2212.08073 (accessed 2026-11-13)
[^s2]: Anthropic, "Claude's new constitution", 22 January 2026. https://www.anthropic.com/research/claude-new-constitution (accessed 2026-11-13)
[^s3]: Lee et al., "RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback", ICML 2024, PMLR 235. https://proceedings.mlr.press/v235/lee24t.html (accessed 2026-11-13)
[^s4]: Huang et al., "Collective Constitutional AI: Aligning a Language Model with Public Input", arXiv 2406.07814, 2024. https://arxiv.org/abs/2406.07814 (accessed 2026-11-13)
