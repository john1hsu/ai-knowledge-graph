---
id: kt:pretraining
type: Technique
title: "Pretraining: learning general-purpose representations before task adaptation"
aliases: [pre-training, model pretraining, unsupervised pre-training, generative pre-training]
domain: training-and-adaptation
summary: >-
  The first phase of training a model, in which it learns general-purpose
  representations from a very large, mostly unlabeled dataset through a self-supervised objective
  such as next-token or masked-token prediction, before being adapted to specific tasks.
maturity: established
broader: [kt:transfer-learning, kt:self-supervised-learning]
related: [kt:large-language-model, kt:scaling-laws, kt:in-context-learning, kt:emergent-abilities]
relations:
  - {predicate: enables, object: kt:fine-tuning}
  - {predicate: enables, object: kt:instruction-tuning}
  - {predicate: causes, object: kt:benchmark-contamination}
  - {predicate: dependsOn, object: kt:distributed-training}
sources:
  - id: s1
    title: "Why Does Unsupervised Pre-training Help Deep Learning?"
    publisher: Journal of Machine Learning Research 11:625-660, 2010 (Erhan, Bengio, Courville, Manzagol, Vincent, Bengio)
    url: https://jmlr.org/papers/v11/erhan10a.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Improving Language Understanding by Generative Pre-Training"
    publisher: OpenAI technical report, 2018 (Radford, Narasimhan, Salimans, Sutskever)
    url: https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
    type: primary
    accessed: 2026-11-12
  - id: s3
    title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
    publisher: NAACL-HLT 2019, pages 4171-4186 (Devlin, Chang, Lee, Toutanova)
    url: https://aclanthology.org/N19-1423/
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "Training Compute-Optimal Large Language Models"
    publisher: Hoffmann et al. (DeepMind), 2022; authors' arXiv version
    url: https://arxiv.org/abs/2203.15556
    type: primary
    accessed: 2026-11-12
  - id: s5
    title: "The Llama 3 Herd of Models"
    publisher: Llama Team, AI @ Meta, 2024; authors' arXiv version
    url: https://arxiv.org/pdf/2407.21783
    type: primary
    accessed: 2026-11-12
created: 2026-11-12
---

# Pretraining

**Pretraining** is the first stage of a two-stage recipe: a model is trained on a large, general dataset so that it acquires broadly useful representations, and only afterwards is it adapted to the tasks people actually care about. In modern language models the pretraining data is unlabeled text and the objective is self-supervised, meaning the training signal comes from the text itself (for example, predicting the next token), so no human annotation is required.[^s2][^s3] It is the stage at which the model learns language from scratch; later stages such as fine-tuning start from the pretrained weights and adapt them with far less labelled data.[^s2][^s3]

## Origin

The idea predates transformers. In the late 2000s, deep belief networks and stacked autoencoders were commonly trained layer by layer without labels before supervised training, and the best supervised results of the time often relied on such an unsupervised phase.[^s1] Erhan, Bengio and colleagues asked why this helped. Through extensive experiments varying depth, capacity and the number of training examples, they concluded that pretraining steers optimisation toward regions of parameter space that generalise better, and argued that its benefit is best explained as a form of regularization.[^s1]

For language, the decisive step came in 2018. OpenAI's GPT paper trained a 12-layer transformer decoder to predict each token from its left context on BooksCorpus, a collection of over 7,000 unpublished books, then fine-tuned it on labelled tasks with a small added output layer; this generative pre-training approach set new state-of-the-art results on 9 of the 12 datasets studied.[^s2] BERT (Devlin et al., 2019) pretrained a bidirectional transformer encoder instead and reported state-of-the-art results on eleven NLP tasks, including an absolute gain of 7.7 points on GLUE.[^s3]

## How it works

The objective defines what the model learns to do with raw data:

- **Causal (autoregressive) language modelling**, used by GPT-style decoders, maximises the likelihood of each token given the tokens before it.[^s2]
- **Masked language modelling**, used by BERT, picks about 15% of input tokens, mostly replaces them with a mask symbol, and trains the model to recover them from context on both sides; BERT added a next-sentence-prediction task alongside it.[^s3]

Scale is the other defining ingredient. BERT-large had about 340M parameters and was pretrained on roughly 3.3 billion words from BooksCorpus and English Wikipedia.[^s3] By 2024, Meta reported pretraining its flagship Llama 3 model (405B parameters) on about 15.6 trillion tokens using roughly 3.8 × 10^25 FLOPs.[^s5] How to split a fixed compute budget between model size and data is a central design question: Hoffmann et al. (2022) trained over 400 models and found that parameters and training tokens should be scaled in equal proportion, and that many large models of the time were undertrained; their 70B-parameter Chinchilla, trained on four times more data than the 280B Gopher with the same compute, outperformed it.[^s4]

A modern pretraining run is a data-engineering project as much as a modelling one. According to its developers, Llama 3's corpus was built by extracting text from web HTML, removing domains with heavy personal or unsafe content, deduplicating at URL, document and line level, applying heuristic filters, and selecting high-quality text with model-based classifiers. The final mix was roughly half general knowledge, a quarter maths and reasoning, 17% code and 8% multilingual text. The run itself proceeded in stages: initial training at an 8K context, a long-context phase that extended the window to 128K, and a final annealing phase.[^s5]

## Limitations and open questions

Pretraining is expensive and hard to undo: whatever is in the corpus, including errors, biases, personal data and copies of evaluation benchmarks, can be absorbed into the weights, which is why data filtering and decontamination take so much effort.[^s5] A pretrained model is also not directly a helpful assistant; it continues text rather than follows instructions, so further adaptation is needed.[^s2][^s5] Why pretraining transfers so well remains only partly understood, a question that the regularisation account of Erhan et al. opened rather than settled.[^s1] Compute-optimal recipes also depend on use: Hoffmann et al. note that a smaller, longer-trained model is cheaper to fine-tune and serve, so the best size-versus-data split depends on deployment as well as training budget.[^s4]

## Connections

Pretraining is a form of **transfer learning** and in language is usually **self-supervised learning**.[^s1][^s3] It **enables** **fine-tuning** and **instruction tuning**, which adapt the pretrained network with far less data.[^s2][^s3] Its compute/data trade-offs are the subject of **scaling laws**, and it produces the **large language models** whose **in-context learning** and **emergent abilities** are studied elsewhere in this graph.[^s4][^s5] Training on web-scale corpora **causes** the risk of **benchmark contamination**, and runs at this scale **depend on** **distributed training** across many accelerators.[^s5] An influential early analysis of why it works is **"Why Does Unsupervised Pre-training Help Deep Learning?"**.[^s1]

## Sources
[^s1]: Erhan et al., "Why Does Unsupervised Pre-training Help Deep Learning?", JMLR 11, 2010. https://jmlr.org/papers/v11/erhan10a.html (accessed 2026-11-12)
[^s2]: Radford et al., "Improving Language Understanding by Generative Pre-Training", OpenAI, 2018. https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf (accessed 2026-11-12)
[^s3]: Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", NAACL-HLT 2019. https://aclanthology.org/N19-1423/ (accessed 2026-11-12)
[^s4]: Hoffmann et al., "Training Compute-Optimal Large Language Models", 2022. https://arxiv.org/abs/2203.15556 (accessed 2026-11-12)
[^s5]: Llama Team, AI @ Meta, "The Llama 3 Herd of Models", 2024. https://arxiv.org/pdf/2407.21783 (accessed 2026-11-12)
