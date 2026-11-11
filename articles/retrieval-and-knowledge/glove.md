---
id: kt:glove
type: Algorithm
title: GloVe
aliases: [Global Vectors for Word Representation, GloVe embeddings, GloVe word vectors]
domain: retrieval-and-knowledge
summary: >-
  A static word-embedding method from Pennington, Socher and Manning at Stanford (EMNLP 2014) that fits word and
  context vectors by weighted least squares so that their dot product approximates the log of how often two words
  co-occur across a whole corpus, uniting count-based matrix factorisation with prediction-style embeddings.
maturity: foundational
broader: [kt:embeddings, kt:representation-learning]
related: [kt:latent-semantic-analysis, kt:semantic-search, kt:named-entity-recognition, kt:algorithmic-bias-and-fairness]
relations:
  - {predicate: introducedIn, object: kt:glove-global-vectors-for-word-representation}
  - {predicate: createdBy, object: kt:stanford-nlp-group}
  - {predicate: alternativeTo, object: kt:word2vec}
  - {predicate: trainedWith, object: kt:adagrad}
  - {predicate: supersededBy, object: kt:transformer-architecture}
sources:
  - id: s1
    title: "GloVe: Global Vectors for Word Representation (full text)"
    publisher: Proceedings of EMNLP 2014, ACL Anthology D14-1162 (Pennington, Socher and Manning), pp. 1532–1543
    url: https://aclanthology.org/D14-1162.pdf
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s2
    title: "GloVe: Global Vectors for Word Representation"
    publisher: Stanford NLP Group project page
    url: https://nlp.stanford.edu/projects/glove/
    type: academic
    accessed: 2026-11-11
  - id: s3
    title: "Improving Distributional Similarity with Lessons Learned from Word Embeddings"
    publisher: Transactions of the Association for Computational Linguistics, vol. 3 (Levy, Goldberg and Dagan), 2015
    url: https://transacl.org/ojs/index.php/tacl/article/viewFile/570/124
    type: peer-reviewed
    accessed: 2026-11-11
  - id: s4
    title: "A New Pair of GloVes"
    publisher: arXiv 2507.18103v1 (Carlson, Bauer and Manning, Stanford), submitted 24 Jul 2025
    url: https://arxiv.org/abs/2507.18103v1
    type: primary
    accessed: 2026-11-11
  - id: s5
    title: "Speech and Language Processing, Chapter 5: Embeddings"
    publisher: Jurafsky and Martin, 3rd edition draft (August 2026 release), Stanford University
    url: https://web.stanford.edu/~jurafsky/slp3/5.pdf
    type: textbook
    accessed: 2026-11-11
created: 2026-11-11
---

# GloVe

**GloVe** (Global Vectors for Word Representation) is an unsupervised method for learning *static* word embeddings, one fixed vector per vocabulary word, from the global word-word co-occurrence counts of a corpus.[^s2] Jeffrey Pennington, Richard Socher and Christopher Manning of Stanford presented it at EMNLP 2014 in Doha.[^s1] Their motivation was to reconcile two families: global matrix-factorisation methods such as latent semantic analysis use corpus statistics efficiently but did poorly on word analogies, while local context-window predictors such as word2vec's skip-gram did well on analogies but learned from one window at a time and so underused the global counts.[^s1] Jurafsky and Martin's textbook describes it as a very widely used static embedding model.[^s5]

## How it works

The starting observation is that *ratios* of co-occurrence probabilities carry meaning better than raw probabilities. In the paper's example from a 6-billion-token corpus, "solid" is about 8.9 times more likely near "ice" than near "steam", "gas" shows the reverse, and words related to both ("water") or neither ("fashion") give ratios close to 1.[^s1] Requiring vector differences to encode such ratios, with word and context roles kept symmetric, leads to the condition that the dot product of a word vector *w_i* and context vector *w̃_j*, plus two bias terms, should equal log *X_ij*, the logarithm of their co-occurrence count.[^s1]

GloVe fits this with a weighted least-squares objective summed over all non-zero matrix entries:

J = Σ f(X_ij) (w_iᵀ w̃_j + b_i + b̃_j − log X_ij)²

The weight f(x) = (x / x_max)^α below a cap, and 1 above it, so pairs that never co-occur contribute nothing and very frequent pairs are not overweighted; the authors used x_max = 100 and α = 3/4, and found 3/4 gave a modest gain over a linear weight.[^s1] Counts were gathered from ten words on each side, with a pair *d* words apart contributing 1/*d*, and the model was trained with AdaGrad on sampled non-zero entries.[^s1] Because the matrix is symmetric, the word and context matrices differ only through random initialisation, so the released vectors are their sum W + W̃.[^s1] Cost scales with the number of non-zero entries rather than corpus length; under a power-law assumption the authors estimated this grows roughly as corpus size to the 0.8 power.[^s1]

## Results and critiques

On the authors' analogy benchmark, 300-dimensional vectors scored 71.7% when trained on 6 billion tokens, against 69.1% for skip-gram and 65.7% for CBOW in their comparison, and 75.0% when trained on 42 billion Common Crawl tokens.[^s1] GloVe also led most word-similarity sets and improved a CRF named-entity recogniser on three of four test sets.[^s1] Returns diminished beyond about 200 dimensions, and small windows favoured syntactic analogies while larger ones helped semantic ones.[^s1]

Those head-to-head claims did not hold up under tighter controls. Levy, Goldberg and Dagan re-ran GloVe, skip-gram with negative sampling (SGNS), PPMI and SVD on the same corpus with matched hyperparameters and found SGNS beat GloVe on every task they tested, with no method holding a consistent edge overall.[^s3] They attributed the gap in the original paper to uncontrolled hyperparameters, a single analogy dataset and differing corpora, and argued that design choices such as context smoothing and adding context vectors often matter more than the algorithm.[^s3]

Like other static embeddings, GloVe gives a word one vector regardless of sense or sentence, which contextual models such as BERT avoid.[^s5] Its vectors also inherit social bias: Caliskan and colleagues reproduced human implicit-association findings using GloVe cosine similarities, including names associated with African Americans sitting closer to unpleasant words, which the textbook treats as a representational harm.[^s5]

## In practice

Stanford distributes the code under Apache 2.0 and pre-trained vectors under a public-domain dedication, including 6-billion-token Wikipedia and Gigaword vectors (400,000 words, 50 to 300 dimensions), 42- and 840-billion-token Common Crawl sets and 27-billion-token Twitter vectors.[^s2] In July 2025 the group added 2024 vectors trained on Wikipedia plus Gigaword (11.9 billion tokens) and on a 220-billion-token Dolma subset, each with a 1.2-million-word vocabulary.[^s2] The accompanying report says these document data versions and preprocessing that the 2014 release left unrecorded, match the originals on analogy and similarity tests, and do better on recent, time-sensitive NER data.[^s4] The report notes that the 2014 vectors were still widely used in 2025, even though contextual models such as BERT now give each occurrence of a word its own vector.[^s4][^s5]

## Connections

GloVe is a way to produce **embeddings** and so an instance of **representation learning**.[^s5] It was **introduced in** its EMNLP 2014 paper and **created by** the **Stanford NLP Group**.[^s1][^s2] It positions itself between count-based **latent semantic analysis** and **word2vec**, its closest **alternative**; Levy and colleagues showed the two perform comparably once tuned alike.[^s1][^s3] It was **trained with AdaGrad**.[^s1] Cosine nearest-neighbour lookup over its vectors is a simple form of **semantic search**, and its gains as input features for a CRF tagger tie it to **named-entity recognition**.[^s1][^s2] Its measured stereotypes make it a reference case in **algorithmic bias and fairness**.[^s5] For most tasks it has been **superseded by** contextual representations from the **transformer architecture**.[^s5]

## Sources

[^s1]: Pennington, Socher and Manning, "GloVe: Global Vectors for Word Representation", EMNLP 2014, pp. 1532–1543. https://aclanthology.org/D14-1162.pdf (accessed 2026-11-11)
[^s2]: Stanford NLP Group, "GloVe: Global Vectors for Word Representation" project page. https://nlp.stanford.edu/projects/glove/ (accessed 2026-11-11)
[^s3]: Levy, Goldberg and Dagan, "Improving Distributional Similarity with Lessons Learned from Word Embeddings", TACL 3 (2015). https://transacl.org/ojs/index.php/tacl/article/viewFile/570/124 (accessed 2026-11-11)
[^s4]: Carlson, Bauer and Manning, "A New Pair of GloVes", arXiv 2507.18103 (2025). https://arxiv.org/abs/2507.18103v1 (accessed 2026-11-11)
[^s5]: Jurafsky and Martin, *Speech and Language Processing*, 3rd ed. draft, Chapter 5 "Embeddings" (August 2026 release). https://web.stanford.edu/~jurafsky/slp3/5.pdf (accessed 2026-11-11)
