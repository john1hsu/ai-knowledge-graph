---
id: kt:tf-idf
type: Technique
title: TF-IDF
aliases: [term frequency–inverse document frequency, tf*idf, tf·idf weighting, inverse document frequency weighting]
domain: retrieval-and-knowledge
summary: >-
  A term-weighting scheme that scores a word's importance to a document by multiplying how often it occurs in
  that document (term frequency) by the logarithm of how rare it is across the collection (inverse document
  frequency), so frequent-but-distinctive words dominate a document's vector.
maturity: foundational
broader: [kt:information-retrieval]
related: [kt:semantic-search, kt:embeddings]
relations:
  - {predicate: createdBy, object: kt:karen-sparck-jones}
  - {predicate: usedIn, object: kt:vector-space-model}
  - {predicate: supersededBy, object: kt:bm25}
  - {predicate: implementedIn, object: kt:apache-lucene}
sources:
  - id: s1
    title: "A statistical interpretation of term specificity and its application in retrieval"
    publisher: Karen Spärck Jones, Journal of Documentation 28(1), 11-21 (1972); 2004 reprint hosted by City, University of London
    url: https://www.staff.city.ac.uk/~sb317/idfpapers/ksj_orig.pdf
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "Term-weighting approaches in automatic text retrieval"
    publisher: Gerard Salton and Christopher Buckley (Cornell University), Information Processing & Management 24(5), 513-523 (1988)
    url: https://www.marilia.unesp.br/Home/Instituicao/Docentes/EdbertoFerneda/MRI%2004%20-%20Salton,%20G;%20Buckley,%20C%20-%201988.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s3
    title: "Understanding inverse document frequency: on theoretical arguments for IDF"
    publisher: Stephen Robertson, Journal of Documentation 60(5), 503-520 (2004); author copy hosted by City, University of London
    url: https://www.staff.city.ac.uk/~sbrp622/idfpapers/Robertson_idf_JDoc.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "Introduction to Information Retrieval, ch. 6: References and further reading"
    publisher: Manning, Raghavan and Schütze, Cambridge University Press (2008), online edition, Stanford NLP Group
    url: https://nlp.stanford.edu/IR-book/html/htmledition/references-and-further-reading-6.html
    type: textbook
    accessed: 2026-11-09
  - id: s5
    title: "sklearn.feature_extraction.text.TfidfTransformer"
    publisher: scikit-learn developers (dev documentation)
    url: https://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html
    type: official-docs
    accessed: 2026-11-09
  - id: s6
    title: "Class TFIDFSimilarity"
    publisher: Apache Lucene Core API documentation
    url: https://lucene.apache.org/core/api/core/org/apache/lucene/search/similarities/TFIDFSimilarity.html
    type: official-docs
    accessed: 2026-11-09
created: 2026-11-09
---

# TF-IDF

**TF-IDF** (term frequency–inverse document frequency) is the classic way to decide how much a word should count when representing or matching a document. A term's weight rises with the number of times it occurs in the document and falls with the number of documents in the collection that contain it, so a word that is common in one document but rare overall gets the most weight.[^s2][^s3] It was the workhorse of keyword search and text classification for decades and is still the default baseline vectorizer in machine-learning toolkits.[^s5]

## Origin

The idf half came first. In a 1972 *Journal of Documentation* paper, Karen Spärck Jones argued that a term's "specificity" could be treated statistically: a term attached to many documents discriminates poorly, however precise its meaning.[^s1] She weighted terms by collection frequency using an integer, base-2 approximation (for *N* documents and a term occurring in *n*, roughly log₂*N* − log₂*n* + 1) and showed on the Cranfield, INSPEC and Keen test collections that weighted matching clearly beat unweighted matching, while simply dropping frequent terms hurt recall badly.[^s1] Manning, Raghavan and Schütze trace earlier hints to Luhn's work in the late 1950s on favouring medium-frequency words.[^s4]

Combining idf with within-document term frequency emerged empirically, largely from Gerard Salton's SMART group at Cornell.[^s3][^s4] Salton and Buckley's 1988 study tested 1,800 weighting combinations (287 distinct) across six collections and recommended tf × idf with cosine length normalization for documents, concluding that well-weighted single terms generally outperformed more elaborate representations such as phrases and thesauri.[^s2]

## How it works

For term *t*, document *d* and a collection of *N* documents, of which df(*t*) contain *t*:[^s2][^s3]

  tf-idf(*t*, *d*) = tf(*t*, *d*) × log(*N* / df(*t*))

Each document becomes a vector with one weight per vocabulary term; vectors are usually normalized to unit length, and query–document relevance is their cosine similarity.[^s2] Small example: in 1,000 documents, "neural" appears in 10 and "the" in all 1,000. One occurrence of "neural" earns log(100) ≈ 4.6 (natural log), while any number of "the" earns log(1) = 0.

Many variants exist, which is why the SMART notation codes each component (tf form, idf form, normalization) with letters such as *ltc* or *nfx*.[^s2][^s4] Common choices include binary or logarithmic tf, smoothed idf and pivoted length normalization.[^s4] scikit-learn, for instance, defaults to idf = ln((1 + *N*)/(1 + df)) + 1 with L2 normalization and optional 1 + log(tf) scaling, and its documentation notes this departs from textbook idf.[^s5] Lucene's classic scorer uses √tf, a similar smoothed idf and a length norm that deliberately keeps some document-length information instead of strict unit vectors.[^s6]

## Limitations and theory

TF-IDF was long regarded as a heuristic. Robertson's 2004 review argues that attempts to justify idf through Zipf's law or Shannon information theory are weak, and that its best justification is the Robertson/Spärck Jones relevance weight, which reduces to an idf form when no relevance judgments are available; the BM25 model then supplies a principled tf component.[^s3] Raw tf grows linearly, so a term repeated many times can swamp a score, and naive normalization treats long documents inconsistently, problems that saturating and pivoted schemes address.[^s3][^s4] Like any bag-of-words method it ignores word order and cannot match synonyms or paraphrases.[^s2]

## In practice

TF-IDF remains a standard first feature extractor for text classification, clustering and keyword extraction, available as `TfidfVectorizer`/`TfidfTransformer` in scikit-learn.[^s5] In search engines it survives as Lucene's `TFIDFSimilarity`/`ClassicSimilarity` scorers, which combine Boolean matching with vector-space cosine scoring.[^s6] In LLM pipelines it appears mostly as a cheap sparse baseline or keyword component alongside dense embeddings.

## Connections

TF-IDF is a core technique of **information retrieval**; its idf component was **created by** Karen Spärck Jones, and its weights are **used in** Salton's **vector space model**, where weighted term vectors are compared by cosine.[^s1][^s2] **BM25** keeps the idf idea but adds saturating tf and length normalization, which is why it is treated here as TF-IDF's **successor**; TF-IDF scoring is still **implemented in Apache Lucene** as its classic similarity.[^s3][^s6] Dense **embeddings** and **semantic search** are the main contrast: they capture meaning beyond exact term overlap, which TF-IDF's sparse vectors cannot.[^s2][^s3]

## Sources

[^s1]: Spärck Jones, "A statistical interpretation of term specificity and its application in retrieval", Journal of Documentation 28(1), 11-21 (1972). https://www.staff.city.ac.uk/~sb317/idfpapers/ksj_orig.pdf (accessed 2026-11-09)
[^s2]: Salton and Buckley, "Term-weighting approaches in automatic text retrieval", Information Processing & Management 24(5), 513-523 (1988). https://www.marilia.unesp.br/Home/Instituicao/Docentes/EdbertoFerneda/MRI%2004%20-%20Salton,%20G;%20Buckley,%20C%20-%201988.pdf (accessed 2026-11-09)
[^s3]: Robertson, "Understanding inverse document frequency: on theoretical arguments for IDF", Journal of Documentation 60(5), 503-520 (2004). https://www.staff.city.ac.uk/~sbrp622/idfpapers/Robertson_idf_JDoc.pdf (accessed 2026-11-09)
[^s4]: Manning, Raghavan and Schütze, Introduction to Information Retrieval, ch. 6 "References and further reading", Cambridge University Press (2008). https://nlp.stanford.edu/IR-book/html/htmledition/references-and-further-reading-6.html (accessed 2026-11-09)
[^s5]: scikit-learn developers, "sklearn.feature_extraction.text.TfidfTransformer". https://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html (accessed 2026-11-09)
[^s6]: Apache Lucene, "Class TFIDFSimilarity", Lucene Core API documentation. https://lucene.apache.org/core/api/core/org/apache/lucene/search/similarities/TFIDFSimilarity.html (accessed 2026-11-09)
