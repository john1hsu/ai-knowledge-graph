---
id: kt:google
type: Organization
title: Google
aliases: [Google LLC, Google Inc.]
domain: ai-infrastructure-and-mlops
summary: >-
  An American technology company founded in 1998 and, since 2015, a subsidiary of Alphabet Inc., whose research
  groups and infrastructure produced foundational AI work such as TensorFlow, the Tensor Processing Unit and the
  Transformer, and which now builds the Gemini model family.
maturity: established
broader: [kt:artificial-intelligence]
related: [kt:tpu, kt:nvidia, kt:attention-is-all-you-need, kt:tensorflow]
relations:
  - {predicate: partOf, object: kt:alphabet-inc}
  - {predicate: hasPart, object: kt:google-deepmind}
sources:
  - id: s1
    title: "Google Inc."
    publisher: Encyclopaedia Britannica (Britannica Money)
    url: https://www.britannica.com/money/Google-Inc
    type: encyclopedia
    accessed: 2026-11-14
  - id: s2
    title: "Alphabet Inc. Annual Report on Form 10-K for the fiscal year ended December 31, 2025"
    publisher: Alphabet Inc. (investor relations), filed February 2026
    url: https://s206.q4cdn.com/479360582/files/doc_financials/2025/q4/GOOG-10-K-2025.pdf
    type: primary
    accessed: 2026-11-14
  - id: s3
    title: "Google DeepMind: Bringing together two world-class AI teams"
    publisher: The Keyword (Google blog), Sundar Pichai, April 20, 2023
    url: https://blog.google/technology/ai/april-ai-update/
    type: lab-research
    accessed: 2026-11-14
  - id: s4
    title: "In-Datacenter Performance Analysis of a Tensor Processing Unit"
    publisher: arXiv 1704.04760 (Jouppi et al., Google; ISCA 2017)
    url: https://arxiv.org/abs/1704.04760v1
    type: primary
    accessed: 2026-11-14
  - id: s5
    title: "TensorFlow: A System for Large-Scale Machine Learning"
    publisher: USENIX OSDI 2016 (Abadi et al.)
    url: https://usenix.org/conference/osdi16/technical-sessions/presentation/abadi
    type: peer-reviewed
    accessed: 2026-11-14
created: 2026-11-14
---

# Google

Google is a technology company headquartered in Mountain View, California. Sergey Brin and Larry Page started it in 1998 after meeting as Stanford graduate students, where they had built a search engine called BackRub that ranked pages by the links pointing to them, treating a link from a heavily linked site as a weightier vote.[^s1] It went public in 2004 in an auction-style IPO that raised $1.66 billion, and since 2015 it has been a subsidiary of the holding company Alphabet Inc.; the operating company is now Google LLC.[^s1] For AI practitioners, Google matters as one of the largest producers of machine-learning research, frameworks and custom hardware, and as an operator of AI at very large scale.[^s2][^s3]

## From search infrastructure to AI infrastructure

Google's early advantage came partly from in-house infrastructure for huge data sets, including the Google File System, Bigtable and MapReduce.[^s1] The same habit of building its own stack carried into machine learning. Its Brain team released TensorFlow, described in an OSDI 2016 paper by 22 Google Brain authors as a system that expresses computation and mutable state as dataflow graphs and maps them across clusters of CPUs, GPUs and custom accelerators.[^s5] The authors contrasted it with earlier parameter-server designs, arguing that it gave developers more freedom to try new training algorithms, and reported that it ran in several Google production services and had been open-sourced.[^s5]

The accelerators in question were Tensor Processing Units. A 2017 paper led by Norman Jouppi reported that Google had run this custom ASIC in its data centres since 2015 to speed up neural-network inference. Its core is a 65,536-unit 8-bit multiply-accumulate matrix unit with a peak of 92 TOPS.[^s4] On production MLP, CNN and LSTM workloads, which the authors put at about 95% of the company's inference demand, the TPU ran roughly 15–30 times faster than contemporary Intel Haswell CPUs and NVIDIA K80 GPUs, with 30–80 times better performance per watt.[^s4] Alphabet's 2025 annual report names Ironwood as the seventh TPU generation.[^s2]

## Research output and reorganisation

On April 20, 2023, CEO Sundar Pichai announced that the Brain team from Google Research and DeepMind would combine into a single unit, Google DeepMind, led by DeepMind CEO Demis Hassabis. Jeff Dean became chief scientist for both Google Research and Google DeepMind.[^s3] Pichai's announcement credited the two groups with AlphaGo, Transformers, word2vec, WaveNet, AlphaFold, sequence-to-sequence models, distillation, deep reinforcement learning, and the TensorFlow and JAX frameworks.[^s3] These are Google's own claims about its history, but several of the items, notably the Transformer, are now standard building blocks across the field.

## Scale, products and constraints

Alphabet calls itself an AI-first company, a stance it dates to 2016. In its 10-K for fiscal 2025 (year ended December 31, 2025) it said Gemini 3 was its most capable model and that Gemini models power all 15 of its products with more than half a billion users.[^s2] The same filing reports 2025 revenue of $402.8 billion, up 15% from $350.0 billion, with Google Cloud revenue up 36% to $58.7 billion. Capital expenditure grew from $52.5 billion to $91.4 billion, mostly for servers, network equipment and data centres, and Alphabet expected spending on technical infrastructure to rise significantly again in 2026.[^s2] Alphabet had 190,820 employees at the end of 2025.[^s2]

The filing also lists risks tied to this strategy. They include returns on AI infrastructure that may fail to materialise, limited power, water, land and specialised chip supply, harmful or inaccurate AI outputs, and new AI laws such as the EU AI Act.[^s2] It describes antitrust litigation as well. A U.S. federal court ruled against Google in the Justice Department's search case in August 2024 and imposed remedies in December 2025, including data-sharing and syndication obligations, and both sides appealed in early 2026.[^s2]

## Connections

Google is one of the main actors in **artificial intelligence** as a field and is part of its parent, **Alphabet Inc.**[^s1] Its AI research unit **Google DeepMind** was formed from Brain and DeepMind.[^s3] Google designed the **TPU**, its in-house alternative to the GPUs supplied by **NVIDIA**, which it benchmarked against NVIDIA's K80.[^s4] Its researchers created **TensorFlow**, and Pichai lists the Transformer, the architecture of **Attention Is All You Need**, among the company's contributions.[^s5][^s3]

## Sources
[^s1]: "Google Inc.", Encyclopaedia Britannica. https://www.britannica.com/money/Google-Inc (accessed 2026-11-14)
[^s2]: Alphabet Inc., Form 10-K for the fiscal year ended December 31, 2025. https://s206.q4cdn.com/479360582/files/doc_financials/2025/q4/GOOG-10-K-2025.pdf (accessed 2026-11-14)
[^s3]: Sundar Pichai, "Google DeepMind: Bringing together two world-class AI teams", Google blog, April 20, 2023. https://blog.google/technology/ai/april-ai-update/ (accessed 2026-11-14)
[^s4]: Jouppi et al., "In-Datacenter Performance Analysis of a Tensor Processing Unit", arXiv 1704.04760 (ISCA 2017). https://arxiv.org/abs/1704.04760v1 (accessed 2026-11-14)
[^s5]: Abadi et al., "TensorFlow: A System for Large-Scale Machine Learning", OSDI 2016. https://usenix.org/conference/osdi16/technical-sessions/presentation/abadi (accessed 2026-11-14)
