# Scope, resources and exactness

## Resources and failure

The explicit construction has $d$ query registers, one retained output and one routing control, each of dimension $d$. This is $d+2$ registers before the calls, including the routed data. A direct qubit encoding uses $(d+2)\lceil\log_2d\rceil$ qubits for these registers. Singlet synthesis, controlled permutations and implementation scratch space are additional known-operation costs; the displayed width is not an optimized fault-tolerant resource estimate. The classical record contains $d$ labels, each from the detector's finite alphabet.

There are exactly $d$ destructive calls per attempt. The attained probabilities are $1/d^2$ and $1/(d r_{\max})$. On independently supplied fresh inputs, repeating the same protocol until one success has mean call cost $d/p$: respectively $d^3$ and $d^2r_{\max}$. This accounting does not create a copy of a one-off unknown input. A failed attempt may destroy it, and there is no proved recovery of the failure branch.

For a $d=2^n$ input, the onset is exponential in $n$. The result is an exact interface-conversion theorem, not a scalable detector upgrade. Optimal success at a fixed budget, constant-success call complexity and efficient singlet/routing synthesis remain outside the established result.

## Full-rank unsharp effects: a different exact problem

Let $\{E_a(x)\}$ be POVMs on the same finite label set and input dimension, with every effect strictly positive. Their destructive channels have Choi matrices

```math
J(\mathcal M_x)=\sum_a|a\rangle\langle a|\otimes E_a(x)^T.
```

For any fixed pair $x,y$, positivity gives finite constants $c,C>0$ such that

```math
cJ(\mathcal M_y)\preceq J(\mathcal M_x)\preceq CJ(\mathcal M_y).
```

An $N$-slot accepted causal processor preserves completely positive order in each slot. Expand $\mathcal M_x=c\mathcal M_y+\Delta$ with $\Delta$ completely positive: every term in the multilinear expansion is completely positive, including the all-$\mathcal M_y$ term. Reversing the comparison gives, for each fixed accepted label,

```math
c^N J(\mathcal S_{y,a})\preceq J(\mathcal S_{x,a})
\preceq C^N J(\mathcal S_{y,a}).
```

Variable-call protocols can be padded with discarded dummy slots. Thus accepted branches at $x$ and $y$ have identical support, or both vanish. Exact canonical Lüders targets instead have Choi rays

```math
J(\mathcal S_{x,a})
=p(x)\operatorname{vec}(\sqrt{E_a(x)})
\operatorname{vec}(\sqrt{E_a(x)})^\dagger.
```

When these rays differ at two parameters, they cannot have identical nonzero support. No finite-call processor therefore realizes a nonzero exact universal canonical instrument on that family. This is a support argument, with the general positive-component principle credited to earlier channel-processing work in [related work](../references/RELATED_WORK.md).

For example, $E_0(x)=\operatorname{diag}(x,1-x)$ and $E_1(x)=I-E_0(x)$ have varying rays for $0<x<1$. Also, adding known strictly positive isotropic noise to an unknown nontrivial PVM generally makes its effects full rank and its canonical rays variable. Exact lifting then changes discontinuously from the projective case. This says nothing quantitative about small-error approximation.

The obstruction is not a claim about every isolated POVM. Effects proportional to fixed operators can have constant canonical rays; a known measurement can simply be implemented from its description. Approximate restoration by estimating a detector is also not excluded.

## Assumptions that cannot be dropped silently

The oracle is ideal, memoryless and identical across calls. Correlated environments, drift and unknown detector dynamics are not analyzed. The processor's known controls and state preparation are ideal. Ordinary destructive channel access is weaker than supplied coherent unitary, dilation or postmeasurement-system access; the query comparison does not identify those resources.

The canonical instrument is fixed by the effects. A real apparatus can share those effects yet have different back-action. Nothing here infers that hidden apparatus behavior from its classical reports.

## Interpreting the result

The surviving contribution is an exact conversion law under destructive access, with a threshold determined by input dimension even for a binary detector. Antisymmetric states, cofactor identities, Choi positivity, polynomial methods and CP-order support constraints are established tools. [Related work](../references/RELATED_WORK.md) distinguishes what those tools previously supplied from the target and guarantees proved here.
