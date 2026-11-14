---
id: kt:ai-winter
type: Event
title: AI winter
aliases: [AI winters, winter of AI]
domain: ai-history
summary: >-
  A period in which funding for and confidence in artificial intelligence research contract sharply after
  ambitious promises go unmet; historians usually identify one in the 1970s, following the 1973 Lighthill report
  and US defense cutbacks, and another from the mid-1980s, after the expert-system and Lisp-machine boom faded.
maturity: historical
broader: [kt:artificial-intelligence]
related: [kt:expert-systems, kt:perceptron, kt:symbolic-ai, kt:machine-learning]
relations:
  - {predicate: influencedBy, object: kt:lighthill-report}
  - {predicate: influencedBy, object: kt:strategic-computing-initiative}
sources:
  - id: s1
    title: "Artificial Intelligence: A General Survey (the Lighthill report)"
    publisher: Sir James Lighthill, for the UK Science Research Council, 1973 (hosted by AIAI, University of Edinburgh)
    url: https://www.aiai.ed.ac.uk/events/lighthill1973/lighthill.pdf
    type: primary
    accessed: 2026-11-14
  - id: s2
    title: "Funding a Revolution: Government Support for Computing Research, ch. 9 Developments in Artificial Intelligence"
    publisher: National Research Council, National Academies Press, 1999
    url: https://www.nationalacademies.org/read/6323/chapter/11
    type: academic
    accessed: 2026-11-14
  - id: s3
    title: "Artificial Intelligence and Life in 2030, Appendix I: A Short History of AI"
    publisher: One Hundred Year Study on Artificial Intelligence (AI100), Stanford University, 2016
    url: https://ai100.stanford.edu/2016-report/appendix-i-short-history-ai
    type: academic
    accessed: 2026-11-14
  - id: s4
    title: "The Quest for Artificial Intelligence, ch. 24 Speed Bumps"
    publisher: Nils J. Nilsson, Cambridge University Press, 2009
    url: https://www.cambridge.org/core/books/quest-for-artificial-intelligence/speed-bumps/2B4303A939E15295F05FF2AA4FB58873
    type: textbook
    accessed: 2026-11-14
  - id: s5
    title: "The Quest for Artificial Intelligence, ch. 23 DARPA's Strategic Computing Program"
    publisher: Nils J. Nilsson, Cambridge University Press, 2009
    url: https://www.cambridge.org/core/books/quest-for-artificial-intelligence/darpas-strategic-computing-program/2DED975CB010E48E9D3E1850A75C7AE4
    type: textbook
    accessed: 2026-11-14
created: 2026-11-14
---

# AI winter

An **AI winter** is a stretch of time in which money, institutional support and public enthusiasm for artificial intelligence research shrink, usually after the field has promised more than it could deliver. The label is a retrospective, informal one rather than a precisely dated event: Nils Nilsson's history of the field describes how outside attacks and disappointment by the mid-1980s helped bring on what some called an AI winter, and the Stanford-hosted AI100 report likewise says that in the mid-1980s interest dropped and funding dried up.[^s3][^s4] Two episodes are usually singled out: a downturn in the 1970s and a second, deeper one beginning in the mid-to-late 1980s.[^s2][^s3]

## The first winter: the 1970s

In the 1960s the US Defense Department's ARPA, through its Information Processing Techniques Office founded in 1962, supplied most American AI funding and dramatically enlarged the field, often with little direction attached.[^s2] That changed around 1969. The Mansfield Amendment, attached to the 1970 defense authorization, limited Pentagon support to basic research with a direct and apparent military use, and some computer-science programmes were shifted to the National Science Foundation.[^s2] When ARPA's director formalised an AI programme in 1969, researchers faced closer scrutiny and reporting demands.[^s2]

In Britain the turning point was a review commissioned by the Science Research Council from the applied mathematician Sir James Lighthill, published in 1973. Lighthill divided AI into advanced automation (A), computer-based studies of the central nervous system (C) and a "bridge" category of robot-building (B) meant to link them.[^s1] He judged progress in category B the most disappointing, argued that the **combinatorial explosion** of possibilities defeated general problem-solving methods, and predicted that the field would fragment, with successful work absorbed into its application areas.[^s1] The report prompted the US Defense Department to commission its own review of DARPA's AI work, after which DARPA moved money away from robotics and towards mission-oriented projects; the National Research Council notes that witnesses disagreed about how much the report affected American funding.[^s2]

A concrete casualty was DARPA's Speech Understanding Research programme. Launched in 1971 at about $3 million a year for five years, it produced demonstration systems, but disputes about how they were tested led some managers to regard it as a failure, and DARPA ended it without funding the planned follow-on.[^s2]

## The second winter: the late 1980s

Funding recovered in the early 1980s on two fronts. Expert systems, descended from DENDRAL and MYCIN, became a hot research topic and then a commercial product.[^s2] And DARPA's **Strategic Computing** programme, announced in 1983 and partly a response to Japan's Fifth Generation Computer Systems project, committed $1 billion over a planned decade to integrate AI with advances in architecture and networking.[^s2][^s5] According to the National Research Council, total federal AI funding including Strategic Computing rose from $106 million in 1984 to $274 million in 1988.[^s2]

The boom proved fragile. Critics found expert systems brittle outside their narrow domains, contractors struggled to meet Strategic Computing's milestones, and the market for specialised Lisp machines collapsed once cheaper general-purpose engineering workstations, especially from Sun Microsystems, caught up.[^s2] High-performance computing priorities then moved away from AI towards other "grand challenges" such as weather modelling.[^s2] The AI100 panel attributes the gap between promise and practice partly to too little grounding in real sensor data and an overreliance on true/false logic rather than quantified uncertainty.[^s3]

## Recovery and lessons

AI100 describes a resurgence in the 1990s built on systems grounded in real tasks, cheaper sensing hardware, growing data and compute, and statistical machine learning, which it calls the key contributor to the field's later surge.[^s3] The commonly drawn lessons concern expectations management: the National Research Council history cites Stefik's warning against prematurely imposing short-term goals and milestones on an underdeveloped field, and Licklider's view that speech understanding was simply ahead of its time.[^s2]

## Connections

AI winters bracket the era of `kt:symbolic-ai`: the second one followed the commercial peak of `kt:expert-systems`, whose brittleness was a central complaint.[^s2] The `kt:perceptron` belongs to the earlier optimism that later cooled. The `kt:lighthill-report` and the `kt:strategic-computing-initiative` are the two documented influences on funding traced above, and the recovery came largely through `kt:machine-learning`.[^s1][^s2][^s3] All of these sit under `kt:artificial-intelligence` as episodes in its history.

## Sources
[^s1]: J. Lighthill, "Artificial Intelligence: A General Survey", Science Research Council, 1973. https://www.aiai.ed.ac.uk/events/lighthill1973/lighthill.pdf (accessed 2026-11-14)
[^s2]: National Research Council, *Funding a Revolution*, ch. 9, National Academies Press, 1999. https://www.nationalacademies.org/read/6323/chapter/11 (accessed 2026-11-14)
[^s3]: AI100 Study Panel, "Artificial Intelligence and Life in 2030", Appendix I, Stanford University, 2016. https://ai100.stanford.edu/2016-report/appendix-i-short-history-ai (accessed 2026-11-14)
[^s4]: N. J. Nilsson, *The Quest for Artificial Intelligence*, ch. 24, Cambridge University Press, 2009. https://www.cambridge.org/core/books/quest-for-artificial-intelligence/speed-bumps/2B4303A939E15295F05FF2AA4FB58873 (accessed 2026-11-14)
[^s5]: N. J. Nilsson, *The Quest for Artificial Intelligence*, ch. 23, Cambridge University Press, 2009. https://www.cambridge.org/core/books/quest-for-artificial-intelligence/darpas-strategic-computing-program/2DED975CB010E48E9D3E1850A75C7AE4 (accessed 2026-11-14)
