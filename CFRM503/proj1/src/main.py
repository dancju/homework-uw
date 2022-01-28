#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from cvxopt import matrix, solvers


def get_data0():
    df = pd.read_excel("REIT_Data.xlsx", skiprows=1, index_col="Symbol")
    df = pd.DataFrame({"mcap": df["Market Capitalization"]})
    df = df.filter(regex="^[D-H]", axis=0)
    df["wei_cur"] = df.index.map(lambda x: x[0] in "DEF") * df["mcap"]
    df["wei_fut"] = df.index.map(lambda x: x[0] in "FGH") * df["mcap"]
    df["wei_cur"] /= df["wei_cur"].sum()
    df["wei_fut"] /= df["wei_fut"].sum()
    return pd.to_numeric(df["wei_cur"]), pd.to_numeric(df["wei_fut"])


def get_data1():
    df = pd.read_csv("REIT_Forecast.csv", index_col="Symbol")
    df = df.filter(regex="^[D-H]", axis=0)
    df_cor = df.drop(columns=["Name", "Mean", "Stdev"])
    df_cor = df_cor.filter(regex="^[D-H]", axis=1)
    assert df.index.equals(df_cor.columns)
    ar_std = np.diag(df["Stdev"])
    ar_cov = ar_std @ df_cor.to_numpy() @ ar_std
    return df["Mean"], ar_cov


def get_data():
    sr_wei_cur, sr_wei_fut = get_data0()
    sr_mean, ar_cov = get_data1()
    assert sr_wei_cur.index.equals(sr_mean.index)
    return sr_wei_cur, sr_wei_fut, sr_mean, ar_cov


def get_weight_optimal(sr_wei_cur, sr_wei_fut, sr_mean, ar_cov):
    i_dim = ar_cov.shape[0]
    l_index = range(4, -1, -1)
    l_alpha = [1, 0.8, 0.6, 0.3, 0]
    l_benchmark = [sr_wei_cur, sr_wei_cur, sr_wei_cur, sr_wei_cur, sr_wei_fut]
    df_wei = pd.DataFrame(index=sr_mean.index)
    for i, f_alpha, sr_benchmark in zip(l_index, l_alpha, l_benchmark):
        res = solvers.qp(
            matrix(ar_cov),
            -matrix(ar_cov @ (f_alpha * sr_wei_cur + (1 - f_alpha) * sr_wei_fut)),
            -matrix(
                np.concatenate([np.eye(i_dim), sr_mean.to_numpy().reshape(1, i_dim)])
            ),
            -matrix(
                np.array([0] * i_dim + [sr_mean @ sr_benchmark + 0.0002]).reshape(
                    i_dim + 1, 1
                )
            ),
            matrix(np.ones((1, i_dim))),
            matrix(1.0),
        )
        assert res["status"] == "optimal"
        df_wei[i] = np.array(res["x"]).squeeze()
    print(df_wei.round(6))
    return df_wei


def plot_tracking_error(df_wei, sr_wei_cur, sr_wei_fut, ar_cov):
    l_index = range(4, -1, -1)
    l_cur = [(df_wei[i] - sr_wei_cur) for i in l_index]
    l_cur = [i @ ar_cov @ i for i in l_cur]
    l_cur = [i ** 0.5 for i in l_cur]
    l_fut = [(df_wei[i] - sr_wei_fut) for i in l_index]
    l_fut = [i @ ar_cov @ i for i in l_fut]
    l_fut = [i ** 0.5 for i in l_fut]
    df = pd.DataFrame({"err_cur": l_cur, "err_fut": l_fut}, index=l_index).T
    print(df)
    plt.figure()
    plt.plot(l_cur, "o-", label="Current")
    plt.plot(l_fut, "o-", label="Future")
    plt.xticks([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])
    plt.legend()
    plt.xlabel("# of Weeks before Reconstitution")
    plt.ylabel("Tracking Error")
    plt.savefig("tracking_error.pdf")


def plot_excess_return(df_wei, sr_wei_cur, sr_wei_fut, sr_mean):
    l_index = range(4, -1, -1)
    l_cur = [sr_mean @ (df_wei[i] - sr_wei_cur) for i in l_index]
    l_fut = [sr_mean @ (df_wei[i] - sr_wei_fut) for i in l_index]
    df = pd.DataFrame({"ret_cur": l_cur, "ret_fut": l_fut}, index=l_index).T
    print(df)
    plt.figure()
    plt.plot(l_cur, "o-", label="Current")
    plt.plot(l_fut, "o-", label="Future")
    plt.xticks([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])
    plt.legend()
    plt.xlabel("# of Weeks before Reconstitution")
    plt.ylabel("Expected Excess Return")
    plt.savefig("excess_return.pdf")


def main():
    sr_wei_cur, sr_wei_fut, sr_mean, ar_cov = get_data()
    df_wei = get_weight_optimal(sr_wei_cur, sr_wei_fut, sr_mean, ar_cov)
    plot_tracking_error(df_wei, sr_wei_cur, sr_wei_fut, ar_cov)
    plot_excess_return(df_wei, sr_wei_cur, sr_wei_fut, sr_mean)


if __name__ == "__main__":
    main()
