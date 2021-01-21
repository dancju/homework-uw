#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def get_corr(f_rho):
    i_sample = 10000
    z0 = np.random.normal(0, 1, i_sample)
    z1 = np.random.normal(0, 1, i_sample)
    v0 = z0
    v1 = f_rho * z0 + (1 - f_rho ** 2) ** 0.5 * z1
    w0 = norm.cdf(v0)
    w1 = norm.cdf(v1)
    x0 = 3 - 2 * np.log(np.e + (1 - np.e) * w0)
    x1 = 5 - np.log(np.exp(3) + (1 - np.exp(3)) * w1)
    return np.corrcoef(x0, x1)[0][1]


ar_rho = np.linspace(-1, 1, 21)
ar_corr = [get_corr(f_rho) for f_rho in ar_rho]
plt.xlabel(r"$\rho$")
plt.ylabel(r"Corr$\left(Y,\widetilde Y\right)$")
plt.plot(ar_rho, ar_corr, "o-")
plt.savefig("main.pdf")
