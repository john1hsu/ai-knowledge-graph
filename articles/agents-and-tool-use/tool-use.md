---
id: kt:tool-use
type: Technique
title: Tool use
aliases: [function calling, tool calling, tool-augmented language models]
domain: agents-and-tool-use
summary: >-
  The capability of a language model to call external functions, APIs and programs: the model emits a structured
  request (a tool name plus arguments matching a declared schema), the application or provider executes it, and the
  result is fed back into the context so the model can continue or answer.
maturity: established
broader: [kt:large-language-model]
related: [kt:toolformer, kt:react-prompting, kt:model-context-protocol, kt:structured-output, kt:prompt-injection]
relations:
  - {predicate: enables, object: kt:ai-agent}
  - {predicate: influencedBy, object: kt:mrkl-systems}
  - {predicate: evaluatedOn, object: kt:berkeley-function-calling-leaderboard}
sources:
  - id: s1
    title: "MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning"
    publisher: arXiv 2205.00445 (Karpas et al., AI21 Labs; authors' version)
    url: https://arxiv.org/pdf/2205.00445
    type: primary
    accessed: 2026-11-12
  - id: s2
    title: "How tool use works"
    publisher: Anthropic, Claude Platform documentation
    url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works
    type: official-docs
    accessed: 2026-11-12
  - id: s3
    title: "Function calling"
    publisher: OpenAI API documentation
    url: https://developers.openai.com/api/docs/guides/function-calling
    type: official-docs
    accessed: 2026-11-12
  - id: s4
    title: "Gorilla: Large Language Model Connected with Massive APIs"
    publisher: Advances in Neural Information Processing Systems 37 (NeurIPS 2024), Patil, Zhang, Wang and Gonzalez
    url: https://proceedings.neurips.cc/paper_files/paper/2024/file/e4c61f578ff07830f5c37378dd3ecb0d-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s5
    title: "The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models"
    publisher: Proceedings of the 42nd International Conference on Machine Learning (ICML 2025), PMLR 267
    url: https://proceedings.mlr.press/v267/patil25a.html
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# Tool use

**Tool use**, usually exposed in APIs as **function calling** or **tool calling**, is the ability of a language model to invoke external software, such as a search engine, calculator, database, code interpreter or business API, instead of answering only from its parameters. A key design point is that the model does not run anything itself: it produces a structured request, the host application or the model provider executes the operation, and the output is returned to the conversation for the model to use.[^s2][^s3]

## Origin

The motivation was laid out clearly in AI21 Labs' 2022 MRKL (Modular Reasoning, Knowledge and Language) paper. Its authors argued that language models lack current information (dates, exchange rates, stock prices), cannot see proprietary data, and are unreliable at formal reasoning; they reported that GPT-3 and Jurassic-1 handled 2-digit addition but failed on 4-digit addition.[^s1] MRKL proposed a router that hands each input to the most suitable "expert" module, which could be neural (the general model or a smaller specialist) or symbolic (a calculator, currency converter or database API), with the general model as fallback.[^s1] In their calculator experiments, a 7B Jurassic model was trained only to extract operands and the operation from text while an actual calculator did the arithmetic; trained on single-digit problems, it generalized to numbers of up to nine digits with near-perfect accuracy for addition and multiplication.[^s1] Later work moved from hand-built routers to models that decide for themselves when to call a tool, either learned during training (as in Toolformer) or prompted, as in ReAct-style agents.

## How it works

Modern APIs share a common contract. The developer declares each tool with a name, a natural-language description of when to use it, and a JSON Schema for its arguments; the model sees only this schema, never the implementation.[^s2][^s3] A typical client-side loop runs as follows:[^s2][^s3]

1. The request includes the user's message and the list of tools.
2. The model replies with one or more tool calls, each with an identifier and arguments (Anthropic's API signals this with a `tool_use` stop reason).
3. The application executes each call and sends the outputs back, matched to the call identifiers.
4. The model either answers or issues further calls, and the loop repeats until it stops requesting tools.[^s2][^s3]

A single model turn may contain several calls at once (parallel tool calling), and each needs its own result.[^s2][^s3] OpenAI's documentation offers a `strict` flag on function definitions to enforce the declared schema, notes that tool definitions count as input tokens, and recommends keeping fewer than about 20 functions available at the start of a turn and offers deferred tool search for larger sets (as of November 2026).[^s3] Anthropic distinguishes client tools, which the developer executes, from server tools such as web search and code execution that Anthropic runs in its own internal loop.[^s2] Anthropic's guide also suggests a practical heuristic: if code is parsing a decision out of free text with a regular expression, that decision should probably be a tool call with a schema.[^s2]

## Limitations and evaluation

Models can call the wrong tool, invent arguments, or hallucinate APIs that do not exist. The Gorilla project at UC Berkeley addressed this by fine-tuning LLaMA-7B on APIBench, roughly 1,600 machine-learning APIs from Torch Hub, TensorFlow Hub and Hugging Face, with retrieved documentation in the training prompts so the model learns to use or ignore it.[^s4] Using abstract-syntax-tree matching to check calls, the authors reported zero-shot accuracy on Hugging Face APIs of about 72% for Gorilla versus about 20% for GPT-4, along with far lower hallucination rates (as of the 2024 paper).[^s4] The same group's Berkeley Function Calling Leaderboard (ICML 2025) evaluates serial and parallel calls, abstention and multi-turn stateful use. It found that state-of-the-art models do well on single-turn calls but still struggle with memory, dynamic decision-making and long-horizon reasoning.[^s5] Because tool outputs re-enter the context, untrusted content returned by a tool is also a channel for prompt injection, so tools with side effects warrant permission checks and human confirmation.

## Connections

Tool use is a capability layered on a **large language model**, which is why that node is its broader concept.[^s2] It **enables** the **AI agent**, whose loop of acting and observing is a repeated tool-calling loop.[^s2] It was **influenced by** the **MRKL** architecture's routing of queries to symbolic modules.[^s1] **Toolformer** is one specific method for teaching a model to use tools, and **ReAct** prompting interleaves reasoning traces with tool actions. The **Model Context Protocol** standardizes how tools are described and served to models, and schema-constrained calls (such as strict mode) overlap with **structured output**.[^s3] **Prompt injection** is the main security risk that tool results introduce, since returned text is read by the model as context. Function-calling ability is **evaluated on** the **Berkeley Function Calling Leaderboard**.[^s5]

## Sources

[^s1]: Karpas et al., "MRKL Systems: A modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning", AI21 Labs, arXiv 2205.00445, 2022. https://arxiv.org/pdf/2205.00445 (accessed 2026-11-12)
[^s2]: Anthropic, "How tool use works", Claude Platform documentation. https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works (accessed 2026-11-12)
[^s3]: OpenAI, "Function calling", OpenAI API documentation. https://developers.openai.com/api/docs/guides/function-calling (accessed 2026-11-12)
[^s4]: Patil, Zhang, Wang and Gonzalez, "Gorilla: Large Language Model Connected with Massive APIs", NeurIPS 2024. https://proceedings.neurips.cc/paper_files/paper/2024/file/e4c61f578ff07830f5c37378dd3ecb0d-Paper-Conference.pdf (accessed 2026-11-12)
[^s5]: Patil et al., "The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models", ICML 2025, PMLR 267. https://proceedings.mlr.press/v267/patil25a.html (accessed 2026-11-12)
