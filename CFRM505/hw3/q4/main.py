#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def simulate_bond_return(f_t, i_step, f_rate):
    return np.exp(f_rate * (f_t / i_step))


def simulate_multivariate_geometric_brownian_return(f_t, i_step, ar_mu, ar_cov):
    assert ar_mu.ndim == 1
    assert ar_cov.ndim == 2
    assert ar_mu.shape[0] == ar_cov.shape[0] == ar_cov.shape[1]
    f_tau = f_t / i_step
    ar = np.exp(
        np.random.multivariate_normal(
            f_tau * (ar_mu - ar_cov.diagonal() / 2),
            f_tau * ar_cov,
            i_step,
        )
    )
    return ar


def simulate_multivariate_geometric_brownian(f_t, i_step, ar_mu, ar_cov):
    ar = simulate_multivariate_geometric_brownian_return(f_t, i_step, ar_mu, ar_cov)
    ar = np.concatenate((np.ones((1, ar_mu.size)), ar))
    ar = ar.cumprod(axis=0)
    return ar


f_t = 1
i_step = 12
f_sigma_a = 0.2
f_sigma_b = 0.25
f_bal_init = 100000
ar_rho = [-0.5, 0, 0.5]
dict_bal = dict()
for f_rho in ar_rho:
    f_cov = f_rho * f_sigma_a * f_sigma_b
    ar_mu = np.array([0.15, 0.2])
    ar_cov = np.array([[f_sigma_a ** 2, f_cov], [f_cov, f_sigma_b ** 2]])
    dict_bal[f_rho] = f_bal_init * np.sort(
        [
            np.prod(
                0.3 * simulate_bond_return(f_t, i_step, 0.05)
                + simulate_multivariate_geometric_brownian_return(
                    f_t, i_step, ar_mu, ar_cov
                )
                @ np.array([0.4, 0.3])
            )
            for i in range(20000)
        ]
    )

plt.figure()
plt.xlabel("$W_T$")
plt.ylabel("Density")
for f_rho in ar_rho:
    plt.hist(
        dict_bal[f_rho],
        32,
        density=True,
        histtype="stepfilled",
        label=f"$\\rho={f_rho}$",
        alpha=0.5,
    )
plt.legend()
plt.savefig("hist.pdf")

for f_rho in ar_rho:
    print(f_rho, dict_bal[f_rho].mean(), dict_bal[f_rho].var())

plt.figure()
plt.xlabel("$W_T$")
plt.ylabel("Density")
for f_rho in ar_rho:
    ar = dict_bal[f_rho]
    plt.step(ar, np.arange(1, len(ar) + 1) / len(ar), label=f"$\\rho={f_rho}$")
plt.legend()
plt.savefig("hist_cumulative.pdf")

for f_rho in ar_rho:
    for f_p in [0.9, 1.0, 1.1, 1.2, 1.3]:
        ar = dict_bal[f_rho]
        print(f_rho, f_p, np.searchsorted(ar, f_bal_init * f_p) / len(ar))
