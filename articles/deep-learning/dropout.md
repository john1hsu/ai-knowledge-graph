---
id: kt:dropout
type: Technique
title: Dropout
aliases: [dropout regularization, inverted dropout, dropout training]
domain: deep-learning
summary: >-
  A regularization technique for neural networks that randomly zeroes a fraction of unit activations on each
  training step, so the network cannot rely on fragile co-adaptations between units; at inference the full
  network is used, approximating an average over the exponentially many "thinned" subnetworks seen in training.
maturity: established
broader: [kt:regularization, kt:deep-learning]
related: [kt:overfitting, kt:artificial-neural-network, kt:bias-variance-tradeoff, kt:ensemble-methods, kt:geoffrey-hinton]
relations:
  - {predicate: introducedIn, object: kt:dropout-a-simple-way-to-prevent-neural-networks-from-overfitting}
  - {predicate: mitigates, object: kt:overfitting}
  - {predicate: createdBy, object: kt:geoffrey-hinton}
  - {predicate: implementedIn, object: kt:pytorch}
  - {predicate: alternativeTo, object: kt:weight-decay}
  - {predicate: enables, object: kt:monte-carlo-dropout}
sources:
  - id: s1
    title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
    publisher: Journal of Machine Learning Research 15(56), 1929–1958 (2014) (Srivastava, Hinton, Krizhevsky, Sutskever and Salakhutdinov)
    url: https://www.jmlr.org/papers/v15/srivastava14a.html
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s2
    title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting (full text PDF)"
    publisher: JMLR 15 (2014), author PDF hosted by the Bau Lab paper archive
    url: https://papers.baulab.info/papers/also/Srivastava-2014.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s3
    title: "Improving neural networks by preventing co-adaptation of feature detectors"
    publisher: arXiv:1207.0580 (July 2012) (Hinton, Srivastava, Krizhevsky, Sutskever and Salakhutdinov)
    url: https://arxiv.org/abs/1207.0580
    type: primary
    accessed: 2026-11-09
  - id: s4
    title: "4.6. Dropout"
    publisher: Zhang, Lipton, Li and Smola, Dive into Deep Learning (classic.d2l.ai)
    url: https://classic.d2l.ai/chapter_multilayer-perceptrons/dropout.html
    type: textbook
    accessed: 2026-11-09
  - id: s5
    title: "torch.nn.Dropout"
    publisher: PyTorch 2.6 documentation
    url: https://docs.pytorch.org/docs/2.6/generated/torch.nn.Dropout.html
    type: official-docs
    accessed: 2026-11-09
  - id: s6
    title: "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning"
    publisher: Proceedings of the 33rd ICML, PMLR 48:1050–1059 (2016) (Gal and Ghahramani)
    url: https://proceedings.mlr.press/v48/gal16
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# Dropout

**Dropout** is a regularization method for neural networks in which, on every training step, each unit is
temporarily removed from the network at random together with its incoming and outgoing connections. Large
networks have enough parameters to memorize small training sets, and the classic remedy of averaging the
predictions of many separately trained networks is too expensive at that scale; dropout offers a cheap
approximation to such an ensemble inside a single model.[^s1] The idea was first released by Geoffrey Hinton,
Nitish Srivastava, Alex Krizhevsky, Ilya Sutskever and Ruslan Salakhutdinov as a July 2012 arXiv report, which
proposed omitting half of the feature detectors on each training case and reported new records on speech and
object recognition benchmarks.[^s3] The full treatment appeared in the *Journal of Machine Learning Research*
in 2014.[^s1]

## How it works

During training, each unit is kept independently with a retention probability *p* (equivalently, dropped with
probability 1 − *p*), so every mini-batch example passes through a different randomly "thinned" network. A
network with *n* droppable units can therefore be viewed as a family of 2<sup>n</sup> weight-sharing
subnetworks. In the original formulation dropout is switched off at test time and each unit's outgoing weights
are multiplied by *p*, so that the expected input to the next layer matches what it saw during training; this
single forward pass approximates averaging the predictions of all the thinned networks, and on MNIST it matched
Monte Carlo averaging over about 50 sampled subnetworks.[^s2]

Modern libraries implement the equivalent **inverted dropout**, which does the rescaling during training
instead. With drop probability *p* (note the flipped meaning), an activation *h* becomes 0 with probability *p*
and *h* / (1 − *p*) otherwise, so its expectation is unchanged and no correction is needed at inference.[^s4]
PyTorch's `torch.nn.Dropout` follows this convention: its argument `p` (default 0.5) is the probability of
zeroing each element, sampled from a Bernoulli distribution on every forward call, surviving outputs are scaled
by 1/(1 − *p*) in training mode, and in evaluation mode the module is simply the identity function.[^s5]
Forgetting to switch a model into evaluation mode is a classic bug, because predictions then stay random.

## Why it works, and its costs

The original authors explained dropout through *co-adaptation*: a unit that can be deleted at any moment cannot
depend on a few specific partners, so it must learn features that are useful in many contexts. They likened
this to sexual reproduction, where genes must work with randomly chosen partners.[^s2][^s3] The *Dive into
Deep Learning* textbook presents this as intuition rather than settled theory, relates dropout to Christopher
Bishop's 1995 result that training with input noise is equivalent to Tikhonov regularization, and notes that
why deep networks generalize remains an open research question.[^s4] A later probabilistic reading by Yarin Gal
and Zoubin Ghahramani showed that dropout training can be interpreted as approximate Bayesian inference in deep
Gaussian processes, which means keeping dropout on at test time and sampling several predictions yields an
estimate of model uncertainty at little extra cost (an approach usually called Monte Carlo dropout).[^s6]

Dropout is not free. Srivastava et al. reported that dropout networks typically take two to three times longer
to train than standard networks of the same architecture, because the gradient updates are noisier.[^s2] They
recommended a retention probability of about 0.5 for hidden units and values closer to 1 (around 0.8) for
real-valued inputs, and found dropout worked best combined with a max-norm constraint on each unit's incoming
weights, large decaying learning rates and high momentum.[^s2] The *Dive into Deep Learning* example likewise
uses lower drop rates near the input (0.2 for the first hidden layer, 0.5 for the second).[^s4]

## Evidence

In the 2014 paper, dropout reduced test error across vision, speech, text and biology tasks. Reported results
include MNIST error falling from 1.60% to 0.95%, SVHN from 3.95% to 2.55%, CIFAR-100 from 43.48% to 37.20%, and
TIMIT phone error from 23.4% to 21.8%; gains on Reuters-RCV1 text classification were smaller (31.05% to
29.62%), and on an alternative-splicing genetics task dropout beat early-stopped networks but trailed a Bayesian
neural network.[^s2] The authors concluded that dropout outperformed the other regularizers they compared and
reached state-of-the-art results on several benchmarks of the time.[^s1]

## Connections

Dropout is a specific form of **regularization** within **deep learning**, aimed squarely at **overfitting**,
the high-variance side of the **bias–variance tradeoff**.[^s1][^s4] Its justification as cheap model averaging
ties it to **ensemble methods**,[^s2] while the textbook framing places it alongside **weight decay** as a
standard alternative or complement for controlling capacity in an **artificial neural network**.[^s4] It was
introduced by **Geoffrey Hinton** and colleagues,[^s3] is built into frameworks such as **PyTorch**,[^s5]
and underpins **Monte Carlo dropout** for uncertainty estimation.[^s6]

## Sources
[^s1]: Srivastava, Hinton, Krizhevsky, Sutskever and Salakhutdinov, "Dropout: A Simple Way to Prevent Neural Networks from Overfitting", JMLR 15(56):1929–1958, 2014. https://www.jmlr.org/papers/v15/srivastava14a.html (accessed 2026-11-09)
[^s2]: Srivastava et al., full text of the JMLR 2014 dropout paper. https://papers.baulab.info/papers/also/Srivastava-2014.pdf (accessed 2026-11-09)
[^s3]: Hinton, Srivastava, Krizhevsky, Sutskever and Salakhutdinov, "Improving neural networks by preventing co-adaptation of feature detectors", arXiv:1207.0580, 2012. https://arxiv.org/abs/1207.0580 (accessed 2026-11-09)
[^s4]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, section 4.6 "Dropout". https://classic.d2l.ai/chapter_multilayer-perceptrons/dropout.html (accessed 2026-11-09)
[^s5]: PyTorch documentation, "torch.nn.Dropout" (v2.6). https://docs.pytorch.org/docs/2.6/generated/torch.nn.Dropout.html (accessed 2026-11-09)
[^s6]: Gal and Ghahramani, "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning", ICML 2016, PMLR 48:1050–1059. https://proceedings.mlr.press/v48/gal16 (accessed 2026-11-09)
