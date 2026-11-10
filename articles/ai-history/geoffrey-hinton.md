---
id: kt:geoffrey-hinton
type: Person
title: Geoffrey Hinton
aliases: [Geoffrey E. Hinton, Geoffrey Everest Hinton, Geoff Hinton]
domain: ai-history
summary: >-
  British-Canadian cognitive psychologist and computer scientist (born 1947) whose work on backpropagation,
  Boltzmann machines, dropout and deep convolutional networks helped found modern deep learning; co-recipient of
  the 2018 ACM Turing Award and the 2024 Nobel Prize in Physics.
maturity: historical
broader: [kt:deep-learning, kt:connectionism]
related: [kt:backpropagation, kt:dropout, kt:knowledge-distillation, kt:imagenet-and-alexnet, kt:boltzmann-machine, kt:deep-belief-network]
sources:
  - id: s1
    title: "Geoffrey E. Hinton's Biographical Sketch"
    publisher: Department of Computer Science, University of Toronto
    url: https://www.cs.toronto.edu/~hinton/bio.html
    type: academic
    accessed: 2026-11-10
  - id: s2
    title: "Geoffrey Hinton"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/biography/Geoffrey-Hinton
    type: encyclopedia
    accessed: 2026-11-10
  - id: s3
    title: "Press release: The Nobel Prize in Physics 2024"
    publisher: The Royal Swedish Academy of Sciences / Nobel Prize Outreach (nobelprize.org)
    url: https://www.nobelprize.org/prizes/physics/2024/press-release/
    type: primary
    accessed: 2026-11-10
  - id: s4
    title: "ImageNet Classification with Deep Convolutional Neural Networks"
    publisher: Advances in Neural Information Processing Systems 25 (NIPS 2012), Krizhevsky, Sutskever and Hinton
    url: https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s5
    title: "Dropout: A Simple Way to Prevent Neural Networks from Overfitting"
    publisher: Journal of Machine Learning Research 15(56), 1929-1958, 2014 (Srivastava, Hinton, Krizhevsky, Sutskever and Salakhutdinov)
    url: https://www.jmlr.org/papers/v15/srivastava14a.html
    type: peer-reviewed
    accessed: 2026-11-10
  - id: s6
    title: "Distilling the Knowledge in a Neural Network"
    publisher: arXiv:1503.02531 (Hinton, Vinyals and Dean), NIPS 2014 Deep Learning Workshop
    url: https://arxiv.org/abs/1503.02531
    type: primary
    accessed: 2026-11-10
created: 2026-11-10
---

# Geoffrey Hinton

Geoffrey Everest Hinton (born 6 December 1947 in London) is a British-Canadian cognitive psychologist and computer scientist, often called the "godfather of AI" for his long advocacy of learning in artificial neural networks.[^s2] He is a University Professor Emeritus of computer science at the University of Toronto, and his group there produced deep learning results that transformed speech recognition and object classification.[^s1] He was a joint recipient of the 2018 ACM A.M. Turing Award, and in 2024 he shared the Nobel Prize in Physics with John Hopfield.[^s2][^s3]

## Career

Hinton earned a BA in experimental psychology at Cambridge in 1970 and a PhD in artificial intelligence at Edinburgh in 1978, then held postdoctoral posts at Sussex and UC San Diego before five years on the computer science faculty at Carnegie Mellon.[^s1] Britannica reports that he moved to Canada in 1987, partly because he objected to US military funding of AI research.[^s2] He set up the Gatsby Computational Neuroscience Unit at University College London (1998–2001), returned to Toronto, and directed CIFAR's Neural Computation and Adaptive Perception program from 2004 to 2013.[^s1] From 2013 to 2023 he worked half-time at Google, becoming a vice president and engineering fellow, after Google bought the small company he had formed with two students.[^s1][^s2]

## Key contributions

- **Backpropagation (1986).** With David Rumelhart and Ronald Williams he published the paper that popularised training multilayer networks by propagating error gradients backward; his own bio also credits him as the first to use it to learn word embeddings.[^s1][^s2]
- **Boltzmann machines.** Building on Hopfield's associative network and borrowing tools from statistical physics, the Boltzmann machine learns the characteristic features of a class of data and can then classify inputs or generate new examples; the Nobel committee cited this work.[^s3]
- **Distributed representations and probabilistic models.** His bio lists contributions to distributed representations, time-delay neural networks, mixtures of experts, variational learning, products of experts and deep belief nets.[^s1]
- **AlexNet (2012).** With Alex Krizhevsky and Ilya Sutskever he trained a 60-million-parameter, eight-layer convolutional network on GPUs, reporting 18.9% top-5 test error on ImageNet; Britannica says it beat the next most accurate program by more than 40 percent.[^s4][^s2]
- **Dropout (2014).** Randomly removing units during training, so the network behaves like an average of many thinned networks, became a standard regulariser.[^s5]
- **Knowledge distillation (2015).** With Oriol Vinyals and Jeff Dean he showed how to compress an ensemble's knowledge into a single smaller model by training on its softened outputs.[^s6]

## Recognition

Besides the Turing Award, Britannica lists the first David E. Rumelhart Prize (2001), the Gerhard Herzberg Canada Gold Medal (2010) and the Royal Society's Royal Medal (2022).[^s2] He is a Fellow of the Royal Society and of the Royal Society of Canada, and a foreign member of the US National Academies of Engineering and Sciences.[^s1] The 2024 Nobel Prize in Physics, worth 11 million Swedish kronor split equally with Hopfield, was awarded for foundational discoveries that enable machine learning with artificial neural networks.[^s3]

## Views on AI risk

In May 2023 Hinton left Google so that he could speak freely about the dangers of AI.[^s2] As summarised by Britannica, his concerns include AI-generated fake content, disruption of the job market and the longer-term possibility that AI systems escape human control; he has said he does not wholly regret his life's work.[^s2]

## Assessment

Hinton's influence runs through both the scientific and the institutional history of deep learning. Scientifically, the Nobel committee credits his Boltzmann machine work with helping launch the current rapid growth of machine learning, and techniques from his groups such as dropout and distillation remain everyday tools for training and compressing networks.[^s3][^s5][^s6] Institutionally, his Toronto group and the CIFAR program he led trained many of the researchers behind the 2012-era breakthroughs, and his company's acquisition brought that group into Google.[^s1][^s2] Credit for backpropagation is shared with his 1986 co-authors, Rumelhart and Williams.[^s2]

## Connections

Hinton is placed under **deep learning** and **connectionism**, the research programmes he helped build.[^s1] He is linked to **backpropagation**, **Boltzmann machines** and **deep belief networks** as their co-inventor or developer, to **ImageNet and AlexNet** through the 2012 paper, and to **dropout** and **knowledge distillation**, whose articles already list him as creator.[^s3][^s4][^s5][^s6] His Nobel recognition also ties him to **John Hopfield**, whose associative network the Boltzmann machine built on.[^s3]

## Sources
[^s1]: University of Toronto Department of Computer Science, "Geoffrey E. Hinton's Biographical Sketch". https://www.cs.toronto.edu/~hinton/bio.html (accessed 2026-11-10)
[^s2]: Encyclopaedia Britannica, "Geoffrey Hinton". https://britannica.com/biography/Geoffrey-Hinton (accessed 2026-11-10)
[^s3]: The Royal Swedish Academy of Sciences, "Press release: The Nobel Prize in Physics 2024", https://www.nobelprize.org/prizes/physics/2024/press-release/ (accessed 2026-11-10)
[^s4]: A. Krizhevsky, I. Sutskever and G. E. Hinton, "ImageNet Classification with Deep Convolutional Neural Networks", NIPS 2012. https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html (accessed 2026-11-10)
[^s5]: N. Srivastava, G. Hinton, A. Krizhevsky, I. Sutskever and R. Salakhutdinov, "Dropout: A Simple Way to Prevent Neural Networks from Overfitting", JMLR 15(56), 2014. https://www.jmlr.org/papers/v15/srivastava14a.html (accessed 2026-11-10)
[^s6]: G. Hinton, O. Vinyals and J. Dean, "Distilling the Knowledge in a Neural Network", arXiv:1503.02531, 2015. https://arxiv.org/abs/1503.02531 (accessed 2026-11-10)
