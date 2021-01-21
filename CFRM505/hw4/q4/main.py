#!/usr/bin/env python3
import numpy as np

f_mu1 = 5.1
f_si1 = 0.3
f_mu2 = 5.2
f_si2 = 0.6
ar_1 = np.random.normal(f_mu1, f_si1, 1000000)
ar_2 = np.random.normal(f_mu2, f_si2, 1000000)
ar_1 = (
    f_si1 * np.exp(-(ar_1 ** 2) / 2 + (ar_1 - f_mu1) ** 2 / f_si1 ** 2 / 2) * (ar_1 > 5)
)
ar_2 = (
    f_si2
    / 2 ** 0.5
    * np.exp(-(ar_2 ** 2) / 4 + (ar_2 - f_mu2) ** 2 / f_si2 ** 2 / 2)
    * (ar_2 > 5)
)
f_mean = ar_1.mean() * ar_2.mean()
f_var = (
    ar_1.mean() ** 2 * ar_2.var()
    + ar_2.mean() ** 2 * ar_1.var()
    + ar_1.var() * ar_2.var()
)
print(f_mean, f_var)
