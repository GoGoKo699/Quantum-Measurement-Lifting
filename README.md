# Quantum Measurement Lifting

**How many uses of a destructive detector are needed to recover a measurement's quantum state update?**

An unknown projective measurement on a $d$-dimensional system consumes its input and returns a classical label. This project constructs its canonical Lüders instrument: on a heralded success, outcome $a$ applies the full projector $P_a$ to the data, preserving coherence within degenerate eigenspaces and correlations with a reference.

## Main result

For every nontrivial fixed rank partition, the exact universal query threshold is

```math
N_{\min}=d.
```

The lower bound allows arbitrary causal adaptation and quantum memory. A parallel construction with $d$ ordinary destructive calls attains

```math
\mathcal S_{P,a}(\rho)=p(P)P_a\rho P_a,
\qquad
p(P)=\frac{1}{d\,r_{\max}(P)},
```

where $r_{\max}(P)$ is the largest projector rank. The protocol needs neither the unknown basis nor the ranks. A fixed-normalization version gives the same coefficient $1/d^2$ for every rank partition. These probabilities are attained values, not claimed global optima.

| Question | Supported result | Full account |
|---|---|---|
| Can classical-output access supply the quantum update? | An antisymmetric state and coherent routing give an exact heralded instrument | [Construction](science/construction.md) |
| Can adaptation use fewer calls? | No nonzero exact universal success below the dimension threshold, even for binary measurements | [Converse](science/converse.md) |
| What changes for full-rank effects? | Varying canonical update rays cannot be lifted exactly by any finite-call processor | [Exactness boundary](science/boundaries.md) |
| What is preserved inside a degenerate sector? | The complete projected state, rather than fine-basis dephasing | [Worked examples](learning/WORKED_EXAMPLE.md) |

The supplied detector need not physically use the Lüders update. The target is the canonical instrument determined by its effects, not reconstruction of inaccessible internal back-action.

## Read and learn

The [scientific overview](science/README.md) connects the model, construction, converse and physical limitations. Specialists can start at the [exact theorem and conventions](science/model.md). The [related-work comparison](references/RELATED_WORK.md) separates this transformation from unitary conjugation, measurement learning and instrument simulation.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. Start with the [learning guide](learning/README.md) and [worked experiment](learning/WORKED_EXAMPLE.md), then use the [Watrous bridge](learning/WATROUS_BRIDGE.md) and [30-milestone map](learning/MILESTONES.md). The map has 12 background milestones and 18 research milestones. Its understanding targets are common to all readers.

The [LLM reading guide](llms.txt) points to the same authoritative accounts.

## Reproduce the checks

With Python 3.11 or later, run from the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The [verification guide](verification/README.md) explains each check and its limits. The suite constructs the physical routing isometry, enumerates hidden measurement histories, tests both filters, compares complete Choi maps and checks reference coherence in dimensions two through four. It also checks the cofactor identity, the converse's singular-matrix witness, learning dependencies and local links. General claims follow from the written proofs, not the finite tests.

## Scope

The device is an ideal memoryless PVM. Known quantum controls, singlet preparation and workspace are available and explicitly identified. For $d=2^n$, the query count is exponential in the number of input qubits. Failure can destroy the input; repeating the protocol does not automatically amplify success on the same unknown state. Optimal success probability, constant-success query complexity, approximate lifting and efficient gate synthesis are not established.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
