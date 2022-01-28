#!/usr/bin/env python3
from math import comb

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def pmf(f_p, f_rho, i_m, i_l):
    ar_z = np.random.normal(0, 1, 1000)
    ar_p = 1 - norm.cdf((norm.ppf(1 - f_p) - f_rho ** 0.5 * ar_z) / (1 - f_rho) ** 0.5)
    ar0 = comb(i_m, i_l) * ar_p ** i_l * (1 - ar_p) ** (i_m - i_l)
    return ar0.mean()


for i_m in [10, 25, 50]:
    plt.figure()
    plt.xlabel(r"$\ell$")
    plt.ylabel(r"$\Pr(L=\ell)$")
    # plt.yscale("log")
    ar_l = range(i_m + 1)
    for f_rho in [0.2, 0.5, 0.8]:
        ar_pmf = np.array([pmf(0.01, f_rho, i_m, i_l) for i_l in ar_l])
        plt.scatter(ar_l, ar_pmf, marker=".", label=fr"$\rho={f_rho}$")
    plt.legend()
    plt.savefig(f"pmf_l_{i_m}.pdf")
