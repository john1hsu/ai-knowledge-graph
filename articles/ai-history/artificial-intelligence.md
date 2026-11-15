---
id: kt:artificial-intelligence
type: Field
title: Artificial intelligence
aliases: [AI, machine intelligence]
domain: ai-history
summary: >-
  The field of computer science that builds machines, especially computer programs, able to perform tasks
  associated with intelligent beings, such as learning, reasoning, problem solving, perception and language;
  the term was coined by John McCarthy in 1955.
maturity: foundational
broader: [kt:computer-science]
related: [kt:symbolic-ai, kt:connectionism, kt:dartmouth-workshop, kt:turing-test, kt:ai-agent, kt:ai-governance]
relations:
  - {predicate: hasPart, object: kt:machine-learning}
  - {predicate: hasPart, object: kt:computer-vision}
  - {predicate: hasPart, object: kt:natural-language-processing}
  - {predicate: influencedBy, object: kt:john-mccarthy}
sources:
  - id: s1
    title: "What is Artificial Intelligence? — Basic Questions"
    publisher: John McCarthy, Stanford University (revised 2007-11-12)
    url: https://www-formal.stanford.edu/jmc/whatisai/node1.html
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "Artificial intelligence"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/technology/Artificial-intelligence
    type: encyclopedia
    accessed: 2026-11-15
  - id: s3
    title: "Artificial intelligence — Methods and goals in AI"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/technology/artificial-intelligence/Methods-and-goals-in-AI
    type: encyclopedia
    accessed: 2026-11-15
  - id: s4
    title: "Updates to the OECD's definition of an AI system explained"
    publisher: S. Russell, K. Perset, M. Grobelnik, OECD.AI (2023-11-29)
    url: https://oecd.ai/en/wonk/ai-system-definition-update
    type: intergovernmental
    accessed: 2026-11-15
  - id: s5
    title: "Artificial Intelligence: A Modern Approach (3rd ed.) — Preface"
    publisher: Stuart Russell and Peter Norvig, UC Berkeley
    url: https://aima.cs.berkeley.edu/3rd-ed/preface.html
    type: textbook
    accessed: 2026-11-15
  - id: s6
    title: "AI Index 2025: State of AI in 10 Charts"
    publisher: Stanford Institute for Human-Centered AI (HAI)
    url: https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts
    type: academic
    accessed: 2026-11-15
  - id: s7
    title: "John McCarthy"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/biography/John-McCarthy
    type: encyclopedia
    accessed: 2026-11-15
created: 2026-11-15
---

# Artificial intelligence

**Artificial intelligence (AI)** is the branch of computer science concerned with building machines that do things we would call intelligent if people did them. John McCarthy, who coined the term in 1955, described it as "the science and engineering of making intelligent machines," and defined intelligence itself as the computational part of the ability to achieve goals in the world.[^s1][^s7] Britannica frames AI similarly, as the ability of a digital computer or computer-controlled robot to carry out tasks commonly associated with intelligent beings.[^s2]

## What counts as intelligence

AI research has concentrated on a handful of abilities that psychologists treat as components of intelligence: learning (from rote memorisation up to generalising experience to new situations), reasoning (drawing deductive or inductive inferences), problem solving (searching through possible actions toward a goal), perception (interpreting sensory input, as in object recognition or driving), and language use.[^s2] McCarthy stressed that AI does not have to imitate people: researchers study the problems the world poses to intelligence and are free to use methods that are not observed in humans or animals.[^s1] The standard textbook by Russell and Norvig organises the whole field around the **intelligent agent**, a system that receives percepts from an environment and acts on it, with each agent design implementing a mapping from percept sequences to actions.[^s5]

Policy bodies have needed a more operational definition. In November 2023 OECD member countries approved a revised definition describing an AI system as a machine-based system that, for explicit or implicit objectives, infers from its input how to generate outputs such as predictions, content, recommendations or decisions that can influence physical or virtual environments; systems differ in how autonomous and adaptive they are after deployment.[^s4] Compared with the 2019 wording, the update allows objectives to be implicit (for example, learned rather than stated), names "content" as an output so generative AI is clearly covered, and emphasises inference from input.[^s4]

## Approaches and goals

Two broad research traditions run through AI's history. The **symbolic** or top-down approach models intelligence as the manipulation of symbols, independent of the brain's biology; Newell and Simon summarised it in 1957 as the physical symbol system hypothesis.[^s3] The **connectionist** or bottom-up approach builds artificial neural networks loosely modelled on the brain and adjusts them through training, building on ideas from Thorndike and Hebb about learning as changing connections between neurons.[^s3] Britannica notes that both were pursued in the 1950s and 1960s, that interest swung between them over the following decades, and that each has limits: symbolic systems often fail outside controlled settings, while connectionist models remain far from replicating even very small nervous systems.[^s3]

Britannica also distinguishes three goals. **Artificial general intelligence** (strong AI) aims at machines with human-level overall intellectual ability; whether scaling language models can reach it, or whether a different approach is needed, is actively debated. **Applied AI** builds commercially useful "smart" systems such as diagnostic or trading software and has been the most successful strand. **Cognitive simulation** uses computers to test theories of human cognition, such as face recognition or memory recall.[^s3]

## The field today

Most current progress comes from machine learning, especially deep neural networks, and from large language models that respond fluently in human languages.[^s2] Stanford HAI's 2025 AI Index reported that the share of surveyed organisations using AI rose from 55% in 2023 to 78% in 2024, and that US private AI investment reached $109 billion in 2024, about 12 times China's $9.3 billion.[^s6] The same report counted 40 notable AI models from US institutions in 2024 versus 15 from China, found the cost of querying a GPT-3.5-level model fell more than 280-fold between November 2022 and October 2024, and recorded 233 reported AI incidents in 2024, a record.[^s6] Regulation is growing alongside adoption: the index counted 131 US state AI laws passed in 2024, more than double the previous year.[^s6]

## Connections

AI is a subfield of **computer science** whose main branches include **machine learning**, **computer vision** and **natural language processing**, all of which address the components of intelligence listed above.[^s2][^s5] Its name traces to **John McCarthy**, who coined it in 1955 while at Dartmouth; the founding meeting is covered in the **Dartmouth workshop** node, and the **Turing test** is the best-known behavioural criterion proposed for machine intelligence.[^s7][^s2] **Symbolic AI** and **connectionism** are its two historic methodological camps.[^s3] The textbook framing of AI as the design of rational **AI agents** links the field to modern agentic systems, and the OECD definition underpins much of contemporary **AI governance**.[^s5][^s4]

## Sources
[^s1]: J. McCarthy, "What is Artificial Intelligence? — Basic Questions", Stanford University (rev. 2007). https://www-formal.stanford.edu/jmc/whatisai/node1.html (accessed 2026-11-15)
[^s2]: "Artificial intelligence", Encyclopaedia Britannica. https://www.britannica.com/technology/Artificial-intelligence (accessed 2026-11-15)
[^s3]: "Artificial intelligence — Methods and goals in AI", Encyclopaedia Britannica. https://www.britannica.com/technology/artificial-intelligence/Methods-and-goals-in-AI (accessed 2026-11-15)
[^s4]: S. Russell, K. Perset, M. Grobelnik, "Updates to the OECD's definition of an AI system explained", OECD.AI, 29 Nov 2023. https://oecd.ai/en/wonk/ai-system-definition-update (accessed 2026-11-15)
[^s5]: S. Russell and P. Norvig, *Artificial Intelligence: A Modern Approach*, 3rd ed., Preface. https://aima.cs.berkeley.edu/3rd-ed/preface.html (accessed 2026-11-15)
[^s6]: Stanford HAI, "AI Index 2025: State of AI in 10 Charts" (2025). https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts (accessed 2026-11-15)
[^s7]: "John McCarthy", Encyclopaedia Britannica. https://britannica.com/biography/John-McCarthy (accessed 2026-11-15)
