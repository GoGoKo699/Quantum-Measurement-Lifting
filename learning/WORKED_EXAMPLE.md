# Two calls, one retained quantum output

## What the detector withholds

An unknown qubit PVM has two basis vectors $u_0,u_1$ and effects $P_a=|u_a\rangle\langle u_a|$. A destructive call reports $a$ but returns no qubit. Knowing the label does not supply the unknown vector needed to prepare the canonical output. For higher-rank effects, preparing a fixed state after a label would also erase information within the measured sector.

The lifting protocol keeps an output register from the beginning. The desired state does not reappear from the detector's classical wire.

## An explicit qubit preparation

Use query qubits $Q_1,Q_2$, retained qubit $B$ and a two-level control $C$. Define the known singlet

```math
|\epsilon_2\rangle=(|01\rangle-|10\rangle)/\sqrt2.
```

For an arbitrary data state $|\psi\rangle$, the routing isometry prepares

```math
V|\psi\rangle
=\frac1{\sqrt2}\left(
-|1\rangle_C|\psi\rangle_{Q_1}|\epsilon_2\rangle_{Q_2B}
+|2\rangle_C|\epsilon_2\rangle_{Q_1B}|\psi\rangle_{Q_2}
\right).
```

The labels 1 and 2 name two orthogonal control states. The relative minus sign is part of the known circuit. Both terms contain the data once; the control makes their coherent routing an isometry.

Measure both query qubits destructively. For reports $(a_1,a_2)$, set $R=\max_a n_a$. When the reports differ, $R=1$, and the accepted control bras are the individual position bras associated with the reported outcomes. When reports agree, the valid symmetric control bra has a factor $1/\sqrt2$; the corresponding hidden-history amplitude cancels, so this branch never accepts.

## Where the probability comes from

There are four hidden fine histories: $(0,0),(0,1),(1,0),(1,1)$. The repeated histories vanish. For either distinct history, the general contraction in [construction](../science/construction.md) gives

```math
K_{\mathbf j,a}=\frac{\det A}{2}P_a,
\qquad |\det A|=1.
```

The two environment histories are summed as maps. Therefore

```math
\mathcal S_{P,a}(\rho)=\frac12P_a\rho P_a,
\qquad
\Pr(\mathrm{success})=\frac12.
```

For input $|\psi\rangle=\alpha|u_0\rangle+\beta|u_1\rangle$, accepted labels have unnormalized probabilities $|\alpha|^2/2$ and $|\beta|^2/2$. Conditioning on success gives the original Born distribution. The fixed-normalization choice $R=2$ instead succeeds with probability $1/4$.

## Why the degenerate case is a stronger test

Now take dimension four with two rank-two sectors:

```math
P_0=|u_1\rangle\langle u_1|+|u_2\rangle\langle u_2|,
\qquad
P_1=|u_3\rangle\langle u_3|+|u_4\rangle\langle u_4|.
```

The detector still reports one bit. The construction uses four calls, and its count-based filter succeeds with probability $1/(4\cdot2)=1/8$. On the data-reference state

```math
|\Psi\rangle_{DR}
=\frac{|u_1\rangle_D|0\rangle_R+|u_2\rangle_D|1\rangle_R}{\sqrt2},
```

accepted outcome 0 returns exactly $|\Psi\rangle$ after normalization. A fine-basis measurement followed by forgetting whether it saw $u_1$ or $u_2$ would instead return a mixture of the two product states. It would reproduce the coarse classical label but destroy the off-diagonal coherence and entanglement. The accepted Kraus matrix being proportional to $P_0$, rather than separate rank-one projectors, is therefore essential.

## How the examples fit the theorem

Two and four are the exact onset call counts for these dimensions, not merely the sizes of convenient constructions. The [converse](../science/converse.md) rules out fewer calls even with adaptive processing. The examples do not establish that $1/2$ or $1/8$ are optimal success probabilities.

Failure may destroy the unknown data. Fresh-input retries and a guarantee on one irreplaceable input are different tasks. The [resource account](../science/boundaries.md) keeps that distinction explicit.
