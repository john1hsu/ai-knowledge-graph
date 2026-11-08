---
id: kt:ai-safety-institutes
type: Organization
title: AI safety institutes
aliases: [AISI, AISIs, AI Safety Institute, International Network of AI Safety Institutes]
domain: governance-and-policy
summary: >-
  Government-backed technical bodies, first created by the UK and US in November 2023, that test advanced AI
  models for national-security and safety risks, research evaluation science and coordinate internationally,
  without holding regulatory powers.
maturity: emerging
broader: [kt:ai-governance]
related: [kt:ai-evaluation, kt:red-teaming, kt:nist-ai-risk-management-framework, kt:executive-orders-on-ai, kt:ai-alignment]
relations:
  - {predicate: hasPart, object: kt:uk-ai-security-institute}
  - {predicate: hasPart, object: kt:center-for-ai-standards-and-innovation}
  - {predicate: influencedBy, object: kt:ai-safety-summit}
sources:
  - id: s1
    title: "Prime Minister launches new AI Safety Institute"
    publisher: UK Department for Science, Innovation and Technology, 2 November 2023
    url: https://www.gov.uk/government/news/prime-minister-launches-new-ai-safety-institute
    type: government
    accessed: 2026-11-08
  - id: s2
    title: "Artificial Intelligence Safety Institute Consortium (Federal Register notice 2023-24216)"
    publisher: National Institute of Standards and Technology, Federal Register Vol. 88 No. 211, 2 November 2023
    url: https://regulations.justia.com/regulations/fedreg/2023/11/02/2023-24216.html
    type: government
    accessed: 2026-11-08
  - id: s3
    title: "Understanding the First Wave of AI Safety Institutes: Characteristics, Functions, and Challenges"
    publisher: Araujo, Fort & Guest (Institute for AI Policy and Strategy), arXiv:2410.09219, October 2024
    url: https://arxiv.org/pdf/2410.09219
    type: primary
    accessed: 2026-11-08
  - id: s4
    title: "Mission Statement: International Network of AI Safety Institutes"
    publisher: National Institute of Standards and Technology, 21 November 2024
    url: https://www.nist.gov/system/files/documents/2024/11/20/Mission%20Statement%20-%20International%20Network%20of%20AISIs.pdf
    type: government
    accessed: 2026-11-08
  - id: s5
    title: "Letter from the Secretary of State on the AI Security Institute"
    publisher: UK Parliament deposited paper DEP2025-0123 (Peter Kyle to Chi Onwurah MP), 24 February 2025
    url: https://data.parliament.uk/DepositedPapers/Files/DEP2025-0123/Letter-AI_Security_Institute.pdf
    type: government
    accessed: 2026-11-08
  - id: s6
    title: "Commerce statement on reforming the U.S. AI Safety Institute into the Center for AI Standards and Innovation"
    publisher: U.S. Department of Commerce, June 2025
    url: https://www.commerce.gov/node/7172
    type: government
    accessed: 2026-11-08
  - id: s7
    title: "Efforts to share best practices on AI measurement and evaluations driven forward through the International Network for Advanced AI Measurement, Evaluation and Science"
    publisher: UK Government press release, 9 December 2025
    url: https://www.gov.uk/government/news/efforts-to-share-best-practices-on-ai-measurement-and-evaluations-driven-forward-through-the-international-network-for-advanced-ai-measurement-evalua
    type: government
    accessed: 2026-11-08
created: 2026-11-08
---

# AI safety institutes

**AI safety institutes** (AISIs) are technical bodies set up inside national governments to evaluate advanced AI systems, build the science of measuring their risks, and share findings with other states. The first two were announced in the same week: the UK launched its AI Safety Institute on 2 November 2023, during the AI Safety Summit at Bletchley Park, and the US set up its own AI Safety Institute within NIST, which announced a supporting research consortium the same day.[^s1][^s2][^s6] A 2024 analysis treats the UK, US and Japanese institutes as the "first wave" and compares later bodies in the EU, Canada, France and Singapore against them.[^s3]

## Origin

The UK institute grew out of the government's Frontier AI Taskforce, kept its chair Ian Hogarth, and was presented as the UK's contribution to the safety-testing collaboration agreed at Bletchley. Its stated job was to test frontier models before and after release, so developers would not be the only judges of their own safety claims.[^s1] In the US, NIST tied its effort to the October 2023 executive order on safe, secure and trustworthy AI, opening a consortium of outside organizations, under research agreements, to develop measurement science for the most capable foundation models.[^s2]

## Characteristics and functions

Araujo, Fort and Guest identify three shared traits of the first wave. These institutes are technical government organizations, their mandate is limited to the safety of advanced AI rather than AI policy in general, and they have no regulatory or enforcement powers.[^s3] Their central activity is **evaluation**: testing models for misuse risks such as cyber, chemical and biological uplift, for autonomous behaviour, and for how well safeguards hold up. Three further functions connect back to evaluation: empirical safety research, contributions to standards, and cooperation between governments, companies and civil society.[^s3] The UK launch announcement also framed this testing as covering everything from bias and misinformation to loss of human control.[^s1]

## International network

On 21 November 2024, ten members (Australia, Canada, the European Commission, France, Japan, Kenya, the Republic of Korea, Singapore, the UK and the US) launched the International Network of AI Safety Institutes in San Francisco. They set four priorities: research, testing, shared guidance on interpreting results, and inclusion of countries at every stage of development.[^s4] At a December 2025 meeting held alongside NeurIPS in San Diego, the group renamed itself the International Network for Advanced AI Measurement, Evaluation and Science. Its focus shifted to shared methods for measuring advanced AI capabilities, with the UK becoming network coordinator.[^s7]

## Rebranding toward security (2025)

Both founding institutes changed their names in 2025. In February the UK renamed its body the **AI Security Institute**. The government said the change reflected a focus on risks with security implications, such as chemical and biological weapons, cyber-attacks, fraud and child sexual abuse material. It added a criminal-misuse team working with the Home Office, while bias and free-speech questions moved to other parts of the department.[^s5] In June 2025 the US Commerce Secretary announced that the US AI Safety Institute would be reformed into the **Center for AI Standards and Innovation** (CAISI), still within NIST. CAISI's mandate includes voluntary agreements with developers, unclassified evaluations of national-security-relevant capabilities, assessment of adversary AI systems, and representing US interests in international standards.[^s6]

## Limitations and critiques

Because AISIs lack regulatory powers, their access to models depends on voluntary commitments from developers. Critics argue that close relationships with leading labs risk regulatory capture and may reduce pressure for binding rules.[^s3] Other critiques are that a narrow safety focus neglects fairness, bias and competitiveness, that evaluations can be gamed or miss sector-specific harms, and that institutes may duplicate the work of standards bodies such as ISO and IEC.[^s3] The 2025 renamings sharpened that debate over scope. Both governments moved explicitly away from broader societal harms toward security and national-interest framing.[^s5][^s6]

## Connections

AISIs sit under **AI governance** as one of its institutional forms. They differ from laws such as the EU AI Act because they test and advise rather than enforce.[^s3] Their core method is **AI evaluation** of misuse and autonomy risks, which overlaps with adversarial **red teaming**.[^s3] The US effort was linked by NIST to the 2023 **executive order on AI**, and it sits in the same agency as the **NIST AI Risk Management Framework**, which it complements with model testing.[^s2][^s6] The movement began at the Bletchley **AI Safety Summit**.[^s1] The two founding bodies now operate as the **UK AI Security Institute** and the **Center for AI Standards and Innovation**.[^s5][^s6] Their research on catastrophic and loss-of-control risks links them to **AI alignment**.[^s1][^s5]

## Sources
[^s1]: UK DSIT, "Prime Minister launches new AI Safety Institute", 2 November 2023. https://www.gov.uk/government/news/prime-minister-launches-new-ai-safety-institute (accessed 2026-11-08)
[^s2]: NIST, "Artificial Intelligence Safety Institute Consortium", Federal Register 88(211), 2 November 2023. https://regulations.justia.com/regulations/fedreg/2023/11/02/2023-24216.html (accessed 2026-11-08)
[^s3]: Araujo, Fort & Guest, "Understanding the First Wave of AI Safety Institutes", arXiv:2410.09219, October 2024. https://arxiv.org/pdf/2410.09219 (accessed 2026-11-08)
[^s4]: NIST, "Mission Statement: International Network of AI Safety Institutes", 21 November 2024. https://www.nist.gov/system/files/documents/2024/11/20/Mission%20Statement%20-%20International%20Network%20of%20AISIs.pdf (accessed 2026-11-08)
[^s5]: Peter Kyle, letter to Chi Onwurah MP on the AI Security Institute, 24 February 2025 (UK Parliament DEP2025-0123). https://data.parliament.uk/DepositedPapers/Files/DEP2025-0123/Letter-AI_Security_Institute.pdf (accessed 2026-11-08)
[^s6]: U.S. Department of Commerce, statement on transforming the U.S. AI Safety Institute into CAISI, June 2025. https://www.commerce.gov/node/7172 (accessed 2026-11-08)
[^s7]: UK Government, press release on the International Network for Advanced AI Measurement, Evaluation and Science, 9 December 2025. https://www.gov.uk/government/news/efforts-to-share-best-practices-on-ai-measurement-and-evaluations-driven-forward-through-the-international-network-for-advanced-ai-measurement-evalua (accessed 2026-11-08)
