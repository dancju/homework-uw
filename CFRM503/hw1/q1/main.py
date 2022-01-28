#!/usr/bin/env python3
import numpy as np
from cvxopt import matrix, solvers

ar_mean = np.array([0.13, 0.1, 0.08])
ar_std = np.diag([0.2, 0.18, 0.12])
ar_cor = np.array([[1, 0.6, 0.5], [0.6, 1, 0.3], [0.5, 0.3, 1]])
ar_cov = ar_std @ ar_cor @ ar_std

n = 3
ar_res = []

for f_tol in np.linspace(np.finfo(float).eps, 0.8, 100):
    res = solvers.qp(
        matrix(ar_cov),
        -matrix(f_tol * ar_mean),
        -matrix(np.eye(n)),
        -matrix(np.zeros((n, 1))),
        matrix(np.ones((1, n)), (1, n)),
        matrix(1.0),
    )
    ar_w = np.array(res["x"]).squeeze()
    ar_res.append((f_tol, ar_mean @ ar_w, (ar_w.T @ ar_cov @ ar_w) ** 0.5, *ar_w))

for i in ar_res:
    print(f"{i[0]:8.6f} {i[1]:8.6f} {i[2]:8.6f} {i[3]:8.6f} {i[4]:8.6f} {i[5]:8.6f}")
