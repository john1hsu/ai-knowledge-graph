---
id: kt:model-compression
type: Paradigm
title: Model compression
aliases: [neural network compression, deep model compression, LLM compression]
domain: inference-and-optimization
summary: >-
  The family of techniques that shrink a trained machine-learning model's memory footprint and inference cost,
  chiefly quantization, pruning, knowledge distillation and low-rank factorization, while trying to keep its
  accuracy close to the original.
maturity: established
broader: [kt:deep-learning]
related: [kt:llm-inference-optimization, kt:large-language-model, kt:gptq, kt:lottery-ticket-hypothesis]
relations:
  - {predicate: introducedIn, object: kt:model-compression-caruana-2006}
  - {predicate: hasPart, object: kt:quantization}
  - {predicate: hasPart, object: kt:model-pruning}
  - {predicate: hasPart, object: kt:knowledge-distillation}
  - {predicate: hasPart, object: kt:low-rank-factorization}
  - {predicate: enables, object: kt:model-serving}
  - {predicate: evaluatedOn, object: kt:perplexity}
sources:
  - id: s1
    title: "Model Compression"
    publisher: KDD 2006 (Bucilă, Caruana and Niculescu-Mizil), authors' copy at Cornell
    url: https://cs.cornell.edu/~caruana/compression.kdd06.pdf
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s2
    title: "Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding"
    publisher: Han, Mao and Dally, authors' arXiv version 1510.00149 (2015; ICLR 2016)
    url: https://arxiv.org/abs/1510.00149v3
    type: primary
    accessed: 2026-11-15
  - id: s3
    title: "Exploiting Linear Structure Within Convolutional Networks for Efficient Evaluation"
    publisher: NeurIPS 2014 (Denton, Zaremba, Bruna, LeCun and Fergus)
    url: https://proceedings.neurips.cc/paper/2014/hash/2afe4567e1bf64d32a5527244d104cea-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s4
    title: "A Survey on Model Compression for Large Language Models"
    publisher: Transactions of the Association for Computational Linguistics 12 (2024), Zhu, Li, Liu, Ma and Wang
    url: https://aclanthology.org/2024.tacl-1.85
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s5
    title: "A Survey on Model Compression for Large Language Models (arXiv HTML version)"
    publisher: Zhu et al., authors' arXiv version 2308.07633v4
    url: https://arxiv.org/html/2308.07633v4
    type: primary
    accessed: 2026-11-15
  - id: s6
    title: "Compressing LLMs: The Truth is Rarely Pure and Never Simple"
    publisher: ICLR 2024 (Jaiswal, Gan, Du, Zhang, Wang and Yang)
    url: https://proceedings.iclr.cc/paper_files/paper/2024/hash/9f09f316a3eaf59d9ced5ffaefe97e0f-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Model compression

**Model compression** is the umbrella term for methods that turn a large, accurate model into a smaller or cheaper one that behaves almost the same at inference time. The motivation is deployment: the most accurate models are often too big, too slow or too power-hungry for phones, embedded devices, real-time services or very large prediction workloads. Today the field is usually organized into four families: quantization, pruning, knowledge distillation and low-rank factorization.[^s4][^s5]

## Origin

The term comes from a 2006 KDD paper by Cristian Bucilă, Rich Caruana and Alexandru Niculescu-Mizil at Cornell. Their targets were not neural networks but ensembles of hundreds or thousands of classifiers, which averaged about 550 MB and took roughly half a second per prediction. They trained a single small neural network to imitate the ensemble on a large pool of synthetic, ensemble-labelled inputs. Across eight binary classification problems the mimic nets came within a hair of the ensemble's error, about 0.264 versus 0.263 RMSE on average, while being roughly a thousand times smaller and faster.[^s1] The function-mimicking idea later became knowledge distillation. "Compression" also grew to cover changes made directly to a network's own weights.

## The main families

- **Quantization** stores weights, and sometimes activations or the KV cache, at lower numeric precision. It is done either after training (post-training quantization) or with retraining to recover accuracy (quantization-aware training), which is costly at LLM scale.[^s5]
- **Pruning** removes redundant parameters. It can be unstructured (individual weights), structured (whole channels, heads or layers), or semi-structured patterns such as N:M sparsity that hardware can accelerate.[^s5]
- **Knowledge distillation** trains a smaller student to reproduce a teacher. With LLMs, black-box distillation uses only the teacher's generated outputs, while white-box distillation also uses its output distributions or internal states.[^s5]
- **Low-rank factorization** approximates a large weight matrix W by the product of two thin matrices, W ≈ UV, so fewer parameters and operations are needed.[^s5] Denton and colleagues showed in 2014 that the redundancy in convolutional filters could be exploited this way. They roughly doubled the speed of convolutional layers on CPU and GPU while keeping accuracy within 1% of the original.[^s3]

These methods stack. Han, Mao and Dally's **Deep Compression** chained magnitude pruning, trained quantization with shared weights, and Huffman coding. It cut AlexNet's storage about 35-fold, from 240 MB to 6.9 MB, and VGG-16's about 49-fold, from 552 MB to 11.3 MB, with no reported loss of ImageNet accuracy. They measured 3-4× layer-wise speedups and 3-7× better energy efficiency on CPU, GPU and mobile GPU. That made the paper a landmark for running vision models on phones.[^s2]

## Measuring success

Zhu and colleagues' 2024 TACL survey lists the usual efficiency metrics. These are parameter count, FLOPs, model FLOPS utilization, latency, the speedup ratio (original over compressed inference time) and the compression ratio (original over compressed size). Quality is typically checked with perplexity on WikiText-2, C4 or PTB plus zero-shot and reasoning benchmarks.[^s5] The survey frames compression as central to running LLMs in resource-limited settings.[^s4]

## Evidence, critiques and open questions

Perplexity can hide damage. Jaiswal and colleagues built the LLM-KICK benchmark of knowledge-intensive tasks to test compressed LLMs. They found that every pruning method they tested degraded noticeably, sometimes at sparsity as low as 25-30%, and that N:M sparsity failed on knowledge-intensive tasks. Current quantization methods held up better than pruning. Pruned models at 50% or more sparsity still did well on in-context retrieval and summarization.[^s6] The 2024 survey adds open problems. These include a remaining performance gap to uncompressed models, the lack of scaling laws for compressed models, hardware-aware evaluation (for example roofline analysis), automating the choice of compression strategy, and explaining why methods such as chain-of-thought distillation work.[^s5] A smaller parameter count also does not guarantee a faster model. Speed depends on whether the hardware and kernels can exploit the new format.[^s2][^s5]

## Connections

Model compression is a branch of **deep learning** engineering, although it was **introduced** for classifier ensembles in the 2006 Caruana paper.[^s1] It **has parts** **quantization**, **model pruning**, **knowledge distillation** and **low-rank factorization**.[^s5] **GPTQ** is linked as one instance of the post-training quantization branch, and the **lottery ticket hypothesis** is among the classic ideas the survey says should be carried over to LLMs.[^s5] By shrinking models for resource-limited deployment, compression **enables** cheaper **model serving** and forms part of **LLM inference optimization**.[^s4] It is commonly **evaluated on** **perplexity**, a practice LLM-KICK challenges.[^s6]

## Sources
[^s1]: Bucilă, Caruana and Niculescu-Mizil, "Model Compression", KDD 2006. https://cs.cornell.edu/~caruana/compression.kdd06.pdf (accessed 2026-11-15)
[^s2]: Han, Mao and Dally, "Deep Compression", arXiv 1510.00149 (ICLR 2016). https://arxiv.org/abs/1510.00149v3 (accessed 2026-11-15)
[^s3]: Denton, Zaremba, Bruna, LeCun and Fergus, "Exploiting Linear Structure Within Convolutional Networks for Efficient Evaluation", NeurIPS 2014. https://proceedings.neurips.cc/paper/2014/hash/2afe4567e1bf64d32a5527244d104cea-Abstract.html (accessed 2026-11-15)
[^s4]: Zhu, Li, Liu, Ma and Wang, "A Survey on Model Compression for Large Language Models", TACL 12 (2024). https://aclanthology.org/2024.tacl-1.85 (accessed 2026-11-15)
[^s5]: Zhu et al., "A Survey on Model Compression for Large Language Models", arXiv 2308.07633v4. https://arxiv.org/html/2308.07633v4 (accessed 2026-11-15)
[^s6]: Jaiswal, Gan, Du, Zhang, Wang and Yang, "Compressing LLMs: The Truth is Rarely Pure and Never Simple", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/9f09f316a3eaf59d9ced5ffaefe97e0f-Abstract-Conference.html (accessed 2026-11-15)
