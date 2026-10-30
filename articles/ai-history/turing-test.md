---
id: kt:turing-test
type: Concept
title: Turing test
aliases: [imitation game, Turing's imitation game]
domain: ai-history
summary: >-
  A behavioural test proposed by Alan Turing in 1950 in which a human interrogator converses by text
  with a hidden human and a hidden machine and tries to tell which is which; the machine does well if
  it is mistaken for the human about as often as not.
maturity: foundational
broader: [kt:ai-evaluation, kt:artificial-intelligence]
related: [kt:chinese-room-argument, kt:eliza, kt:large-language-model]
relations:
  - {predicate: introducedIn, object: kt:computing-machinery-and-intelligence}
  - {predicate: createdBy, object: kt:alan-turing}
  - {predicate: contrastsWith, object: kt:chinese-room-argument}
sources:
  - id: s1
    title: "Computing Machinery and Intelligence"
    publisher: A. M. Turing, Mind 59 (236), 1950 (copy hosted for MIT CSAIL course 6.803)
    url: https://courses.csail.mit.edu/6.803/pdf/turing.pdf
    type: primary
    accessed: 2026-10-30
  - id: s2
    title: "The Turing Test (Summer 2006 edition)"
    publisher: Stanford Encyclopedia of Philosophy
    url: https://plato.stanford.edu/archives/sum2006/entries/turing-test/
    type: academic
    accessed: 2026-10-30
  - id: s3
    title: "Turing test"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/Turing-test
    type: encyclopedia
    accessed: 2026-10-30
  - id: s4
    title: "Large Language Models Pass the Turing Test"
    publisher: Jones and Bergen, UC San Diego, arXiv 2503.23674 (authors' version)
    url: https://arxiv.org/abs/2503.23674v1
    type: primary
    accessed: 2026-10-30
created: 2026-10-30
---

# Turing test

The Turing test is a behavioural criterion for machine intelligence proposed by the English mathematician Alan Turing in his 1950 paper "Computing Machinery and Intelligence", published in the philosophy journal *Mind*. Rather than trying to define "thinking", Turing proposed judging a machine by how it behaves in conversation: if a remote interrogator cannot reliably tell it apart from a person, the machine is doing what we would call thinking in a human.[^s1][^s3] Turing himself called it the "imitation game"; the name "Turing test" came later.[^s3]

## How it works

Turing began with a party game. A man (A) and a woman (B) sit in another room from an interrogator (C), who asks them typed questions and must decide which is which; A tries to mislead the interrogator while B tries to help. Typed answers remove clues such as tone of voice. Turing then replaced the vague question "Can machines think?" with a concrete one: what happens when a machine takes the part of A?[^s1] In the form most later writers use, the interrogator questions two hidden witnesses, one human and one machine, and the machine's success is measured by how often it is wrongly judged to be the human.[^s2][^s3]

Turing also made a dated prediction. Within about fifty years, he wrote, computers with a storage capacity of roughly 10^9 could be programmed to play so well that an average interrogator would have no better than a 70 percent chance of a correct identification after five minutes of questioning.[^s1] He anticipated nine objections, including theological, mathematical (Gödel-style limits on discrete machines), consciousness, "Lady Lovelace's" objection that machines only do what they are told, and the informality of human behaviour, and replied to each. The paper closes by proposing "learning machines": instead of programming an adult mind directly, build a simple child machine and educate it with rewards and punishments, an early statement of the idea behind machine learning.[^s1][^s2]

## Critiques

The test has drawn criticism from the start. John Searle's Chinese Room argument imagines a person who knows no Chinese following a rulebook to answer Chinese questions; outsiders might judge the room to pass, yet nothing in it understands Chinese, so passing would not show genuine thought.[^s3][^s2] Ned Block's "Blockhead" thought experiment makes a related point with a giant lookup table that could in principle pass without intelligence, though defenders note that such a table is physically impossible. Others argue the test is too hard and culture-bound (Robert French, 1990), too narrow because it ignores perception and action (Stevan Harnad's "Total Turing Test" adds robotic capacities), or simply a poor research goal for AI (Hayes and Ford, 1995).[^s2] A general difficulty is that any sign of original thought can be dismissed as sophisticated mimicry programmed in by the designers.[^s3]

## In practice

For decades the test served more as a philosophical touchstone than a working benchmark. The Loebner Prize competition ran restricted versions, but the Stanford Encyclopedia of Philosophy's 2006 edition reports that entrants were easily unmasked by simple questioning, and it notes most commentators judged Turing's 70 percent prediction unmet by 2000.[^s2] The release of ChatGPT in late 2022 reopened the question of whether the test's conditions had been met.[^s3]

In a pre-registered study posted in March 2025, Cameron Jones and Benjamin Bergen of UC San Diego ran a three-party version with five-minute chats, using undergraduate and online participants. As reported by the authors, GPT-4.5 prompted to adopt a humanlike persona was picked as the human 73 percent of the time, more often than the real humans; LLaMa-3.1-405B with the same prompt reached 56 percent, while ELIZA (23 percent) and an unprompted GPT-4o (21 percent) scored below chance. The authors caution that results depended on the persona prompt, that interrogators leaned on style and social cues rather than knowledge questions, and that the test measures humanlikeness rather than intelligence directly; as of 2026 the study is an arXiv preprint.[^s4]

## Connections

The Turing test is an early, influential form of **AI evaluation** and a founding idea of **artificial intelligence** as a field, introduced in Turing's paper **Computing Machinery and Intelligence** by **Alan Turing**.[^s1][^s3] It **contrasts with** the **Chinese Room argument**, its best-known philosophical rebuttal.[^s2] **ELIZA**, an early chatbot, and today's **large language models** are the systems most often discussed against it; the 2025 UC San Diego study used ELIZA as a baseline and found persona-prompted LLMs judged human at or above the rate of real people.[^s4]

## Sources
[^s1]: A. M. Turing, "Computing Machinery and Intelligence", Mind 59 (236), 1950. https://courses.csail.mit.edu/6.803/pdf/turing.pdf (accessed 2026-10-30)
[^s2]: "The Turing Test", Stanford Encyclopedia of Philosophy, Summer 2006 edition. https://plato.stanford.edu/archives/sum2006/entries/turing-test/ (accessed 2026-10-30)
[^s3]: "Turing test", Encyclopaedia Britannica. https://www.britannica.com/topic/Turing-test (accessed 2026-10-30)
[^s4]: C. R. Jones and B. K. Bergen, "Large Language Models Pass the Turing Test", arXiv 2503.23674, 2025. https://arxiv.org/abs/2503.23674v1 (accessed 2026-10-30)
