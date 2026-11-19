---
id: kt:mathematical-optimization
type: Field
title: Mathematical optimization
aliases: [optimization, mathematical programming, numerical optimization]
domain: ml-foundations
summary: >-
  The branch of applied mathematics concerned with choosing values of decision variables that minimize or maximize an
  objective function, usually subject to constraints; it supplies the problem formulation and the algorithms (gradient
  methods, linear and convex programming) that underlie training machine-learning models.
maturity: foundational
broader: [kt:applied-mathematics]
related: [kt:machine-learning, kt:loss-function, kt:gradient-descent, kt:stochastic-gradient-descent, kt:regularization, kt:overfitting, kt:statistical-learning-theory]
relations:
  - {predicate: hasPart, object: kt:convex-optimization}
  - {predicate: hasPart, object: kt:linear-programming}
  - {predicate: enables, object: kt:empirical-risk-minimization}
sources:
  - id: s1
    title: "Optimization (mathematics)"
    publisher: Encyclopaedia Britannica
    url: https://britannica.com/science/optimization
    type: encyclopedia
    accessed: 2026-11-19
  - id: s2
    title: "EE364a Convex Optimization I — Lecture 1: Introduction"
    publisher: Stanford University (Stephen Boyd), course slides
    url: https://web.stanford.edu/class/ee364a/lectures/intro.pdf
    type: academic
    accessed: 2026-11-19
  - id: s3
    title: "Optimization Methods for Large-Scale Machine Learning"
    publisher: SIAM Review 60(2), 223–311, 2018 (Bottou, Curtis and Nocedal), authors' copy
    url: https://leon.bottou.org/publications/pdf/sirev-2018.pdf
    type: peer-reviewed
    accessed: 2026-11-19
  - id: s4
    title: "12.1. Optimization and Deep Learning"
    publisher: Dive into Deep Learning (Zhang, Lipton, Li and Smola), d2l.ai
    url: https://d2l.ai/chapter_optimization/optimization-intro.html
    type: textbook
    accessed: 2026-11-19
created: 2026-11-19
---

# Mathematical optimization

Mathematical optimization is the body of principles and methods for solving quantitative problems by picking the best values of some adjustable quantities. Britannica describes every optimization problem as having three parts: an objective function that yields a single number to maximize or minimize (profit, cost, travel time), decision variables that can be changed, and constraints that limit those variables, such as available resources or non-negativity. The older synonym "mathematical programming" was coined in the 1940s, when "programming" meant planning rather than writing code.[^s1]

## Standard form

Stanford's convex-optimization course writes the general problem as: minimize f₀(x) over a vector x ∈ ℝⁿ, subject to inequality constraints fᵢ(x) ≤ 0 for i = 1…m and equality constraints gᵢ(x) = 0 for i = 1…p. Maximization is handled by minimizing the negated objective, and multi-objective variants exist.[^s2] The problem is **convex** when the objective and inequality-constraint functions are convex and the equality constraints are linear (Ax = b). The course summarizes the practical consequence bluntly: problems with nonnegative curvature are easy, while nonconvex problems with negative curvature are hard.[^s2]

## Main branches

Classical taxonomy splits the field by the form of the functions and variables. In **linear programming** the objective and constraints are linear in real-valued variables; in **nonlinear programming** at least one of them is nonlinear. Britannica also lists stochastic programming, network optimization and combinatorial optimization as distinct classes.[^s1] Within nonlinear problems, the Stanford slides distinguish *local methods*, which scale to very large problems such as neural-network training but need an initial guess, often need tuning, and say nothing about how far the answer is from the true optimum, from *global methods*, whose worst-case cost grows exponentially with problem size.[^s2]

## History

Joseph Fourier appears to have seen the potential of linear inequality systems as early as 1823, and Leonid Kantorovich's 1939 monograph on planning production is credited as the first treatise to recognize the mathematical structure of such scheduling problems, though it went largely unnoticed for two decades. Work for the U.S. Air Force from 1947 produced the simplex method, John von Neumann connected linear programs to matrix games and introduced duality, and by 1951 the simplex method was running on the National Bureau of Standards' SEAC computer.[^s1] The Stanford course dates convex analysis to roughly 1900–1970, ellipsoid and subgradient methods to the 1970s, and interior-point methods to the 1980s–90s (Karmarkar; Nesterov and Nemirovski); it notes that applications moved from operations research before 1990 into engineering and, from the 2000s, into machine learning, statistics and finance.[^s2]

## Optimization in machine learning

Learning a model is naturally posed as an optimization problem: the variables are model parameters and the objective combines prediction error on observed data with a regularization term that penalizes complexity.[^s2] Bottou, Curtis and Nocedal stress how this differs from classical optimization. The quantity one actually cares about is the expected risk over an unknown data distribution, which cannot be computed; practitioners instead minimize the empirical risk, the average loss over a training sample, and driving that training loss as low as possible can produce memorization rather than generalization. Early stopping therefore acts as a form of regularization, and an optimizer need not run to convergence.[^s3] The d2l.ai textbook makes the same point: optimization reduces training error, whereas deep learning cares about generalization error, and the minimizer of the empirical risk may differ from that of the true risk.[^s4]

The scale of modern datasets also changes which algorithms win. Stochastic gradient methods cost the same per step regardless of dataset size and exploit redundancy across examples, so in the authors' logistic-regression experiment they made far faster early progress than the quasi-Newton method L-BFGS. For strongly convex problems they show stochastic gradient's total work to reach a given accuracy is independent of the number of examples, while full-batch gradient descent's grows with it. Their survey frames noise-reduction and second-order approximations as the main routes to improving on plain stochastic gradient.[^s3]

## Limitations and open questions

Deep-network objectives are nonconvex, so classical guarantees rarely apply. The d2l.ai authors list three recurring difficulties: many local minima; saddle points, where the gradient vanishes but the Hessian has eigenvalues of mixed sign, and which become more common than local minima in high dimensions; and vanishing gradients, where a saturating activation such as tanh leaves the gradient near 0.0013 at an input of 4 and training stalls. Minibatch noise, ReLU activations, careful initialization and reparametrization all help in practice.[^s4] Why local methods find solutions that generalize so well in such landscapes remains an active research question.[^s3]

## Connections

Mathematical optimization is a branch of `kt:applied-mathematics` and has `kt:convex-optimization` and `kt:linear-programming` as major subfields.[^s1][^s2] In machine learning it is what makes `kt:empirical-risk-minimization` operational: a `kt:loss-function` supplies the objective and `kt:regularization` the complexity penalty.[^s2][^s3] `kt:gradient-descent` and `kt:stochastic-gradient-descent` are the local methods that dominate large-scale training.[^s3] Its relationship with `kt:overfitting` is one of tension, since minimizing training loss too aggressively works against generalization, the concern formalized in `kt:statistical-learning-theory`; together these place the field at the core of `kt:machine-learning`.[^s3][^s4]

## Sources
[^s1]: Encyclopaedia Britannica, "Optimization (mathematics)". https://britannica.com/science/optimization (accessed 2026-11-19)
[^s2]: S. Boyd, EE364a Convex Optimization I, Lecture 1: Introduction, Stanford University. https://web.stanford.edu/class/ee364a/lectures/intro.pdf (accessed 2026-11-19)
[^s3]: L. Bottou, F. E. Curtis and J. Nocedal, "Optimization Methods for Large-Scale Machine Learning", SIAM Review 60(2):223–311, 2018. https://leon.bottou.org/publications/pdf/sirev-2018.pdf (accessed 2026-11-19)
[^s4]: A. Zhang, Z. C. Lipton, M. Li and A. J. Smola, "12.1. Optimization and Deep Learning", Dive into Deep Learning. https://d2l.ai/chapter_optimization/optimization-intro.html (accessed 2026-11-19)
