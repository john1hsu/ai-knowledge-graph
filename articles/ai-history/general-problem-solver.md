---
id: kt:general-problem-solver
type: Model
title: General Problem Solver
aliases: [GPS, General Problem Solver program, Newell-Shaw-Simon GPS]
domain: ai-history
summary: >-
  An early artificial intelligence program by Allen Newell, J. C. (Cliff) Shaw and Herbert A. Simon, first run
  in 1957, that separated a general problem-solving method — means-ends analysis over goals, operators and
  differences — from the knowledge of any particular task, and doubled as a theory of human problem solving.
maturity: historical
broader: [kt:symbolic-ai, kt:heuristic-search]
related: [kt:automated-planning, kt:planning-in-llms, kt:ai-agent]
relations:
  - {predicate: createdBy, object: kt:allen-newell}
  - {predicate: createdBy, object: kt:herbert-a-simon}
  - {predicate: createdBy, object: kt:cliff-shaw}
  - {predicate: introducedIn, object: kt:report-on-a-general-problem-solving-program}
  - {predicate: precededBy, object: kt:logic-theorist}
  - {predicate: followedBy, object: kt:soar}
sources:
  - id: s1
    title: "General Problem Solver"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/science/General-Problem-Solver
    type: encyclopedia
    accessed: 2026-11-17
  - id: s2
    title: "Report on a General Problem-Solving Program (archival copy, dated 30 December 1958)"
    publisher: A. Newell and H. A. Simon; Edward A. Feigenbaum papers, Stanford University Libraries Special Collections
    url: https://purl.stanford.edu/cq467bm9495
    type: primary
    accessed: 2026-11-17
  - id: s3
    title: "Computer Science as Empirical Inquiry: Symbols and Search (1975 ACM Turing Award Lecture)"
    publisher: A. Newell and H. A. Simon, Communications of the ACM 19(3):113–126, 1976 (course reading copy, CSU Long Beach)
    url: https://home.csulb.edu/~cwallis/382/readings/482/Newell&Simonpssh.1976.html
    type: primary
    accessed: 2026-11-17
  - id: s4
    title: "Paradigms of Artificial Intelligence Programming, Chapter 4: GPS: The General Problem Solver"
    publisher: P. Norvig, Morgan Kaufmann 1992 (author's open edition on GitHub)
    url: https://github.com/norvig/paip-lisp/blob/main/docs/chapter4.md
    type: textbook
    accessed: 2026-11-17
  - id: s5
    title: "Allen Newell"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/biography/Allen-Newell
    type: encyclopedia
    accessed: 2026-11-17
created: 2026-11-17
---

# General Problem Solver

The **General Problem Solver (GPS)** was a computer program built by Allen Newell and Herbert A. Simon, working with J. C. (Cliff) Shaw, whose first version ran in 1957; the project continued for roughly a decade.[^s1][^s5] Its ambition is in its name: rather than encoding a strategy for one puzzle, GPS tried to capture a single, task-independent method that could be pointed at many kinds of formally stated problems. It solved puzzles, logical proofs, mathematical word problems and theorems, provided the problems were fairly well structured.[^s1]

## Origin

GPS grew directly out of the same team's Logic Theorist (1956), the theorem prover that searched selectively for proofs from *Principia Mathematica*.[^s5] The group's write-up, *Report on a General Problem-Solving Program*, survives in Stanford's special collections as a 30-page paper dated 30 December 1958.[^s2] In their 1975 Turing Award lecture, Newell and Simon described GPS as perhaps the first program to separate general problem-solving mechanisms from the requirements of particular tasks, and said that many of its mechanisms came from analysing transcripts of human subjects thinking aloud while they solved problems.[^s3] The project was therefore both an engineering effort and a psychological theory, and research on its approach led Newell and Simon to propose a general theory of human problem solving, published in 1972.[^s1][^s5]

## How it works

The core of GPS is **means-ends analysis**. The program compares the current situation with the goal, identifies the differences between them, and selects an operator known to reduce one of those differences; if that operator cannot yet be applied, satisfying its preconditions becomes a new subgoal, and the process recurses.[^s3][^s4] Newell and Simon called means-ends analysis central to the structure of GPS, and noted that the original program paired it with a modified depth-first search rather than best-first search.[^s3] Britannica summarises the same loop as repeatedly applying heuristic rules of thumb and checking after each step whether the program had moved closer to the goal.[^s1]

Peter Norvig's textbook reconstruction makes the mechanism concrete. Each operator is a record with an action, a list of preconditions, an add-list of conditions it makes true and a delete-list of conditions it makes false; a state is a set of conditions. To get a child to school, for example, the "drive son to school" operator requires that the son is at home and the car works, adds "son at school" and deletes "son at home". If the car does not work, fixing it becomes a subgoal.[^s4] Norvig notes that this operator format follows the later STRIPS planner rather than the exact 1950s implementation.[^s4]

## Limitations and critiques

GPS was never as general as its name promised. Norvig argues that its representation could not express problems involving variables, time, costs or uncertain outcomes, and that many interesting problems are computationally hard, so search time grows explosively with problem size; judged by how well it solves problems, he calls it mostly a failure, while crediting it with clarifying what problem solving involves.[^s4] His reconstruction also exposes classic bugs of naive goal-directed search, such as achieving one goal by undoing another already-satisfied goal (the "prerequisite clobbers sibling goal" problem), which requires checking that all goals still hold at the end.[^s4] Britannica likewise notes that critics raised concerns about GPS and similar programs, whose successes were confined to fairly structured problems.[^s1]

## Legacy

GPS's ideas propagated widely. Newell and Simon traced means-ends analysis through many later programs and observed that it was repeatedly reinvented; they also counted planning languages such as PLANNER and CONNIVER among GPS's descendants.[^s3] Norvig places later planners such as Abstrips, Warplan, Nonlin and Tweak in the same line.[^s4] The work fed Newell and Simon's physical symbol system and heuristic search hypotheses, which hold that intelligent systems solve problems by generating and progressively modifying symbol structures.[^s3] Newell's later Soar project, begun in the 1980s, revisited the goal of a general problem-solving architecture built on goals and subgoals.[^s5] Newell and Simon shared the 1975 Turing Award for contributions to AI, the psychology of human cognition and list processing.[^s5]

## Connections

GPS is a landmark of **symbolic AI** and an early, explicit instance of **heuristic search**, the two broader nodes it sits under.[^s3] It was created by **Allen Newell**, **Herbert A. Simon** and **Cliff Shaw**, follows their **Logic Theorist**, and was later succeeded in spirit by Newell's **Soar** architecture.[^s5] Its goal–operator–precondition formulation is the ancestor of classical **automated planning** (via STRIPS-style operators), and the decomposition of goals into subgoals reappears in modern **planning in LLMs** and **AI agent** designs, which pursue the same generality with learned rather than hand-coded knowledge.[^s4]

## Sources
[^s1]: Encyclopaedia Britannica, "General Problem Solver". https://britannica.com/science/General-Problem-Solver (accessed 2026-11-17)
[^s2]: A. Newell and H. A. Simon, "Report on a General Problem-Solving Program", paper dated 30 Dec 1958, Edward A. Feigenbaum papers, Stanford University Libraries. https://purl.stanford.edu/cq467bm9495 (accessed 2026-11-17)
[^s3]: A. Newell and H. A. Simon, "Computer Science as Empirical Inquiry: Symbols and Search", Communications of the ACM 19(3), 1976. https://home.csulb.edu/~cwallis/382/readings/482/Newell&Simonpssh.1976.html (accessed 2026-11-17)
[^s4]: P. Norvig, *Paradigms of Artificial Intelligence Programming*, ch. 4 "GPS: The General Problem Solver". https://github.com/norvig/paip-lisp/blob/main/docs/chapter4.md (accessed 2026-11-17)
[^s5]: Encyclopaedia Britannica, "Allen Newell". https://www.britannica.com/biography/Allen-Newell (accessed 2026-11-17)
