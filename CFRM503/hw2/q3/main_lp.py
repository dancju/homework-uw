#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize, sparse


def get_data():
    ar_mean = np.array([0.13, 0.1, 0.08])
    ar_std = np.diag([0.2, 0.18, 0.12])
    ar_cor = np.array([[1, 0.6, 0.5], [0.6, 1, 0.3], [0.5, 0.3, 1]])
    ar_cov = ar_std @ ar_cor @ ar_std
    return 3, ar_mean, ar_cov


def get_frontier_var(n, ar_mean, ar_cov):
    ar_ones = np.ones(n)
    ar_cov_inv = np.linalg.inv(ar_cov)
    f_a = ar_ones @ ar_cov_inv @ ar_mean
    f_b = ar_mean @ ar_cov_inv @ ar_mean
    f_c = ar_ones @ ar_cov_inv @ ar_ones
    f_d = f_b * f_c - f_a ** 2

    def frontier_efficient(f_mean):
        return ((1 + (f_mean - f_a / f_c) ** 2 * f_c ** 2 / f_d) / f_c) ** 0.5

    print(ar_cov_inv @ ar_ones / f_c, 1 / f_c ** 0.5, f_a / f_c)
    ar_mean = np.linspace(0.08, 0.13, 100)
    ar_std = np.vectorize(frontier_efficient)(ar_mean)
    return np.array([ar_std, ar_mean]).T


def get_frontier_mad(n, ar_mean, ar_cov, i_sample=int(1e3)):
    ar_sample = np.random.multivariate_normal(ar_mean, ar_cov, size=i_sample)
    ar_res = []
    ar_ae = np.concatenate([np.ones(n), np.zeros(i_sample)])
    ar_be = 1
    ar_ai = sparse.bmat(
        [
            [-ar_sample + ar_mean, sparse.eye(i_sample)],
            [ar_sample - ar_mean, sparse.eye(i_sample)],
        ]
    )
    ar_bi = np.zeros(2 * i_sample)
    ar_bounds = [(-1, 1)] * n + [(0, None)] * i_sample
    for f_tol in np.linspace(0, 2.3, 100):
        res = optimize.linprog(
            np.concatenate([-f_tol * i_sample * ar_mean, np.ones(i_sample)]),
            -ar_ai,
            -ar_bi,
            ar_ae,
            ar_be,
            ar_bounds,
            "highs-ds",
            options={"sparse": True},
        )
        assert res["success"]
        ar_w = res["x"][:n]
        f_mean = ar_mean @ ar_w
        f_std = (ar_w @ ar_cov @ ar_w) ** 0.5
        if f_tol == 0:
            print(ar_w, f_std, f_mean)
        ar_res.append([f_std, f_mean])
    return np.array(ar_res)


def main():
    n, ar_mean, ar_cov = get_data()
    ar_frontier_var = get_frontier_var(n, ar_mean, ar_cov)
    ar_frontier_mad = get_frontier_mad(n, ar_mean, ar_cov)
    plt.plot(
        ar_frontier_var[:, 0],
        ar_frontier_var[:, 1],
        ":",
        label="Mean-variance frontier",
    )
    plt.plot(
        ar_frontier_mad[:, 0], ar_frontier_mad[:, 1], ":", label="Mean-MAD frontier"
    )
    plt.legend()
    plt.xlabel("Standard Deviation")
    plt.ylabel("Mean")
    plt.savefig("main_lp.pdf")


if __name__ == "__main__":
    main()
