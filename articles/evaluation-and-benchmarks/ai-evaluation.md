---
id: kt:ai-evaluation
type: Field
title: Evaluation of AI systems
aliases: [AI evaluation, model evaluation, LLM evaluation, evals, AI testing and evaluation]
domain: evaluation-and-benchmarks
summary: >-
  The practice and research field of measuring what an AI model or system can do, how reliably and safely it
  does it, and how well those measurements predict behaviour in real use, through benchmarks, human and
  model-based judgments, red teaming and field testing.
maturity: established
broader: [kt:machine-learning]
related: [kt:llm-as-a-judge, kt:benchmark-contamination, kt:red-teaming, kt:mmlu]
relations:
  - {predicate: regulatedBy, object: kt:nist-ai-risk-management-framework}
  - {predicate: implementedIn, object: kt:inspect-ai}
  - {predicate: influencedBy, object: kt:turing-test}
sources:
  - id: s1
    title: "Holistic Evaluation of Language Models"
    publisher: Transactions on Machine Learning Research, 2023 (Liang, Bommasani, Lee et al.)
    url: https://mlanthology.org/tmlr/2023/liang2023tmlr-holistic
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s2
    title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
    publisher: NeurIPS 2023 Datasets and Benchmarks Track (Zheng et al.)
    url: https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract.html
    type: peer-reviewed
    accessed: 2026-10-31
  - id: s3
    title: "The TEVV-Athlon Framework for Evaluating AI Systems (NIST AI 200-2, initial public draft)"
    publisher: National Institute of Standards and Technology, August 2026
    url: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.200-2.ipd.pdf
    type: government
    accessed: 2026-10-31
  - id: s4
    title: "Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1"
    publisher: National Institute of Standards and Technology (Tabassi), January 2023
    url: https://www.nist.gov/node/1731741
    type: government
    accessed: 2026-10-31
  - id: s5
    title: "AI Benchmarks Hit Saturation"
    publisher: Stanford HAI (Shana Lynch, on the 2023 AI Index), 3 April 2023
    url: https://hai.stanford.edu/news/ai-benchmarks-hit-saturation
    type: academic
    accessed: 2026-10-31
  - id: s6
    title: "Inspect: an open-source framework for large language model evaluations"
    publisher: OECD.AI Catalogue of Tools & Metrics for Trustworthy AI (tool by UK AI Security Institute)
    url: https://oecd.ai/en/catalogue/tools/inspect
    type: intergovernmental
    accessed: 2026-10-31
created: 2026-10-31
---

# Evaluation of AI systems

**Evaluation of AI systems** ("AI evaluation", or "evals" in practitioner shorthand) is the work of measuring an AI model's or system's capabilities, limitations and risks, and of checking whether those measurements say anything trustworthy about how it will behave once deployed.[^s1][^s3] In government and standards language the same activity is called test, evaluation, verification and validation (TEVV). NIST's draft TEVV-Athlon framework (NIST AI 200-2, initial public draft, August 2026) presents itself as an implementation of the Measure function of the AI Risk Management Framework.[^s3][^s4] The field covers static benchmarks, human and model-based preference judgments, adversarial red teaming, user studies and field tests, and the methodology for designing and interpreting all of these.[^s2][^s3]

## From single benchmarks to holistic evaluation

For most of machine learning's history, evaluation meant reporting accuracy on a fixed held-out test set, such as ImageNet for vision. That approach worked until top systems pressed against the ceiling. Stanford HAI's coverage of the 2023 AI Index reported that many technical benchmarks had plateaued at roughly 80–90% accuracy. ImageNet's best result moved by only 0.1 percentage points between 2021 and 2022, and the top Visual Question Answering model (84.3%) had passed the roughly 80% human baseline.[^s5] The same report argued that high scores did not mean systems worked the way people needed, and called for broader benchmarks that capture trade-offs such as accuracy against bias or toxicity.[^s5]

The Holistic Evaluation of Language Models (HELM) project from Stanford's Center for Research on Foundation Models is the best-known response. Published in TMLR in 2023, HELM ran 30 prominent language models through 42 scenarios. On 16 core scenarios it measured seven metrics: accuracy, calibration, robustness, fairness, bias, toxicity and efficiency.[^s1] The authors found that before HELM, models had on average been evaluated on only 17.9% of these core scenarios, so published numbers were often not comparable. Standardising prompts and conditions raised that coverage to 96.0%.[^s1] HELM's lessons were to measure several properties at once, to evaluate every model under the same conditions, and to release raw prompts and completions so others can audit the results.[^s1]

## Main methods

- **Automated benchmarks** score outputs against reference answers or tests. They are cheap and repeatable, but they often measure a proxy instead of the real-world outcome of interest.[^s3]
- **Human preference evaluation** asks people to compare or rate outputs. It reflects open-ended quality better but costs more and is noisier.[^s2]
- **LLM-as-a-judge** uses a strong model to grade outputs. Zheng et al. (NeurIPS 2023) found that GPT-4 as a judge agreed with human preferences more than 80% of the time, about the same rate at which humans agree with one another. They also documented position, verbosity and self-enhancement biases in model judges.[^s2]
- **Red teaming, user testing and field testing** look for failures that a fixed test set cannot anticipate. NIST's draft treats them as necessary complements to model-level testing.[^s3]
- **Agentic evaluation** gives the system tools and a sandbox and scores whether it completes multi-step tasks. The UK AI Security Institute's open-source Inspect framework (MIT-licensed) supports this kind of evaluation with built-in tool calling, sandboxed code execution and agent primitives.[^s6]

## Validity and known pitfalls

NIST's draft says measurement validation should be ongoing, not a one-time sign-off: evaluators should keep asking whether a test captures the intended construct, whether results generalise, and whether they track real outcomes.[^s3] It names recurring threats: contamination, where test items leak into training data and inflate scores; Goodhart's law, where a metric that becomes an optimisation target stops tracking the property it stood for; and hidden variance, which calls for multiple trials, appropriate baselines and explicit reporting of uncertainty and limitations.[^s3] LLM judges add their own systematic biases, so their scores need checking against human labels.[^s2] Saturated benchmarks stop separating strong systems from one another, which leads to a steady cycle of retiring old test sets and building harder ones.[^s5]

## In practice

Model developers publish benchmark tables in technical reports and system cards. Deployers build application-specific test suites, which NIST's draft recommends partly as a defence against contamination of public benchmarks.[^s3] Governments use pre-deployment evaluations of frontier models, and the UK AI Security Institute released Inspect so that evaluations can be shared and reproduced.[^s6] Within the NIST AI RMF, evaluation sits in the Measure function. The Govern and Map functions set the goals of testing, and the results feed risk decisions in Manage.[^s3][^s4]

## Connections

Evaluation is a subfield of **machine learning**, since every learned model needs a held-out measure of how well it generalises.[^s1] **LLM-as-a-judge** is one of its methods, with documented biases, and **benchmark contamination** is one of its main threats to validity, while **red teaming** supplies the adversarial, open-ended side of testing.[^s2][^s3] It is governed by the **NIST AI Risk Management Framework**, whose Measure function TEVV implements, and implemented in tools such as **Inspect**.[^s3][^s4][^s6] Historically it is influenced by the **Turing test**, an early proposal to judge machine intelligence by observable behaviour.

## Sources
[^s1]: Liang, Bommasani, Lee et al., "Holistic Evaluation of Language Models", TMLR 2023. https://mlanthology.org/tmlr/2023/liang2023tmlr-holistic (accessed 2026-10-31)
[^s2]: Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", NeurIPS 2023 Datasets and Benchmarks Track. https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract.html (accessed 2026-10-31)
[^s3]: NIST, "The TEVV-Athlon Framework for Evaluating AI Systems", NIST AI 200-2 initial public draft, August 2026. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.200-2.ipd.pdf (accessed 2026-10-31)
[^s4]: NIST, "Artificial Intelligence Risk Management Framework (AI RMF 1.0)", NIST AI 100-1, January 2023. https://www.nist.gov/node/1731741 (accessed 2026-10-31)
[^s5]: Stanford HAI, "AI Benchmarks Hit Saturation", 3 April 2023. https://hai.stanford.edu/news/ai-benchmarks-hit-saturation (accessed 2026-10-31)
[^s6]: OECD.AI Catalogue of Tools & Metrics, "Inspect" (UK AI Security Institute). https://oecd.ai/en/catalogue/tools/inspect (accessed 2026-10-31)
