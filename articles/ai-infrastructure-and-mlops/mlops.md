---
id: kt:mlops
type: Paradigm
title: MLOps
aliases: [machine learning operations, ML operations]
domain: ai-infrastructure-and-mlops
summary: >-
  An engineering paradigm and culture that applies DevOps and data-engineering practice to machine learning,
  automating and monitoring the full lifecycle of ML products, from data and training pipelines through
  deployment, serving and continuous retraining.
maturity: established
broader: [kt:devops, kt:machine-learning]
related: [kt:llmops, kt:model-serving, kt:distributed-training, kt:ai-evaluation]
relations:
  - {predicate: influencedBy, object: kt:hidden-technical-debt-in-machine-learning-systems}
  - {predicate: hasPart, object: kt:feature-store}
  - {predicate: hasPart, object: kt:model-registry}
  - {predicate: mitigates, object: kt:data-drift}
  - {predicate: implementedIn, object: kt:mlflow}
sources:
  - id: s1
    title: "Hidden Technical Debt in Machine Learning Systems"
    publisher: NeurIPS 2015 (Sculley et al., Google)
    url: https://proceedings.neurips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf
    type: peer-reviewed
    accessed: 2026-10-30
  - id: s2
    title: "Machine Learning Operations (MLOps): Overview, Definition, and Architecture"
    publisher: IEEE Access vol. 11, 2023 (Kreuzberger, Kühl, Hirschl), University of Bayreuth repository
    url: https://epub.uni-bayreuth.de/7577/1/Machine_Learning_Operations_MLOps_Overview_Definition_and_Architecture.pdf
    type: peer-reviewed
    accessed: 2026-10-30
  - id: s3
    title: "MLOps: Continuous delivery and automation pipelines in machine learning"
    publisher: Google Cloud Architecture Center
    url: https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
    type: official-docs
    accessed: 2026-10-30
  - id: s4
    title: "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction"
    publisher: IEEE Big Data 2017 (Breck et al.), Google Research
    url: https://research.google/pubs/pub46555/
    type: lab-research
    accessed: 2026-10-30
  - id: s5
    title: "MLflow documentation: traditional ML"
    publisher: MLflow Project (LF Projects)
    url: https://mlflow.org/docs/latest/ml/
    type: official-docs
    accessed: 2026-10-30
created: 2026-10-30
---

# MLOps

**MLOps** (machine learning operations) is the set of practices, tools and team culture used to take machine learning models out of notebooks and keep them working in production. Kreuzberger, Kühl and Hirschl, after reviewing 27 peer-reviewed articles, surveying tools and interviewing eight experts, define it as a paradigm spanning the end-to-end conceptualization, implementation, monitoring, deployment and scalability of ML products, drawing on machine learning, software engineering (especially DevOps) and data engineering to bridge development and operations.[^s2]

## Origin: technical debt in ML systems

The field's founding motivation is usually traced to a 2015 NeurIPS paper by D. Sculley and colleagues at Google. They argued that ML systems are fast to build but costly to maintain, and that in real deployments the model code is only a small box surrounded by much larger infrastructure for data collection, feature extraction, serving and monitoring.[^s1] They catalogued ML-specific debt: *entanglement* summarized as CACE ("Changing Anything Changes Everything"), correction cascades, undeclared consumers of model outputs, unstable data dependencies, feedback loops in which a model shapes its own future training data, glue code, "pipeline jungles" and neglected configuration.[^s1] A follow-up from the same group, the ML Test Score (IEEE Big Data 2017), turned this into 28 concrete tests and monitoring requirements for judging production readiness.[^s4]

## How it works

ML differs from ordinary software delivery in several ways that MLOps addresses. Google Cloud's reference architecture notes that testing must cover data, schemas and model quality as well as code; that what gets deployed is often a whole multi-step training pipeline rather than one binary; and that models decay in production as data distributions shift, so data statistics and online performance must be monitored.[^s3] Hence MLOps adds **continuous training (CT)** to the DevOps pair of continuous integration and continuous delivery.[^s3]

Google describes three maturity levels.[^s3]

- **Level 0 — manual:** notebooks, hand-offs from data scientists to engineers, rare releases and little monitoring.[^s3]
- **Level 1 — pipeline automation:** an automated training pipeline is deployed and retrains on triggers such as a schedule, new data, a performance drop or a distribution shift, with automated data and model validation and metadata tracking.[^s3]
- **Level 2 — CI/CD automation:** new pipeline components are themselves built, tested and deployed automatically, backed by source control, a model registry, a feature store, a metadata store and a pipeline orchestrator.[^s3]

Kreuzberger et al. distil nine principles: CI/CD automation, workflow orchestration, reproducibility, versioning of data, model and code, collaboration, continuous training and evaluation, metadata tracking and logging, continuous monitoring, and feedback loops.[^s2] They map these to nine technical components (including a feature store, model registry, metadata store, serving and monitoring) and seven roles, from business stakeholder and data engineer to a dedicated ML/MLOps engineer.[^s2]

## Limitations and open questions

MLOps is a loosely bounded term, which is why survey work set out to define it in the first place.[^s2] The same study identifies organizational challenges (a research-oriented data science culture clashing with product delivery, shortages of ML and data engineers, siloed teams), infrastructure challenges from fluctuating data volume and compute demand, and operational difficulty in root-causing failures across many interacting components.[^s2] Sculley et al. stressed that debt is hard to measure and that paying it down needs a culture that rewards simplification and stability, not just accuracy gains.[^s1]

## In practice

Teams typically assemble an MLOps stack from an orchestrator, experiment tracking, a registry and serving infrastructure, either from cloud services or open source. MLflow, maintained under the Linux Foundation's LF Projects, is a widely used open-source example offering experiment tracking, a model registry, evaluation and deployment tooling; as of 2026 its documentation also covers tracing, evaluation and prompt management for LLM applications and agents.[^s5] That extension reflects how practices for LLM-based systems (often called LLMOps) build on MLOps foundations.[^s5]

## Connections

MLOps is a specialization of **DevOps** applied to **machine learning**, adding continuous training and data-centric testing.[^s3] It was strongly **influenced by** Sculley et al.'s *Hidden Technical Debt in Machine Learning Systems*.[^s1] Its core parts include a **feature store**, which prevents training-serving skew, and a **model registry** for versioned models; continuous monitoring and retraining **mitigate data drift**.[^s3] It is **implemented in** tools such as **MLflow**, is a precursor to **LLMOps**, and interacts closely with **model serving**, **distributed training** and **AI evaluation**, since automated model validation gates each release.[^s2][^s5]

## Sources

[^s1]: Sculley et al., "Hidden Technical Debt in Machine Learning Systems", NeurIPS 2015. https://proceedings.neurips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf (accessed 2026-10-30)
[^s2]: Kreuzberger, Kühl, Hirschl, "Machine Learning Operations (MLOps): Overview, Definition, and Architecture", IEEE Access 11, 2023. https://epub.uni-bayreuth.de/7577/1/Machine_Learning_Operations_MLOps_Overview_Definition_and_Architecture.pdf (accessed 2026-10-30)
[^s3]: Google Cloud, "MLOps: Continuous delivery and automation pipelines in machine learning" (updated 2024-08-28). https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning (accessed 2026-10-30)
[^s4]: Breck et al., "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction", IEEE Big Data 2017. https://research.google/pubs/pub46555/ (accessed 2026-10-30)
[^s5]: MLflow Project, MLflow documentation. https://mlflow.org/docs/latest/ml/ (accessed 2026-10-30)
