---
id: kt:mechanistic-interpretability
type: Field
title: Mechanistic interpretability
aliases: [mech interp, mechanistic interpretability research, circuits research]
domain: safety-alignment-and-security
summary: >-
  A research field that tries to reverse-engineer trained neural networks, identifying the features they represent
  and the circuits that compute with them, to give a causal, human-understandable account of model behaviour.
maturity: emerging
broader: [kt:interpretability]
related: [kt:large-language-model, kt:artificial-neural-network, kt:in-context-learning, kt:hallucination, kt:chain-of-thought]
relations:
  - {predicate: enables, object: kt:ai-alignment}
  - {predicate: basedOn, object: kt:sparse-autoencoder}
  - {predicate: hasPart, object: kt:induction-head}
sources:
  - id: s1
    title: "Zoom In: An Introduction to Circuits"
    publisher: Distill, 2020 (Olah, Cammarata, Schubert, Goh, Petrov, Carter); doi:10.23915/distill.00024.001
    url: https://mlanthology.org/distill/2020/olah2020distill-zoom
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s2
    title: "Mechanistic Interpretability for AI Safety — A Review"
    publisher: Transactions on Machine Learning Research, 2024 (Bereska, Gavves)
    url: https://mlanthology.org/tmlr/2024/bereska2024tmlr-mechanistic
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s3
    title: "In-context Learning and Induction Heads"
    publisher: arXiv:2209.11895 (Olsson, Elhage, Nanda et al., Anthropic), 2022
    url: https://arxiv.org/abs/2209.11895
    type: primary
    accessed: 2026-11-08
  - id: s4
    title: "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning"
    publisher: Anthropic, Transformer Circuits Thread, 4 October 2023 (Bricken, Templeton, Batson et al.)
    url: https://transformer-circuits.pub/2023/monosemantic-features/
    type: lab-research
    accessed: 2026-11-08
  - id: s5
    title: "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet"
    publisher: Anthropic, Transformer Circuits Thread, 21 May 2024
    url: https://transformer-circuits.pub/2024/scaling-monosemanticity/
    type: lab-research
    accessed: 2026-11-08
  - id: s6
    title: "On the Biology of a Large Language Model"
    publisher: Anthropic, Transformer Circuits Thread, 27 March 2025
    url: https://transformer-circuits.pub/2025/attribution-graphs/biology.html
    type: lab-research
    accessed: 2026-11-08
created: 2026-11-08
---

# Mechanistic interpretability

Mechanistic interpretability is the effort to reverse-engineer what a trained neural network actually computes: which internal representations ("features") it learns, and how those features are wired together into algorithms that produce its outputs. A 2024 TMLR review by Bereska and Gavves frames the goal as a granular, causal account of model behaviour, as opposed to correlational explanations of which inputs mattered.[^s2] The field matters to AI safety because it promises a way to check what a model is doing internally rather than relying only on its observed outputs.[^s2]

## Origin

The modern research programme is usually traced to the circuits work led by Chris Olah. In "Zoom In: An Introduction to Circuits" (Distill, 2020), Olah and colleagues studied vision models and set out three working claims: networks contain meaningful features; those features are connected into interpretable circuits; and similar features and circuits recur across different models ("universality").[^s1] The agenda then moved to transformers. Olsson et al. (2022) described *induction heads*, attention heads that implement a simple copying rule: if token A was earlier followed by B, predict B when A reappears.[^s3] They found these heads form at the same point in training as a sudden jump in in-context learning, and argued they may underlie much of it, while calling the evidence preliminary: causal for small attention-only models but only correlational for larger ones.[^s3]

## How it works

A central obstacle is *polysemanticity*: individual neurons often respond to mixtures of unrelated inputs. The leading explanation is *superposition*, the hypothesis that a network represents more features than it has neurons by encoding each feature as a direction spread across many neurons.[^s4] Anthropic's "Towards Monosemanticity" (October 2023) attacked this with dictionary learning: a sparse autoencoder trained on the 512-neuron MLP layer of a one-layer transformer, with dictionaries of up to 131,072 features, trained with a reconstruction loss plus an L1 sparsity penalty.[^s4] Many resulting features were more interpretable than neurons (for example, features for Arabic script, DNA sequences or base64), and artificially activating them steered generation, which is evidence of a causal role.[^s4]

The method was scaled in May 2024 to a production model, Claude 3 Sonnet, with sparse autoencoders of roughly 1M, 4M and 34M features on a middle-layer residual stream.[^s5] Features found there ranged from concrete entities (a Golden Gate Bridge feature) to safety-relevant concepts such as unsafe code, sycophantic praise and deception; clamping a feature to a high value changed behaviour in matching ways.[^s5] In March 2025 Anthropic introduced *attribution graphs*, which replace a model's MLPs with a cross-layer transcoder of about 30 million features and trace how features interact on a given prompt in Claude 3.5 Haiku.[^s6] Case studies showed the model apparently inferring an intermediate fact during two-step questions and choosing a rhyme word before writing a line of verse.[^s6]

## Limitations and open questions

Practitioners are explicit about the gaps. Sparse-autoencoder features are not perfectly monosemantic, and weak activations are harder to interpret.[^s4][^s5] Dictionaries capture only part of what a model knows: in the 34M-feature run many features never activated, and rarer concepts needed larger dictionaries.[^s5] Attribution graphs gave satisfying explanations for only about a quarter of the prompts the authors tried, miss mechanisms located in attention, and approximate the real model through a replacement model.[^s6] The 2024 review lists scaling, automation and comprehensive interpretation as the main open challenges, and notes dual-use risks such as interpretability insights accelerating capabilities.[^s2] Finding a "deception" feature also does not by itself show that a model is deceptive; the Scaling Monosemanticity authors caution against over-reading such features.[^s5]

## Connections

Mechanistic interpretability is a sub-area of the broader study of **interpretability**, distinguished by its demand for causal, circuit-level explanations.[^s2] It is pursued largely as a tool for **AI alignment**, since inspecting internal mechanisms could help verify and control model behaviour.[^s2] Its main current workhorse is the **sparse autoencoder**, and one of its best-known findings is the **induction head**, linked to **in-context learning** in transformers.[^s3][^s4] Most recent work targets **large language models** and has begun to shed light on **hallucination** and on whether **chain-of-thought** text reflects a model's actual computation.[^s6] Its intellectual roots lie in feature visualisation of **artificial neural networks** for vision.[^s1]

## Sources

[^s1]: Olah et al., "Zoom In: An Introduction to Circuits", Distill, 2020. https://mlanthology.org/distill/2020/olah2020distill-zoom (accessed 2026-11-08)
[^s2]: Bereska and Gavves, "Mechanistic Interpretability for AI Safety — A Review", TMLR, 2024. https://mlanthology.org/tmlr/2024/bereska2024tmlr-mechanistic (accessed 2026-11-08)
[^s3]: Olsson et al., "In-context Learning and Induction Heads", arXiv:2209.11895, 2022. https://arxiv.org/abs/2209.11895 (accessed 2026-11-08)
[^s4]: Bricken et al., "Towards Monosemanticity: Decomposing Language Models With Dictionary Learning", Anthropic, 2023. https://transformer-circuits.pub/2023/monosemantic-features/ (accessed 2026-11-08)
[^s5]: Anthropic interpretability team, "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet", Anthropic, 2024. https://transformer-circuits.pub/2024/scaling-monosemanticity/ (accessed 2026-11-08)
[^s6]: Anthropic interpretability team, "On the Biology of a Large Language Model", Anthropic, 2025. https://transformer-circuits.pub/2025/attribution-graphs/biology.html (accessed 2026-11-08)
