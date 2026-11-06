# Watrous-to-project bridge

The sole educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) supplies chapter manuscripts and errata. Section numbers below were checked against its contents and Chapter 2. The online manuscript is a pre-publication copy; no textbook file is redistributed here.

## Focused reading

| Watrous location | Use in this project | Local bridge |
|---|---|---|
| Sections 1.1.1–1.1.3 | Tensor spaces, positive operators, decompositions and norms | [Model and conventions](../science/model.md) |
| Sections 2.1.2–2.1.3 | Density matrices, reduced states and purification | [Reference-preserving example](WORKED_EXAMPLE.md) |
| Sections 2.2.1–2.2.2, especially Theorem 2.22 | Complete positivity; Choi, Kraus and dilation representations | [Accepted maps](../science/model.md) and [converse](../science/converse.md) |
| Sections 2.3.1–2.3.2 | Measurement effects and their channel representation; nondestructive measurements and instruments | [Destructive versus quantum output](WORKED_EXAMPLE.md) |
| Section 3.3.2, optional | Why a reference-sensitive norm is appropriate when an approximate problem is later posed | [Limits of the exact theorem](../science/boundaries.md) |
| Section 7.1, optional | Permutation actions on tensor powers | The alternating-sign state is constructed directly in [construction](../science/construction.md) |

Section 7.1 studies permutation invariance, not this lifting protocol. The antisymmetric state changes by the permutation sign rather than remaining invariant; that distinction is supplied locally. The optional channel-distance section does not turn our exact converse into an approximation theorem.

## Convention dictionary

Watrous writes the adjoint as $A^*$. Here it is $A^\dagger$; $\overline A$ means entrywise conjugation and $A^T$ means transpose. A measurement effect denoted $\mu(a)$ in the textbook is $P_a$ for a PVM or $E_a$ for a general POVM here. A textbook instrument component $\Phi_a$ becomes the accepted map $\mathcal S_{P,a}$, including its success weight.

Our output-first vectorization agrees with the tensor ordering in the textbook's Choi representation:

```math
\operatorname{vec}(A)=\sum_{b,x}A_{bx}|b\rangle|x\rangle,
\qquad
J(A\,\cdot\,A^\dagger)=\operatorname{vec}(A)\operatorname{vec}(A)^\dagger.
```

There is no $1/d$ normalization in $J$. The normalized maximally entangled input would produce $J/d$ instead. In particular, a rank-$r_a$ projector has vectorization norm squared $r_a$, while its one-Kraus map has Choi rank one. Projector rank and Choi rank answer different questions.

## The missing steps, supplied by the project

First, an effect specifies probabilities but not a unique physical instrument. We deliberately choose the canonical Lüders component and demand equality before normalization. This makes reference preservation and input-independent success explicit.

Second, the routing control creates a sum of amplitudes inside each hidden oracle history. The environment histories themselves remain an incoherent Kraus sum. Expanding the known singlet produces cofactors; their cancellation yields the entire projector, not fine-basis dephasing.

Third, Choi positivity makes exactness a branchwise constraint. Destructive oracle bras then make each fine-history matrix polynomial in conjugated unknown-basis entries. The [converse](../science/converse.md) supplies the complexification and determinant-factor argument in full; these algebraic steps are not attributed to Watrous.

Finally, the [boundaries](../science/boundaries.md) use CP order to compare full-rank destructive channels. Identical input support cannot be converted into distinct pure accepted Choi supports by a finite queried processor. This distinguishes the sharp projective theorem from unsharp families without asserting an approximate impossibility.

Use the [milestone map](MILESTONES.md) to connect these bridges, rather than reading the book cover to cover.
