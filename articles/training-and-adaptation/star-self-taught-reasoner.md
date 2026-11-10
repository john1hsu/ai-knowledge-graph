---
id: kt:star-self-taught-reasoner
type: Technique
title: "STaR: Self-Taught Reasoner"
aliases: [STaR, Self-Taught Reasoner, bootstrapping reasoning with reasoning, rationale bootstrapping]
domain: training-and-adaptation
summary: >-
  An iterative self-training method in which a language model generates step-by-step rationales for training
  questions, keeps only those that reach the correct answer (retrying with the answer as a hint when it fails), and is
  fine-tuned on them, so its reasoning improves without a large human-written rationale dataset.
maturity: established
broader: [kt:fine-tuning]
related: [kt:synthetic-data, kt:reasoning-models, kt:policy-gradient, kt:self-consistency, kt:quiet-star]
relations:
  - {predicate: introducedIn, object: kt:star-bootstrapping-reasoning-with-reasoning}
  - {predicate: basedOn, object: kt:chain-of-thought}
  - {predicate: extends, object: kt:scratchpad}
  - {predicate: evaluatedOn, object: kt:gsm8k}
  - {predicate: evaluatedOn, object: kt:commonsenseqa}
  - {predicate: influencedBy, object: kt:expert-iteration}
sources:
  - id: s1
    title: "STaR: Bootstrapping Reasoning With Reasoning"
    publisher: Advances in Neural Information Processing Systems 35 (NeurIPS 2022), Zelikman, Wu, Mu and Goodman
    url: https://proceedings.neurips.cc/paper_files/paper/2022/hash/639a9a172c044fbb64175b5fad42e9a5-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s2
    title: "STaR: Bootstrapping Reasoning With Reasoning (full text)"
    publisher: arXiv 2203.14465 (Zelikman, Wu, Mu and Goodman; Stanford University and Google Research)
    url: https://arxiv.org/pdf/2203.14465
    type: primary
    accessed: 2026-11-10
  - id: s3
    title: "STaR: Self-Taught Reasoner Bootstrapping Reasoning With Reasoning"
    publisher: Google Research publications
    url: https://research.google/pubs/star-self-taught-reasoner-bootstrapping-reasoning-with-reasoning/
    type: lab-research
    accessed: 2026-11-10
  - id: s4
    title: "Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking"
    publisher: arXiv 2403.09629 (Zelikman, Harik, Shao, Jayasiri, Haber and Goodman)
    url: https://arxiv.org/abs/2403.09629
    type: primary
    accessed: 2026-11-10
  - id: s5
    title: "RL-STaR: Theoretical Analysis of Reinforcement Learning Frameworks for Self-Taught Reasoner"
    publisher: arXiv 2410.23912 (Chang, Lee, Shih, Tseng and Wu)
    url: https://arxiv.org/pdf/2410.23912
    type: preprint
    accessed: 2026-11-10
  - id: s6
    title: "Towards Reasoning in Large Language Models: A Survey"
    publisher: arXiv 2212.10403 (Huang and Chang, University of Illinois Urbana-Champaign)
    url: https://arxiv.org/pdf/2212.10403
    type: preprint
    accessed: 2026-11-10
created: 2026-11-10
---

# STaR: Self-Taught Reasoner

**STaR** (Self-Taught Reasoner) is a training loop that lets a language model teach itself to reason step by step. Instead of relying on a large dataset of human-written rationales, or on few-shot chain-of-thought prompting alone, STaR has the model write its own rationales for many questions, keeps the ones that lead to the right answer, fine-tunes on them, and repeats.[^s1] It was introduced by Eric Zelikman, Yuhuai Wu, Jesse Mu and Noah D. Goodman of Stanford University (Wu also at Google Research) in the paper "STaR: Bootstrapping Reasoning With Reasoning", first posted to arXiv in March 2022 and published at NeurIPS 2022.[^s2][^s1][^s3]

## How it works

STaR needs only a handful of worked examples with rationales (about ten in the paper) plus a large dataset that has questions and final answers but no reasoning.[^s2] Each iteration has four steps:[^s2]

1. **Generate.** Prompt the current model with the few-shot rationale examples followed by each training question; it writes a rationale and an answer.[^s2]
2. **Filter.** Keep only rationales whose final answer matches the ground truth.[^s2]
3. **Rationalize.** For questions the model got wrong, show the correct answer as a hint and ask it to produce a rationale that reaches that answer; correct ones are added to the training set with the hint removed, as if the model had found them unaided.[^s2]
4. **Fine-tune.** Fine-tune the *original* pretrained model on the collected rationales (restarting from the base model each round to limit overfitting), then use the new model to generate the next round's data, until performance plateaus.[^s2]

Rationalization matters because plain filtering only ever learns from problems the model can already solve; the hint exposes it to harder problems and enlarges the training set.[^s2] The authors also frame STaR in reinforcement-learning terms: treating the rationale as a latent variable and answer correctness as a 0/1 reward, the filter-then-fine-tune step approximates a policy-gradient update that discards gradients from incorrect samples. It resembles expert iteration, except that the "expert" is the fixed set of ground-truth answers and no value function is trained.[^s2]

## Evidence

The 2022 experiments used the 6-billion-parameter GPT-J.[^s2] On CommonsenseQA (five-way multiple choice), STaR with rationalization reached 72.5% dev accuracy, against 36.6% for few-shot chain-of-thought GPT-J and 60.0% for GPT-J fine-tuned to output answers directly. That came within about half a point of a fine-tuned GPT-3 model roughly 30 times larger (73.0%), while training on 86.7% of the dataset.[^s2][^s1] On GSM8K grade-school math the gains were real but small in absolute terms: 10.7% versus 5.8% for direct fine-tuning, and rationalization helped little there.[^s2] On synthetic multi-digit addition, written in the scratchpad format, accuracy rose to 89.5% after 16 iterations, compared with 76.3% for a model trained without rationales.[^s2] In a human study, crowdworkers preferred STaR-generated CommonsenseQA rationales over few-shot ones more often than chance, though the authors warn this does not show human-level explanation.[^s2]

## Limitations

The authors list several caveats.[^s2] The loop only starts if few-shot performance is already above chance; GPT-2 could not bootstrap even on arithmetic. On tasks with high chance accuracy, such as yes/no questions, many bad rationales reach the right answer by luck and pass the filter. A correct answer does not guarantee a *faithful* rationale, since the model may pick the answer first and justify it afterwards. And because STaR reinforces whatever reasoning solves the dataset, it can amplify biases, with rationalization sometimes eliciting biased answers the model would not otherwise give.[^s2] A 2024 theoretical analysis (RL-STaR, an arXiv preprint) modeled the loop as an MDP and argued that, if the pretrained model beats random guessing at each reasoning step, expected return does not decrease across iterations and trajectories that reach the answer through wrong steps fade out — under simplifying assumptions such as a fixed number of steps and no rationalization.[^s5]

## In practice and successors

STaR became a reference point for "self-improving" reasoning: a 2022–23 survey of LLM reasoning groups it with later work showing models can raise their reasoning ability by training on their own filtered outputs.[^s6] The same group's Quiet-STaR (arXiv, March 2024) generalized the idea from question answering to arbitrary text, training a model to generate internal rationales at each token to better predict what comes next; after continued pretraining on web text, the authors reported zero-shot gains from 5.9% to 10.9% on GSM8K and from 36.3% to 47.2% on CommonsenseQA without task-specific fine-tuning.[^s4] Later theoretical work treats STaR-style loops (sample reasoning, check the final answer, retrain on what worked) as a reinforcement-learning framework for chain-of-thought training.[^s5]

## Connections

STaR is a form of **fine-tuning** whose training data is model-generated, making it a case of **synthetic data**.[^s2] It is **based on** **chain-of-thought** rationales elicited by few-shot prompting, and **extends** the **scratchpad** idea, whose arithmetic format it reuses, by having the model write its own traces.[^s2] It is **introduced in** the NeurIPS 2022 paper[^s1] and **evaluated on** **GSM8K** and **CommonsenseQA**.[^s2] Its reward-filtered updates link it to **policy gradient** methods and **expert iteration**,[^s2][^s5] it is a precursor of today's **reasoning models**, and **Quiet-STaR** carries it into pretraining.[^s4][^s6] It is also related to **self-consistency**: the survey notes that a follow-up self-improvement method used self-consistency in place of labeled answers to select its own training rationales.[^s6]

## Sources

[^s1]: Zelikman, Wu, Mu and Goodman, "STaR: Bootstrapping Reasoning With Reasoning", NeurIPS 2022. https://proceedings.neurips.cc/paper_files/paper/2022/hash/639a9a172c044fbb64175b5fad42e9a5-Abstract-Conference.html (accessed 2026-11-10)
[^s2]: Zelikman, Wu, Mu and Goodman, "STaR: Bootstrapping Reasoning With Reasoning", arXiv 2203.14465. https://arxiv.org/pdf/2203.14465 (accessed 2026-11-10)
[^s3]: Google Research, "STaR: Self-Taught Reasoner Bootstrapping Reasoning With Reasoning". https://research.google/pubs/star-self-taught-reasoner-bootstrapping-reasoning-with-reasoning/ (accessed 2026-11-10)
[^s4]: Zelikman, Harik, Shao, Jayasiri, Haber and Goodman, "Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking", arXiv 2403.09629. https://arxiv.org/abs/2403.09629 (accessed 2026-11-10)
[^s5]: Chang, Lee, Shih, Tseng and Wu, "RL-STaR: Theoretical Analysis of Reinforcement Learning Frameworks for Self-Taught Reasoner", arXiv 2410.23912. https://arxiv.org/pdf/2410.23912 (accessed 2026-11-10)
[^s6]: Huang and Chang, "Towards Reasoning in Large Language Models: A Survey", arXiv 2212.10403. https://arxiv.org/pdf/2212.10403 (accessed 2026-11-10)
