---
id: kt:named-entity-recognition
type: Application
title: Named-entity recognition
aliases: [NER, named entity recognition, named entity recognition and classification, entity extraction, entity tagging]
domain: retrieval-and-knowledge
summary: >-
  The information-extraction task of finding the spans of text that name people, organizations, locations and other
  entity types and labelling each span with its type; defined as an evaluation task at MUC-6 in 1995 and usually
  framed today as token-level sequence labelling scored by entity-level F1.
maturity: established
broader: [kt:information-extraction]
related: [kt:conditional-random-field, kt:hidden-markov-model, kt:glove, kt:knowledge-graph, kt:large-language-model]
relations:
  - {predicate: studiedIn, object: kt:natural-language-processing}
  - {predicate: introducedIn, object: kt:message-understanding-conference-6}
  - {predicate: evaluatedOn, object: kt:conll-2003}
  - {predicate: enables, object: kt:entity-linking}
  - {predicate: enables, object: kt:relation-extraction}
sources:
  - id: s1
    title: "Message Understanding Conference-6: A Brief History"
    publisher: Proceedings of COLING 1996, ACL Anthology C96-1079 (Grishman and Sundheim)
    url: https://aclanthology.org/C96-1079.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s2
    title: "Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition"
    publisher: Proceedings of CoNLL-2003, ACL Anthology W03-0419 (Tjong Kim Sang and De Meulder)
    url: https://aclanthology.org/W03-0419.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "Sequence Labeling for Parts of Speech and Named Entities (Speech and Language Processing, 3rd ed. draft, ch. 17)"
    publisher: Stanford University (Jurafsky and Martin), draft of January 2026
    url: https://web.stanford.edu/%7Ejurafsky/slp3/17.pdf
    type: textbook
    accessed: 2026-11-15
  - id: s4
    title: "Neural Architectures for Named Entity Recognition"
    publisher: Proceedings of NAACL-HLT 2016, ACL Anthology N16-1030 (Lample, Ballesteros, Subramanian, Kawakami and Dyer), pp. 260–270
    url: https://aclanthology.org/N16-1030.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition"
    publisher: ICLR 2024 proceedings (Zhou, Zhang, Gu, Chen and Poon)
    url: https://proceedings.iclr.cc/paper_files/paper/2024/hash/34678d08b36076de986df95c5bbba92f-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s6
    title: "UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition (arXiv v2)"
    publisher: arXiv 2308.03279 (authors' version)
    url: https://arxiv.org/abs/2308.03279
    type: primary
    accessed: 2026-11-15
created: 2026-11-15
---

# Named-entity recognition

**Named-entity recognition (NER)** is the task of finding the spans of text that refer to something by a proper name, such as a person, a place or an organization, and assigning each span a type.[^s3] Jurafsky and Martin note that the term "named entity" is commonly stretched to cover dates, times and numeric expressions such as prices, and that applications often add their own types, such as genes, proteins, products or works of art.[^s3] NER is one of the most widely used building blocks of information extraction: it turns unstructured text into typed mentions that later stages can link, relate and store.[^s3]

## Origin

The task was defined for the Sixth Message Understanding Conference (MUC-6), whose formal evaluation took place in September 1995.[^s1] The organizers wanted near-term, practical component tasks that were independent of any one domain and could be done automatically with high accuracy. The named-entity task asked systems to mark names of people, organizations and geographic locations, plus time, currency and percentage expressions, using SGML tags.[^s1] Systems did well: most participants exceeded 90% recall and precision, and the best reached 96% recall and 97% precision. Grishman and Sundheim cautioned, however, that every test text came from the *Wall Street Journal*.[^s1]

The CoNLL-2003 shared task then established the benchmark that dominated the next two decades. It used English Reuters news from 1996–97 and German *Frankfurter Rundschau* text, annotated with four types: PER, ORG, LOC and MISC.[^s2] The English training set held roughly 15,000 sentences (203,621 tokens). A predicted entity counted only if it matched the gold span exactly, and systems were ranked by F1.[^s2] Of sixteen entries, the best (Florian et al.) scored 88.76 F1 on English and 72.41 on German. It combined maximum-entropy, transformation-based, hidden-Markov and robust-risk-minimization classifiers. Eleven teams used external resources, all of them gazetteers (lists of known names).[^s2]

## How it works

NER is normally cast as **sequence labelling** over tokens. In the BIO scheme each token is tagged B (begins an entity of type X), I (inside one) or O (outside any), so *n* entity types need 2*n*+1 tags. Variants include IO, which drops B and blurs the boundary between adjacent same-type entities, and BIOES, which adds E for the last token and S for single-token entities.[^s3] For example, "Jane Villanueva of United Airlines" becomes B-PER I-PER O B-ORG I-ORG.

The task is hard for two reasons. Segmentation is the first: most tokens are not entities, and the system must find where each name starts and ends.[^s3] Type ambiguity is the second: Jurafsky and Martin's example "Washington" can be a person, a sports team, a location or a geo-political entity depending on context.[^s3]

Methods have tracked the field's broader history. Feature-based taggers such as hidden Markov models and linear-chain conditional random fields (CRFs), decoded with the Viterbi algorithm, used word identity, neighbouring words, affixes, word shape and gazetteer membership as features.[^s3] Lample et al. (NAACL 2016) replaced hand-built features with a bidirectional LSTM topped by a CRF. They fed it character-level word representations learned in training plus pretrained word embeddings, with no gazetteers or language-specific resources. It reached 90.94 F1 on CoNLL-2003 English and 78.76 on German.[^s4] As of the January 2026 textbook draft, neural models, including Transformer and BERT-based taggers, are the standard approach.[^s3]

## Evaluation and limitations

NER is scored with entity-level precision, recall and F1, because the entity rather than the word is the unit of output. Training, by contrast, usually optimizes per-token labels, and this mismatch is a known wrinkle.[^s3] Exact-span matching is strict: tagging only "Jane" in "Jane Villanueva" counts as both a false positive and a false negative.[^s3][^s2] High scores on news benchmarks also transfer poorly to other genres, a concern raised as early as MUC-6.[^s1] Fixed type inventories are a further limit, since real applications need domain types the classic benchmarks do not include.[^s3]

## In practice

NER feeds relation and event extraction, early stages of question answering, entity linking to knowledge bases, entity-level sentiment analysis, and the building of semantic representations.[^s3] Commercial systems often combine high-precision rules, name lists and supervised learners in staged passes.[^s3] Large language models have reopened the task as **open NER** over arbitrary, user-named types. UniversalNER (ICLR 2024) distilled ChatGPT into smaller models through mission-focused instruction tuning, without supervised NER examples, and evaluated them on a 43-dataset, 9-domain benchmark. The authors report they beat ChatGPT by 7–9 average F1 points with a small fraction of its parameters.[^s5][^s6]

## Connections

NER is a core task within **information extraction** and is **studied in** **natural language processing**.[^s3] It was **introduced in** the **MUC-6** evaluation and is classically **evaluated on** **CoNLL-2003**.[^s1][^s2] Its tagged mentions **enable** **entity linking** and **relation extraction**, which is how text becomes the nodes and edges of a **knowledge graph**.[^s3] **Conditional random fields** and **hidden Markov models** are the classic sequence models for the task, and pretrained word vectors such as **GloVe** served as input features for neural taggers.[^s3][^s4] **Large language models** now handle open-type NER, either by prompting or, as in UniversalNER, by distilling them into smaller specialist models.[^s5]

## Sources
[^s1]: Grishman and Sundheim, "Message Understanding Conference-6: A Brief History", COLING 1996. https://aclanthology.org/C96-1079.pdf (accessed 2026-11-15)
[^s2]: Tjong Kim Sang and De Meulder, "Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition", CoNLL 2003. https://aclanthology.org/W03-0419.pdf (accessed 2026-11-15)
[^s3]: Jurafsky and Martin, *Speech and Language Processing*, 3rd ed. draft (January 2026), ch. 17. https://web.stanford.edu/%7Ejurafsky/slp3/17.pdf (accessed 2026-11-15)
[^s4]: Lample et al., "Neural Architectures for Named Entity Recognition", NAACL-HLT 2016. https://aclanthology.org/N16-1030.pdf (accessed 2026-11-15)
[^s5]: Zhou et al., "UniversalNER: Targeted Distillation from Large Language Models for Open Named Entity Recognition", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/34678d08b36076de986df95c5bbba92f-Abstract-Conference.html (accessed 2026-11-15)
[^s6]: Zhou et al., UniversalNER, arXiv 2308.03279v2. https://arxiv.org/abs/2308.03279 (accessed 2026-11-15)
