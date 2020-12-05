#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from statsmodels.formula.api import ols


def step0_read(s_asset: str) -> pd.Series:
    return (
        pd.read_csv(s_asset + ".csv", index_col="Date")["Adj Close"]
        .pct_change()
        .dropna()
    )


def step0() -> None:
    l_stock = ["IBM", "MCD", "MMM", "WMT"]
    df_stock = pd.DataFrame({s_stock: step0_read(s_stock) for s_stock in l_stock})
    sr_index = step0_read("SPY")
    df_resid = pd.DataFrame()
    for s_stock in l_stock:
        df = pd.DataFrame({"SPY": sr_index, s_stock: df_stock[s_stock]})
        model = ols(formula=f"{s_stock} ~ SPY", data=df).fit()
        print(model.summary())
        df_resid[s_stock] = model.resid
        fig = plt.figure()
        sns.regplot(x="SPY", y=s_stock, data=df)
        fig.savefig(f"{s_stock}.pdf")
    print("Correlation matrix of returns")
    corr_return = df_stock.corr()
    print(corr_return)
    fig = plt.figure()
    sns.heatmap(corr_return, vmin=-0.04)
    fig.savefig("corr_return.pdf")
    print("Correlation matrix of residuals")
    corr_resid = df_resid.corr()
    print(corr_resid)
    fig = plt.figure()
    sns.heatmap(corr_resid, vmin=-0.04)
    fig.savefig("corr_resid.pdf")


step0()
