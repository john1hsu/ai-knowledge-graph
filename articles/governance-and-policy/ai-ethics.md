---
id: kt:ai-ethics
type: Field
title: AI ethics
aliases: [ethics of artificial intelligence, ethics of AI, artificial intelligence ethics, AI ethics principles]
domain: governance-and-policy
summary: >-
  The branch of applied ethics that studies the moral questions raised by designing, deploying and living with
  artificial intelligence, from privacy, bias and opacity in today's systems to machine moral agency, and that
  produced the wave of AI ethics principles (transparency, fairness, non-maleficence, responsibility, privacy)
  issued by companies, governments and intergovernmental bodies since the mid-2010s.
maturity: established
broader: [kt:ai-governance, kt:applied-ethics]
related: [kt:algorithmic-bias-and-fairness, kt:fairness-accountability-and-transparency, kt:oecd-ai-principles, kt:ai-safety, kt:explainable-ai, kt:unesco-recommendation-on-the-ethics-of-ai]
relations:
  - {predicate: hasPart, object: kt:machine-ethics}
  - {predicate: influencedBy, object: kt:bioethics}
  - {predicate: contrastsWith, object: kt:ai-alignment}
sources:
  - id: s1
    title: "Ethics of Artificial Intelligence and Robotics"
    publisher: Stanford Encyclopedia of Philosophy (Vincent C. Müller; first published 30 April 2020, revised 27 March 2026)
    url: https://plato.stanford.edu/entries/ethics-ai/
    type: academic
    accessed: 2026-11-19
  - id: s2
    title: "Artificial Intelligence: the global landscape of ethics guidelines"
    publisher: Jobin, Ienca & Vayena, arXiv 1906.11668 (published in Nature Machine Intelligence, 2019, doi:10.1038/s42256-019-0088-2)
    url: https://arxiv.org/pdf/1906.11668
    type: primary
    accessed: 2026-11-19
  - id: s3
    title: "Principles alone cannot guarantee ethical AI"
    publisher: Brent Mittelstadt, arXiv 1906.06668 (published in Nature Machine Intelligence, 2019)
    url: https://arxiv.org/pdf/1906.06668
    type: primary
    accessed: 2026-11-19
  - id: s4
    title: "A Unified Framework of Five Principles for AI in Society"
    publisher: Floridi & Cowls, Harvard Data Science Review 1(1), 2019 (authors' archived copy, PhilArchive)
    url: https://philarchive.org/archive/FLOAUF
    type: primary
    accessed: 2026-11-19
  - id: s5
    title: "193 countries adopt first-ever global agreement on the Ethics of Artificial Intelligence"
    publisher: UN News, 25 November 2021
    url: https://news.un.org/en/story/2021/11/1106612
    type: intergovernmental
    accessed: 2026-11-19
created: 2026-11-19
---

# AI ethics

**AI ethics** (the ethics of artificial intelligence) is the part of applied ethics concerned with what people should and should not do with AI systems, what those systems themselves should do, what risks they pose and how they can be controlled.[^s1] Müller's Stanford Encyclopedia of Philosophy entry calls it a very young discipline: the first robot-ethics and machine-ethics publications date from the early 2000s, and the first AI ethics conference was held in 2012.[^s1] Like other technology-driven applied ethics, it draws heavily on fields outside philosophy, including law, political science, economics and media studies.[^s1]

## Scope: AI as tool and AI as subject

The philosophical literature organises the field around a basic split.[^s1] The larger part treats AI as an **object**, a tool that humans build and use, and asks about the harms that use can cause: privacy and surveillance, manipulation of behaviour, the opacity of automated decisions, bias in decision systems, human–robot interaction, automation and employment, and the effects of autonomous systems such as vehicles and weapons.[^s1] The smaller part treats AI as a possible **subject**: *machine ethics* asks how systems could be built to behave ethically, and the debate on *artificial moral agency* asks whether such systems could ever carry moral responsibility or rights.[^s1] Speculation about superintelligence and a technological "singularity" is usually discussed separately, as a long-term risk.[^s1] Müller notes that early writing sometimes equated machine ethics with all of AI ethics, a conflation he says has now been overcome.[^s1]

## The principles wave

Between roughly 2015 and 2020, companies, research institutes, governments and intergovernmental bodies published a large number of AI ethics principles and guidelines.[^s1] Jobin, Ienca and Vayena mapped this landscape in 2019 and assembled a corpus of 84 documents.[^s2] Private companies issued the largest share (19 documents, 22.6%), closely followed by government agencies (18, 21.4%).[^s2] The corpus was geographically skewed: the United States (20) and the United Kingdom (14) together produced more than a third, while Africa and South and Central America appeared only through international bodies.[^s2]

Across that corpus the authors found convergence on five principles: transparency, justice and fairness, non-maleficence, responsibility, and privacy.[^s2] Other values were rare; solidarity appeared in only 6 of the 84 documents, dignity in 13 and sustainability in 14.[^s2] Even where the labels agreed, the documents differed substantially on how each principle should be interpreted, why it matters, whom it applies to and how it should be implemented.[^s2]

Floridi and Cowls, comparing six high-profile sets that together listed 47 principles, argued that most of the overlap can be mapped onto the four classic principles of bioethics (beneficence, non-maleficence, autonomy and justice).[^s4] They added a fifth, **explicability**, which joins intelligibility (how does the system work?) with accountability (who is responsible for how it works?).[^s4] They also acknowledged that their framework draws mainly on Western initiatives.[^s4]

## Critiques: from principles to practice

The most influential critique is that principles alone do little. Mittelstadt, counting at least 84 public–private initiatives, argued that the borrowed medical-ethics model works in medicine because of features AI development lacks.[^s3] Medicine has a shared goal (the patient's health) and fiduciary duties; a long professional history with codified norms; tested ways to turn principles into decisions, such as review boards and precedent; and legal and professional accountability through licensing and malpractice law.[^s3] Without these, he argued, high-level agreement can mask deep normative and political disagreement.[^s3] His recommendations included binding accountability and independent auditing, licensing for developers of high-risk systems, attention to organisations and business models rather than individual conduct, and treating ethics as an ongoing process rather than a design problem to be solved once.[^s3]

The SEP entry records a similar shift: debate has moved from drafting principles toward actual policy and regulation, with assessments of the principles ranging from toothless to useful work in progress.[^s1]

## Institutionalisation

The clearest move from voluntary principles to an intergovernmental instrument is UNESCO's *Recommendation on the Ethics of Artificial Intelligence*, adopted by all 193 UNESCO member states in November 2021 and described as the first global agreement on AI ethics.[^s5] It addresses transparency, accountability and privacy, includes policy chapters on data governance, education, culture, labour, health and the economy, and rules out using AI for social scoring or mass surveillance.[^s5] Member states are asked to report regularly on how they implement it.[^s5]

## Connections

AI ethics sits under `kt:ai-governance`, which turns ethical commitments into institutions, laws and standards, and under `kt:applied-ethics` as its parent discipline.[^s1] Its fairness and justice strand is developed in `kt:algorithmic-bias-and-fairness` and in the research venue `kt:fairness-accountability-and-transparency`, while the explicability principle links to `kt:explainable-ai`.[^s2][^s4] The `kt:oecd-ai-principles` and the `kt:unesco-recommendation-on-the-ethics-of-ai` are intergovernmental codifications of the same principles wave.[^s5] `kt:machine-ethics` is its sub-field on AI as a moral subject, and the field's principle sets were explicitly modelled on `kt:bioethics`.[^s1][^s4] It overlaps with but contrasts with `kt:ai-safety` and `kt:ai-alignment`, which focus on making systems reliably pursue intended goals; AI ethics also asks whose goals and values those should be.[^s1]

## Sources

[^s1]: Vincent C. Müller, "Ethics of Artificial Intelligence and Robotics", Stanford Encyclopedia of Philosophy (rev. 27 March 2026). https://plato.stanford.edu/entries/ethics-ai/ (accessed 2026-11-19)
[^s2]: Anna Jobin, Marcello Ienca & Effy Vayena, "Artificial Intelligence: the global landscape of ethics guidelines", arXiv 1906.11668 / Nature Machine Intelligence (2019). https://arxiv.org/pdf/1906.11668 (accessed 2026-11-19)
[^s3]: Brent Mittelstadt, "Principles alone cannot guarantee ethical AI", arXiv 1906.06668 / Nature Machine Intelligence (2019). https://arxiv.org/pdf/1906.06668 (accessed 2026-11-19)
[^s4]: Luciano Floridi & Josh Cowls, "A Unified Framework of Five Principles for AI in Society", Harvard Data Science Review 1(1), 2019. https://philarchive.org/archive/FLOAUF (accessed 2026-11-19)
[^s5]: UN News, "193 countries adopt first-ever global agreement on the Ethics of Artificial Intelligence", 25 November 2021. https://news.un.org/en/story/2021/11/1106612 (accessed 2026-11-19)
