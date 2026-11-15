---
id: kt:natural-language-processing
type: Field
title: Natural language processing
aliases: [NLP, computational linguistics]
domain: transformers-and-llms
summary: >-
  The subfield of artificial intelligence and computer science that uses computational methods to analyze,
  understand and generate human language, which moved from hand-written rules to statistical corpus-based
  models and then to neural networks and large language models.
maturity: established
broader: [kt:artificial-intelligence, kt:machine-learning]
related: [kt:large-language-model, kt:information-retrieval, kt:automatic-speech-recognition, kt:embeddings, kt:transformer-architecture, kt:eliza]
relations:
  - {predicate: hasPart, object: kt:machine-translation}
  - {predicate: hasPart, object: kt:named-entity-recognition}
  - {predicate: hasPart, object: kt:sentiment-analysis}
  - {predicate: influencedBy, object: kt:deep-learning}
sources:
  - id: s1
    title: "Advances in natural language processing"
    publisher: J. Hirschberg and C. D. Manning, Science 349(6245):261–266, 2015 (copy hosted by Princeton COS 484)
    url: https://nlp.cs.princeton.edu/cos484-sp22/readings/advances_in_nlp.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s2
    title: "Natural language processing"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/technology/natural-language-processing-computer-science
    type: encyclopedia
    accessed: 2026-11-15
  - id: s3
    title: "Natural Language Processing (Almost) from Scratch"
    publisher: R. Collobert, J. Weston, L. Bottou, M. Karlen, K. Kavukcuoglu, P. Kuksa, JMLR 12:2493–2537, 2011
    url: https://jmlr.org/papers/v12/collobert11a.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "Speech and Language Processing (3rd ed. draft)"
    publisher: D. Jurafsky and J. H. Martin, Stanford University
    url: https://web.stanford.edu/~jurafsky/slp3/
    type: textbook
    accessed: 2026-11-15
created: 2026-11-15
---

# Natural language processing

**Natural language processing (NLP)**, also called computational linguistics, is the subfield of computer science and artificial intelligence that applies computational methods to learning, understanding and producing human language.[^s1] Its systems serve three broad purposes: helping people communicate with each other (machine translation), letting people communicate with machines (conversational agents), and analyzing the very large volumes of language now available online.[^s1] Britannica describes the field as drawing jointly on computational linguistics, statistics, machine learning and deep learning to let computers process and respond to written and spoken language in a humanlike way.[^s2]

## History: rules, statistics, neural networks

For its first decades the field tried to give computers hand-written vocabularies and grammar rules. Machine translation was studied intensively from the late 1950s, but hand-built grammars handled ambiguity and context poorly and achieved limited success.[^s1] Rule-based systems had to anticipate every exception explicitly, which made sarcasm, idiom and metaphor especially hard.[^s2]

During the 1980s and 1990s the field shifted to statistical, corpus-based models learned from large collections of text; the Linguistic Data Consortium, which distributes such corpora, was founded in 1992.[^s1] A landmark was IBM's work in the early 1990s on probabilistic translation models learned from parallel English–French Canadian parliamentary proceedings, and by the 2000s phrase-based statistical translation, as used in Google Translate, dominated the task.[^s1] Statistical systems assign probabilities to competing interpretations of a text rather than choosing one by rule.[^s2]

The neural turn came next. Collobert, Weston and colleagues showed in 2011 that a single neural architecture could perform part-of-speech tagging, chunking, named-entity recognition and semantic role labeling, learning internal representations from mostly unlabeled text instead of relying on hand-engineered, task-specific features.[^s3] By 2015, recurrent networks with long short-term memory units had produced state-of-the-art neural machine translation.[^s1] Transformer-based pretrained models followed; OpenAI's GPT-3, released in June 2020, was one of the first large language models, and ChatGPT, released in November 2022, brought the technology to a mass audience.[^s2]

## Core tasks and applications

Classic NLP decomposes language into layers of linguistic analysis. Toolkits such as Stanford CoreNLP perform part-of-speech tagging, named-entity recognition, syntactic parsing and coreference resolution, and these annotations feed higher-level applications.[^s1] Major application areas include machine translation, spoken dialogue systems that chain speech recognition, dialogue management and speech synthesis, machine reading and relation extraction that turn text into structured knowledge, social-media mining, and sentiment and emotion analysis.[^s1] Everyday deployments include predictive text, voice-operated navigation, customer-service chatbots, search auto-completion and social-media monitoring.[^s2]

A standard textbook reflects how the field's centre of gravity has moved. The August 2026 draft of Jurafsky and Martin's *Speech and Language Processing* (3rd edition) opens with a volume on large language models (tokens, n-gram models, embeddings, transformers, pretraining and post-training), puts retrieval-augmented generation, agents, translation and speech in a second volume, and moves classic structure-annotation tasks such as parsing, sequence labeling, coreference and semantic role labeling to a third.[^s4]

## Limitations and open problems

Ambiguity, context and world knowledge remain the core difficulty. Writing in 2015, Hirschberg and Manning argued that the hardest problems of semantics, context and knowledge would probably need new advances in linguistics and inference, and noted that most tools covered only a few high-resource languages, leaving many low-resource languages under-served.[^s1] Open-domain dialogue, natural turn-taking and response latency were also unsolved then, and machine translation lacked discourse awareness.[^s1] Modern neural models raise further concerns: they absorb biases from training data, as when an Amazon résumé-screening system was found in 2015 to disadvantage women, and probability-driven generators can produce fluent but false text rather than admitting ignorance.[^s2] Britannica stresses that such models produce humanlike output through statistical patterns without truly understanding language, a point still debated by researchers.[^s2]

## Connections

NLP is one of the main subfields of **artificial intelligence** and, since the statistical turn, has been built on **machine learning**; its current methods were reshaped by **deep learning**, as the shift from feature engineering to learned representations shows.[^s1][^s3] Learned word and sentence **embeddings** and the **transformer architecture** are its central modern tools, and **large language models** now underpin most tasks, which is why a standard textbook is now organized around them.[^s4] Machine translation, named-entity recognition and sentiment analysis are long-standing task areas within the field.[^s1] It overlaps with **information retrieval** (search and question answering) and with **automatic speech recognition** in spoken dialogue systems,[^s1] and **ELIZA** is linked as an example of the hand-written-rule era described above.[^s1][^s2]

## Sources
[^s1]: J. Hirschberg and C. D. Manning, "Advances in natural language processing", Science 349(6245):261–266, 2015. https://nlp.cs.princeton.edu/cos484-sp22/readings/advances_in_nlp.pdf (accessed 2026-11-15)
[^s2]: "Natural language processing", Encyclopaedia Britannica. https://www.britannica.com/technology/natural-language-processing-computer-science (accessed 2026-11-15)
[^s3]: R. Collobert et al., "Natural Language Processing (Almost) from Scratch", JMLR 12:2493–2537, 2011. https://jmlr.org/papers/v12/collobert11a.html (accessed 2026-11-15)
[^s4]: D. Jurafsky and J. H. Martin, "Speech and Language Processing (3rd ed. draft)", Stanford University. https://web.stanford.edu/~jurafsky/slp3/ (accessed 2026-11-15)
