---
id: kt:deep-blue
type: Model
title: Deep Blue
aliases: [IBM Deep Blue, Deep Blue II, Deeper Blue, Deep Blue chess computer]
domain: ai-history
summary: >-
  IBM's purpose-built chess system that combined a parallel supercomputer with hundreds of custom chess chips
  running massively parallel alpha-beta search and a hand-tuned evaluation function; in May 1997 it beat world
  champion Garry Kasparov 3.5–2.5, the first match loss by a reigning world champion to a computer under
  standard tournament time controls.
maturity: historical
broader: [kt:symbolic-ai, kt:heuristic-search]
related: [kt:alphazero, kt:alphago, kt:expert-systems, kt:artificial-intelligence]
relations:
  - {predicate: createdBy, object: kt:ibm-research}
  - {predicate: createdBy, object: kt:feng-hsiung-hsu}
  - {predicate: createdBy, object: kt:murray-campbell}
  - {predicate: basedOn, object: kt:alpha-beta-pruning}
  - {predicate: runsOn, object: kt:application-specific-integrated-circuit}
  - {predicate: precededBy, object: kt:deep-thought-chess-computer}
  - {predicate: contrastsWith, object: kt:alphazero}
sources:
  - id: s1
    title: "Deep Blue (authors' manuscript of Artificial Intelligence 134(1–2):57–83, 2002)"
    publisher: M. Campbell, A. J. Hoane Jr. and F.-h. Hsu; copy hosted by Northern Arizona University course readings
    url: https://www.cefns.nau.edu/~edo/Classes/CS470-570_WWW/Readings/Campbell2002.pdf
    type: primary
    accessed: 2026-11-15
  - id: s2
    title: "IBM's Deep Blue Chess Grandmaster Chips"
    publisher: F.-h. Hsu, IEEE Micro 19(2):70–81, March–April 1999 (Computer History Museum archive copy)
    url: https://archive.computerhistory.org/projects/chess/related_materials/text/5-4.IBM's_deep_blue_chess_grandmaster_chips/5-4.IBM's_deep_blue_chess_grandmaster_chips.hsu-fh.1999.IEEE.062303055.sm.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s3
    title: "Deep Blue"
    publisher: IBM History
    url: https://ibm.com/history/deep-blue
    type: lab-research
    accessed: 2026-11-15
  - id: s4
    title: "Deep Blue"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/topic/Deep-Blue
    type: encyclopedia
    accessed: 2026-11-15
  - id: s5
    title: "AIJ Classic Paper Award 2023"
    publisher: Artificial Intelligence journal (Elsevier / IJCAI), 2023
    url: https://aij.ijcai.org/wp-content/uploads/2023/09/AIJ-Classic-Paper-Award-2023.pdf
    type: primary
    accessed: 2026-11-15
  - id: s6
    title: "20 Years after Deep Blue: How AI Has Advanced Since Conquering Chess"
    publisher: Scientific American (interview with Murray Campbell)
    url: https://www.scientificamerican.com/article/20-years-after-deep-blue-how-ai-has-advanced-since-conquering-chess/
    type: news
    accessed: 2026-11-15
created: 2026-11-15
---

# Deep Blue

**Deep Blue** was a chess-playing computer built at IBM Research that, in a six-game match in New York in May 1997, defeated reigning world champion Garry Kasparov by 3.5 points to 2.5.[^s3] It was the first time a sitting world champion lost a match to a computer under standard tournament conditions, and it became one of the most widely cited milestones in the history of artificial intelligence.[^s3][^s4] Its designers later described the system in a paper in the journal *Artificial Intelligence* (2002), which that journal honoured with its Classic Paper Award in 2023.[^s1][^s5]

## History

Deep Blue grew out of a line of student-built chess machines at Carnegie Mellon University: ChipTest (1986–1987) and Deep Thought (1988), which used single-chip move generators; Deep Thought was the first machine to beat a grandmaster in tournament play.[^s1] IBM Research hired Feng-hsiung Hsu and Murray Campbell in 1989, and the team, later including Joe Hoane, Jerry Brody and C. J. Tan, continued the work as Deep Thought 2 and then Deep Blue.[^s3][^s1] In a first six-game match in Philadelphia in 1996, Deep Blue won the opening game, the first win by a computer over a reigning champion at regular time controls, but Kasparov took the match 4–2.[^s3] For the 1997 rematch a substantially upgraded machine (called Deep Blue II in the technical paper) lost game 1, won game 2, drew games 3–5 and won game 6.[^s3][^s1]

## How it worked

The 1997 system was a three-layer parallel machine: an IBM RS/6000 SP supercomputer with 30 nodes, each hosting 16 custom chess chips, for 480 chips in total.[^s1] A master node searched the top of the game tree, worker nodes searched the middle levels in software written in C, and the chips searched the last few plies in hardware, typically four or five in the middlegame.[^s1] Popular accounts summarise the processor count differently (IBM cites 32 processors, Britannica 256), so the authors' paper is the most precise reference.[^s3][^s4][^s1]

Each chip, fabricated in a 0.6-micron CMOS process with about 1.5 million transistors, integrated a move generator, an evaluation function and search control, and could search 2 to 2.5 million positions per second.[^s2] The hardware ran a minimum-window alpha-beta search with quiescence search, which let it dispense with a value stack.[^s2][^s1] Whole-system speed reached roughly 100 to 200 million positions per second depending on the position; the authors report an average of 126 million per second for long searches during the 1997 match.[^s1]

Speed alone was not the design goal. Hsu wrote that packing as much software-adjustable chess knowledge onto the chip as possible came first, with speed second.[^s2] The evaluation function recognised about 8,000 features, governed by more than 8,000 parameters that could be retuned between games.[^s1][^s2] In software, a selective "dual credit with delayed extensions" scheme deepened the search along forcing lines, while the team deliberately avoided null-move pruning.[^s1] Deep Blue also drew on an opening book of about 4,000 positions prepared largely with grandmaster Joel Benjamin, an extended book derived from a 700,000-game grandmaster database, and endgame databases covering all positions with five or fewer pieces.[^s1]

## Significance and critiques

Deep Blue showed that a narrowly specialised combination of brute-force search, custom silicon and expert-encoded knowledge could reach world-champion strength in a domain long treated as a benchmark of intelligence.[^s3][^s1] Critics and its own designers have stressed how little it learned: Campbell has described it as essentially "good old-fashioned AI", with machine learning playing almost no role, and he contrasts it with later systems that learn from large datasets.[^s6] Its knowledge was hand-crafted and chess-specific, so the approach did not transfer to other problems in the way later learning-based systems did.[^s6] IBM, for its part, presents the project as a precursor of its later parallel-computing and AI work, including Blue Gene and Watson; that is the company's own characterisation of its legacy.[^s3] After the match the machine was retired, and part of it went to the Smithsonian.[^s3]

## Connections

Deep Blue is a late, high-profile product of `kt:symbolic-ai` and of `kt:heuristic-search`: its strength came from searching game trees and scoring positions with explicit rules rather than from learned representations.[^s1][^s6] It is **based on** `kt:alpha-beta-pruning`, applied in parallel across software and hardware, and **runs on** custom `kt:application-specific-integrated-circuit` chess chips.[^s2] It was **created by** `kt:ibm-research`, led by `kt:feng-hsiung-hsu` and `kt:murray-campbell`, and was **preceded by** the CMU-built `kt:deep-thought-chess-computer`.[^s1][^s3] Its reliance on encoded grandmaster knowledge links it to `kt:expert-systems`, and it **contrasts with** `kt:alphazero` and `kt:alphago`, which reached superhuman play through self-play learning and neural evaluation instead of hand-tuned features.[^s6] It is a standard milestone in surveys of `kt:artificial-intelligence`.[^s4]

## Sources
[^s1]: M. Campbell, A. J. Hoane Jr., F.-h. Hsu, "Deep Blue", *Artificial Intelligence* 134(1–2):57–83, 2002 (authors' manuscript). https://www.cefns.nau.edu/~edo/Classes/CS470-570_WWW/Readings/Campbell2002.pdf (accessed 2026-11-15)
[^s2]: F.-h. Hsu, "IBM's Deep Blue Chess Grandmaster Chips", *IEEE Micro* 19(2):70–81, 1999. https://archive.computerhistory.org/projects/chess/related_materials/text/5-4.IBM's_deep_blue_chess_grandmaster_chips/5-4.IBM's_deep_blue_chess_grandmaster_chips.hsu-fh.1999.IEEE.062303055.sm.pdf (accessed 2026-11-15)
[^s3]: IBM History, "Deep Blue". https://ibm.com/history/deep-blue (accessed 2026-11-15)
[^s4]: Encyclopaedia Britannica, "Deep Blue". https://www.britannica.com/topic/Deep-Blue (accessed 2026-11-15)
[^s5]: *Artificial Intelligence* journal, "AIJ Classic Paper Award 2023". https://aij.ijcai.org/wp-content/uploads/2023/09/AIJ-Classic-Paper-Award-2023.pdf (accessed 2026-11-15)
[^s6]: Scientific American, "20 Years after Deep Blue: How AI Has Advanced Since Conquering Chess" (interview with Murray Campbell). https://www.scientificamerican.com/article/20-years-after-deep-blue-how-ai-has-advanced-since-conquering-chess/ (accessed 2026-11-15)
