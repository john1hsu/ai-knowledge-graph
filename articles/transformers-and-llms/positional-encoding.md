---
id: kt:positional-encoding
type: Technique
title: Positional encoding
aliases: [position encoding, positional embedding, position embedding, sinusoidal positional encoding]
domain: transformers-and-llms
summary: >-
  A technique for giving a transformer information about token order, which self-attention cannot see on its own,
  either by adding absolute position vectors (sinusoidal or learned) to the input embeddings or by building relative
  offsets into the attention computation, as in relative position representations, rotary embeddings (RoPE) and ALiBi.
maturity: established
broader: [kt:transformer-architecture]
related: [kt:self-attention, kt:context-window, kt:embeddings, kt:large-language-model]
relations:
  - {predicate: introducedIn, object: kt:attention-is-all-you-need}
  - {predicate: hasPart, object: kt:rotary-position-embedding}
  - {predicate: hasPart, object: kt:alibi}
  - {predicate: hasPart, object: kt:relative-position-representations}
  - {predicate: enables, object: kt:context-window}
sources:
  - id: s1
    title: "Attention is All you Need"
    publisher: NeurIPS 2017, Advances in Neural Information Processing Systems 30 (Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin)
    url: https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Self-Attention with Relative Position Representations"
    publisher: NAACL-HLT 2018, Volume 2 (Short Papers), pp. 464–468 (Shaw, Uszkoreit, Vaswani)
    url: https://aclanthology.org/N18-2074/
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "RoFormer: Enhanced Transformer with Rotary Position Embedding"
    publisher: arXiv:2104.09864 (Su, Lu, Pan, Murtadha, Wen, Liu), 2021, revised 2023
    url: https://arxiv.org/abs/2104.09864v5
    type: primary
    accessed: 2026-11-16
  - id: s4
    title: "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation"
    publisher: ICLR 2022, authors' arXiv version 2108.12409 (Press, Smith, Lewis)
    url: https://arxiv.org/pdf/2108.12409
    type: primary
    accessed: 2026-11-16
  - id: s5
    title: "Extending Context Window of Large Language Models via Positional Interpolation"
    publisher: arXiv:2306.15595v2 (Chen, Wong, Chen, Tian; Meta), 2023
    url: https://arxiv.org/html/2306.15595v2
    type: primary
    accessed: 2026-11-16
  - id: s6
    title: "11.6. Self-Attention and Positional Encoding"
    publisher: Dive into Deep Learning (d2l.ai), version 1.0.3
    url: https://d2l.ai/chapter_attention-mechanisms-and-transformers/self-attention-and-positional-encoding.html
    type: textbook
    accessed: 2026-11-16
created: 2026-11-16
---

# Positional encoding

**Positional encoding** is how a transformer learns where each token sits in a sequence. Self-attention processes all tokens in parallel and, by itself, does not preserve their order, so a model without position information would treat a sentence and any shuffle of its words alike.[^s6] Because the original Transformer had no recurrence or convolution to supply order, Vaswani et al. added positional encodings of the same dimension as the token embeddings and summed the two at the bottom of the encoder and decoder stacks.[^s1] Later work moved position information out of the input and into the attention scores themselves.[^s2][^s3][^s4]

## How it works

**Sinusoidal (absolute, fixed).** The 2017 Transformer assigns position *pos* a vector whose dimensions are sines and cosines of different frequencies: PE(pos, 2i) = sin(pos / 10000^(2i/d)) and PE(pos, 2i+1) = cos(pos / 10000^(2i/d)), with wavelengths forming a geometric progression from 2π to 10000·2π.[^s1] The textbook *Dive into Deep Learning* compares this to binary counting: low dimensions oscillate quickly and high ones slowly, like low and high bits, but as continuous values.[^s6] For any fixed offset k, the encoding at pos+k is a linear function of the encoding at pos, which the authors hoped would make attending by relative position easy to learn.[^s1][^s6]

**Learned (absolute).** A trainable vector per position works too: Vaswani et al. found learned embeddings gave nearly identical results, but kept sinusoids in the hope that they would extrapolate to sequences longer than those seen in training.[^s1]

**Relative position representations.** Shaw, Uszkoreit and Vaswani extended self-attention to account for the distance between elements rather than their absolute indices. On WMT 2014 translation this beat absolute encodings by 1.3 BLEU (English–German) and 0.3 BLEU (English–French), and adding absolute encodings on top gave no further gain.[^s2]

**Rotary position embedding (RoPE).** Su et al. rotate each two-dimensional slice of the query and key vectors by an angle proportional to the token's position. Because both sides are rotated, their dot product depends only on the offset m − n, so an absolute encoding yields a relative attention pattern; the authors also report decaying dependency with distance and compatibility with linear attention.[^s3]

**ALiBi.** Press, Smith and Lewis drop position embeddings entirely and instead subtract a fixed, non-learned penalty proportional to query–key distance from each attention score, with a different slope per head (for eight heads, 1/2 through 1/2^8).[^s4]

## Limitations and open questions

The extrapolation hoped for in 2017 largely did not materialise. In the ALiBi paper's WikiText-103 experiments, a sinusoidal model trained on 512 tokens improved for only about 20 extra tokens before degrading; rotary embeddings stretched this to roughly 200, and the T5 relative bias further, but at least twice as slow to train.[^s4] ALiBi models trained on 1,024 tokens matched sinusoidal models trained on 2,048 (8.92 vs 9.01 perplexity at 1.3B parameters) while using less memory, the authors report.[^s4] For RoPE models, Chen et al. showed that running past the trained length can produce very large attention scores and perplexity above 10³; their *position interpolation* rescales position indices to fit the original window and extended LLaMA models from 2,048 to 32,768 tokens with under 1,000 fine-tuning steps.[^s5] How best to reach very long contexts without such patches remains an active research question.[^s4][^s5]

## In practice

The original Transformer used fixed sinusoidal encodings, and learned or fixed absolute encodings remain the textbook default.[^s1][^s6] Meta's LLaMA models (7B to 65B, as of 2023) are RoPE-based, which is why context-extension methods such as position interpolation were designed around RoPE.[^s5] RoFormer itself is available in Hugging Face Transformers.[^s3] ALiBi targets the "train short, test long" setting: its authors report training and inference speeds within 1% and 3% of sinusoidal encodings, adding at most about 100 MB of memory.[^s4]

## Connections

Positional encoding is a component of the **transformer architecture** (broader) and was **introduced in** *Attention Is All You Need*.[^s1] It exists to compensate for the order-blindness of **self-attention**,[^s6] and it is combined with token **embeddings** at the model input in the absolute variants.[^s1] Its main families, **relative position representations**, **rotary position embedding** and **ALiBi**, are parts of this topic.[^s2][^s3][^s4] The choice of scheme largely determines how far a model's **context window** can be stretched, which matters most for **large language models**.[^s4][^s5]

## Sources

[^s1]: Vaswani et al., "Attention is All you Need", NeurIPS 2017. https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf (accessed 2026-11-16)
[^s2]: Shaw, Uszkoreit, Vaswani, "Self-Attention with Relative Position Representations", NAACL-HLT 2018. https://aclanthology.org/N18-2074/ (accessed 2026-11-16)
[^s3]: Su et al., "RoFormer: Enhanced Transformer with Rotary Position Embedding", arXiv:2104.09864. https://arxiv.org/abs/2104.09864v5 (accessed 2026-11-16)
[^s4]: Press, Smith, Lewis, "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation", ICLR 2022. https://arxiv.org/pdf/2108.12409 (accessed 2026-11-16)
[^s5]: Chen, Wong, Chen, Tian, "Extending Context Window of Large Language Models via Positional Interpolation", arXiv:2306.15595. https://arxiv.org/html/2306.15595v2 (accessed 2026-11-16)
[^s6]: Dive into Deep Learning, §11.6 "Self-Attention and Positional Encoding". https://d2l.ai/chapter_attention-mechanisms-and-transformers/self-attention-and-positional-encoding.html (accessed 2026-11-16)
