---
id: kt:information-retrieval
type: Field
title: Information retrieval
aliases: [IR, document retrieval, text retrieval]
domain: retrieval-and-knowledge
summary: >-
  The field concerned with finding material, usually documents, of an unstructured nature that satisfies an
  information need from within large collections, typically by indexing the collection and ranking items by
  estimated relevance to a query.
maturity: foundational
broader: [kt:information-science, kt:natural-language-processing]
related: [kt:bm25, kt:tf-idf, kt:semantic-search, kt:retrieval-augmented-generation]
relations:
  - {predicate: hasPart, object: kt:inverted-index}
  - {predicate: hasPart, object: kt:vector-space-model}
  - {predicate: evaluatedOn, object: kt:trec}
sources:
  - id: s1
    title: "Introduction to Information Retrieval (online edition), Chapter 1: Boolean retrieval"
    publisher: Manning, Raghavan and Schütze, Cambridge University Press (2008); online edition hosted by Stanford NLP Group
    url: https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf
    type: textbook
    accessed: 2026-11-12
  - id: s2
    title: "On the history of evaluation in IR"
    publisher: Stephen Robertson, Journal of Information Science 34(4), 439-456 (2008); author preprint hosted by City, University of London
    url: https://www.staff.city.ac.uk/~sbrp622/papers/JIS_history_preprint.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s3
    title: "A Vector Space Model for Automatic Indexing"
    publisher: Salton, Wong and Yang, Communications of the ACM 18(11), 613-620 (1975); copy hosted by University of Maryland course CMSC 828R
    url: https://www.cs.umd.edu/class/fall2009/cmsc828r/PAPERS/VSM_salton-2.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "Text REtrieval Conference (TREC) Overview"
    publisher: National Institute of Standards and Technology (NIST)
    url: https://trec.nist.gov/overview.html
    type: government
    accessed: 2026-11-12
  - id: s5
    title: "Dense Passage Retrieval for Open-Domain Question Answering"
    publisher: Karpukhin et al., Proceedings of EMNLP 2020, 6769-6781 (ACL Anthology)
    url: https://aclanthology.org/2020.emnlp-main.550
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s6
    title: "Information retrieval"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/print/article/1379580
    type: encyclopedia
    accessed: 2026-11-12
created: 2026-11-12
---

# Information retrieval

**Information retrieval (IR)** is the study and engineering of systems that find material, usually documents, of an unstructured nature that satisfies a user's information need from within a large collection, usually stored on computers.[^s1] Unlike a database query, which returns exactly the records matching a structured condition, an IR system works over free text and must judge *relevance*, which is why ranking and evaluation sit at the centre of the field.[^s1][^s2] Britannica describes the two classic access routes as keyword searching against an index and traversal of hypertext links, with web search engines now combining both with language processing.[^s6] Manning, Raghavan and Schütze's textbook argued in 2008 that IR was fast becoming the dominant form of information access, overtaking database-style searching.[^s1]

## Scope and core machinery

The textbook distinguishes three scales of system: web search over billions of documents, personal search (desktop, email, spam filtering) and enterprise or domain-specific search over collections such as patents or research articles.[^s1] At every scale, scanning each document at query time is too slow, so collections are **indexed in advance**. The standard structure is the **inverted index**: a dictionary of terms, each pointing to a postings list of the documents that contain it.[^s1] Early systems answered **Boolean** queries (AND, OR, NOT over terms); modern systems instead return a **ranked list**, scoring documents by how well they match the query.[^s1]

Ranking models grew out of two main traditions. Gerard Salton's **SMART** project, begun at Harvard in the early 1960s and based mostly at Cornell, pioneered automatic text indexing, document scoring and ranking, cosine similarity in a vector space, TF-IDF weighting and Rocchio relevance feedback.[^s2] In the 1975 vector space paper, Salton, Wong and Yang represented each document as a vector of weighted index terms and measured similarity by inner product or vector angle; they reported that indexing which spread documents apart in that space improved recall and precision, and that medium-frequency terms were the best discriminators.[^s3] The parallel **probabilistic** tradition, which estimates the probability that a document is relevant, later produced BM25.[^s2]

## Evaluation: the Cranfield paradigm

IR is unusual among computing fields in having had a rigorous experimental methodology since the 1960s. Cyril Cleverdon's **Cranfield experiments** (1958-1966, at the Cranfield College of Aeronautics) compared indexing schemes and, in Cranfield 2, set the template still used today: a fixed document collection, a set of queries and human relevance judgments.[^s2] The two foundational measures are **precision**, the fraction of retrieved documents that are relevant, and **recall**, the fraction of relevant documents that were retrieved; Robertson notes that most later measures derive from these two.[^s1][^s2]

NIST scaled this paradigm up with the **Text REtrieval Conference (TREC)**, which began in 1992 as part of the TIPSTER program, co-sponsored with the U.S. Department of Defense.[^s4] Participants run their systems on a shared collection, NIST pools their top-ranked documents and has assessors judge them, and results are discussed at an annual workshop.[^s2][^s4] NIST reports that retrieval effectiveness roughly doubled in TREC's first six years and that 93 groups from 22 countries took part in TREC 2003; TREC also ran the first large-scale evaluations of cross-language retrieval, speech retrieval and open-domain question answering.[^s4]

## Neural IR and the link to AI

Since about 2020 the field has shifted toward learned representations. Karpukhin et al.'s Dense Passage Retrieval (EMNLP 2020) encoded questions and passages separately with a dual encoder and, on open-domain QA benchmarks, beat a strong Lucene-BM25 baseline by 9-19 points absolute in top-20 passage retrieval accuracy, as reported by the authors.[^s5] Such dense retrievers underpin semantic search and are the retrieval stage of retrieval-augmented generation, though lexical methods like BM25 remain the standard baseline they are compared against.[^s5][^s2]

## Limitations and open questions

Relevance is a human judgment, so every test collection embeds the choices of its assessors and queries; in TREC, only the pooled top-ranked documents from participating systems (typically the top 100 from each) are judged at all.[^s2] Even within the Cranfield experiments, how a "good answer" was defined changed between Cranfield 1 and Cranfield 2.[^s2] Web-scale IR also faces adversarial content, as the textbook notes for pages manipulated to rank highly.[^s1]

## Connections

Information retrieval is a branch of **information science** that overlaps heavily with **natural language processing**.[^s1] Its core data structure is the **inverted index**, and the **vector space model** is one of its founding ranking models.[^s1][^s3] **TF-IDF** came out of the SMART tradition, and **BM25** out of the probabilistic one.[^s2] Systems are **evaluated on** **TREC** test collections in the Cranfield tradition.[^s2][^s4] **Semantic search** with dense embeddings is its neural extension, and **retrieval-augmented generation** uses IR systems as the retrieval stage for language models.[^s5]

## Sources

[^s1]: Manning, Raghavan and Schütze, *Introduction to Information Retrieval*, Cambridge University Press (2008), online edition, Chapter 1. https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf (accessed 2026-11-12)
[^s2]: Robertson, "On the history of evaluation in IR", Journal of Information Science 34(4), 439-456 (2008). https://www.staff.city.ac.uk/~sbrp622/papers/JIS_history_preprint.pdf (accessed 2026-11-12)
[^s3]: Salton, Wong and Yang, "A Vector Space Model for Automatic Indexing", Communications of the ACM 18(11), 613-620 (1975). https://www.cs.umd.edu/class/fall2009/cmsc828r/PAPERS/VSM_salton-2.pdf (accessed 2026-11-12)
[^s4]: NIST, "Text REtrieval Conference (TREC) Overview". https://trec.nist.gov/overview.html (accessed 2026-11-12)
[^s5]: Karpukhin et al., "Dense Passage Retrieval for Open-Domain Question Answering", Proceedings of EMNLP 2020, 6769-6781. https://aclanthology.org/2020.emnlp-main.550 (accessed 2026-11-12)
[^s6]: Encyclopaedia Britannica, "Information retrieval". https://britannica.com/print/article/1379580 (accessed 2026-11-12)
