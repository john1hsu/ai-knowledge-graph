---
id: kt:self-attention
type: Architecture
title: Self-attention
aliases: [intra-attention, scaled dot-product self-attention]
domain: transformers-and-llms
summary: >-
  An attention mechanism in which every position of a single sequence computes its new representation
  as a weighted sum over all positions of that same sequence, with weights derived from query-key
  similarity; it is the core layer of the transformer.
maturity: established
broader: [kt:attention-mechanism]
related: [kt:positional-encoding, kt:attention-is-all-you-need, kt:context-window, kt:kv-cache, kt:flash-attention, kt:mechanistic-interpretability]
relations:
  - {predicate: introducedIn, object: kt:long-short-term-memory-networks-for-machine-reading}
  - {predicate: partOf, object: kt:transformer-architecture}
  - {predicate: alternativeTo, object: kt:recurrent-neural-network}
  - {predicate: alternativeTo, object: kt:convolutional-neural-network}
sources:
  - id: s1
    title: "Attention is All you Need"
    publisher: Vaswani et al., Advances in Neural Information Processing Systems 30 (NIPS 2017)
    url: https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s2
    title: "11.6. Self-Attention and Positional Encoding"
    publisher: Zhang, Lipton, Li and Smola, Dive into Deep Learning (d2l.ai)
    url: https://d2l.ai/chapter_attention-mechanisms-and-transformers/self-attention-and-positional-encoding.html
    type: textbook
    accessed: 2026-11-13
  - id: s3
    title: "Long Short-Term Memory-Networks for Machine Reading"
    publisher: Cheng, Dong and Lapata, Proceedings of EMNLP 2016 (ACL Anthology D16-1053)
    url: https://aclanthology.org/D16-1053.pdf
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "Attention is not Explanation"
    publisher: Jain and Wallace, Proceedings of NAACL-HLT 2019 (ACL Anthology N19-1357)
    url: https://aclanthology.org/N19-1357/
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s5
    title: "Efficient Transformers: A Survey"
    publisher: Tay, Dehghani, Bahri and Metzler (Google Research), arXiv:2009.06732v3 (March 2022)
    url: https://arxiv.org/pdf/2009.06732
    type: primary
    accessed: 2026-11-13
created: 2026-11-13
---

# Self-attention

**Self-attention**, also called intra-attention, is an attention mechanism that relates the different positions of one sequence to each other in order to compute a representation of that sequence.[^s1] Given input tokens x₁ … xₙ, it produces an output sequence of the same length in which each output is an attention-weighted pooling over every token in the input: each token acts as a query against all tokens' keys, and its output is a weighted sum of their values.[^s2] It is the layer that lets a transformer mix information across positions without recurrence or convolution.[^s1]

## Origin

Attention between two sequences (for example, a decoder attending to an encoder in translation) came first; attending within a single sequence emerged around 2016. Cheng, Dong and Lapata's Long Short-Term Memory-Network (EMNLP 2016) replaced the LSTM's single memory cell with a tape holding one vector per earlier token, and at each step scored the current token against previous hidden states to form a softmax-weighted summary; the authors described these soft, differentiable links as weakly inducing relations among tokens.[^s3] Vaswani et al. note that self-attention had already been used for reading comprehension, summarization and textual entailment before their 2017 paper, which was the first to build a sequence transduction model from attention alone, dispensing with recurrence and convolution entirely.[^s1]

## How it works

The transformer's form is **scaled dot-product attention**. Queries Q, keys K and values V are all linear projections of the same input, and the output is softmax(QKᵀ / √dₖ)·V. The √dₖ scaling exists because for large key dimensions the dot products grow large and push the softmax into regions with extremely small gradients.[^s1] **Multi-head attention** runs several such attentions in parallel on lower-dimensional projections and concatenates the results; the original base model used 8 heads of dimension 64, at a total cost similar to one full-width head.[^s1]

The same mechanism appears in three roles in the original encoder-decoder transformer: encoder self-attention, where every position attends to every other; decoder self-attention, where a mask sets scores for future positions to −∞ before the softmax so that generation stays auto-regressive; and encoder-decoder (cross) attention, where queries come from the decoder but keys and values from the encoder output, which is not self-attention.[^s1] Decoder-only language models use only the masked (causal) form.

Self-attention is permutation-invariant on its own: shuffling the input tokens shuffles the outputs identically, so order information must be injected separately, typically by adding positional encodings (learned, or fixed sinusoidal) to the input embeddings.[^s2]

## Why it matters, and its costs

Vaswani et al. compared layer types for a sequence of length n and representation dimension d. A self-attention layer costs O(n²·d) per layer, needs O(1) sequential operations and connects any two positions in a path of length O(1); a recurrent layer costs O(n·d²) but needs O(n) sequential steps and has O(n) path length; a convolutional layer needs a stack of layers to link distant positions.[^s1][^s2] The constant path length helps the model learn long-range dependencies, and the lack of sequential steps makes training highly parallel on accelerators.[^s1]

The price is the quadratic term: time and memory grow with the square of sequence length, which limits long documents, high-resolution images and video.[^s5] The original paper already suggested restricting each position to a neighbourhood of size r, cutting cost to O(r·n·d) at the expense of an O(n/r) path length.[^s1] Tay et al.'s survey (v3, March 2022) catalogues the many "efficient transformer" responses, including fixed sparse patterns (Sparse Transformer, Longformer), learned patterns (Reformer), low-rank approximations (Linformer), kernel-based linear attention (Performer) and segment recurrence (Transformer-XL), and cautions that lower theoretical complexity does not always translate into faster wall-clock speed.[^s5]

A second open question is interpretability. Vaswani et al. observed that individual heads seemed to specialize and to track syntactic and semantic structure.[^s1] Jain and Wallace (NAACL 2019), however, found across several NLP tasks that learned attention weights often correlate poorly with gradient-based importance measures and that quite different attention distributions can yield the same prediction, so raw attention maps should not be read as faithful explanations.[^s4]

## Connections

Self-attention is a specialisation of the broader **attention mechanism** (kt:attention-mechanism) to a single sequence, and it is **part of** the **transformer architecture** (kt:transformer-architecture), which popularised it in *Attention Is All You Need* (kt:attention-is-all-you-need); its intra-attention precursor appeared in **Long Short-Term Memory-Networks for Machine Reading** (kt:long-short-term-memory-networks-for-machine-reading).[^s1][^s3] It is an **alternative to** the **recurrent** (kt:recurrent-neural-network) and **convolutional** (kt:convolutional-neural-network) layers it was benchmarked against.[^s1][^s2] Because it ignores order, it relies on **positional encoding** (kt:positional-encoding).[^s2] Its quadratic cost in sequence length bounds the practical **context window** (kt:context-window), motivates memory-aware kernels such as **FlashAttention** (kt:flash-attention) and the efficient-attention variants surveyed by Tay et al., and in causal decoding its keys and values are reused through the **KV cache** (kt:kv-cache).[^s5] Whether attention patterns explain model behaviour is a question taken up by **mechanistic interpretability** (kt:mechanistic-interpretability).[^s4]

## Sources

[^s1]: Vaswani et al., "Attention is All you Need", NIPS 2017. https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf (accessed 2026-11-13)
[^s2]: Zhang, Lipton, Li and Smola, "Self-Attention and Positional Encoding", *Dive into Deep Learning*. https://d2l.ai/chapter_attention-mechanisms-and-transformers/self-attention-and-positional-encoding.html (accessed 2026-11-13)
[^s3]: Cheng, Dong and Lapata, "Long Short-Term Memory-Networks for Machine Reading", EMNLP 2016. https://aclanthology.org/D16-1053.pdf (accessed 2026-11-13)
[^s4]: Jain and Wallace, "Attention is not Explanation", NAACL-HLT 2019. https://aclanthology.org/N19-1357/ (accessed 2026-11-13)
[^s5]: Tay, Dehghani, Bahri and Metzler, "Efficient Transformers: A Survey", arXiv:2009.06732v3, 2022. https://arxiv.org/pdf/2009.06732 (accessed 2026-11-13)
