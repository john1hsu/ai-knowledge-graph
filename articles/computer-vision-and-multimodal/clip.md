---
id: kt:clip
type: Model
title: CLIP
aliases: [Contrastive Language-Image Pre-training, Contrastive Language-Image Pretraining, OpenAI CLIP]
domain: computer-vision-and-multimodal
summary: >-
  A dual-encoder vision-language model from OpenAI (2021) that trains an image encoder and a text encoder
  jointly with a contrastive objective on hundreds of millions of web image-caption pairs, so that images
  and text share one embedding space and new visual categories can be recognized zero-shot from
  natural-language descriptions.
maturity: established
broader: [kt:vision-language-model, kt:representation-learning]
related: [kt:embeddings, kt:contrastive-learning, kt:vision-transformer, kt:diffusion-model, kt:large-language-model, kt:scaling-laws]
relations:
  - {predicate: introducedIn, object: kt:learning-transferable-visual-models-from-natural-language-supervision}
  - {predicate: createdBy, object: kt:openai}
  - {predicate: basedOn, object: kt:transformer-architecture}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
  - {predicate: enables, object: kt:zero-shot-learning}
sources:
  - id: s1
    title: "Learning Transferable Visual Models From Natural Language Supervision"
    publisher: Radford, Kim, Hallacy, Ramesh, Goh, Agarwal, Sastry, Askell, Mishkin, Clark, Krueger and Sutskever, Proceedings of ICML 2021 (PMLR 139), pp. 8748–8763
    url: https://proceedings.mlr.press/v139/radford21a.html
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s2
    title: "Learning Transferable Visual Models From Natural Language Supervision (authors' arXiv version, 2103.00020v1)"
    publisher: Radford et al., OpenAI, February 2021
    url: https://arxiv.org/pdf/2103.00020v1
    type: primary
    accessed: 2026-11-09
  - id: s3
    title: "CLIP — Transformers documentation"
    publisher: Hugging Face
    url: https://huggingface.co/docs/transformers/model_doc/clip
    type: official-docs
    accessed: 2026-11-09
  - id: s4
    title: "Reproducible Scaling Laws for Contrastive Language-Image Learning"
    publisher: Cherti, Beaumont, Wightman, Wortsman, Ilharco, Gordon, Schuhmann, Schmidt and Jitsev, CVPR 2023, pp. 2818–2829
    url: https://openaccess.thecvf.com/content/CVPR2023/papers/Cherti_Reproducible_Scaling_Laws_for_Contrastive_Language-Image_Learning_CVPR_2023_paper.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s5
    title: "Sigmoid Loss for Language Image Pre-Training"
    publisher: Zhai, Mustafa, Kolesnikov and Beyer, ICCV 2023, pp. 11975–11986
    url: https://openaccess.thecvf.com/content/ICCV2023/papers/Zhai_Sigmoid_Loss_for_Language_Image_Pre-Training_ICCV_2023_paper.pdf
    type: peer-reviewed
    accessed: 2026-11-09
  - id: s6
    title: "Visual Instruction Tuning (authors' arXiv version, 2304.08485v2; NeurIPS 2023)"
    publisher: Liu, Li, Wu and Lee
    url: https://arxiv.org/pdf/2304.08485v2
    type: primary
    accessed: 2026-11-09
created: 2026-11-09
---

# CLIP

**CLIP** (Contrastive Language-Image Pre-training) is a vision-language model introduced by Alec Radford and colleagues at OpenAI, posted in February 2021 and published at ICML 2021.[^s1][^s2] Instead of training an image classifier on a fixed list of labelled categories, CLIP learns from raw captions paired with images: it is trained to tell which caption belongs to which image. Because images and text end up in a shared embedding space, a user can classify an image into any set of categories simply by writing them down as text, with no task-specific training. This "zero-shot" transfer is CLIP's defining capability.[^s1]

## How it works

CLIP has two towers: an image encoder and a text encoder, each followed by a projection into a common embedding space, where similarity is the dot product (cosine similarity after normalization).[^s3] The authors trained ResNet variants (ResNet-50 up to RN50x64) and Vision Transformers (ViT-B/32, ViT-B/16 and ViT-L/14) as image encoders, paired with a 63M-parameter, 12-layer, 512-wide Transformer text encoder; the best released model was ViT-L/14 fine-tuned for one extra epoch at 336-pixel resolution.[^s2]

Training uses a batch of N image-text pairs. The model computes all N×N image-text similarities and is trained with a symmetric cross-entropy loss that raises the scores of the N true pairs and lowers the N²−N mismatched ones, scaled by a learned temperature. The paper used a batch size of 32,768.[^s2] The authors report that this contrastive objective was markedly more compute-efficient than predicting caption text: a bag-of-words predictor learned about 3× faster than a Transformer captioning model, and switching to the contrastive objective gave roughly a further 4× gain.[^s2]

The training set, called WIT, contained 400 million image-text pairs gathered from the internet using about 500,000 search queries, capped at 20,000 pairs per query to keep it balanced.[^s2] Training the largest ResNet took 18 days on 592 V100 GPUs; the largest ViT took 12 days on 256 V100 GPUs.[^s2]

**Zero-shot classification.** To classify an image, one embeds each class name inside a text prompt such as "a photo of a {label}.", embeds the image, and picks the prompt with the highest similarity. On ImageNet, this template alone added 1.3 points of accuracy and ensembling 80 prompt templates added another 3.5.[^s2] Hugging Face exposes the same procedure through a `zero-shot-image-classification` pipeline and the `CLIPModel` and `CLIPProcessor` classes, with OpenAI's original checkpoints hosted on the Hub.[^s3]

## Results and limitations

Zero-shot CLIP matched the accuracy of the original supervised ResNet-50 on ImageNet without using any of its 1.28 million labelled training images, and was evaluated on more than 30 existing vision datasets.[^s1] The authors also found that zero-shot models were considerably more robust to natural distribution shifts, closing up to 75% of the "robustness gap" seen in ImageNet-trained models.[^s2]

The paper is candid about weaknesses. Zero-shot CLIP struggled with fine-grained classification (car models, aircraft, flower species), counting, and abstract tasks such as estimating distance; it reached only 88% on MNIST digits, below logistic regression on raw pixels, and generally trailed fully supervised linear classifiers by about 10–25 points.[^s2] The authors estimated that roughly a 1000× increase in compute would be needed for zero-shot CLIP to reach state-of-the-art results overall, and they analysed social biases inherited from uncurated web data.[^s2]

## Successors and use in practice

Because the WIT dataset was never released, LAION's OpenCLIP project retrained CLIP-style models on the public LAION datasets. Cherti et al. (CVPR 2023) found power-law scaling with model size, data and samples seen across zero-shot classification, retrieval and fine-tuning, and observed that the training data shapes the scaling curve: OpenAI's models scaled better on ImageNet classification, LAION-trained ones on retrieval. Their largest measured model, ViT-H/14 on LAION-2B, reached 78.0% zero-shot ImageNet top-1 accuracy (reported in 2023).[^s4]

Google's SigLIP (ICCV 2023) replaced CLIP's batch-wide softmax with an independent sigmoid loss per image-text pair. This removes the global normalization, lets the loss be computed in chunks across devices, and performs better at small batch sizes; the authors found that gains largely saturate around a 32k batch.[^s5]

CLIP encoders became common building blocks. LLaVA (NeurIPS 2023), an early open vision-language assistant, feeds features from a frozen CLIP ViT-L/14 through a trainable linear projection into the Vicuna language model.[^s6] CLIP-style embeddings are also used directly for zero-shot image-text retrieval, one of the tasks on which OpenCLIP models are benchmarked.[^s4]

## Connections

CLIP is a **vision-language model** and an instance of **representation learning**: its output is a joint image-text **embedding** space rather than a fixed classifier.[^s1][^s3] It was **introduced in** *Learning Transferable Visual Models From Natural Language Supervision* and **created by** OpenAI.[^s1] Both towers can be **Transformers**, including the **Vision Transformer**, and its training objective is a form of **contrastive learning**.[^s2] It **enables zero-shot learning** for image classification and is **implemented in** Hugging Face Transformers.[^s2][^s3] It is related to **diffusion models** as a neighbouring multimodal node: CLIP learns to match images with text, whereas diffusion models learn to generate images.[^s1] OpenCLIP's results connect it to **scaling laws**, and LLaVA shows how a CLIP encoder is bolted onto a **large language model**.[^s4][^s6]

## Sources
[^s1]: Radford et al., "Learning Transferable Visual Models From Natural Language Supervision", Proceedings of ICML 2021, PMLR 139:8748–8763. https://proceedings.mlr.press/v139/radford21a.html (accessed 2026-11-09)
[^s2]: Radford et al., "Learning Transferable Visual Models From Natural Language Supervision", arXiv 2103.00020v1, 2021. https://arxiv.org/pdf/2103.00020v1 (accessed 2026-11-09)
[^s3]: Hugging Face, "CLIP", Transformers documentation. https://huggingface.co/docs/transformers/model_doc/clip (accessed 2026-11-09)
[^s4]: Cherti et al., "Reproducible Scaling Laws for Contrastive Language-Image Learning", CVPR 2023, pp. 2818–2829. https://openaccess.thecvf.com/content/CVPR2023/papers/Cherti_Reproducible_Scaling_Laws_for_Contrastive_Language-Image_Learning_CVPR_2023_paper.pdf (accessed 2026-11-09)
[^s5]: Zhai, Mustafa, Kolesnikov and Beyer, "Sigmoid Loss for Language Image Pre-Training", ICCV 2023, pp. 11975–11986. https://openaccess.thecvf.com/content/ICCV2023/papers/Zhai_Sigmoid_Loss_for_Language_Image_Pre-Training_ICCV_2023_paper.pdf (accessed 2026-11-09)
[^s6]: Liu, Li, Wu and Lee, "Visual Instruction Tuning", NeurIPS 2023, arXiv 2304.08485v2. https://arxiv.org/pdf/2304.08485v2 (accessed 2026-11-09)
