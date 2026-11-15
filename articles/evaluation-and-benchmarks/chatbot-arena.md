---
id: kt:chatbot-arena
type: Benchmark
title: Chatbot Arena
aliases: [LMArena, LMSYS Chatbot Arena, Arena (AI evaluation platform), LM Arena]
domain: evaluation-and-benchmarks
summary: >-
  A crowdsourced, live evaluation platform, started at UC Berkeley in 2023 and later run as the company
  LMArena (renamed Arena in 2026), that ranks language models from anonymous pairwise human preference votes
  using a Bradley-Terry model.
maturity: established
broader: [kt:ai-evaluation, kt:human-evaluation]
related: [kt:llm-as-a-judge, kt:mt-bench, kt:benchmark-contamination, kt:goodharts-law, kt:rlhf]
relations:
  - {predicate: introducedIn, object: kt:chatbot-arena-an-open-platform-for-evaluating-llms-by-human-preference}
  - {predicate: basedOn, object: kt:bradley-terry-model}
  - {predicate: createdBy, object: kt:lmsys}
  - {predicate: studiedIn, object: kt:the-leaderboard-illusion}
  - {predicate: contrastsWith, object: kt:mmlu}
sources:
  - id: s1
    title: "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference"
    publisher: Proceedings of ICML 2024, PMLR 235:8359-8388 (Chiang, Zheng, Sheng, Angelopoulos et al.)
    url: https://proceedings.mlr.press/v235/chiang24b.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s2
    title: "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference (arXiv 2403.04132v1, full text)"
    publisher: arXiv (Chiang et al., 2024)
    url: https://arxiv.org/html/2403.04132v1
    type: primary
    accessed: 2026-11-15
  - id: s3
    title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
    publisher: NeurIPS 2023 Datasets and Benchmarks Track (Zheng, Chiang, Sheng et al.)
    url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "The Leaderboard Illusion"
    publisher: arXiv 2504.20879 (Singh, Nan, Wang et al., 2025)
    url: https://arxiv.org/abs/2504.20879
    type: preprint
    accessed: 2026-11-15
  - id: s5
    title: "LMArena is now Arena"
    publisher: Arena (company blog), January 2026
    url: https://arena.ai/blog/lmarena-is-now-arena/
    type: primary
    accessed: 2026-11-15
  - id: s6
    title: "Chatbot Arena Group Goes From Academic Project to $600 Million Startup"
    publisher: Bloomberg Law, 21 May 2025
    url: https://news.bloomberglaw.com/private-equity/lmarena-goes-from-academic-project-to-600-million-startup
    type: news
    accessed: 2026-11-15
created: 2026-11-15
---

# Chatbot Arena

**Chatbot Arena** is an open, crowdsourced platform that ranks large language models by human preference. A visitor types any prompt, receives answers from two anonymous models side by side, and votes for the better one; the accumulated votes are turned into a leaderboard.[^s1] Its authors, a UC Berkeley team led by Wei-Lin Chiang, Lianmin Zheng, Joseph E. Gonzalez and Ion Stoica, began collecting votes in April 2023 and described the method in a paper at ICML 2024.[^s1][^s2] The project became a venture-backed company, LMArena, in 2025, and the company renamed itself **Arena** on 28 January 2026, saying the platform had outgrown its language-model-only focus.[^s5][^s6]

## How it works

Each "battle" samples two models and hides their identities until after the user votes. Users can choose either model, declare a tie, or mark both answers as bad, and can keep chatting before deciding.[^s2] Because prompts come from real users rather than a fixed test set, the evaluation is open-ended and harder to memorise than a static benchmark.[^s1]

Rankings are fitted with the **Bradley-Terry model**, in which the probability that model *i* beats model *j* is a logistic function of the difference in their latent scores, roughly P(i beats j) = 1 / (1 + e^-(β_i − β_j)). The authors moved from an online Elo rating to Bradley-Terry coefficients because the latter support cleaner statistical estimation, and they report confidence intervals using robust "sandwich" standard errors, which were tighter than bootstrap intervals in large samples.[^s2] An active-sampling rule chooses which model pairs to show next, favouring pairs whose intervals would shrink most; the paper reports this reached a target precision with about 4,400 votes instead of 6,800 under random sampling.[^s2] A p-value-based detector flags anomalous users who submit repetitive or meaningless input.[^s2]

## Evidence of validity

As of January 2024 the platform had gathered roughly 240,000 votes from about 90,000 users across more than 50 models and over 100 languages, with English making up around 77% of the data.[^s2] Topic modelling found about 600 prompt clusters with a long tail, the largest holding only about 1% of prompts, which the authors cite as evidence of diversity. Agreement between crowd votes and expert labels was 72.8–83.1%, compared with 79.4–89.8% between experts.[^s2] An earlier NeurIPS 2023 paper by the same group used Arena data to validate GPT-4 as a judge, reporting over 80% agreement with human preferences, and released 30,000 Arena conversations with preference labels.[^s3]

## Limitations and critiques

The authors acknowledge that the user base likely skews toward hobbyists and researchers, that chat-interface prompts may not reflect production workloads, and that the leaderboard measures helpfulness rather than safety.[^s2] A 2025 preprint, *The Leaderboard Illusion* by Singh, Hooker and co-authors, argued that undisclosed private testing let some providers try many variants and publish only the best; it reported that Meta tested 27 private Llama 4 variants before release.[^s4] The same study estimated that Google and OpenAI received about 19.2% and 20.4% of Arena data, against about 29.7% for 83 open-weight models combined, and found that training on Arena-style data could raise Arena win rates by up to 112% in relative terms. Its authors read this as a risk of overfitting to the leaderboard rather than improving general quality.[^s4] These are the study authors' claims, but they illustrate how any widely watched ranking invites optimisation pressure.

## In practice

Chatbot Arena became one of the most cited LLM leaderboards, and labs routinely quote its rankings when launching models.[^s1] In May 2025 the team announced a $100 million seed round led by Andreessen Horowitz and UC Investments, reportedly at a $600 million valuation.[^s6] In January 2026 Arena said it served more than 5 million monthly users in 150 countries and 60 million conversations a month, and that it now evaluates writing, coding, reasoning, design, search and other tasks.[^s5]

## Connections

- **Broader:** it is a form of **AI evaluation** built on **human evaluation**, replacing small expert panels with large-scale crowd votes.[^s1]
- **Bradley-Terry model:** the statistical model behind the scores, the same pairwise-preference form used for reward models in **RLHF**.[^s2]
- **LLM-as-a-judge and MT-Bench:** Arena votes were the human reference against which **LLM-as-a-judge** and **MT-Bench** were validated.[^s3]
- **Contrasts with static benchmarks:** unlike fixed question sets such as **MMLU**, live user prompts resist **benchmark contamination**, though selective testing creates its own **Goodhart's law** pressure.[^s1][^s4]

## Sources

[^s1]: Chiang et al., "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference", ICML 2024, PMLR 235. https://proceedings.mlr.press/v235/chiang24b.html (accessed 2026-11-15)
[^s2]: Chiang et al., arXiv 2403.04132v1 full text. https://arxiv.org/html/2403.04132v1 (accessed 2026-11-15)
[^s3]: Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", NeurIPS 2023 Datasets and Benchmarks. https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract.html (accessed 2026-11-15)
[^s4]: Singh et al., "The Leaderboard Illusion", arXiv 2504.20879, 2025. https://arxiv.org/abs/2504.20879 (accessed 2026-11-15)
[^s5]: Arena, "LMArena is now Arena", January 2026. https://arena.ai/blog/lmarena-is-now-arena/ (accessed 2026-11-15)
[^s6]: Bloomberg Law, "Chatbot Arena Group Goes From Academic Project to $600 Million Startup", 21 May 2025. https://news.bloomberglaw.com/private-equity/lmarena-goes-from-academic-project-to-600-million-startup (accessed 2026-11-15)
