---
id: kt:expert-systems
type: Paradigm
title: Expert systems
aliases: [expert system, knowledge-based system, rule-based expert system]
domain: ai-history
summary: >-
  Symbolic AI programs that capture the knowledge of human specialists in a narrow domain, usually as if-then
  production rules in a knowledge base, and apply it through a separate inference engine; pioneered at Stanford
  with DENDRAL (from 1965) and MYCIN (from 1972), they were the first commercially significant form of AI.
maturity: historical
broader: [kt:symbolic-ai, kt:knowledge-representation]
related: [kt:logic-theorist, kt:ai-winter, kt:dendral, kt:mycin]
relations:
  - {predicate: createdBy, object: kt:edward-feigenbaum}
  - {predicate: hasPart, object: kt:knowledge-base}
  - {predicate: hasPart, object: kt:inference-engine}
  - {predicate: contrastsWith, object: kt:machine-learning}
sources:
  - id: s1
    title: "Artificial intelligence: Expert systems"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com:443/technology/artificial-intelligence/Expert-systems
    type: encyclopedia
    accessed: 2026-11-13
  - id: s2
    title: "Edward Albert Feigenbaum"
    publisher: Encyclopaedia Britannica
    url: https://www.britannica.com/biography/Edward-Albert-Feigenbaum
    type: encyclopedia
    accessed: 2026-11-13
  - id: s3
    title: "Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project"
    publisher: B. G. Buchanan and E. H. Shortliffe (eds.), Addison-Wesley, 1984 (author-hosted edition, Columbia DBMI)
    url: https://people.dbmi.columbia.edu/~ehs7001/Buchanan-Shortliffe-1984/MYCIN%20Book.htm
    type: primary
    accessed: 2026-11-13
  - id: s4
    title: "Major Lessons from This Work (ch. 36 of Rule-Based Expert Systems)"
    publisher: B. G. Buchanan and E. H. Shortliffe, Addison-Wesley, 1984
    url: https://people.dbmi.columbia.edu/shortliffe/Buchanan-Shortliffe-1984/Chapter-36.pdf
    type: primary
    accessed: 2026-11-13
  - id: s5
    title: "Extending a Knowledge-Based System to Deal with Ad Hoc Constraints"
    publisher: J. McDermott and B. Steele, Proceedings of IJCAI 1981, pp. 824–827
    url: https://ijcai.org/proceedings/1981/157
    type: peer-reviewed
    accessed: 2026-11-13
created: 2026-11-13
---

# Expert systems

An **expert system** is a computer program that encodes the specialised knowledge of human experts so it can solve problems in a narrow, self-contained domain, sometimes performing better than any single expert would. Classic examples worked in medical diagnosis and chemical analysis, and commercial systems later handled credit authorisation, financial management, airline scheduling and automobile design.[^s1] Expert systems were the dominant applied form of symbolic AI: instead of learning from data, they reasoned over knowledge that people wrote down explicitly.

## How it works

An expert system has two main parts. The **knowledge base** holds domain knowledge, typically as if-then *production rules*. The **inference engine** applies those rules to the facts of a case. For instance, from "if x then y" and "if y then z" it can conclude z once x is known, and it can ask the user about conditions it cannot settle on its own.[^s1] The people who built knowledge bases were called *knowledge engineers*. They interviewed domain specialists to bring out the tacit rules of thumb the experts used, and this practice became known as knowledge engineering.[^s2]

Keeping knowledge separate from the reasoning procedure was a deliberate design principle. The MYCIN team argued that it made programs easier to extend one rule at a time. It also meant the same engine could be reused: EMYCIN was MYCIN with its medical rules removed, and it was later applied to electronics, tax advice and software consulting.[^s4] Because the engine records which rules fired, it can answer WHY a question was asked and HOW a conclusion was reached by replaying its chain of goals. That early form of explainability turned out to be essential for physicians to accept the system.[^s4] To deal with uncertain evidence, MYCIN attached *certainty factors* to its rules. The authors admitted this was a heuristic calculus rather than rigorous probability, and found that experts needed only four or five levels of evidential strength.[^s4]

## History

Edward Feigenbaum, a student of Herbert Simon, moved to Stanford in 1965 and began DENDRAL there with the geneticist Joshua Lederberg (the chemist Carl Djerassi also collaborated).[^s2][^s1] DENDRAL inferred the molecular structure of organic compounds from mass-spectrometry data, rivalled expert chemists in performance, and was used in both industry and academia.[^s1] Work on MYCIN began at Stanford in 1972. It diagnosed bacterial blood infections, requested additional patient data and laboratory tests, recommended antibiotic therapy, and could explain its reasoning when asked.[^s1] In a blinded evaluation, outside infectious-disease experts disagreed with MYCIN's therapy recommendations no more often than with those of Stanford faculty.[^s4] Buchanan and Shortliffe's 1984 retrospective on the project covers rule representation, knowledge acquisition, explanation, tutoring and evaluation, and it became a standard reference for the field.[^s3] In industry, John McDermott's rule-based R1 program was used to by Digital Equipment Corporation's manufacturing organisation to configure VAX-11 computer systems from customer orders.[^s5] Feigenbaum received the 1994 ACM Turing Award, and his biography credits him as a major pioneer of expert systems.[^s2]

## Limitations

The MYCIN authors identified knowledge acquisition as "the critical bottleneck in building expert systems." Extracting and debugging rules took scarce expert time, and tools that let experts edit rules directly did not remove the need for knowledge engineers.[^s4] Expert systems also proved brittle. They had no common sense and did not recognise the edges of their competence. Britannica gives two examples: MYCIN would look for a bacterial cause in a patient bleeding to death from a gunshot wound, and a system would act on a dosage error caused by swapped age and weight fields.[^s1] Good test performance did not guarantee use. MYCIN never entered routine clinical practice because it ran only in Interlisp on costly time-sharing systems (TENEX and TOPS-20) unavailable on wards or in offices, required 50–60 typed answers per consultation, and lost both funding and clinical collaborators by the late 1970s.[^s4] The EMYCIN approach also suited diagnosis and classification much better than planning or constraint problems.[^s4]

## Connections

Expert systems are a branch of `kt:symbolic-ai` that depends on `kt:knowledge-representation`. Structurally they consist of a `kt:knowledge-base` and an `kt:inference-engine`, the separation emphasised in the MYCIN work.[^s4] They follow the earlier heuristic-search programs such as `kt:logic-theorist`, co-created by Herbert Simon, under whom Feigenbaum trained.[^s2] `kt:dendral` and `kt:mycin` are the canonical systems, and `kt:edward-feigenbaum` is credited as the paradigm's chief architect.[^s2][^s1] The approach contrasts with `kt:machine-learning`: expert systems receive their knowledge by hand-written rules from human experts, whereas learned models infer it from data.[^s1] The brittleness and acquisition costs described above are linked to the later collapse of enthusiasm for symbolic AI, covered under `kt:ai-winter`.

## Sources
[^s1]: Encyclopaedia Britannica, "Artificial intelligence: Expert systems". https://www.britannica.com:443/technology/artificial-intelligence/Expert-systems (accessed 2026-11-13)
[^s2]: Encyclopaedia Britannica, "Edward Albert Feigenbaum". https://www.britannica.com/biography/Edward-Albert-Feigenbaum (accessed 2026-11-13)
[^s3]: B. G. Buchanan and E. H. Shortliffe (eds.), *Rule-Based Expert Systems: The MYCIN Experiments of the Stanford Heuristic Programming Project*, Addison-Wesley, 1984. https://people.dbmi.columbia.edu/~ehs7001/Buchanan-Shortliffe-1984/MYCIN%20Book.htm (accessed 2026-11-13)
[^s4]: B. G. Buchanan and E. H. Shortliffe, "Major Lessons from This Work", ch. 36 of *Rule-Based Expert Systems*, 1984. https://people.dbmi.columbia.edu/shortliffe/Buchanan-Shortliffe-1984/Chapter-36.pdf (accessed 2026-11-13)
[^s5]: J. McDermott and B. Steele, "Extending a Knowledge-Based System to Deal with Ad Hoc Constraints", IJCAI 1981, pp. 824–827. https://ijcai.org/proceedings/1981/157 (accessed 2026-11-13)
