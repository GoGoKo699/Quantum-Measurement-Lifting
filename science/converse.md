# Converse: fewer than d destructive calls cannot lift exactly

Fix a nontrivial rank partition with diagonal sector projectors \(E_a\) and unknown \(P_a(U)=UE_aU^\dagger\), \(U\in U(d)\). Consider any finite-dimensional causal processor making at most \(N\) ordinary destructive calls.

## Polynomial representation of a successful history

Fine-grain each oracle use into a hidden basis label \(j\), with Kraus operator \(|f(j)\rangle\langle u_j|\), and refine the processor's known operations and successful flags into Kraus histories. For a history with \(n\le N\) calls, its data-to-output Kraus matrix \(K_h(Z)\) is polynomial of degree at most \(n\) in \(Z=\overline U\): each oracle contributes one unknown bra and every other tensor is known. Adaptation changes which known tensors are contracted in a fixed history, not the polynomial degree. An arbitrary finite-dimensional comb has a finite positive Choi operator and a finite Kraus realization; this reduction also accommodates classical records with a continuous presentation.

Exactness of the accepted completely positive map gives
\[
\sum_h|K_h(U)\rangle\!\rangle\langle\!\langle K_h(U)|
=p(U)|P_a(U)\rangle\!\rangle\langle\!\langle P_a(U)|.
\]
Positivity and the rank-one right side force \(K_h(U)=c_h(U)P_a(U)\) for every fine history, including zeros when \(p(U)=0\). Since \(r_a=\operatorname{tr}P_a>0\),
\[
c_h(Z)=\operatorname{tr}K_h(Z)/r_a
\]
is a polynomial of degree at most \(n\).

## Determinant obstruction

Write \(T=Z^T=U^\dagger\). Then \(P_a(U)=T^{-1}E_aT\), so on unitary \(T\)
\[
\det(T)K_h(Z)=c_h(Z)\operatorname{adj}(T)E_aT. \tag{1}
\]
The unitary group is Zariski dense in all complex matrices: a polynomial vanishing on unitaries vanishes on a complex-open neighborhood of identity by complexifying the exponential of a real Hermitian basis, and hence identically. Thus (1) is a polynomial identity for arbitrary complex \(T\), including singular matrices.

The generic determinant is irreducible in \(\mathbb C[T_{ij}]\) and therefore prime. If \(0<r_a<d\), at least one entry of \(F(T)=\operatorname{adj}(T)E_aT\) is not divisible by \(\det T\). To see this, select one coordinate in sector \(a\) and one outside it, insert the singular block
\[
\begin{pmatrix}1&1\\1&1\end{pmatrix}
\]
and leave the remaining coordinates as identity. The corresponding block of \(F\) is
\[
\begin{pmatrix}1&1\\-1&-1\end{pmatrix}\ne0
\]
while \(\det T=0\). Therefore (1) implies \(\det T\mid c_h(Z)\). Since \(\deg\det T=d\) and \(\deg c_h\le n<d\), \(c_h=0\) and \(K_h=0\).

Every accepted fine history vanishes when \(N<d\). Hence no such processor has nonzero universal exact success, even for a two-outcome PVM and even with causal adaptation. The upper construction proves the threshold is attained.

This is a degree obstruction to **exact** restoration; it does not establish a lower bound on approximate recovery or on the success probability once \(N\ge d\).
