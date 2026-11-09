---
id: kt:automatic-speech-recognition
type: Application
title: Automatic speech recognition
aliases: [ASR, speech recognition, speech-to-text, STT]
domain: computer-vision-and-multimodal
summary: >-
  The task of mapping an audio waveform of spoken language to the sequence of words it contains, now
  done mostly by end-to-end neural models (CTC, RNN-Transducer and attention-based encoder-decoders)
  and scored by word error rate.
maturity: established
broader: [kt:speech-processing, kt:sequence-to-sequence-learning]
related: [kt:hidden-markov-model, kt:recurrent-neural-network, kt:transformer-architecture, kt:whisper]
relations:
  - {predicate: evaluatedOn, object: kt:librispeech}
  - {predicate: evaluatedOn, object: kt:switchboard-corpus}
sources:
  - id: s1
    title: "Speech and Language Processing (3rd ed. draft), Chapter 16: Automatic Speech Recognition"
    publisher: Daniel Jurafsky and James H. Martin, Stanford University (draft of August 2026)
    url: https://web.stanford.edu/~jurafsky/slp3/16.pdf
    type: textbook
    accessed: 2026-11-09
  - id: s2
    title: "Deep Neural Networks for Acoustic Modeling in Speech Recognition"
    publisher: Hinton, Deng, Yu, Dahl, Mohamed, Jaitly, Senior, Vanhoucke, Nguyen, Sainath and Kingsbury, IEEE Signal Processing Magazine, 2012 (Google Research publication page)
    url: https://research.google/pubs/deep-neural-networks-for-acoustic-modeling-in-speech-recognition/
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s3
    title: "Connectionist Temporal Classification: Labelling Unsegmented Sequence Data with Recurrent Neural Networks"
    publisher: Graves, Fernández, Gomez and Schmidhuber, ICML 2006, pp. 369–376 (doi:10.1145/1143844.1143891)
    url: https://mlanthology.org/icml/2006/graves2006icml-connectionist
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "Robust Speech Recognition via Large-Scale Weak Supervision"
    publisher: Radford, Kim, Xu, Brockman, McLeavey and Sutskever, Proceedings of ICML 2023 (PMLR 202), pp. 28492–28518
    url: https://proceedings.mlr.press/v202/radford23a.html
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# Automatic speech recognition

Automatic speech recognition (ASR) converts a recorded or streamed audio waveform into the words that were spoken.[^s1] How hard it is depends on several dimensions: vocabulary size (a handful of command words is close to solved, open transcription with tens of thousands of words is not), whether the speaker is reading or talking to a machine rather than conversing with another person, the recording channel and background noise, and how closely the speaker's accent or dialect matches the training data.[^s1]

## History: from HMMs to end-to-end networks

For decades the standard recipe was a hidden Markov model (HMM) to handle the variable timing of speech, with Gaussian mixture models (GMMs) scoring how well each HMM state fit a short window of acoustic features.[^s2] In 2012, four research groups jointly reported that a deep feedforward network taking several frames of features as input and outputting posteriors over HMM states beat GMMs on a range of benchmarks, sometimes by a large margin.[^s2] This "hybrid" DNN-HMM result was one of the first large industrial wins for deep learning.[^s2]

A parallel line removed the need for frame-level alignments. Connectionist Temporal Classification (CTC), introduced by Graves and colleagues at ICML 2006, lets a recurrent network be trained directly on unsegmented audio paired with label sequences; on the TIMIT corpus it outperformed both a baseline HMM and a hybrid HMM-RNN.[^s3]

## How modern systems work

Input audio is usually turned into a log mel spectrogram (often 80 or 128 channels, one frame roughly every 10 ms), and convolutional layers with stride subsample it, because acoustic frames vastly outnumber the characters or words to be produced.[^s1] Three output designs dominate:[^s1]

- **CTC** emits one label per frame, including a special blank; decoding merges repeats and deletes blanks, and training sums over every alignment that yields the target. Each frame's output is assumed independent of the others given the audio, so CTC learns no implicit language model and an external one is often interpolated. It runs left to right, which suits streaming.[^s1]
- **RNN-Transducer (RNN-T)** adds a predictor network conditioned on previously emitted tokens, relaxing CTC's independence assumption while keeping streaming.[^s1]
- **Attention-based encoder-decoders** run a transformer encoder over the subsampled features and a decoder that generates subword tokens one at a time using cross-attention, trained with cross-entropy and teacher forcing and decoded greedily or with beam search, optionally rescoring an n-best list with a language model.[^s1]

Self-supervised pretraining (wav2vec 2.0, HuBERT) first learns from unlabeled audio by masking parts of the input and predicting hidden targets, then fine-tunes with CTC on a much smaller labelled set.[^s1]

## Evaluation and limitations

The standard metric is word error rate: substitutions plus deletions plus insertions, divided by the number of words in the reference transcript and multiplied by 100. Because insertions count, WER can exceed 100%. Alignment uses minimum edit distance (NIST's sclite is the usual scoring tool), after text normalization.[^s1]

Accuracy is very uneven across conditions. Figures compiled in the textbook for roughly 2023–2024 systems show about 1.4% WER on LibriSpeech "clean" read audiobooks and 5.8% on Switchboard telephone conversations, but 16.2% on the CORAAL corpus of African American English interviews and 25.5% on CHiME-6 distant-microphone dinner-party recordings.[^s1] Conversational, accented and noisy speech therefore remains the main open problem, and the gap across dialects is also a fairness concern.[^s1]

## In practice

OpenAI's Whisper (ICML 2023) illustrates the current large-scale approach: an encoder-decoder trained on about 680,000 hours of multilingual, multitask, weakly supervised audio-transcript pairs from the internet.[^s4] The authors report that it transfers to standard benchmarks zero-shot, without dataset-specific fine-tuning, and approaches human accuracy and robustness; these are the authors' own claims.[^s4] The same model handles transcription, speech translation, language identification and voice-activity detection through special task tokens, and its weights and inference code were released.[^s1][^s4]

## Connections

ASR is a branch of **speech processing** and a classic instance of **sequence-to-sequence learning**, since a long acoustic sequence must be mapped to a much shorter token sequence.[^s1] It grew out of **hidden Markov model** systems, was transformed by deep acoustic models and **recurrent neural networks** trained with CTC, and now largely uses the **transformer architecture**, decoded with beam search.[^s2][^s3][^s1] Self-supervised pretraining and the **Whisper** model show the field's shift toward scale and weak supervision.[^s1][^s4] Systems are routinely **evaluated on** LibriSpeech and the Switchboard corpus, alongside harder sets such as CHiME and CORAAL.[^s1]

## Sources
[^s1]: Jurafsky & Martin, *Speech and Language Processing* (3rd ed. draft, Aug 2026), Ch. 16 "Automatic Speech Recognition". https://web.stanford.edu/~jurafsky/slp3/16.pdf (accessed 2026-11-09)
[^s2]: Hinton et al., "Deep Neural Networks for Acoustic Modeling in Speech Recognition", IEEE Signal Processing Magazine, 2012. https://research.google/pubs/deep-neural-networks-for-acoustic-modeling-in-speech-recognition/ (accessed 2026-11-09)
[^s3]: Graves, Fernández, Gomez & Schmidhuber, "Connectionist Temporal Classification", ICML 2006. https://mlanthology.org/icml/2006/graves2006icml-connectionist (accessed 2026-11-09)
[^s4]: Radford et al., "Robust Speech Recognition via Large-Scale Weak Supervision", ICML 2023 (PMLR 202). https://proceedings.mlr.press/v202/radford23a.html (accessed 2026-11-09)
