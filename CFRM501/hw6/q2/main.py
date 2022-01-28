#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
from sklearn.decomposition import PCA as PCA1
from statsmodels.multivariate.pca import PCA as PCA0


def step0_distribution_of_sum(df_x, s_filename):
    sr_l = df_x[0] + df_x[1] + df_x[2] + df_x[3]
    f_mean = sr_l.mean()
    f_var = sr_l.var()
    f_std = sr_l.std()
    print(f"mean of L is     {f_mean}")
    print(f"variance of L is {f_var}")

    fig = plt.figure()
    ax = fig.subplots()
    ax.set_ylabel("Density")
    ax.set_xlabel("$L$")
    sr_l.hist(ax=ax, density=True, bins=32)
    x = np.linspace(sr_l.min(), sr_l.max(), 128)
    plt.plot(x, stats.norm.pdf(x, f_mean, f_std), figure=fig)
    fig.savefig(f"{s_filename}.pdf")


def step0_method0(df_x: pd.DataFrame):
    sr_mean = df_x.mean()
    df_cov = df_x.cov()
    eigenval, eigenvec = np.linalg.eig(df_cov)
    idx = eigenval.argsort()[::-1]
    eigenval = eigenval[idx][:2]
    eigenvec = eigenvec[:, idx][:, :2]
    return eigenval, eigenvec, (df_x - sr_mean) @ eigenvec @ eigenvec.T + sr_mean


def step0_method1(df_x: pd.DataFrame):
    sr_mean = df_x.mean()
    pc = PCA0(df_x, ncomp=2, standardize=False, method="eig")
    return (
        pc.eigenvals / df_x.shape[0],
        pc.eigenvecs,
        (df_x - sr_mean) @ pc.eigenvecs @ pc.eigenvecs.T + sr_mean,
    )


def step0_method2(df_x: pd.DataFrame):
    pc = PCA1(n_components=2).fit(df_x)
    return (
        pc.explained_variance_,
        pc.components_,
        pc.inverse_transform(pc.transform(df_x)),
    )


def step0():
    df_x = pd.read_csv("data.csv", header=None)
    step0_distribution_of_sum(df_x, "1")
    eigenval, eigenvec, df_estimation = step0_method0(df_x)
    print("eigenvalues are")
    print(eigenval)
    print("eigenvectors are")
    print(eigenvec.T)
    step0_distribution_of_sum(df_estimation, "3")


step0()
