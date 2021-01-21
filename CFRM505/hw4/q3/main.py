#!/usr/bin/env python3
import numpy as np

f_lambda1 = 0.05
f_lambda2 = 0.05
ar_1 = np.random.exponential(1 / f_lambda1, 1000000)
ar_2 = np.random.exponential(1 / f_lambda2, 1000000)
ar_1 = 1 / f_lambda1 * np.exp((-1 + f_lambda1) * ar_1) * (ar_1 > 20)
ar_2 = 2 / f_lambda2 * np.exp((-2 + f_lambda2) * ar_2) * (ar_2 > 20)
f_mean = 1 - (1 - ar_1.mean()) * (1 - ar_2.mean())
f_var = (
    (1 - ar_1.mean()) ** 2 * ar_2.var()
    + (1 - ar_2.mean()) ** 2 * ar_1.var()
    + ar_1.var() * ar_2.var()
)
print(f_mean, f_var)
