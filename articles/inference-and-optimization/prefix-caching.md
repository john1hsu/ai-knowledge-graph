---
id: kt:prefix-caching
type: Technique
title: Prefix caching
aliases: [prompt caching, automatic prefix caching, KV cache reuse, RadixAttention]
domain: inference-and-optimization
summary: >-
  An LLM inference optimization that keeps the key-value (KV) cache computed for a prompt prefix after a request
  finishes and reuses it for later requests that begin with the identical token sequence, so the shared prefix is not
  recomputed during prefill.
maturity: established
broader: [kt:llm-inference-optimization]
related: [kt:batching-and-paged-attention, kt:retrieval-augmented-generation, kt:ai-agent, kt:chatbot-arena]
relations:
  - {predicate: dependsOn, object: kt:kv-cache}
  - {predicate: implementedIn, object: kt:vllm}
  - {predicate: implementedIn, object: kt:sglang}
  - {predicate: introducedIn, object: kt:sglang-efficient-execution-of-structured-language-model-programs}
  - {predicate: causes, object: kt:timing-side-channel}
sources:
  - id: s1
    title: "SGLang: Efficient Execution of Structured Language Model Programs"
    publisher: Zheng et al., NeurIPS 2024 (proceedings)
    url: https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf
    type: peer-reviewed
    accessed: 2026-11-17
  - id: s2
    title: "Automatic Prefix Caching (design document)"
    publisher: vLLM documentation
    url: https://docs.vllm.ai/design/prefix_caching.html
    type: official-docs
    accessed: 2026-11-17
  - id: s3
    title: "Prompt Cache: Modular Attention Reuse for Low-Latency Inference"
    publisher: Gim et al., arXiv 2311.04934 (v2, 2024)
    url: https://arxiv.org/abs/2311.04934
    type: primary
    accessed: 2026-11-17
  - id: s4
    title: "Prompt caching"
    publisher: Anthropic, Claude Platform documentation
    url: https://platform.claude.com/en/docs/build-with-claude/prompt-caching
    type: official-docs
    accessed: 2026-11-17
  - id: s5
    title: "Auditing Prompt Caching in Language Model APIs"
    publisher: Gu et al., ICML 2025, PMLR 267
    url: https://proceedings.mlr.press/v267/gu25b.html
    type: peer-reviewed
    accessed: 2026-11-17
created: 2026-11-17
---

# Prefix caching

**Prefix caching** (often called **prompt caching** when exposed by an API) is the practice of keeping the attention keys and values that an LLM computed for a prompt and reusing them when a later request starts with exactly the same tokens. Ordinary serving engines throw a request's KV cache away when the request finishes; prefix caching instead retains it so that a repeated system prompt, few-shot template, long document or earlier chat history skips the prefill computation the next time it appears.[^s1] Because keys and values at a position depend only on the tokens up to that position, any request sharing a token-identical prefix can safely reuse the stored state, and the model's output is unchanged.[^s4]

## Origin

The idea grew out of KV-cache memory management. Gim et al.'s *Prompt Cache* (arXiv, first posted November 2023) reused attention states for text segments that recur across prompts, using an explicit schema of reusable "prompt modules," and reported time-to-first-token reductions from about 8× on GPUs to 60× on CPUs, largest for long prompts.[^s3] Because it also reuses non-prefix segments, the SGLang authors note it can cost up to 43% in accuracy.[^s1] Zheng et al.'s **SGLang** paper (NeurIPS 2024) introduced **RadixAttention**, making automatic, multi-level prefix reuse a general runtime feature, whereas earlier engines such as vLLM handled only simple cases like a shared system prompt.[^s1]

## How it works

RadixAttention stores cached prefixes in a **radix tree**, a compressed prefix tree whose edges carry token sequences, mapping each sequence to its KV tensors held in a paged, non-contiguous GPU layout.[^s1] A new request walks the tree to find its longest cached prefix, computes only the remaining tokens, and inserts its own result. Each node carries a reference count of running requests; when memory runs short the least recently used *leaf* is evicted first, so shared ancestors survive as long as any descendant is useful. Cached and running tokens share one memory pool, letting the system drop the whole cache when a large batch needs room.[^s1] The scheduler sorts waiting requests by matched prefix length, which the authors prove is equivalent to a depth-first traversal of the tree and optimal for an offline batch; they also note this greedy order can starve some requests.[^s1]

vLLM's **automatic prefix caching** uses hashing rather than an explicit tree. Each full KV block is identified by a hash of its parent block's hash, its own token ids and "extra" keys such as LoRA adapter ids, multimodal input hashes and an optional per-request cache salt; only full blocks are cached, and free blocks are evicted in LRU order, with a request's last block evicted first because it is least likely to be shared.[^s2] Chaining the parent hash means a block can only match when every earlier token matches too, which encodes the strict-prefix requirement.[^s2]

Hosted APIs expose the same mechanism as a billing feature. In Anthropic's API, as of November 2026, the cached prefix is built in the order tools, system prompt, then messages, so changing an earlier part invalidates everything after it. Callers mark up to four breakpoints or enable automatic placement. Entries live five minutes by default, refreshed on each hit, or one hour at extra cost. Cache writes are billed at 1.25× (5-minute) or 2× (1-hour) the base input price and reads at a fraction of it, typically 0.1×. Models have a minimum cacheable length, for example 512 tokens on the newest models and 4,096 on some older ones.[^s4]

## Evidence and limitations

The SGLang authors measured cache hit rates of roughly 50%–99% across their benchmarks, reported that cache-aware scheduling reached about 96% of the optimal hit rate on average, and observed hit rates of 52.4% (LLaVA-NeXT-34B) and 74.1% (Vicuna-33B) over a month of serving on Chatbot Arena; they report up to 6.4× higher throughput for SGLang overall, a figure that combines several optimizations.[^s1] Tree upkeep took under 0.3% of runtime on a ShareGPT workload with no reuse.[^s1]

Reuse only pays off when prefixes are byte-for-byte identical, so prompt layout matters: putting a timestamp or per-user detail early in a prompt defeats the cache.[^s4] Retained cache also competes with running requests for GPU memory.[^s1] The largest open issue is privacy. A cache hit returns faster, which is a **timing side channel**: Gu et al. (ICML 2025) built statistical audits and detected caches shared globally across users at seven API providers, including OpenAI, and used the same signal to infer that OpenAI's embedding model is a decoder-only transformer.[^s5] Mitigations include per-organization or per-workspace isolation, which Anthropic documents, and vLLM's cache salt; vLLM also warns that fast non-cryptographic block hashes raise collision risk that could leak data across tenants.[^s4][^s2]

## In practice

Prefix caching is built into major open-source engines: vLLM's V1 engine implements the hash-based block cache described above, and the SGLang runtime is built around RadixAttention.[^s2][^s1] It is most valuable for workloads with heavy repetition, including multi-turn chat, agents that resend long tool definitions and histories every step, few-shot prompting, and retrieval-augmented generation over the same documents.[^s1][^s4]

## Connections

Prefix caching **depends on** the **KV cache**, which it keeps alive across requests, under **LLM inference optimization**.[^s1] It builds on the paged blocks of **batching and PagedAttention** and is **implemented in** **vLLM** and **SGLang**, whose NeurIPS 2024 paper **introduced** RadixAttention.[^s2][^s1] It helps **AI agents** and **retrieval-augmented generation**, and was measured on **Chatbot Arena**.[^s1] Shared caches **cause** a **timing side channel**, hence tenant isolation.[^s5][^s4]

## Sources

[^s1]: L. Zheng et al., "SGLang: Efficient Execution of Structured Language Model Programs", NeurIPS 2024. https://proceedings.neurips.cc/paper_files/paper/2024/file/724be4472168f31ba1c9ac630f15dec8-Paper-Conference.pdf (accessed 2026-11-17)
[^s2]: vLLM, "Automatic Prefix Caching" (design document). https://docs.vllm.ai/design/prefix_caching.html (accessed 2026-11-17)
[^s3]: I. Gim et al., "Prompt Cache: Modular Attention Reuse for Low-Latency Inference", arXiv 2311.04934. https://arxiv.org/abs/2311.04934 (accessed 2026-11-17)
[^s4]: Anthropic, "Prompt caching" (Claude Platform documentation). https://platform.claude.com/en/docs/build-with-claude/prompt-caching (accessed 2026-11-17)
[^s5]: C. Gu, X. L. Li, R. Kuditipudi, P. Liang, T. Hashimoto, "Auditing Prompt Caching in Language Model APIs", ICML 2025, PMLR 267. https://proceedings.mlr.press/v267/gu25b.html (accessed 2026-11-17)
