---
id: kt:google-deepmind
type: Organization
title: Google DeepMind
aliases: [DeepMind, DeepMind Technologies]
domain: ai-infrastructure-and-mlops
summary: >-
  Alphabet's central AI research laboratory, formed in April 2023 by combining the London-based lab DeepMind
  (launched 2010, acquired by Google in 2014) with the Brain team from Google Research; known for deep
  reinforcement learning, AlphaGo, AlphaFold and the Gemini model family.
maturity: established
broader: [kt:artificial-intelligence]
related: [kt:deep-q-network, kt:alphago, kt:alphazero, kt:alphafold, kt:gemini, kt:openai]
relations:
  - {predicate: partOf, object: kt:google}
  - {predicate: partOf, object: kt:alphabet-inc}
sources:
  - id: s1
    title: "Announcing Google DeepMind"
    publisher: Google DeepMind blog, April 20, 2023
    url: https://deepmind.google/en/blog/announcing-google-deepmind/
    type: lab-research
    accessed: 2026-11-17
  - id: s2
    title: "Demis Hassabis"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/biography/Demis-Hassabis
    type: encyclopedia
    accessed: 2026-11-17
  - id: s3
    title: "For Google, a leg up in the artificial intelligence arms race"
    publisher: Fortune, February 5, 2014
    url: https://fortune.com/2014/02/05/for-google-a-leg-up-in-the-artificial-intelligence-arms-race
    type: news
    accessed: 2026-11-17
  - id: s4
    title: "From Pixels to Actions: Human-level control through Deep Reinforcement Learning"
    publisher: Google Research blog (Kumaran and Hassabis), February 25, 2015
    url: https://research.google/blog/from-pixels-to-actions-human-level-control-through-deep-reinforcement-learning/
    type: lab-research
    accessed: 2026-11-17
  - id: s5
    title: "Demis Hassabis & John Jumper awarded Nobel Prize in Chemistry"
    publisher: Google DeepMind blog, October 9, 2024
    url: https://deepmind.google/blog/demis-hassabis-john-jumper-awarded-nobel-prize-in-chemistry/
    type: lab-research
    accessed: 2026-11-17
  - id: s6
    title: "Gemini: A Family of Highly Capable Multimodal Models"
    publisher: arXiv 2312.11805 (Gemini Team, Google)
    url: https://arxiv.org/abs/2312.11805
    type: primary
    accessed: 2026-11-17
created: 2026-11-17
---

# Google DeepMind

Google DeepMind is the AI research laboratory of Alphabet. In its current form it dates from April 20, 2023, when DeepMind and the Brain team from Google Research were combined into one unit led by DeepMind co-founder Demis Hassabis.[^s1] The lab describes its mission as building AI responsibly to benefit humanity, and its announcement credited the two predecessor groups with foundational work such as deep reinforcement learning and the Transformer.[^s1] Its output spans game-playing agents, scientific models such as AlphaFold, and the Gemini family of multimodal language models.[^s2][^s6]

## Origins and acquisition

DeepMind was started in London by Hassabis, the New Zealand computer scientist Shane Legg and the entrepreneur Mustafa Suleyman.[^s2] Sources differ slightly on the date: the company's own 2023 post says it launched in 2010, while Britannica gives 2011.[^s1][^s2] Google bought the startup in January 2014, with Hassabis staying on as chief executive.[^s2][^s3] Fortune reported at the time that the price was said to be between $400 million and $500 million for a firm of about 50 people whose technical details had not been made public; those figures were press reports, not disclosed terms.[^s3]

## Research milestones

The lab's first widely noticed result was the deep Q-network (DQN), published in *Nature* in February 2015 by Mnih and colleagues.[^s4] A single network architecture with fixed hyperparameters learned 49 Atari 2600 games using only raw screen pixels, the available actions and the score as input. According to the accompanying Google post, it beat earlier machine-learning methods on 43 of the 49 games and reached over 75% of a professional human tester's score on more than half of them.[^s4] This established deep reinforcement learning, combining neural-network function approximation with reward-driven learning, as a research programme.

Game playing remained a showcase. In 2016 AlphaGo defeated the Go champion Lee Sedol four games to one, and its successor AlphaGo Zero, which learned from the rules alone without human game records, later beat the original AlphaGo 100 games to none.[^s2] The lab then turned similar ambitions to science. AlphaFold reached roughly 60% accuracy at the CASP13 protein-structure assessment in 2018, and AlphaFold2 reached about 90% at CASP14 in 2020, an accuracy Britannica describes as comparable to experimental methods.[^s2] In October 2024 Hassabis and John Jumper shared half of the Nobel Prize in Chemistry for this protein-structure prediction work, with David Baker receiving the other half for computational protein design.[^s2][^s5] Google DeepMind says AlphaFold predictions, released free through a public database, have been used by more than two million researchers in 190 countries; this is the lab's own figure.[^s5]

## The Gemini era

After the 2023 merger the combined lab became responsible for Google's frontier language models. The Gemini technical report, first posted in December 2023, introduced Ultra, Pro and Nano model sizes trained to handle text, images, audio and video together.[^s6] Google's team claimed that Gemini Ultra advanced the state of the art on 30 of 32 benchmarks it reported and was the first model to reach human-expert performance on MMLU; these are the developer's own claims as of that report, and benchmark comparisons across labs are sensitive to prompting and evaluation choices.[^s6] The leadership announced at the merger placed Koray Kavukcuoglu over a new scientific board and research leadership team, joined by Zoubin Ghahramani from Google Research.[^s1]

## Significance and open questions

Google DeepMind illustrates the shift of frontier AI research into large industrial labs that control their own data, compute and deployment channels. Merging Brain and DeepMind ended a period in which two Alphabet groups had pursued overlapping research separately.[^s1] It also tied a lab originally framed around long-horizon research, from games to protein folding, more closely to product timelines for Gemini.[^s1][^s6] How well that balance between open science and commercial competition holds is a recurring question for observers of the field.

## Connections

Google DeepMind is part of **Google** and, through it, of **Alphabet Inc.**, and it is one of the main organisations advancing **artificial intelligence** as a field.[^s1] It created the **deep Q-network**, **AlphaGo** and its descendant **AlphaZero**, and **AlphaFold**.[^s4][^s2][^s5] It builds the **Gemini** multimodal models.[^s6] The 2023 merger was intended to speed this frontier-model work, putting the lab in the same category of industrial AI developers as **OpenAI**.[^s1][^s6]

## Sources
[^s1]: "Announcing Google DeepMind", Google DeepMind blog, April 20, 2023. https://deepmind.google/en/blog/announcing-google-deepmind/ (accessed 2026-11-17)
[^s2]: "Demis Hassabis", Encyclopaedia Britannica. https://www.britannica.com/biography/Demis-Hassabis (accessed 2026-11-17)
[^s3]: "For Google, a leg up in the artificial intelligence arms race", Fortune, February 5, 2014. https://fortune.com/2014/02/05/for-google-a-leg-up-in-the-artificial-intelligence-arms-race (accessed 2026-11-17)
[^s4]: Kumaran and Hassabis, "From Pixels to Actions: Human-level control through Deep Reinforcement Learning", Google Research blog, February 25, 2015. https://research.google/blog/from-pixels-to-actions-human-level-control-through-deep-reinforcement-learning/ (accessed 2026-11-17)
[^s5]: "Demis Hassabis & John Jumper awarded Nobel Prize in Chemistry", Google DeepMind blog, October 9, 2024. https://deepmind.google/blog/demis-hassabis-john-jumper-awarded-nobel-prize-in-chemistry/ (accessed 2026-11-17)
[^s6]: Gemini Team, "Gemini: A Family of Highly Capable Multimodal Models", arXiv 2312.11805. https://arxiv.org/abs/2312.11805 (accessed 2026-11-17)
