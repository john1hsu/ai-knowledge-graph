---
id: kt:neural-machine-translation-by-jointly-learning-to-align-and-translate
type: Work
title: Neural Machine Translation by Jointly Learning to Align and Translate
aliases: [Bahdanau et al. 2015, Bahdanau Cho and Bengio 2014, the RNNsearch paper]
domain: transformers-and-llms
summary: >-
  The paper by Bahdanau, Cho and Bengio (arXiv 2014, ICLR 2015) that added a learned soft-alignment
  ("attention") step to the recurrent encoder-decoder, letting the decoder build a fresh context vector
  from all source positions at every output step instead of relying on one fixed-length sentence vector.
maturity: foundational
broader: [kt:attention-mechanism, kt:sequence-to-sequence-learning]
related: [kt:recurrent-neural-network, kt:attention-is-all-you-need, kt:transformer-architecture, kt:long-short-term-memory, kt:beam-search]
relations:
  - {predicate: createdBy, object: kt:yoshua-bengio}
  - {predicate: extends, object: kt:sequence-to-sequence-learning}
  - {predicate: influencedBy, object: kt:alex-graves}
  - {predicate: evaluatedOn, object: kt:wmt-2014}
  - {predicate: enables, object: kt:transformer-architecture}
sources:
  - id: s1
    title: "Neural Machine Translation by Jointly Learning to Align and Translate"
    publisher: Bahdanau, Cho and Bengio, ICLR 2015 conference paper (authors' arXiv version 1409.0473v7, 19 May 2016)
    url: https://arxiv.org/pdf/1409.0473
    type: primary
    accessed: 2026-11-11
  - id: s2
    title: "Dive into Deep Learning, 11.4: The Bahdanau Attention Mechanism"
    publisher: Zhang, Lipton, Li and Smola, d2l.ai
    url: https://d2l.ai/chapter_attention-mechanisms-and-transformers/bahdanau-attention.html
    type: textbook
    accessed: 2026-11-11
  - id: s3
    title: "Speech and Language Processing (3rd ed. draft), Chapter 8: RNNs and LSTMs"
    publisher: D. Jurafsky and J. H. Martin, Stanford University (draft of 12 January 2025)
    url: https://web.stanford.edu/~jurafsky/slp3/old_jan25/8.pdf
    type: textbook
    accessed: 2026-11-11
  - id: s4
    title: "Sequence to Sequence Learning with Neural Networks"
    publisher: Sutskever, Vinyals and Le, Proc. NIPS 2014; Google Research publication page
    url: https://research.google/pubs/sequence-to-sequence-learning-with-neural-networks/
    type: lab-research
    accessed: 2026-11-11
  - id: s5
    title: "Speech and Language Processing (3rd ed. draft), Chapter 13: Machine Translation"
    publisher: D. Jurafsky and J. H. Martin, Stanford University (draft of 19 August 2026)
    url: https://web.stanford.edu/%7ejurafsky/slp3/13.pdf
    type: textbook
    accessed: 2026-11-11
created: 2026-11-11
---

# Neural Machine Translation by Jointly Learning to Align and Translate

**"Neural Machine Translation by Jointly Learning to Align and Translate"** is the paper by Dzmitry Bahdanau (then at Jacobs University Bremen), KyungHyun Cho and Yoshua Bengio (Université de Montréal) that introduced what is now called **Bahdanau attention** or **additive attention**. First posted to arXiv in 2014 and published as a conference paper at ICLR 2015, it proposed a translation model, **RNNsearch**, whose decoder learns to look back at different parts of the source sentence as it generates each target word.[^s1] The Jurafsky and Martin textbook credits it with extending an earlier soft-weighting idea, giving it the name "attention", and applying it to machine translation.[^s3]

## The problem: a fixed-length bottleneck

Neural machine translation in 2014 was dominated by the **encoder-decoder** (sequence-to-sequence) design. In Sutskever, Vinyals and Le's NIPS 2014 version, one deep LSTM read the source sentence into a single vector of fixed dimensionality and a second LSTM generated the translation from that vector; on WMT'14 English-French it scored 34.8 BLEU, above a phrase-based baseline's 33.3.[^s4] Bahdanau and colleagues argued that squeezing every sentence into one fixed-length vector limits such models, especially on long sentences, and cited evidence that basic encoder-decoder quality falls quickly as inputs grow longer.[^s1] Jurafsky and Martin describe the same issue: the encoder's final hidden state is the decoder's only view of the source, so early words of a long sentence may be poorly represented.[^s3]

## How RNNsearch works

The encoder is a **bidirectional RNN**. Forward and backward hidden states are concatenated into an *annotation* h_j for each source word, so each annotation summarizes the words both before and after it.[^s1] At each output step i, a small feed-forward **alignment model** scores how well each annotation matches the decoder's previous state: e_ij = v_aᵀ tanh(W_a s_{i−1} + U_a h_j). A softmax turns the scores into weights α_ij, and the **context vector** c_i = Σ_j α_ij h_j feeds the decoder's next state and word prediction.[^s1] Because the alignment is soft rather than a discrete latent choice, gradients flow through it and the alignment and translation are trained jointly, which gives the paper its title.[^s1]

In today's vocabulary, the previous decoder state acts as the **query**, and the encoder states serve as both **keys** and **values**; the scoring function is called additive attention.[^s2] Jurafsky and Martin contrast this learned scoring with the simpler dot-product score, noting that adding learned weights lets training decide which similarities matter and allows encoder and decoder vectors of different sizes.[^s3]

## Experiments and results

The authors trained on WMT'14 English-French data, about 348 million words after data selection, with 30,000-word vocabularies per language and news-test-2014 (3,003 sentences) as the test set. They compared plain encoder-decoders (RNNencdec) with RNNsearch, each trained on sentences up to 30 or 50 words, using recurrent layers of 1,000 hidden units, minibatch SGD with Adadelta, and beam search for decoding.[^s1]

RNNsearch beat the baseline in every setting: on the full test set, RNNsearch-50 scored 26.75 BLEU against 17.82 for RNNencdec-50, and a longer-trained RNNsearch-50* reached 28.45. On sentences with no unknown words it scored 36.15, slightly above the phrase-based Moses system's 35.63, although Moses (which also used a 418-million-word monolingual corpus) still led on the full test set at 33.30.[^s1] The baseline's BLEU collapsed as sentences lengthened, while RNNsearch-50 showed no clear decline even past 50 words.[^s1] Plotting the weights α_ij also produced interpretable alignments: mostly monotonic, but correctly reordering phrases such as "European Economic Area" into "zone économique européenne".[^s1]

## Limitations

The authors named rare and unknown words as the main open problem, since performance matched Moses only on sentences free of them. They also noted that scoring every source word for every target word is affordable for typical 15–40-word sentences but could limit other applications.[^s1] Each model took about five days to train.[^s1]

## Legacy

The d2l.ai textbook calls the mechanism one of the most influential deep learning ideas of the past decade and traces the Transformer directly to it.[^s2] Its lineage is visible in modern translation systems: the current standard is the encoder-decoder Transformer, whose decoder uses cross-attention, with queries from the decoder and keys and values from the encoder output, to attend to each source word, the same pattern RNNsearch introduced with recurrent states.[^s5]

## Connections

The paper is a landmark work on the **attention mechanism** and **extends sequence-to-sequence learning** by replacing the fixed sentence vector with a per-step context.[^s1][^s4] It was **created by** a team led by **Yoshua Bengio** and was **influenced by Alex Graves**, whose 2013 handwriting-synthesis model used a soft but strictly monotonic alignment that the authors judged too restrictive for translation.[^s1][^s2] Its encoder and decoder are **recurrent neural networks**, contrasting with the **LSTM** encoder-decoder it was compared against, and it decodes with **beam search**.[^s1][^s4] It was **evaluated on WMT 2014** English-French.[^s1] By showing that a model could learn where to look, it **enabled** the **Transformer architecture**: **Attention Is All You Need** kept the attention and dropped the recurrence.[^s2][^s5]

## Sources

[^s1]: Bahdanau, Cho and Bengio, "Neural Machine Translation by Jointly Learning to Align and Translate", ICLR 2015 (arXiv 1409.0473v7). https://arxiv.org/pdf/1409.0473 (accessed 2026-11-11)
[^s2]: Zhang, Lipton, Li and Smola, "11.4. The Bahdanau Attention Mechanism", Dive into Deep Learning. https://d2l.ai/chapter_attention-mechanisms-and-transformers/bahdanau-attention.html (accessed 2026-11-11)
[^s3]: Jurafsky and Martin, "RNNs and LSTMs", Speech and Language Processing, 3rd ed. draft (January 2025), ch. 8. https://web.stanford.edu/~jurafsky/slp3/old_jan25/8.pdf (accessed 2026-11-11)
[^s4]: Sutskever, Vinyals and Le, "Sequence to Sequence Learning with Neural Networks", Proc. NIPS 2014. https://research.google/pubs/sequence-to-sequence-learning-with-neural-networks/ (accessed 2026-11-11)
[^s5]: Jurafsky and Martin, "Machine Translation", Speech and Language Processing, 3rd ed. draft (August 2026), ch. 13. https://web.stanford.edu/%7ejurafsky/slp3/13.pdf (accessed 2026-11-11)
