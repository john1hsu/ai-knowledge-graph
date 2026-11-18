---
id: kt:decomposed-prompting
type: Technique
title: Decomposed prompting
aliases: [DecomP, DECOMP, modular prompting]
domain: prompting-and-reasoning
summary: >-
  A few-shot prompting technique in which a decomposer prompt writes a step-by-step program of sub-tasks
  and a controller routes each step to a dedicated handler (another prompt, a further decomposition, a
  trained model or a symbolic function such as retrieval), so complex tasks are solved by a library of
  simpler, separately tunable modules.
maturity: established
broader: [kt:prompt-engineering]
related: [kt:least-to-most-prompting, kt:chain-of-thought, kt:tool-use, kt:retrieval-augmented-generation, kt:agentic-workflow]
relations:
  - {predicate: introducedIn, object: kt:decomposed-prompting-a-modular-approach-for-solving-complex-tasks}
  - {predicate: createdBy, object: kt:allen-institute-for-ai}
  - {predicate: extends, object: kt:few-shot-prompting}
  - {predicate: evaluatedOn, object: kt:hotpotqa}
sources:
  - id: s1
    title: "Decomposed Prompting: A Modular Approach for Solving Complex Tasks"
    publisher: arXiv 2210.02406 (Khot, Trivedi, Finlayson, Fu, Richardson, Clark, Sabharwal)
    url: https://arxiv.org/pdf/2210.02406.pdf
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "Decomposed Prompting: A Modular Approach for Solving Complex Tasks (ICLR 2023 poster)"
    publisher: ICLR 2023
    url: https://iclr.cc/virtual/2023/poster/10871
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "The Prompt Report: A Systematic Survey of Prompting Techniques"
    publisher: arXiv 2406.06608v5 (Schulhoff, Ilie, Balepur, Kahadze, Liu, et al.)
    url: https://arxiv.org/html/2406.06608v5
    type: preprint
    accessed: 2026-11-18
  - id: s4
    title: "allenai/DecomP: code, datasets and prompts for Decomposed Prompting"
    publisher: Allen Institute for AI (GitHub)
    url: https://github.com/allenai/DecomP
    type: primary
    accessed: 2026-11-18
created: 2026-11-18
---

# Decomposed prompting

**Decomposed prompting** (DecomP) is a few-shot prompting method for tasks that are too complex, or whose individual steps are too hard, for a single prompt to teach reliably. Rather than asking one prompt to demonstrate an entire reasoning chain, DecomP splits the task into sub-tasks and assigns each to a dedicated handler, much as a program calls functions from a software library.[^s1] It was introduced by Tushar Khot, Harsh Trivedi, Matthew Finlayson, Yao Fu, Kyle Richardson, Peter Clark and Ashish Sabharwal, mostly of the Allen Institute for AI, and presented as a poster at ICLR 2023.[^s1][^s2] The authors argued that few-shot prompting degrades as task complexity grows, and that modularity lets each piece be optimized, decomposed further, or swapped for a better component.[^s2]

## How it works

A DecomP system has three parts.[^s1]

- **Decomposer.** A few-shot prompt whose exemplars show how to write a "prompting program": a sequence of sub-questions, each tagged with the sub-task that should answer it.[^s1]
- **Sub-task handlers.** Each sub-task can be an ordinary few-shot prompt, another decomposed prompt (giving hierarchy), or a non-LLM component such as a trained model, a calculator or a retrieval system.[^s1]
- **Controller.** A symbolic loop that passes each sub-question to its handler, feeds the answer back to the decomposer so it can write the next step, and stops when the decomposer emits an end marker.[^s1]

A worked example from the paper: asked to take the letters at a given position in each word of "Herbert Alexander Simon" and join them with spaces, the decomposer calls a `split` sub-task to get the words, a `str_pos` sub-task to pull each letter, and a `merge` sub-task to concatenate them.[^s1] Because finding the k-th letter is itself error-prone for an LLM, that handler can be decomposed again, into splitting a word into characters and then indexing the list (`arr_pos`).[^s1] Control operators such as a `foreach` loop and references to earlier answers (for example `#1`) keep the programs short.[^s1]

Two structural features distinguish DecomP from linear chains. The decomposer can call itself **recursively**, for instance reversing a long list by splitting it in half until each piece is small enough for a plain chain-of-thought prompt.[^s1] And **retrieval is just another handler**: in open-domain multi-hop QA, an Elasticsearch-backed sub-task returns an answer plus supporting paragraphs that later reading-comprehension sub-tasks consume.[^s1]

## Evidence

The paper evaluated mainly with GPT-3 (text-davinci-002), plus Codex and Flan-T5 models for open-domain QA.[^s1] On letter concatenation it outperformed chain-of-thought and least-to-most prompting and stayed close to perfect on longer inputs, where chain-of-thought accuracy declined.[^s1] On list reversal, recursive decomposition generalized to longer lists than its exemplars, whereas chain-of-thought did not.[^s1] On the synthetic long-context benchmark CommaQA-E, it beat chain-of-thought at both coarse and fine decomposition granularities and on a compositional-generalization split.[^s1] In open-domain QA over HotpotQA, 2WikiMultihopQA and MuSiQue, decomposition with retrieval beat a closed-book baseline everywhere and a single-retrieval baseline in most settings; with Codex on HotpotQA the two were roughly tied.[^s1] Delegating final-answer extraction to a separate GPT-3 handler raised GSM8K accuracy from 36 to 50.6 in the paper's appendix experiment.[^s1]

## Limitations

The method leans on large models: the authors used GPT-3-scale decomposers because they reliably produced the structured programs required.[^s1] Errors in individual sub-tasks, such as extracting the wrong letter or answering a single hop incorrectly, remained the main failure mode, and evaluations used subsets of a few hundred examples under 2,049-token context limits typical of 2022-era GPT-3.[^s1] Designing a good library of sub-tasks and exemplars is also manual work.[^s4]

## In practice

The authors released code, datasets and prompts under the Apache-2.0 license; experiments are driven by Jsonnet configs that select decomposition, chain-of-thought or unrolled baselines, while the open-domain QA pipeline lives in a companion repository.[^s4] The Prompt Report survey (v5) files DecomP under decomposition techniques alongside least-to-most, plan-and-solve and tree-of-thought prompting, describing it as teaching the model to use functions like string splitting or web search and reporting gains over least-to-most on some tasks.[^s3] Its pattern of a planner routing sub-calls to specialized prompts and tools anticipates the routing and orchestration designs common in later LLM applications.[^s1][^s3]

## Connections

DecomP is a technique within **prompt engineering** (`broader`) and `extends` **few-shot prompting**, since both the decomposer and most handlers are few-shot prompts.[^s1] It was `introducedIn` the ICLR 2023 paper and `createdBy` researchers at the **Allen Institute for AI**.[^s1][^s2] Its closest relative is **least-to-most prompting**: both break problems into sub-questions, but least-to-most proceeds from easiest to hardest and has the model answer the full question at the end, while DecomP allows recursion and other non-linear structures.[^s1][^s3] It contrasts with a single **chain-of-thought** prompt, which it uses as a base-case handler.[^s1] Calling calculators or retrievers as handlers links it to **tool use** and **retrieval-augmented generation**, and it was `evaluatedOn` **HotpotQA**.[^s1] Its decomposer-controller loop is an early instance of an **agentic workflow**.[^s3]

## Sources

[^s1]: Khot et al., "Decomposed Prompting: A Modular Approach for Solving Complex Tasks", arXiv 2210.02406. https://arxiv.org/pdf/2210.02406.pdf (accessed 2026-11-18)
[^s2]: "Decomposed Prompting: A Modular Approach for Solving Complex Tasks", ICLR 2023 poster. https://iclr.cc/virtual/2023/poster/10871 (accessed 2026-11-18)
[^s3]: Schulhoff et al., "The Prompt Report: A Systematic Survey of Prompting Techniques", arXiv 2406.06608v5. https://arxiv.org/html/2406.06608v5 (accessed 2026-11-18)
[^s4]: Allen Institute for AI, "allenai/DecomP" repository. https://github.com/allenai/DecomP (accessed 2026-11-18)
