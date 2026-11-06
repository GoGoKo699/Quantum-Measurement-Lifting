# Converse for arbitrary causal processors

Fix diagonal sector projectors $E_a$ of a nontrivial rank partition and unknown projectors $P_a(U)=UE_aU^\dagger$, with $U\in U(d)$. The desired accepted instrument is the one in the [model](model.md). Knowing the rank partition is allowed in this converse.

## Each resolved call contributes one unknown bra

Choose oracle Kraus operators $B_j(U)=|f(j)\rangle\langle u_j|$. Resolve all hidden oracle labels, known-operation Kraus indices and discarded final memory in a successful history $h$. A history with $n\le N$ calls has a data-to-output matrix $K_h(Z)$ polynomial of degree at most $n$ in $Z=\overline U$. Every call contributes one bra, and all other contracted tensors are independent of $U$.

Classical adaptation chooses which known tensors occur along a resolved history; it does not make their coefficients unknown functions of $U$. The statement is not restricted to parallel circuits. A finite-slot causal processor with finite exposed input/output systems has a finite-dimensional positive comb representation. Factoring it gives finite Kraus tensors and the same polynomial contractions, even when a particular implementation uses continuous classical records. Equivalently, unused slots may be filled with discarded dummy calls to use a common budget. The standard finite-slot representation is background from quantum-network theory, cited in [related work](../references/RELATED_WORK.md).

## Exactness constrains every positive contribution

For an accepted label $a$, complete-map exactness gives

```math
\sum_h\operatorname{vec}(K_h(U))\operatorname{vec}(K_h(U))^\dagger
=p(U)\operatorname{vec}(P_a(U))\operatorname{vec}(P_a(U))^\dagger.
```

The right side has rank at most one. For any vector orthogonal to $\operatorname{vec}(P_a)$, its quadratic form on the left is a sum of nonnegative squared overlaps, so every overlap must vanish. Thus each history satisfies $K_h(U)=c_h(U)P_a(U)$, also at points where the accepted map vanishes.

Because $r_a=\operatorname{Tr}P_a$ is fixed and positive, the proportionality scalar can be chosen as the polynomial

```math
c_h(Z)=\frac{\operatorname{Tr}K_h(Z)}{r_a}.
```

This step controls its degree. No assumption that the success probability is constant on the unitary orbit is needed.

## Complexifying the identity

Put $T=Z^T$. On the unitary group, $T=U^\dagger$ and $P_a=T^{-1}E_aT$. Therefore

```math
\det(T)K_h(Z)=c_h(Z)\operatorname{adj}(T)E_aT. \tag{1}
```

Both sides are polynomial matrices in the entries of $T$. To extend (1) beyond unitaries, take a real basis $H_1,\ldots,H_{d^2}$ of Hermitian matrices; it is also a complex basis of all matrices. A complex polynomial vanishing on unitaries makes

```math
F\!\left(\exp\!\left(i\sum_j z_jH_j\right)\right)
```

vanish for real $z$ near zero. Repeated application of the one-variable holomorphic identity theorem extends this to complex $z$ near zero. The exponential parametrization has invertible complex derivative at zero, so its image contains a complex-open neighborhood of identity. The polynomial is consequently identically zero. This is the Zariski-density fact needed here, with its reasoning supplied rather than assumed from the textbook.

## Why a determinant factor is unavoidable

The generic determinant is irreducible in the polynomial ring $\mathbb C[T_{ij}]$. One proof uses the rank-deficient variety: every matrix of rank at most $d-1$ factors as $AB$ with inner dimension $d-1$, so this variety is the closure of a polynomial image of an irreducible affine space and is irreducible. Its determinant has multiplicity one, because its gradient has a nonzero cofactor at a rank-$d-1$ point. Thus the determinant polynomial is irreducible; in this unique-factorization ring it is prime.

For $0<r_a<d$, some entry of $F_a(T)=\operatorname{adj}(T)E_aT$ is not divisible by $\det T$. Choose one coordinate inside sector $a$ and one outside. Put the block

```math
T_{\{i,j\}}=\begin{pmatrix}1&1\\1&1\end{pmatrix}
```

on these coordinates and the identity elsewhere. It has determinant zero, while the corresponding block of $F_a(T)$ is

```math
\begin{pmatrix}1&1\\-1&-1\end{pmatrix}\ne0.
```

Select a nonzero entry at this singular witness. Equation (1) and primality force $\det T$ to divide $c_h(Z)$. But the determinant has total degree $d$, whereas $\deg c_h\le n$. If $n<d$, then $c_h=0$ and $K_h=0$.

All accepted histories therefore vanish when $N<d$. Together with the [parallel construction](construction.md), this proves the exact onset $N_{\min}=d$. Every binary partition has an inside and outside coordinate, so reporting just one classical bit does not weaken the lower bound. A one-outcome PVM is excluded: then $E_a=I$ and $F_a(T)=\det(T)I$, so the singular witness disappears, consistently with its zero-query identity target.

This is an exact polynomial obstruction. Small-matrix witness checks validate the displayed witness, not irreducibility or the universal statement. No lower bound for approximate lifting is inferred.
