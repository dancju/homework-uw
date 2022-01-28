#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def cdf_y(f_p, f_rho, f_y):
    return norm.cdf(
        (norm.ppf(1 - f_p) - (1 - f_rho) ** 0.5 * norm.ppf(1 - f_y)) / f_rho ** 0.5
    )


plt.xlabel("$y$")
plt.ylabel(r"$\Pr(Y<y)$")
# plt.xscale("log")
ar_x = np.exp(np.linspace(np.log(1e-7), np.log(1), 256))
for f_rho in [0.2, 0.5, 0.8]:
    plt.plot(
        ar_x,
        np.array([cdf_y(0.01, f_rho, i) for i in ar_x]),
        label=fr"$\rho={f_rho}$",
    )
plt.legend()
plt.savefig("cdf_y.pdf")
