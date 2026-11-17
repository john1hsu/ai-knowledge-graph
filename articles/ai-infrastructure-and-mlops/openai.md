---
id: kt:openai
type: Organization
title: OpenAI
aliases: [OpenAI Inc, OpenAI LP, OpenAI Group PBC, OpenAI Foundation]
domain: ai-infrastructure-and-mlops
summary: >-
  An American AI research and deployment organization founded in December 2015 as a nonprofit, later
  restructured around a capped-profit subsidiary (2019) and then a public benefit corporation controlled
  by the OpenAI Foundation (2025); known for the GPT model series, InstructGPT, DALL-E, Codex and ChatGPT.
maturity: established
broader: [kt:artificial-intelligence]
related: [kt:large-language-model, kt:pretraining, kt:rlhf, kt:language-models-are-few-shot-learners, kt:google-deepmind, kt:anthropic]
relations:
  - {predicate: enables, object: kt:chatgpt}
  - {predicate: influencedBy, object: kt:transformer-architecture}
sources:
  - id: s1
    title: "Introducing OpenAI"
    publisher: OpenAI, December 11, 2015
    url: https://openai.com/index/introducing-openai/
    type: primary
    accessed: 2026-11-17
  - id: s2
    title: "OpenAI"
    publisher: Encyclopaedia Britannica (Britannica Money)
    url: https://britannica.com/topic/OpenAI
    type: encyclopedia
    accessed: 2026-11-17
  - id: s3
    title: "OpenAI LP"
    publisher: OpenAI, March 11, 2019
    url: https://openai.com/index/openai-lp/
    type: primary
    accessed: 2026-11-17
  - id: s4
    title: "Built to benefit everyone"
    publisher: OpenAI, October 28, 2025
    url: https://openai.com/index/built-to-benefit-everyone
    type: primary
    accessed: 2026-11-17
  - id: s5
    title: "Improving Language Understanding by Generative Pre-Training"
    publisher: OpenAI technical report, 2018 (Radford, Narasimhan, Salimans and Sutskever)
    url: https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
    type: primary
    accessed: 2026-11-17
  - id: s6
    title: "Training language models to follow instructions with human feedback"
    publisher: NeurIPS 2022 (Ouyang et al.)
    url: https://neurips.cc/virtual/2022/poster/52886
    type: peer-reviewed
    accessed: 2026-11-17
created: 2026-11-17
---

# OpenAI

OpenAI is a US artificial intelligence organization that both publishes research and ships commercial AI products. It was announced on December 11, 2015 as a nonprofit research company whose goal was to advance digital intelligence in the way most likely to benefit humanity as a whole, free of pressure to produce financial returns.[^s1] Its launch post named Sam Altman and Elon Musk as co-chairs, Greg Brockman as CTO and Ilya Sutskever as research director, and said that a group of backers including Altman, Brockman, Musk and Reid Hoffman had committed $1 billion, of which only a small part was expected to be spent in the first few years.[^s1] The founding team also included researchers such as Andrej Karpathy, Durk Kingma, John Schulman and Wojciech Zaremba.[^s1]

## Corporate structure

OpenAI's legal form has changed twice, each time to raise more capital while keeping the original nonprofit in control. In March 2019 it created OpenAI LP, which it described as a "capped-profit" company: the nonprofit (legally OpenAI Inc) was the general partner, investors and employees were limited partners, and first-round investors' returns were capped at 100 times their investment, with anything above the cap flowing to the nonprofit.[^s3] OpenAI justified the change by saying it needed billions of dollars for cloud compute, supercomputers and talent, and that no existing legal structure balanced fundraising with its mission.[^s3] The same year it entered a strategic partnership with Microsoft that included a $1 billion commitment, with Microsoft's Azure cloud becoming central to later development.[^s2]

On October 28, 2025 OpenAI completed a recapitalization. The nonprofit was renamed the OpenAI Foundation, and the for-profit business became a public benefit corporation, OpenAI Group PBC, which remains under the Foundation's control.[^s4] According to OpenAI, the Foundation's equity in the company was valued at roughly $130 billion at that time, and it announced an initial $25 billion commitment to health research and to technical work on AI resilience; these are the organization's own figures.[^s4]

Governance has been contested. In November 2023 the nonprofit board briefly removed Altman as chief executive and Brockman as board chair; after backlash from employees and Microsoft, Altman returned as CEO, Brockman as president, and a reconstituted board was chaired by Bret Taylor.[^s2]

## Research and products

OpenAI's most influential research line is the generative pre-trained transformer (GPT). The 2018 report by Radford, Narasimhan, Salimans and Sutskever pre-trained a 12-layer decoder-only Transformer on the BooksCorpus collection of more than 7,000 unpublished books, then fine-tuned it on each labeled task, setting new state-of-the-art results on 9 of the 12 datasets studied.[^s5] This "pre-train, then adapt" recipe became the template for later large language models. GPT-3 followed as a beta release in 2020, DALL-E and the code model Codex in 2021, and ChatGPT was released to the public in November 2022.[^s2] Earlier work included OpenAI Gym, a 2016 Python toolkit for reinforcement-learning research, and the open-source Whisper speech-transcription model.[^s2]

A second line made models follow instructions. In the InstructGPT work, published at NeurIPS 2022, OpenAI researchers fine-tuned GPT-3 on human-written demonstrations and then further trained it with reinforcement learning from human feedback on rankings of model outputs.[^s6] In their human evaluations, a 1.3-billion-parameter InstructGPT model was preferred over the 175-billion-parameter GPT-3 despite having roughly 100 times fewer parameters.[^s6] That alignment-oriented training pipeline underpins the conversational assistants OpenAI later deployed.[^s2][^s6]

## Significance and critiques

OpenAI shows how frontier AI shifted from academic labs toward organizations that need very large compute budgets, which in turn pushed it toward commercial structures and big-tech partners.[^s3][^s2] Britannica notes that the move toward for-profit status brings return-on-investment expectations and more regulatory scrutiny, a tension with the founding promise of research free from financial pressure.[^s2][^s1] Whether a nonprofit can meaningfully control a company of this scale remains an open question, highlighted by the 2023 board crisis and the 2025 recapitalization.[^s2][^s4]

## Connections

OpenAI is one of the major organizations advancing **artificial intelligence** and a peer of industrial labs such as **Google DeepMind** and **Anthropic**.[^s2] Its GPT report popularized generative **pretraining** of **Transformer** decoders, the basis of the modern **large language model**; the GPT-3 work is covered in **Language Models are Few-Shot Learners**.[^s5][^s2] Its InstructGPT research is a landmark application of **RLHF**, and that pipeline enabled **ChatGPT**.[^s6][^s2]

## Sources
[^s1]: "Introducing OpenAI", OpenAI, December 11, 2015. https://openai.com/index/introducing-openai/ (accessed 2026-11-17)
[^s2]: "OpenAI", Encyclopaedia Britannica (Britannica Money). https://britannica.com/topic/OpenAI (accessed 2026-11-17)
[^s3]: "OpenAI LP", OpenAI, March 11, 2019. https://openai.com/index/openai-lp/ (accessed 2026-11-17)
[^s4]: "Built to benefit everyone", OpenAI, October 28, 2025. https://openai.com/index/built-to-benefit-everyone (accessed 2026-11-17)
[^s5]: Radford, Narasimhan, Salimans and Sutskever, "Improving Language Understanding by Generative Pre-Training", OpenAI, 2018. https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf (accessed 2026-11-17)
[^s6]: Ouyang et al., "Training language models to follow instructions with human feedback", NeurIPS 2022. https://neurips.cc/virtual/2022/poster/52886 (accessed 2026-11-17)
