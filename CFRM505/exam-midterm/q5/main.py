#!/usr/bin/env python3
import numpy as np
from scipy.stats import norm

i_sample = 50000
i_pilot = 1000
f_delta = 0.05
f_epsilon = 0.01
f_z = norm.ppf(1 - f_delta / 2)


def stat(ar):
    mean = ar.mean()
    std = ar.std()
    intv_dev = f_z * std / i_sample ** 0.5
    print(
        f"Mean = {mean:.5f}\t"
        f"Std = {std:8.5f}\t"
        f"Conf Interv = {mean-intv_dev:.5f}, {mean+intv_dev:.5f}"
    )


ar_z_pilot = np.exp(
    np.random.uniform(-0.5, 1.5, i_pilot) + np.random.normal(-0.2, 2 ** 0.5, i_pilot)
)
ar_x_pilot = np.maximum(0, ar_z_pilot - 2)
f_z_mean = (np.exp(2.3) - np.exp(0.3)) / 2
f_z_var = ((ar_z_pilot - f_z_mean) ** 2).sum() / (i_pilot - 1)
f_c = -np.cov(ar_z_pilot, ar_x_pilot)[0][1] / f_z_var

ar_z = np.exp(
    np.random.uniform(-0.5, 1.5, i_sample) + np.random.normal(-0.2, 2 ** 0.5, i_sample)
)
ar_x = np.maximum(0, ar_z - 2)
ar_y = ar_x + f_c * (ar_z - f_z_mean)
print("Crude MC")
stat(ar_x)
print("Control variate")
stat(ar_y)
print(f"The variance is reduced by {1 - ar_y.var() / ar_x.var()}")
