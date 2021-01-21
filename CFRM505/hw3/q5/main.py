#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def simulate_geometric_brownian_return(f_t, i_n, f_mu, f_sigma):
    return np.random.lognormal(
        (f_mu - f_sigma ** 2 / 2) * (f_t / i_n), f_sigma * (f_t / i_n) ** 0.5, i_n
    )


def simulate_geometric_brownian(f_t, i_step, f_mu, f_sigma):
    ar = simulate_geometric_brownian_return(f_t, i_step, f_mu, f_sigma)
    ar = np.concatenate(([1], ar))
    ar = ar.cumprod()
    return ar


f_t = 1
i_step = 252
f_mu = 0.05

plt.figure()
ax0 = plt.gca()
ax0.set_xlabel("Time")
ax0.set_ylabel("Relative Drawdown")
ax0.invert_yaxis()
ax0.margins(y=0)
ax0.tick_params(axis="y", colors="C1")
ax1 = ax0.twinx()
ax1.set_ylabel("Price")
ax1.tick_params(axis="y", colors="C0", top=0)
ar_x = np.linspace(0, 1, i_step + 1)
ar_price = simulate_geometric_brownian(f_t, i_step, f_mu, 0.15)
ar_drawdown = np.maximum.accumulate(ar_price) / ar_price - 1
ax0.fill_between(ar_x, 1 * ar_drawdown, alpha=0.5, color="C1")
ax0.set_ylim(ax0.get_ylim()[0] * 2)
ax1.plot(ar_x, ar_price, color="C0")
plt.savefig("path.pdf")

plt.figure()
plt.xlabel("Volatility")
plt.ylabel("Expected Max. Relative Drawdown")
ar_x = np.arange(0.1, 0.4, 0.02)
ar_y = []
for f_sigma in ar_x:
    i_sample = 10000
    f_sum_drawdown = 0
    for i in range(i_sample):
        ar_price = simulate_geometric_brownian(f_t, i_step, f_mu, f_sigma)
        ar_drawdown = np.maximum.accumulate(ar_price) / ar_price - 1
        f_sum_drawdown += ar_drawdown.max()
    ar_y += [f_sum_drawdown / i_sample]
plt.plot(ar_x, ar_y, "o-")
plt.savefig("drawdown.pdf")
