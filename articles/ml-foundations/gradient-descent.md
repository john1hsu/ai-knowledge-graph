---
id: kt:gradient-descent
type: Algorithm
title: Gradient descent
aliases: [steepest descent, method of steepest descent, batch gradient descent, full-batch gradient descent]
domain: ml-foundations
summary: >-
  An iterative first-order optimization algorithm that minimizes a differentiable function by repeatedly moving the
  parameters a small step in the direction of the negative gradient, scaled by a step size (learning rate); it and its
  stochastic variants are the workhorse for training machine-learning models.
maturity: foundational
broader: [kt:mathematical-optimization, kt:machine-learning]
related: [kt:stochastic-gradient-descent, kt:backpropagation, kt:adam-optimizer, kt:supervised-learning, kt:regularization]
relations:
  - {predicate: createdBy, object: kt:augustin-louis-cauchy}
  - {predicate: dependsOn, object: kt:loss-function}
  - {predicate: alternativeTo, object: kt:newtons-method}
  - {predicate: usedIn, object: kt:deep-learning}
sources:
  - id: s1
    title: "12.3. Gradient Descent"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), d2l.ai
    url: https://d2l.ai/chapter_optimization/gd.html
    type: textbook
    accessed: 2026-11-16
  - id: s2
    title: "General method for the solution of systems of simultaneous equations (Méthode générale pour la résolution des systèmes d'équations simultanées)"
    publisher: Comptes Rendus de l'Académie des Sciences 25, 536–538 (1847) (Cauchy); English translation by R. J. Pulskamp, hosted at Royal Holloway, University of London
    url: https://gtfp.cs.rhul.ac.uk/pulskamp/Cauchy/Orbits/1847%20CR%20536%28383%29.pdf
    type: primary
    accessed: 2026-11-16
  - id: s3
    title: "A Stochastic Approximation Method"
    publisher: The Annals of Mathematical Statistics 22(3), 400–407 (1951) (Robbins and Monro); copy hosted by Columbia University
    url: https://www.columbia.edu/~ww2040/8100F16/RM51.pdf
    type: peer-reviewed
    accessed: 2026-11-16
  - id: s4
    title: "Lecture 1: Gradient Descent (10-725/36-725 Convex Optimization, Fall 2016, scribed notes)"
    publisher: Carnegie Mellon University (Ryan Tibshirani)
    url: https://www.stat.cmu.edu/~ryantibs/convexopt-F16/scribes/grad-descent-scribed.pdf
    type: academic
    accessed: 2026-11-16
  - id: s5
    title: "Optimization Methods for Large-Scale Machine Learning"
    publisher: Bottou, Curtis and Nocedal, arXiv:1606.04838
    url: https://arxiv.org/abs/1606.04838v2
    type: primary
    accessed: 2026-11-16
created: 2026-11-16
---

# Gradient descent

Gradient descent is a first-order iterative method for minimizing a differentiable function f. Starting from an initial guess x, it repeatedly applies the update x ← x − η∇f(x), where ∇f(x) is the gradient and η > 0 is the step size, called the learning rate in machine learning. The justification is a first-order Taylor expansion: for a small enough step, moving against the gradient is guaranteed to lower f. The loop stops when the gradient becomes small or after a fixed budget of iterations.[^s1] In machine learning, f is a training loss averaged over a dataset and x is the vector of model parameters, so "training" a model is, for most methods, running some form of this loop.[^s5]

## Origin

The method is usually credited to Augustin-Louis Cauchy, who described it in a three-page 1847 note to the French Academy of Sciences. To find where a nonnegative function u of several variables vanishes, he computed its partial derivatives, shifted each variable by a positive multiple θ of the negative derivative, and enlarged θ until u stopped decreasing, then repeated. He reduced a whole system of equations to this case by minimizing the sum of their squares, and noted that Newton's method could refine the answer once it was close; his intended application was computing planetary orbits.[^s2] The stochastic version that dominates modern ML descends from Robbins and Monro's 1951 stochastic approximation method, which found the root of a function observable only through noisy measurements using steps a_n that shrink over time, for example in proportion to 1/n.[^s3]

## How it works

The learning rate controls everything. In the d2l.ai worked example on f(x) = x², a rate of 0.05 is still far from the optimum after 10 steps, 0.2 gets close, and 1.1 overshoots so badly that the iterate diverges to about 61.9.[^s1] On a two-variable quadratic such as x₁² + 2x₂², the path heads steadily toward the minimum but slowly, because one fixed rate must suit directions of very different curvature.[^s1]

For convex problems the behavior is well understood. If f is convex and its gradient is L-Lipschitz (L-smooth), a fixed step t < 1/L gives f(x⁽ᵏ⁾) − f* ≤ ‖x⁽⁰⁾ − x*‖² / (2tk), an O(1/k) rate, so reaching accuracy ε takes O(1/ε) iterations. If f is also strongly convex the error shrinks geometrically (linear convergence), at a rate that worsens as the condition number L/m grows. Backtracking line search, which shrinks a trial step until a sufficient-decrease test passes, achieves these rates without knowing L.[^s4]

## Limitations and variants

On nonconvex functions, which include virtually all neural-network losses, gradient descent offers no guarantee of a global minimum and can settle in a poor local minimum; an overly large learning rate makes this more likely.[^s1] It is also slow on ill-conditioned problems. Second-order methods such as Newton's method rescale the step by the inverse Hessian and converge very fast near an optimum, but storing and inverting a d × d Hessian is impractical for deep networks; cheaper preconditioning, such as using only the Hessian's diagonal to give each coordinate its own effective rate, is a middle ground. Exact line search is likewise too costly when every function evaluation means a pass over the full dataset.[^s1]

That last cost is why practice moved to stochastic gradients. Bottou, Curtis and Nocedal argue that large-scale ML is a distinct optimization setting in which the stochastic gradient method, which estimates the gradient from a single example or a small mini-batch, has long played the central role, while conventional deterministic nonlinear methods tend to struggle.[^s5] They identify two main directions for improving on plain stochastic gradient: reducing the noise in the search direction and exploiting approximate second-order information.[^s5]

## In practice

Full-batch gradient descent is mostly a teaching and analysis tool; production training uses mini-batch stochastic gradient descent or adaptive descendants such as Adam, with gradients computed by backpropagation and learning rates set by schedules or tuning.[^s5][^s1] The convex theory still guides intuition about step sizes, conditioning and stopping rules.[^s4]

## Connections

Gradient descent is a core algorithm of **mathematical optimization** and of **machine learning** (broader). It minimizes a **loss function** (*dependsOn*), which in **supervised learning** measures error on labeled data and may include a **regularization** penalty.[^s5] Its noisy mini-batch form, **stochastic gradient descent**, traces to Robbins and Monro,[^s3] and the **Adam optimizer** adapts its step per coordinate. In neural networks the gradient itself comes from **backpropagation**, which is why the pair underlies **deep learning** (*usedIn*).[^s1] **Newton's method** is the classic second-order *alternative*, already mentioned by Cauchy as a finishing step,[^s2] and the method itself was *created by* **Augustin-Louis Cauchy**.[^s2]

## Sources
[^s1]: Zhang, Lipton, Li and Smola, "12.3. Gradient Descent", *Dive into Deep Learning*. https://d2l.ai/chapter_optimization/gd.html (accessed 2026-11-16)
[^s2]: Cauchy, "Méthode générale pour la résolution des systèmes d'équations simultanées", *Comptes Rendus* 25, 536–538, 1847; trans. R. J. Pulskamp. https://gtfp.cs.rhul.ac.uk/pulskamp/Cauchy/Orbits/1847%20CR%20536%28383%29.pdf (accessed 2026-11-16)
[^s3]: Robbins and Monro, "A Stochastic Approximation Method", *The Annals of Mathematical Statistics* 22(3), 400–407, 1951. https://www.columbia.edu/~ww2040/8100F16/RM51.pdf (accessed 2026-11-16)
[^s4]: Tibshirani, "Lecture 1: Gradient Descent", 10-725/36-725 Convex Optimization, Carnegie Mellon University, Fall 2016 (scribed notes). https://www.stat.cmu.edu/~ryantibs/convexopt-F16/scribes/grad-descent-scribed.pdf (accessed 2026-11-16)
[^s5]: Bottou, Curtis and Nocedal, "Optimization Methods for Large-Scale Machine Learning", arXiv:1606.04838. https://arxiv.org/abs/1606.04838v2 (accessed 2026-11-16)
