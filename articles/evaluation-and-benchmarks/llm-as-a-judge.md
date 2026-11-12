---
id: kt:llm-as-a-judge
type: Technique
title: LLM-as-a-judge
aliases: [LLM judge, model-based evaluation, LLM-based evaluator, LLM evaluator, model-graded evaluation]
domain: evaluation-and-benchmarks
summary: >-
  An evaluation technique in which a strong large language model is prompted, or fine-tuned, to grade or
  compare the outputs of other models, serving as a scalable approximation of human judgment for open-ended
  tasks.
maturity: established
broader: [kt:ai-evaluation]
related: [kt:human-evaluation, kt:sycophancy, kt:reward-hacking, kt:self-refine-iterative-refinement-with-self-feedback, kt:rlhf]
relations:
  - {predicate: introducedIn, object: kt:judging-llm-as-a-judge-with-mt-bench-and-chatbot-arena}
  - {predicate: basedOn, object: kt:large-language-model}
  - {predicate: usedIn, object: kt:chatbot-arena}
  - {predicate: usedIn, object: kt:mt-bench}
  - {predicate: dependsOn, object: kt:chain-of-thought}
sources:
  - id: s1
    title: "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"
    publisher: arXiv 2306.05685, NeurIPS 2023 Datasets and Benchmarks Track (Zheng, Chiang, Sheng et al.)
    url: https://arxiv.org/abs/2306.05685
    type: primary
    accessed: 2026-11-12
  - id: s2
    title: "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment"
    publisher: Proceedings of EMNLP 2023, pp. 2511–2522 (Liu, Iter, Xu, Wang, Xu, Zhu)
    url: https://aclanthology.org/2023.emnlp-main.153
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s3
    title: "Large Language Models are not Fair Evaluators"
    publisher: "Proceedings of ACL 2024 (Volume 1: Long Papers), pp. 9440–9450 (Wang, Li, Chen et al.)"
    url: https://aclanthology.org/2024.acl-long.511
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s4
    title: "Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models"
    publisher: ICLR 2024 (Kim, Seo et al.), via ML Anthology
    url: https://mlanthology.org/iclr/2024/kim2024iclr-prometheus
    type: peer-reviewed
    accessed: 2026-11-12
  - id: s5
    title: "LLM Evaluators Recognize and Favor Their Own Generations"
    publisher: NeurIPS 2024 Main Conference Track (Panickssery, Bowman, Feng)
    url: https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html
    type: peer-reviewed
    accessed: 2026-11-12
created: 2026-11-12
---

# LLM-as-a-judge

**LLM-as-a-judge** is the practice of using a capable large language model as the grader in an evaluation: it reads a question together with one or more candidate answers and returns a verdict, a score, or a written critique. The approach targets open-ended outputs such as chat replies, summaries and essays, where fixed-answer benchmarks and string-overlap metrics capture little of what people care about and human rating is slow and expensive.[^s1][^s2] The term was popularised by Zheng et al. (submitted June 2023, published at the NeurIPS 2023 Datasets and Benchmarks Track), who used GPT-4 to judge chat assistants and introduced the MT-Bench question set and the crowdsourced Chatbot Arena alongside it.[^s1]

## How it works

Zheng et al. describe three variants.[^s1]

- **Pairwise comparison**: the judge sees a question and two answers and picks a winner or a tie; pair counts grow quadratically with the number of models.[^s1]
- **Single-answer grading**: the judge assigns one answer an absolute score (1–10 in their setup); cheaper, but it can miss small differences and drift when the judge changes.[^s1]
- **Reference-guided grading**: the judge is given a reference solution, which the authors used mainly for maths questions.[^s1]

The prompt usually spells out the criteria, and the judge is often asked to reason before scoring. G-Eval (Liu et al., EMNLP 2023) combines chain-of-thought prompting with a form-filling template, so the model first generates evaluation steps and then fills in scores for criteria such as coherence or fluency. With GPT-4 as the backbone it reached a Spearman correlation of 0.514 with human ratings on a summarisation benchmark, well above earlier automatic metrics.[^s2] A judge can also be a smaller open model fine-tuned for the job. Prometheus (Kim et al., ICLR 2024) is a 13B model trained on about 100K GPT-4-written feedback examples covering roughly 1K score rubrics; given a rubric and a reference answer, it matched GPT-4's correlation with human raters in the authors' tests (Pearson 0.897 versus 0.882).[^s4]

## Evidence of reliability

The headline result of Zheng et al. is that GPT-4 agreed with human preferences more than 80% of the time on both expert and crowdsourced votes. On non-tied MT-Bench votes, GPT-4 agreed with human experts 85% of the time, while experts agreed with one another 81% of the time.[^s1] MT-Bench itself contains 80 multi-turn questions, ten in each of eight categories including writing, reasoning, maths and coding, and the released data includes about 3K expert votes and 30K Chatbot Arena conversations.[^s1] Agreement rises as the quality gap between the two models grows, so judges are most trustworthy at separating clearly different systems.[^s1] Judges also explain their verdicts, which makes errors easier to audit than a bare metric.[^s1]

## Biases and limitations

- **Position bias**: in Zheng et al.'s tests, GPT-4 gave the same verdict after the two answers were swapped only 65.0% of the time; GPT-3.5 managed 46.2% and Claude-v1 23.8%.[^s1]
- Wang et al. (ACL 2024) showed that order alone could flip rankings: with ChatGPT as judge, Vicuna-13B beat ChatGPT on 66 of 80 queries depending on answer order.[^s3]
- **Verbosity bias**: padding an answer with restated list items fooled Claude-v1 and GPT-3.5 in 91.3% of test cases, compared with 8.7% for GPT-4.[^s1]
- **Self-preference**: Panickssery et al. (NeurIPS 2024) found that models such as GPT-4 and Llama 2 can recognise their own text and rate it above equally good outputs from others, with evidence that recognition partly causes the preference.[^s5]
- **Weak grading of reasoning**: GPT-4 could solve maths questions on its own yet was misled by wrong answers it was asked to grade.[^s1]

G-Eval's authors likewise flag a risk that LLM evaluators favour LLM-generated text, which matters when the judged systems are themselves models.[^s2] Wang et al. note that such order effects let evaluation results be skewed without any change to the answers themselves.[^s3]

## Mitigations and practice

Standard countermeasures include scoring both answer orders and counting a win only when the verdict is consistent, few-shot examples (which raised GPT-4's consistency from 65.0% to 77.5% at roughly four times the prompt cost), and reference answers for maths, which cut GPT-4's grading failures from 14 of 20 to 3 of 20 in Zheng et al.'s experiments.[^s1] Wang et al. propose a simple calibration framework for position bias, validated against their own human win/tie/lose annotations, and report that it brings judge verdicts closer to human labels.[^s3] Taken together, these results support using LLM judges as a fast, cheap first pass that is checked against a sample of human ratings rather than as a full replacement for human evaluation.[^s1][^s3] The self-preference finding is also a reason not to let a model grade its own outputs.[^s5]

## Connections

LLM-as-a-judge is a method within the broader field of **AI evaluation**, introduced in its modern form by the **MT-Bench and Chatbot Arena paper** and used to score **MT-Bench** and to analyse **Chatbot Arena** votes.[^s1] It is **based on** a **large language model** and depends on **chain-of-thought** style reasoning in recipes such as G-Eval.[^s2] Its validity is always measured against **human evaluation**.[^s1] Its self-preference bias resembles **sycophancy**, a model tilting judgments toward what pleases rather than what is correct, and a policy optimised against a biased judge invites **reward hacking**.[^s5][^s3] The same judge-model idea powers AI feedback in **RLHF**-style pipelines and critique loops such as **Self-Refine**, which Panickssery et al. name as settings that self-preference can distort.[^s5]

## Sources

[^s1]: Zheng, Chiang, Sheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", arXiv 2306.05685 (NeurIPS 2023 Datasets and Benchmarks Track). https://arxiv.org/abs/2306.05685 (accessed 2026-11-12)
[^s2]: Liu, Iter, Xu, Wang, Xu, Zhu, "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment", EMNLP 2023. https://aclanthology.org/2023.emnlp-main.153 (accessed 2026-11-12)
[^s3]: Wang, Li, Chen et al., "Large Language Models are not Fair Evaluators", ACL 2024. https://aclanthology.org/2024.acl-long.511 (accessed 2026-11-12)
[^s4]: Kim et al., "Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models", ICLR 2024. https://mlanthology.org/iclr/2024/kim2024iclr-prometheus (accessed 2026-11-12)
[^s5]: Panickssery, Bowman, Feng, "LLM Evaluators Recognize and Favor Their Own Generations", NeurIPS 2024. https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html (accessed 2026-11-12)
