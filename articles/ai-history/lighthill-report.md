---
id: kt:lighthill-report
type: Work
title: Lighthill report
aliases: ["Artificial Intelligence: A General Survey", Lighthill survey of artificial intelligence]
domain: ai-history
summary: >-
  A critical review of artificial intelligence research written by the applied mathematician Sir James Lighthill
  for the UK Science Research Council, submitted in 1972 and published in 1973, which sorted AI into three
  categories, blamed the combinatorial explosion for the field's disappointments, and led to cuts in British AI
  and robotics funding.
maturity: historical
broader: [kt:artificial-intelligence]
related: [kt:symbolic-ai, kt:general-problem-solver, kt:dendral, kt:machine-translation, kt:donald-michie]
relations:
  - {predicate: createdBy, object: kt:james-lighthill}
  - {predicate: causes, object: kt:ai-winter}
  - {predicate: contrastsWith, object: kt:dartmouth-workshop}
sources:
  - id: s1
    title: "Artificial Intelligence: A General Survey"
    publisher: Sir James Lighthill, for the UK Science Research Council, 1972/1973 (hosted by AIAI, University of Edinburgh)
    url: https://www.aiai.ed.ac.uk/events/lighthill1973/lighthill.pdf
    type: primary
    accessed: 2026-11-17
  - id: s2
    title: "What is science for? The Lighthill report and the purpose of artificial intelligence research"
    publisher: Jon Agar, University College London (author's accepted manuscript for the British Journal for the History of Science, UCL Discovery)
    url: https://discovery.ucl.ac.uk/10105726/3/Agar_What%20is%20science%20for,%20the%20Lighthill%20report%20and%20the%20purpose%20of%20artificial%20intelligence%20research,%20revised%20for%20BJHS.pdf
    type: academic
    accessed: 2026-11-17
  - id: s3
    title: "Lighthill 17 years on: end of a shotgun divorce"
    publisher: Donald Michie, The Knowledge Engineering Review 5(4), 277–293, 1990
    url: https://www.maxapress.com/data/article/ker/preview/pdf/S0269888900005506.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s4
    title: "BBC TV - June 1973 - Lighthill Controversy Debate at the Royal Institution"
    publisher: Artificial Intelligence Applications Institute (AIAI), University of Edinburgh
    url: https://www.aiai.ed.ac.uk/events/lighthill1973/
    type: academic
    accessed: 2026-11-17
  - id: s5
    title: "Freddy the Robot Was the Fall Guy for British AI"
    publisher: Allison Marsh, IEEE Spectrum, 30 April 2025
    url: https://spectrum.ieee.org/freddy-robot-british-ai-winter
    type: news
    accessed: 2026-11-17
created: 2026-11-17
---

# Lighthill report

The **Lighthill report**, formally *Artificial Intelligence: A General Survey*, is an appraisal of artificial intelligence research that Sir James Lighthill, then Lucasian Professor of Applied Mathematics at Cambridge, wrote at the invitation of the chairman of Britain's Science Research Council (SRC). Lighthill presented it as a personal, independent view formed after roughly two months of study, and took sole responsibility for its opinions.[^s1] The SRC chairman, Brian Flowers, invited him on 20 September 1971; the report was submitted in March 1972 and published in 1973 as part of an SRC volume subtitled *a Paper Symposium*.[^s2] It is remembered as one of the triggers of the first British AI downturn, though historians still argue about what Lighthill was really attacking.[^s2][^s5]

## What the report said

Lighthill organised the field into an "ABC". Category **A**, advanced automation, aimed to replace people with machines for specific industrial, military and scientific jobs such as pattern recognition, speech, translation, theorem proving and chemical structure analysis. Category **C** covered computer-based studies of the central nervous system: models in neurobiology and psychology meant to be tested against experimental data. Category **B**, the "bridge", meant building robots that imitate human abilities in limited worlds, justified mainly by what it fed into A and C.[^s1]

His verdicts were uneven. In A he credited some real successes, including automatic aircraft landing, analysis of microscope images and the DENDRAL program for inferring chemical structures, but judged speech recognition, machine translation, handwriting recognition and general-purpose theorem proving disappointing. He observed that systems worked best when they were loaded with detailed knowledge of their domain.[^s1] He thought computer models had helped psychology discard implausible theories. Category B he found the most disappointing of all: hand–eye coordination and scene analysis had proved far harder than expected, chess programs played at only experienced-amateur level, and general problem solving looked remote.[^s1]

The central technical argument was the **combinatorial explosion**: as the knowledge a program must consider grows, the number of possible combinations grows so quickly that faster computers cannot keep up, undermining both logic-based search and learning approaches.[^s1] Lighthill predicted that over the next twenty-five years A and C would advance where they stayed close to their application areas, while B would become less productive and fragment.[^s1]

## Commentaries and the public debate

The published volume included responses. N. Stuart Sutherland of Sussex defended the bridge category as the heart of AI; Roger Needham of Cambridge largely agreed with Lighthill; Christopher Longuet-Higgins defended cognitive science; and Donald Michie of Edinburgh rejected the categorisation altogether.[^s2] The dispute went public in a BBC *Controversy* programme filmed at the Royal Institution in 1973, in which Lighthill faced Michie, the psychologist Richard Gregory and John McCarthy; the University of Edinburgh's AIAI later restored the 81-minute recording.[^s4] (Sources disagree on the exact broadcast date.[^s4][^s5])

## Consequences

The SRC sided with Lighthill and reorganised its support so that A and C were funded separately, leaving B without a home.[^s2] At Edinburgh, Michie's laboratory, whose FREDDY robots could by 1973 be taught to assemble a simple model car, shrank to a skeleton staff, and IEEE Spectrum describes the result as a British AI winter of about a decade.[^s5] Michie himself argued in 1990 that the report was a private commission rather than formal SRC policy, that it split cognitive science from knowledge engineering, and that the cuts drove trained researchers abroad.[^s3] He also saw its legacy in the 1980s Alvey programme, which funded the work as "intelligent knowledge-based systems" rather than under the AI label.[^s3]

## Interpretation

The usual reading treats the report as a rebuke to AI's overconfident promises. The historian Jon Agar argues instead that it applied Lighthill's lifelong conviction that the best science is tightly coupled to practical problems, so it was less a specific attack on AI than a statement about what research is for; he also finds evidence that the SRC gave Lighthill a preliminary steer.[^s2] Read that way, the report's praise for knowledge-rich, application-driven systems anticipated the expert-system boom that followed.[^s1][^s2]

## Connections

The report was written by `kt:james-lighthill` and is a standard cause cited for the first `kt:ai-winter`.[^s2] Its targets were the general methods of `kt:symbolic-ai` and programs such as the `kt:general-problem-solver`, while it singled out `kt:dendral` as a success and `kt:machine-translation` as a failure.[^s1] `kt:donald-michie` was its most prominent opponent.[^s3] Its sober tone contrasts with the optimism of the `kt:dartmouth-workshop` that launched the field.

## Sources

[^s1]: Sir James Lighthill, "Artificial Intelligence: A General Survey", UK Science Research Council, 1972/1973. https://www.aiai.ed.ac.uk/events/lighthill1973/lighthill.pdf (accessed 2026-11-17)
[^s2]: Jon Agar, "What is science for? The Lighthill report and the purpose of artificial intelligence research", author's accepted manuscript for the British Journal for the History of Science, UCL Discovery. https://discovery.ucl.ac.uk/10105726/3/Agar_What%20is%20science%20for,%20the%20Lighthill%20report%20and%20the%20purpose%20of%20artificial%20intelligence%20research,%20revised%20for%20BJHS.pdf (accessed 2026-11-17)
[^s3]: Donald Michie, "Lighthill 17 years on: end of a shotgun divorce", The Knowledge Engineering Review 5(4), 277–293, 1990. https://www.maxapress.com/data/article/ker/preview/pdf/S0269888900005506.pdf (accessed 2026-11-17)
[^s4]: AIAI, University of Edinburgh, "BBC TV - June 1973 - Lighthill Controversy Debate at the Royal Institution". https://www.aiai.ed.ac.uk/events/lighthill1973/ (accessed 2026-11-17)
[^s5]: Allison Marsh, "Freddy the Robot Was the Fall Guy for British AI", IEEE Spectrum, 30 April 2025. https://spectrum.ieee.org/freddy-robot-british-ai-winter (accessed 2026-11-17)
