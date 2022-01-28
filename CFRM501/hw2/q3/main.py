#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

for stock in ["AMZN", "GOOG", "MSFT"]:
    ar = pd.read_csv(stock + "_d.csv", index_col="Date")["Adj Close"]
    ar = ar.pct_change().dropna()

    f_mean = ar.mean()
    f_std = ar.std()

    print(f"{stock}{f_mean:12f}{f_std ** 2:12f}{ar.skew():12f}{ar.kurt():12f}")

    plt.figure()
    plt.xlabel("Arithmetic Return")
    plt.ylabel("Density")
    plt.hist(ar, bins=32, density=True)
    ar_x = np.linspace(ar.min(), ar.max(), 128)
    plt.plot(ar_x, stats.norm.pdf(ar_x, f_mean, f_std))
    plt.savefig(stock + ".pdf")
