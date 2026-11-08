---
id: kt:speculative-decoding
type: Technique
title: Speculative decoding
aliases: [speculative sampling, assisted generation, assisted decoding, draft-and-verify decoding]
domain: inference-and-optimization
summary: >-
  An inference technique that speeds up autoregressive generation by letting a cheap draft mechanism propose
  several tokens that the large target model then verifies in a single parallel forward pass, using a
  rejection-sampling rule that leaves the target model's output distribution unchanged.
maturity: established
broader: [kt:llm-inference-optimization]
related: [kt:large-language-model, kt:quantization, kt:kv-cache, kt:model-serving]
relations:
  - {predicate: introducedIn, object: kt:fast-inference-from-transformers-via-speculative-decoding}
  - {predicate: usedIn, object: kt:large-language-model}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: implementedIn, object: kt:vllm}
  - {predicate: enables, object: kt:model-serving}
  - {predicate: alternativeTo, object: kt:quantization}
sources:
  - id: s1
    title: "Fast Inference from Transformers via Speculative Decoding"
    publisher: ICML 2023, PMLR 202:19274–19286 (Leviathan, Kalman and Matias)
    url: https://proceedings.mlr.press/v202/leviathan23a.html
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s2
    title: "Fast Inference from Transformers via Speculative Decoding (authors' arXiv version)"
    publisher: Leviathan, Kalman and Matias, arXiv 2211.17192
    url: https://arxiv.org/pdf/2211.17192
    type: primary
    accessed: 2026-11-08
  - id: s3
    title: "Accelerating Large Language Model Decoding with Speculative Sampling"
    publisher: Chen, Borgeaud, Irving, Lespiau, Sifre and Jumper (DeepMind), arXiv 2302.01318 (2023)
    url: https://arxiv.org/abs/2302.01318v1
    type: primary
    accessed: 2026-11-08
  - id: s4
    title: "Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads"
    publisher: ICML 2024, PMLR 235:5209–5235 (Cai, Li, Geng, Peng, Lee, Chen and Dao)
    url: https://proceedings.mlr.press/v235/cai24b
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s5
    title: "Assisted decoding"
    publisher: Hugging Face Transformers documentation
    url: https://huggingface.co/docs/transformers/assisted_decoding
    type: official-docs
    accessed: 2026-11-08
  - id: s6
    title: "Speculative Decoding"
    publisher: vLLM documentation
    url: https://docs.vllm.ai/usage/speculative_decoding/
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# Speculative decoding

**Speculative decoding** accelerates text generation from autoregressive models such as transformer language models. Normally, producing *K* tokens takes *K* sequential forward passes of the large model. Speculative decoding instead has a cheaper "draft" (or approximation) model guess several upcoming tokens, then runs the large "target" model once over all of the guesses in parallel and keeps the prefix it agrees with.[^s1] Its key property is that it is exact: a modified rejection-sampling step guarantees that the tokens produced follow the target model's distribution, so it needs no retraining and no change to the model's outputs.[^s2] The idea was published independently by Leviathan, Kalman and Matias at Google (arXiv, November 2022; ICML 2023) and by Chen and colleagues at DeepMind (February 2023), who called it *speculative sampling*.[^s1][^s3]

## How it works

The method rests on the observation that large-model decoding is usually limited by memory bandwidth, not arithmetic: scoring a short continuation of several tokens in one pass takes about as long as generating a single token.[^s3] Each iteration has three steps.[^s2]

1. **Draft.** The approximation model *q* autoregressively proposes γ tokens.[^s2]
2. **Verify.** The target model *p* scores all γ + 1 positions in one parallel forward pass.[^s2]
3. **Accept or reject.** For each drafted token *x* in order: if q(x) ≤ p(x), keep it; otherwise reject it with probability 1 − p(x)/q(x). At the first rejection, sample a replacement from the residual distribution norm(max(0, p − q)) and stop; if all γ guesses survive, sample one bonus token from *p*.[^s2]

Leviathan et al. prove that this procedure yields exactly the samples *p* would have produced.[^s2] Under greedy (argmax) decoding it reduces to keeping drafted tokens while they match the target's top choice.[^s2]

Speed depends on the **acceptance rate** α, the expected probability that a draft token is accepted. The paper shows that per-step acceptance equals one minus the total variation distance between *p* and *q*, so α measures how closely the draft imitates the target.[^s2] Treating acceptances as independent, the expected number of tokens per target-model call is (1 − α^(γ+1)) / (1 − α); with α = 0.8 and γ = 5 that is about 3.7 tokens, before accounting for the draft model's own cost.[^s2]

## Results and limitations

Using T5-small (77M parameters) to draft for T5-XXL (11B), Leviathan et al. measured about 3.4x speedup with greedy decoding and 2.6x with sampling on English–German translation, at batch size 1 on a TPU-v4; even a trivial bigram draft model gave around 1.25x.[^s2] Chen et al. reported a 2–2.5x decoding speedup for the 70B-parameter Chinchilla model in a distributed setup, without changing the model or sample quality.[^s3]

The speedup is not free. The target model evaluates positions that are later discarded, so total arithmetic rises as α falls, and the authors note the technique does not help when spare compute is unavailable.[^s2] In practice that makes it best suited to latency-sensitive, low-to-medium-traffic serving, where the GPU is memory-bound; under heavy batched load the spare compute disappears and gains shrink.[^s6] The draft must also be cheap yet well aligned: Hugging Face notes that a separate assistant works best when much smaller than the main model and sharing its tokenizer.[^s5] Exactness holds only up to floating-point precision, and some implementations offer explicitly lossy variants that relax verification to raise acceptance.[^s5][^s6]

## Variants

Later work removes the separate draft model. **Medusa** (ICML 2024) adds extra decoding heads to the target model that predict several future tokens, and verifies a tree of candidates at once with tree-structured attention; its authors report over 2.2x speedup when only the heads are trained (keeping outputs lossless) and 2.3–2.8x when heads and backbone are fine-tuned together.[^s4] Other drafters include **prompt lookup** (copying n-grams from the prompt, useful for summarization), **self-speculative** decoding via early exit from intermediate layers, and **multi-token prediction** layers built into checkpoints such as DeepSeek-V3.[^s5]

## In practice

As of November 2026, speculative decoding is a standard option in open-source inference stacks. Hugging Face Transformers exposes it through an `assistant_model` argument to `generate`, plus prompt lookup, early-exit, multi-token-prediction and cross-tokenizer ("universal") variants; the basic draft-model mode does not support batched inputs.[^s5] vLLM supports draft models, EAGLE, multi-token prediction, n-gram and suffix decoding, and describes its standard sampler as lossless up to hardware numerics; it advises measuring gains on one's own model, traffic and hardware.[^s6]

## Connections

Speculative decoding is a technique of **LLM inference optimization** and is used mainly for **large language models**, where sequential token generation dominates latency.[^s1][^s3] It was **introduced in** Leviathan et al.'s ICML 2023 paper.[^s1] It is complementary to, and an alternative lever to, **quantization**: quantization shrinks the cost of each forward pass, while speculative decoding reduces how many sequential target passes are needed.[^s2] Its efficiency argument depends on the **KV cache** and memory bandwidth, since the target's weights and cache are read once per verified block rather than once per token.[^s2] It is **implemented in** **Hugging Face Transformers** and **vLLM** and so enables lower-latency **model serving**.[^s5][^s6]

## Sources

[^s1]: Leviathan, Kalman and Matias, "Fast Inference from Transformers via Speculative Decoding", ICML 2023, PMLR 202. https://proceedings.mlr.press/v202/leviathan23a.html (accessed 2026-11-08)
[^s2]: Leviathan, Kalman and Matias, "Fast Inference from Transformers via Speculative Decoding", arXiv 2211.17192. https://arxiv.org/pdf/2211.17192 (accessed 2026-11-08)
[^s3]: Chen, Borgeaud, Irving, Lespiau, Sifre and Jumper, "Accelerating Large Language Model Decoding with Speculative Sampling", arXiv 2302.01318. https://arxiv.org/abs/2302.01318v1 (accessed 2026-11-08)
[^s4]: Cai et al., "Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads", ICML 2024, PMLR 235. https://proceedings.mlr.press/v235/cai24b (accessed 2026-11-08)
[^s5]: Hugging Face, "Assisted decoding", Transformers documentation. https://huggingface.co/docs/transformers/assisted_decoding (accessed 2026-11-08)
[^s6]: vLLM, "Speculative Decoding", vLLM documentation. https://docs.vllm.ai/usage/speculative_decoding/ (accessed 2026-11-08)
