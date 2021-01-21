#!/usr/bin/env python3
import numpy as np
from scipy.stats import norm


def get_delta_put_formula(f_spot, f_rate, f_vola, f_time, f_strike):
    f0 = (
        1 / f_vola / f_time ** 0.5 * np.log(f_spot / f_strike)
        + f_rate * f_time ** 0.5 / f_vola
    )
    f1 = f_vola * f_time ** 0.5 / 2
    return -norm.cdf(-f0 - f1)


def get_delta_put_pw(f_spot, f_rate, f_vola, f_time, f_strike, i_sample):
    ar0 = np.random.lognormal(
        (f_rate - f_vola ** 2 / 2) * f_time, f_vola * f_time ** 0.5, i_sample
    )
    return -np.exp(-f_rate * f_time) * (f_spot * ar0 < f_strike) * ar0


def get_delta_put_lr(f_spot, f_rate, f_vola, f_time, f_strike, i_sample):
    ar0 = np.random.normal(0, 1, i_sample)
    ar0 *= np.maximum(
        0,
        f_strike
        - f_spot
        * np.exp((f_rate - f_vola ** 2 / 2) * f_time + f_vola * f_time ** 0.5 * ar0),
    )
    return np.exp(-f_rate * f_time) / f_vola / f_time ** 0.5 / f_spot * ar0


def get_gamma_formula(f_spot, f_rate, f_vola, f_time, f_strike):
    f0 = (
        1 / f_vola / f_time ** 0.5 * np.log(f_spot / f_strike)
        + f_rate * f_time ** 0.5 / f_vola
    )
    f1 = f_vola * f_time ** 0.5 / 2
    return 1 / f_spot / f_vola / f_time ** 0.5 * norm.pdf(f0 + f1)


def get_gamma_lr(f_spot, f_rate, f_vola, f_time, f_strike, i_sample):
    ar0 = np.random.normal(0, 1, i_sample)
    ar0 = (1 / f_vola / f_time ** 0.5 * (ar0 ** 2 - 1) - ar0) * np.maximum(
        0,
        f_strike
        - f_spot
        * np.exp((f_rate - f_vola ** 2 / 2) * f_time + f_vola * f_time ** 0.5 * ar0),
    )
    return np.exp(-f_rate * f_time) / f_vola / f_time ** 0.5 / f_spot ** 2 * ar0


def get_gamma_lrpw(f_spot, f_rate, f_vola, f_time, f_strike, i_sample):
    ar0 = np.random.normal(0, 1, i_sample)
    ar0 *= (
        f_spot
        * np.exp((f_rate - f_vola ** 2 / 2) * f_time + f_vola * f_time ** 0.5 * ar0)
        < f_strike
    )
    return -(
        np.exp(-f_rate * f_time) * f_strike / f_vola / f_time ** 0.5 / f_spot ** 2 * ar0
    )


def get_gamma_pwlr(f_spot, f_rate, f_vola, f_time, f_strike, i_sample):
    ar0 = np.random.normal(0, 1, i_sample)
    ar1 = np.exp((f_rate - f_vola ** 2 / 2) * f_time + f_vola * f_time ** 0.5 * ar0)
    ar2 = (1 / f_vola / f_time ** 0.5 * ar0 - 1) * (f_spot * ar1 < f_strike) * ar1
    return -np.exp(-f_rate * f_time) / f_spot * ar2


d = {"f_spot": 100, "f_rate": 0.03, "f_vola": 0.25, "f_time": 0.5}
i_sample = 100000

print(r"  K &         ∆ &    E_∆_PW &    E_∆_LR & Var_V_PW & Var_V_LR \\")
for f_strike in [90, 100, 110]:
    f_formula = get_delta_put_formula(**d, f_strike=f_strike)
    ar_pw = get_delta_put_pw(**d, f_strike=f_strike, i_sample=i_sample)
    ar_lr = get_delta_put_lr(**d, f_strike=f_strike, i_sample=i_sample)
    print(
        f"{f_strike:3} & {f_formula:9.6f} & "
        f"{ar_pw.mean():9.6f} & {ar_lr.mean():9.6f} & "
        fr"{ar_pw.var():8.6f} & {ar_lr.var():8.6f} \\"
    )
print()

print(
    "  K &         Γ & "
    "   E_Γ_LR &  E_Γ_LRPW &  E_Γ_PWLR & "
    r" Var_Γ_LR & Var_Γ_LRPW & Var_Γ_PWLR \\"
)
for f_strike in [90, 100, 110]:
    f_formula = get_gamma_formula(**d, f_strike=f_strike)
    ar_lr = get_gamma_lr(**d, f_strike=f_strike, i_sample=i_sample)
    ar_lrpw = get_gamma_lrpw(**d, f_strike=f_strike, i_sample=i_sample)
    ar_pwlr = get_gamma_pwlr(**d, f_strike=f_strike, i_sample=i_sample)
    print(
        f"{f_strike:3} & {f_formula:9.7f} & "
        f"{ar_lr.mean():9.7f} & {ar_lrpw.mean():9.7f} & {ar_pwlr.mean():9.7f} & "
        fr"{ar_lr.var():9.7f} & {ar_lrpw.var():10.7f} & {ar_pwlr.var():10.7f} \\"
    )
