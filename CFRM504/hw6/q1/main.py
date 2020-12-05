#!/usr/bin/env python3
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np


def get_brownian_motion(f_t: float, i_n: int) -> np.ndarray:
    ar_0 = np.random.normal(0, np.sqrt(f_t / i_n), i_n - 1)
    return np.array([0] + [sum(ar_0[: i + 1]) for i in range(len(ar_0))])


def get_stock(
    f_stock_init: float,
    f_mu: float,
    f_sigma: float,
    ar_time: np.ndarray,
    ar_wiener: np.ndarray,
) -> np.ndarray:
    assert len(ar_time) == len(ar_wiener)
    return f_stock_init * np.exp(
        (f_mu - f_sigma ** 2 / 2) * ar_time + f_sigma * ar_wiener
    )


def get_bond(f_bond_init: float, f_r: float, ar_time: np.ndarray) -> np.ndarray:
    return np.array([f_bond_init * np.exp(f_r * t) for t in ar_time])


def get_option(
    f_sigma: float,
    f_r: float,
    f_t: float,
    f_p: float,
    ar_time: np.ndarray,
    ar_stock: np.ndarray,
) -> np.ndarray:
    return ar_stock ** f_p * np.exp(
        (f_p - 1) * (2 * f_r + f_p * f_sigma ** 2) / 2 * (f_t - ar_time)
    )


def get_portfolio(
    f_stock_init: float,
    f_mu: float,
    f_sigma: float,
    f_r: float,
    f_t: float,
    f_p: float,
    i_n: int,
    ar_time: np.ndarray,
    ar_wiener: np.ndarray,
    ar_stock: np.ndarray,
) -> np.ndarray:
    ar_delta_s = (
        f_p
        * ar_stock ** f_p
        * np.exp((f_p - 1) * (2 * f_r + f_p * f_sigma ** 2) / 2 * (f_t - ar_time))
    )
    ar_d_wiener = np.diff(ar_wiener)
    f_d_t = f_t / i_n
    ar_portfolio = [
        f_stock_init * np.exp((f_p - 1) * (2 * f_r + f_sigma ** 2 * f_p) * f_t / 2)
    ]
    for i in range(i_n - 1):
        ar_portfolio += [
            ar_portfolio[-1]
            + (f_mu - f_r) * ar_delta_s[i] * f_d_t
            + f_sigma * ar_delta_s[i] * ar_d_wiener[i]
            + f_r * ar_portfolio[-1] * f_d_t
        ]
    return np.array(ar_portfolio)


def get_all(
    f_stock_init: float,
    f_bond_init: float,
    f_mu: float,
    f_sigma: float,
    f_r: float,
    f_t: float,
    f_p: float,
    i_n: int,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    ar_time = np.linspace(0, f_t, i_n)
    ar_wiener = get_brownian_motion(f_t, i_n)
    ar_bond = get_bond(f_bond_init, f_r, ar_time)
    ar_stock = get_stock(f_stock_init, f_mu, f_sigma, ar_time, ar_wiener)
    ar_option = get_option(f_sigma, f_r, f_t, f_p, ar_time, ar_stock)
    ar_portfolio = get_portfolio(
        f_stock_init, f_mu, f_sigma, f_r, f_t, f_p, i_n, ar_time, ar_wiener, ar_stock
    )
    return ar_time, ar_wiener, ar_bond, ar_stock, ar_option, ar_portfolio


def simulate_single(
    f_stock_init: float,
    f_bond_init: float,
    f_mu: float,
    f_sigma: float,
    f_r: float,
    f_t: float,
    f_p: float,
    i_n: int,
):
    ar_time, _, ar_bond, ar_stock, ar_option, ar_portfolio = get_all(
        f_stock_init, f_bond_init, f_mu, f_sigma, f_r, f_t, f_p, i_n
    )
    fig = plt.figure()
    plt.plot(ar_time, ar_bond, figure=fig)
    plt.plot(ar_time, ar_stock, figure=fig)
    plt.plot(ar_time, ar_option, figure=fig)
    plt.plot(ar_time, ar_portfolio, figure=fig)
    plt.legend(["bond $B$", "stock $S$", "option $V$", "portfolio $X$"])
    plt.xlabel("Time")
    plt.ylabel("Price")
    fig.savefig("c_d.pdf")


def simulate_multiple(
    f_stock_init: float,
    f_bond_init: float,
    f_mu: float,
    f_sigma: float,
    f_r: float,
    f_t: float,
    f_p: float,
    i_n: int,
    i_m: int,
):
    ar_diff = []
    for i in range(i_m):
        _, _, _, _, ar_option, ar_portfolio = get_all(
            f_stock_init, f_bond_init, f_mu, f_sigma, f_r, f_t, f_p, i_n
        )
        ar_diff += [ar_portfolio[-1] - ar_option[-1]]
    fig = plt.figure()
    plt.hist(ar_diff, bins=32, density=True, figure=fig)
    plt.xlabel("$X_T-V_T$")
    plt.ylabel("Density")
    fig.savefig("f.pdf")


cin = open("input.txt")
ar = cin.readline().split()
[f_stock_init, f_bond_init, f_mu, f_sigma, f_r, f_t, f_p] = [float(s) for s in ar[:7]]
[i_n, i_m] = [int(s) for s in ar[7:]]
simulate_single(f_stock_init, f_bond_init, f_mu, f_sigma, f_r, f_t, f_p, i_n)
simulate_multiple(f_stock_init, f_bond_init, f_mu, f_sigma, f_r, f_t, f_p, i_n, i_m)
