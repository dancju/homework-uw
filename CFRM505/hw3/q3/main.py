#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def simulate_bond_return(f_t, i_step, f_rate):
    return np.exp(f_rate * (f_t / i_step))


def simulate_geometric_brownian_return(f_t, i_n, f_mu, f_sigma):
    return np.random.lognormal(
        (f_mu - f_sigma ** 2 / 2) * (f_t / i_n), f_sigma * (f_t / i_n) ** 0.5, i_n
    )


f_bal_init = 100000
ar_bal = f_bal_init * np.sort(
    [
        np.prod(
            0.4 * simulate_bond_return(1, 12, 0.05)
            + 0.6 * simulate_geometric_brownian_return(1, 12, 0.15, 0.2)
        )
        for i in range(20000)
    ]
)

plt.figure()
plt.xlabel("$W_T$")
plt.ylabel("Density")
plt.hist(ar_bal, 32, density=True)
plt.savefig("hist.pdf")

print(np.mean(ar_bal))
print(np.var(ar_bal))

plt.figure()
plt.xlabel("$W_T$")
plt.ylabel("Density")
plt.step(ar_bal, np.arange(1, len(ar_bal) + 1) / len(ar_bal))
plt.savefig("hist_cumulative.pdf")

for p in [0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]:
    print(p, np.searchsorted(ar_bal, f_bal_init * p) / len(ar_bal))
