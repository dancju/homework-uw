#!/usr/bin/env python3
import numpy as np
import pandas as pd
import pandas_datareader as pdr
from requests_cache import CachedSession


def get_data(ar):
    res = {
        s: pdr.DataReader(s, "yahoo", s_begin, s_end, session=session)["Adj Close"]
        for s in ar
    }
    return pd.DataFrame(res).pct_change()[1:]


session = CachedSession(cache_name="cache")
s_begin = "2010-04-08"
s_end = "2021-03-31"

df_return = get_data(["XLF", "XLB", "XLI", "XLY", "XLK", "XLE", "XLV", "XLP", "XLU"])
df_cov = df_return.cov()
l_sr_weight = [
    [1 / 9] * 9,
    [0.05, 0.1, 0.1, 0.15, 0.2, 0.15, 0.1, 0.1, 0.05],
    [0.16, 0.14, 0.13, 0.12, 0.11, 0.1, 0.09, 0.08, 0.07],
]
l_sr_weight = [pd.Series(i, index=df_return.columns) for i in l_sr_weight]

df = pd.DataFrame(index=df_return.columns)
for i in range(3):
    sr_weight = l_sr_weight[i]
    sr_cov = sr_weight @ df_cov
    df[f"wC_{i+1}"] = sr_weight * sr_cov
    df[f"2C_{i+1}"] = 2 * sr_cov
pd.options.display.float_format = "{:.4e}".format
print(df)

sr = pd.Series(
    np.linalg.inv(df_cov) @ np.ones(df_return.columns.size), index=df_return.columns
)
pd.options.display.float_format = None
print(sr / sr.sum())
