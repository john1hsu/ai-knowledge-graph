---
id: kt:knowledge-graph
type: Concept
title: Knowledge graph
aliases: [KG, knowledge graphs, entity graph]
domain: retrieval-and-knowledge
summary: >-
  A graph of data meant to accumulate and convey knowledge of the real world, in which nodes stand for
  entities and labelled edges for the relations between them, often paired with an ontology or schema
  that fixes what the labels mean.
maturity: established
broader: [kt:knowledge-representation]
related: [kt:named-entity-recognition, kt:retrieval-augmented-generation, kt:semantic-search, kt:embeddings, kt:symbolic-ai]
relations:
  - {predicate: enables, object: kt:graphrag}
  - {predicate: contrastsWith, object: kt:vector-database}
  - {predicate: basedOn, object: kt:resource-description-framework}
  - {predicate: enables, object: kt:knowledge-graph-embedding}
sources:
  - id: s1
    title: "Knowledge Graphs"
    publisher: ACM Computing Surveys 54(4), Article 71, 2021 (Hogan, Blomqvist, Cochez, d'Amato, de Melo, Gutierrez et al.), DOI 10.1145/3447772; university repository copy
    url: https://iris.unibs.it/bitstream/11379/551223/2/3447772.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "Introducing the Knowledge Graph: things, not strings"
    publisher: Google (Amit Singhal), The Keyword blog, 16 May 2012
    url: https://blog.google/products/search/introducing-knowledge-graph-things-not/
    type: lab-research
    accessed: 2026-11-16
  - id: s3
    title: "RDF 1.1 Concepts and Abstract Syntax"
    publisher: W3C Recommendation, 25 February 2014
    url: https://w3.org/TR/rdf11-concepts/
    type: standards-body
    accessed: 2026-11-16
  - id: s4
    title: "Translating Embeddings for Modeling Multi-relational Data"
    publisher: NeurIPS 2013 (Bordes, Usunier, Garcia-Duran, Weston and Yakhnenko)
    url: https://proceedings.neurips.cc/paper/5071-translating-embeddings-for-modeling-multi-rela
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s5
    title: "Wikidata: A Free Collaborative Knowledge Base"
    publisher: Communications of the ACM 57, 2014 (Vrandečić and Krötzsch); Google Research publication page
    url: https://research.google/pubs/wikidata-a-free-collaborative-knowledge-base/
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s6
    title: "Unifying Large Language Models and Knowledge Graphs: A Roadmap"
    publisher: arXiv:2306.08302 v3, Jan 2024 (Pan, Luo, Wang, Chen, Wang and Wu); DOI 10.1109/TKDE.2024.3352100
    url: https://arxiv.org/abs/2306.08302
    type: primary
    accessed: 2026-11-16
created: 2026-11-16
---

# Knowledge graph

A **knowledge graph** (KG) is a graph-structured store of facts about the world. Hogan and colleagues' widely cited survey defines it as a graph of data intended to accumulate and convey real-world knowledge, where nodes represent entities of interest and edges represent relations between them.[^s1] The facts can be as simple as "Paris — capital of → France", but the graph is usually backed by a schema or ontology that says what each node type and edge label means, so that machines can query, validate and reason over the data rather than just match strings.[^s1]

## Origin of the term

The survey traces the phrase "knowledge graph" in the literature back to at least 1972, but its modern usage comes from Google's 2012 announcement, after which Airbnb, Amazon, Microsoft and others described knowledge graphs of their own.[^s1] Google framed its system as a shift to "things, not strings": a model of real-world entities and their relationships that, at launch in May 2012, held more than 500 million objects and over 3.5 billion facts and relationships, drawing on sources such as Freebase and the CIA World Factbook.[^s2] Google said the graph would help search disambiguate entities that share a name, summarise the key facts about an entity, and suggest related entities to explore.[^s2]

## How it works

**Data models.** The survey distinguishes three common models.[^s1] A *directed edge-labelled graph* is a set of nodes joined by labelled edges; the W3C's Resource Description Framework (RDF) is the standard example. In RDF 1.1 every fact is a triple of subject, predicate and object, where the subject is an IRI or blank node, the predicate is an IRI, and the object may also be a literal such as a string or date; an RDF graph is simply a set of such triples.[^s3] RDF datasets add *named graphs*, letting one store keep a single default graph plus any number of graphs identified by name.[^s3] A *heterogeneous graph* assigns each node and edge a type, and a *property graph* (as in Neo4j) lets nodes and edges carry property–value pairs directly.[^s1]

**Schema and reasoning.** Ontology languages such as OWL formally define the meaning of terms, which lets a reasoner entail facts that were never stated (deductive knowledge); shape languages such as SHACL and ShEx validate that the data conforms to an expected structure.[^s1] The survey notes that richer logics trade expressivity against decidability and efficiency, a tension familiar from earlier symbolic AI.[^s1]

**Learning over the graph.** Inductive methods find patterns the schema does not state: graph analytics (centrality, community detection), rule mining scored by support and confidence, graph neural networks, and *knowledge graph embeddings* that map entities and relations to low-dimensional vectors for link prediction.[^s1] The influential TransE model represents each relation as a translation between entity embeddings; its authors reported that this simple, low-parameter model outperformed prior methods on link prediction and scaled to a dataset of about one million entities and 17 million training examples (NeurIPS 2013).[^s4]

## Open and enterprise graphs

Open knowledge graphs include DBpedia, YAGO, BabelNet, Freebase and Wikidata; some are extracted automatically from sources such as Wikipedia, while others are curated by volunteer communities.[^s1] Wikidata, described by its founders in 2014, is a multilingual, collaboratively edited knowledge base that manages the factual data behind Wikipedia.[^s5] Enterprise knowledge graphs are internal to organisations, with prominent uses in web search, e-commerce, social networks and finance.[^s1]

## Limitations and knowledge graphs in the LLM era

Knowledge graphs are hard to build and keep current, so quality assessment and refinement, including machine-learning methods that predict missing links, are an active area of work.[^s1][^s6] Pan et al. (2023–24) contrast them with large language models: LLMs are black boxes that often struggle to capture and access factual knowledge, while KGs store facts explicitly and interpretably but are hard to construct and evolve, and struggle to represent unseen knowledge.[^s6] Their roadmap proposes three patterns: KG-enhanced LLMs (using graphs in pre-training, inference or interpretation), LLM-augmented KGs (using LLMs for embedding, completion, construction and question answering), and synergised systems in which both reason together.[^s6] These remain research directions rather than settled practice as of 2026.

## Connections

A knowledge graph is a form of **knowledge representation**, and its ontologies and description-logic reasoning continue the tradition of **symbolic AI**.[^s1] It is typically built in RDF (**resource description framework**)[^s3] or a property-graph model, populated partly by information-extraction steps such as **named entity recognition**, and exploited by **knowledge graph embeddings** that bridge symbolic facts and **embeddings**.[^s1][^s4] In LLM systems it supplies structured context for **retrieval-augmented generation**, most visibly in **GraphRAG**, and it contrasts with a **vector database**, which retrieves by embedding similarity rather than explicit, typed relations.[^s6] Google's search use made it a backbone of entity-aware **semantic search**.[^s2]

## Sources

[^s1]: Hogan et al., "Knowledge Graphs", ACM Computing Surveys 54(4), 2021. https://iris.unibs.it/bitstream/11379/551223/2/3447772.pdf (accessed 2026-11-16)
[^s2]: Singhal, "Introducing the Knowledge Graph: things, not strings", Google, 16 May 2012. https://blog.google/products/search/introducing-knowledge-graph-things-not/ (accessed 2026-11-16)
[^s3]: W3C, "RDF 1.1 Concepts and Abstract Syntax", Recommendation, 25 Feb 2014. https://w3.org/TR/rdf11-concepts/ (accessed 2026-11-16)
[^s4]: Bordes et al., "Translating Embeddings for Modeling Multi-relational Data", NeurIPS 2013. https://proceedings.neurips.cc/paper/5071-translating-embeddings-for-modeling-multi-rela (accessed 2026-11-16)
[^s5]: Vrandečić and Krötzsch, "Wikidata: A Free Collaborative Knowledge Base", Communications of the ACM 57, 2014. https://research.google/pubs/wikidata-a-free-collaborative-knowledge-base/ (accessed 2026-11-16)
[^s6]: Pan et al., "Unifying Large Language Models and Knowledge Graphs: A Roadmap", arXiv:2306.08302v3, 2024. https://arxiv.org/abs/2306.08302 (accessed 2026-11-16)
