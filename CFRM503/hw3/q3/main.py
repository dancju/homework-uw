#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from requests_cache import CachedSession


def get_rar(f_rf, f_mu, f_sigma2, ar_weight):
    ar_e_g = 1 + f_rf + (f_mu - f_rf) * ar_weight
    ar_v_g = f_sigma2 * ar_weight ** 2
    ar_e2_g = ar_e_g ** 2
    f_e_r = ar_e_g.prod()
    f_v_r = (ar_v_g + ar_e2_g).prod() - (ar_e2_g).prod()
    return (f_e_r - 1) / f_v_r ** 0.5


session = CachedSession(cache_name="cache")
s_begin = "1980-01-01"
s_end = "2020-04-01"
sr_rua = yf.download("^RUA", s_begin, s_end, interval="1mo", session=session)
sr_rua = sr_rua["Adj Close"].pct_change()[1:]
sr_rua = (sr_rua + 1) ** 12 - 1
f_mu = sr_rua.mean()
f_sigma2 = sr_rua.var()
print(f_mu, f_sigma2)
# fmt: off
ar_weight = pd.DataFrame({
    "A": [
        .9, .9, .85, .85, .8, .8, .75, .75, .7, .7, .65, .65, .6, .6, .55, .55, .5, .5,
        .45, .4, .35, .3
    ],
    "B": [
        .8, .8, .8, .8, .76, .72, .68, .64, .62, .6, .58, .56, .64, .52, .5, .49, .48,
        .47, .49, .51, .53, .55
    ],
    "C": [.7] * 22,
})
# fmt: on

plt.figure()
for i in ["A", "B", "C"]:
    ar = np.linspace(0, 0.02, 1024)
    plt.plot(
        ar,
        [get_rar(f, f_mu, f_sigma2, ar_weight[i]) for f in ar],
        label=f"Plan {i}",
    )
plt.legend()
plt.xlabel("$r_f$")
plt.ylabel("Risk-adjusted Return")
plt.title(fr"RAR with $\mu={f_mu:.4f}$ and $\sigma^2={f_sigma2:.4f}$")
plt.savefig("rf.pdf")

plt.figure()
for i in ["A", "B", "C"]:
    ar = np.linspace(f_mu * 0.95, f_mu * 1.05, 1024)
    plt.plot(
        ar,
        [get_rar(0.01, f, f_sigma2, ar_weight[i]) for f in ar],
        label=f"Plan {i}",
    )
plt.legend()
plt.xlabel(r"$\mu$")
plt.ylabel("Risk-adjusted Return")
plt.title(fr"RAR with $r_f=0.01$ and $\sigma^2={f_sigma2:.4f}$")
plt.savefig("mu.pdf")

plt.figure()
for i in ["A", "B", "C"]:
    ar = np.linspace(f_sigma2 * 0.95, f_sigma2 * 1.05, 1024)
    plt.plot(
        ar,
        [get_rar(0.01, f_mu, f, ar_weight[i]) for f in ar],
        label=f"Plan {i}",
    )
plt.legend()
plt.xlabel(r"$\sigma^2$")
plt.ylabel("Risk-adjusted Return")
plt.title(fr"RAR with $r_f=0.01$ and $\mu={f_mu:.4f}$")
plt.savefig("sigma2.pdf")
