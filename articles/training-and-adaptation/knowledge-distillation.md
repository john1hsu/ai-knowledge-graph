---
id: kt:knowledge-distillation
type: Technique
title: Knowledge distillation
aliases: [model distillation, teacher-student training, teacher–student learning, soft-target training]
domain: training-and-adaptation
summary: >-
  A training technique in which a smaller "student" model learns to reproduce the outputs (and sometimes the
  internal representations) of a larger "teacher" model or ensemble, so that much of the teacher's accuracy is kept
  at a fraction of its size and inference cost.
maturity: established
broader: [kt:model-compression]
related: [kt:quantization, kt:model-pruning, kt:ensemble-methods, kt:large-language-model, kt:beam-search, kt:synthetic-data]
relations:
  - {predicate: introducedIn, object: kt:distilling-the-knowledge-in-a-neural-network}
  - {predicate: createdBy, object: kt:geoffrey-hinton}
  - {predicate: influencedBy, object: kt:model-compression-caruana-2006}
  - {predicate: usedIn, object: kt:distilbert}
sources:
  - id: s1
    title: "Distilling the Knowledge in a Neural Network"
    publisher: arXiv 1503.02531, NIPS 2014 Deep Learning Workshop (Hinton, Vinyals and Dean)
    url: https://arxiv.org/abs/1503.02531
    type: primary
    accessed: 2026-11-09
  - id: s2
    title: "Distilling the Knowledge in a Neural Network (full text)"
    publisher: ar5iv rendering of arXiv 1503.02531 (Hinton, Vinyals and Dean)
    url: https://ar5iv.labs.arxiv.org/html/1503.02531
    type: primary
    accessed: 2026-11-09
  - id: s3
    title: "Model Compression"
    publisher: KDD 2006, Proceedings of the 12th ACM SIGKDD Conference (Buciluǎ, Caruana and Niculescu-Mizil)
    url: https://cs.cornell.edu/~caruana/compression.kdd06.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s4
    title: "Sequence-Level Knowledge Distillation"
    publisher: EMNLP 2016, pp. 1317–1327 (Kim and Rush)
    url: https://aclanthology.org/D16-1139.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s5
    title: "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter"
    publisher: arXiv 1910.01108 (Sanh, Debut, Chaumond and Wolf, Hugging Face)
    url: https://arxiv.org/pdf/1910.01108
    type: primary
    accessed: 2026-11-09
  - id: s6
    title: "Knowledge Distillation: A Survey"
    publisher: International Journal of Computer Vision 129(6):1789–1819, 2021; authors' arXiv version (Gou, Yu, Maybank and Tao)
    url: https://arxiv.org/pdf/2006.05525v6
    type: peer-reviewed
    accessed: 2026-11-09
created: 2026-11-09
---

# Knowledge distillation

**Knowledge distillation** (KD) trains a compact *student* model to imitate a larger *teacher* — a single big network or a whole ensemble — rather than learning only from ground-truth labels. The term and its now-standard recipe come from Geoffrey Hinton, Oriol Vinyals and Jeff Dean, whose 2015 arXiv paper (presented at the NIPS 2014 Deep Learning Workshop) framed the problem as moving an ensemble's knowledge into one model that is cheap enough to deploy.[^s1] The idea extends earlier work on *model compression* by Buciluǎ, Caruana and Niculescu-Mizil, who in 2006 trained a small neural network to mimic large ensembles of classifiers using teacher-labelled pseudo-data.[^s3]

## How it works

In the Hinton formulation, the teacher's logits *z* are passed through a softmax with a temperature *T*: *q_i* = exp(*z_i*/*T*) / Σ_j exp(*z_j*/*T*). A temperature above 1 flattens the distribution, so the relative probabilities the teacher assigns to *wrong* classes — which digit a "2" most resembles, say — become visible. These **soft targets** carry more information per example than one-hot labels.[^s2] The student is trained at the same high temperature on a weighted sum of two losses: cross-entropy against the soft targets, and ordinary cross-entropy against the true labels at *T* = 1, usually with a smaller weight. Because the gradients of the soft loss shrink roughly as 1/*T*², the authors multiply that term by *T*² so the balance between the two objectives stays stable as *T* is tuned. At deployment the student runs at *T* = 1.[^s2] The paper also shows that the earlier approach of directly regressing the teacher's logits is a special case of distillation in the high-temperature limit.[^s2]

The 2006 model-compression work illustrates the alternative route of generating a large *transfer set*: the authors' MUNGE procedure synthesised extra inputs near real training points, had the ensemble label them, and trained a one-hidden-layer network on the result. Across eight problems the mimic network roughly matched the ensemble's error while being about a thousand times smaller and faster.[^s3]

## Variants

A 2021 survey in the *International Journal of Computer Vision* organises the field along two axes.[^s6] By *what* is transferred: **response-based** knowledge (the teacher's output distribution, as above), **feature-based** knowledge (intermediate activations, as in FitNets' "hints"), and **relation-based** knowledge (relationships between layers or between examples). By *how* training is scheduled: **offline** distillation from a fixed pre-trained teacher (the most common), **online** distillation where teacher and student are updated together, and **self-distillation**, where one network teaches itself, for example from deeper to shallower layers.[^s6]

For sequence models, Kim and Rush proposed **sequence-level KD**: the teacher decodes the training inputs with beam search and the student is trained with plain cross-entropy on those generated outputs. In their 2016 machine-translation experiments the distilled student ran about ten times faster than its teacher with little loss in BLEU, and performed nearly as well with greedy decoding as with beam search.[^s4] Training on teacher-generated text is the same basic pattern later used to distil large language models into smaller ones.

## Evidence and limitations

Hinton et al. reported that on MNIST a small network trained with soft targets made 74 test errors, against 146 for the same network trained on labels alone and 67 for the teacher; on a production speech model, a single distilled network recovered more than 80% of the frame-accuracy gain of a 10-model ensemble.[^s2] DistilBERT (Hugging Face, 2019) combined a distillation loss with masked-language-modelling and hidden-state cosine losses and reported a model about 40% smaller and 60% faster than BERT that kept about 97% of its language-understanding performance on GLUE.[^s5] Limitations are well documented: compression in the 2006 study failed on a dataset with many high-arity categorical features,[^s3] real unlabelled data proved more sample-efficient than synthesised pseudo-data in another,[^s3] and offline setups still pay the full training cost of the large teacher.[^s6] Hinton et al. also found that a transfer set missing a whole class (all the 3s in MNIST) produced most of the student's errors on that class until its bias term for 3s was raised.[^s2]

## Connections

Distillation is one of the main families of model compression, alongside quantization and model pruning; the three are complementary and are often stacked — Kim and Rush pruned an already-distilled student further.[^s4] It was born as a way to deploy ensemble methods cheaply.[^s1][^s3] Sequence-level KD connects it to beam search and, through teacher-generated training data, to synthetic data and to the compression of large language models, of which DistilBERT is an early example.[^s4][^s5]

## Sources

[^s1]: Hinton, Vinyals and Dean, "Distilling the Knowledge in a Neural Network", arXiv 1503.02531 (NIPS 2014 Deep Learning Workshop). https://arxiv.org/abs/1503.02531 (accessed 2026-11-09)
[^s2]: Hinton, Vinyals and Dean, "Distilling the Knowledge in a Neural Network", full text (ar5iv). https://ar5iv.labs.arxiv.org/html/1503.02531 (accessed 2026-11-09)
[^s3]: Buciluǎ, Caruana and Niculescu-Mizil, "Model Compression", KDD 2006. https://cs.cornell.edu/~caruana/compression.kdd06.pdf (accessed 2026-11-09)
[^s4]: Kim and Rush, "Sequence-Level Knowledge Distillation", EMNLP 2016. https://aclanthology.org/D16-1139.pdf (accessed 2026-11-09)
[^s5]: Sanh, Debut, Chaumond and Wolf, "DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter", arXiv 1910.01108. https://arxiv.org/pdf/1910.01108 (accessed 2026-11-09)
[^s6]: Gou, Yu, Maybank and Tao, "Knowledge Distillation: A Survey", International Journal of Computer Vision 129 (2021). https://arxiv.org/pdf/2006.05525v6 (accessed 2026-11-09)
