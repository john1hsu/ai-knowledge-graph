---
id: kt:truthfulqa
type: Benchmark
title: TruthfulQA
aliases: [Truthful QA, TruthfulQA benchmark]
domain: evaluation-and-benchmarks
summary: >-
  A benchmark of 817 questions across 38 categories, introduced by Lin, Hilton and Evans in 2021, that measures
  whether language models avoid repeating popular misconceptions ("imitative falsehoods") learned from human text.
maturity: established
broader: [kt:ai-evaluation]
related: [kt:hallucination, kt:large-language-model, kt:scaling-laws, kt:rlhf, kt:benchmark-contamination, kt:llm-as-a-judge]
relations:
  - {predicate: introducedIn, object: kt:truthfulqa-measuring-how-models-mimic-human-falsehoods}
  - {predicate: studiedIn, object: kt:ai-alignment}
sources:
  - id: s1
    title: "TruthfulQA: Measuring How Models Mimic Human Falsehoods"
    publisher: "Proceedings of ACL 2022 (Volume 1: Long Papers), pp. 3214–3252 (Lin, Hilton, Evans)"
    url: https://aclanthology.org/2022.acl-long.229
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s2
    title: "TruthfulQA: Measuring How Models Mimic Human Falsehoods (arXiv:2109.07958, HTML version)"
    publisher: arXiv / ar5iv (Lin, Hilton, Evans)
    url: https://ar5iv.labs.arxiv.org/html/2109.07958
    type: primary
    accessed: 2026-11-10
  - id: s3
    title: "sylinrl/TruthfulQA README"
    publisher: TruthfulQA authors on GitHub
    url: https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md
    type: official-docs
    accessed: 2026-11-10
  - id: s4
    title: "Training language models to follow instructions with human feedback"
    publisher: NeurIPS 2022 (Ouyang et al.; OpenAI)
    url: https://papers.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s5
    title: "Performances are plateauing, let's make the leaderboard steep again"
    publisher: Hugging Face Open LLM Leaderboard team
    url: https://open-llm-leaderboard-blog.static.hf.space/
    type: official-docs
    accessed: 2026-11-10
  - id: s6
    title: "New, improved multiple-choice TruthfulQA"
    publisher: LessWrong (Evans, Chua, Lin), 15 January 2025
    url: https://www.lesswrong.com/posts/Bunfwz6JsNd44kgLT/new-improved-multiple-choice-truthfulqa
    type: community
    accessed: 2026-11-10
created: 2026-11-10
---

# TruthfulQA

**TruthfulQA** is a question-answering benchmark that tests whether a language model tells the truth when the most "human-sounding" answer is false. It was introduced by Stephanie Lin, Jacob Hilton and Owain Evans in a 2021 preprint and published at ACL 2022.[^s1] Its 817 questions span 38 categories, among them health, law, finance and politics, and each is written so that some people would answer it wrongly because of a common misconception or myth.[^s1] The benchmark targets what the authors call **imitative falsehoods**: false answers that a model rates as likely precisely because they appear often in the human-written text it was trained on.[^s2]

## How it works

Each question ships with sets of true and false reference answers and a supporting source.[^s2] The authors built the set partly adversarially: 437 questions were filtered against GPT-3-175B, keeping those it tended to get wrong, and 380 more were written without testing them on a model.[^s2] The standard setting is zero-shot, and the paper warns that few-shot prompting was not part of the design and would probably overstate truthfulness.[^s2]

Truthfulness is defined strictly. An answer counts as truthful only if it asserts nothing false about the real world, so a refusal such as "I have no comment" is truthful but uninformative.[^s2] The paper therefore scores **informativeness** separately and treats the two as roughly analogous to precision and recall; the headline figure is the share of answers that are both true and informative.[^s2]

There are two task formats. In **generation**, the model writes a full answer, which humans grade; as a cheaper proxy the authors fine-tuned a 6.7B-parameter GPT-3 model as "GPT-judge," which agreed with human labels 90–96% of the time on held-out model families.[^s2] In **multiple choice**, the model's likelihoods over the reference answers are compared.[^s2] The repository defines MC1 (one correct option) and MC2 (several true options) variants, and lists BLEURT, ROUGE and BLEU as weaker automatic metrics.[^s3] In January 2025 the maintainers added a recommended **binary** multiple-choice setting that pairs the best answer with the best incorrect answer in random order, fixed typos, reworded some questions and dropped a few.[^s3] They introduced it because MC1 could be gamed by test-taking tricks, such as avoiding wrong options that paraphrase one another; scores on the two formats correlate strongly.[^s6]

## Key findings

In the original evaluation (2021 models), human participants were truthful on 94% of questions, while the best model, GPT-3-175B with a "helpful" prompt, managed 58% and was both truthful and informative only 21% of the time.[^s1][^s2] The most cited result is **inverse scaling**: within the GPT-3, GPT-Neo/J, GPT-2 and UnifiedQA families, larger models were generally *less* truthful. The largest GPT-Neo/J was 17% less truthful than a model 60 times smaller.[^s2] The authors argued that scaling alone was unlikely to fix this and that training objectives beyond imitating web text were needed.[^s1]

Later work bore part of this out. OpenAI's InstructGPT paper reported small but significant gains on TruthfulQA from RLHF-tuned models over GPT-3, without telling the model to be truthful. It also credited Lin and Evans with noticing that the automatic metrics had overstated those gains.[^s4] By 2025 the maintainers observed that the top scores came from the most capable models, partly because post-training targeted truthfulness, and that one frontier model appeared close to the human baseline.[^s6]

## Limitations

The authors stress that a high score does not show a model is truthful in specialized domains, long-form writing or interactive use. The questions were written by the authors rather than drawn from real usage, and validators disagreed with 6–7% of the reference answers.[^s2] GPT-judge is an approximation that struggles with multi-sentence answers, so human grading remains the gold standard.[^s2] Contamination is another problem: when Hugging Face rebuilt its Open LLM Leaderboard in 2024, it dropped TruthfulQA partly because the benchmark had found its way into instruction-tuning datasets, so scores no longer reflected general ability.[^s5] The maintainers themselves note that TruthfulQA covers only a narrow slice of truthfulness.[^s6]

## Connections

TruthfulQA is a benchmark within the broader practice of **evaluation of AI systems**, introduced in the paper *TruthfulQA: Measuring How Models Mimic Human Falsehoods*.[^s1] It measures one form of **hallucination** in a **large language model**: confidently stated falsehoods that mirror human misconceptions.[^s2] Its inverse-scaling result is a well-known counterexample to the trend described by **scaling laws**, where bigger usually means better.[^s2] It became a standard check on **RLHF** and other post-training methods, and so an early measure in **AI alignment** work on honesty.[^s4][^s6] Its GPT-judge metric anticipated **LLM-as-a-judge** evaluation, and its removal from a major leaderboard is a case study in **benchmark contamination**.[^s2][^s5]

## Sources

[^s1]: Lin, Hilton & Evans, "TruthfulQA: Measuring How Models Mimic Human Falsehoods", ACL 2022. https://aclanthology.org/2022.acl-long.229 (accessed 2026-11-10)
[^s2]: Lin, Hilton & Evans, arXiv:2109.07958 (HTML). https://ar5iv.labs.arxiv.org/html/2109.07958 (accessed 2026-11-10)
[^s3]: sylinrl/TruthfulQA README, GitHub. https://raw.githubusercontent.com/sylinrl/TruthfulQA/main/README.md (accessed 2026-11-10)
[^s4]: Ouyang et al., "Training language models to follow instructions with human feedback", NeurIPS 2022. https://papers.neurips.cc/paper_files/paper/2022/file/b1efde53be364a73914f58805a001731-Paper-Conference.pdf (accessed 2026-11-10)
[^s5]: Hugging Face Open LLM Leaderboard team, "Performances are plateauing, let's make the leaderboard steep again". https://open-llm-leaderboard-blog.static.hf.space/ (accessed 2026-11-10)
[^s6]: Evans, Chua & Lin, "New, improved multiple-choice TruthfulQA", LessWrong, 15 January 2025. https://www.lesswrong.com/posts/Bunfwz6JsNd44kgLT/new-improved-multiple-choice-truthfulqa (accessed 2026-11-10)
