---
id: kt:long-short-term-memory
type: Architecture
title: Long short-term memory
aliases: [LSTM, LSTM network, long short-term memory network]
domain: deep-learning
summary: >-
  A gated recurrent neural network architecture whose memory cell carries an additively updated internal
  state, regulated by input, forget and output gates, so that error signals can flow across hundreds or
  thousands of time steps without vanishing.
maturity: established
broader: [kt:recurrent-neural-network, kt:deep-learning]
related: [kt:backpropagation, kt:transformer-architecture, kt:automatic-speech-recognition, kt:sequence-to-sequence-learning, kt:dropout]
relations:
  - {predicate: introducedIn, object: kt:long-short-term-memory-1997}
  - {predicate: createdBy, object: kt:sepp-hochreiter}
  - {predicate: createdBy, object: kt:juergen-schmidhuber}
  - {predicate: mitigates, object: kt:vanishing-gradient-problem}
  - {predicate: supersededBy, object: kt:transformer-architecture}
  - {predicate: implementedIn, object: kt:pytorch}
sources:
  - id: s1
    title: "Long Short-Term Memory"
    publisher: Neural Computation 9(8):1735–1780 (1997) (Hochreiter and Schmidhuber), via ML Anthology
    url: https://mlanthology.org/neco/1997/hochreiter1997neco-long
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s2
    title: "Learning to Forget: Continual Prediction with LSTM"
    publisher: Neural Computation 12:2451–2471 (2000) (Gers, Schmidhuber and Cummins), via ML Anthology
    url: https://mlanthology.org/neco/2000/gers2000neco-learning
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s3
    title: "10.1. Long Short-Term Memory (LSTM)"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola)
    url: https://d2l.ai/chapter_recurrent-modern/lstm.html
    type: textbook
    accessed: 2026-11-10
  - id: s4
    title: "LSTM: A Search Space Odyssey"
    publisher: arXiv:1503.04069v2; IEEE Transactions on Neural Networks and Learning Systems (Greff, Srivastava, Koutník, Steunebrink and Schmidhuber)
    url: https://arxiv.org/abs/1503.04069v2
    type: primary
    accessed: 2026-11-10
  - id: s5
    title: "torch.nn.LSTM"
    publisher: PyTorch documentation (main)
    url: https://docs.pytorch.org/docs/main/generated/torch.nn.LSTM.html
    type: official-docs
    accessed: 2026-11-10
  - id: s6
    title: "xLSTM: Extended Long Short-Term Memory"
    publisher: NeurIPS 2024 (Beck, Pöppel, Spanring, Auer, Prudnikova, Kopp, Klambauer, Brandstetter and Hochreiter)
    url: https://proceedings.neurips.cc/paper_files/paper/2024/hash/c2ce2f2701c10a2b2f2ea0bfa43cfaa3-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-10
created: 2026-11-10
---

# Long short-term memory

Long short-term memory (LSTM) is a recurrent neural network (RNN) architecture designed to learn dependencies that span long gaps in a sequence. Sepp Hochreiter and Jürgen Schmidhuber introduced it in *Neural Computation* in 1997, arguing that ordinary recurrent backpropagation learns very slowly over long intervals because the error signal decays as it is propagated back through time. Their remedy was a special memory unit whose error flow is kept roughly constant, guarded by multiplicative gates; they reported bridging lags of more than 1,000 discrete time steps with per-step cost linear in the number of weights.[^s1]

## Origin and the vanishing-gradient problem

Simple Elman-style RNNs trained by backpropagation through time were in use by 1990, and it soon became clear that they struggled with long-range dependencies because gradients either vanish or explode as they are multiplied across many steps. Hochreiter analysed this problem in his 1991 diploma thesis, written in German, before the 1997 LSTM paper proposed one of the first successful fixes.[^s3] The original design centred on what the authors called a constant error carousel: a self-connected unit inside each memory cell through which error can circulate without being repeatedly scaled down, with input and output gates learning when to write to and read from it.[^s1]

The forget gate, now considered part of the standard cell, came later. Gers, Schmidhuber and Cummins showed in 2000 that the original LSTM failed on continual input streams with no marked sequence boundaries, because the internal state could grow without bound when it was never reset. Adding an adaptive forget gate let each cell learn when to clear its own state, and the modified network solved continual versions of benchmark tasks that every earlier method, including the original LSTM, failed.[^s2]

## How it works

At time step *t*, with input **x**ₜ and previous hidden state **h**ₜ₋₁, a modern LSTM layer computes three sigmoid gates (input **i**ₜ, forget **f**ₜ, output **o**ₜ) and a tanh candidate **g**ₜ, each an affine function of **x**ₜ and **h**ₜ₋₁. The cell and hidden states are then updated as **c**ₜ = **f**ₜ ⊙ **c**ₜ₋₁ + **i**ₜ ⊙ **g**ₜ and **h**ₜ = **o**ₜ ⊙ tanh(**c**ₜ), where ⊙ is element-wise multiplication.[^s5] Because the gates lie between 0 and 1, a cell with forget gate near 1 and input gate near 0 simply carries its state forward unchanged; the gates thus learn when to preserve, overwrite or expose memory. Only **h**ₜ is passed to the output layer, while **c**ₜ stays internal to the cell.[^s3]

The additive cell update is the key design choice: gradients flowing along the cell path are scaled by the forget gate rather than by a repeated weight-matrix product, which is why LSTMs keep useful gradient signal over far longer spans than plain RNNs.[^s3]

## Evidence, variants and limitations

Many gate variants have been proposed. A large-scale study by Greff and colleagues compared eight LSTM variants on speech recognition, handwriting recognition and polyphonic music modelling across 5,400 runs (roughly 15 CPU-years). None meaningfully beat the standard ("vanilla") LSTM, and the forget gate and the output activation function emerged as the most critical components; hyperparameters were found to be largely independent, which simplifies tuning.[^s4]

The main limitation is sequential computation: each step depends on the previous hidden state, so training cannot be parallelised across time the way self-attention can. LSTMs became prominent after winning prediction competitions in the mid-2000s and, in the *Dive into Deep Learning* authors' account, were the dominant sequence model from 2011 until the Transformer arrived in 2017.[^s3] Work on the architecture continues: xLSTM (NeurIPS 2024), from a team including Hochreiter, adds exponential gating with normalisation, a scalar-memory sLSTM cell and a fully parallelisable matrix-memory mLSTM cell; its authors report that it compares favourably with Transformers and state space models in performance and scaling, a claim that awaits broad independent replication.[^s6]

## In practice

LSTMs remain a standard building block in deep-learning frameworks. PyTorch's `torch.nn.LSTM` supports stacking (`num_layers`), bidirectional processing, dropout between stacked layers and an optional projection of the hidden state (`proj_size`), and returns the per-step outputs together with the final hidden and cell states for each layer and direction.[^s5] Because an LSTM summarises everything seen so far in fixed-size hidden and cell states, its memory per step stays constant regardless of sequence length; the xLSTM work instead targets the sequential bottleneck, making its matrix-memory variant fully parallelisable.[^s5][^s6]

## Connections

LSTM is a specialised **recurrent neural network** and a core architecture of **deep learning**; it is trained with **backpropagation** through time and was created by **Sepp Hochreiter** and **Jürgen Schmidhuber** in the 1997 paper it is introduced in.[^s1] Its purpose is to mitigate the **vanishing-gradient problem**.[^s3] Speech recognition was one of the benchmark domains in the largest comparative study of LSTM variants, linking it to **automatic speech recognition**; as the dominant sequence model of the 2010s it is also tied to **sequence-to-sequence learning**.[^s3] Stacked LSTMs are commonly regularised with **dropout** between layers, as PyTorch implements.[^s4][^s5] For most large-scale language work the **Transformer architecture** has superseded them, though xLSTM revisits the design as a scalable alternative.[^s3][^s6]

## Sources
[^s1]: Hochreiter and Schmidhuber, "Long Short-Term Memory", *Neural Computation* 9(8):1735–1780, 1997 (doi:10.1162/NECO.1997.9.8.1735). https://mlanthology.org/neco/1997/hochreiter1997neco-long (accessed 2026-11-10)
[^s2]: Gers, Schmidhuber and Cummins, "Learning to Forget: Continual Prediction with LSTM", *Neural Computation* 12:2451–2471, 2000. https://mlanthology.org/neco/2000/gers2000neco-learning (accessed 2026-11-10)
[^s3]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, section 10.1 "Long Short-Term Memory (LSTM)". https://d2l.ai/chapter_recurrent-modern/lstm.html (accessed 2026-11-10)
[^s4]: Greff, Srivastava, Koutník, Steunebrink and Schmidhuber, "LSTM: A Search Space Odyssey", arXiv:1503.04069v2 (IEEE TNNLS). https://arxiv.org/abs/1503.04069v2 (accessed 2026-11-10)
[^s5]: PyTorch documentation, "torch.nn.LSTM". https://docs.pytorch.org/docs/main/generated/torch.nn.LSTM.html (accessed 2026-11-10)
[^s6]: Beck et al., "xLSTM: Extended Long Short-Term Memory", NeurIPS 2024. https://proceedings.neurips.cc/paper_files/paper/2024/hash/c2ce2f2701c10a2b2f2ea0bfa43cfaa3-Abstract.html (accessed 2026-11-10)
