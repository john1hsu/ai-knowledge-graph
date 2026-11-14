---
id: kt:beam-search
type: Algorithm
title: Beam search
aliases: [beam decoding, beam-search decoding]
domain: inference-and-optimization
summary: >-
  A heuristic decoding algorithm for sequence models that, at each generation step, keeps only the k highest-scoring
  partial sequences (the beam) and extends them, trading search cost against the chance of finding the most probable
  output.
maturity: established
broader: [kt:decoding-strategy, kt:heuristic-search]
related: [kt:sequence-to-sequence-learning, kt:knowledge-distillation, kt:self-consistency, kt:diverse-beam-search, kt:if-beam-search-is-the-answer-what-was-the-question]
relations:
  - {predicate: alternativeTo, object: kt:sampling-temperature-and-top-p}
  - {predicate: usedIn, object: kt:neural-machine-translation-by-jointly-learning-to-align-and-translate}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: contrastsWith, object: kt:the-curious-case-of-neural-text-degeneration}
sources:
  - id: s1
    title: "10.8. Beam Search"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li, Smola)
    url: https://d2l.ai/chapter_recurrent-modern/beam-search.html
    type: textbook
    accessed: 2026-11-14
  - id: s2
    title: "Six Challenges for Neural Machine Translation"
    publisher: Proceedings of the First Workshop on Neural Machine Translation, ACL 2017 (Koehn, Knowles)
    url: https://aclanthology.org/W17-3204/
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s3
    title: "If beam search is the answer, what was the question?"
    publisher: EMNLP 2020 (Meister, Cotterell, Vieira)
    url: https://aclanthology.org/2020.emnlp-main.170
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s4
    title: "Diverse Beam Search for Improved Description of Complex Scenes"
    publisher: AAAI 2018 (Vijayakumar, Cogswell, Selvaraju, Sun, Lee, Crandall, Batra)
    url: https://ojs.aaai.org/index.php/AAAI/article/view/12340
    type: peer-reviewed
    accessed: 2026-11-14
  - id: s5
    title: "The Curious Case of Neural Text Degeneration"
    publisher: arXiv:1904.09751v2 (Holtzman, Buys, Du, Forbes, Choi)
    url: https://arxiv.org/abs/1904.09751
    type: primary
    accessed: 2026-11-14
  - id: s6
    title: "Generation (GenerationConfig reference), Transformers v5.3.0"
    publisher: Hugging Face Transformers documentation
    url: https://huggingface.co/docs/transformers/v5.3.0/en/main_classes/text_generation
    type: official-docs
    accessed: 2026-11-14
created: 2026-11-14
---

# Beam search

**Beam search** is the classic deterministic decoding algorithm for autoregressive sequence models such as encoder–decoder translators and language models. Instead of committing to a single token at each step, it keeps a fixed number *k* of the most probable partial outputs, called the **beam**, and expands all of them in parallel. The beam size *k* is its one hyperparameter, and it sets the trade-off between computational efficiency and how close the search gets to the single most probable sequence.[^s1]

## How it works

Decoding asks for the output sequence with the highest conditional probability given the input. **Greedy search** picks the most probable token at every step at a cost of O(|Y|T′) for vocabulary size |Y| and maximum length T′, but it can miss better sequences: in the *Dive into Deep Learning* example, greedy decoding finds a sequence with probability 0.048 while a different path reaches 0.054. **Exhaustive search** is optimal but costs O(|Y|^T′), which for a 10,000-word vocabulary and length 10 means 10^40 candidates.[^s1]

Beam search sits between them. At the first step it keeps the *k* most probable tokens; at every later step it scores all *k*·|Y| one-token extensions of the current beam and again keeps the top *k*, for a cost of O(k|Y|T′). Greedy search is simply beam search with *k* = 1.[^s1] Hypotheses that emit an end-of-sequence token are set aside as finished candidates, and the final output is chosen by a length-normalised log-probability, dividing the summed log-probabilities by *L*^α, where *L* is the length; the textbook gives α = 0.75 as a usual setting. Without this correction, longer outputs are unfairly penalised because every extra token adds another negative log term.[^s1]

## Limitations and open questions

Wider beams do not reliably give better output. Koehn and Knowles tested beam sizes from 1 to 1,000 across eight language pairs and found that translation quality usually worsens past an optimal size, which ranged from 4 to about 30; they traced the drop mainly to translations becoming shorter. Length normalisation softened, but did not remove, the decline.[^s2] Meister, Cotterell and Vieira sharpen the puzzle: exact maximum-probability decoding often yields poor text, yet beam search, which makes many search errors, underpins most state-of-the-art results. They argue that beam search exactly solves a different objective that favours **uniform information density**, and report that adherence to that property correlates strongly with BLEU in translation experiments.[^s3]

Two further weaknesses matter in practice. Beam outputs tend to be near-duplicates; Vijayakumar et al. note that the top candidates are often minor rewordings of one utterance and propose **diverse beam search**, which adds diversity constraints between groups of beams at little extra cost and improved both diversity and quality on image captioning and question generation.[^s4] And for open-ended generation, Holtzman et al. argue that decoding by maximising likelihood produces dull, oddly repetitive text, motivating truncated sampling instead.[^s5]

## In practice

The studies above show where beam search earns its keep: tasks such as machine translation and image captioning, where a fairly narrow set of outputs is correct,[^s2][^s4] whereas the degeneration critique applies to open-ended text generation.[^s5] In Hugging Face Transformers, `num_beams` sets the beam width, with 1 meaning no beam search; `length_penalty` is the exponent on output length used to divide the sequence's log-likelihood score, so positive values favour longer outputs; `early_stopping` chooses between stopping once `num_beams` candidates are complete, a heuristic cut-off, or the canonical rule of running until no better candidate can exist; and `num_return_sequences` returns several finished beams. Setting `do_sample=True` with beams turns the method into beam-search multinomial sampling (as documented for Transformers v5.3).[^s6]

## Connections

Beam search is an instance of the broader family of **decoding strategies** (kt:decoding-strategy) and of **heuristic search** (kt:heuristic-search), since it prunes the search space to a fixed width.[^s1] It is the standard decoder of **sequence-to-sequence learning** (kt:sequence-to-sequence-learning) and the attention-based translator of Bahdanau et al. (kt:neural-machine-translation-by-jointly-learning-to-align-and-translate), the setting whose failure modes Koehn and Knowles measured.[^s2] Its main **alternative** is stochastic decoding with **temperature and top-p** (kt:sampling-temperature-and-top-p), introduced by the nucleus-sampling paper (kt:the-curious-case-of-neural-text-degeneration), which contrasts likelihood-maximising search with sampling.[^s5] **Diverse beam search** (kt:diverse-beam-search) extends it for varied outputs,[^s4] and Meister et al.'s paper (kt:if-beam-search-is-the-answer-what-was-the-question) recasts what it optimises.[^s3] The graph's articles on **knowledge distillation** (kt:knowledge-distillation) and **self-consistency** (kt:self-consistency) both discuss beam search as a point of comparison, and the algorithm is **implemented in Hugging Face Transformers** (kt:hugging-face-transformers).[^s6]

## Sources
[^s1]: Zhang, Lipton, Li, Smola, "10.8. Beam Search", *Dive into Deep Learning*. https://d2l.ai/chapter_recurrent-modern/beam-search.html (accessed 2026-11-14)
[^s2]: Koehn, Knowles, "Six Challenges for Neural Machine Translation", Proceedings of the First Workshop on Neural Machine Translation, ACL 2017, pp. 28–39. https://aclanthology.org/W17-3204/ (accessed 2026-11-14)
[^s3]: Meister, Cotterell, Vieira, "If beam search is the answer, what was the question?", EMNLP 2020, pp. 2173–2185. https://aclanthology.org/2020.emnlp-main.170 (accessed 2026-11-14)
[^s4]: Vijayakumar et al., "Diverse Beam Search for Improved Description of Complex Scenes", AAAI 2018. https://ojs.aaai.org/index.php/AAAI/article/view/12340 (accessed 2026-11-14)
[^s5]: Holtzman, Buys, Du, Forbes, Choi, "The Curious Case of Neural Text Degeneration", arXiv:1904.09751v2. https://arxiv.org/abs/1904.09751 (accessed 2026-11-14)
[^s6]: Hugging Face, "Generation" (GenerationConfig reference), Transformers v5.3.0 documentation. https://huggingface.co/docs/transformers/v5.3.0/en/main_classes/text_generation (accessed 2026-11-14)
