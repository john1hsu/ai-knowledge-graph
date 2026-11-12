---
id: kt:retrieval-augmented-generation
type: Technique
title: Retrieval-augmented generation for knowledge-intensive tasks
aliases: [retrieval-augmented generation, RAG, retrieval augmented generation, RAG-Sequence, RAG-Token]
domain: retrieval-and-knowledge
summary: >-
  A technique that couples a text generator with a retriever, so that documents fetched from an external
  corpus at inference time condition the model's output; the "parametric" knowledge in the model's weights
  is supplemented by "non-parametric" knowledge held in an updatable index.
maturity: established
broader: [kt:information-retrieval, kt:large-language-model]
related: [kt:semantic-search, kt:vector-database, kt:context-window, kt:reranking, kt:toolformer]
relations:
  - {predicate: introducedIn, object: kt:retrieval-augmented-generation-for-knowledge-intensive-nlp-tasks}
  - {predicate: influencedBy, object: kt:realm}
  - {predicate: dependsOn, object: kt:embeddings}
  - {predicate: dependsOn, object: kt:approximate-nearest-neighbor-search}
  - {predicate: mitigates, object: kt:hallucination}
  - {predicate: alternativeTo, object: kt:fine-tuning}
  - {predicate: implementedIn, object: kt:hugging-face-transformers}
sources:
  - id: s1
    title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
    publisher: Advances in Neural Information Processing Systems 33 (NeurIPS 2020), pp. 9459-9474 (Lewis, Perez, Piktus, Petroni, Karpukhin, Goyal, Küttler, Lewis, Yih, Rocktäschel, Riedel and Kiela)
    url: https://papers.nips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s2
    title: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (full text, arXiv:2005.11401)"
    publisher: Lewis et al., authors' arXiv paper, full text as mirrored on Hugging Face Papers
    url: https://huggingface.co/papers/2005.11401.md
    type: primary
    accessed: 2026-11-12
  - id: s3
    title: "Retrieval Augmented Language Model Pre-Training"
    publisher: Proceedings of the 37th ICML, PMLR 119:3929-3938, 2020 (Guu, Lee, Tung, Pasupat and Chang)
    url: https://proceedings.mlr.press/v119/guu20a.html
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "Retrieval-Augmented Generation for Large Language Models: A Survey"
    publisher: arXiv:2312.10997v2, 2024 (Gao, Xiong, Gao, Jia, Pan, Bi, Dai, Sun, Wang and Wang)
    url: https://arxiv.org/pdf/2312.10997v2.pdf
    type: preprint
    accessed: 2026-11-12
  - id: s5
    title: "Lost in the Middle: How Language Models Use Long Contexts"
    publisher: Transactions of the Association for Computational Linguistics 12, 157-173, 2024 (Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni and Liang)
    url: https://aclanthology.org/2024.tacl-1.9/
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s6
    title: "RAG"
    publisher: Hugging Face Transformers documentation
    url: https://huggingface.co/docs/transformers/en/model_doc/rag
    type: official-docs
    accessed: 2026-11-12
created: 2026-11-12
---

# Retrieval-augmented generation for knowledge-intensive tasks

**Retrieval-augmented generation (RAG)** is a technique in which a language model's output is conditioned not only on its input but also on documents retrieved from an external corpus at inference time. The name comes from a 2020 NeurIPS paper by Patrick Lewis and eleven co-authors, which framed the idea as combining a model's *parametric* memory (knowledge stored in its weights) with a *non-parametric* memory: a dense vector index of Wikipedia searched by a neural retriever.[^s1] The motivation was that large pretrained models trail task-specific systems on knowledge-intensive tasks, cannot easily show where an answer came from, and are hard to update when facts change.[^s1] Today "RAG" is used more loosely for any pipeline that retrieves context and inserts it into a large language model's prompt.[^s4]

## Origin

RAG built on retrieval-augmented pretraining. Guu et al.'s REALM (ICML 2020) added a latent knowledge retriever to masked-language-model pretraining, letting the model attend to Wikipedia documents during pretraining, fine-tuning and inference, and reported gains of 4–16 points of absolute accuracy on three open-domain question-answering benchmarks over prior methods.[^s3] REALM was an encoder that extracted answers; Lewis et al. extended the idea to a sequence-to-sequence *generator*, so retrieved evidence could inform free-form outputs.[^s1][^s2]

## How it works

In the original system the retriever is Dense Passage Retrieval (DPR), a bi-encoder that embeds the query and passages, and the generator is BART-large, a 400M-parameter seq2seq model.[^s2] Wikipedia was split into disjoint 100-word chunks, giving an index of about 21 million passages stored as dense vectors.[^s2] For an input *x*, the retriever returns the top-*k* passages *z* with probabilities p(z|x), and the generator produces output *y* conditioned on *x* and each passage. Two variants marginalise over the passages differently:[^s2]

- **RAG-Sequence** uses one passage for the whole answer: p(y|x) ≈ Σ_z p(z|x) · ∏_i p(y_i | x, z, y_<i).[^s2]
- **RAG-Token** can switch passages per token: p(y|x) ≈ ∏_i Σ_z p(z|x) · p(y_i | x, z, y_<i).[^s2]

The retrieved documents are treated as a latent variable to marginalise over; the paper retrieved *k* = 5 or 10 passages per query during training and tuned *k* for test time on development data.[^s2][^s2] After fine-tuning, RAG set state-of-the-art results on three open-domain QA tasks and, on generation tasks, produced text the authors judged more specific, diverse and factual than a parametric-only BART baseline.[^s1]

## Modern RAG pipelines

With instruction-following LLMs, most deployments drop joint training: a frozen model receives retrieved chunks pasted into its prompt. Gao et al.'s survey (2024) groups the evolution into three paradigms.[^s4] *Naive RAG* splits documents into chunks, embeds them into a vector index offline, embeds each query with the same model, retrieves the top-K most similar chunks and places them in the prompt.[^s4] *Advanced RAG* adds pre-retrieval steps (finer chunking, metadata filters, query rewriting or decomposition, mixed keyword and vector search) and post-retrieval steps (reranking, context compression).[^s4] *Modular RAG* replaces the fixed pipeline with interchangeable modules and flows such as iterative retrieval or adaptive retrieval that decides when to search.[^s4]

## Limitations and open questions

RAG is only as good as its retrieval: the Gao survey lists low retrieval precision and recall, outdated or redundant data, and hallucinated or irrelevant answers among naive RAG's weaknesses, and notes the added latency of a retrieval step.[^s4] Simply retrieving more passages is not a fix. Liu et al. (TACL 2024) found that models used information best when it sat at the start or end of a long context and performed noticeably worse when the relevant passage was in the middle, even for models built for long contexts.[^s5] Evaluating RAG systems therefore means scoring retrieval and generation separately; the survey highlights context relevance, answer faithfulness and answer relevance, plus robustness to noisy or counterfactual passages, and calls for better evaluation methods.[^s4] RAG reduces, but does not eliminate, hallucination: nothing in the architecture forces the generator to stay within the retrieved text.[^s1][^s4]

## In practice

The original models remain available in the Hugging Face Transformers library as `RagSequenceForGeneration` and `RagTokenForGeneration`, built from a question encoder, a `RagRetriever` over a DPR Wikipedia index, and a generator; by default five documents are retrieved and concatenated with the input before generation.[^s6] Production systems more often assemble RAG from a general-purpose LLM, an embedding model and a vector index.[^s4] Compared with fine-tuning, the survey credits RAG with easy knowledge updates and traceable answers, and credits fine-tuning with control over style and format and lower latency; the two are often combined.[^s4]

## Connections

RAG is a meeting point of **information retrieval** and **large language models**, its two broader fields.[^s1] It was introduced in the Lewis et al. paper and influenced by **REALM**.[^s3] Its retrieval stage depends on **embeddings** and **approximate nearest-neighbour search**, usually served from a **vector database** and often driven by **semantic search** plus a **reranking** step.[^s2][^s4] It is a common mitigation for **hallucination** and an alternative to **fine-tuning** for injecting domain knowledge.[^s4] Retrieved text competes for the **context window**, where position effects matter.[^s5] Tool-using models such as **Toolformer** generalise the idea by letting the model decide when to call a search tool. The reference implementation ships in **Hugging Face Transformers**.[^s6]

## Sources
[^s1]: Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", NeurIPS 2020. https://papers.nips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html (accessed 2026-11-12)
[^s2]: Lewis et al., full text of arXiv:2005.11401 (Hugging Face Papers mirror). https://huggingface.co/papers/2005.11401.md (accessed 2026-11-12)
[^s3]: Guu et al., "Retrieval Augmented Language Model Pre-Training", ICML 2020, PMLR 119. https://proceedings.mlr.press/v119/guu20a.html (accessed 2026-11-12)
[^s4]: Gao et al., "Retrieval-Augmented Generation for Large Language Models: A Survey", arXiv:2312.10997v2, 2024. https://arxiv.org/pdf/2312.10997v2.pdf (accessed 2026-11-12)
[^s5]: Liu et al., "Lost in the Middle: How Language Models Use Long Contexts", TACL 12, 2024. https://aclanthology.org/2024.tacl-1.9/ (accessed 2026-11-12)
[^s6]: Hugging Face, "RAG", Transformers documentation. https://huggingface.co/docs/transformers/en/model_doc/rag (accessed 2026-11-12)
