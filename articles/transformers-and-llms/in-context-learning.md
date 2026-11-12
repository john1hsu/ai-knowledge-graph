---
id: kt:in-context-learning
type: Concept
title: In-context learning
aliases: [ICL, in-context learner, learning from demonstrations in the prompt]
domain: transformers-and-llms
summary: >-
  The ability of a pretrained language model to perform a new task from instructions or a handful of
  input-output demonstrations placed in its prompt, at inference time and without any update to its weights.
maturity: established
broader: [kt:large-language-model]
related: [kt:few-shot-prompting, kt:prompt-sensitivity, kt:context-window, kt:emergent-abilities, kt:induction-head, kt:mechanistic-interpretability]
relations:
  - {predicate: introducedIn, object: kt:language-models-are-few-shot-learners}
  - {predicate: dependsOn, object: kt:pretraining}
  - {predicate: contrastsWith, object: kt:fine-tuning}
  - {predicate: enables, object: kt:chain-of-thought}
sources:
  - id: s1
    title: "Language Models are Few-Shot Learners"
    publisher: NeurIPS 2020 (Brown, Mann, Ryder, Subbiah, Kaplan, Dhariwal, et al.)
    url: https://papers.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"
    publisher: EMNLP 2022, pp. 11048-11064 (Min, Lyu, Holtzman, Artetxe, Lewis, Hajishirzi, Zettlemoyer)
    url: https://aclanthology.org/2022.emnlp-main.759
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s3
    title: "In-context Learning and Induction Heads"
    publisher: Anthropic, Transformer Circuits Thread, March 2022 (Olsson, Elhage, Nanda, Olah, et al.)
    url: https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html
    type: lab-research
    accessed: 2026-11-12
  - id: s4
    title: "An Explanation of In-context Learning as Implicit Bayesian Inference"
    publisher: arXiv 2111.02080 (Xie, Raghunathan, Liang, Ma; ICLR 2022)
    url: https://arxiv.org/pdf/2111.02080
    type: primary
    accessed: 2026-11-12
  - id: s5
    title: "Transformers Learn In-Context by Gradient Descent"
    publisher: ICML 2023, pp. 35151-35174 (von Oswald, Niklasson, Randazzo, Sacramento, Mordvintsev, Zhmoginov, Vladymyrov), via Google Research
    url: https://research.google/pubs/transformers-learn-in-context-by-gradient-descent/
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s6
    title: "Calibrate Before Use: Improving Few-shot Performance of Language Models"
    publisher: ICML 2021, PMLR vol. 139, pp. 12697-12706 (Zhao, Wallace, Feng, Klein, Singh)
    url: https://proceedings.mlr.press/v139/zhao21c.html
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# In-context learning

In-context learning (ICL) is the capacity of a pretrained language model to pick up a task from text supplied in its prompt — a natural-language instruction, a few worked input-output pairs, or both — and then apply it to a new input, all within a single forward pass and with the model's parameters left unchanged. The idea was popularised by the GPT-3 paper, which evaluated a 175-billion-parameter autoregressive model on many NLP benchmarks with no gradient updates or fine-tuning, specifying both the task and its demonstrations purely through text.[^s1] What makes ICL notable is that nothing in the training objective asks for it: the model is trained only to predict the next token, yet at sufficient scale it behaves as though it can learn from examples on the fly.

## How it works

A typical ICL prompt is a sequence such as `review: great film -> positive`, `review: dull plot -> negative`, followed by `review: superb acting ->`, and the model completes it with a label. The GPT-3 authors distinguished zero-shot (instruction only), one-shot and few-shot settings, and reported that scaling the model markedly improved task-agnostic few-shot performance, in some cases making it competitive with earlier fine-tuned state-of-the-art systems; they also flagged datasets where few-shot learning still struggled.[^s1]

Several explanations of the mechanism have been proposed, and they are complementary rather than settled:

- **Implicit Bayesian inference.** Xie et al. argue that coherent pretraining documents force a model to infer a latent document-level concept; a prompt of examples sharing one concept lets the model infer it and predict accordingly, which they reproduce on a synthetic dataset built from a mixture of hidden Markov models.[^s4]
- **Induction heads.** Anthropic researchers identified attention-head circuits that find an earlier occurrence of the current token and copy what followed it. In small models these heads form during a sudden phase change early in training, at the same time as in-context ability jumps, and ablating them sharply reduces ICL; the evidence for large models is mainly correlational.[^s3]
- **Learning by gradient descent in the forward pass.** Von Oswald et al. constructed a single linear self-attention layer whose output matches one step of gradient descent on a regression loss, and found that trained self-attention-only transformers on simple regression tasks often converge toward such solutions.[^s5]

## What the demonstrations actually do

Empirical work shows ICL is not simply learning an input-label mapping. Min et al. found that replacing gold labels in demonstrations with random ones barely hurt accuracy on classification and multiple-choice tasks across 12 models including GPT-3; what mattered more was exposure to the label space, the distribution of input text, and the overall format.[^s2] This supports a view of ICL as partly task *recognition* — locating a behaviour acquired in pretraining — rather than wholly new learning.[^s2][^s4]

## Limitations

ICL is fragile. Zhao et al. showed GPT-3's few-shot accuracy could range from near chance to near state-of-the-art depending on prompt format, which examples were chosen and their order, and traced part of this to biases toward labels that are frequent or appear late in the prompt; their contextual-calibration fix raised accuracy by up to 30 percentage points.[^s6] Xie et al. likewise report 10–40% accuracy swings from reordering the same examples in their synthetic setting.[^s4] Mechanistic accounts are still incomplete: the gradient-descent construction is demonstrated only on simple regression,[^s5] and the induction-head authors caution against extrapolating from small to very large models.[^s3]

## In practice

ICL underlies everyday prompting: because tasks and demonstrations are supplied purely as text with no gradient updates, few-shot examples and output-format templates can steer a single deployed model across many tasks without retraining.[^s1] Its sensitivity means practitioners should vary example selection and ordering, and evaluate on held-out inputs, before trusting a prompt.[^s6]

## Connections

ICL is a capability of **large language models** that arises from **pretraining** and was introduced as a named evaluation setting in **the GPT-3 paper**.[^s1] It contrasts with **fine-tuning**, which changes weights, whereas ICL changes only the input.[^s1] **Few-shot prompting** is the practical technique that exploits it, and **prompt sensitivity** describes its main failure mode.[^s6] Because demonstrations must fit in the prompt, the **context window** limits how many can be supplied. Its scale-dependent appearance links it to debates over **emergent abilities**, while **mechanistic interpretability** studies its circuitry through the **induction head**.[^s3] **Chain-of-thought** prompting builds on ICL by placing worked reasoning, not just answers, in the demonstrations.

## Sources

[^s1]: Brown et al., "Language Models are Few-Shot Learners", NeurIPS 2020. https://papers.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html (accessed 2026-11-12)
[^s2]: Min et al., "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?", EMNLP 2022. https://aclanthology.org/2022.emnlp-main.759 (accessed 2026-11-12)
[^s3]: Olsson et al., "In-context Learning and Induction Heads", Anthropic Transformer Circuits Thread, 2022. https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html (accessed 2026-11-12)
[^s4]: Xie, Raghunathan, Liang, Ma, "An Explanation of In-context Learning as Implicit Bayesian Inference", ICLR 2022 (arXiv 2111.02080). https://arxiv.org/pdf/2111.02080 (accessed 2026-11-12)
[^s5]: von Oswald et al., "Transformers Learn In-Context by Gradient Descent", ICML 2023. https://research.google/pubs/transformers-learn-in-context-by-gradient-descent/ (accessed 2026-11-12)
[^s6]: Zhao, Wallace, Feng, Klein, Singh, "Calibrate Before Use: Improving Few-shot Performance of Language Models", ICML 2021. https://proceedings.mlr.press/v139/zhao21c.html (accessed 2026-11-12)
