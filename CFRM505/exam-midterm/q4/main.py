#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def generate_cir_2(
    f_theta0,
    f_theta1,
    f_mu0,
    f_mu1,
    f_sigma0,
    f_sigma1,
    f_init0,
    f_init1,
    f_time,
    i_step,
    f_rho,
):
    f_tau = f_time / i_step
    ar0 = [f_init0]
    ar1 = [f_init1]
    for _ in range(i_step):
        f_brownian0 = np.random.normal(0, f_tau ** 0.5)
        f_brownian1 = np.random.normal(
            f_rho * f_brownian0, (1 - f_rho ** 2) ** 0.5 * f_tau ** 0.5
        )
        ar0 += [
            ar0[-1]
            + f_theta0 * (f_mu0 - ar0[-1]) * f_tau
            + f_sigma0 * ar0[-1] ** 0.5 * f_brownian0
        ]
        ar1 += [
            ar1[-1]
            + f_theta1 * (f_mu1 - ar1[-1]) * f_tau
            + f_sigma1 * ar1[-1] ** 0.5 * f_brownian1
        ]
    return ar0[-1], ar1[-1]


x = np.array(
    [generate_cir_2(10, 16, 15, 10, 6, 3, 0, 0, 2, 250, 0.2) for _ in range(1000)]
).T
print("E(X_2)   = ", x.mean(axis=1))
print("Var(X_2) = ", x.var(axis=1))

ar_rho = [-0.8, -0.2, 0, 0.2, 0.8]
ar_corr = [
    np.corrcoef(
        np.array(
            [
                generate_cir_2(10, 16, 15, 10, 6, 3, 0, 0, 2, 250, f_rho)
                for _ in range(1000)
            ]
        ).T
    )[0][1]
    for f_rho in ar_rho
]
plt.xlabel(r"$\rho$")
plt.ylabel(r"Corr$\left(X_2,\widetilde X_2\right)$")
plt.plot(ar_rho, ar_corr, "o-")
plt.savefig("main.pdf")
