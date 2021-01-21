#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

f_init = 10
f_strike = 11
f_mu = 0.08
f_time = 1
i_sample = int(1e5)
ar_v = np.random.uniform(0.1, 0.5, i_sample)
ar = np.log(f_strike / f_init) - (f_mu - ar_v ** 2 / 2) * f_time
ar = ar / ar_v / f_time ** 0.5
ar = 1 - norm.cdf(ar)
print(ar.mean(), ar.var())
plt.figure()
plt.hist(ar, 64, density=True)
plt.xlabel(r"$\Pr(S_T>K|V)$")
plt.ylabel("Density")
plt.savefig("c.pdf")
