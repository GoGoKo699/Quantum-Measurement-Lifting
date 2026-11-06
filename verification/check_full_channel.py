#!/usr/bin/env python3
"""Rebuild the physical routing circuit and check its complete accepted maps.

The implementation starts from permutation amplitudes, not the cofactor formula.
Finite floating-point checks do not establish the all-dimension converse.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
from pathlib import Path
import numpy as np

TOLERANCE = 2e-11

def sign(perm: tuple[int, ...]) -> int:
    return (-1) ** sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i + 1, len(perm)))

def routing_isometry(d: int) -> np.ndarray:
    # Axes: control, Q_1,...,Q_d, output B, input D.
    v = np.zeros((d,) * (d + 3), dtype=complex)
    for k in range(d):
        for perm in itertools.permutations(range(d)):
            amplitude = (-1) ** (d - 1 - k) * sign(perm) / math.sqrt(d * math.factorial(d))
            for x in range(d):
                query = list(perm[:-1])
                query.insert(k, x)
                v[(k, *query, perm[-1], x)] = amplitude
    return v

def basis(d: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    q, r = np.linalg.qr(z)
    phases = np.diag(r)
    return q @ np.diag(phases / np.abs(phases))

def hidden_history_tensor(v: np.ndarray, u: np.ndarray) -> np.ndarray:
    result = v
    for axis in range(1, u.shape[0] + 1):
        result = np.tensordot(u.conj().T, result, axes=(1, axis))
        result = np.moveaxis(result, 0, axis)
    return result

def verify_case(d: int, ranks: tuple[int, ...], seed: int, mode: str) -> dict:
    if sum(ranks) != d or min(ranks) <= 0:
        raise ValueError("Ranks must be positive and sum to d")
    v = routing_isometry(d)
    flat = v.reshape(-1, d)
    iso_error = float(np.linalg.norm(flat.conj().T @ flat - np.eye(d)))
    u = basis(d, seed)
    amplitude = hidden_history_tensor(v, u)
    labels = np.repeat(np.arange(len(ranks)), ranks)
    projectors = [u[:, labels == a] @ u[:, labels == a].conj().T for a in range(len(ranks))]
    chois = [np.zeros((d*d, d*d), complex) for _ in ranks]
    effect = np.zeros((d, d), complex)
    repeated_error = 0.0
    min_failure_eigenvalue = 1.0
    fine_branch_error = 0.0
    for history in itertools.product(range(d), repeat=d):
        reported = labels[list(history)]
        counts = np.bincount(reported, minlength=len(ranks))
        normalization = d if mode == "constant" else int(max(counts))
        filter_effect = np.zeros((d, d), complex)
        for a in range(len(ranks)):
            selected = np.flatnonzero(reported == a)
            row = np.zeros(d, complex)
            row[selected] = 1 / math.sqrt(normalization)
            filter_effect += np.outer(row.conj(), row)
            k = sum((amplitude[(int(c), *history)] for c in selected), start=np.zeros((d, d), complex)) / math.sqrt(normalization)
            # This comparison is additional; the physical circuit above does not use it.
            a_matrix = np.column_stack([u[:, j].conj() for j in history])
            expected_k = np.linalg.det(a_matrix) * projectors[a] / math.sqrt(d * math.factorial(d) * normalization)
            fine_branch_error = max(fine_branch_error, float(np.linalg.norm(k - expected_k)))
            vector = k.reshape(-1)  # output-first vectorization, matching vec(A).
            chois[a] += np.outer(vector, vector.conj())
            effect += k.conj().T @ k
            if len(set(history)) < d:
                repeated_error = max(repeated_error, float(np.linalg.norm(k)))
        min_failure_eigenvalue = min(min_failure_eigenvalue, float(np.linalg.eigvalsh(np.eye(d)-filter_effect).min()))
    p = 1 / (d * (d if mode == "constant" else max(ranks)))
    choi_error = max(float(np.linalg.norm(j - p * np.outer(pj.reshape(-1), pj.reshape(-1).conj()))) for j, pj in zip(chois, projectors))
    success_error = float(np.linalg.norm(effect - p * np.eye(d)))
    # An explicit reference-entangled test inside a degenerate sector.
    reference_error = 0.0
    for a, rank in enumerate(ranks):
        if rank < 2:
            continue
        cols = u[:, labels == a]
        entangled = (np.kron(cols[:, 0], np.eye(2)[0]) + np.kron(cols[:, 1], np.eye(2)[1])) / math.sqrt(2)
        state = np.outer(entangled, entangled.conj())
        recovered = np.zeros_like(state)
        for i in range(d):
            for j in range(d):
                for out_i in range(d):
                    for out_j in range(d):
                        recovered[2*out_i:2*out_i+2, 2*out_j:2*out_j+2] += chois[a][out_i*d+i, out_j*d+j] * state[2*i:2*i+2, 2*j:2*j+2]
        reference_error = max(reference_error, float(np.linalg.norm(recovered - p * state)))
    errors = [iso_error, fine_branch_error, choi_error, success_error, repeated_error, reference_error]
    if max(errors) > TOLERANCE or min_failure_eigenvalue < -TOLERANCE:
        raise AssertionError((d, ranks, seed, mode, errors, min_failure_eigenvalue))
    return dict(d=d, ranks=list(ranks), seed=seed, normalization=mode, success=p,
                isometry_error=iso_error, fine_branch_error=fine_branch_error,
                choi_error=choi_error, success_effect_error=success_error,
                repeated_history_error=repeated_error, reference_error=reference_error,
                minimum_failure_eigenvalue=min_failure_eigenvalue)

def run() -> dict:
    partitions = {2: [(1, 1), (2,)], 3: [(1, 2), (1, 1, 1)],
                  4: [(1, 3), (2, 2), (1, 1, 2), (1, 1, 1, 1), (4,)]}
    cases = [verify_case(d, ranks, seed, mode) for d, ps in partitions.items()
             for ranks in ps for seed in (731, 2026) for mode in ("constant", "counts")]
    return {"status": "pass", "tolerance": TOLERANCE, "case_count": len(cases),
            "scope": "Physical routing, all hidden histories, both filters, full Choi maps, reference coherence; d=2,3,4 only.",
            "cases": cases}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: {report['case_count']} full-channel cases; tolerance {TOLERANCE:g}")
