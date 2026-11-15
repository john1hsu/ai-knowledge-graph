---
id: kt:latent-diffusion-model
type: Architecture
title: Latent diffusion model
aliases: [LDM, latent diffusion]
domain: computer-vision-and-multimodal
summary: >-
  A diffusion model that runs its noising and denoising process in the compressed latent space of a
  pretrained autoencoder rather than on raw pixels, with cross-attention layers for conditioning on text
  or other inputs; it is the architecture behind Stable Diffusion.
maturity: established
broader: [kt:diffusion-model, kt:generative-model]
related: [kt:variational-autoencoder, kt:clip, kt:attention-mechanism]
relations:
  - {predicate: introducedIn, object: kt:high-resolution-image-synthesis-with-latent-diffusion-models}
  - {predicate: extends, object: kt:diffusion-model}
  - {predicate: basedOn, object: kt:u-net}
  - {predicate: usedIn, object: kt:text-to-image-generation}
  - {predicate: implementedIn, object: kt:hugging-face-diffusers}
  - {predicate: alternativeTo, object: kt:generative-adversarial-network}
sources:
  - id: s1
    title: "High-Resolution Image Synthesis With Latent Diffusion Models"
    publisher: Rombach, Blattmann, Lorenz, Esser and Ommer, Proceedings of IEEE/CVF CVPR 2022, pp. 10684–10695
    url: https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s2
    title: "High-Resolution Image Synthesis with Latent Diffusion Models (arXiv:2112.10752v2)"
    publisher: Rombach et al., authors' arXiv version (v1 December 2021, v2 April 2022)
    url: https://arxiv.org/pdf/2112.10752
    type: primary
    accessed: 2026-11-15
  - id: s3
    title: "Text-to-image (Stable Diffusion pipeline)"
    publisher: Hugging Face Diffusers documentation
    url: https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/text2img
    type: official-docs
    accessed: 2026-11-15
  - id: s4
    title: "Revolutionizing image generation by AI: Turning text into images"
    publisher: LMU Munich newsroom (1 September 2022)
    url: https://lmu.de/en/newsroom/news-overview/news/revolutionizing-image-generation-by-ai-turning-text-into-images.html
    type: academic
    accessed: 2026-11-15
  - id: s5
    title: "SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis"
    publisher: Podell et al., ICLR 2024
    url: https://proceedings.iclr.cc/paper_files/paper/2024/hash/081b08068e4733ae3e7ad019fe8d172f-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-15
  - id: s6
    title: "Scalable Diffusion Models with Transformers"
    publisher: Peebles and Xie, ICCV 2023 (CVF open access)
    url: https://openaccess.thecvf.com/content/ICCV2023/papers/Peebles_Scalable_Diffusion_Models_with_Transformers_ICCV_2023_paper.pdf
    type: peer-reviewed
    accessed: 2026-11-15
created: 2026-11-15
---

# Latent diffusion model

A latent diffusion model (LDM) is a diffusion model that does its iterative denoising not on image pixels but on a much smaller latent representation produced by a pretrained autoencoder. The idea was introduced by Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser and Björn Ommer in "High-Resolution Image Synthesis with Latent Diffusion Models", posted to arXiv in December 2021 and published at CVPR 2022.[^s1][^s2] Its motivation was cost: pixel-space diffusion models produced excellent images but, the authors noted, often needed hundreds of GPU-days to train and were expensive to sample from. Moving the process into a compressed space cut those requirements substantially while keeping image quality competitive.[^s1]

## How it works

Training happens in two separate stages.[^s2] First, an autoencoder is trained to map an image *x* to a latent *z = E(x)* and back to *D(z)*, using a perceptual loss plus a patch-based adversarial loss so reconstructions stay sharp. The latent is regularized either with a light KL penalty toward a standard normal (as in a variational autoencoder) or with a vector-quantization layer. The image is downsampled spatially by a factor *f*; the paper tested *f* from 1 to 32 and found that *f* = 4 and *f* = 8 gave the best trade-off, while *f* = 1 trained slowly and *f* = 32 lost too much detail.[^s2]

Second, a time-conditional U-Net denoiser ε_θ is trained on those latents with the standard noise-prediction objective, minimizing the expected squared error ‖ε − ε_θ(z_t, t)‖² between the true noise and the predicted noise at each step *t*.[^s2] Because the autoencoder is frozen and shared, the expensive perceptual compression is learned once and reused, and the diffusion model can focus on the semantic structure of the data.[^s2]

Conditioning is added through cross-attention. A domain-specific encoder τ_θ turns the conditioning signal *y* (a caption, a class label, a semantic map) into a sequence of embeddings; inside the U-Net, queries come from the image features and keys and values come from τ_θ(y), combined as softmax(QKᵀ/√d)·V.[^s2] This lets one architecture handle text-to-image generation, layout-to-image synthesis, inpainting and super-resolution.[^s1]

## Evidence and limitations

The original paper reported state-of-the-art inpainting and strong results across tasks, for example an FID of 3.60 on class-conditional ImageNet 256×256 with classifier-free guidance (LDM-4-G), and a 1.45-billion-parameter text-to-image model trained on LAION-400M that reached an FID of 12.63 on MS-COCO with guidance.[^s2] The authors also listed weaknesses: sampling is still sequential and slower than a GAN's single forward pass, and the autoencoder's reconstruction ceiling can limit tasks that demand exact pixel-level accuracy.[^s2] They flagged societal risks too, including deepfakes and misinformation, possible leakage of sensitive training data, and reproduction of dataset biases.[^s2]

## In practice

Stable Diffusion, released in 2022, is a latent diffusion model. It was developed by Ommer's Machine Vision & Learning Group at LMU Munich with Stability AI, which trained it on its servers, and it was released openly under the CreativeML Open RAIL-M license.[^s4] The Hugging Face Diffusers documentation credits CompVis, Stability AI, Runway and LAION, and describes the v1 model as an 860M-parameter U-Net with a frozen 123M-parameter CLIP ViT-L/14 text encoder, trained on 512×512 images from a LAION-5B subset, small enough to run on consumer GPUs.[^s3] The Diffusers `StableDiffusionPipeline` exposes the architecture directly as separate components: a KL autoencoder (`vae`), a CLIP text encoder and tokenizer, a conditional U-Net and a swappable noise scheduler.[^s3]

Later systems kept the latent space but changed the denoiser. SDXL (ICLR 2024) used a U-Net roughly three times larger, a second text encoder, multi-aspect-ratio training and a separate refinement model, and its authors reported it as competitive with closed generators such as Midjourney.[^s5] Diffusion Transformers (DiT, ICCV 2023) replaced the U-Net with a transformer operating on patches of the Stable Diffusion VAE's latent (a 256×256 image becomes a 32×32×4 latent) and reported an ImageNet 256×256 FID of 2.27, improving on LDM's 3.60.[^s6]

## Connections

A latent diffusion model **extends** the general **diffusion model** by relocating it to a learned latent space, and sits under the broader family of generative models.[^s1] Its first stage is closely **related** to the **variational autoencoder**, whose KL regularization it borrows.[^s2] The denoiser is **based on** the U-Net, and its conditioning relies on the cross-attention form of the **attention mechanism**.[^s2] In Stable Diffusion the text encoder is **CLIP**, which ties LDMs to vision–language pretraining, and the model is **used in** text-to-image generation and **implemented in** Hugging Face Diffusers.[^s3] It is an **alternative to** the **generative adversarial network**, trading slower iterative sampling for more stable training and broader conditioning.[^s2] DiT shows the latent-space idea outliving the original U-Net backbone.[^s6]

## Sources
[^s1]: Rombach, Blattmann, Lorenz, Esser and Ommer, "High-Resolution Image Synthesis With Latent Diffusion Models", CVPR 2022, pp. 10684–10695. https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html (accessed 2026-11-15)
[^s2]: Rombach et al., "High-Resolution Image Synthesis with Latent Diffusion Models", arXiv:2112.10752v2. https://arxiv.org/pdf/2112.10752 (accessed 2026-11-15)
[^s3]: Hugging Face, "Text-to-image" (Stable Diffusion pipeline), Diffusers documentation. https://huggingface.co/docs/diffusers/api/pipelines/stable_diffusion/text2img (accessed 2026-11-15)
[^s4]: LMU Munich, "Revolutionizing image generation by AI: Turning text into images", 1 September 2022. https://lmu.de/en/newsroom/news-overview/news/revolutionizing-image-generation-by-ai-turning-text-into-images.html (accessed 2026-11-15)
[^s5]: Podell et al., "SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis", ICLR 2024. https://proceedings.iclr.cc/paper_files/paper/2024/hash/081b08068e4733ae3e7ad019fe8d172f-Abstract-Conference.html (accessed 2026-11-15)
[^s6]: Peebles and Xie, "Scalable Diffusion Models with Transformers", ICCV 2023. https://openaccess.thecvf.com/content/ICCV2023/papers/Peebles_Scalable_Diffusion_Models_with_Transformers_ICCV_2023_paper.pdf (accessed 2026-11-15)
