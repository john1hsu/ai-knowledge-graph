---
id: kt:logic-theorist
type: Model
title: Logic Theorist
aliases: [Logic Theory Machine, LT, Newell-Shaw-Simon Logic Theorist]
domain: ai-history
summary: >-
  A 1955–1957 computer program by Allen Newell, J. C. (Cliff) Shaw and Herbert A. Simon at RAND that searched
  for proofs of propositional-logic theorems from Whitehead and Russell's Principia Mathematica using heuristic
  methods modelled on human problem solving; it is widely regarded as the first artificial intelligence program.
maturity: historical
broader: [kt:symbolic-ai, kt:automated-theorem-proving]
related: [kt:dartmouth-workshop, kt:heuristic-search, kt:ai-agent, kt:turing-test]
relations:
  - {predicate: createdBy, object: kt:allen-newell}
  - {predicate: createdBy, object: kt:herbert-a-simon}
  - {predicate: createdBy, object: kt:cliff-shaw}
  - {predicate: introducedIn, object: kt:the-logic-theory-machine-a-complex-information-processing-system}
  - {predicate: implementedIn, object: kt:information-processing-language}
  - {predicate: followedBy, object: kt:general-problem-solver}
sources:
  - id: s1
    title: "The Logic Theory Machine: A Complex Information Processing System (RAND P-868)"
    publisher: A. Newell and H. A. Simon, RAND Corporation, 1956 (doi:10.7249/P868)
    url: https://www.rand.org/pubs/papers/P868.html
    type: primary
    accessed: 2026-11-12
  - id: s2
    title: "Early Heuristic Programs (ch. 5 of The Quest for Artificial Intelligence)"
    publisher: N. J. Nilsson, Cambridge University Press, 2009 (doi:10.1017/CBO9780511819346.007)
    url: https://www.cambridge.org/core/books/abs/quest-for-artificial-intelligence/early-heuristic-programs/2E2E2219739947C7868D9A68C49A49D1
    type: textbook
    accessed: 2026-11-12
  - id: s3
    title: "Allen Newell"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/biography/Allen-Newell
    type: encyclopedia
    accessed: 2026-11-12
  - id: s4
    title: "The Early History of Automated Deduction"
    publisher: M. Davis, in Handbook of Automated Reasoning, Elsevier, 2001 (author copy hosted by L. C. Paulson, University of Cambridge)
    url: https://lawrencecpaulson.github.io/papers/Early-History-of-ATP.pdf
    type: academic
    accessed: 2026-11-12
  - id: s5
    title: "Executable Archaeology: Reanimating the Logic Theorist from its IPL-V Source"
    publisher: J. Shrager, arXiv:2603.13514, 2026
    url: https://arxiv.org/abs/2603.13514
    type: preprint
    accessed: 2026-11-12
created: 2026-11-12
---

# Logic Theorist

The **Logic Theorist** (LT), also called the Logic Theory Machine, was a program written in 1955–1956 by Allen Newell, J. C. Shaw and Herbert A. Simon at the RAND Corporation to find proofs of theorems in symbolic logic.[^s1][^s5] It is widely described as the first artificial intelligence program.[^s5] Rather than enumerating every possible derivation, it relied on rules of thumb resembling those people use when solving problems, which its authors called heuristics.[^s1] Britannica notes the work was funded mainly by the US Air Force and that LT tackled logic problems including ones from Whitehead and Russell's *Principia Mathematica* (1910–13).[^s3]

## Origin

Newell and Simon's RAND paper P-868 (1956) specified the system in a pseudo-code-like formal language suited to coding on a digital computer; the authors stressed the specification rather than a particular implementation, and presented LT as one step in a research programme of building complex information-processing systems in order to study them empirically.[^s1] A version of the program was coded on RAND's JOHNNIAC computer, named after John von Neumann, around the time of the 1956 Dartmouth workshop.[^s2][^s3] Shrager's 2026 reconstruction of the program's history reports that parts of LT were first hand-simulated, that the first machine-generated proofs came on the JOHNNIAC in late 1956 or early 1957 under the IPL-II language, and that later versions ran on the IBM 704.[^s5] To write LT, Newell and Simon created the Information Processing Language (IPL), an early list-processing language they also used for other early AI programs.[^s3]

## How it works

LT started from the five axioms of propositional logic in *Principia*, represented as symbol structures, and applied transformations until it produced the target theorem.[^s2] Because many transformations were possible at each step, choosing among them was a search problem.[^s2] Its proof methods included substitution, detachment (modus ponens), forward chaining, backward chaining and replacement of subexpressions.[^s5] Working backward from the goal, it generated subproblems whose solution would yield the theorem, and it looked for substitutions that made expressions match.[^s4] Practical limits bounded the search: the IPL-V version caps effort at 20,000 interpreter cycles and holds the subproblem and substitution lists to 50 entries each.[^s5]

The authors contrasted this heuristic approach with a "British Museum algorithm" that blindly generates all proofs until the target appears.[^s4]

## Results and critiques

According to Shrager's account, the 1957 JOHNNIAC runs proved 38 of the first 52 theorems in chapter 2 of *Principia*, and for Theorem 2.85 LT found a shorter proof than the published one, which Simon showed to Russell.[^s5] These figures come from a secondary historical reconstruction rather than a fresh audit of the original 1957 output.[^s5]

Logician Martin Davis argues that the "heuristic versus algorithmic" framing caused confusion, since "heuristic" amounted mainly to giving up a guarantee of success.[^s4] Hao Wang showed that a complete, efficient propositional procedure easily handled the *Principia* examples that stumped LT, and criticised the implication that exhaustive enumeration was the only non-heuristic alternative; Davis counters that efficient proof generation was never LT's aim, which was to model human problem solving.[^s4] Davis also credits LT with making explicit techniques that became standard in automated reasoning, notably forward and backward chaining and goal-directed subproblem generation.[^s4]

## Legacy

LT's successor, the General Problem Solver, first ran in 1957 and generalised the approach with means-ends analysis.[^s3] Newell and Simon shared the 1975 A.M. Turing Award for contributions to artificial intelligence, the psychology of human cognition and list processing.[^s3] In 2026 Shrager wrote a new IPL-V interpreter in Common Lisp and ran LT from code transcribed from E. Stefferud's 1963 RAND re-coding; it proved 16 of 23 attempted theorems, results the author describes as consistent with the original within its search limits.[^s5]

## Connections

- **Broader:** LT is a founding example of **symbolic AI**, manipulating explicit symbol structures, and an early program in **automated theorem proving**.[^s2][^s4]
- **Created by / introduced in:** it was built by **Allen Newell**, **Herbert A. Simon** and **Cliff Shaw** and specified in the RAND paper *The Logic Theory Machine*.[^s1][^s5]
- **Implemented in:** it was written in **Information Processing Language**, created for the purpose.[^s3]
- **Followed by:** the **General Problem Solver** extended its heuristic, goal-directed style to general problems.[^s3]
- **Related:** it was coded around the time of the **Dartmouth workshop**, and its pruned, goal-directed proof search is an early instance of **heuristic search**.[^s2][^s4] Its search over operators toward a goal prefigures the plan-act loop of a modern **AI agent**, and like the **Turing test** it framed intelligence as something a machine's behaviour could exhibit.[^s1][^s3]

## Sources

[^s1]: A. Newell and H. A. Simon, "The Logic Theory Machine: A Complex Information Processing System", RAND P-868, 1956. https://www.rand.org/pubs/papers/P868.html (accessed 2026-11-12)
[^s2]: N. J. Nilsson, "Early Heuristic Programs", ch. 5 of *The Quest for Artificial Intelligence*, Cambridge University Press, 2009. https://www.cambridge.org/core/books/abs/quest-for-artificial-intelligence/early-heuristic-programs/2E2E2219739947C7868D9A68C49A49D1 (accessed 2026-11-12)
[^s3]: "Allen Newell", Encyclopaedia Britannica. https://www.britannica.com/biography/Allen-Newell (accessed 2026-11-12)
[^s4]: M. Davis, "The Early History of Automated Deduction", Handbook of Automated Reasoning, Elsevier, 2001. https://lawrencecpaulson.github.io/papers/Early-History-of-ATP.pdf (accessed 2026-11-12)
[^s5]: J. Shrager, "Executable Archaeology: Reanimating the Logic Theorist from its IPL-V Source", arXiv:2603.13514, 2026. https://arxiv.org/abs/2603.13514 (accessed 2026-11-12)
