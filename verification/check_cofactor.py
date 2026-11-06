#!/usr/bin/env python3
"""Finite cofactor identities and the converse's explicit singular witness."""
from __future__ import annotations
import itertools
import numpy as np
from check_full_channel import basis

def cofactor(a: np.ndarray) -> np.ndarray:
    d = a.shape[0]
    c = np.empty_like(a)
    for i in range(d):
        for j in range(d):
            c[i, j] = (-1)**(i+j) * np.linalg.det(np.delete(np.delete(a, i, axis=0), j, axis=1))
    return c

def run() -> dict:
    largest = 0.0
    histories = 0
    for d in (2, 3, 4):
        u = basis(d, 100+d)
        for split in range(1, d):
            sectors = [list(range(split)), list(range(split, d))]
            projectors = [u[:, s] @ u[:, s].conj().T for s in sectors]
            for history in itertools.product(range(d), repeat=d):
                a = np.column_stack([u[:, j].conj() for j in history])
                c = cofactor(a)
                histories += 1
                for label, sector in enumerate(sectors):
                    selector = np.diag([int(j in sector) for j in history])
                    error = float(np.linalg.norm(c @ selector @ a.T - np.linalg.det(a) * projectors[label]))
                    largest = max(largest, error)
                    if error >= 2e-11:
                        raise AssertionError((d, split, history, label, error))
    witnesses = 0
    for d in range(2, 7):
        for rank in range(1, d):
            t = np.eye(d)
            inside, outside = 0, rank
            t[np.ix_([inside, outside], [inside, outside])] = 1
            e = np.diag([1]*rank+[0]*(d-rank))
            f = cofactor(t).T @ e @ t
            block = f[np.ix_([inside, outside], [inside, outside])]
            if not (abs(np.linalg.det(t)) < 1e-12 and np.array_equal(block, [[1.,1.],[-1.,-1.]])):
                raise AssertionError((d, rank, t, f))
            witnesses += 1
    return {"status":"pass", "histories": histories, "largest_cofactor_error":largest, "singular_witnesses":witnesses}

if __name__ == '__main__':
    import json
    print(json.dumps(run(), indent=2))
