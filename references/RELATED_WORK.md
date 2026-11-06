# Related work and attribution

The contribution is the matched exact query onset for producing the canonical Lüders instrument from ordinary destructive PVM calls, including degenerate-sector and reference coherence. The following are task-and-access comparisons, not an exhaustive priority certificate. Primary-source records and the closest statements were rechecked on 7 November 2026 (Singapore time).

## Antisymmetric transformations of unknown unitaries

J. Miyazaki, A. Soeda and M. Murao, *Complex conjugation supermap of unitary quantum maps and its universal implementation protocol*, Physical Review Research **1**, 013007 (2019), [arXiv:1706.03481](https://arxiv.org/abs/1706.03481), [DOI](https://doi.org/10.1103/PhysRevResearch.1.013007).

M. T. Quintino, Q. Dong, A. Shimbo, A. Soeda and M. Murao, *Probabilistic exact universal quantum circuits for transforming unitary operations*, Physical Review A **100**, 062339 (2019), [arXiv:1909.01366](https://arxiv.org/abs/1909.01366), [DOI](https://doi.org/10.1103/PhysRevA.100.062339).

Antisymmetric/exterior-power constructions and degree restrictions for unknown transformations are antecedents, not new general methods here. In the second paper, Section V and Theorem 1 treat complex conjugation with coherent unitary input operations and a threshold of at least dimension minus one. A destructive detector does not supply a chosen basis unitary. Our construction instead contracts inaccessible measurement bras and must preserve an entire possibly degenerate projector on a retained output. Its converse concerns that different output map and destructive access. The additional call count is not claimed novel merely as a changed constant: the operational addition is the conversion between outcome-only and quantum-output interfaces.

## Learning and retrieving classical measurement outcomes

A. Bisio, G. M. D'Ariano, P. Perinotti and M. Sedlak, *Quantum learning algorithms for quantum measurements*, Physics Letters A **375**, 3425–3434 (2011), [arXiv:1103.0480v2](https://arxiv.org/abs/1103.0480v2).

F. Turoboś, L. Marcinkowska and Z. Puchała, *Quantum and Classical Memory for Storage and Retrieval of Quantum Measurements*, [arXiv:2610.36972](https://arxiv.org/abs/2610.36972) (2026).

These questions concern reproducing the outcome channel. The latter paper's Definition 2, Eq. (3), and Definition 7, Eq. (9), make the quantum-to-classical target explicit; Section 8 distinguishes stronger coherent access. Its single-query probability does not supply a Lüders output. The corresponding Choi block is an effect transpose, whereas a Lüders component has the pure Choi matrix built from the vectorized projector. Similar probability formulas do not equate these tasks. Storage timing is also different: our input may participate in the queried circuit rather than arriving only after training.

## Instruments and the value of postmeasurement states

S. Khandelwal and A. Tavakoli, *Simulating quantum instruments with projective measurements and quantum post-processing*, [arXiv:2503.00956v2](https://arxiv.org/html/2503.00956v2) (2025), Section II and Theorems 1–2. Their supplied projective instruments retain postmeasurement quantum states before further processing. This is stronger than the destructive interface supplied here.

Z. Liu, Q. Ye, Z. Cai and J. Eisert, *Exponential speedup in measurement property learning with post-measurement states*, [arXiv:2602.22126v1](https://arxiv.org/abs/2602.22126v1) (2026).

C. Eid and M. T. Quintino, *Post-measurement states are (very) useful for measurement discrimination*, [arXiv:2602.12258v2](https://arxiv.org/abs/2602.12258v2) (2026).

These works establish that supplied postmeasurement-state access has operational value. They motivate the interface distinction but do not establish the exact universal construction from destructive calls. No downstream learning or discrimination speedup is claimed for our low-success conversion after charging all calls.

## General tools used in the proofs

G. Chiribella, G. M. D'Ariano and P. Perinotti, *Theoretical framework for quantum networks*, Physical Review A **80**, 022339 (2009), [arXiv:0904.4483v2](https://arxiv.org/abs/0904.4483v2). Finite-dimensional quantum combs and memory-channel realizations justify representing general finite-slot causal processing by fixed tensors. The [converse](../science/converse.md) then supplies the task-specific polynomial argument.

B. Regula and R. Takagi, *Fundamental limitations on distillation of quantum channel resources*, Nature Communications **12**, 4411 (2021), [DOI](https://doi.org/10.1038/s41467-021-24699-0). Positive-component and CP-order methods underlie general purification restrictions. The [full-rank boundary](../science/boundaries.md) gives a self-contained support comparison for the present target, rather than claiming a new general distillation principle.

The only educational anchor is [Watrous (2018)](../learning/WATROUS_BRIDGE.md). The primary papers above provide attribution and research comparisons, not additional required textbooks. Metadata are retained in [references.bib](references.bib).

## Other repository tasks

[Quantum Detector Memory](https://github.com/GoGoKo699/Quantum-Detector-Memory) concerns calibration information retained through destructive calls. [Quantum Program Composition](https://github.com/GoGoKo699/Quantum-Program-Composition) processes supplied unitary Choi programs. [Quantum Order Distillation](https://github.com/GoGoKo699/Quantum-Order-Distillation) uses coherent ordering of supplied quantum channels. [Canonical Purification Cost](https://github.com/GoGoKo699/Canonical-Purification-Cost) concerns state preparation from sample streams, and [Quantum Conditional Learning](https://github.com/GoGoKo699/Quantum-Conditional-Learning) concerns conditional-state prediction. Their targets and supplied resources differ from the measurement-channel transformation here; shared tools alone establish no transfer or adopted sister relationship.
