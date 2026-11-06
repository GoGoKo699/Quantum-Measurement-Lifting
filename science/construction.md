# Exact antisymmetric lifting

## Known preparation and coherent routing

Prepare the normalized $d$-qudit state

```math
|\epsilon_d\rangle
=\frac1{\sqrt{d!}}\sum_{\pi\in S_d}\operatorname{sgn}(\pi)
|\pi(1),\ldots,\pi(d)\rangle.
```

Use query registers $Q_1,\ldots,Q_d$, one retained output $B$, and a $d$-level routing control $C$. In branch $k$, put the data into $Q_k$ and the singlet into the ordered registers $(Q_1,\ldots,Q_{k-1},Q_{k+1},\ldots,Q_d,B)$. Include the known phase $(-1)^{d-k}$ and call this isometry $W_k$. Prepare

```math
V=\frac1{\sqrt d}\sum_{k=1}^d|k\rangle_C\otimes W_k.
```

Each $W_k$ is an isometry. Orthogonality of the control labels gives $V^\dagger V=I$, regardless of overlap between their query-register embeddings. A known singlet preparation, a uniform control state and controlled register permutations implement this step. It routes one input coherently; it does not clone it.

Apply the supplied destructive channel once to every query port. These are $d$ ordinary calls, which can be parallel. There is no controlled use of an unknown channel and no indefinite causal order. The control and output are retained.

## A valid filter from classical reports

Let the observed labels be $a_1,\ldots,a_d$, and let $n_a$ count occurrences of label $a$. Choose either $R=d$ or $R=\max_a n_a$. On the routing control apply the successful Kraus bras

```math
L_a=\frac1{\sqrt R}\sum_{k:a_k=a}\langle k|.
```

For fixed reports, the groups of control positions are disjoint. The successful effect has a nonzero eigenvalue $n_a/R$ on the uniform vector of each group and zero on its orthogonal complement. Consequently

```math
\sum_a L_a^\dagger L_a\preceq I_C.
```

The square root of the remaining effect supplies a valid failure branch. Both choices of $R$ are physical for every possible report, including reports that will ultimately cancel. Empty groups contribute the zero bra.

## Resolving the inaccessible environment for the proof

Choose any orthonormal basis $u_1,\ldots,u_d$ refining the projectors and write $f(j)=a$ for its sector. The channel has Kraus operators $|f(j)\rangle\langle u_j|$. The fine index $j$ is a mathematical environment label, not information available to the processor.

For one hidden history $\mathbf j=(j_1,\ldots,j_d)$, let $A$ have columns $\overline{u_{j_k}}$, and let $C(A)$ be the cofactor matrix. It is the transpose of the adjugate and satisfies

```math
C(A)A^T=\det(A)I.
```

This identity holds for singular matrices as well. Define $D_a$ as the diagonal indicator of query positions with coarse label $a$. Since $\langle u_{j_k}|P_a$ is either that same bra or zero,

```math
A^T P_a=D_aA^T.
```

Expanding the singlet permutations in routing branch $k$ gives the outer product of the $k$th cofactor column with the $k$th row of $A^T$, divided by $\sqrt{d\,d!}$. The routing phase above supplies precisely the cofactor sign. Applying the control bra therefore gives

```math
\begin{aligned}
K_{\mathbf j,a}
&=\frac{C(A)D_aA^T}{\sqrt{d\,d!\,R}}\\
&=\frac{\det(A)}{\sqrt{d\,d!\,R}}P_a.
\end{aligned}
```

The entire data-to-output matrix is proportional to the full projector. No fine-basis dephasing remains in the accepted branch.

## Summing probabilities, not hidden amplitudes

Repeated fine indices make $\det A=0$, so their individual accepted Kraus matrices vanish. Distinct fine indices form one of $d!$ permutations of the complete basis; each has $|\det A|=1$. Environment histories must be summed as completely positive contributions, not coherently with one another.

With $R=d$, every surviving history has the same normalization. Summing their squared amplitudes yields

```math
\mathcal S_{P,a}(\rho)=\frac1{d^2}P_a\rho P_a.
```

With $R=\max_a n_a$, every surviving history contains each basis vector once. Its coarse counts equal the unknown ranks, so $R=r_{\max}(P)$ on those histories. The same sum gives

```math
\mathcal S_{P,a}(\rho)=\frac1{d\,r_{\max}(P)}P_a\rho P_a.
```

The rule uses observed counts and never needs supplied ranks or a separate estimation stage. It is valid even on nonsurviving histories. The success coefficient is common to all outcomes, so conditioning on success does not distort their relative Born probabilities.

## Physical meaning and checks

Coherent interference occurs among routing positions inside a fixed hidden history. It does not require access to, or interference between, distinct environment records. The surviving records differ only by a scalar multiplying the same projector map. That distinction explains why a destructive device can still supply the canonical quantum instrument probabilistically.

The [worked examples](../learning/WORKED_EXAMPLE.md) show two calls on a qubit and a four-dimensional degenerate sector. The [full-channel test](../verification/check_full_channel.py) constructs $V$ directly from singlet amplitudes, rather than assuming the cofactor identity, then checks all hidden histories and complete Choi maps in small dimensions. Resource and failure costs are in [boundaries](boundaries.md).
