---
id: kt:toolformer
type: Model
title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
aliases: [Toolformer]
domain: agents-and-tool-use
summary: >-
  A 2023 Meta AI method and model in which a language model (GPT-J, 6.7B parameters) annotates its own training text
  with candidate API calls, keeps only the calls whose results make the following tokens easier to predict, and is
  fine-tuned on the result, so it learns by self-supervision when and how to call a calculator, QA system, search
  engine, translator and calendar.
maturity: established
broader: [kt:tool-use]
related: [kt:ai-agent, kt:react-prompting, kt:retrieval-augmented-generation, kt:emergent-abilities, kt:star-self-taught-reasoner]
relations:
  - {predicate: basedOn, object: kt:gpt-j}
  - {predicate: createdBy, object: kt:meta-ai}
  - {predicate: trainedWith, object: kt:synthetic-data}
  - {predicate: dependsOn, object: kt:fine-tuning}
  - {predicate: influencedBy, object: kt:large-language-model}
sources:
  - id: s1
    title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
    publisher: arXiv 2302.04761 (Schick et al., Meta AI Research; authors' version)
    url: https://arxiv.org/pdf/2302.04761
    type: primary
    accessed: 2026-11-10
  - id: s2
    title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
    publisher: Advances in Neural Information Processing Systems 36 (NeurIPS 2023), Main Conference Track
    url: https://proceedings.neurips.cc/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s3
    title: "Augmented Language Models: a Survey"
    publisher: Meta AI Research (Mialon et al., TMLR 2023)
    url: https://ai.meta.com/research/publications/augmented-language-models-a-survey
    type: lab-research
    accessed: 2026-11-10
  - id: s4
    title: "Gorilla: Large Language Model Connected with Massive APIs"
    publisher: arXiv 2305.15334 (Patil et al., UC Berkeley and Microsoft Research; authors' version)
    url: https://arxiv.org/pdf/2305.15334
    type: primary
    accessed: 2026-11-10
  - id: s5
    title: "Tool use with Claude"
    publisher: Anthropic Claude Platform documentation
    url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# Toolformer: Language Models Can Teach Themselves to Use Tools

Toolformer is a language model, and the training recipe that produced it, that learns on its own which external tools to call, when to call them, what arguments to pass, and how to fold the returned results into its next-token predictions.[^s2] It was introduced in February 2023 by Timo Schick and colleagues at Meta AI Research (with a co-author from Universitat Pompeu Fabra) and published at NeurIPS 2023.[^s1][^s2] The motivating observation was that large models learn new tasks from a few examples yet still stumble on arithmetic, factual lookup and knowing today's date, where small specialised systems excel; Toolformer combines the two through plain-text API calls, needing only a handful of human-written demonstrations per tool.[^s2]

## How it works

Toolformer represents a tool call inline in ordinary text as `<API> tool(input) → result </API>`; in practice the markers are written with existing tokens such as brackets and an arrow, so the vocabulary does not change.[^s1] Building the training set takes three steps:[^s1]

1. **Sample.** A few-shot prompt asks the base model to propose API calls inside unlabelled text. Positions where the probability of opening a call exceeds a threshold (0.05 by default, top 5 positions) are kept, and up to 5 candidate calls are sampled at each.[^s1]
2. **Execute.** Each candidate is run against the real tool, which returns a single text string.[^s1]
3. **Filter.** A call survives only if inserting the call *and its result* lowers the weighted cross-entropy loss on the following tokens by at least a margin (1.0 by default, 0.5 for the calculator and translator) compared with making no call, or making the call without seeing its result.[^s1]

The surviving calls are spliced into the original documents and the model is fine-tuned with its usual language-modelling objective. Because the underlying text is unchanged, the authors report that perplexity on WikiText and CCNet is essentially unaffected when API calls are disabled.[^s1] At inference, decoding pauses whenever the model emits the arrow token, the tool is invoked, its output is inserted, and generation resumes.[^s1]

The paper used GPT-J (6.7B parameters) fine-tuned on a heuristically filtered subset of CCNet, with five tools: a question-answering model (Atlas), a four-operation Python calculator, a BM25 search engine over a Wikipedia dump, a 600M-parameter NLLB translation model, and a calendar that returns the current date.[^s1]

## Results and limitations

In zero-shot evaluation reported in the 2023 paper, Toolformer beat both OPT (66B) and GPT-3 (175B) on the LAMA fact-completion subsets, on the ASDiv, SVAMP and MAWPS maths word-problem sets, and on a temporal DATESET task; for example, it scored 40.4 on ASDiv against 14.0 for GPT-3.[^s1] It still trailed GPT-3 on open-domain QA benchmarks such as TriviaQA and Natural Questions, and its multilingual QA results were mixed.[^s1] Experiments with smaller GPT-2-family models suggested the ability to benefit from tools only appears at roughly 775M parameters and above.[^s1]

The authors list clear limits: tools cannot be chained because each tool's training calls are generated independently; the model cannot interact with a tool, for instance by browsing several search results or reformulating a query; whether it calls a tool is sensitive to the exact wording of the input; the filtering is sample-inefficient, with over a million documents yielding only a few thousand useful calculator examples; and it ignores the cost of each call.[^s1]

## Influence and practice

Toolformer became a reference point for the broader "augmented language model" agenda that a contemporaneous Meta AI survey (several authors overlap) framed as models that keep the next-token objective but call external, possibly non-parametric modules such as code interpreters.[^s3] Follow-up work such as Gorilla (UC Berkeley and Microsoft Research) cites Toolformer among early tool-use systems that focus on a few specific tools, and instead fine-tunes LLaMA-7B on retrieved API documentation to cover thousands of machine-learning APIs.[^s4] Production systems have since converged on a different interface: in current function-calling APIs, developers declare each tool with a name, description and JSON Schema, the model emits a structured tool-call block, and the application runs the tool and returns the result in the next turn, as in Anthropic's Claude documentation as of 2026.[^s5] Toolformer's lasting contribution is the idea that a model can generate and self-filter its own tool-use training data instead of relying on large human-annotated datasets.[^s1][^s2]

## Connections

Toolformer is a specific instance of **tool use** (`kt:tool-use`), the broader capability of models invoking external functions.[^s3] It is **based on GPT-J** and was **created by Meta AI**, and it is **trained with synthetic data** the model generates for itself before **fine-tuning**.[^s1] Its loss-based self-filtering parallels **STaR**, which likewise keeps only self-generated rationales that lead to correct answers. Its question-answering and search tools tie it to **retrieval-augmented generation**, its scale threshold relates to debates on **emergent abilities**, and its single-shot, non-interactive calls contrast with prompting-based **ReAct** loops and full **AI agents** that interleave reasoning, tool calls and observations over many steps.[^s1][^s3]

## Sources
[^s1]: Schick et al., "Toolformer: Language Models Can Teach Themselves to Use Tools", arXiv 2302.04761. https://arxiv.org/pdf/2302.04761 (accessed 2026-11-10)
[^s2]: Schick et al., "Toolformer: Language Models Can Teach Themselves to Use Tools", NeurIPS 2023. https://proceedings.neurips.cc/paper/2023/hash/d842425e4bf79ba039352da0f658a906-Abstract.html (accessed 2026-11-10)
[^s3]: Mialon et al., "Augmented Language Models: a Survey", Meta AI Research / TMLR 2023. https://ai.meta.com/research/publications/augmented-language-models-a-survey (accessed 2026-11-10)
[^s4]: Patil et al., "Gorilla: Large Language Model Connected with Massive APIs", arXiv 2305.15334. https://arxiv.org/pdf/2305.15334 (accessed 2026-11-10)
[^s5]: Anthropic, "Tool use with Claude", Claude Platform docs. https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview (accessed 2026-11-10)
