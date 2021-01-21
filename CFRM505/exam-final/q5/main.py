#!/usr/bin/env python3
import numpy as np
from scipy.stats import norm

f_rho = 0.5
i_sample = int(1e6)
ar = np.random.normal(0, 1, i_sample)
ar = norm.cdf((ar * f_rho ** 0.5 - 2) / (1 - f_rho) ** 0.5)
print(2 * (ar - ar ** 2).mean() + 4 * ar.var())
