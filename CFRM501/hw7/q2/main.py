#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA as PCA

df = pd.read_csv("US_treasury_yields.csv", index_col="Date").diff().dropna()
pc = PCA(n_components=3).fit(df)
print(pc.explained_variance_)
print(pc.components_)
maturity = [1, 2, 3, 5, 7, 10, 20, 30]
plt.plot(maturity, pc.components_[0], marker="o", label="first")
plt.plot(maturity, pc.components_[1], marker="o", label="second")
plt.plot(maturity, -pc.components_[2], marker="o", label="third")
plt.legend()
plt.xlabel("Maturity (years)")
plt.ylabel("Loading")
plt.savefig("main.pdf")
