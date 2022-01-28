#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

f_init = 10
f_strike = 11
f_mu = 0.08
f_time = 1
i_sample = int(1e5)
ar_v = np.random.uniform(0.1, 0.5, i_sample)
ar_z = np.random.normal(0, 1, i_sample)
ar = f_init * np.exp((f_mu - ar_v ** 2 / 2) * f_time + f_time ** 0.5 * ar_v * ar_z)
ar = 1 * (ar > f_strike)
print(ar.mean(), ar.var())
plt.figure()
plt.hist(ar, 2, density=True)
plt.xlabel("$1_{S_T>K}$")
plt.ylabel("Density")
plt.savefig("a.pdf")
