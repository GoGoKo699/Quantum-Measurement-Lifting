# Quantum Measurement Lifting

**Can a destructive measurement oracle be converted into its canonical quantum state-update instrument?**

For an unknown projective measurement \(P=\{P_a\}\) on \(\mathbb C^d\), the supplied oracle returns only the classical label, destroying the queried quantum system. The target is a heralded, reference-preserving Lüders instrument
\[
\mathcal S_{P,a}(\rho)=p(P)P_a\rho P_a
\]
with one common, input-independent success coefficient for all outcomes.

## Main theorem

For every nontrivial fixed rank partition (at least two nonzero sectors), **exact universal nonzero-success lifting requires at least \(d\) ordinary destructive oracle calls**, even allowing arbitrary causal adaptive processing and coherent memory. A parallel protocol using exactly \(d\) calls achieves
\[
p(P)=\frac{1}{d\,r_{\max}(P)},\qquad r_{\max}(P)=\max_a\operatorname{rank}P_a.
\]
It needs no supplied basis or ranks. A simpler rank-independent choice attains \(1/d^2\). The query threshold remains \(d\) even for a binary PVM.

The theorem concerns **the canonical Lüders update determined by the effects**, not the inaccessible detector's unknown physical back-action.

## Read the science

- [Operational model and exact statement](science/model.md)
- [Antisymmetric construction and probabilities](science/construction.md)
- [Universal adaptive converse](science/converse.md)
- [Scope, unsharp obstruction and resources](science/boundaries.md)
- [Primary prior-work comparison](references/RELATED_WORK.md)

The construction is an exact query result, **not** a scalable gate-efficiency or constant-success guarantee. In particular, for \(d=2^n\) the call count is exponential in \(n\); failures may destroy the unknown input. The optimal success probability, approximate/noisy lifting and constant-success query cost are open.

The scientific account is currently being integrated and checked; the educational route and final hosted rendering review are pending.
