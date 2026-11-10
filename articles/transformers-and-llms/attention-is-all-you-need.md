---
id: kt:attention-is-all-you-need
type: Work
title: Attention Is All You Need
aliases: [Vaswani et al. 2017, the Transformer paper]
domain: transformers-and-llms
summary: >-
  The 2017 NeurIPS paper by Vaswani and seven Google colleagues that introduced the Transformer, an
  encoder-decoder network built entirely from attention and feed-forward layers, with no recurrence or
  convolution, and showed it beat recurrent translation models while training far faster.
maturity: foundational
broader: [kt:sequence-to-sequence-learning, kt:attention-mechanism]
related: [kt:transformer-architecture, kt:self-attention, kt:positional-encoding, kt:recurrent-neural-network, kt:large-language-model]
relations:
  - {predicate: createdBy, object: kt:google}
  - {predicate: influencedBy, object: kt:neural-machine-translation-by-jointly-learning-to-align-and-translate}
  - {predicate: evaluatedOn, object: kt:wmt-2014}
  - {predicate: enables, object: kt:large-language-model}
sources:
  - id: s1
    title: "Attention is All you Need"
    publisher: Vaswani et al., Advances in Neural Information Processing Systems 30 (NIPS 2017), proceedings PDF
    url: https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s2
    title: "Attention Is All You Need (arXiv 1706.03762, v7)"
    publisher: Vaswani et al., authors' arXiv version (v1 12 June 2017; v7 2 August 2023)
    url: https://arxiv.org/abs/1706.03762
    type: primary
    accessed: 2026-11-10
  - id: s3
    title: "Transformer: A Novel Neural Network Architecture for Language Understanding"
    publisher: Google Research blog (Jakob Uszkoreit), 31 August 2017
    url: https://research.google/blog/transformer-a-novel-neural-network-architecture-for-language-understanding/
    type: lab-research
    accessed: 2026-11-10
  - id: s4
    title: "Dive into Deep Learning, 11.7: The Transformer Architecture"
    publisher: Zhang, Lipton, Li and Smola, d2l.ai
    url: https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html
    type: textbook
    accessed: 2026-11-10
  - id: s5
    title: "Neural Machine Translation by Jointly Learning to Align and Translate"
    publisher: Bahdanau, Cho and Bengio, ICLR 2015 (authors' arXiv version)
    url: https://arxiv.org/pdf/1409.0473
    type: primary
    accessed: 2026-11-10
  - id: s6
    title: "Speech and Language Processing (3rd ed. draft), Chapter 7: Transformers and Pretraining"
    publisher: D. Jurafsky and J. H. Martin, Stanford University (draft of August 2026)
    url: https://web.stanford.edu/~jurafsky/slp3/7.pdf
    type: textbook
    accessed: 2026-11-10
created: 2026-11-10
---

# Attention Is All You Need

*Attention Is All You Need* is the paper that introduced the **Transformer**. Written by Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser and Illia Polosukhin, it appeared in *Advances in Neural Information Processing Systems 30* (NIPS 2017).[^s1] Its central proposal was a sequence transduction model based solely on attention, discarding the recurrent and convolutional layers that then dominated machine translation.[^s1] The first arXiv version was posted on 12 June 2017, and the authors revised it through a seventh version in August 2023.[^s2]

## Background

By 2017 the best translation systems were encoder-decoder networks built from recurrent or convolutional layers, usually joined by an attention mechanism.[^s1] That attention idea came from Bahdanau, Cho and Bengio (ICLR 2015), who argued that squeezing a whole source sentence into one fixed-length vector was a bottleneck that hurt long sentences, and let the decoder instead take a learned, weighted average over encoder states for each output word.[^s5] Recurrent networks still processed tokens one after another, which limited how well training could use parallel hardware such as GPUs and TPUs.[^s3] Vaswani et al.'s step was to drop recurrence altogether and let attention do all the work of relating positions.[^s4]

## What the paper proposed

The model keeps the encoder-decoder layout. Each side is a stack of N = 6 identical layers; encoder layers combine multi-head self-attention with a position-wise feed-forward network, and decoder layers add a third sub-layer that attends over the encoder output.[^s1] Every sub-layer is wrapped in a residual connection followed by layer normalization.[^s1] In the decoder, connections to future positions are masked out before the softmax so that each prediction depends only on earlier outputs.[^s4]

The core operation is **scaled dot-product attention**, softmax(QKᵀ/√d_k)V; the authors divide by √d_k because large dot products otherwise push the softmax into regions with tiny gradients.[^s1] **Multi-head attention** runs h = 8 such attentions in parallel on learned projections (d_model = 512, d_k = d_v = 64), letting the model attend to different representation subspaces at roughly the cost of one full-width head.[^s1] Because attention ignores order, the paper adds sinusoidal **positional encodings** to the embeddings; learned position embeddings gave nearly identical results, but the sinusoids were kept in the hope that they extrapolate to longer sequences.[^s1]

The paper's complexity comparison explains the speed claim: a self-attention layer costs O(n²·d) but needs only O(1) sequential operations and connects any two positions in one step, whereas a recurrent layer costs O(n·d²) with O(n) sequential steps.[^s1] Self-attention is therefore cheaper whenever sequence length n is smaller than the representation width d.[^s1]

## Results

On WMT 2014 English-German, the large Transformer scored 28.4 BLEU, more than 2 points above previous results including ensembles, and the base model scored 27.3.[^s1] On English-French the proceedings version reports 41.0 BLEU for the large model as a new single-model state of the art; the later arXiv revision's abstract gives 41.8.[^s1][^s2] Training ran on one machine with eight NVIDIA P100 GPUs: about 12 hours for the base model and 3.5 days for the large one.[^s1] Google's announcement added that the same architecture handled English constituency parsing with little adaptation, and it released the code through the Tensor2Tensor library.[^s3]

## Influence and limitations

The architecture soon outgrew translation. It was first used as an encoder-decoder, then adapted for masked language modelling (BERT) and for autoregressive decoder-only models such as GPT-2, the lineage of today's large language models.[^s6] Textbooks now describe Transformers as pervasive across language, vision, speech and reinforcement learning.[^s4] The paper's own conclusion anticipated this, naming images, audio and video as targets, and it flagged the cost of attending over very long inputs, proposing restricted local attention as future work.[^s1] Its own complexity table makes the trade-off explicit: per-layer attention cost grows with the square of sequence length, so the advantage over recurrence shrinks for very long sequences.[^s1] The paper also lists making generation less sequential as an open goal, since the decoder still emits one token at a time.[^s1]

The author footnote records that the eight listed authors contributed equally in random order; Uszkoreit proposed replacing RNNs with self-attention, and Shazeer proposed scaled dot-product attention, multi-head attention and the parameter-free position representation.[^s1]

## Connections

The paper belongs to **sequence-to-sequence learning** and builds on the **attention mechanism**, and it was **influenced by** Bahdanau et al.'s alignment model.[^s5] It was **created by** researchers at **Google** and **evaluated on** the WMT 2014 translation tasks.[^s1][^s3] It is the origin of the **Transformer architecture** and of its components **self-attention** and sinusoidal **positional encoding**, positioned as a replacement for the **recurrent neural network**.[^s1] By supplying the backbone later scaled up into GPT-style models, it **enables** the **large language model**.[^s6]

## Sources
[^s1]: Vaswani et al., "Attention is All you Need", NIPS 2017 proceedings. https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf (accessed 2026-11-10)
[^s2]: Vaswani et al., "Attention Is All You Need", arXiv 1706.03762 (v7). https://arxiv.org/abs/1706.03762 (accessed 2026-11-10)
[^s3]: Uszkoreit, "Transformer: A Novel Neural Network Architecture for Language Understanding", Google Research blog, 2017. https://research.google/blog/transformer-a-novel-neural-network-architecture-for-language-understanding/ (accessed 2026-11-10)
[^s4]: Zhang et al., Dive into Deep Learning, section 11.7. https://d2l.ai/chapter_attention-mechanisms-and-transformers/transformer.html (accessed 2026-11-10)
[^s5]: Bahdanau, Cho and Bengio, "Neural Machine Translation by Jointly Learning to Align and Translate", ICLR 2015. https://arxiv.org/pdf/1409.0473 (accessed 2026-11-10)
[^s6]: Jurafsky and Martin, Speech and Language Processing, ch. 7 (Aug 2026 draft). https://web.stanford.edu/~jurafsky/slp3/7.pdf (accessed 2026-11-10)
