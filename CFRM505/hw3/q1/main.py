#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def simulate_ornstein_uhlenbeck(f_time, i_step, f_init, f_theta, f_mu, f_sigma):
    f_tau = f_time / i_step
    ar = [f_init]
    for j in range(i_step):
        ar += [
            ar[-1]
            + np.random.normal(
                f_theta * (f_mu - ar[-1]) * f_tau, f_sigma * f_tau ** 0.5
            )
        ]
    return np.array(ar)


f_t = 1
i_step = 100
f_mu = 1
f_theta = 1
f_sigma = 0.1
f_init = 0

plt.figure()
plt.xlabel("$t$")
plt.ylabel("$P_t$")
plt.plot(
    np.linspace(0, f_t, i_step + 1),
    np.exp(simulate_ornstein_uhlenbeck(f_t, i_step, f_init, f_theta, f_mu, f_sigma)),
)
plt.savefig("path.pdf")

plt.figure()
plt.xlabel("$P_1$")
plt.ylabel("Density")
ar = [
    np.exp(simulate_ornstein_uhlenbeck(f_t, i_step, f_init, f_theta, f_mu, f_sigma)[-1])
    for i in range(10000)
]
print(np.mean(ar))
plt.hist(ar, 32, density=True, label="frequency")
f_mean = f_mu * (1 - np.exp(-f_theta))
f_std = (f_sigma ** 2 / 2 / f_theta * (1 - np.exp(-2 * f_theta))) ** 0.5
ar_x = np.linspace(np.exp(f_mean - 4 * f_std), np.exp(f_mean + 4 * f_std), 1024)
ar_y = stats.lognorm.pdf(ar_x, f_std, 0, np.exp(f_mean))
plt.plot(ar_x, ar_y, label="probability")
plt.legend()
plt.savefig("hist.pdf")
