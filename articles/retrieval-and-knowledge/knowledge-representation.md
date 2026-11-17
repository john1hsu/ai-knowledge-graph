---
id: kt:knowledge-representation
type: Field
title: Knowledge representation
aliases: [knowledge representation and reasoning, KR&R, KRR]
domain: retrieval-and-knowledge
summary: >-
  The area of AI concerned with encoding what an agent knows in explicit, usually symbolic structures
  (logic, rules, frames, ontologies) and with the automated reasoning that derives implicit conclusions
  from them.
maturity: established
broader: [kt:artificial-intelligence]
related: [kt:symbolic-ai, kt:knowledge-graph, kt:automated-planning]
relations:
  - {predicate: hasPart, object: kt:description-logic}
  - {predicate: enables, object: kt:expert-systems}
  - {predicate: contrastsWith, object: kt:representation-learning}
sources:
  - id: s1
    title: "What Is a Knowledge Representation?"
    publisher: AI Magazine 14(1), 1993, pp. 17-33 (Davis, Shrobe and Szolovits); UMBC course copy
    url: https://courses.cs.umbc.edu/771/papers/davis.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "Knowledge Representation and Reasoning"
    publisher: Morgan Kaufmann / Elsevier, 2004 (Ronald Brachman and Hector Levesque)
    url: https://shop.elsevier.com/books/knowledge-representation-and-reasoning/brachman/978-1-55860-932-7
    type: textbook
    accessed: 2026-11-17
  - id: s3
    title: "A Framework for Representing Knowledge"
    publisher: MIT AI Laboratory, AI Memo 306, June 1974 (Marvin Minsky); MIT DSpace
    url: https://dspace.mit.edu/entities/publication/0eca0164-cb5f-42de-8c86-43f54b23306d
    type: primary
    accessed: 2026-11-17
  - id: s4
    title: "OWL 2 Web Ontology Language Document Overview (Second Edition)"
    publisher: W3C Recommendation, 11 December 2012
    url: https://www.w3.org/TR/owl2-overview/
    type: standards-body
    accessed: 2026-11-17
  - id: s5
    title: "KR 2026: 23rd International Conference on Principles of Knowledge Representation and Reasoning"
    publisher: KR Inc. (Lisbon, 20-23 July 2026)
    url: https://kr.org/KR2026/
    type: academic
    accessed: 2026-11-17
created: 2026-11-17
---

# Knowledge representation

**Knowledge representation** (KR, often *knowledge representation and reasoning*, KR&R) is the part of artificial intelligence that asks what an agent needs to know to behave intelligently, how that knowledge can be written down in a formal, usually symbolic language, and how automated reasoning can put it to use.[^s2] Rather than building intelligence bottom-up from perception, the KR tradition starts from explicit declarative knowledge and derives what is only implicit in it through inference.[^s2][^s5] Brachman and Levesque's 2004 textbook presents the field as a synthesis of roughly fifty years of work and addresses it to AI practitioners as well as to researchers in databases, information retrieval and object-oriented systems.[^s2]

## What a representation does

The most cited answer to "what is a knowledge representation?" comes from Davis, Shrobe and Szolovits (AI Magazine, 1993), who argued that a representation plays five distinct roles at once.[^s1]

1. **A surrogate**: a stand-in for things in the world, so a system can reason about consequences instead of acting them out.[^s1]
2. **A set of ontological commitments**: a decision about which terms and categories to see the world through.[^s1]
3. **A fragmentary theory of intelligent reasoning**: a view of which inferences are sanctioned and which are recommended.[^s1]
4. **A medium for efficient computation**: an organisation of information that makes the recommended inferences tractable.[^s1]
5. **A medium of human expression**: the language people use to tell the system facts and to understand it.[^s1]

Two consequences follow. Because every surrogate simplifies or omits something, any broad reasoning about the natural world will eventually reach wrong conclusions even when the inference itself is sound; soundness only guarantees that the reasoning step is not the source of error.[^s1] And choosing a formalism (logic, rules or frames) is already a commitment that brings some aspects of a domain into focus while blurring others.[^s1]

## Main formalisms

**Logic.** First-order logic is the reference language for stating knowledge, with resolution and Horn-clause reasoning as classic proof procedures; the textbook also treats procedural control of reasoning and rule-based production systems, the machinery behind many expert systems.[^s2]

**Frames and structured descriptions.** Marvin Minsky's 1974 MIT memo proposed *frames*: stored templates for stereotyped situations that a reasoner retrieves and adapts, carrying expectations about what should happen next and what to do when those expectations fail.[^s3] Related frames link into frame-systems, and Minsky applied the idea to vision, language understanding, retrieval and reasoning by analogy.[^s3] Frames fed into object-oriented representation, inheritance hierarchies and the structured descriptions that later became description logics.[^s2]

**Ontology languages.** The W3C's OWL 2 is the standard descendant of that line for the web: it defines classes, properties, individuals and data values with formally defined meaning.[^s4] Its Direct Semantics is compatible with the *SROIQ* description logic, a decidable fragment of first-order logic, and an RDF-based semantics lets the same ontologies be read as RDF graphs.[^s4]

**Beyond classical logic.** Real knowledge is incomplete and uncertain, so the field also covers numerical uncertainty, default reasoning, abductive explanation, and reasoning about actions and planning.[^s2]

## The central trade-off

A recurring theme is that more expressive languages make reasoning computationally harder; Brachman and Levesque close their textbook on exactly this trade-off between expressiveness and tractability.[^s2] OWL 2 builds the trade-off into the standard: its EL, QL and RL profiles each give up expressive power to gain polynomial-time reasoning, query answering over relational databases, or rule-based reasoning directly on RDF triples.[^s4] Picking a representation is therefore an engineering decision as much as a philosophical one, which is the fourth of Davis et al.'s roles in practice.[^s1]

## KR today

KR remains an active research field with its own venue: the International Conference on Principles of Knowledge Representation and Reasoning held its 23rd edition in Lisbon in July 2026, co-located with workshops on description logics and non-monotonic reasoning.[^s5] The organisers list KR's contributions to agents, automated planning, robotics, natural language processing, data management, the semantic web, verification and cybersecurity, and the 2026 programme added a special track pairing KR with machine learning and explanation.[^s5] That pairing reflects the current landscape, in which explicit, inspectable representations such as ontologies and knowledge graphs are combined with learned statistical models rather than competing with them.[^s4][^s5]

## Connections

Knowledge representation is a core field of **artificial intelligence** and the backbone of **symbolic AI**; rule-based **expert systems** were its most visible commercial application.[^s2] **Description logics**, standardised for the web through OWL 2, are one of its main formalisms, and the ontologies they define give **knowledge graphs** their schema and entailment rules.[^s4] Its work on actions and planning underlies **automated planning**.[^s2][^s5] KR contrasts with **representation learning**, in which models discover their own distributed features from data instead of having knowledge written down by hand; the 2026 KR programme's machine-learning track shows the two increasingly meeting.[^s5]

## Sources

[^s1]: Davis, Shrobe and Szolovits, "What Is a Knowledge Representation?", AI Magazine 14(1), 1993. https://courses.cs.umbc.edu/771/papers/davis.pdf (accessed 2026-11-17)
[^s2]: Brachman and Levesque, *Knowledge Representation and Reasoning*, Morgan Kaufmann, 2004. https://shop.elsevier.com/books/knowledge-representation-and-reasoning/brachman/978-1-55860-932-7 (accessed 2026-11-17)
[^s3]: Minsky, "A Framework for Representing Knowledge", MIT AI Memo 306, 1974. https://dspace.mit.edu/entities/publication/0eca0164-cb5f-42de-8c86-43f54b23306d (accessed 2026-11-17)
[^s4]: W3C, "OWL 2 Web Ontology Language Document Overview (Second Edition)", Recommendation, 11 Dec 2012. https://www.w3.org/TR/owl2-overview/ (accessed 2026-11-17)
[^s5]: KR Inc., "KR 2026: 23rd International Conference on Principles of Knowledge Representation and Reasoning". https://kr.org/KR2026/ (accessed 2026-11-17)
