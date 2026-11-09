---
id: kt:sampling-temperature-and-top-p
type: Technique
title: Sampling temperature and top-p
aliases: [nucleus sampling, top-p sampling, temperature sampling, top-k sampling, decoding sampling parameters]
domain: inference-and-optimization
summary: >-
  Decoding controls for language models that reshape or truncate the next-token probability distribution before a
  token is drawn: temperature rescales the logits to make sampling more or less random, while top-p (nucleus) and
  top-k sampling restrict the draw to the most probable tokens.
maturity: established
broader: [kt:large-language-model]
related: [kt:self-consistency, kt:speculative-decoding, kt:knowledge-distillation, kt:hugging-face-transformers, kt:min-p-sampling]
relations:
  - {predicate: introducedIn, object: kt:the-curious-case-of-neural-text-degeneration}
  - {predicate: alternativeTo, object: kt:beam-search}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: usedIn, object: kt:self-consistency}
sources:
  - id: s1
    title: "The Curious Case of Neural Text Degeneration"
    publisher: ICLR 2020 (Holtzman, Buys, Du, Forbes, Choi); arXiv:1904.09751v2
    url: https://arxiv.org/pdf/1904.09751
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s2
    title: "Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs"
    publisher: ICLR 2025 (Nguyen, Baker, Neo, Roush, Kirsch, Shwartz-Ziv)
    url: https://proceedings.iclr.cc/paper_files/paper/2025/hash/afa5f124e36bed5cc2125067005d43f5-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s3
    title: "Generation strategies"
    publisher: Hugging Face Transformers documentation
    url: https://huggingface.co/docs/transformers/en/generation_strategies
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "Generation (GenerationConfig reference), Transformers v5.13.0"
    publisher: Hugging Face Transformers documentation
    url: https://huggingface.co/docs/transformers/v5.13.0/main_classes/text_generation
    type: official-docs
    accessed: 2026-11-09
  - id: s5
    title: "Claude Opus 5.5 migration guide"
    publisher: Anthropic, Claude Platform documentation
    url: https://platform.claude.com/docs/en/models/opus-5-5/migration-guide
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# Sampling temperature and top-p

A language model does not emit text directly; at each step it produces a probability distribution over its vocabulary, and a **decoding strategy** turns that distribution into a token. Deterministic strategies such as greedy search always take the most likely token, while stochastic strategies draw a token at random from the distribution.[^s3] **Temperature**, **top-k** and **top-p (nucleus) sampling** are the standard knobs for stochastic decoding: temperature reshapes the distribution, and top-k and top-p truncate its unreliable tail before the draw.[^s1]

## How it works

**Temperature.** Before the softmax, each logit is divided by a temperature *t*. With *t* < 1 the distribution sharpens, shifting mass toward already-likely tokens and shrinking the tail; with *t* > 1 it flattens, making unlikely tokens more probable. Holtzman et al. trace the idea back to Ackley et al. (1985) and note that lowering temperature tends to raise quality at the cost of diversity.[^s1] In the limit *t* → 0 the draw approaches greedy decoding.

**Top-k.** Sampling is restricted to the *k* most probable tokens, whose probabilities are renormalised to sum to one. It became popular for open-ended generation, including in the GPT-2 work.[^s1] Its weakness is that *k* is fixed: when the distribution is flat, a small *k* cuts off many reasonable continuations; when it is peaked, a large *k* lets implausible tokens back in.[^s1]

**Top-p (nucleus sampling).** Holtzman et al. instead keep the smallest set of tokens whose cumulative probability reaches a threshold *p*, renormalise within that set, and sample from it.[^s1] Because the nucleus grows and shrinks with the shape of the distribution, it adapts to the model's confidence at each step. For example, with *p* = 0.9, a step where one token holds 95% of the mass yields a nucleus of one token, while a step with many near-equal options keeps dozens.

## Why it matters and limitations

The motivating finding was that maximising likelihood at decode time produces bland, repetitive text even from strong models. In the paper's GPT-2 Large experiments, greedy decoding repeated itself in 73.66% of generations and beam search (width 16) in 28.94%, while pure unrestricted sampling instead wandered into incoherence because of the long low-probability tail.[^s1] Truncated sampling sits between these failure modes, and the authors report that nucleus sampling produced text closer to human text in diversity without losing fluency.[^s1]

Top-p is not the last word. Nguyen et al. argue that top-p struggles to balance quality and diversity at higher temperatures, and propose **min-p**, which sets the truncation threshold relative to the top token's probability; at ICLR 2025 they reported gains on GPQA, GSM8K and AlpacaEval creative writing across Mistral and Llama 3 models from 1B to 123B parameters (author-reported results).[^s2] More broadly, temperature and truncation trade off creativity against factual reliability, and no single setting suits every task.

## In practice

Open-source stacks expose these controls directly. In Hugging Face Transformers, greedy search is the default and sampling is enabled with `do_sample=True`.[^s3] As of Transformers v5.13 the `GenerationConfig` reference lists `temperature` (default 1.0), `top_k` (default 50) and `top_p` (default 1.0, meaning no nucleus truncation) when a model's own `generation_config.json` does not set them, alongside `min_p` and `typical_p`.[^s4] The min-p authors state that their method has been adopted by frameworks including Transformers and vLLM.[^s2]

Hosted APIs are moving in a different direction. As of November 2026, Anthropic's migration guide for Claude Opus 5.5 tells developers to omit `temperature`, `top_p` and `top_k`, lists their removal as a breaking change that began with Claude Opus 4.7, recommends prompting instead, and notes that temperature 0 never guaranteed identical outputs.[^s5] Practitioners should therefore check each provider's current parameter support rather than assume these knobs are universal.

## Connections

Sampling controls are a decoding-time property of a **large language model** (kt:large-language-model), the broader node. They are an **alternative to beam search** (kt:beam-search), whose likelihood-maximising behaviour the nucleus-sampling paper (kt:the-curious-case-of-neural-text-degeneration) criticised.[^s1] **Self-consistency** (kt:self-consistency) depends on sampling diverse reasoning paths, so temperature directly sets how varied its votes are. **Speculative decoding** (kt:speculative-decoding) must reproduce the target model's sampling distribution, and **knowledge distillation** (kt:knowledge-distillation) reuses the same softmax-temperature idea to soften teacher outputs. The parameters are implemented in **Hugging Face Transformers** (kt:hugging-face-transformers),[^s3][^s4] and **min-p sampling** (kt:min-p-sampling) is a newer truncation rule proposed as a successor.[^s2]

## Sources
[^s1]: Holtzman, Buys, Du, Forbes, Choi, "The Curious Case of Neural Text Degeneration", ICLR 2020. https://arxiv.org/pdf/1904.09751 (accessed 2026-11-09)
[^s2]: Nguyen et al., "Turning Up the Heat: Min-p Sampling for Creative and Coherent LLM Outputs", ICLR 2025. https://proceedings.iclr.cc/paper_files/paper/2025/hash/afa5f124e36bed5cc2125067005d43f5-Abstract-Conference.html (accessed 2026-11-09)
[^s3]: Hugging Face, "Generation strategies", Transformers documentation. https://huggingface.co/docs/transformers/en/generation_strategies (accessed 2026-11-09)
[^s4]: Hugging Face, "Generation" (GenerationConfig reference), Transformers v5.13.0 documentation. https://huggingface.co/docs/transformers/v5.13.0/main_classes/text_generation (accessed 2026-11-09)
[^s5]: Anthropic, "Claude Opus 5.5 migration guide", Claude Platform documentation. https://platform.claude.com/docs/en/models/opus-5-5/migration-guide (accessed 2026-11-09)
