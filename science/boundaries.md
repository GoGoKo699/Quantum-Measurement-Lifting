# Resources, scope and exactness boundary

## What is and is not restored

The oracle reveals classical labels only. The protocol synthesizes the *canonical Lüders instrument* determined by its projectors, not an arbitrary physical detector's inaccessible internal back-action. The accepted operation is exact on all inputs and external references. A failure may destroy the data, so repeated attempts on the same unknown input are not automatically possible.

For \(d=2^n\), the exact query onset is exponential in \(n\). The construction has \(d\) query registers, one output register and a control, each of dimension \(d\), and known antisymmetric-state preparation and routing. No efficient gate count or fault-tolerant implementation is established. The achievable coefficients \(1/d^2\) and \(1/(d r_{\max})\) are not proven optimal.

## Why arbitrary unsharp POVMs cannot be covered by the same exact claim

For an unknown family of strictly positive POVM effects, the destructive measurement channels at any two parameter points are mutually comparable in completely positive order. A finite causal supermap preserves this support equivalence on its accepted branches. By contrast, the desired canonical Lüders branch has rank-one Choi support \(|\sqrt{E_a}\rangle\!\rangle\), whose ray generally changes with the parameter. Two distinct such rays cannot have the same positive support. Thus no finite-use processor can have nonzero exact success throughout a family where these rays vary. This argument excludes genuinely varying full-rank effects, not all isolated nonprojective POVMs or scalar-ray families.

A simple example is \(E_0(x)=\operatorname{diag}(x,1-x)\), \(E_1(x)=I-E_0(x)\), with \(x\) varying over an open interval in \((0,1)\). The projective theorem and this obstruction have different hypotheses.

Approximate restoration via measurement tomography is not ruled out. The optimal error-dependent call cost, success-optimal exact protocols, robustness to detector drift and correlated noise are separate open questions.
