---
id: kt:image-captioning
type: Application
title: Image captioning
aliases: [automatic image captioning, image description generation, image-to-text generation]
domain: computer-vision-and-multimodal
summary: >-
  The task of automatically generating a natural-language sentence that describes the content of an
  image, typically solved with an encoder-decoder network that conditions a language decoder on visual
  features and scored against human-written reference captions.
maturity: established
broader: [kt:computer-vision]
related: [kt:attention-mechanism, kt:beam-search, kt:bleu, kt:vision-language-model, kt:recurrent-neural-network]
relations:
  - {predicate: introducedIn, object: kt:show-and-tell-a-neural-image-caption-generator}
  - {predicate: basedOn, object: kt:sequence-to-sequence-learning}
  - {predicate: evaluatedOn, object: kt:ms-coco}
  - {predicate: evaluatedOn, object: kt:cider}
  - {predicate: contrastsWith, object: kt:image-classification}
sources:
  - id: s1
    title: "Show and Tell: A Neural Image Caption Generator"
    publisher: CVPR 2015 (Vinyals, Toshev, Bengio, Erhan)
    url: https://openaccess.thecvf.com/content_cvpr_2015/html/Vinyals_Show_and_Tell_2015_CVPR_paper.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s2
    title: "Show, Attend and Tell: Neural Image Caption Generation with Visual Attention"
    publisher: Xu, Ba, Kiros, Cho, Courville, Salakhutdinov, Zemel and Bengio; arXiv 1502.03044 (authors' version of the ICML 2015 paper)
    url: https://arxiv.org/abs/1502.03044v3
    type: primary
    accessed: 2026-11-18
  - id: s3
    title: "Microsoft COCO Captions: Data Collection and Evaluation Server"
    publisher: Chen, Fang, Lin, Vedantam, Gupta, Dollár and Zitnick; arXiv 1504.00325
    url: https://arxiv.org/abs/1504.00325
    type: primary
    accessed: 2026-11-18
  - id: s4
    title: "CIDEr: Consensus-Based Image Description Evaluation"
    publisher: CVPR 2015 (Vedantam, Zitnick, Parikh)
    url: https://openaccess.thecvf.com/content_cvpr_2015/html/Vedantam_CIDEr_Consensus-Based_Image_2015_CVPR_paper.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s5
    title: "Bottom-Up and Top-Down Attention for Image Captioning and Visual Question Answering"
    publisher: CVPR 2018 (Anderson, He, Buehler, Teney, Johnson, Gould, Zhang)
    url: https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Bottom-Up_and_Top-Down_CVPR_2018_paper.html
    type: peer-reviewed
    accessed: 2026-11-18
  - id: s6
    title: "BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation"
    publisher: ICML 2022, PMLR 162 (Li, Li, Xiong, Hoi)
    url: https://proceedings.mlr.press/v162/li22n.html
    type: peer-reviewed
    accessed: 2026-11-18
created: 2026-11-18
---

# Image captioning

Image captioning is the task of producing a fluent natural-language description of what an image shows: the objects present, what they are doing and how they relate. It sits at the junction of computer vision and natural-language generation, because a system must both recognise visual content and express it as a grammatical sentence. The modern neural formulation was popularised by Google's "Show and Tell" model (Vinyals, Toshev, Bengio and Erhan, CVPR 2015), which treated captioning as translating an image into a sentence and trained a single network end to end to maximise the likelihood of a reference caption given the image.[^s1]

## How it works

The classic architecture is an encoder-decoder. A convolutional network encodes the image into a feature vector, and a recurrent language model decodes that vector one word at a time, each step conditioned on the image and the words generated so far. Training maximises the probability of human-written captions, i.e. it minimises the cross-entropy of each next word. At test time a search procedure such as beam search assembles the most probable sentence. Show and Tell borrowed this recipe directly from neural machine translation and reported large BLEU gains over earlier retrieval- and template-based systems; on the Pascal sentence dataset, for instance, its BLEU rose to 59 against a previous best of 25, with humans at about 69.[^s1]

Compressing the whole image into one vector loses spatial detail, so Xu and colleagues ("Show, Attend and Tell", 2015) added visual attention: at every decoding step the decoder computes weights over a grid of convolutional features and attends to the image region relevant to the next word. They trained one variant deterministically with ordinary backpropagation and another stochastically via a variational lower bound, and their visualisations showed attention shifting to salient objects as the matching words were produced.[^s2] Anderson et al. (CVPR 2018) moved attention from grid cells to objects: a Faster R-CNN detector proposes salient regions ("bottom-up"), and a caption-generating LSTM weighs those region features ("top-down"). The approach reached a CIDEr of 117.9, SPICE of 21.5 and BLEU-4 of 36.9 on the MS COCO test server and also won the 2017 VQA Challenge.[^s5]

## Data and evaluation

Progress has been organised around shared datasets, chiefly Flickr8k, Flickr30k and MS COCO.[^s2] The MS COCO Captions release collects five independent human captions for each training and validation image, targeting more than 1.5 million captions over 330,000+ images, and runs a central evaluation server so that systems are scored identically.[^s3] The server reports BLEU, METEOR, ROUGE and CIDEr.[^s3]

Automatic metrics are a known weak point. N-gram metrics borrowed from translation reward surface word overlap, so Vedantam, Zitnick and Parikh introduced CIDEr, which scores a candidate by how well it agrees with the consensus of many human descriptions of the same image; they built PASCAL-50S and ABSTRACT-50S with 50 sentences per image and found CIDEr tracked human consensus judgments better than earlier metrics.[^s4] The CIDEr authors' premise is that the yardstick should be human judgment, which is why they validated metrics against human annotations collected with a triplet-comparison protocol; a variant, CIDEr-D, was adopted by the MS COCO evaluation server.[^s4]

## Limitations and current practice

Likelihood training ties a captioner to the quantity and quality of its paired data, and curated caption datasets are small next to the web. Web-scale image-text pairs offer far more data but are noisy. BLIP (Li et al., ICML 2022) addressed this by bootstrapping: a captioner writes synthetic captions for web images and a filter removes poor ones, and the cleaned data improved captioning CIDEr by 2.8% while one pretrained model served both understanding tasks (retrieval, visual question answering) and generation tasks such as captioning, and even transferred zero-shot to video-language tasks.[^s6] This unification is the direction the field has taken: rather than a dedicated captioning network, captioning is increasingly one capability of general pretrained vision-language models, with COCO-style caption benchmarks still used to report results.[^s6][^s3]

## Connections

Image captioning is an application within **computer vision** (`kt:computer-vision`) and, unlike **image classification** (`kt:image-classification`), outputs an open-ended sentence rather than a label.[^s1] Its founding neural recipe is **sequence-to-sequence learning** (`kt:sequence-to-sequence-learning`) with a **recurrent neural network** (`kt:recurrent-neural-network`) decoder, introduced for images in **Show and Tell** (`kt:show-and-tell-a-neural-image-caption-generator`) and decoded with **beam search** (`kt:beam-search`).[^s1] The **attention mechanism** (`kt:attention-mechanism`) entered vision through captioning, from grid attention to Faster R-CNN region attention.[^s2][^s5] Systems are **evaluated on MS COCO** (`kt:ms-coco`) with **BLEU** (`kt:bleu`) and **CIDEr** (`kt:cider`).[^s3][^s4] Today the task is a standard capability of **vision-language models** (`kt:vision-language-model`).[^s6]

## Sources
[^s1]: Vinyals, Toshev, Bengio and Erhan, "Show and Tell: A Neural Image Caption Generator", CVPR 2015. https://openaccess.thecvf.com/content_cvpr_2015/html/Vinyals_Show_and_Tell_2015_CVPR_paper.html (accessed 2026-11-18)
[^s2]: Xu et al., "Show, Attend and Tell: Neural Image Caption Generation with Visual Attention", arXiv 1502.03044 (ICML 2015). https://arxiv.org/abs/1502.03044v3 (accessed 2026-11-18)
[^s3]: Chen et al., "Microsoft COCO Captions: Data Collection and Evaluation Server", arXiv 1504.00325, 2015. https://arxiv.org/abs/1504.00325 (accessed 2026-11-18)
[^s4]: Vedantam, Zitnick and Parikh, "CIDEr: Consensus-Based Image Description Evaluation", CVPR 2015. https://openaccess.thecvf.com/content_cvpr_2015/html/Vedantam_CIDEr_Consensus-Based_Image_2015_CVPR_paper.html (accessed 2026-11-18)
[^s5]: Anderson et al., "Bottom-Up and Top-Down Attention for Image Captioning and Visual Question Answering", CVPR 2018. https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Bottom-Up_and_Top-Down_CVPR_2018_paper.html (accessed 2026-11-18)
[^s6]: Li, Li, Xiong and Hoi, "BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation", ICML 2022, PMLR 162. https://proceedings.mlr.press/v162/li22n.html (accessed 2026-11-18)
