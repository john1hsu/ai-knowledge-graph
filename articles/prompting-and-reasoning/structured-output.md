---
id: kt:structured-output
type: Technique
title: Structured output
aliases: [structured outputs, structured generation, guided generation, JSON mode, schema-constrained generation]
domain: prompting-and-reasoning
summary: >-
  The practice of making a language model emit text in a machine-readable format, such as JSON that
  validates against a given JSON Schema or a string accepted by a formal grammar, typically enforced by
  masking disallowed tokens during decoding rather than by prompting alone.
maturity: established
broader: [kt:prompt-engineering]
related: [kt:tool-use, kt:sampling-temperature-and-top-p, kt:chain-of-thought, kt:function-calling]
relations:
  - {predicate: basedOn, object: kt:constrained-decoding}
  - {predicate: dependsOn, object: kt:tokenization}
  - {predicate: implementedIn, object: kt:outlines}
  - {predicate: evaluatedOn, object: kt:jsonschemabench}
  - {predicate: enables, object: kt:tool-use}
sources:
  - id: s1
    title: "Efficient Guided Generation for Large Language Models"
    publisher: arXiv 2307.09702v4 (Willard and Louf, Normal Computing)
    url: https://arxiv.org/pdf/2307.09702
    type: primary
    accessed: 2026-11-14
  - id: s2
    title: "Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning"
    publisher: EMNLP 2023 (Geng, Josifoski, Peyrard, West)
    url: https://aclanthology.org/2023.emnlp-main.674
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "Structured model outputs"
    publisher: OpenAI API documentation
    url: https://developers.openai.com/api/docs/guides/structured-outputs.md
    type: official-docs
    accessed: 2026-11-14
  - id: s4
    title: "Let Me Speak Freely? A Study on the Impact of Format Restrictions on Large Language Model Performance"
    publisher: EMNLP 2024 Industry Track (Tam, Wu, Tsai, Lin, Lee, Chen)
    url: https://aclanthology.org/2024.emnlp-industry.91
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models"
    publisher: arXiv 2501.10868v3 (Geng, Cooper, Moskal, et al.; Microsoft, EPFL)
    url: https://arxiv.org/html/2501.10868v3
    type: primary
    accessed: 2026-11-14
created: 2026-11-14
---

# Structured output

**Structured output** (also called structured or guided generation) means getting a large language model to produce text that downstream software can parse without guesswork: JSON that conforms to a supplied JSON Schema, XML, a regular-expression pattern, or any string in a formal grammar. Asking for a format in the prompt works most of the time, but free-running models still emit stray prose, missing fields or broken brackets. Production systems therefore enforce the format at decoding time, so that the model can only sample tokens that keep the output valid.[^s1][^s3]

## How it works

An autoregressive model chooses each token from a probability distribution over its whole vocabulary. Constrained (guided) decoding inserts a step before sampling: it computes which next tokens would still allow the partial output to be completed into a valid string, sets the probability of every other token to zero, and renormalises. Sampling settings such as temperature still apply, but only within the allowed set.[^s1]

The practical difficulty is speed. Naively checking every vocabulary entry against the format at every step costs time proportional to the vocabulary size. Brandon Willard and Rémi Louf (2023) reframed the problem as transitions in a finite-state machine: a regular expression (or a JSON Schema compiled to one) becomes an automaton, and an index built before generation maps each automaton state to the vocabulary tokens it accepts. Generation then becomes a lookup that the authors describe as constant-cost on average per token, with context-free grammars handled through pushdown-automaton parsing. Their method shipped in the open-source Outlines library; they note the index costs memory, about 50 MB for a slightly extended Python grammar in their tests.[^s1]

Saibo Geng and colleagues at EPFL showed at EMNLP 2023 that grammar-constrained decoding generalises well beyond code and parsing. Their *input-dependent grammars* let the allowed output space change with each input, and on information extraction, entity disambiguation and constituency parsing, constrained models clearly beat unconstrained ones and in some cases beat task-specific fine-tuned models, which makes the approach attractive when training data is scarce.[^s2]

## In practice

Hosted APIs expose the technique as a request option. In OpenAI's API, *Structured Outputs* is turned on by passing a JSON Schema with strict mode enabled; the documentation (accessed November 2026) distinguishes it from the older *JSON mode*, which guarantees syntactically valid JSON but not adherence to a schema. The same documentation lists caveats that apply to most implementations: the first request with a new schema is slower while it is processed, a safety refusal may not follow the schema, outputs truncated by a token limit are incomplete, and business rules the schema cannot express still need application-side validation.[^s3]

Coverage of the JSON Schema language varies widely. JSONSchemaBench, released in early 2025 by researchers from Microsoft and EPFL, collected about 10,000 real-world schemas and compared Guidance, Outlines, llama.cpp, XGrammar and the OpenAI and Gemini APIs. Guidance had the widest coverage on most datasets; the closed APIs had the lowest coverage but very high compliance, which the authors attribute to supporting only a conservative subset of schema features. XGrammar showed the most under-constrained failures, accepting outputs that should have been rejected.[^s5]

## Limitations and open questions

Whether constraints hurt answer quality is debated. Tam et al. (EMNLP 2024 Industry Track) found that forcing formats such as JSON was associated with a notable drop in reasoning performance, and that stricter constraints tended to hurt more.[^s4] The JSONSchemaBench authors, using their own setups, reported the opposite on three reasoning tasks, with every constrained engine slightly ahead of an unconstrained baseline and Guidance roughly 3% better.[^s5] Structured output also guarantees form, not correctness: OpenAI's guidance is to keep validating values and business rules in application code.[^s3]

## Connections

Structured output is a branch of `kt:prompt-engineering` that moves format control from the prompt into the decoder; its mechanism is `kt:constrained-decoding`, and it interacts with `kt:tokenization` because token boundaries rarely align with grammar symbols, which is why the token index in Outlines (`kt:outlines`) is needed.[^s1] It underpins `kt:tool-use` and `kt:function-calling`, where a model must emit arguments that match a tool's schema, and it filters the distribution shaped by `kt:sampling-temperature-and-top-p`.[^s3] Its tension with step-by-step reasoning links it to `kt:chain-of-thought`, and its engines are compared on `kt:jsonschemabench`.[^s4][^s5]

## Sources

[^s1]: Willard and Louf, "Efficient Guided Generation for Large Language Models", arXiv 2307.09702v4, 2023. https://arxiv.org/pdf/2307.09702 (accessed 2026-11-14)
[^s2]: Geng, Josifoski, Peyrard and West, "Grammar-Constrained Decoding for Structured NLP Tasks without Finetuning", EMNLP 2023, pp. 10932–10952. https://aclanthology.org/2023.emnlp-main.674 (accessed 2026-11-14)
[^s3]: OpenAI, "Structured model outputs", API documentation. https://developers.openai.com/api/docs/guides/structured-outputs.md (accessed 2026-11-14)
[^s4]: Tam et al., "Let Me Speak Freely? A Study on the Impact of Format Restrictions on Large Language Model Performance", EMNLP 2024 Industry Track, pp. 1218–1236. https://aclanthology.org/2024.emnlp-industry.91 (accessed 2026-11-14)
[^s5]: Geng et al., "JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models", arXiv 2501.10868v3, 2025. https://arxiv.org/html/2501.10868v3 (accessed 2026-11-14)
