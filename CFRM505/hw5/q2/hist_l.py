#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def get_l(i_m, f_rho, f_p):
    f_z = np.random.normal(0, 1)
    ar_eps = np.random.normal(0, 1, i_m)
    ar0 = f_rho ** 0.5 * f_z + (1 - f_rho) ** 0.5 * ar_eps
    ar0 = ar0 > norm.ppf(1 - f_p)
    return ar0.sum()


ar_l = np.array([get_l(50, 0.5, 0.01) for i in range(100000)])
print(f"Pr(L > 10) = {(ar_l > 10).sum() / ar_l.size}")
plt.xlabel("$L$")
plt.ylabel("Density")
plt.hist(ar_l, range(51), density=True)
plt.savefig("hist_l.pdf")
