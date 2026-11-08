---
id: kt:hugging-face-transformers
type: Tool
title: Hugging Face Transformers
aliases: [Transformers library, 🤗 Transformers, pytorch-transformers, pytorch-pretrained-bert]
domain: ai-infrastructure-and-mlops
summary: >-
  An open-source Python library from Hugging Face that provides reference implementations of
  transformer-based and other pretrained models for text, vision, audio and multimodal tasks,
  with a uniform API for loading checkpoints from the Hugging Face Hub, running inference and fine-tuning.
maturity: established
broader: [kt:deep-learning-framework, kt:mlops]
related: [kt:transformer-architecture, kt:fine-tuning, kt:quantization, kt:speculative-decoding, kt:model-serving]
relations:
  - {predicate: createdBy, object: kt:hugging-face}
  - {predicate: introducedIn, object: kt:transformers-state-of-the-art-natural-language-processing}
  - {predicate: dependsOn, object: kt:pytorch}
  - {predicate: usedIn, object: kt:vllm}
sources:
  - id: s1
    title: "Transformers: State-of-the-Art Natural Language Processing"
    publisher: Proceedings of EMNLP 2020, System Demonstrations, pp. 38–45 (Wolf et al., Hugging Face)
    url: https://aclanthology.org/2020.emnlp-demos.6.pdf
    type: peer-reviewed
    accessed: 2026-11-08
  - id: s2
    title: "Transformers documentation (v5.12.0): index"
    publisher: Hugging Face
    url: https://huggingface.co/docs/transformers/v5.12.0/index
    type: official-docs
    accessed: 2026-11-08
  - id: s3
    title: "Transformers v5: Simple model definitions powering the AI ecosystem"
    publisher: Hugging Face blog, 1 December 2025
    url: https://huggingface.co/blog/transformers-v5
    type: primary
    accessed: 2026-11-08
  - id: s4
    title: "Using 🤗 transformers at Hugging Face"
    publisher: Hugging Face Hub documentation
    url: https://huggingface.co/docs/hub/transformers
    type: official-docs
    accessed: 2026-11-08
created: 2026-11-08
---

# Hugging Face Transformers

**Hugging Face Transformers** is an open-source Python library that packages pretrained models, mostly but not only based on the **transformer architecture**, behind a single consistent interface. It was described in a 2020 EMNLP system-demonstration paper by Thomas Wolf and colleagues at Hugging Face, who set out to make it extensible for researchers, simple for practitioners and robust in industrial deployment, and released it under the Apache 2.0 licence.[^s1] Hugging Face's current documentation calls it a "model-definition framework": a shared, canonical definition of each model that training frameworks, inference engines and other libraries can reuse, covering text, vision, audio, video and multimodal models.[^s2]

## How it works

The original paper decomposed every model into three parts: a **tokenizer** that turns raw text into token indices, a **transformer** body that turns those indices into contextual embeddings, and a task-specific **head** (classification, question answering, generation and so on) that adds an output layer and optional loss. Pretrained checkpoints ship with their pretraining head, and the same body can be paired with a different head for fine-tuning.[^s1] The current docs describe the equivalent split as three classes per model: a configuration, the model itself and a preprocessor (a tokenizer, or an image or audio processor for other modalities).[^s2]

**Auto classes** select the right implementation from a checkpoint's configuration, so swapping one architecture for another usually needs only a different model identifier.[^s1] In practice a user passes a Hub model ID either to the high-level `pipeline` function or to `AutoTokenizer` and an `AutoModel*` class via `from_pretrained`, optionally pinning a `revision` (commit, tag or branch); `push_to_hub` uploads models, tokenizers and trainers back to the Hub.[^s4] A typical Hub repository holds a `config.json` architecture blueprint, weights in the `safetensors` format (sharded for large models, with an index file), an optional `generation_config.json`, and tokenizer files that include the chat template.[^s4]

On top of the model classes sit three main features: `Pipeline` for task-level inference, `Trainer` for training with mixed precision, `torch.compile`, FlashAttention and distributed PyTorch training, and `generate` for streaming text generation from LLMs and vision-language models with multiple decoding strategies.[^s2]

## History and scale

At publication in 2020 the library offered models in both PyTorch and TensorFlow, interchangeable between frameworks, and the Hub held 2,097 community-contributed models; the project reported more than 400 external contributors and explored deployment via TorchScript, ONNX export (nearly 4x faster in their BERT, RoBERTa and GPT-2 tests) and CoreML.[^s1] Hugging Face's December 2025 announcement of version 5, five years after the v4 release candidate, reported growth from 40 to over 400 supported architectures, roughly 1,000 to over 750,000 compatible Hub checkpoints, and from about 20,000 to over 3 million pip installs per day (figures as reported by Hugging Face).[^s3] The v5.12 documentation cites over 1 million Transformers checkpoints on the Hub.[^s2]

Version 5 made PyTorch the sole backend, sunsetting TensorFlow and Flax support; centralised attention variants (SDPA, FlashAttention, FlexAttention) behind an `AttentionInterface`; promoted modular model files to cut the code needed to add an architecture; made quantized weight loading first-class; and added `transformers serve`, an OpenAI-API-compatible server with continuous batching and paged attention.[^s3]

## Limitations and trade-offs

The library prioritises readable, one-file-per-model definitions over peak throughput, so Hugging Face itself says its built-in serving does not aim to match dedicated engines such as vLLM, SGLang or TensorRT-LLM; its v5 strategy is instead to be the definition those engines import.[^s3] The pace of change carries costs: dropping TensorFlow and Flax and removing the "fast" versus "slow" tokenizer split in v5 are breaking changes for older code.[^s3] Checkpoint counts on the Hub also vary by page and date, so they should be read as order-of-magnitude indicators rather than precise measurements.[^s2][^s4]

## Connections

Transformers sits under **deep-learning frameworks** and the wider **MLOps** toolchain: it depends on **PyTorch** for tensors and autograd, and its model definitions feed downstream inference engines such as **vLLM** and llama.cpp.[^s2][^s3] It is the reference implementation of the **transformer architecture** for most open models and the usual starting point for **fine-tuning** via `Trainer`.[^s2] Its `generate` API offers multiple decoding strategies for LLMs and VLMs,[^s2] which is why the **speculative decoding** node in this graph lists Transformers as an implementation; and its loaders treat **quantization** formats as first-class options.[^s3] With `transformers serve` it also touches **model serving**, though dedicated engines remain the production choice.[^s3] It was created by **Hugging Face** and introduced in the **EMNLP 2020 demo paper**.[^s1]

## Sources
[^s1]: Wolf et al., "Transformers: State-of-the-Art Natural Language Processing", EMNLP 2020 System Demonstrations, pp. 38–45. https://aclanthology.org/2020.emnlp-demos.6.pdf (accessed 2026-11-08)
[^s2]: Hugging Face, "Transformers documentation (v5.12.0)". https://huggingface.co/docs/transformers/v5.12.0/index (accessed 2026-11-08)
[^s3]: Hugging Face, "Transformers v5: Simple model definitions powering the AI ecosystem", 1 December 2025. https://huggingface.co/blog/transformers-v5 (accessed 2026-11-08)
[^s4]: Hugging Face, "Using 🤗 transformers at Hugging Face", Hub documentation. https://huggingface.co/docs/hub/transformers (accessed 2026-11-08)
