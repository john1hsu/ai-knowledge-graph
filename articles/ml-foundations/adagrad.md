---
id: kt:adagrad
type: Algorithm
title: AdaGrad
aliases: [Adagrad, adaptive gradient algorithm, adaptive subgradient method, ADAGRAD]
domain: ml-foundations
summary: >-
  An adaptive first-order optimization algorithm, introduced by Duchi, Hazan and Singer (COLT 2010; JMLR 2011), that
  gives each parameter its own learning rate by dividing the step by the square root of that parameter's accumulated
  squared gradients, so rarely updated (sparse) features take larger steps and frequently updated ones take smaller steps.
maturity: established
broader: [kt:gradient-descent, kt:mathematical-optimization]
related: [kt:stochastic-gradient-descent, kt:rmsprop, kt:adam-optimizer, kt:online-learning, kt:distributed-training, kt:embeddings]
relations:
  - {predicate: introducedIn, object: kt:adaptive-subgradient-methods-for-online-learning-and-stochastic-optimization}
  - {predicate: createdBy, object: kt:john-duchi}
  - {predicate: extends, object: kt:stochastic-gradient-descent}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: usedIn, object: kt:glove}
sources:
  - id: s1
    title: "Adaptive Subgradient Methods for Online Learning and Stochastic Optimization"
    publisher: Journal of Machine Learning Research 12(61), 2121–2159 (2011) (Duchi, Hazan and Singer)
    url: https://www.jmlr.org/papers/v12/duchi11a.html
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "Adaptive Subgradient Methods for Online Learning and Stochastic Optimization (COLT 2010 version)"
    publisher: Conference on Learning Theory 2010 (Duchi, Hazan and Singer), learningtheory.org
    url: https://www.learningtheory.org/colt2010/papers/023Duchi.pdf
    type: primary
    accessed: 2026-11-17
  - id: s3
    title: "12.7. Adagrad"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), d2l.ai
    url: https://d2l.ai/chapter_optimization/adagrad.html
    type: textbook
    accessed: 2026-11-17
  - id: s4
    title: "Large Scale Distributed Deep Networks"
    publisher: NeurIPS 2012 (Dean, Corrado, Monga, Chen, Devin, Mao, Ranzato, Senior, Tucker, Yang, Le and Ng)
    url: https://papers.nips.cc/paper_files/paper/2012/file/6aca97005c68f1206823815f66102863-Paper.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s5
    title: "Adam: A Method for Stochastic Optimization"
    publisher: ICLR 2015 (Kingma and Ba), arXiv:1412.6980
    url: https://arxiv.org/pdf/1412.6980
    type: primary
    accessed: 2026-11-17
  - id: s6
    title: "torch.optim.Adagrad"
    publisher: PyTorch documentation (main)
    url: https://docs.pytorch.org/docs/main/generated/torch.optim.Adagrad.html
    type: official-docs
    accessed: 2026-11-17
  - id: s7
    title: "GloVe: Global Vectors for Word Representation"
    publisher: EMNLP 2014 (Pennington, Socher and Manning), ACL Anthology D14-1162
    url: https://aclanthology.org/D14-1162.pdf
    type: peer-reviewed
    accessed: 2026-11-17
created: 2026-11-17
---

# AdaGrad

**AdaGrad** (adaptive gradient) is an optimization algorithm that adapts the learning rate separately for every
parameter, using the history of gradients seen so far. Coordinates that have received large or frequent gradients get
progressively smaller steps, while coordinates that are rarely touched keep comparatively large steps. John Duchi, Elad
Hazan and Yoram Singer presented it at COLT 2010 and published the full treatment in the *Journal of Machine Learning
Research* in 2011.[^s1][^s2] It was one of the first widely used adaptive-learning-rate methods and is a direct
ancestor of RMSProp and Adam.[^s3][^s5]

## Origin

The authors framed AdaGrad within online learning and stochastic optimization, where proximal functions control how far
each update moves. Their idea was to adapt that proximal function to the geometry of the data observed in earlier
iterations, which helps surface rare but highly predictive features and makes the learning rate much easier to set.[^s1]
They proved regret bounds that are competitive with the best proximal function one could have chosen in hindsight.[^s1]
In the diagonal version, the bound scales with the sum of per-coordinate gradient norms; for sparse data the paper shows
this can give regret on the order of log *d* · √*T*, compared with √(*dT*) for plain online gradient descent.[^s2] The
paper also describes a full-matrix variant based on the matrix square root of the summed gradient outer products, which
it notes may be impractical in high dimensions.[^s2] Early experiments on Reuters RCV1 text classification, with about
two million bigram features, found the adaptive variants had lower test error than their non-adaptive
counterparts.[^s2]

## How it works

With an accumulator *s* initialised to zero and all operations applied coordinate-wise, each step computes the gradient
*g*ₜ, adds its square to the accumulator, and scales the update by the inverse square root:[^s3]

- *s*ₜ = *s*ₜ₋₁ + *g*ₜ²
- *w*ₜ = *w*ₜ₋₁ − η · *g*ₜ / √(*s*ₜ + ε)

Here η is a global learning rate and ε a small constant that avoids division by zero.[^s3] The textbook treatment in
*Dive into Deep Learning* motivates this two ways. First, sparse features such as rare words only get meaningful
updates when they appear, so a single global decay schedule can shrink too fast for them; accumulating squared gradients
replaces a crude occurrence count. Second, the per-coordinate scaling acts as a cheap diagonal preconditioner, using
gradient magnitude as a stand-in for the Hessian diagonal on ill-conditioned problems.[^s3] The method keeps one extra
state value per parameter, and its cost per step is close to that of stochastic gradient descent.[^s3]

## Limitations

Because the accumulator only grows, the effective learning rate decays roughly as O(*t*^−1/2) per coordinate. That is
adequate for convex problems but often too aggressive for deep networks, where steps may need to stay large for
longer.[^s3] Kingma and Ba's Adam paper shows AdaGrad is equivalent to a version of Adam with β₁ = 0, infinitesimal
(1 − β₂) and a step size annealed as *t*^−1/2; Adam replaces the ever-growing sum with exponential moving averages.[^s5]
In their 2014 experiments, AdaGrad beat SGD with Nesterov momentum by a wide margin on sparse bag-of-words logistic
regression (IMDB), but converged more slowly than other methods on MNIST logistic regression and on a CIFAR-10
convolutional network.[^s5]

## In practice

AdaGrad found an early large-scale use at Google: the DistBelief system paired it with asynchronous Downpour SGD,
keeping per-parameter rates locally in each parameter-server shard. The authors reported that this let more model
replicas work productively and, with warm starting, virtually eliminated stability problems; the combination was the
dominant method in their speech-model experiments at budgets of up to 2,000 CPU cores.[^s4] It remains available in
standard frameworks: as of November 2026, PyTorch's `torch.optim.Adagrad` defaults to a learning rate of 0.01,
ε = 1e-10 and a zero initial accumulator, with optional learning-rate decay and weight decay.[^s6] Its strength on
sparse gradients made it a natural fit for word-embedding training; the GloVe vectors were trained with AdaGrad at an initial learning rate of 0.05.[^s7]

## Connections

AdaGrad is a refinement of **gradient descent** and, more broadly, a method of **mathematical optimization**; it
**extends stochastic gradient descent** by adding per-coordinate adaptive step sizes.[^s1][^s3] It was **introduced in**
the JMLR paper by Duchi, Hazan and Singer and is **created by** **John Duchi** with co-authors, in the setting of
**online learning**.[^s1] Its aggressive decay motivated **RMSProp** and **Adam**, which is formally related to it.[^s3][^s5]
It shaped early **distributed training** at scale through DistBelief,[^s4] is **implemented in** **PyTorch**,[^s6] and
is **used in** training **GloVe** and similar **embeddings** where gradients are sparse.[^s7]

## Sources
[^s1]: Duchi, Hazan and Singer, "Adaptive Subgradient Methods for Online Learning and Stochastic Optimization", JMLR 12 (2011). https://www.jmlr.org/papers/v12/duchi11a.html (accessed 2026-11-17)
[^s2]: Duchi, Hazan and Singer, "Adaptive Subgradient Methods for Online Learning and Stochastic Optimization", COLT 2010. https://www.learningtheory.org/colt2010/papers/023Duchi.pdf (accessed 2026-11-17)
[^s3]: Zhang, Lipton, Li and Smola, "12.7. Adagrad", *Dive into Deep Learning*. https://d2l.ai/chapter_optimization/adagrad.html (accessed 2026-11-17)
[^s4]: Dean et al., "Large Scale Distributed Deep Networks", NeurIPS 2012. https://papers.nips.cc/paper_files/paper/2012/file/6aca97005c68f1206823815f66102863-Paper.pdf (accessed 2026-11-17)
[^s5]: Kingma and Ba, "Adam: A Method for Stochastic Optimization", ICLR 2015. https://arxiv.org/pdf/1412.6980 (accessed 2026-11-17)
[^s6]: PyTorch, "torch.optim.Adagrad". https://docs.pytorch.org/docs/main/generated/torch.optim.Adagrad.html (accessed 2026-11-17)
[^s7]: Pennington, Socher and Manning, "GloVe: Global Vectors for Word Representation", EMNLP 2014. https://aclanthology.org/D14-1162.pdf (accessed 2026-11-17)
