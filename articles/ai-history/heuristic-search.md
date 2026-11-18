---
id: kt:heuristic-search
type: Technique
title: Heuristic search
aliases: [informed search, heuristic state-space search, best-first heuristic search]
domain: ai-history
summary: >-
  A family of problem-solving methods that explore a space of candidate states or partial solutions while using
  problem-specific knowledge, typically a heuristic function estimating the remaining cost to a goal, to decide
  what to expand next; A* and IDA* are its best-known algorithms, and Newell and Simon held it to be central to intelligence.
maturity: foundational
broader: [kt:symbolic-ai, kt:state-space-search]
related: [kt:automated-planning, kt:monte-carlo-tree-search, kt:beam-search, kt:tree-of-thoughts]
relations:
  - {predicate: hasPart, object: kt:a-star-search}
  - {predicate: hasPart, object: kt:iterative-deepening-a-star}
  - {predicate: influencedBy, object: kt:physical-symbol-system-hypothesis}
  - {predicate: usedIn, object: kt:general-problem-solver}
  - {predicate: usedIn, object: kt:deep-blue}
  - {predicate: studiedIn, object: kt:a-formal-basis-for-the-heuristic-determination-of-minimum-cost-paths}
sources:
  - id: s1
    title: "A Formal Basis for the Heuristic Determination of Minimum Cost Paths"
    publisher: P. E. Hart, N. J. Nilsson and B. Raphael, IEEE Transactions on Systems Science and Cybernetics SSC-4(2), 1968 (copy hosted for a St. Francis Xavier University course)
    url: https://people.stfx.ca/jdelamer/courses/csci-564/_downloads/b2220c66675ddde471ca1795147b8e86/A_Formal_Basis_for_the_Heuristic_Determination_of_Minimum_Cost_Paths.pdf
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "Computer Science as Empirical Inquiry: Symbols and Search"
    publisher: A. Newell and H. A. Simon, Communications of the ACM 19(3), 1976 (1975 Turing Award lecture; copy hosted by Politecnico di Milano)
    url: https://schiaffonati.faculty.polimi.it/TFI/newell_simon_1976.pdf
    type: primary
    accessed: 2026-11-18
  - id: s3
    title: "Iterative-Deepening-A*: An Optimal Admissible Tree Search"
    publisher: R. E. Korf, Proceedings of IJCAI 1985, pp. 1034–1035
    url: https://ijcai.org/proceedings/1985/208
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "CSC384 Lecture 3: Heuristic Search (part 2)"
    publisher: University of Toronto, Department of Computer Science, CSC384 Introduction to Artificial Intelligence, Winter 2020
    url: https://www.teach.cs.toronto.edu/~csc384h/winter/Lectures/csc384w20-Lecture03-Heuristic-Search-part2-1pp.pdf
    type: academic
    accessed: 2026-11-18
created: 2026-11-18
---

# Heuristic search

**Heuristic search** (also *informed search*) is the strategy of solving a problem by exploring a space of candidate states or partial solutions while using knowledge about the problem to choose which candidates to examine first, instead of enumerating possibilities blindly. In their 1975 Turing Award lecture, Allen Newell and Herbert A. Simon framed problem solving as generating and progressively modifying symbol structures until one passes a test for being a solution, and argued that any system with limited resources must make that search heuristic.[^s2] In modern AI the term usually refers to graph-search algorithms, above all A*, that rank candidate nodes using a heuristic function estimating the remaining cost to a goal.[^s1][^s4]

## Origin

The idea predates a formal algorithm. Newell and Simon's early programs, starting with the Logic Theorist and the General Problem Solver, used rules of thumb such as means-ends analysis and best-first ordering to avoid exhaustive search.[^s2] Their 1976 lecture stated this as the **heuristic search hypothesis**, alongside the physical symbol system hypothesis, and made a sharp claim about where intelligence lies: not in how much a system searches, but in how well it extracts and uses information about the structure of the problem space so that it can avoid searching.[^s2] They illustrated the stakes with branching: a tree in which each node has B successors grows as B to the power of depth, so chess programs might examine a million branches while strong human players look at roughly a hundred by being selective.[^s2]

The formal turn came in 1968, when Peter Hart, Nils Nilsson and Bertram Raphael of the Stanford Research Institute published A*.[^s1] They contrasted a "mathematical" tradition, which proves that algorithms find minimum-cost paths but pays little attention to computational cost, with a "heuristic" tradition that uses domain knowledge for speed but usually cannot guarantee optimal answers. Their contribution was to place domain knowledge inside a formal framework, keeping the optimality guarantee while exploiting the heuristic.[^s1]

## How it works

A* keeps a frontier of open nodes and always expands the one with the smallest value of

f(n) = g(n) + h(n),

where g(n) is the cost of the cheapest path found so far from the start to n and h(n) is an estimate of the cost from n to the nearest goal.[^s1] Setting h to zero reduces A* to uniform-cost search; a greedy best-first search would instead rank nodes on h alone, and weighted A* multiplies h by a factor to bias the search toward the goal.[^s4]

Two properties of h govern behaviour:

- **Admissibility.** If h never overestimates the true remaining cost, A* is guaranteed to return an optimal path.[^s1][^s4]
- **Consistency (monotonicity).** If, for every step, h(m) is at most the step cost from m to n plus h(n), then f never decreases along a path, and the first time A* expands a node it already has the cheapest path to it.[^s1][^s4]

Hart, Nilsson and Raphael also proved that, among admissible algorithms using no more problem knowledge than A*, A* expands the fewest nodes, apart from ties at the optimal cost.[^s1] Good heuristics are often obtained by **relaxation**: solve a simplified version of the problem and use its cost as h. In the 8-puzzle, dropping movement constraints yields the misplaced-tiles and Manhattan-distance heuristics, both admissible.[^s4]

## Limitations and refinements

A sharper heuristic expands fewer nodes, but worst-case time remains exponential unless h is very accurate, and A* must store its whole frontier, so memory often runs out before time does.[^s4] Richard Korf's **Iterative-Deepening-A*** (IDA*, 1985) addresses the memory problem by running repeated depth-first searches with an increasing cutoff on f, needing only linear space while expanding asymptotically as many nodes as A* on exponential trees and remaining admissible.[^s3] Korf reported it was the only algorithm then known to find optimal solutions to random instances of the Fifteen Puzzle within practical limits.[^s3] IDA* performs poorly in state spaces with many cycles, because it does not remember states it has already visited.[^s4] The admissibility guarantee is itself a trade-off: Hart and colleagues noted that the choice of h lets practitioners give up some optimality in exchange for speed.[^s1]

## Connections

Heuristic search is a core method of **symbolic AI** and a refinement of **state-space search**; Newell and Simon presented it as the companion of the **physical symbol system hypothesis**.[^s2] Its canonical algorithms, **A\*** and **IDA\***, are parts of the family, with A* introduced in the Hart–Nilsson–Raphael paper.[^s1][^s3] It was used in the **General Problem Solver**, whose means-ends analysis Newell and Simon list among their search-limiting techniques, and its argument that chess play depends on selective rather than exhaustive branching frames game-tree programs such as **Deep Blue**, which this graph places under heuristic search.[^s2] Classical **automated planning** searches state spaces with heuristics derived from relaxed problems, the technique illustrated in the 8-puzzle example.[^s4] **Monte Carlo tree search** and **beam search** are later selective-search methods, and **tree of thoughts** runs explicit search over language-model reasoning steps, echoing the generate-and-test framing of the 1976 lecture.[^s2]

## Sources

[^s1]: P. E. Hart, N. J. Nilsson and B. Raphael, "A Formal Basis for the Heuristic Determination of Minimum Cost Paths", IEEE Transactions on Systems Science and Cybernetics, SSC-4(2):100–107, 1968. https://people.stfx.ca/jdelamer/courses/csci-564/_downloads/b2220c66675ddde471ca1795147b8e86/A_Formal_Basis_for_the_Heuristic_Determination_of_Minimum_Cost_Paths.pdf (accessed 2026-11-18)
[^s2]: A. Newell and H. A. Simon, "Computer Science as Empirical Inquiry: Symbols and Search", Communications of the ACM 19(3), 1976. https://schiaffonati.faculty.polimi.it/TFI/newell_simon_1976.pdf (accessed 2026-11-18)
[^s3]: R. E. Korf, "Iterative-Deepening-A*: An Optimal Admissible Tree Search", Proceedings of IJCAI 1985, pp. 1034–1035. https://ijcai.org/proceedings/1985/208 (accessed 2026-11-18)
[^s4]: University of Toronto, CSC384 Introduction to Artificial Intelligence, "Lecture 3: Heuristic Search (part 2)", Winter 2020. https://www.teach.cs.toronto.edu/~csc384h/winter/Lectures/csc384w20-Lecture03-Heuristic-Search-part2-1pp.pdf (accessed 2026-11-18)
