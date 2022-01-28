#!/usr/bin/env python3
import numpy as np


def generate_poisson_(f_lam):
    j = 0
    f_p = np.exp(-f_lam)
    f_f = f_p
    f_u = np.random.rand()
    while f_u > f_f:
        f_p *= f_lam / (j + 1)
        f_f += f_p
        j += 1
    return j


def generate_poisson(f_lam, i_size):
    return np.array([generate_poisson_(f_lam) for i in range(i_size)])


data = generate_poisson(f_lam=1, i_size=10000)
print(data.mean())
print(data.var())
