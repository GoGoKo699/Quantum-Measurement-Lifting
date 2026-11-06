# Operational model and theorem

Let \(d\ge2\) and \(\{P_a\}\) be a projective resolution of identity on \(\mathbb C^d\), with at least two nonzero projectors. The black-box channel is
\[
\mathcal M_P(\rho)=\sum_a\operatorname{tr}(P_a\rho)|a\rangle\langle a|.
\]
Each call consumes its quantum input and returns only the classical label. No unknown basis, inverse, coherent dilation, postmeasurement quantum output or QRAM is supplied. The device is memoryless.

A processor receives one arbitrary input, possibly entangled with a reference, and uses \(N\) oracle calls plus arbitrary known finite-dimensional quantum operations, ancillary registers, adaptive classical control and coherent memory. The successful branch must implement the entire trace-decreasing instrument
\[
\mathcal S_{P,a}(\rho)=p(P)P_a\rho P_a\quad\text{for all }a,\rho,
\]
with \(p(P)>0\) for every member of the unknown unitary orbit. This complete-map identity includes arbitrary references; \(p(P)\) is independent of the input and reported output, but may depend on the unknown PVM.

**Theorem (exact query onset).** For every fixed nontrivial rank partition, the least number of calls for such universal exact lifting is \(N_{\min}=d\). The lower bound permits arbitrary causal adaptive strategies. A rank-oblivious parallel construction achieves \(p(P)=1/(d r_{\max}(P))\) using \(d\) calls, and a rank-independent normalization achieves \(1/d^2\).

The trivial one-outcome PVM has target identity and requires no calls. This theorem establishes onset of nonzero exact success, not success-optimality or an approximate lower bound. See [construction](construction.md) and [converse](converse.md).
