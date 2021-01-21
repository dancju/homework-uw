#!/usr/bin/env python3
import numpy as np


def rho_pw(f_init, f_rate, f_vola, f_time, f_p, f_strike, ar_z):
    ar = np.exp((f_rate - f_vola ** 2 / 2) * f_time + f_vola * f_time ** 0.5 * ar_z)
    ar = (ar * f_init) ** f_p
    ar = np.maximum(0, f_strike - ar) + f_p * (f_strike > ar) * ar
    return -np.exp(-f_rate * f_time) * f_time * ar


def rho_lr(f_init, f_rate, f_vola, f_time, f_p, f_strike, ar_z):
    ar_0 = np.exp((f_rate - f_vola ** 2 / 2) * f_time + f_vola * f_time ** 0.5 * ar_z)
    ar_1 = np.maximum(0, f_strike - (f_init * ar_0) ** f_p)
    ar_2 = f_time ** 0.5 / f_vola * ar_z - f_time
    return np.exp(-f_rate * f_time) * ar_1 * ar_2


d = {
    "f_init": 10,
    "f_rate": 0.03,
    "f_vola": 0.2,
    "f_time": 1,
    "f_p": 2,
    "f_strike": 100,
    "ar_z": np.random.normal(0, 1, int(1e6)),
}
ar = rho_pw(**d)
print(ar.mean(), ar.var())
ar = rho_lr(**d)
print(ar.mean(), ar.var())
