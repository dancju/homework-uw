#!/usr/bin/env python3
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

N_D_IN_Y = 252
L_STOCK = ["AAPL", "BBBY", "EBAY", "GE", "GOOG", "INTC", "MMM", "MSFT", "ORCL", "TEVA"]


def step0() -> pd.DataFrame:
    df = pd.DataFrame()
    for s_stock in L_STOCK:
        df_t = pd.read_csv(s_stock + ".csv", index_col="Date")
        df_t = df_t["Adj Close"].pct_change().dropna()
        df[s_stock] = df_t
    return df


def step1_annualize_covariance(mean_d: pd.Series, cov_d: pd.DataFrame) -> pd.DataFrame:
    df = (mean_d + 1).to_frame()
    df = df @ df.T
    return (cov_d + df) ** N_D_IN_Y - df**N_D_IN_Y


def step1a() -> Tuple[pd.Series, pd.DataFrame]:
    df_data = step0()
    sr_mean_d = df_data.mean()
    sr_mean_a = (sr_mean_d + 1) ** N_D_IN_Y - 1
    df_cov_d = df_data.cov()
    df_cov_a = step1_annualize_covariance(sr_mean_d, df_cov_d)
    return sr_mean_a, df_cov_a


def step1b() -> Tuple[
    pd.Series,
    pd.Series,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
]:
    sr_mean, df_cov = step1a()
    sr_std = pd.Series(np.diag(df_cov) ** 0.5, index=sr_mean.index)
    sr_std_inv = sr_std.apply(lambda x: 1 / x)
    df_cor = df_cov.multiply(sr_std_inv, axis=0).multiply(sr_std_inv, axis=1)
    df_cor_add = df_cor + 0.1
    df_cor_sub = df_cor - 0.1
    df_cov_add = df_cor_add.multiply(sr_std, axis=0).multiply(sr_std, axis=1)
    df_cov_sub = df_cor_sub.multiply(sr_std, axis=0).multiply(sr_std, axis=1)
    for i in sr_mean.index:
        df_cov_sub[i][i] = df_cov[i][i]
        df_cov_add[i][i] = df_cov[i][i]
    return sr_mean, sr_std, df_cov, df_cov_add, df_cov_sub


def step2_get_vertex(
    sr_mean: pd.Series, df_cov: pd.DataFrame, ar_cov_inv: np.ndarray
) -> Tuple[pd.Series, float, float]:
    ar_weights = ar_cov_inv @ np.ones(len(ar_cov_inv)) / ar_cov_inv.sum()
    f_mean = ar_weights @ sr_mean
    f_var = ar_weights @ df_cov @ ar_weights
    return pd.Series(ar_weights, index=sr_mean.index), f_mean, f_var


def step2_get_boundry(
    sr_mean: pd.Series,
    df_cov: pd.DataFrame,
    ar_cov_inv: np.ndarray,
    f_mean_global: float,
    f_var_global: float,
) -> pd.DataFrame:
    ar_ones = np.ones(len(df_cov))
    f_a = ar_cov_inv.sum()
    f_b = ar_ones @ ar_cov_inv @ sr_mean
    f_c = sr_mean @ ar_cov_inv @ sr_mean
    f_p = f_a * f_c - f_b**2
    df_boundry = pd.DataFrame()
    for f_mean in np.linspace(sr_mean.min(), sr_mean.max(), 32):
        f_l1 = (f_b * f_mean - f_c) / f_p
        f_l2 = (f_b - f_a * f_mean) / f_p
        ar_weights = -f_l1 * ar_cov_inv @ ar_ones - f_l2 * ar_cov_inv @ sr_mean
        f_mean = ar_weights @ sr_mean
        f_var = f_var_global + (f_mean - f_mean_global) ** 2 / f_p / f_var_global
        df_boundry = pd.concat(
            [df_boundry, pd.DataFrame([{"mean": f_mean, "std": f_var**0.5}])],
            ignore_index=True,
        )
    return df_boundry


def step2_get_vertex_boundry(sr_mean: pd.Series, df_cov: pd.DataFrame) -> dict:
    ar_cov_inv = np.linalg.inv(df_cov.values)
    sr_weights, f_mean, f_var = step2_get_vertex(sr_mean, df_cov, ar_cov_inv)
    df_boundry = step2_get_boundry(sr_mean, df_cov, ar_cov_inv, f_mean, f_var)
    return {
        "sr_weights": sr_weights,
        "f_mean": f_mean,
        "f_std": f_var**0.5,
        "df_boundry": df_boundry,
    }


def step2() -> Tuple[pd.Series, pd.Series, dict, dict, dict]:
    sr_mean, sr_std, df_cov, df_cov_add, df_cov_sub = step1b()
    d_res = step2_get_vertex_boundry(sr_mean, df_cov)
    d_res_add = step2_get_vertex_boundry(sr_mean, df_cov_add)
    d_res_sub = step2_get_vertex_boundry(sr_mean, df_cov_sub)
    return sr_mean, sr_std, d_res, d_res_add, d_res_sub


def step3_plot(
    s_label: str,
    sr_weights: pd.Series,
    f_mean: float,
    f_std: float,
    df_boundry: pd.DataFrame,
) -> None:
    # print weights, mean, and std
    print("# " + s_label)
    print(f"Mean {f_mean}")
    print(f"Std   {f_std}")
    print(sr_weights)
    print()
    # scatter of vertex
    plt.scatter([f_std], [f_mean])
    # boundry
    plt.plot(df_boundry["std"], df_boundry["mean"], alpha=0.6, label=s_label)


def step3() -> None:
    sr_mean, sr_std, d_res, d_res_add, d_res_sub = step2()
    # vertices and boundries
    step3_plot("real data", **d_res)
    step3_plot("corr$=-0.1$", **d_res_sub)
    step3_plot("corr$=+0.1$", **d_res_add)
    # scatter of stocks
    plt.scatter(sr_std, sr_mean)
    # text of stocks
    for i in range(len(sr_mean)):
        plt.text(x=sr_std[i], y=sr_mean[i], s=sr_mean.index[i], fontsize=9)
    # misc
    plt.legend()
    plt.xlabel("Standard Deviation")
    plt.ylabel("Mean")
    plt.savefig("main.pdf")


step3()
