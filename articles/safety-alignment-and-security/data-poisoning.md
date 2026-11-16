---
id: kt:data-poisoning
type: Risk
title: Data poisoning
aliases: [poisoning attack, training data poisoning, dataset poisoning]
domain: safety-alignment-and-security
summary: >-
  A training-time attack in which an adversary inserts or modifies training examples so that the resulting model
  performs worse overall, misbehaves on chosen inputs, or carries a hidden backdoor that a trigger activates.
maturity: established
broader: [kt:adversarial-machine-learning]
related: [kt:benchmark-contamination, kt:red-teaming, kt:model-extraction, kt:federated-learning]
relations:
  - {predicate: hasPart, object: kt:backdoor-attack}
  - {predicate: contrastsWith, object: kt:adversarial-example}
  - {predicate: exploits, object: kt:pretraining}
sources:
  - id: s1
    title: "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (NIST AI 100-2 E2025)"
    publisher: NIST (Vassilev, Oprea, Fordyce, Anderson, Davies, Hamin), March 2025
    url: https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf
    type: government
    accessed: 2026-11-16
  - id: s2
    title: "Poisoning Attacks against Support Vector Machines"
    publisher: arXiv:1206.6389 (Biggio, Nelson, Laskov), 2012
    url: https://arxiv.org/abs/1206.6389
    type: primary
    accessed: 2026-11-16
  - id: s3
    title: "BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain"
    publisher: arXiv:1708.06733 (Gu, Dolan-Gavitt, Garg), 2017
    url: https://arxiv.org/abs/1708.06733
    type: primary
    accessed: 2026-11-16
  - id: s4
    title: "Poisoning Web-Scale Training Datasets is Practical"
    publisher: arXiv:2302.10149 (Carlini, Jagielski, Choquette-Choo, Paleka, Pearce, Anderson, Terzis, Thomas, Tramèr), 2023
    url: https://arxiv.org/abs/2302.10149v2
    type: primary
    accessed: 2026-11-16
  - id: s5
    title: "A small number of samples can poison LLMs of any size"
    publisher: Anthropic, with the UK AI Security Institute and The Alan Turing Institute, October 2025
    url: https://www.anthropic.com/research/small-samples-poison?from_blog=true
    type: lab-research
    accessed: 2026-11-16
created: 2026-11-16
---

# Data poisoning

Data poisoning is an attack on the training stage of a machine learning system: the adversary controls part of the training set, by inserting new samples or altering existing ones, so that the model learned from it behaves as the attacker wants.[^s1] NIST's adversarial machine learning taxonomy (AI 100-2 E2025) treats poisoning as one of the three main attack classes against predictive AI, alongside evasion and privacy attacks, and distinguishes it from **model poisoning**, where the attacker manipulates parameters directly, as in federated learning or a compromised model supply chain.[^s1]

## Origins

A widely cited early formalization of poisoning is Biggio, Nelson and Laskov's 2012 work on support vector machines. They noted that learning algorithms usually assume well-behaved training data, an assumption that fails in security settings, and showed that an attacker who can predict how a model's decision boundary will shift can craft training points that raise its test error.[^s2] Their attack used gradient ascent on the model's validation error and could be kernelized, so poison points were built in input space even for non-linear kernels.[^s2]

In 2017 Gu, Dolan-Gavitt and Garg shifted attention to deep networks and the model supply chain. Their "BadNets" were trained to match state-of-the-art accuracy on the user's own validation data while misbehaving on attacker-chosen inputs; in one demonstration a road-sign classifier read a stop sign bearing a particular sticker as a speed-limit sign.[^s3] They argued that outsourced training and reuse of pretrained models create the opening, and that the backdoor can persist after the model is retrained for another task.[^s3]

## Attack types

NIST classifies poisoning by the attacker's objective and capability.[^s1]

- **Availability poisoning** degrades accuracy across most inputs; flipping labels is the simplest form.[^s1]
- **Targeted poisoning** changes predictions on a small set of chosen samples, usually in a clean-label setting.[^s1]
- **Backdoor poisoning** makes any input that contains a trigger pattern misclassify, which needs influence over both training data and later test inputs.[^s1]
- **Clean-label poisoning** leaves labels untouched; it typically needs more poisoned samples but is a more realistic threat model.[^s1]

## Poisoning at web scale

Foundation models are trained on data crawled from the open web, which widens the attack surface. Carlini and colleagues described two practical routes in 2023. **Split-view poisoning** exploits the fact that web content can change between when a dataset is indexed and when a user later downloads it, and **frontrunning poisoning** targets datasets built by snapshotting crowd-sourced sites, where an attacker needs only a brief window of edits.[^s4] They estimated that about 0.01% of LAION-400M or COYO-700M could have been poisoned for roughly US$60, and they notified the affected dataset maintainers before publication.[^s4]

A 2025 study by Anthropic, the UK AI Security Institute and The Alan Turing Institute examined backdoors in language-model pretraining. Training models from 600 million to 13 billion parameters, the authors reported that about 250 poisoned documents installed a simple denial-of-service backdoor at every model size tested, so the absolute number of poisons, not their share of the corpus, determined success.[^s5] They cautioned that the backdoor only produced gibberish, that 100 documents was not reliably enough, and that it is unknown whether the finding extends to larger models or more harmful behaviors.[^s5]

## Defenses and limits

NIST lists several families of mitigation: sanitizing training data (outlier detection, clustering, provenance and integrity checks), robust training that bounds the influence of any one sample, trigger reconstruction, inspecting and repairing trained models, certified defenses with provable guarantees, and Byzantine-resilient aggregation for federated learning.[^s1] Each has gaps. Availability attacks are often noticed only after performance has already dropped; sanitization struggles with stealthy poisons; targeted poisoning is notoriously hard to defend; many backdoor defenses were designed for image classifiers with fixed triggers; and verifying how a third-party model was trained remains an open problem because training is nondeterministic.[^s1] The Anthropic-led team argued that poisoning is somewhat defense-favored, since attackers must commit their data before defenders inspect the corpus and model, but that defenses must work even when the number of poisons is small and constant.[^s5]

## Connections

Data poisoning is a core attack class within **adversarial machine learning**, and **backdoor attacks** are its most studied sub-type.[^s1][^s3] It contrasts with the **adversarial example**, which manipulates inputs at test time rather than training data.[^s1] It exploits the scale of web-crawled **pretraining** corpora, and model poisoning is a recognized threat in **federated learning**.[^s1][^s4] It is related to **benchmark contamination**, another failure of training-data integrity, though contamination is usually accidental, and to **model extraction**, a privacy attack in the same taxonomy.[^s1] **Red teaming** exercises probe deployed models for implanted behaviors.

## Sources
[^s1]: NIST, "Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations" (NIST AI 100-2 E2025), March 2025. https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-2e2025.pdf (accessed 2026-11-16)
[^s2]: Biggio, Nelson & Laskov, "Poisoning Attacks against Support Vector Machines", arXiv:1206.6389, 2012. https://arxiv.org/abs/1206.6389 (accessed 2026-11-16)
[^s3]: Gu, Dolan-Gavitt & Garg, "BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain", arXiv:1708.06733, 2017. https://arxiv.org/abs/1708.06733 (accessed 2026-11-16)
[^s4]: Carlini et al., "Poisoning Web-Scale Training Datasets is Practical", arXiv:2302.10149, 2023. https://arxiv.org/abs/2302.10149v2 (accessed 2026-11-16)
[^s5]: Anthropic, UK AI Security Institute & The Alan Turing Institute, "A small number of samples can poison LLMs of any size", October 2025. https://www.anthropic.com/research/small-samples-poison?from_blog=true (accessed 2026-11-16)
