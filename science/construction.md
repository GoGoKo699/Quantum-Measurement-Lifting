# Exact antisymmetric lifting construction

Let
\[
|\epsilon_d\rangle=\frac1{\sqrt{d!}}\sum_{\pi\in S_d}\operatorname{sgn}(\pi)|\pi(1),\ldots,\pi(d)\rangle.
\]
Use \(d\) query registers \(Q_1,\ldots,Q_d\), one retained output \(B\), and a \(d\)-level control \(C\). In branch \(k\), put the data input into \(Q_k\) and the normalized antisymmetric state into the remaining \(d-1\) query registers and \(B\), with the ordering sign \((-1)^{d-k}\). Denote the isometry by \(W_k\). Prepare
\[
V=\frac1{\sqrt d}\sum_{k=1}^d|k\rangle_C W_k.
\]
Orthogonal control labels give \(V^\dagger V=I\). Query each \(Q_k\) once using an ordinary destructive measurement, in parallel. No controlled oracle or indefinite causal order is needed.

For reported coarse labels \(a_1,\ldots,a_d\), put \(n_a=|\{k:a_k=a\}|\). For each reported \(a\), accept by applying the control bra
\[
L_a=R^{-1/2}\sum_{k:a_k=a}\langle k|,
\]
where either \(R=d\) or \(R=\max_a n_a\). The sum of successful control effects has eigenvalues \(n_a/R\le1\) on mutually orthogonal label groups; the positive complement is the failure effect.

## Environment-resolved calculation

Choose an arbitrary orthonormal refinement \(\{u_j\}_{j=1}^d\) of the projectors and let \(f(j)\) denote the coarse label. The oracle's hidden Kraus bra for fine label \(j\) is \(\langle u_j|\). For a hidden history \(\mathbf j=(j_1,\ldots,j_d)\), form \(A\) with columns \(\overline{u_{j_k}}\). Let \(C(A)\) be its cofactor matrix, satisfying \(C(A)A^T=\det(A)I\). Let \(D_a\) be the diagonal indicator of positions whose fine label lies in sector \(a\). Then \(A^TP_a=D_a A^T\), and the successful data-to-output Kraus matrix is
\[
K_{\mathbf j,a}=\frac{C(A)D_aA^T}{\sqrt{d\,d!\,R}}
=\frac{\det(A)}{\sqrt{d\,d!\,R}}P_a.
\]
Repeated fine indices yield zero determinant and hence zero Kraus operator, not merely a vanishing averaged amplitude. Distinct indices give one of \(d!\) permutations of the complete unknown basis, each with \(|\det A|=1\). Summing these orthogonal environment histories produces
\[
\mathcal S_{P,a}(\rho)=\frac1{dR}P_a\rho P_a.
\]
For \(R=d\), this is \(p=1/d^2\) uniformly across rank partitions. For \(R=\max_a n_a\), every surviving permutation has \(n_a=\operatorname{rank}P_a\), so \(p(P)=1/(d r_{\max})\) without rank knowledge. The full projector, rather than a sum of fine dephasings, acts on the retained quantum output; coherence inside degenerate sectors and reference entanglement are preserved.

The protocol uses \(d\) destructive calls, \(d\) query registers of dimension \(d\), one retained \(d\)-dimensional output, and a \(d\)-dimensional control, plus known singlet preparation/routing. It does not establish efficient gate synthesis or reusability after failure.
