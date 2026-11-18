---
id: kt:recommender-system
type: Application
title: Recommender system
aliases: [recommendation system, recommendation engine, recommender]
domain: retrieval-and-knowledge
summary: >-
  A system that predicts which items (products, videos, articles, songs) a user is likely to prefer and
  ranks a personalised shortlist of them, typically by learning from past user–item interactions
  (collaborative filtering), item attributes (content-based filtering), or both.
maturity: established
broader: [kt:information-retrieval, kt:machine-learning]
related: [kt:multi-armed-bandit, kt:reranking, kt:algorithmic-bias-and-fairness]
relations:
  - {predicate: hasPart, object: kt:collaborative-filtering}
  - {predicate: dependsOn, object: kt:approximate-nearest-neighbor-search}
  - {predicate: evaluatedOn, object: kt:netflix-prize}
sources:
  - id: s1
    title: "Matrix Factorization Techniques for Recommender Systems"
    publisher: IEEE Computer 42(8), 2009 (Koren, Bell and Volinsky); copy hosted on a Columbia University course reading list
    url: https://www.cs.columbia.edu/%7Eblei/fogm/2023F/readings/KorenBellVolinsky2009.pdf
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "Item-based collaborative filtering recommendation algorithms"
    publisher: Proceedings of WWW 2001, ACM, pp. 285–295 (Sarwar, Karypis, Konstan and Riedl); University of Minnesota research portal
    url: https://experts.umn.edu/en/publications/item-based-collaborative-filtering-recommendation-algorithms/
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s3
    title: "Deep Neural Networks for YouTube Recommendations"
    publisher: Google Research; ACM RecSys 2016 (Covington, Adams and Sargin)
    url: https://research.google/pubs/pub45530?hl=es
    type: lab-research
    accessed: 2026-11-18
  - id: s4
    title: "Recommendation systems overview: types and architecture"
    publisher: Google for Developers, Machine Learning recommendation systems course
    url: https://developers.google.cn/machine-learning/recommendation/overview/types?hl=en
    type: official-docs
    accessed: 2026-11-18
created: 2026-11-18
---

# Recommender system

A recommender system estimates how much a given user will value items they have not yet seen and presents a short, personalised ranked list of the most promising ones. Unlike a search engine, it usually works without an explicit query: the user's history of ratings, purchases, clicks or watches stands in for the query. Koren, Bell and Volinsky divide the classic approaches into two families. Content filtering builds explicit profiles of users and items (for a film: genre, cast, popularity) and matches them, while collaborative filtering ignores item content and learns only from past behaviour across many users.[^s1]

## Approaches

**Collaborative filtering** is domain-free and generally more accurate than content filtering, but it suffers from the *cold-start* problem: new users and new items have no interaction history, which is where content-based methods do better.[^s1] Collaborative methods come in two flavours. *Neighbourhood* methods recommend items liked by similar users, or items similar to those a user already liked; *latent factor* models instead infer a modest number of hidden factors (roughly 20 to 100) that characterise both users and items.[^s1]

Sarwar, Karypis, Konstan and Riedl at the University of Minnesota showed at WWW 2001 that *item-based* neighbourhood collaborative filtering scales better than the user-based k-nearest-neighbour approach. Their method first mines the user–item matrix for relationships between items, then uses those item–item similarities (computed by correlation or cosine) to predict a user's preferences, and their experiments found it both faster and more accurate than the best user-based algorithms of the time.[^s2]

## Matrix factorization

The best-known latent factor technique is matrix factorization. Each user *u* receives a vector *p_u* and each item *i* a vector *q_i* in the same low-dimensional space, and the predicted rating is their dot product, *q_iᵀp_u*.[^s1] Because the rating matrix is mostly empty, classic SVD is undefined and imputing the gaps is costly and distorting, so the model is fitted only to observed ratings by minimising regularised squared error, with the regularisation strength picked by cross-validation.[^s1] Two optimisers dominate: stochastic gradient descent, which updates the vectors after each training rating, and alternating least squares, which fixes one set of vectors, solves for the other in closed form, and parallelises well.[^s1]

Practical refinements add a global mean plus per-user and per-item biases (prediction = μ + b_i + b_u + q_iᵀp_u), incorporate *implicit feedback* such as purchases and browsing with confidence weights, and let biases and user preferences drift over time.[^s1]

## The Netflix Prize

Netflix announced its prize in 2006, releasing more than 100 million 1–5 star ratings from about 500,000 customers on over 17,000 films and offering $1 million for a 10% improvement in RMSE over its own system. More than 48,000 teams from 182 countries downloaded the data. The BellKor team won the 2007 Progress Prize with an 8.43% improvement and, jointly with Big Chaos, the 2008 Progress Prize at 9.46%, with matrix factorization at the core of their models.[^s1] The competition made latent factor models the standard baseline for the field.

## Industrial architecture

Large modern recommenders are multi-stage pipelines. Google's recommendation course describes three stages: *candidate generation* shrinks a corpus of billions of items (YouTube's videos, in its example) to hundreds or thousands; *scoring* ranks that smaller set with a more expensive model to pick about ten items; and *re-ranking* applies further constraints such as removing disliked items, boosting freshness, and promoting diversity and fairness.[^s4] Covington, Adams and Sargin described YouTube's deep learning version of this design at RecSys 2016: a deep candidate generation network followed by a separate deep ranking network, and reported large quality gains from switching to deep learning.[^s3]

## Limitations

Cold start remains a persistent problem for behaviour-based models.[^s1] Offline accuracy metrics such as RMSE capture only part of what users value, which is why production systems add re-ranking for freshness, diversity and fairness rather than optimising predicted engagement alone.[^s4] Data sparsity and the cost of serving millions of users in real time also shaped the field's early move to item-based methods.[^s2]

## Connections

Recommender systems are a branch of **information retrieval** that ranks items without an explicit query, and they are built with the tools of **machine learning**.[^s1] **Collaborative filtering** is the core family of methods inside most recommenders.[^s2] Because the candidate-generation stage must narrow billions of items to a few hundred quickly, embedding-based recommenders rely on fast similarity lookup such as **approximate nearest neighbor search**, and the scoring and re-ranking stages parallel second-stage **reranking** in search.[^s3][^s4] The **Netflix Prize** served as the field's landmark benchmark.[^s1] Choosing what to show under uncertainty links recommenders to the **multi-armed bandit** problem, and the fairness goals of re-ranking connect them to **algorithmic bias and fairness**.[^s4]

## Sources

[^s1]: Koren, Bell and Volinsky, "Matrix Factorization Techniques for Recommender Systems", IEEE Computer 42(8), 2009. https://www.cs.columbia.edu/%7Eblei/fogm/2023F/readings/KorenBellVolinsky2009.pdf (accessed 2026-11-18)
[^s2]: Sarwar, Karypis, Konstan and Riedl, "Item-based collaborative filtering recommendation algorithms", WWW 2001, ACM, pp. 285–295. https://experts.umn.edu/en/publications/item-based-collaborative-filtering-recommendation-algorithms/ (accessed 2026-11-18)
[^s3]: Covington, Adams and Sargin, "Deep Neural Networks for YouTube Recommendations", ACM RecSys 2016, Google Research. https://research.google/pubs/pub45530?hl=es (accessed 2026-11-18)
[^s4]: Google for Developers, "Recommendation systems overview: types and architecture". https://developers.google.cn/machine-learning/recommendation/overview/types?hl=en (accessed 2026-11-18)
