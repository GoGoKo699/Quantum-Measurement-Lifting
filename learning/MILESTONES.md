# Thirty-milestone map

The route has **12 background/preliminaries milestones (M01–M12)** and **18 narrative/innovation milestones (M13–M30)**. The background moves from individual registers and maps to the complete operational question. The research phase assembles the circuit, derives the converse and joins both results to their physical boundaries. Dependencies always point backward.

The sole educational anchor is [Watrous (2018)](WATROUS_BRIDGE.md). Primary papers supply research attribution, not extra educational anchors. The specialist arguments remain in their canonical scientific files.

<a id="m01"></a>
## M01 — Registers and retained output

**Phase:** Background / preliminaries.

**Central question:** Where can the output exist after a destructive call?

**Understanding target:** Distinguish data, query, retained output, control and inaccessible reference registers; account for each system rather than treating a classical label as a quantum output.

**Dependencies:** None.

**Connection and story role:** Physical register accounting fixes what an interface-conversion protocol must preserve.

**Sources:** Watrous §§2.1.1–2.1.2; [model](../science/model.md).

<a id="m02"></a>
## M02 — States and reference correlations

**Phase:** Background / preliminaries.

**Central question:** Why must the task include inputs entangled with another system?

**Understanding target:** Explain why equality on all inputs is a channel requirement and why destroying data-reference coherence is a failure even when local probabilities agree.

**Dependencies:** [M01](#m01)

**Connection and story role:** Purification turns a local state-update promise into a reference-sensitive guarantee.

**Sources:** Watrous §2.1.3; [degenerate example](WORKED_EXAMPLE.md#why-the-degenerate-case-is-a-stronger-test).

<a id="m03"></a>
## M03 — Effects and projectors

**Phase:** Background / preliminaries.

**Central question:** What does a projective resolution of identity specify?

**Understanding target:** Use positivity, orthogonality and the identity sum to derive outcome probabilities, distinguish rank from outcome count, and identify the trivial one-outcome case.

**Dependencies:** [M01](#m01)

**Connection and story role:** The same input dimension can support either many outcomes or only two large sectors.

**Sources:** Watrous §§2.3.1–2.3.2; [model](../science/model.md).

<a id="m04"></a>
## M04 — Destructive measurement channels

**Phase:** Background / preliminaries.

**Central question:** Which part of a measurement survives at the oracle output?

**Understanding target:** Write the quantum-to-classical channel and explain why a refining basis label can be useful mathematically without being accessible to the processor.

**Dependencies:** [M02](#m02), [M03](#m03)

**Connection and story role:** Classical-output access is the charged resource, not a supplied coherent implementation.

**Sources:** Watrous §2.3.1; [model](../science/model.md#destructive-input-quantum-output-target).

<a id="m05"></a>
## M05 — Instruments and success weights

**Phase:** Background / preliminaries.

**Central question:** How is a probability rule different from a state-update map?

**Understanding target:** Separate the unnormalized instrument component, its trace and its normalized output; explain why one input-independent success coefficient is required.

**Dependencies:** [M02](#m02), [M03](#m03), [M04](#m04)

**Connection and story role:** The canonical Lüders target fixes the quantum output while keeping heralding linear.

**Sources:** Watrous §2.3.2, instruments; [model](../science/model.md).

<a id="m06"></a>
## M06 — Degenerate-sector coherence

**Phase:** Background / preliminaries.

**Central question:** Why is fine measurement followed by forgetting not enough?

**Understanding target:** Compare a rank-two projector update with dephasing in a refining basis, using a coherent superposition or a reference-entangled state.

**Dependencies:** [M02](#m02), [M05](#m05)

**Connection and story role:** Correct classical statistics do not certify the desired quantum interface.

**Sources:** Watrous §§2.1.3 and 2.3.2; [worked example](WORKED_EXAMPLE.md).

<a id="m07"></a>
## M07 — Completely positive branch maps

**Phase:** Background / preliminaries.

**Central question:** What makes a successful quantum operation physically valid?

**Understanding target:** Use a Kraus sum and a success effect bounded by identity; explain how a positive complementary effect completes the failure operation.

**Dependencies:** [M05](#m05)

**Connection and story role:** Heralding allows trace decrease but not a nonphysical filter.

**Sources:** Watrous §§2.2.1–2.2.2; [filter](../science/construction.md#a-valid-filter-from-classical-reports).

<a id="m08"></a>
## M08 — Choi representations and ranks

**Phase:** Background / preliminaries.

**Central question:** Why can a degenerate projector have a rank-one Choi map?

**Understanding target:** Translate output-first vectorization and unnormalized Choi conventions; distinguish matrix rank of a projector, Choi rank of a map and trace normalization.

**Dependencies:** [M06](#m06), [M07](#m07)

**Connection and story role:** The same representation verifies complete outputs and later constrains every accepted history.

**Sources:** Watrous §2.2.2; [conventions](../science/model.md#matrix-and-choi-conventions).

<a id="m09"></a>
## M09 — Hidden Kraus histories

**Phase:** Background / preliminaries.

**Central question:** Which amplitudes may interfere, and which contributions must be added positively?

**Understanding target:** Distinguish coherent routing positions within one environment history from the incoherent sum over different hidden histories.

**Dependencies:** [M04](#m04), [M07](#m07), [M08](#m08)

**Connection and story role:** Correct treatment of inaccessible records prevents a false cancellation argument.

**Sources:** Watrous §2.2.2; [environment resolution](../science/construction.md#resolving-the-inaccessible-environment-for-the-proof).

<a id="m10"></a>
## M10 — Isometries and coherent routing

**Phase:** Background / preliminaries.

**Central question:** How can one unknown input occupy a superposition of ports without cloning?

**Understanding target:** Explain why orthogonal control branches normalize a sum of isometric embeddings; separate routing known registers from controlling an unknown oracle.

**Dependencies:** [M01](#m01), [M07](#m07), [M09](#m09)

**Connection and story role:** Known control produces useful interference without strengthening the oracle.

**Sources:** Watrous §§1.1.1 and 2.2.2; [routing](../science/construction.md#known-preparation-and-coherent-routing).

<a id="m11"></a>
## M11 — Antisymmetry and determinants

**Phase:** Background / preliminaries.

**Central question:** Why do repeated vectors disappear in an alternating contraction?

**Understanding target:** Connect the signed permutation state, determinant alternation and cofactor identity, including the singular-matrix case; distinguish cofactor matrix from adjugate.

**Dependencies:** [M03](#m03), [M10](#m10)

**Connection and story role:** Linear algebra supplies the cancellation mechanism without assuming any unknown basis information.

**Sources:** Watrous §1.1 and optional §7.1; [construction](../science/construction.md).

<a id="m12"></a>
## M12 — The complete operational question

**Phase:** Background / preliminaries.

**Central question:** What exactly must be achieved and counted?

**Understanding target:** Assemble the oracle, allowed processing, reference-sensitive target, common success coefficient and worst-case call budget; distinguish exact onset from constant-success or approximate complexity.

**Dependencies:** [M01](#m01), [M02](#m02), [M03](#m03), [M04](#m04), [M05](#m05), [M06](#m06), [M07](#m07), [M08](#m08), [M09](#m09), [M10](#m10), [M11](#m11)

**Connection and story role:** This closes the background phase with a single model against which both bounds are compared.

**Sources:** Watrous Chapter 2; [theorem](../science/model.md#exact-query-onset).

<a id="m13"></a>
## M13 — Preparing the known resource

**Phase:** Narrative / innovation.

**Central question:** Which registers are prepared before any unknown call?

**Understanding target:** Locate the singlet, data and control in a general dimension and account for the retained output, rather than imagining quantum information emerging from the classical oracle output.

**Dependencies:** [M10](#m10), [M11](#m11), [M12](#m12)

**Connection and story role:** The construction begins with retained coherent workspace and an explicitly known state.

**Sources:** [preparation](../science/construction.md#known-preparation-and-coherent-routing); Watrous §2.2.2.

<a id="m14"></a>
## M14 — Routing phases and normalization

**Phase:** Narrative / innovation.

**Central question:** Why are the branch signs and the uniform control weight necessary?

**Understanding target:** Relate the sign for each insertion position to a cofactor expansion and show that the routing map is an isometry with the stated normalization.

**Dependencies:** [M11](#m11), [M13](#m13)

**Connection and story role:** Correct phases enable the algebraic identity while control orthogonality ensures physical normalization.

**Sources:** [construction](../science/construction.md); [qubit preparation](WORKED_EXAMPLE.md#an-explicit-qubit-preparation).

<a id="m15"></a>
## M15 — Filtering from reported labels

**Phase:** Narrative / innovation.

**Central question:** How can classical reports determine a valid coherent filter?

**Understanding target:** Form label groups on the control positions, compute their nonzero effect eigenvalues and identify a valid failure complement for both normalizations.

**Dependencies:** [M07](#m07), [M14](#m14)

**Connection and story role:** The report is classical, but the retained control still supports coherent postprocessing.

**Sources:** [filter](../science/construction.md#a-valid-filter-from-classical-reports); Watrous §§2.2.2 and 2.3.2.

<a id="m16"></a>
## M16 — One hidden-history contraction

**Phase:** Narrative / innovation.

**Central question:** What matrix does a fixed inaccessible fine history induce?

**Understanding target:** Build the matrix of conjugated basis columns, identify the diagonal coarse-label selector and obtain the outer product contributed by one routing position.

**Dependencies:** [M09](#m09), [M11](#m11), [M14](#m14), [M15](#m15)

**Connection and story role:** Resolving a channel into Kraus histories is an analytical device, not extra access.

**Sources:** [resolved contraction](../science/construction.md#resolving-the-inaccessible-environment-for-the-proof); Watrous §2.2.2.

<a id="m17"></a>
## M17 — Cofactor assembly

**Phase:** Narrative / innovation.

**Central question:** How do the routing positions combine into one matrix expression?

**Understanding target:** Follow how singlet amplitudes, routing phase and control bra assemble the cofactor-selector product, keeping all three normalization factors.

**Dependencies:** [M16](#m16)

**Connection and story role:** A physical circuit produces a precise algebraic expression whose entries can be checked independently.

**Sources:** [construction](../science/construction.md); [full-channel implementation](../verification/check_full_channel.py).

<a id="m18"></a>
## M18 — Recovering the whole projector

**Phase:** Narrative / innovation.

**Central question:** Why does the accepted matrix retain all within-sector coherence?

**Understanding target:** Use the selector relation and cofactor identity to factor the accepted matrix into a scalar determinant times the complete projector.

**Dependencies:** [M06](#m06), [M17](#m17)

**Connection and story role:** The target is a single projector Kraus matrix, not a mixture over basis vectors.

**Sources:** [factorization](../science/construction.md#resolving-the-inaccessible-environment-for-the-proof); [degenerate example](WORKED_EXAMPLE.md).

<a id="m19"></a>
## M19 — Eliminating repeated histories

**Phase:** Narrative / innovation.

**Central question:** Why does cancellation occur before the environment sum?

**Understanding target:** Show that repeated fine indices make each accepted Kraus matrix zero; count the distinct histories and explain why their probabilities, not amplitudes, are added.

**Dependencies:** [M09](#m09), [M18](#m18)

**Connection and story role:** Alternation removes the histories that would otherwise retain unwanted which-basis information.

**Sources:** [history sum](../science/construction.md#summing-probabilities-not-hidden-amplitudes).

<a id="m20"></a>
## M20 — The uniform success coefficient

**Phase:** Narrative / innovation.

**Central question:** How does normalization yield a complete instrument rather than only one branch?

**Understanding target:** Derive the fixed-normalization coefficient and show that summing accepted traces gives an input-independent total; distinguish branch Choi trace from success.

**Dependencies:** [M08](#m08), [M19](#m19)

**Connection and story role:** The counting and channel conventions jointly fix the operational probability.

**Sources:** [construction](../science/construction.md); [Choi conventions](../science/model.md#matrix-and-choi-conventions).

<a id="m21"></a>
## M21 — Rank-oblivious improvement

**Phase:** Narrative / innovation.

**Central question:** How can the filter exploit ranks that were not supplied?

**Understanding target:** Use observed maximum multiplicity and show why it equals the largest rank on every surviving history while remaining a valid filter on all other histories.

**Dependencies:** [M15](#m15), [M19](#m19), [M20](#m20)

**Connection and story role:** Postprocessing can adapt to observed counts without a separate rank-estimation assumption.

**Sources:** [count-based filter](../science/construction.md#summing-probabilities-not-hidden-amplitudes).

<a id="m22"></a>
## M22 — Complete small experiments

**Phase:** Narrative / innovation.

**Central question:** What should a qubit or degenerate-sector test actually verify?

**Understanding target:** Follow the two-call qubit experiment and rank-two reference example, then distinguish cofactor checks from full routing-isometry and Choi-map checks.

**Dependencies:** [M18](#m18), [M20](#m20), [M21](#m21)

**Connection and story role:** Concrete calculations integrate construction, probability and the quantum output requirement.

**Sources:** [worked examples](WORKED_EXAMPLE.md); [verification](../verification/README.md).

<a id="m23"></a>
## M23 — Polynomial dependence under adaptation

**Phase:** Narrative / innovation.

**Central question:** What limitation survives arbitrary causal feedback?

**Understanding target:** Resolve a general processor into fine histories and explain why every destructive call contributes one conjugated unknown bra; identify the role of finite-slot dilation.

**Dependencies:** [M09](#m09), [M12](#m12), [M22](#m22)

**Connection and story role:** The converse uses the same oracle but does not inherit the parallel architecture of the construction.

**Sources:** [polynomial histories](../science/converse.md#each-resolved-call-contributes-one-unknown-bra); Watrous §2.2.2 for finite Kraus foundations.

<a id="m24"></a>
## M24 — Exactness on each history

**Phase:** Narrative / innovation.

**Central question:** Why can positive Kraus contributions not cancel an unwanted Choi direction?

**Understanding target:** Use a vector orthogonal to the target Choi ray to derive branchwise proportionality, and recover the scalar as a trace so its polynomial degree is controlled.

**Dependencies:** [M08](#m08), [M23](#m23)

**Connection and story role:** Complete positivity turns a global exact-output requirement into an algebraic constraint on every history.

**Sources:** [rank-one argument](../science/converse.md#exactness-constrains-every-positive-contribution); Watrous Theorem 2.22.

<a id="m25"></a>
## M25 — Extending away from unitary matrices

**Phase:** Narrative / innovation.

**Central question:** Why is a singular matrix relevant to an identity first proved on unitaries?

**Understanding target:** Explain the complexification argument using a Hermitian basis, holomorphic uniqueness and the exponential map; track transpose, adjoint and conjugation.

**Dependencies:** [M11](#m11), [M24](#m24)

**Connection and story role:** The unitary-orbit equality becomes a polynomial identity on all matrices, enabling a singular witness.

**Sources:** [complexification](../science/converse.md#complexifying-the-identity). The necessary analytic argument is supplied locally.

<a id="m26"></a>
## M26 — The determinant factor

**Phase:** Narrative / innovation.

**Central question:** How does one nonzero singular witness force a minimum degree?

**Understanding target:** Connect determinant irreducibility and primality to the inside/outside-sector block witness, then infer divisibility of the scalar coefficient.

**Dependencies:** [M25](#m25)

**Connection and story role:** A matrix-space obstruction becomes a call-count bound because each call contributes only one degree.

**Sources:** [determinant argument](../science/converse.md#why-a-determinant-factor-is-unavoidable).

<a id="m27"></a>
## M27 — Matching onset and binary detectors

**Phase:** Narrative / innovation.

**Central question:** Why is the input dimension decisive even with one reported bit?

**Understanding target:** Combine the universal lower bound with the parallel upper construction for every nontrivial rank partition; explain the one-outcome exception without changing models.

**Dependencies:** [M21](#m21), [M26](#m26)

**Connection and story role:** The two proof routes close the exact query law and isolate its operational meaning.

**Sources:** [theorem](../science/model.md#exact-query-onset); [converse](../science/converse.md).

<a id="m28"></a>
## M28 — The full-rank exactness boundary

**Phase:** Narrative / innovation.

**Central question:** Why does a varying unsharp family resist finite exact lifting?

**Understanding target:** Derive mutual CP-order comparison, propagate it through finitely many slots and compare supports of the desired pure Choi rays; identify constant-ray exceptions.

**Dependencies:** [M07](#m07), [M08](#m08), [M24](#m24), [M27](#m27)

**Connection and story role:** The exact sharp case is distinguished by support geometry, not by a general claim that noisy recovery is impossible.

**Sources:** [unsharp proof](../science/boundaries.md#full-rank-unsharp-effects-a-different-exact-problem); Watrous §2.2.2.

<a id="m29"></a>
## M29 — Costs and closest-work differences

**Phase:** Narrative / innovation.

**Central question:** What is left after every supplied resource and inherited ingredient is stated?

**Understanding target:** Account for calls, registers, known controls, heralding and fresh-input retries; distinguish destructive lifting from unitary conjugation, classical measurement retrieval and instrument simulation.

**Dependencies:** [M22](#m22), [M27](#m27), [M28](#m28)

**Connection and story role:** Resource accounting and attribution prevent a formal interface conversion from being misreported as an efficient practical upgrade.

**Sources:** [boundaries](../science/boundaries.md); [related work](../references/RELATED_WORK.md).

<a id="m30"></a>
## M30 — Global synthesis

**Phase:** Narrative / innovation.

**Central question:** What has been established, and which questions remain separate?

**Understanding target:** Give one connected account of the exact threshold, attaining protocol, degenerate coherence, adaptive converse and unsharp boundary; separate proved onset from unknown success optima, approximation and implementation efficiency.

**Dependencies:** [M27](#m27), [M28](#m28), [M29](#m29)

**Connection and story role:** The final milestone joins the whole story without adding an unproved extension or relying on a development diary.

**Sources:** [scientific overview](../science/README.md); [model](../science/model.md); [scope](../science/boundaries.md).
