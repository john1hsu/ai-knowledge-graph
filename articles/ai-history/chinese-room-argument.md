---
id: kt:chinese-room-argument
type: Concept
title: Chinese room argument
aliases: [Chinese room, Searle's Chinese room]
domain: ai-history
summary: >-
  A thought experiment published by philosopher John Searle in 1980 arguing that running a program,
  however convincing its outputs, is not by itself sufficient for understanding, because symbol
  manipulation is purely syntactic while minds have semantic content.
maturity: foundational
broader: [kt:philosophy-of-artificial-intelligence]
related: [kt:turing-test, kt:large-language-model, kt:symbol-grounding-problem, kt:strong-ai]
relations:
  - {predicate: createdBy, object: kt:john-searle}
  - {predicate: introducedIn, object: kt:minds-brains-and-programs}
  - {predicate: contrastsWith, object: kt:turing-test}
sources:
  - id: s1
    title: "Minds, brains, and programs"
    publisher: J. R. Searle, The Behavioral and Brain Sciences 3 (1980) 417–457 (copy hosted for Yale CPSC 458)
    url: https://zoo.cs.yale.edu/classes/cs458/lectures/minds-brains-and-programs.pdf
    type: primary
    accessed: 2026-10-30
  - id: s2
    title: "The Chinese Room Argument (Summer 2006 edition)"
    publisher: Stanford Encyclopedia of Philosophy (David Cole)
    url: https://plato.stanford.edu/archives/sum2006/entries/chinese-room/
    type: academic
    accessed: 2026-10-30
  - id: s3
    title: "Chinese Room Argument"
    publisher: Internet Encyclopedia of Philosophy (Larry Hauser)
    url: https://iep.utm.edu/chinese-room-argument/
    type: academic
    accessed: 2026-10-30
  - id: s4
    title: "Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data"
    publisher: Bender and Koller, Proceedings of ACL 2020, pp. 5185–5198
    url: https://aclanthology.org/2020.acl-main.463.pdf
    type: peer-reviewed
    accessed: 2026-10-30
created: 2026-10-30
---

# Chinese room argument

The Chinese room argument is a thought experiment introduced by the Berkeley philosopher John Searle in "Minds, brains, and programs", published in *The Behavioral and Brain Sciences* in 1980. It targets what Searle called **strong AI**: the claim that an appropriately programmed computer does not merely simulate a mind but literally has cognitive states such as understanding, and that its program explains human cognition. Searle had no quarrel with **weak AI**, the use of computers as tools for testing hypotheses about the mind.[^s1] The paper appeared with commentaries from 27 cognitive scientists and Searle's replies, and it became one of the most discussed arguments in cognitive science.[^s2]

## The thought experiment

Searle's immediate target was Roger Schank's story-understanding programs, which could answer questions about short restaurant stories, such as whether a customer ate his hamburger, even when the story never said so.[^s1] Searle imagines himself, a man who knows no Chinese, locked in a room with batches of Chinese characters and a rulebook written in English that tells him how to match and return symbols purely by their shapes. Questions in Chinese come in; by following the rules he sends back answers that native speakers outside cannot tell apart from a fluent speaker's. Yet he understands nothing of the stories or the questions. Since he is doing exactly what a computer running the program does, Searle concludes that the computer understands nothing either.[^s1][^s3]

Searle later restated the point as a short derivation: programs are formal (syntactic); minds have mental contents (semantics); syntax by itself is neither constitutive of nor sufficient for semantics; therefore programs are neither constitutive of nor sufficient for minds. The room is meant to support the third premise.[^s2][^s3] Searle did not claim machines cannot think; brains are machines that do. His claim is that whatever thinks must have causal powers equivalent to the brain's, and running a formal program cannot supply them.[^s1][^s3]

## Replies and responses

Searle anticipated several objections in the original paper. The **systems reply** says the man is only one component and the whole system understands; Searle answers that the man could memorize the rulebook and do everything in his head and would still understand nothing. The **robot reply** says the program needs a body with sensors and motors; Searle replies that camera input is just more symbols for the man to shuffle. The **brain simulator reply** proposes simulating the neuron firings of a Chinese speaker; Searle counters with a system of water pipes and valves that copies the formal structure but not the causal properties that produce intentionality. He also rejects the **other minds reply** (we judge people by behaviour, so we should judge machines the same way) and the **many mansions reply** (future non-program devices may succeed), the latter on the grounds that it redefines strong AI.[^s1][^s3]

The debate did not settle. Daniel Dennett, Jerry Fodor, Ned Block and others defended versions of the systems reply; David Cole and others developed a "virtual mind" reply, locating understanding in an abstract mind realised by the system rather than in the man or the hardware; and critics including Dennett and Steven Pinker argued that the argument trades on unreliable intuitions, for instance by ignoring the enormous speed and scale a real system would need.[^s2] Paul and Patricia Churchland argued that brain-like parallel processing escapes the argument, to which Searle answered with a "Chinese gym" of many monolingual English speakers working in parallel.[^s3] The argument has precedents in Leibniz's mill and Block's 1978 "Chinese nation" scenario.[^s2]

## Relevance to modern AI

The room is often read as a parody of the **Turing test**: it describes a system that passes a purely behavioural test while, Searle argues, lacking understanding, and so attacks behaviourism and functionalism about the mind.[^s3] The question returned with neural language models. Emily Bender and Alexander Koller's ACL 2020 paper revisits the Chinese room and argues that a model trained only on linguistic form cannot, in principle, learn meaning, defined as the link between form and communicative intent. Their "octopus test" imagines an eavesdropper who mimics one side of a conversation well enough for small talk but fails once real-world grounding is needed, and they connect this to Stevan Harnad's symbol grounding problem.[^s4] Unlike Searle, they frame the issue as one of what training data provides rather than of computation as such, and they stress careful evaluation of claims that models "understand".[^s4]

## Connections

The argument was created by **John Searle** and introduced in **Minds, brains, and programs**, and it is a central text in the **philosophy of artificial intelligence**.[^s1][^s2] It **contrasts with** the **Turing test**, whose behavioural criterion it was designed to undercut, and its target is the thesis of **strong AI**.[^s1][^s3] Through Bender and Koller's form-versus-meaning critique it links to current debates over whether **large language models** understand language, and to the **symbol grounding problem**.[^s4]

## Sources
[^s1]: J. R. Searle, "Minds, brains, and programs", The Behavioral and Brain Sciences 3 (1980) 417–457. https://zoo.cs.yale.edu/classes/cs458/lectures/minds-brains-and-programs.pdf (accessed 2026-10-30)
[^s2]: D. Cole, "The Chinese Room Argument", Stanford Encyclopedia of Philosophy, Summer 2006 edition. https://plato.stanford.edu/archives/sum2006/entries/chinese-room/ (accessed 2026-10-30)
[^s3]: L. Hauser, "Chinese Room Argument", Internet Encyclopedia of Philosophy. https://iep.utm.edu/chinese-room-argument/ (accessed 2026-10-30)
[^s4]: E. M. Bender and A. Koller, "Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data", ACL 2020, pp. 5185–5198. https://aclanthology.org/2020.acl-main.463.pdf (accessed 2026-10-30)
