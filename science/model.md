# Operational model and theorem

## Destructive input, quantum-output target

Let $d\ge2$ and let $P=\{P_a:a\in\mathcal A\}$ be a finite projective resolution of identity on $\mathbb C^d$. Zero outcomes may be removed. The supplied memoryless channel is

```math
\mathcal M_P(\rho)
=\sum_{a\in\mathcal A}\operatorname{Tr}(P_a\rho)
|a\rangle\langle a|.
```

Each ordinary call consumes its quantum input and returns only a classical label. The unknown basis, projector ranks, coherent dilation, inverse, environmental output and postmeasurement system are not supplied. No QRAM is assumed. All calls, including those in failed attempts, count.

The processor receives one arbitrary data register $D$, possibly entangled with an inaccessible reference $R$. Known quantum operations, finite-dimensional ancillary registers, coherent memory, measurements and causal classical adaptation are permitted. The count $N$ is a worst-case call budget, not an expected count conditioned on success.

For each accepted output label $a$, the unnormalized map must be

```math
\mathcal S_{P,a}(\rho)=p(P)P_a\rho P_a.
```

There is one common coefficient $p(P)>0$ for all labels and all inputs; it may depend on the unknown measurement. This equality is a completely positive map identity and hence also holds after tensoring with the identity on any reference. Its summed trace is $p(P)$ for every density matrix, because the projectors resolve identity. Conditional on success, the output is precisely the Lüders instrument.

This target is determined by the measurement effects. It does not identify a physical detector's inaccessible internal state-update mechanism.

## Exact query onset

**Theorem.** Fix any rank partition with at least two positive parts. Universal exact lifting over its complete unitary orbit requires $N\ge d$, even with arbitrary causal adaptation and coherent memory. A rank-oblivious parallel protocol uses $d$ ordinary calls and achieves

```math
p(P)=\frac{1}{d\,r_{\max}(P)},
\qquad
r_{\max}(P)=\max_a\operatorname{rank}P_a.
```

A fixed-normalization version instead achieves $p=1/d^2$ for every PVM. Thus $N_{\min}=d$ for every nontrivial fixed rank partition, including every binary partition. The lower bound still holds when the ranks are known; the construction does not require them. A one-outcome PVM is the identity instrument and needs zero calls.

The theorem is about the first possible nonzero exact success. It does not optimize the success probability or establish an approximate-error lower bound. [Construction](construction.md) and [converse](converse.md) give the two directions under the same access model.

## Matrix and Choi conventions

For a matrix $A$ from input to output, define

```math
\operatorname{vec}(A)=\sum_{b,x}A_{bx}|b\rangle\otimes|x\rangle,
\qquad
J(\Phi)=\sum_{x,y}\Phi(|x\rangle\langle y|)\otimes|x\rangle\langle y|.
```

Output is the first tensor factor. Choi matrices are unnormalized: a channel with $d$-dimensional input has Choi trace $d$. For a one-Kraus map, $J(A\,\cdot\,A^\dagger)=\operatorname{vec}(A)\operatorname{vec}(A)^\dagger$. Therefore an accepted Lüders branch has Choi rank one even if $P_a$ has rank greater than one. The branch Choi trace is $p(P)\operatorname{rank}P_a$, not the total success probability.

We use $A^\dagger$ for adjoint, $A^T$ for transpose and $\overline A$ for entrywise conjugation. These distinctions are essential in the cofactor proof. The [Watrous bridge](../learning/WATROUS_BRIDGE.md) gives the source-to-project dictionary.
