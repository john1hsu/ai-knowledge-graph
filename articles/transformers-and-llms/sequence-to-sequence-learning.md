---
id: kt:sequence-to-sequence-learning
type: Paradigm
title: Sequence-to-sequence learning
aliases: [seq2seq, encoder-decoder model, RNN encoder-decoder]
domain: transformers-and-llms
summary: >-
  An approach in which a neural encoder reads a variable-length input sequence into a learned
  representation and a decoder generates a variable-length output sequence from it token by token,
  trained end to end; popularised in 2014 for machine translation by Sutskever, Vinyals and Le and by Cho et al.
maturity: established
broader: [kt:deep-learning]
related: [kt:recurrent-neural-network, kt:attention-mechanism, kt:transformer-architecture, kt:beam-search]
relations:
  - {predicate: basedOn, object: kt:long-short-term-memory}
  - {predicate: evaluatedOn, object: kt:wmt-2014}
  - {predicate: usedIn, object: kt:automatic-speech-recognition}
sources:
  - id: s1
    title: "Sequence to Sequence Learning with Neural Networks"
    publisher: Sutskever, Vinyals and Le (Google), NIPS 2014; authors' arXiv version 1409.3215v3
    url: https://arxiv.org/pdf/1409.3215
    type: primary
    accessed: 2026-11-13
  - id: s2
    title: "Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation"
    publisher: Cho, van Merriënboer, Gulcehre, Bahdanau, Bougares, Schwenk and Bengio, Proc. EMNLP 2014, pp. 1724–1734
    url: https://aclanthology.org/D14-1179.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "Dive into Deep Learning, 10.7: Sequence-to-Sequence Learning for Machine Translation"
    publisher: Zhang, Lipton, Li and Smola, d2l.ai
    url: https://d2l.ai/chapter_recurrent-modern/seq2seq.html
    type: textbook
    accessed: 2026-11-13
  - id: s4
    title: "Speech and Language Processing (3rd ed. draft), Chapter 12: Machine Translation"
    publisher: D. Jurafsky and J. H. Martin, Stanford University (draft of 6 January 2026)
    url: https://web.stanford.edu/%7Ejurafsky/slp3/12.pdf
    type: textbook
    accessed: 2026-11-13
  - id: s5
    title: "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"
    publisher: Raffel et al., Journal of Machine Learning Research 21(140):1–67, 2020
    url: https://www.jmlr.org/papers/v21/20-074.html
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s6
    title: "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (arXiv 1910.10683v3)"
    publisher: Raffel et al., authors' arXiv version
    url: https://arxiv.org/pdf/1910.10683v3
    type: primary
    accessed: 2026-11-13
created: 2026-11-13
---

# Sequence-to-sequence learning

**Sequence-to-sequence learning** (often **seq2seq**, or the **encoder-decoder** approach) trains a single neural network to map one sequence of symbols to another whose length may differ, such as an English sentence to its French translation. An **encoder** reads the input and produces a representation of it; a **decoder** then emits the output one token at a time, conditioned on that representation and on the tokens it has already produced, so the decoder behaves like a conditional language model.[^s4] The whole system is trained jointly to maximise the probability of the correct target sequence given the source.[^s2]

## Origins

Jurafsky and Martin credit Kalchbrenner and Blunsom (2013), who paired a convolutional encoder with a recurrent decoder, with pioneering the modern neural encoder-decoder.[^s4] The idea took its familiar form in 2014 in two papers. Cho and colleagues at Montréal proposed an **RNN Encoder–Decoder** whose encoder's final hidden state served as a fixed-length summary vector of the input, and introduced a new gated hidden unit with **reset** and **update** gates, simpler than an LSTM, after finding that a plain tanh unit gave no meaningful results.[^s2] They used it inside a phrase-based system to rescore phrase pairs, adding about 0.57 BLEU on the WMT'14 English–French test set.[^s2] Sutskever, Vinyals and Le at Google instead used the network as a complete translator, and their paper's title gave the field its name.[^s1]

## How it works

In the Sutskever et al. design, one 4-layer LSTM with 1,000 cells per layer encodes the source and a second 4-layer LSTM decodes the target; the model has about 384 million parameters, with 160,000-word source and 80,000-word target vocabularies.[^s1] The d2l.ai textbook contrasts two ways of passing the encoder's summary (the context variable *c*) to the decoder: Sutskever et al. use it only to initialise the decoder's first state, while Cho et al. feed it into every decoding step.[^s3]

Training uses **teacher forcing**: the decoder input is the ground-truth target shifted right by one position and prefixed with a beginning-of-sequence token, and the labels are the same target ending in an end-of-sequence token. Sentences in a minibatch are padded to a common length, and padding positions are masked out of the cross-entropy loss.[^s3] At inference the decoder must consume its own predictions, starting from the beginning-of-sequence token and stopping when it emits the end-of-sequence token, either greedily or with beam search.[^s3]

## Results and practical tricks

Sutskever et al. trained on a 12-million-sentence WMT'14 English–French subset. An ensemble of five LSTMs with a beam of 12 scored 34.81 BLEU, beating a phrase-based baseline's 33.30, which the authors described as the first time a pure neural system clearly outperformed such a baseline on a large-scale translation task; rescoring the baseline's 1,000-best lists reached 36.5.[^s1] Small beams sufficed: a beam of 2 captured most of the gain of larger ones.[^s1]

Their most cited trick was **reversing the source sentence** (but not the target), which cut test perplexity from 5.8 to 4.7 and raised a single model's BLEU from 25.9 to 30.6. The authors hypothesised that reversal shortens the distance between early source words and their translations, easing optimisation, but admitted they could not fully explain it.[^s1] Other details included gradient-norm clipping at 5, batches of length-matched sentences, and about ten days of training on eight GPUs.[^s1]

## Limitations

Compressing an entire input into one fixed-size vector is a bottleneck; d2l.ai notes that attention mechanisms were developed precisely to avoid it.[^s3] Fixed word vocabularies also penalised the 2014 systems, since every out-of-vocabulary word was mapped to an unknown token and scored as wrong.[^s1] Autoregressive decoding is sequential and approximate, because beam search does not guarantee the most probable output.[^s1][^s3]

## Legacy

The encoder-decoder framing outlived recurrent networks. In the Transformer version, encoder blocks apply unmasked self-attention over the source, while each decoder block keeps causal self-attention and adds **cross-attention** whose queries come from the decoder and whose keys and values come from the encoder output.[^s4] Jurafsky and Martin present the encoder-decoder as the architecture for tasks whose output depends on the whole input, naming machine translation and speech recognition.[^s4] Google's T5 (2020) recast every text task as text-to-text with a standard encoder-decoder Transformer, and in its architecture comparison the encoder-decoder with a denoising objective beat decoder-only language-model variants on every task tested.[^s5][^s6]

## Connections

Seq2seq is a **deep learning** paradigm whose original instances were **based on** stacked **LSTMs** and other **recurrent neural networks**, including the gated unit that Cho et al. introduced.[^s1][^s2] It was **evaluated on WMT 2014** English–French and decodes with **beam search**.[^s1] The fixed-vector bottleneck motivated the **attention mechanism**: the Bahdanau, Cho and Bengio paper extends seq2seq with a per-step context, and the **Transformer architecture** keeps the encoder-decoder layout while replacing recurrence with attention.[^s3][^s4] Beyond translation, the same framing is **used in automatic speech recognition**.[^s4]

## Sources

[^s1]: Sutskever, Vinyals and Le, "Sequence to Sequence Learning with Neural Networks", NIPS 2014 (arXiv 1409.3215v3). https://arxiv.org/pdf/1409.3215 (accessed 2026-11-13)
[^s2]: Cho et al., "Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation", EMNLP 2014, pp. 1724–1734. https://aclanthology.org/D14-1179.pdf (accessed 2026-11-13)
[^s3]: Zhang, Lipton, Li and Smola, "10.7. Sequence-to-Sequence Learning for Machine Translation", Dive into Deep Learning. https://d2l.ai/chapter_recurrent-modern/seq2seq.html (accessed 2026-11-13)
[^s4]: Jurafsky and Martin, "Machine Translation", Speech and Language Processing, 3rd ed. draft (January 2026), ch. 12. https://web.stanford.edu/%7Ejurafsky/slp3/12.pdf (accessed 2026-11-13)
[^s5]: Raffel et al., "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", JMLR 21(140), 2020. https://www.jmlr.org/papers/v21/20-074.html (accessed 2026-11-13)
[^s6]: Raffel et al., "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", arXiv 1910.10683v3. https://arxiv.org/pdf/1910.10683v3 (accessed 2026-11-13)
