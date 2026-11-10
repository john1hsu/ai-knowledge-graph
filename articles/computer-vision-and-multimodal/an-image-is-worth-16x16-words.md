---
id: kt:an-image-is-worth-16x16-words
type: Work
title: "An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale"
aliases: [Dosovitskiy et al. 2021, the ViT paper]
domain: computer-vision-and-multimodal
summary: >-
  The ICLR 2021 paper by Dosovitskiy and eleven Google Research colleagues that introduced the Vision
  Transformer (ViT): it cuts an image into fixed-size patches, embeds each patch as a token and feeds the
  sequence to a nearly unmodified Transformer encoder, showing that with enough pre-training data this
  convolution-free model matches or beats state-of-the-art CNNs at lower pre-training compute.
maturity: foundational
broader: [kt:image-classification]
related: [kt:vision-transformer, kt:convolutional-neural-network, kt:clip, kt:scaling-laws]
relations:
  - {predicate: createdBy, object: kt:google}
  - {predicate: influencedBy, object: kt:attention-is-all-you-need}
  - {predicate: evaluatedOn, object: kt:vtab}
  - {predicate: runsOn, object: kt:tpu}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: enables, object: kt:vision-language-model}
sources:
  - id: s1
    title: "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (oral)"
    publisher: Dosovitskiy, Beyer, Kolesnikov, Weissenborn, Zhai, Unterthiner, Dehghani, Minderer, Heigold, Gelly, Uszkoreit and Houlsby, ICLR 2021 virtual conference page
    url: https://www.iclr.cc/virtual/2021/oral/3458
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s2
    title: "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (arXiv 2010.11929v2)"
    publisher: Dosovitskiy et al., Google Research, Brain Team; authors' arXiv version (v2, 3 June 2021)
    url: https://arxiv.org/html/2010.11929
    type: primary
    accessed: 2026-11-10
  - id: s3
    title: "Transformers for Image Recognition at Scale"
    publisher: Google Research blog (Neil Houlsby and Dirk Weissenborn), 3 December 2020
    url: https://research.google/blog/transformers-for-image-recognition-at-scale/
    type: lab-research
    accessed: 2026-11-10
  - id: s4
    title: "Dive into Deep Learning, 11.8: Transformers for Vision"
    publisher: Zhang, Lipton, Li and Smola, d2l.ai
    url: https://www.d2l.ai/chapter_attention-mechanisms-and-transformers/vision-transformer.html
    type: textbook
    accessed: 2026-11-10
  - id: s5
    title: "Vision Transformer (ViT) — Transformers documentation"
    publisher: Hugging Face
    url: https://huggingface.co/docs/transformers/model_doc/vit
    type: official-docs
    accessed: 2026-11-10
created: 2026-11-10
---

# An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale

"An Image Is Worth 16x16 Words" is the paper that brought the Transformer from language into mainstream image recognition. Written by Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov and nine other researchers at Google Research's Brain Team, it was presented as an oral at ICLR 2021, with the authors' version also posted to arXiv.[^s1][^s2] Its model, the Vision Transformer (ViT), classifies images using a standard Transformer encoder applied directly to a sequence of image patches, with no convolutional layers in the pure variant.[^s1][^s3]

## How it works

The title states the core trick. An image of height H and width W is split into N = HW/P² square patches of side P (16 pixels in the headline models), each patch is flattened, and a trainable linear projection maps it to a D-dimensional embedding, the visual equivalent of a word embedding.[^s2] A learnable classification token is prepended, learnable 1D position embeddings are added, and the sequence passes through alternating multi-head self-attention and MLP blocks with layer normalization before each block and residual connections after it; the final state of the classification token is the image representation fed to the classifier head.[^s2] The authors found that more elaborate 2D-aware position embeddings gave no significant gain, and that when fine-tuning at a higher resolution than pre-training, the learned position embeddings can simply be interpolated in 2D.[^s2] Textbook implementations perform patching and projection in one step with a convolution whose kernel size and stride both equal the patch size.[^s4]

The paper defined three model sizes: ViT-Base (12 layers, 86M parameters), ViT-Large (24 layers, 307M) and ViT-Huge (32 layers, 632M); a name such as ViT-L/16 adds the patch size.[^s2]

## Key results and the inductive-bias argument

The central finding is about data scale. ViT has much less image-specific inductive bias than a convolutional network: self-attention is global, so locality and two-dimensional structure must be learned rather than built in.[^s2] Trained on ImageNet alone (about 1.3M images) without strong regularization, ViT trailed comparably sized ResNets by a few points and overfit small subsets more readily; pre-trained on ImageNet-21k (about 14M images) or Google's internal JFT-300M (about 303M images), it matched or surpassed them, leading the authors to conclude that large-scale training outweighs the missing inductive bias.[^s2][^s3]

The best model reported, ViT-H/14 pre-trained on JFT-300M, reached 88.55% top-1 accuracy on ImageNet and 77.63% on the 19-task VTAB transfer suite (figures as reported in the 2020–2021 paper).[^s2] The authors also reported that ViT-L/16 beat the BiT-L convolutional baseline on every task they measured while using substantially less pre-training compute, measured in TPUv3-core-days; Google's announcement framed this as roughly four times less compute.[^s2][^s3] A hybrid that feeds CNN feature maps into the Transformer helped at small budgets, but the advantage disappeared for larger models.[^s2] An early self-supervised experiment with masked patch prediction lifted ViT-B/16 to 79.9% on ImageNet, still about 4 points behind supervised pre-training.[^s2]

Analyses in the paper and blog showed that ViT learns image structure anyway: its position embeddings encode row and column similarity, and some heads attend globally even in the lowest layers, unlike the strictly local early layers of a CNN.[^s3]

## Limitations and legacy

The data appetite the paper documented is its main caveat: on small datasets a ViT built from scratch can lose to a ResNet, as the d2l.ai Fashion-MNIST exercise shows.[^s4] Self-attention also scales quadratically with the number of patches, which makes plain ViT costly for high-resolution inputs; follow-ups such as DeiT (data-efficient training on ImageNet alone) and Swin Transformer (windowed attention that reintroduces convolution-like priors) were responses to these limits.[^s4] In practice, the released checkpoints remain widely used: Hugging Face Transformers ships `ViTModel` and `ViTForImageClassification`, with checkpoint names such as `google/vit-base-patch16-224` encoding patch size and resolution, and an option to interpolate position embeddings for higher-resolution fine-tuning.[^s5]

## Connections

The paper sits under **image classification**, the task it targeted, and is **influenced by** *Attention Is All You Need*, whose encoder it reuses with minimal change.[^s1][^s2] It **introduced** the **vision transformer** architecture, the patch-token image encoder that later multimodal work such as **CLIP** and **vision-language models** builds on (see those nodes), and its argument against hand-built priors positions it as an alternative to the **convolutional neural network**.[^s3][^s4] Its finding that performance kept improving with data and model size ties it to **scaling laws**; it was **created by** **Google**, pre-trained on Cloud **TPUs**, **evaluated on** VTAB among other benchmarks, and is **implemented in** **Hugging Face Transformers**.[^s2][^s5]

## Sources

[^s1]: Dosovitskiy et al., "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale", ICLR 2021 oral. https://www.iclr.cc/virtual/2021/oral/3458 (accessed 2026-11-10)
[^s2]: Dosovitskiy et al., arXiv 2010.11929v2, Google Research, 2021. https://arxiv.org/html/2010.11929 (accessed 2026-11-10)
[^s3]: Houlsby and Weissenborn, "Transformers for Image Recognition at Scale", Google Research blog, 3 December 2020. https://research.google/blog/transformers-for-image-recognition-at-scale/ (accessed 2026-11-10)
[^s4]: Zhang, Lipton, Li and Smola, *Dive into Deep Learning*, 11.8 "Transformers for Vision". https://www.d2l.ai/chapter_attention-mechanisms-and-transformers/vision-transformer.html (accessed 2026-11-10)
[^s5]: Hugging Face, "Vision Transformer (ViT)", Transformers documentation. https://huggingface.co/docs/transformers/model_doc/vit (accessed 2026-11-10)
