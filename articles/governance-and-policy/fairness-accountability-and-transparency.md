---
id: kt:fairness-accountability-and-transparency
type: Field
title: Fairness, accountability and transparency (FAccT)
aliases: [FAccT, FAT*, FAT/ML, ACM Conference on Fairness, Accountability, and Transparency, fairness accountability and transparency in machine learning]
domain: governance-and-policy
summary: >-
  An interdisciplinary research field, anchored by the ACM FAccT conference (founded as FAT* in 2018 out of the
  FAT/ML workshops), that studies the social effects of algorithmic and AI systems through the values of fairness,
  accountability and transparency, combining computer science with law, social science and philosophy.
maturity: established
broader: [kt:ai-ethics, kt:ai-governance]
related: [kt:algorithmic-bias-and-fairness, kt:model-cards, kt:datasheets-for-datasets, kt:explainable-ai, kt:ai-evaluation]
relations:
  - {predicate: influencedBy, object: kt:science-and-technology-studies}
sources:
  - id: s1
    title: "Press release: 2018 Conference on Fairness, Accountability, and Transparency (FAT*)"
    publisher: FAT* / ACM FAccT Conference, 30 January 2018
    url: https://facctconference.org/2018/press_release.html
    type: primary
    accessed: 2026-11-18
  - id: s2
    title: "FAccT frequently asked questions"
    publisher: ACM FAccT Conference
    url: https://facctconference.org/faq.html
    type: primary
    accessed: 2026-11-18
  - id: s3
    title: "Fairness and Abstraction in Sociotechnical Systems"
    publisher: FAT* 2019 (Selbst, boyd, Friedler, Venkatasubramanian, Vertesi); NSF Public Access Repository
    url: https://par.nsf.gov/servlets/purl/10121131
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s4
    title: "Four Years of FAccT: A Reflexive, Mixed-Methods Analysis of Research Contributions, Shortcomings, and Future Prospects"
    publisher: FAccT 2022 (Laufer, Jain, Cooper, Kleinberg, Heidari); author copy, Cornell University
    url: https://www.cs.cornell.edu/home/kleinber/facct22-4years.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s5
    title: "ACM FAccT 2026 Call for Papers"
    publisher: ACM FAccT Conference
    url: https://facctconference.org/2026/cfp.html
    type: primary
    accessed: 2026-11-18
  - id: s6
    title: "Reflections on the FAccT 2026 Review Process"
    publisher: FAccT conference blog, 22 June 2026
    url: https://facct-blog.github.io/2026-06-22/review-process
    type: primary
    accessed: 2026-11-18
created: 2026-11-18
---

# Fairness, accountability and transparency (FAccT)

**Fairness, accountability and transparency** (FAccT, formerly FAT*) names both a research field and its flagship venue, the ACM Conference on Fairness, Accountability, and Transparency. The field asks how algorithmic and machine-learning systems that make or shape consequential decisions affect people, and how such systems can be built, audited and governed responsibly. It deliberately mixes computer scientists with social scientists, legal scholars, philosophers and policy experts.[^s1][^s5]

## Origins

The community grew out of the Workshop on Fairness, Accountability, and Transparency in Machine Learning (FAT/ML), which had run for more than four years by early 2018, alongside sibling workshops on recommender systems (FAT/REC), ethics in NLP and data and algorithmic transparency.[^s1] The first stand-alone, peer-reviewed conference, FAT*, met at New York University School of Law on 23–24 February 2018, chaired by Solon Barocas, with Sorelle Friedler as programme co-chair. It accepted 17 papers and 6 tutorials and drew more than 450 attendees; Latanya Sweeney and Deborah Hellman gave keynotes, and funders included the MacArthur Foundation, the Ethics and Governance of AI Initiative, Google and Facebook Research.[^s1] After the 2020 edition the conference adopted the name FAccT, following a year-long consultation with its community, a change the organisers describe as made to promote inclusion.[^s2] It is sponsored by ACM, and an Executive Committee oversees the series between years while general and programme chairs run each edition.[^s2][^s5]

## Core ideas

The three values in the name map onto distinct research agendas. *Fairness* work measures and mitigates disparities in how systems treat or perform for different groups; *accountability* covers auditing, documentation and the allocation of responsibility; *transparency* covers explanation and disclosure of how systems work.[^s4] A defining intellectual move of the field is its insistence that these are properties of **sociotechnical** systems, not of a model alone. Selbst and colleagues' FAT* 2019 paper argued that treating fairness as a property of an isolated classifier is an "abstraction error", and named five traps:[^s3]

- **Framing** — modelling only the algorithm and leaving out the people and institutions that act on its output.[^s3]
- **Portability** — assuming a fairness solution built for one social context transfers unchanged to another.[^s3]
- **Formalism** — reducing fairness, which is procedural and contested, to a single mathematical definition.[^s3]
- **Ripple effect** — ignoring how deploying a system changes behaviour, power and values in the setting it enters.[^s3]
- **Solutionism** — assuming a technical fix is appropriate without asking whether technology should be used at all.[^s3]

Drawing on science and technology studies, the authors recommended a process focus over a solutions focus, and accepted that sometimes the right answer is not to build.[^s3]

## Evidence and critiques

A reflexive study presented at FAccT 2022 analysed the 224 papers published at the conference from 2018 to 2021 and surveyed past authors. It found fairness discussed in 69% of papers versus 26% each for transparency and accountability; about 61% of papers were classed as STEM and about 30% as humanities, social sciences and arts.[^s4] Empirical work leaned on a handful of benchmark datasets: among papers using off-the-shelf data, Adult Income, COMPAS and German Credit were the most common, while only about 10% of papers collected original data.[^s4] Respondents criticised the field for insularity from affected communities, a narrow focus on technical fairness in ML, thin engagement with law and enforcement, inconsistent use of terms such as "algorithm", and concern about industry influence; accountability work, the authors noted, centred on self-governance and audits rather than regulation.[^s4]

## The field today

FAccT has grown steadily. For the Montréal edition on 25–28 June 2026, organisers reported a record 985 full-paper submissions (up 21.3% from 812 in 2025) and 325 acceptances, about 33%, after introducing a revise-and-resubmit round.[^s6] The 2026 call framed the venue around responsible, safe, ethical and trustworthy computing and organised submissions into six areas: evaluations, experiences and interactions, law and policy, normative foundations, power and practice, and system development and deployment. It explicitly excluded work that does not engage deeply with the social side of computing.[^s5]

## Connections

FAccT sits under `kt:ai-ethics` and `kt:ai-governance`: it is the main academic venue where ethical principles are turned into measurable criteria, audits and documentation practices.[^s4][^s5] `kt:algorithmic-bias-and-fairness` is its single largest topic, and `kt:explainable-ai` covers much of its transparency strand.[^s4] Documentation instruments such as `kt:model-cards` and `kt:datasheets-for-datasets` belong to the accountability and transparency agenda the field promotes, and its "evaluations and evaluation practices" area links it to `kt:ai-evaluation`.[^s4][^s5] The sociotechnical framing it adopted is borrowed from `kt:science-and-technology-studies`.[^s3]

## Sources
[^s1]: FAT* Conference, "Press release: 2018 Conference on Fairness, Accountability, and Transparency", 30 January 2018. https://facctconference.org/2018/press_release.html (accessed 2026-11-18)
[^s2]: ACM FAccT Conference, "Frequently asked questions". https://facctconference.org/faq.html (accessed 2026-11-18)
[^s3]: Selbst, boyd, Friedler, Venkatasubramanian and Vertesi, "Fairness and Abstraction in Sociotechnical Systems", FAT* 2019. https://par.nsf.gov/servlets/purl/10121131 (accessed 2026-11-18)
[^s4]: Laufer, Jain, Cooper, Kleinberg and Heidari, "Four Years of FAccT: A Reflexive, Mixed-Methods Analysis of Research Contributions, Shortcomings, and Future Prospects", FAccT 2022. https://www.cs.cornell.edu/home/kleinber/facct22-4years.pdf (accessed 2026-11-18)
[^s5]: ACM FAccT Conference, "FAccT 2026 Call for Papers". https://facctconference.org/2026/cfp.html (accessed 2026-11-18)
[^s6]: FAccT conference blog, "Reflections on the FAccT 2026 Review Process", 22 June 2026. https://facct-blog.github.io/2026-06-22/review-process (accessed 2026-11-18)
