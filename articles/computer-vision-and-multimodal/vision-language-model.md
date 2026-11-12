---
id: kt:vision-language-model
type: Architecture
title: "Vision-language model: LLMs with visual input"
aliases: [vision-language model, VLM, VLMs, large vision-language model, LVLM, large multimodal model, multimodal LLM, visual language model]
domain: computer-vision-and-multimodal
summary: >-
  A model that takes images (and often video) together with text as input and generates text, typically
  built by connecting a pretrained image encoder to a pretrained large language model through a learned
  bridge such as a projector, a query transformer or cross-attention layers.
maturity: established
broader: [kt:large-language-model, kt:multimodal-learning]
related: [kt:clip, kt:an-image-is-worth-16x16-words, kt:hallucination, kt:in-context-learning, kt:instruction-tuning]
relations:
  - {predicate: basedOn, object: kt:transformer-architecture}
  - {predicate: basedOn, object: kt:clip}
  - {predicate: introducedIn, object: kt:flamingo-a-visual-language-model-for-few-shot-learning}
  - {predicate: trainedWith, object: kt:instruction-tuning}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: causes, object: kt:hallucination}
sources:
  - id: s1
    title: "Flamingo: a Visual Language Model for Few-Shot Learning"
    publisher: Alayrac et al. (DeepMind), Advances in Neural Information Processing Systems 35 (NeurIPS 2022)
    url: https://papers.neurips.cc/paper_files/paper/2022/file/960a172bc7fbf0177ccccbb411a7d800-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Flamingo: a Visual Language Model for Few-Shot Learning (authors' arXiv version, 2204.14198)"
    publisher: Alayrac et al., arXiv, April 2022 (v2 November 2022)
    url: https://arxiv.org/abs/2204.14198
    type: primary
    accessed: 2026-11-12
  - id: s3
    title: "BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models"
    publisher: Li, Li, Savarese and Hoi, Proceedings of ICML 2023 (PMLR 202), pp. 19730–19742
    url: https://proceedings.mlr.press/v202/li23q.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "Visual Instruction Tuning"
    publisher: Liu, Li, Wu and Lee, Advances in Neural Information Processing Systems 36 (NeurIPS 2023), pp. 34892–34916
    url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/6dcf277ea32ce3288914faf369fe6de0-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s5
    title: "Evaluating Object Hallucination in Large Vision-Language Models"
    publisher: Li, Du, Zhou, Wang, Zhao and Wen, arXiv 2305.10355, May 2023
    url: https://arxiv.org/abs/2305.10355v1
    type: primary
    accessed: 2026-11-12
  - id: s6
    title: "Vision Language Models Explained"
    publisher: Hugging Face blog (merve and Edward Beeching), April 2024
    url: https://huggingface.co/blog/vlms
    type: community
    accessed: 2026-11-12
created: 2026-11-12
---

# Vision-language model: LLMs with visual input

A **vision-language model (VLM)** is a generative model that accepts images, and in many cases video, alongside text and produces text. Typical uses are chatting about a picture, visual question answering, captioning and document understanding; some VLMs can also output bounding boxes or segmentation masks.[^s6] Most modern VLMs are not trained from scratch. They reuse a pretrained vision encoder and a pretrained large language model and learn a comparatively small bridge between them, which makes them an extension of the LLM rather than a separate lineage.[^s1][^s3]

## Origin

The term was popularised by DeepMind's **Flamingo** (Alayrac et al., arXiv April 2022; NeurIPS 2022), which described itself as a family of visual language models able to adapt to new tasks from a handful of examples.[^s2] Flamingo connected two frozen pretrained networks, an NFNet-F6 image encoder and a Chinchilla language model, and trained only new connecting layers; the largest version, Flamingo-80B, sits on a 70-billion-parameter Chinchilla.[^s1] Its training mix included M3W, interleaved images and text drawn from about 43 million web pages, plus large image-caption and video-caption pair datasets. The authors credit the interleaved web data for its few-shot in-context learning.[^s1][^s2] Earlier contrastive dual-encoder models such as CLIP learned a shared image-text embedding space but did not generate free-form text; generative VLMs commonly use a CLIP-style encoder as their eyes.[^s6]

## How it works

A typical VLM has three parts: an **image encoder** (usually a Vision Transformer), a **connector** that maps visual features into the language model's input space, and a **text decoder** (the LLM).[^s6] Designs differ mainly in the connector:

- **Cross-attention with a resampler (Flamingo).** A Perceiver Resampler compresses a variable number of image or video features into 64 visual tokens. Gated cross-attention layers inserted between the frozen LM's layers read those tokens.[^s1]
- **Gating for stability.** Each new layer's output is scaled by tanh(α), with α initialised to zero, so at the start of training the model behaves exactly like the original LM.[^s1]
- **Query transformer (BLIP-2).** A lightweight Querying Transformer (Q-Former) between a frozen image encoder and a frozen LLM is pretrained in two stages: representation learning, then vision-to-language generation.[^s3]
- **Simple projector (LLaVA).** A projection layer feeds CLIP image features directly into the LLM's token sequence, as if they were extra words.[^s4][^s6]

Training is usually staged. In LLaVA's recipe the projector is trained first with the encoder and LLM frozen; in a second stage the LLM is unfrozen and tuned together with the projector, while the encoder stays frozen.[^s6] LLaVA's key contribution was **visual instruction tuning**: a text-only GPT-4 was prompted to write image-grounded instruction-following conversations, and the resulting data turned a pretrained pipeline into a general visual assistant.[^s4] Freezing the large components keeps training cheap. The BLIP-2 authors report beating Flamingo-80B by 8.7% on zero-shot VQAv2 while training 54 times fewer parameters.[^s3] Alternatives exist: KOSMOS-2 trains end to end at higher compute cost, and Fuyu-8B drops the image encoder and projects raw patches straight into the decoder.[^s6]

## Limitations and open questions

The best-documented failure is **object hallucination**: describing objects that are not in the image. A 2023 systematic study found severe object hallucination in several representative VLMs. Objects that are frequent in visual-instruction data, or that commonly co-occur with objects actually present, were especially likely to be invented.[^s5] The same study showed that caption-based hallucination metrics can be skewed by prompts and generation style. It proposed POPE, which polls the model with yes/no questions about specific objects, as a more stable evaluation.[^s5] Other practical caveats: most open models are trained mostly on English, each model expects its own prompt template, and a wrong template can noticeably degrade output.[^s6]

## In practice

As of the April 2024 Hugging Face overview, most users adapt an existing open VLM rather than pretraining one. Fine-tuning is supported in libraries such as TRL, and leaderboards such as the Open VLM Leaderboard and Vision Arena compare submitted models.[^s6] Common evaluation suites include MMMU (11.5K college-level multimodal questions) and MMBench (3,000 single-choice questions across 20 skills, scored with answer shuffling to test consistency). MathVista, AI2D, ScienceQA and OCRBench are also widely used.[^s6] LLaVA's own reported results (NeurIPS 2023) give an 85.1% relative score versus GPT-4 on a synthetic multimodal instruction benchmark and 92.53% on ScienceQA when combined with GPT-4. These are the authors' claims on their chosen evaluations.[^s4]

## Connections

A VLM is a specialisation of the **large language model**: the LLM supplies language ability, reasoning and in-context learning, which Flamingo showed can be extended to few-shot prompts that mix images and text.[^s1] It sits under the wider umbrella of **multimodal learning**. **CLIP** and the **Vision Transformer** (introduced in *An Image Is Worth 16x16 Words*) provide the usual vision encoder.[^s6] **Instruction tuning** is the step that turns a captioning-style model into a conversational assistant, as LLaVA demonstrated.[^s4] VLMs inherit and extend the LLM failure mode of **hallucination**, here grounded in visual content.[^s5] Open VLMs are commonly distributed and run through **Hugging Face Transformers**.[^s6]

## Sources

[^s1]: Alayrac et al., "Flamingo: a Visual Language Model for Few-Shot Learning", NeurIPS 2022. https://papers.neurips.cc/paper_files/paper/2022/file/960a172bc7fbf0177ccccbb411a7d800-Paper-Conference.pdf (accessed 2026-11-12)
[^s2]: Alayrac et al., "Flamingo: a Visual Language Model for Few-Shot Learning", arXiv 2204.14198. https://arxiv.org/abs/2204.14198 (accessed 2026-11-12)
[^s3]: Li, Li, Savarese and Hoi, "BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models", ICML 2023, PMLR 202. https://proceedings.mlr.press/v202/li23q.html (accessed 2026-11-12)
[^s4]: Liu, Li, Wu and Lee, "Visual Instruction Tuning", NeurIPS 2023. https://proceedings.neurips.cc/paper_files/paper/2023/hash/6dcf277ea32ce3288914faf369fe6de0-Abstract.html (accessed 2026-11-12)
[^s5]: Li et al., "Evaluating Object Hallucination in Large Vision-Language Models", arXiv 2305.10355. https://arxiv.org/abs/2305.10355v1 (accessed 2026-11-12)
[^s6]: merve and E. Beeching, "Vision Language Models Explained", Hugging Face blog, April 2024. https://huggingface.co/blog/vlms (accessed 2026-11-12)
