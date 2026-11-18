---
id: kt:allen-newell
type: Person
title: Allen Newell
aliases: [A. Newell]
domain: ai-history
summary: >-
  American computer scientist and cognitive psychologist (1927–1992) who, with Herbert A. Simon and Cliff Shaw,
  built the Logic Theorist, the General Problem Solver and the IPL list-processing languages, co-formulated the
  physical symbol system hypothesis, and later led the Soar cognitive architecture; co-recipient of the 1975 ACM Turing Award.
maturity: historical
broader: [kt:symbolic-ai]
related: [kt:logic-theorist, kt:general-problem-solver, kt:herbert-a-simon, kt:soar, kt:physical-symbol-system-hypothesis, kt:heuristic-search]
relations:
  - {predicate: influencedBy, object: kt:george-polya}
sources:
  - id: s1
    title: "Allen Newell — A.M. Turing Award Laureate"
    publisher: Association for Computing Machinery (amturing.acm.org)
    url: https://amturing.acm.org/award_winners/newell_3167755.cfm
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "Allen Newell"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/biography/Allen-Newell
    type: encyclopedia
    accessed: 2026-11-18
  - id: s3
    title: "Computer Science as Empirical Inquiry: Symbols and Search (1975 ACM Turing Award Lecture)"
    publisher: A. Newell and H. A. Simon, Communications of the ACM 19(3), 113–126, March 1976 (course-reading copy, California State University Long Beach)
    url: https://home.csulb.edu/~cwallis/382/readings/482/Newell&Simonpssh.1976.html
    type: primary
    accessed: 2026-11-18
  - id: s4
    title: "Towards the Knowledge Level in Soar: The Role of the Architecture in the Use of Knowledge (Technical Report AIP-65)"
    publisher: P. S. Rosenbloom, A. Newell and J. E. Laird, 1989 (Defense Technical Information Center)
    url: https://apps.dtic.mil/sti/pdfs/ADA218926.pdf
    type: primary
    accessed: 2026-11-18
  - id: s5
    title: "Professional History — John E. Laird"
    publisher: University of Michigan, College of Engineering
    url: https://laird.engin.umich.edu/professional-history
    type: academic
    accessed: 2026-11-18
created: 2026-11-18
---

# Allen Newell

Allen Newell (19 March 1927, San Francisco – 19 July 1992, Pittsburgh) was an American computer scientist and cognitive psychologist and one of the founders of artificial intelligence as a research field.[^s1][^s2] Working mostly with Herbert A. Simon, he helped write some of the first AI programs, invented list processing as a programming technique, and spent the last part of his career pursuing a single architecture meant to account for the whole of human cognition.[^s1] He and Simon shared the 1975 ACM A.M. Turing Award, which Britannica reports was given for basic contributions to AI, the psychology of human cognition and list processing.[^s2]

## Career

After Navy service in the Second World War, Newell took a BS in physics at Stanford in 1949, where he attended courses taught by George Pólya, whose writing on heuristic problem solving shaped his later work.[^s1] He spent about a year in graduate mathematics at Princeton and then joined the RAND Corporation in 1950, applying game theory and operations research to organizations and simulating an Air Force early-warning radar station and its crew.[^s1][^s2] According to the ACM profile, this radar work convinced him that computers could manipulate symbols in general, not merely numbers.[^s1] The project brought him into contact with Simon, and in 1955 Newell moved to Pittsburgh as a graduate student at the Carnegie Institute of Technology, earning a PhD in 1957; Britannica describes it as the institution's first AI-based doctorate.[^s1][^s2] He left RAND for the Carnegie faculty in 1961 as a professor of computer science and psychology, helped found one of the first US computer science departments, and remained at Carnegie Mellon until his death.[^s1][^s2]

## Contributions

- **Logic Theorist (1955–56).** With Simon and Cliff Shaw he built a program, run on RAND's JOHNNIAC, that proved theorems from *Principia Mathematica* by heuristic search; it is often cited as the first successful AI program.[^s1][^s2]
- **IPL and list processing.** To program it the trio created the Information Processing Language, the first list-processing language; the ACM profile credits it with lists, dynamic memory allocation, recursion and functions as arguments, ideas that LISP later built on.[^s1]
- **General Problem Solver (1957).** GPS separated a general method, means-ends analysis, from task knowledge, and was offered as a model of how people solve well-defined problems.[^s1][^s2]
- **Human problem solving (1972).** With Simon he proposed that people think by recursively breaking goals into subgoals until a solution is reached.[^s2]
- **Soar (1980s–1992).** With his students John Laird and Paul Rosenbloom he developed Soar, which he never considered finished.[^s2][^s5]

## Symbols and search

In their Turing Award lecture, Newell and Simon stated two empirical hypotheses that summarise the symbolic programme. The physical symbol system hypothesis holds that a physical symbol system has the necessary and sufficient means for general intelligent action; the heuristic search hypothesis holds that such systems solve problems by generating and progressively modifying symbol structures, and must search selectively because exhaustive search grows exponentially.[^s3] The authors framed both as claims to be tested by building programs, which is why they called computer science an empirical inquiry.[^s3]

## Soar and unified theories of cognition

Soar grew out of Newell's idea of organising rule-based systems around problem spaces; Laird's 1983 thesis work on a universal weak method and universal subgoaling, combined with Rosenbloom's thesis work on chunking, produced the architecture.[^s5] In Soar, goal-directed behaviour is search in a problem space, long-term knowledge is stored as productions, and an impasse in choosing a state or operator spawns a subgoal; when the subgoal is resolved, chunking stores a new production that summarises it, so similar problems are later solved by recognition rather than search.[^s4] Newell treated Soar as a candidate unified theory of cognition — one such theory rather than the final one — and the ACM profile records that he worked on it until his death.[^s1]

## Recognition

Besides the Turing Award, Newell was elected to the US National Academy of Sciences (1972) and National Academy of Engineering (1980), was the first president of the American Association for Artificial Intelligence, and received the IEEE Computer Society Computer Pioneer Award (1981) and the US National Medal of Science (1992).[^s1][^s2] The ACM/AAAI Allen Newell Award is named after him.[^s1]

## Connections

Newell sits under **symbolic AI**, the paradigm his work with Simon largely defined.[^s3] He is linked to the **Logic Theorist** and the **General Problem Solver**, whose articles list him as co-creator, to his long-time collaborator **Herbert A. Simon**, and to **Soar**, the architecture he led in his final decade.[^s1][^s4] The **physical symbol system hypothesis** and **heuristic search** are the theses of his Turing lecture, and the `influencedBy` edge to **George Pólya** records the heuristic-problem-solving teaching he met at Stanford.[^s1][^s3]

## Sources
[^s1]: Association for Computing Machinery, "Allen Newell — A.M. Turing Award Laureate". https://amturing.acm.org/award_winners/newell_3167755.cfm (accessed 2026-11-18)
[^s2]: Encyclopaedia Britannica, "Allen Newell". https://www.britannica.com/biography/Allen-Newell (accessed 2026-11-18)
[^s3]: A. Newell and H. A. Simon, "Computer Science as Empirical Inquiry: Symbols and Search", Communications of the ACM 19(3), 113–126, 1976. https://home.csulb.edu/~cwallis/382/readings/482/Newell&Simonpssh.1976.html (accessed 2026-11-18)
[^s4]: P. S. Rosenbloom, A. Newell and J. E. Laird, "Towards the Knowledge Level in Soar: The Role of the Architecture in the Use of Knowledge", Technical Report AIP-65, 1989. https://apps.dtic.mil/sti/pdfs/ADA218926.pdf (accessed 2026-11-18)
[^s5]: J. E. Laird, "Professional History", University of Michigan. https://laird.engin.umich.edu/professional-history (accessed 2026-11-18)
