# Verification

Run from the repository root with Python 3.11 or later:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The pinned numerical dependency is NumPy 2.3.5. The furnishing run used Python 3.13.5. The scripts need no network, external datasets or GPU. Local outputs are written under `verification/output/`, which is ignored by Git. Every command fails with a nonzero exit status when a required check fails; errors are not disabled by Python optimization.

## What is checked

| Script | Evidence | Limits |
|---|---|---|
| `check_cofactor.py` | Cofactor/sector identity over all hidden histories for binary partitions in dimensions two through four; singular witness in dimensions two through six | Finite identities, not a proof of universal divisibility |
| `check_full_channel.py` | 36 physical-circuit cases: two seeded bases, both control normalizations, nine dimension/rank choices | Ideal finite floating-point calculations |
| `check_repository.py` | Exactly 30 ordered milestones, 12/18 phases, required fields and backward dependencies, local links/anchors, source-math delimiter hygiene and essential files | Does not verify pixels, mathematical truth or external-link availability |
| `run_all.py` | Executes the complete suite and retains JSON/stdout records | No independent expert certification |

The full-channel implementation constructs the routing tensor directly from singlet permutation amplitudes. It does not use the claimed cofactor formula to generate the accepted maps. It checks the isometry, physical failure complement, each refined accepted matrix, repeated-history cancellation, complete Choi matrices and the summed success effect. Rank-two and larger sectors also receive an explicit entangled-reference test.

The rank choices are: dimension two, ranks 1+1 and 2; dimension three, ranks 1+2 and 1+1+1; dimension four, ranks 1+3, 2+2, 1+1+2, 1+1+1+1 and 4. One-outcome cases test the construction's consistency only; the lower-bound theorem excludes them.

The numerical tolerance is $2\times10^{-11}$. The documented run's largest full-channel Choi residual was below $5\times10^{-16}$, and its largest isometry residual was below $4\times10^{-16}$. Last-bit values may differ across platforms. Expected output ends with `PASS: all local checks`; this is not an assertion about future runs.

## Analytical review boundary

The general theorem relies on the written cofactor identity, the complete-map positivity argument, finite-slot polynomial dependence, complexification, determinant irreducibility and the singular witness. The full-rank obstruction uses CP order under finitely many oracle slots. Review these in [construction](../science/construction.md), [converse](../science/converse.md) and [boundaries](../science/boundaries.md); finite matrix tests cannot prove their universal quantifiers.

## Hosted presentation

Local syntax and link checks do not certify GitHub's rendered equations, table layout or navigation behavior. A final hosted review must be tied to the exact integrated commit, compare all rendered mathematics with source, and inspect actual wide and narrow screenshots. Repository content and scientific tests can be complete while that separate review remains pending. Hosted-review evidence belongs to the private completion record, not to a generic passing flag in this guide.
