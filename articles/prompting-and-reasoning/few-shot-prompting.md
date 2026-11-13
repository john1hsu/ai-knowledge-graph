---
id: kt:few-shot-prompting
type: Technique
title: Few-shot prompting
aliases: [multishot prompting, k-shot prompting, prompting with demonstrations, example-based prompting]
domain: prompting-and-reasoning
summary: >-
  A prompting technique that places a small number of worked input-output examples (demonstrations) in a
  language model's prompt ahead of the real query, so the model infers the task, label set and output format
  from the examples without any weight update.
maturity: established
broader: [kt:prompt-engineering]
related: [kt:zero-shot-prompting, kt:prompt-sensitivity, kt:chain-of-thought, kt:semantic-search]
relations:
  - {predicate: introducedIn, object: kt:language-models-are-few-shot-learners}
  - {predicate: dependsOn, object: kt:in-context-learning}
  - {predicate: dependsOn, object: kt:context-window}
  - {predicate: alternativeTo, object: kt:fine-tuning}
sources:
  - id: s1
    title: "Language Models are Few-Shot Learners"
    publisher: arXiv 2005.14165 via ar5iv (Brown, Mann, Ryder, Subbiah, Kaplan, Dhariwal, et al.; NeurIPS 2020)
    url: https://ar5iv.labs.arxiv.org/html/2005.14165
    type: primary
    accessed: 2026-11-13
  - id: s2
    title: "What Makes Good In-Context Examples for GPT-3?"
    publisher: DeeLIO 2022 workshop, ACL, pp. 100-114 (Liu, Shen, Zhang, Dolan, Carin, Chen)
    url: https://aclanthology.org/2022.deelio-1.10
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s3
    title: "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?"
    publisher: EMNLP 2022, pp. 11048-11064 (Min, Lyu, Holtzman, Artetxe, Lewis, Hajishirzi, Zettlemoyer)
    url: https://aclanthology.org/2022.emnlp-main.759
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s4
    title: "Many-Shot In-Context Learning"
    publisher: NeurIPS 2024, vol. 37, pp. 76930-76966 (Agarwal, Singh, Zhang, Bohnet, et al.)
    url: https://papers.neurips.cc/paper_files/paper/2024/hash/8cb564df771e9eacbfe9d72bd46a24a9-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-13
  - id: s5
    title: "Prompting best practices: Use examples effectively"
    publisher: Anthropic, Claude Platform Docs
    url: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/multishot-prompting
    type: official-docs
    accessed: 2026-11-13
created: 2026-11-13
---

# Few-shot prompting

**Few-shot prompting** is the practice of writing a handful of solved examples (demonstrations) into a prompt before the real query, so that a pretrained language model picks up the task from the pattern rather than from training on it. The term was fixed by the 2020 GPT-3 paper, which defined three evaluation settings by how many demonstrations the prompt carries: *zero-shot* (an instruction only), *one-shot* (an instruction plus a single demonstration) and *few-shot* (K demonstrations of context and completion followed by one unanswered context). In every setting the model's weights stay frozen.[^s1] Vendors also call it *multishot prompting*.[^s5]

## How it works

A few-shot prompt is a template: an optional instruction, then K examples in an identical format, then the new input in that same format with its output left blank. A sentiment classifier, for example, might show three short reviews each followed by `Label: positive` or `Label: negative`, then a fourth review followed by `Label:`; the model completes the pattern. In the GPT-3 paper K typically ranged from 10 to 100, bounded by what fit into the model's 2,048-token context window.[^s1] The authors also reported that few-shot accuracy grew faster with model size than zero-shot accuracy, which is why the technique became associated with large models.[^s1]

What the demonstrations actually teach is narrower than it looks. Min et al. (EMNLP 2022) found that randomly replacing the gold labels in demonstrations barely hurt accuracy on classification and multiple-choice tasks across 12 models, including GPT-3. Their analysis attributes most of the benefit to three things the examples reveal: the label space, the distribution of input text, and the overall format of the sequence.[^s3] In practice, then, few-shot examples work largely as a specification of shape and vocabulary, which is also why vendor guidance stresses them for controlling output format, tone and structure.[^s5]

## Choosing and formatting examples

Which examples go in the prompt matters. Liu et al. showed that GPT-3's results depended heavily on the chosen demonstrations, and that retrieving examples semantically similar to each test query (via a sentence encoder) consistently beat random selection on several understanding and generation benchmarks, with the largest reported gains on table-to-text generation (ToTTo) and open-domain question answering (Natural Questions). Encoders fine-tuned on related tasks retrieved even more useful examples.[^s2] This turned example selection into a retrieval problem: production systems often keep a pool of labelled cases and pull the nearest neighbours of each incoming query into the prompt.[^s2]

Anthropic's documentation (as of November 2026) recommends three to five examples for best results, chosen to mirror the real use case, varied enough to cover edge cases without teaching unintended patterns, and wrapped in `<example>` tags so the model can tell them apart from instructions. It also notes that worked examples shape how the model reasons, not only what it outputs.[^s5]

## Limitations

Few-shot prompting spends context tokens on every call, and the demonstrations still have to be collected and maintained; the GPT-3 authors noted that its results at the time fell well short of state-of-the-art fine-tuned models.[^s1] Results also depend heavily on which demonstrations are chosen,[^s2] part of the broader brittleness treated under prompt sensitivity. Because demonstrations mostly convey format and label space, they are a weak tool for teaching genuinely new knowledge.[^s3]

Long context windows have stretched the technique. Agarwal et al. (NeurIPS 2024) studied a "many-shot" regime with hundreds or thousands of examples and found significant gains over few-shot prompting across many generative and discriminative tasks, performance that approached supervised fine-tuning, and an ability to override pretraining biases that few-shot prompts could not.[^s4] To reduce dependence on human-written outputs they proposed *Reinforced ICL*, which uses model-generated rationales as demonstrations, and *Unsupervised ICL*, which supplies only domain inputs. They also found next-token loss to be an unreliable predictor of downstream in-context performance.[^s4]

## Connections

Few-shot prompting is a core technique within **prompt engineering** and the practical counterpart of **in-context learning**: in-context learning is the model capability, while few-shot prompting is the deliberate act of exploiting it with demonstrations.[^s1] The number of examples it can use is bounded by the **context window**, and many-shot results show how larger windows change what it can do.[^s4] It contrasts with **zero-shot prompting**, which drops the demonstrations, and it is an **alternative to fine-tuning** that trades per-call tokens for not having to update weights.[^s1] Its fragility links it to **prompt sensitivity**, retrieval-based example selection connects it to **semantic search**,[^s2] and demonstrations that include worked reasoning are the basis of few-shot **chain-of-thought** prompting.[^s4][^s5] The technique was introduced and named in **"Language Models are Few-Shot Learners"**.[^s1]

## Sources

[^s1]: Brown et al., "Language Models are Few-Shot Learners", arXiv 2005.14165 (NeurIPS 2020). https://ar5iv.labs.arxiv.org/html/2005.14165 (accessed 2026-11-13)
[^s2]: Liu et al., "What Makes Good In-Context Examples for GPT-3?", DeeLIO 2022, pp. 100-114. https://aclanthology.org/2022.deelio-1.10 (accessed 2026-11-13)
[^s3]: Min et al., "Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?", EMNLP 2022, pp. 11048-11064. https://aclanthology.org/2022.emnlp-main.759 (accessed 2026-11-13)
[^s4]: Agarwal et al., "Many-Shot In-Context Learning", NeurIPS 2024. https://papers.neurips.cc/paper_files/paper/2024/hash/8cb564df771e9eacbfe9d72bd46a24a9-Abstract-Conference.html (accessed 2026-11-13)
[^s5]: Anthropic, "Prompting best practices: Use examples effectively", Claude Platform Docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/multishot-prompting (accessed 2026-11-13)
