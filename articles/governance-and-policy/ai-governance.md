---
id: kt:ai-governance
type: Field
title: AI governance
aliases: [artificial intelligence governance, governance of artificial intelligence, governance of AI]
domain: governance-and-policy
summary: >-
  The study and practice of the norms, laws, standards, institutions and organisational processes that
  shape how AI systems are developed, deployed and used, so that their benefits are realised and their
  risks are identified, managed and held to account.
maturity: emerging
broader: [kt:artificial-intelligence]
related: [kt:ai-safety, kt:ai-alignment, kt:algorithmic-bias-and-fairness, kt:ai-safety-institutes]
relations:
  - {predicate: hasPart, object: kt:compute-governance}
  - {predicate: hasPart, object: kt:eu-ai-act}
  - {predicate: hasPart, object: kt:nist-ai-risk-management-framework}
  - {predicate: hasPart, object: kt:oecd-ai-principles}
  - {predicate: influencedBy, object: kt:ai-governance-a-research-agenda}
sources:
  - id: s1
    title: "AI Governance: A Research Agenda (v1.0)"
    publisher: Allan Dafoe, Centre for the Governance of AI, Future of Humanity Institute, University of Oxford, 27 August 2018
    url: https://www.fhi.ox.ac.uk/29928-2
    type: primary
    accessed: 2026-11-12
  - id: s2
    title: "OECD AI Principles overview"
    publisher: OECD.AI Policy Observatory (OECD Recommendation on Artificial Intelligence, adopted 2019, updated 2024)
    url: https://oecd.ai/en/ai-principles
    type: intergovernmental
    accessed: 2026-11-12
  - id: s3
    title: "AI Act enters into force"
    publisher: European Commission, 1 August 2024
    url: https://commission.europa.eu/news/ai-act-enters-force-2024-08-01_en
    type: government
    accessed: 2026-11-12
  - id: s4
    title: "AI RMF 1.0, Section 5: AI RMF Core"
    publisher: National Institute of Standards and Technology (NIST), Trustworthy and Responsible AI Resource Center
    url: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/
    type: government
    accessed: 2026-11-12
  - id: s5
    title: "Artificial Intelligence: the global landscape of ethics guidelines (arXiv 1906.11668)"
    publisher: Anna Jobin, Marcello Ienca and Effy Vayena, authors' arXiv version, June 2019 (published in Nature Machine Intelligence, 2019)
    url: https://arxiv.org/abs/1906.11668
    type: primary
    accessed: 2026-11-12
  - id: s6
    title: "Principles alone cannot guarantee ethical AI (arXiv 1906.06668)"
    publisher: Brent Mittelstadt, Oxford Internet Institute and Alan Turing Institute, authors' arXiv version, 2019
    url: https://arxiv.org/pdf/1906.06668
    type: primary
    accessed: 2026-11-12
created: 2026-11-12
---

# AI governance

**AI governance** is both a field of research and a body of practice concerned with the rules, institutions and processes that steer how artificial intelligence is built and used. It spans binding law, soft-law principles, technical standards, international agreements and the internal controls of the organisations that develop and deploy AI. An influential early framing came from Allan Dafoe's *AI Governance: A Research Agenda* (first drafted in 2017, version 1.0 in August 2018) at Oxford's Future of Humanity Institute, which described the field as studying how humanity can best navigate the transition to advanced AI, with attention to its political, economic, military and ethical dimensions.[^s1]

## Scope and research questions

Dafoe organised the field into three clusters.[^s1] The **technical landscape** asks what AI will be able to do and when, including forecasting progress. **AI politics** looks at the dynamics among firms, governments, publics and researchers, including international security and economic competition. **Ideal governance** asks which norms, institutions and systems would best ensure that AI is developed and used beneficially.[^s1] Alongside this long-range framing, much of the guidance written since has centred on present-day concerns such as fairness, transparency and privacy.[^s5]

## Layers of governance

AI governance operates at several levels at once.

**International principles.** The OECD Recommendation on Artificial Intelligence, adopted in May 2019 and updated in May 2024 sets five values-based principles (inclusive growth and well-being; human rights and democratic values, including fairness and privacy; transparency and explainability; robustness, security and safety; and accountability) and five recommendations to governments, ranging from investment in R&D to international co-operation. The OECD.AI site listed 47 adherent jurisdictions as of November 2026.[^s2] It defines an "AI system" as a machine-based system that infers from its inputs how to generate outputs such as predictions, content, recommendations or decisions, with varying autonomy and adaptiveness.[^s2]

**Binding regulation.** The EU AI Act, which entered into force on 1 August 2024, is the most comprehensive AI statute so far. It takes a risk-based approach: most systems, such as spam filters, carry no obligations; systems like chatbots carry transparency duties; high-risk uses such as medical software or recruitment tools must meet requirements on risk mitigation, data quality and human oversight; and practices of unacceptable risk, such as social scoring, are banned. A new European AI Office supervises the rules for general-purpose AI models.[^s3]

**Organisational governance.** Inside companies and agencies, governance means policies, accountability lines and risk processes. The NIST AI Risk Management Framework makes **Govern** one of its four core functions alongside Map, Measure and Manage. NIST treats it as cross-cutting: it builds a risk-aware culture set by senior leadership, documents roles and responsibilities, covers third-party software and data, and places responsibility for AI risk decisions on executives.[^s4]

## Evidence and critiques

A recurring critique is that AI governance has produced far more principles than enforceable practice. Jobin, Ienca and Vayena analysed 84 AI ethics guidelines published by companies, research bodies and governments and found convergence on five themes (transparency, justice and fairness, non-maleficence, responsibility and privacy), but deep divergence on what those terms mean, why they matter and how to implement them. No single principle appeared in every document, and the corpus was dominated by the US, the UK and Europe, with Africa and South America barely represented except through international bodies.[^s5]

Brent Mittelstadt argued that copying medical ethics' principle-based model gives false reassurance, because AI development lacks medicine's common aims and fiduciary duties, its professional history and norms, its proven methods for turning principles into decisions, and its legal and professional accountability.[^s6] High-level consensus can therefore hide real political disagreement, and he located the hard work in binding accountability and sector-specific practice.[^s6] The move since 2023 toward binding law such as the AI Act and toward auditable management frameworks such as the NIST AI RMF can be read as a response to that gap.[^s3][^s4]

## Connections

AI governance sits beneath **artificial intelligence** as its policy and institutional counterpart. It **has parts** that already have their own nodes: **compute governance**, which uses chips and data centres as a policy lever; the **EU AI Act** as binding law; the **NIST AI Risk Management Framework** as an organisational standard; and the **OECD AI Principles** as an intergovernmental baseline.[^s2][^s3][^s4] It was **influenced by** Dafoe's *AI Governance: A Research Agenda*, which helped define it as a field.[^s1] It is closely related to **AI safety** and **AI alignment**, which supply technical methods that governance can require or verify; to **algorithmic bias and fairness**, one of the convergent principles Jobin et al. identified; and to government **AI safety institutes**, which are among its newest institutions.[^s5]

## Sources

[^s1]: A. Dafoe, "AI Governance: A Research Agenda", v1.0, Centre for the Governance of AI, Future of Humanity Institute, University of Oxford, 27 August 2018. https://www.fhi.ox.ac.uk/29928-2 (accessed 2026-11-12)
[^s2]: OECD.AI Policy Observatory, "OECD AI Principles overview". https://oecd.ai/en/ai-principles (accessed 2026-11-12)
[^s3]: European Commission, "AI Act enters into force", 1 August 2024. https://commission.europa.eu/news/ai-act-enters-force-2024-08-01_en (accessed 2026-11-12)
[^s4]: NIST, "AI RMF 1.0, Section 5: AI RMF Core", Trustworthy and Responsible AI Resource Center. https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ (accessed 2026-11-12)
[^s5]: A. Jobin, M. Ienca and E. Vayena, "Artificial Intelligence: the global landscape of ethics guidelines", arXiv:1906.11668, 2019 (Nature Machine Intelligence). https://arxiv.org/abs/1906.11668 (accessed 2026-11-12)
[^s6]: B. Mittelstadt, "Principles alone cannot guarantee ethical AI", arXiv:1906.06668, 2019. https://arxiv.org/pdf/1906.06668 (accessed 2026-11-12)
