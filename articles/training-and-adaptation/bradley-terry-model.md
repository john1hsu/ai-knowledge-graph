---
id: kt:bradley-terry-model
type: Concept
title: Bradley-Terry model
aliases: [Bradley–Terry model, BT model, Bradley-Terry-Luce model, BTL model]
domain: training-and-adaptation
summary: >-
  A statistical model of paired comparisons in which the probability that one item beats another is a logistic
  function of the difference between their latent strength scores; it underlies reward-model training in RLHF, the
  DPO loss and preference-vote leaderboards such as Chatbot Arena.
maturity: foundational
broader: [kt:logistic-regression, kt:paired-comparison]
related: [kt:rlhf, kt:human-evaluation, kt:plackett-luce-model, kt:thurstone-mosteller-model]
relations:
  - {predicate: usedIn, object: kt:reward-model}
  - {predicate: usedIn, object: kt:chatbot-arena}
  - {predicate: usedIn, object: kt:direct-preference-optimization}
  - {predicate: contrastsWith, object: kt:elo-rating-system}
sources:
  - id: s1
    title: "MM algorithms for generalized Bradley-Terry models"
    publisher: Annals of Statistics 32(1):384–406, 2004 (David R. Hunter); Penn State research portal record
    url: https://pure.psu.edu/en/publications/mm-algorithms-for-generalized-bradley-terry-models/
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s2
    title: "The many routes to the ubiquitous Bradley-Terry model"
    publisher: arXiv 2312.13619 (Hamilton, Tawn and Firth, University of Warwick)
    url: https://arxiv.org/pdf/2312.13619
    type: preprint
    accessed: 2026-11-16
  - id: s3
    title: "Lecture 3: Sports rating models"
    publisher: University of California, Berkeley, Department of Statistics (David Aldous, 2017)
    url: https://www.stat.berkeley.edu/~aldous/157/Lectures/lecture_3.pdf
    type: academic
    accessed: 2026-11-16
  - id: s4
    title: "Direct Preference Optimization: Your Language Model is Secretly a Reward Model (arXiv full text)"
    publisher: arXiv 2305.18290v2 (Rafailov, Sharma, Mitchell, Manning, Ermon and Finn); NeurIPS 2023
    url: https://arxiv.org/html/2305.18290v2
    type: primary
    accessed: 2026-11-16
  - id: s5
    title: "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference (arXiv full text)"
    publisher: arXiv 2403.04132v1 (Chiang, Zheng, Sheng, Angelopoulos et al., 2024)
    url: https://arxiv.org/html/2403.04132v1
    type: primary
    accessed: 2026-11-16
created: 2026-11-16
---

# Bradley-Terry model

The Bradley-Terry (BT) model is a probability model for paired comparisons. Each item *i* gets a positive strength π_i, and the chance that *i* is preferred to (or beats) *j* is π_i / (π_i + π_j).[^s2] Writing π_i = exp(θ_i) turns this into a logistic function of the score difference, P(i ≻ j) = σ(θ_i − θ_j), so the model is a logistic regression on the difference between two latent scores.[^s3] In modern AI it is the default way to turn human "A is better than B" judgments into numbers: it defines the loss used to train reward models for RLHF, it is baked into the Direct Preference Optimization objective, and it ranks models on preference-vote leaderboards.[^s4][^s5]

## Origin

The model carries the names of Bradley and Terry's 1952 paired-comparison work, but the same form was studied earlier by Zermelo (1928) for rating chess players; Ford (1957) and Luce's choice axiom (1959) gave it further foundations.[^s2] A review by Hamilton, Tawn and Firth catalogues many independent routes to the same model: axioms such as Luce's choice axiom and transitivity of odds; maximum entropy subject to matching observed win counts; latent "noisy strength" models with Gumbel-type noise (Gaussian noise gives the Thurstone-Mosteller model instead); and special cases of the Rasch and Cox proportional-hazards models.[^s2] They also note that BT is an exponential family in which each item's win total is the sufficient statistic, which helps explain why it keeps reappearing.[^s2]

## How it works

Given counts of wins between pairs of items, the strengths are fitted by maximum likelihood.[^s3] Hunter (2004) showed how to build simple iterative fitting algorithms for BT and its generalisations (ties, home-field advantage, multi-item rankings) using the minorization-maximization (MM) framework, and gave conditions under which they converge to the unique maximum-likelihood estimate.[^s1] Two practical caveats follow from the maths. Strengths are identified only up to a constant (adding the same amount to every θ changes nothing), so one score is usually pinned or the scores are centred; and finite estimates need the comparison data to be connected enough that no group of items wins or loses every comparison against the rest.[^s2]

## BT versus Elo

Elo-style ratings update two players' scores after each game in proportion to how surprising the result was, rather than refitting a probability model.[^s3] Aldous's Berkeley lecture notes that the logistic BT form is computationally convenient but assumes fixed strengths and strictly transitive probabilities, while Elo implicitly tracks changing strength by weighting recent games more; on the chess scale one logistic unit corresponds to about 174 rating points.[^s3]

## In AI practice

In RLHF, a reward model r(x, y) is trained so that the human-preferred response y_w outscores the rejected one y_l, minimising −log σ(r(x, y_w) − r(x, y_l)), which is exactly the BT negative log-likelihood.[^s4] The DPO paper (NeurIPS 2023) starts from the same BT preference model and substitutes an implicit reward β·log(π(y|x)/π_ref(y|x)); because BT depends only on reward differences, the intractable normalising term cancels and the policy can be trained with a classification-style loss and no separate reward model.[^s4] The authors note that the Plackett-Luce model extends the derivation from pairs to full rankings.[^s4]

Chatbot Arena's 2024 paper reports that the platform moved from online Elo scores to BT coefficients because they suit statistical estimation better; it reweights votes so the scores target a uniform mix of model pairs and reports sandwich (robust) confidence intervals.[^s5] The paper describes roughly 240,000 votes from more than 90,000 users as of January 2024.[^s5] Limitations carry over directly: BT assumes a single scalar quality per item, so it cannot represent intransitive or context-dependent preferences, and its scores are relative to the pool of items compared.[^s3][^s2]

## Connections

BT is a special case of **logistic regression** applied to **paired comparison** data.[^s3] It is **used in** the **reward model** stage of **RLHF**, in **Direct Preference Optimization**, and in **Chatbot Arena**'s leaderboard, which is a form of **human evaluation**.[^s4][^s5] It **contrasts with** the **Elo rating system**, an online update rule rather than a fitted model.[^s3] The **Plackett-Luce model** generalises it to rankings of several items, and the **Thurstone-Mosteller model** is the Gaussian-noise counterpart.[^s2][^s4]

## Sources
[^s1]: Hunter, "MM algorithms for generalized Bradley-Terry models", Annals of Statistics 32(1), 2004. https://pure.psu.edu/en/publications/mm-algorithms-for-generalized-bradley-terry-models/ (accessed 2026-11-16)
[^s2]: Hamilton, Tawn and Firth, "The many routes to the ubiquitous Bradley-Terry model", arXiv 2312.13619. https://arxiv.org/pdf/2312.13619 (accessed 2026-11-16)
[^s3]: Aldous, "Lecture 3: Sports rating models", UC Berkeley Statistics, 2017. https://www.stat.berkeley.edu/~aldous/157/Lectures/lecture_3.pdf (accessed 2026-11-16)
[^s4]: Rafailov et al., "Direct Preference Optimization: Your Language Model is Secretly a Reward Model", arXiv 2305.18290v2 / NeurIPS 2023. https://arxiv.org/html/2305.18290v2 (accessed 2026-11-16)
[^s5]: Chiang et al., "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference", arXiv 2403.04132v1, 2024. https://arxiv.org/html/2403.04132v1 (accessed 2026-11-16)
