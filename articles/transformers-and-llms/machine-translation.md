---
id: kt:machine-translation
type: Application
title: Machine translation
aliases: [MT, automatic translation, computer translation]
domain: transformers-and-llms
summary: >-
  The use of computers to translate text (or transcribed speech) from a source natural language into a target
  language, which evolved from hand-written rule systems in the 1950s through statistical word- and phrase-based
  models to neural encoder-decoder and Transformer models.
maturity: established
broader: [kt:natural-language-processing]
related: [kt:sequence-to-sequence-learning, kt:bleu, kt:wmt-2014, kt:beam-search, kt:lighthill-report, kt:transformer-architecture]
relations:
  - {predicate: hasPart, object: kt:statistical-machine-translation}
  - {predicate: hasPart, object: kt:neural-machine-translation}
  - {predicate: evaluatedOn, object: kt:wmt-2014}
  - {predicate: influencedBy, object: kt:georgetown-ibm-experiment}
sources:
  - id: s1
    title: "The Georgetown-IBM experiment demonstrated in January 1954"
    publisher: Proceedings of the 6th Conference of the Association for Machine Translation in the Americas (AMTA 2004), pp. 102-114 (W. John Hutchins)
    url: https://aclanthology.org/2004.amta-papers.12
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "Language and Machines: Computers in Translation and Linguistics (ALPAC report)"
    publisher: Automatic Language Processing Advisory Committee, National Academy of Sciences / National Research Council, 1966
    url: https://aclanthology.org/www.mt-archive.info/ALPAC-1966-TOC.htm
    type: primary
    accessed: 2026-11-17
  - id: s3
    title: "The Mathematics of Statistical Machine Translation: Parameter Estimation"
    publisher: Computational Linguistics 19(2), 1993, pp. 263-311 (Brown, Della Pietra, Della Pietra, Mercer)
    url: https://aclanthology.org/J93-2003.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "Statistical Phrase-Based Translation"
    publisher: Proceedings of HLT-NAACL 2003, pp. 127-133 (Koehn, Och, Marcu)
    url: https://aclanthology.org/N03-1017/
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation"
    publisher: Google Research (Wu, Schuster, Chen, Le, Norouzi et al.), arXiv:1609.08144, 2016
    url: https://research.google/pubs/googles-neural-machine-translation-system-bridging-the-gap-between-human-and-machine-translation/
    type: primary
    accessed: 2026-11-17
  - id: s6
    title: "Attention Is All You Need"
    publisher: Vaswani et al., arXiv:1706.03762 (NeurIPS 2017)
    url: https://arxiv.org/abs/1706.03762
    type: primary
    accessed: 2026-11-17
  - id: s7
    title: "Machine Translation and the Dataset (Dive into Deep Learning, ch. 10.5)"
    publisher: Zhang, Lipton, Li, Smola, d2l.ai
    url: https://d2l.ai/chapter_recurrent-modern/machine-translation-and-dataset.html
    type: textbook
    accessed: 2026-11-17
created: 2026-11-17
---

# Machine translation

**Machine translation (MT)** is the task of having a computer map a sentence in a *source* language to a fluent, meaning-preserving sentence in a *target* language. The two sentences may differ in length and word order, so the system must read the whole input and generate a differently shaped output; this is why textbooks treat translation as the canonical sequence-to-sequence (seq2seq) problem.[^s7] MT is one of the oldest applications of computing to language, and each of its major paradigm shifts (rules, statistics, neural networks) has shaped natural language processing more broadly.[^s1][^s3][^s5]

## History

**Early rule-based systems (1950s-1960s).** On 7 January 1954, Georgetown University and IBM publicly demonstrated Russian-to-English translation on an IBM 701 in New York. The system translated more than 60 prepared sentences, mostly on organic chemistry, using a vocabulary of roughly 250 items and just six rules for word choice and reordering. Press coverage was enthusiastic, and project leader Léon Dostert predicted practical multilingual MT within three to five years.[^s1] The following decade of research fell far short of that promise. Funders convened the Automatic Language Processing Advisory Committee (ALPAC), chaired by John R. Pierce, whose 1966 National Academy of Sciences report reviewed the state of MT and its prospects.[^s2] Hutchins notes that ALPAC judged MT output to need extensive post-editing, and that the disappointment was amplified by the inflated expectations the 1954 demonstration had created.[^s1]

**Statistical MT (1990s-2010s).** Researchers at IBM recast translation as probabilistic inference. To translate a French sentence *f*, choose the English sentence *e* that maximizes Pr(e)·Pr(f|e), splitting the problem into a language model (is *e* fluent?), a translation model (does *f* match *e*?), and a search procedure. Brown et al. (1993) called this the "Fundamental Equation of Machine Translation" and defined five increasingly rich alignment models, now known as IBM Models 1-5, trained with expectation-maximization on about 1.78 million English-French sentence pairs from Canadian parliamentary proceedings.[^s3] Because the approach used little hand-coded linguistics, it could in principle be retrained for any language pair with a parallel corpus.[^s3] Koehn, Och and Marcu (2003) then showed that translating multi-word *phrases* rather than single words beat the word-based IBM Model 4 system, that phrases of up to three words captured most of the gain, and that restricting phrases to syntactic constituents hurt quality.[^s4] Phrase-based systems were still the production baseline that Google measured its neural system against in 2016.[^s5]

**Neural MT (2014-present).** Neural approaches model translation end to end with an encoder that reads the source and a decoder that generates the target.[^s7] Google's 2016 GNMT system used an 8-layer LSTM encoder and 8-layer LSTM decoder with attention and residual connections, split rare words into sub-word "wordpieces", and used beam search with length normalization and a coverage penalty. Google reported that, in human side-by-side evaluation on isolated simple sentences, it cut translation errors by an average of 60% relative to its own phrase-based production system.[^s5] A year later the Transformer dropped recurrence entirely in favor of attention; Vaswani et al. reported 28.4 BLEU on WMT 2014 English-German and 41.8 BLEU on English-French, with the latter model trained in about 3.5 days on eight GPUs.[^s6]

## How a modern system works

A neural MT pipeline tokenizes parallel sentence pairs (typically into sub-word units), appends end-of-sequence markers, and trains an encoder-decoder with teacher forcing: the decoder receives the target shifted by one token and learns to predict the next token.[^s7] At inference the decoder generates one token at a time, usually with beam search, until it emits the end-of-sequence token.[^s5][^s7] Training data size, vocabulary handling for rare words, and decoding heuristics strongly affect quality.[^s5]

## Limitations and open questions

Automatic metrics such as BLEU are convenient but imperfect proxies for adequacy and fluency, so GNMT's headline claim rested on human side-by-side ratings, and of simple, isolated sentences rather than whole documents.[^s5] Quality still depends on the availability of parallel data, which the statistical era made explicit: the IBM models were learned entirely from aligned bilingual text.[^s3] The 1954 to 1966 episode remains a standard caution about extrapolating from small, curated demonstrations.[^s1]

## Connections

Machine translation is an application within `kt:natural-language-processing`, and its split into `kt:statistical-machine-translation` and `kt:neural-machine-translation` traces the field's shift from probabilistic models to deep learning.[^s3][^s5] It is the motivating task for `kt:sequence-to-sequence-learning` and for decoding with `kt:beam-search`.[^s5][^s7] The `kt:transformer-architecture` was introduced and first validated on translation, using the `kt:wmt-2014` test sets scored with `kt:bleu`.[^s6] The `kt:georgetown-ibm-experiment` and the ALPAC report set expectations whose collapse is echoed in the later `kt:lighthill-report`, which counted translation among AI's disappointments.

## Sources
[^s1]: W. John Hutchins, "The Georgetown-IBM experiment demonstrated in January 1954", AMTA 2004, pp. 102-114. https://aclanthology.org/2004.amta-papers.12 (accessed 2026-11-17)
[^s2]: ALPAC, *Language and Machines: Computers in Translation and Linguistics*, National Academy of Sciences / National Research Council, 1966. https://aclanthology.org/www.mt-archive.info/ALPAC-1966-TOC.htm (accessed 2026-11-17)
[^s3]: Brown, Della Pietra, Della Pietra & Mercer, "The Mathematics of Statistical Machine Translation: Parameter Estimation", *Computational Linguistics* 19(2), 1993. https://aclanthology.org/J93-2003.pdf (accessed 2026-11-17)
[^s4]: Koehn, Och & Marcu, "Statistical Phrase-Based Translation", HLT-NAACL 2003. https://aclanthology.org/N03-1017/ (accessed 2026-11-17)
[^s5]: Wu et al., "Google's Neural Machine Translation System: Bridging the Gap between Human and Machine Translation", Google Research, 2016. https://research.google/pubs/googles-neural-machine-translation-system-bridging-the-gap-between-human-and-machine-translation/ (accessed 2026-11-17)
[^s6]: Vaswani et al., "Attention Is All You Need", arXiv:1706.03762, 2017. https://arxiv.org/abs/1706.03762 (accessed 2026-11-17)
[^s7]: Zhang, Lipton, Li & Smola, *Dive into Deep Learning*, §10.5 "Machine Translation and the Dataset". https://d2l.ai/chapter_recurrent-modern/machine-translation-and-dataset.html (accessed 2026-11-17)
