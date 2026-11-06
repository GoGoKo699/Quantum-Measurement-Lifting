#!/usr/bin/env python3
"""Deterministic finite checks of the cofactor identity; not a universal proof."""
import itertools
import math
import numpy as np

def cofactor(A):
    d = A.shape[0]
    C = np.empty_like(A)
    for i in range(d):
        for j in range(d):
            minor = np.delete(np.delete(A, i, axis=0), j, axis=1)
            C[i, j] = (-1)**(i+j) * np.linalg.det(minor)
    return C

def haar(d, seed):
    rng = np.random.default_rng(seed)
    Z = rng.normal(size=(d,d)) + 1j*rng.normal(size=(d,d))
    Q, R = np.linalg.qr(Z)
    return Q @ np.diag(np.diag(R)/np.abs(np.diag(R)))

for d in (2, 3, 4):
    U = haar(d, 100+d)
    for split in range(1, d):
        sectors = [list(range(split)), list(range(split,d))]
        Ps = [U[:,s] @ U[:,s].conj().T for s in sectors]
        rmax = max(map(len,sectors))
        for history in itertools.product(range(d), repeat=d):
            A = np.column_stack([np.conj(U[:,j]) for j in history])
            C = cofactor(A)
            for a, s in enumerate(sectors):
                D = np.diag([int(j in s) for j in history])
                lhs = C @ D @ A.T
                rhs = np.linalg.det(A)*Ps[a]
                assert np.linalg.norm(lhs-rhs) < 2e-10, (d,split,history,a)
        assert np.isclose(1/(d*rmax), 1/(d*max(map(len,sectors))))
    print("PASS", d)
print("Finite cofactor and sector checks passed; no asymptotic claim is inferred.")
