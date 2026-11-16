---
id: kt:bleu
type: Concept
title: BLEU
aliases: [bilingual evaluation understudy, BLEU score, Bleu]
domain: evaluation-and-benchmarks
summary: >-
  An automatic metric for machine translation and other text generation that scores a candidate against one or more
  human reference translations by combining clipped n-gram precisions (usually up to 4-grams) in a geometric mean
  and multiplying by a brevity penalty.
maturity: foundational
broader: [kt:ai-evaluation, kt:machine-translation]
related: [kt:perplexity, kt:wmt-2014, kt:sequence-to-sequence-learning, kt:llm-as-a-judge]
relations:
  - {predicate: introducedIn, object: kt:bleu-a-method-for-automatic-evaluation-of-machine-translation}
  - {predicate: alternativeTo, object: kt:human-evaluation}
  - {predicate: alternativeTo, object: kt:meteor}
  - {predicate: implementedIn, object: kt:sacrebleu}
sources:
  - id: s1
    title: "Bleu: a Method for Automatic Evaluation of Machine Translation"
    publisher: ACL 2002 (Papineni, Roukos, Ward, Zhu; IBM T. J. Watson Research Center)
    url: https://aclanthology.org/P02-1040.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Re-evaluating the Role of Bleu in Machine Translation Research"
    publisher: EACL 2006 (Callison-Burch, Osborne, Koehn)
    url: https://www.cis.upenn.edu/~ccb/publications/re-evaluating-the-role-of-bleu-in-mt-research.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s3
    title: "A Call for Clarity in Reporting BLEU Scores"
    publisher: arXiv 1804.08771 (Matt Post, Amazon Research), 2018
    url: https://arxiv.org/pdf/1804.08771
    type: primary
    accessed: 2026-11-16
  - id: s4
    title: "Tangled up in BLEU: Reevaluating the Evaluation of Automatic Machine Translation Evaluation Metrics"
    publisher: ACL 2020 (Mathur, Baldwin, Cohn)
    url: https://aclanthology.org/2020.acl-main.448
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "Metric: bleu (README)"
    publisher: Hugging Face Evaluate
    url: https://huggingface.co/spaces/evaluate-metric/bleu/blob/main/README.md
    type: official-docs
    accessed: 2026-11-16
created: 2026-11-16
---

# BLEU

BLEU, short for *bilingual evaluation understudy*, is an automatic metric that estimates the quality of a machine translation by measuring how many of its word n-grams also appear in one or more human reference translations. It was introduced by Kishore Papineni, Salim Roukos, Todd Ward and Wei-Jing Zhu of IBM's T. J. Watson Research Center at ACL 2002, and the name signals its intended role as a fast, cheap stand-in for human judges.[^s1] For roughly two decades it was the default headline number in machine translation papers, and it is still widely reported for translation and other generation tasks.[^s3]

## How it works

BLEU has three ingredients.[^s1]

1. **Clipped (modified) n-gram precision.** For each n, every candidate n-gram is counted, but its count is clipped to the largest number of times that n-gram occurs in any single reference: Count_clip = min(Count, Max_Ref_Count). The clipped counts are summed over the whole test corpus and divided by the total number of candidate n-grams, giving p_n. Clipping stops a system from scoring well by repeating a common reference word.[^s1]
2. **Geometric mean.** The precisions for n = 1 to N (the paper uses N = 4 with uniform weights w_n = 1/N) are combined as exp(Σ w_n log p_n), so a system must match words *and* longer phrases.[^s1]
3. **Brevity penalty.** Precision alone rewards short outputs, so BLEU multiplies by BP = 1 if the candidate corpus length c exceeds the effective reference length r, and BP = e^(1 − r/c) otherwise. The penalty is computed over the corpus rather than per sentence, so individual short sentences are not punished harshly.[^s1]

The final score is BLEU = BP · exp(Σ w_n log p_n), between 0 and 1 (often reported ×100). With several references, each n-gram's maximum count is taken across all of them, so scores rise with more references: in the original paper a human translation scored 0.3468 against four references but 0.2571 against two.[^s1] On a small study of five systems, the authors reported correlations of 0.99 with monolingual and 0.96 with bilingual human judges.[^s1]

## Limitations and critiques

BLEU measures surface overlap, not meaning. Callison-Burch, Osborne and Koehn (EACL 2006) showed that it gives no credit for synonyms or paraphrases, weights content and function words equally, and handles recall only through the brevity penalty. Because it constrains word order only through matching higher-order n-grams, a hypothesis can be shuffled into a very large number of permutations with an identical score.[^s2] In the 2005 NIST evaluation, the entry human judges ranked first was ranked sixth by BLEU, and the metric substantially underrated the rule-based Systran system relative to statistical systems. Their conclusion: a higher BLEU score is neither necessary nor sufficient for better translation, and the metric is best used to compare similar systems or track incremental changes to one system.[^s2]

A second problem is reproducibility. Matt Post (2018) argued that BLEU is really a parameterized family of metrics whose value depends on the number of references, tokenization and other reference preprocessing, casing, and test-set version. On WMT 2017 data, these choices moved scores by up to 1.8 points for one language pair, often more than the gains new methods claimed.[^s3] Mathur, Baldwin and Cohn (ACL 2020) further found that judging how well metrics like BLEU agree with humans is sensitive to outlier systems, and proposed thresholds on the size of a metric improvement before treating it as meaningful.[^s4]

## In practice

Post's SacreBLEU tool addresses the reporting problem by downloading standard test sets itself, applying WMT-standard tokenization internally to detokenized output, and printing a signature string that records every setting (casing, language pair, number of references, smoothing, test set, tokenizer, version).[^s3] Library implementations such as Hugging Face Evaluate default to a maximum n-gram order of 4 and the WMT `13a` tokenizer, return the n-gram precisions, brevity penalty and length ratio alongside the score, and warn that scores are not comparable across datasets, languages, or tokenization settings.[^s5] Sentence-level use usually requires smoothing, since a single missing 4-gram drives the geometric mean to zero; the Evaluate implementation offers optional Lin et al. (2004) smoothing.[^s5]

## Connections

BLEU is a classic instance of automatic **AI evaluation** for **machine translation**, designed as a cheaper **alternative to human evaluation**, against which it is still validated.[^s1][^s4] It was **introduced in** the 2002 ACL paper and is most reliably computed with **SacreBLEU**, the tool built to make WMT-style scores comparable.[^s1][^s3] Like **perplexity**, it is an easy-to-compute proxy whose numbers mean little outside a fixed setup; unlike perplexity, it scores generated text against references rather than a model's probabilities.[^s3][^s5] It is an **alternative to** other reference-based metrics such as **METEOR**, which Callison-Burch et al. note shares similar limitations, while approaches like **LLM-as-a-judge** try to capture meaning that n-gram overlap misses.[^s2] WMT test sets, including the two versions of the **WMT 2014** English–German set, are the standard data on which BLEU is reported for **sequence-to-sequence** translation models.[^s3]

## Sources
[^s1]: Papineni, Roukos, Ward, Zhu, "Bleu: a Method for Automatic Evaluation of Machine Translation", ACL 2002. https://aclanthology.org/P02-1040.pdf (accessed 2026-11-16)
[^s2]: Callison-Burch, Osborne, Koehn, "Re-evaluating the Role of Bleu in Machine Translation Research", EACL 2006. https://www.cis.upenn.edu/~ccb/publications/re-evaluating-the-role-of-bleu-in-mt-research.pdf (accessed 2026-11-16)
[^s3]: Post, "A Call for Clarity in Reporting BLEU Scores", arXiv:1804.08771, 2018. https://arxiv.org/pdf/1804.08771 (accessed 2026-11-16)
[^s4]: Mathur, Baldwin, Cohn, "Tangled up in BLEU: Reevaluating the Evaluation of Automatic Machine Translation Evaluation Metrics", ACL 2020. https://aclanthology.org/2020.acl-main.448 (accessed 2026-11-16)
[^s5]: Hugging Face Evaluate, "Metric: bleu" README. https://huggingface.co/spaces/evaluate-metric/bleu/blob/main/README.md (accessed 2026-11-16)
