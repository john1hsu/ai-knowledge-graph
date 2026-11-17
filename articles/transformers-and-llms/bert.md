---
id: kt:bert
type: Model
title: BERT
aliases: [Bidirectional Encoder Representations from Transformers, BERT-base, BERT-large]
domain: transformers-and-llms
summary: >-
  An encoder-only Transformer language model released by Google AI Language in 2018 that is pretrained on
  unlabeled text with masked language modeling and next sentence prediction, giving deeply bidirectional
  contextual representations that are then fine-tuned for downstream language-understanding tasks.
maturity: established
broader: [kt:transformer-architecture, kt:pretraining]
related: [kt:self-supervised-learning, kt:transfer-learning, kt:fine-tuning, kt:embeddings, kt:reranking, kt:language-models-are-few-shot-learners]
relations:
  - {predicate: createdBy, object: kt:google}
  - {predicate: basedOn, object: kt:attention-is-all-you-need}
  - {predicate: trainedWith, object: kt:masked-language-modeling}
  - {predicate: contrastsWith, object: kt:word2vec}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: supersededBy, object: kt:roberta}
sources:
  - id: s1
    title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
    publisher: Devlin, Chang, Lee and Toutanova, Proceedings of NAACL-HLT 2019, Vol. 1, pp. 4171–4186, ACL Anthology (doi 10.18653/v1/N19-1423)
    url: https://aclanthology.org/N19-1423.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "Open Sourcing BERT: State-of-the-Art Pre-training for Natural Language Processing"
    publisher: Jacob Devlin and Ming-Wei Chang, Google Research blog, 2 November 2018
    url: https://research.google/blog/open-sourcing-bert-state-of-the-art-pre-training-for-natural-language-processing/
    type: lab-research
    accessed: 2026-11-17
  - id: s3
    title: "Dive into Deep Learning, 15.8: Bidirectional Encoder Representations from Transformers (BERT)"
    publisher: Zhang, Lipton, Li and Smola, d2l.ai
    url: https://d2l.ai/chapter_natural-language-processing-pretraining/bert.html
    type: textbook
    accessed: 2026-11-17
  - id: s4
    title: "RoBERTa: A Robustly Optimized BERT Pretraining Approach (arXiv 1907.11692)"
    publisher: Liu, Ott, Goyal et al., authors' arXiv version, July 2019
    url: https://arxiv.org/abs/1907.11692
    type: primary
    accessed: 2026-11-17
  - id: s5
    title: "Transformers documentation: BERT"
    publisher: Hugging Face
    url: https://huggingface.co/docs/transformers/model_doc/bert
    type: official-docs
    accessed: 2026-11-17
created: 2026-11-17
---

# BERT

**BERT** (Bidirectional Encoder Representations from Transformers) is a language representation model introduced by Jacob Devlin, Ming-Wei Chang, Kenton Lee and Kristina Toutanova of Google AI Language. It pretrains a stack of Transformer encoder layers on unlabeled text so that every token's representation draws on both its left and right context in all layers; a pretrained BERT can then be adapted to a task by adding as little as one output layer and fine-tuning the whole network.[^s1] The paper appeared at NAACL 2019, where it received the Best Long Paper award, and Google released code and pretrained English checkpoints on 2 November 2018.[^s1][^s2]

## Origin and motivation

Before BERT, contextual representations came either from feature-based models such as ELMo, whose bidirectional LSTM outputs were fed as frozen features into task-specific architectures, or from fine-tuned models such as OpenAI's GPT, a Transformer decoder that reads text strictly left to right.[^s3] The BERT authors argued that this left-to-right restriction limits pretraining, because in GPT's self-attention each token can see only earlier tokens.[^s1] Google's announcement framed the contrast as GPT being unidirectional, ELMo shallowly bidirectional and BERT deeply bidirectional, while context-free embeddings such as word2vec and GloVe assign one vector per word regardless of usage.[^s2]

## How it works

**Input.** Text is split into WordPiece tokens from a 30,000-token vocabulary. A sequence starts with a special classification token and separates sentence pairs with a separator token; each input vector is the sum of a token embedding, a learned segment embedding (first or second sentence) and a learned position embedding, rather than the fixed sinusoidal encoding of the original Transformer.[^s1][^s3]

**Masked language modeling (MLM).** Letting a bidirectional model condition on both sides of a word would let it trivially see the word it must predict, so BERT hides words instead, an objective the authors say was inspired by the Cloze task.[^s1][^s2] 15% of token positions are selected; of these, 80% are replaced by a mask token, 10% by a random token and 10% are left unchanged, which reduces the mismatch with fine-tuning, where mask tokens never appear. The model predicts the original tokens with a cross-entropy loss.[^s3]

**Next sentence prediction (NSP).** For sentence pairs, half the time the second sentence really follows the first and half the time it is drawn at random; a classifier on the classification token's output predicts which. The pretraining loss combines the MLM and NSP losses, and both labels come from raw text, so no annotation is needed.[^s3] In the paper's ablation, dropping NSP lowered development-set scores on QNLI, MNLI and SQuAD 1.1.[^s1]

**Sizes and training.** BERT-base has 12 layers, hidden size 768 and 12 attention heads (110M parameters); BERT-large has 24 layers, hidden size 1024 and 16 heads (340M). Both were pretrained on BooksCorpus (about 800M words) and English Wikipedia (about 2.5B words) for 1,000,000 steps with 256-sequence batches and a 512-token maximum length; each run took about four days on 16 TPU chips (base) or 64 (large).[^s1][^s3]

## Results and impact

The NAACL paper reported new state-of-the-art results on eleven NLP tasks, including a GLUE score of 80.5 (7.7 points absolute over the prior best), MultiNLI accuracy of 86.7% and SQuAD v1.1 test F1 of 93.2.[^s1] Google's release post noted that the SQuAD v1.1 figure exceeded the human-performance score of 91.2 reported for that benchmark, and claimed a question-answering system could be fine-tuned in about 30 minutes on one Cloud TPU or a few hours on one GPU (claims as of November 2018).[^s2]

## Limitations and critiques

BERT's encoder-only, masked design suits understanding tasks such as classification, tagging and extractive question answering rather than free-running text generation; Hugging Face's library exposes generation only through a separate causal-LM head and decoder configuration.[^s5] Because it uses absolute position embeddings, inputs are padded on the right and length is capped by the pretrained position table.[^s5][^s1] A 2019 replication study by Liu and colleagues concluded that BERT was significantly undertrained and that a more carefully tuned recipe, RoBERTa, matched or beat every model published after it on GLUE, RACE and SQuAD, showing that many of BERT's design and hyperparameter choices were not optimal.[^s4]

## In practice

BERT checkpoints such as bert-base-uncased remain widely used through Hugging Face Transformers, which provides the base encoder plus heads for masked-token prediction, next sentence prediction and sequence classification (as of the library's 2026 documentation).[^s5] BERT-style encoders are a common backbone for sentence embeddings, cross-encoder rerankers and lightweight classifiers where a decoder-only large language model would be costlier.[^s5][^s3]

## Connections

BERT is an instance of the **Transformer architecture** that keeps only the encoder stack introduced in *Attention Is All You Need*, and it is a landmark of **pretraining** followed by **fine-tuning**, the **transfer-learning** pattern that made task-specific architectures largely unnecessary.[^s1][^s3] Its **masked language modeling** objective is a canonical form of **self-supervised learning**, since labels come from the text itself.[^s3] It contrasts with static **word2vec** and GloVe **embeddings** by producing context-dependent vectors, and with the left-to-right decoder line that led to GPT-3 (*Language Models are Few-Shot Learners*).[^s2][^s3] It was created at **Google**, is implemented in **Hugging Face Transformers**, underpins many **reranking** models, and was superseded as a recipe by **RoBERTa**.[^s2][^s5][^s4]

## Sources
[^s1]: Devlin, Chang, Lee and Toutanova, "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", NAACL-HLT 2019, pp. 4171–4186. https://aclanthology.org/N19-1423.pdf (accessed 2026-11-17)
[^s2]: Devlin and Chang, "Open Sourcing BERT: State-of-the-Art Pre-training for Natural Language Processing", Google Research blog, 2 November 2018. https://research.google/blog/open-sourcing-bert-state-of-the-art-pre-training-for-natural-language-processing/ (accessed 2026-11-17)
[^s3]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, §15.8 "Bidirectional Encoder Representations from Transformers (BERT)". https://d2l.ai/chapter_natural-language-processing-pretraining/bert.html (accessed 2026-11-17)
[^s4]: Liu, Ott, Goyal et al., "RoBERTa: A Robustly Optimized BERT Pretraining Approach", arXiv:1907.11692, 2019. https://arxiv.org/abs/1907.11692 (accessed 2026-11-17)
[^s5]: Hugging Face, "Transformers documentation: BERT". https://huggingface.co/docs/transformers/model_doc/bert (accessed 2026-11-17)
