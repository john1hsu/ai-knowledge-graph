---
id: kt:eliza
type: Model
title: ELIZA
aliases: [ELIZA chatbot, DOCTOR (ELIZA script), Weizenbaum's ELIZA]
domain: ai-history
summary: >-
  A natural-language conversation program written by Joseph Weizenbaum at MIT and published in 1966, which
  matched keywords in typed input against an editable script of decomposition and reassembly rules; run with its
  Rogerian-psychotherapist script (DOCTOR), it became the best-known early chatbot.
maturity: historical
broader: [kt:chatbot, kt:natural-language-processing]
related: [kt:turing-test, kt:symbolic-ai, kt:large-language-model, kt:rule-based-system, kt:logic-theorist]
relations:
  - {predicate: createdBy, object: kt:joseph-weizenbaum}
  - {predicate: introducedIn, object: kt:eliza-a-computer-program-for-the-study-of-natural-language-communication-between-man-and-machine}
  - {predicate: causes, object: kt:eliza-effect}
  - {predicate: dependsOn, object: kt:time-sharing}
sources:
  - id: s1
    title: "ELIZA — A Computer Program for the Study of Natural Language Communication Between Man and Machine"
    publisher: J. Weizenbaum, Communications of the ACM 9(1), January 1966 (copy hosted by UMBC CMSC 331)
    url: https://courses.cs.umbc.edu/331/papers/eliza.html
    type: primary
    accessed: 2026-11-12
  - id: s2
    title: "Eliza"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/Eliza
    type: encyclopedia
    accessed: 2026-11-12
  - id: s3
    title: "ELIZA Reanimated: The world's first chatbot restored on the world's first time sharing system"
    publisher: R. Lane, A. Hay, A. Schwarz, D. M. Berry and J. Shrager, arXiv:2501.06707, January 2025
    url: https://arxiv.org/html/2501.06707v1
    type: preprint
    accessed: 2026-11-12
  - id: s4
    title: "Joseph Weizenbaum obituary"
    publisher: MIT News, March 2008
    url: https://news.mit.edu/2008/obit-weizenbaum-0310
    type: news
    accessed: 2026-11-12
  - id: s5
    title: "Joseph Weizenbaum (Computer Pioneers)"
    publisher: IEEE Computer Society History
    url: https://history.computer.org/pioneers/weizenbaum.html
    type: community
    accessed: 2026-11-12
created: 2026-11-12
---

# ELIZA

**ELIZA** is a program that let a person hold a typed conversation in English with a computer. Joseph Weizenbaum of MIT described it in *Communications of the ACM* in January 1966, in work supported in part by Project MAC.[^s1] Britannica counts it among the best-known early AI programs and notes that it simulated a human therapist.[^s2] Weizenbaum named it after the heroine of *My Fair Lady*, and MIT has called it perhaps the first "chatterbot".[^s4]

## How it works

ELIZA ran on MIT's MAC time-sharing system and was written in MAD-SLIP for the IBM 7094; users typed at a remote typewriter and ELIZA typed back.[^s1] The program itself held no knowledge of a topic. Its behaviour came from a **script**, which was data rather than code, so different scripts could be loaded; Weizenbaum mentions scripts in Welsh and German as well as English.[^s1]

Processing a sentence followed a fixed pipeline.[^s1]

- **Keywords and ranks:** the input is scanned left to right for script keywords; each has a rank, and a higher-ranked keyword displaces a lower one already found.[^s1]
- **Decomposition rules:** templates such as `(0 YOU 0 ME)` split the input around the keyword, where 0 matches any number of words.[^s1]
- **Reassembly rules:** the matched fragments are rebuilt into a reply, swapping pronouns (you to I) and adding stock phrases.[^s1]

Weizenbaum named five technical problems the design had to solve: picking the most important keyword, finding its minimal context, choosing a transformation, replying sensibly when no keyword appears, and editing scripts.[^s1] In other words, ELIZA was pattern matching over surface text, an example of the symbol-manipulating approach of early AI.[^s1][^s3]

## The DOCTOR script

The serious scripts of the time imitated a psychotherapist of the Rogerian school. Weizenbaum chose the psychiatric interview because such an interviewer can plausibly seem to know almost nothing about the outside world, which hides the program's ignorance.[^s1] A team that restored the original program in 2025 makes the same point: the DOCTOR persona was picked so that a lack of knowledge would not break the illusion of understanding.[^s3]

## Reception and Weizenbaum's critique

Weizenbaum's stated aim in the 1966 paper was to explain the program so plainly that its apparent intelligence would be seen as a set of procedures.[^s1] He argued that people supply the understanding themselves, crediting the program with background knowledge and reasoning it did not have.[^s1] He was nonetheless surprised that many users took ELIZA seriously and confided in it, and the experience turned him into a critic of AI.[^s4] His 1976 book *Computer Power and Human Reason* warned against handing machines choices that are properly human.[^s4][^s5] He is credited with being among the first to warn of the danger of confusing computers with people, and he publicly accused AI colleagues of overselling the field.[^s5] This tendency of users to read understanding into simple conversational output, which Weizenbaum located on the human side of the exchange, is what later writers call the ELIZA effect.[^s1][^s4]

## Rediscovery and legacy

ELIZA's history was long misremembered. Soon after the 1966 paper, Bernie Cosell at BBN wrote a Lisp clone that spread over the ARPANET, and for about fifty years many assumed ELIZA had been written in Lisp; a 1977 BASIC version in *Creative Computing* became the one most of the public knew.[^s3] In 2021 Jeff Shrager and MIT archivist Myles Crowley found an original MAD-SLIP printout in Weizenbaum's papers.[^s3] Lane and colleagues restored it on an emulated IBM 7094 running a reconstructed CTSS, with a first successful run announced on 21 December 2024; they report the running code is about 96 percent identical to the printout and that it contains a little-documented "teaching" mode for editing scripts during a session.[^s3] The authors argue that ELIZA showed the appearance of AI could be produced without solving intelligence, a point that resonates with today's debate over large language models.[^s3]

## Connections

- **Broader:** ELIZA is a founding example of a **chatbot** and an early system in **natural language processing**.[^s1][^s4]
- **Created by / introduced in:** it was built by **Joseph Weizenbaum** and described in his 1966 CACM paper.[^s1]
- **Depends on:** it relied on the interactive **time-sharing** of Project MAC, which let users converse with a program from a terminal.[^s1][^s3]
- **Causes:** the attribution of understanding it provoked is the origin of the **ELIZA effect**.[^s1][^s3]
- **Related:** like the **Logic Theorist**, it is an artefact of **symbolic AI**, manipulating explicit symbols rather than learning.[^s3] It is a routine reference point in discussions of the **Turing test**, and modern **large language models** are often compared with it.[^s3][^s5] Its hand-written keyword and transformation rules make it a simple **rule-based system**, the opposite of the learned behaviour of today's models.[^s1]

## Sources

[^s1]: J. Weizenbaum, "ELIZA — A Computer Program for the Study of Natural Language Communication Between Man and Machine", Communications of the ACM 9(1), 1966. https://courses.cs.umbc.edu/331/papers/eliza.html (accessed 2026-11-12)
[^s2]: "Eliza", Encyclopaedia Britannica. https://www.britannica.com/topic/Eliza (accessed 2026-11-12)
[^s3]: R. Lane, A. Hay, A. Schwarz, D. M. Berry and J. Shrager, "ELIZA Reanimated: The world's first chatbot restored on the world's first time sharing system", arXiv:2501.06707, 2025. https://arxiv.org/html/2501.06707v1 (accessed 2026-11-12)
[^s4]: "Joseph Weizenbaum" (obituary), MIT News, 2008. https://news.mit.edu/2008/obit-weizenbaum-0310 (accessed 2026-11-12)
[^s5]: "Joseph Weizenbaum", IEEE Computer Society, Computer Pioneers. https://history.computer.org/pioneers/weizenbaum.html (accessed 2026-11-12)
