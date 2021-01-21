#!/usr/bin/env python3
import pandas as pd
import pandas_datareader as pdr
from requests_cache import CachedSession


def get_data(ar):
    res = {
        s: pdr.DataReader(s, "yahoo", s_begin, s_end, session=session)["Adj Close"]
        for s in ar
    }
    return pd.DataFrame(res).pct_change()[1:]


def get_sharpe(df_return, sr_rf):
    return df_return.sub(sr_rf, axis="index").mean() / df_return.std()


def get_treynor(df_return, sr_rf, sr_rua):
    sr = pd.Series(dtype="float64")
    f_var_rua = sr_rua.var()
    for s in df_return:
        sr[s] = (df_return[s] - sr_rf).mean() / sr_rua.cov(df_return[s]) * f_var_rua
    return sr


def get_modigliani_modigliani(df_return, sr_rf, sr_rua):
    sr = pd.Series(dtype="float64")
    f_std_rua = sr_rua.std()
    for s in df_return:
        sr[s] = (df_return[s] - sr_rf).mean() / df_return[s].std() * f_std_rua
        sr[s] += sr_rf.mean()
    return sr


pd.options.display.float_format = "{:.4e}".format
session = CachedSession(cache_name="cache")
s_begin = "2010-04-08"
s_end = "2021-03-31"

# fmt: off
df_return = get_data([
    "PSCC", "PSCD", "PSCE", "PSCF", "PSCH", "PSCI", "PSCM", "PSCT", "PSCU", "XLB",
    "XLC", "XLE", "XLF", "XLI", "XLK", "XLP", "XLRE", "XLU", "XLV", "XLY",
    "AAPL", "AMGN", "AXP", "BA", "CAT", "CRM", "CSCO", "CVX", "DD", "DIS", "GE", "GS",
    "HD", "HON", "IBM", "INTC", "JNJ", "JPM", "KO", "MCD", "MMM", "MRK", "MSFT", "NKE",
    "PFE", "PG", "RTX", "T", "TRV", "UNH", "V", "VZ", "WBA", "WMT", "XOM",
])
# fmt: on
sr_rua = get_data(["^RUA"])["^RUA"]
sr_rf = pdr.DataReader(
    "F-F_Research_Data_Factors_daily", "famafrench", s_begin, s_end, session=session
)[0]["RF"][1:]
sr_rf /= 100

df_res = pd.DataFrame(
    {
        "sharpe": get_sharpe(df_return, sr_rf),
        "treynor": get_treynor(df_return, sr_rf, sr_rua),
        "m2": get_modigliani_modigliani(df_return, sr_rf, sr_rua),
    }
)

print(df_res)
print(df_res['sharpe'].sort_values(ascending=False).head())
print(df_res['treynor'].sort_values(ascending=False).head())
print(df_res['m2'].sort_values(ascending=False).head())
