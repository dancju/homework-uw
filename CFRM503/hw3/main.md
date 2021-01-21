---
title: CFRM 503, 2021 Spring, HW 3
...

# 1

\inputminted{python}{q1/main.py}

```
          sharpe     treynor          m2
PSCC  5.0795e-02  8.1547e-04  5.9420e-04
PSCD  4.1613e-02  6.1465e-04  4.9040e-04
PSCE -5.3784e-03 -9.8334e-05 -4.0779e-05
PSCF  3.3145e-02  4.6701e-04  3.9468e-04
PSCH  5.7952e-02  8.0576e-04  6.7510e-04
PSCI  3.9623e-02  5.4064e-04  4.6791e-04
PSCM  2.9181e-02  4.9852e-04  3.4987e-04
PSCT  4.7323e-02  6.2707e-04  5.5494e-04
PSCU  4.3036e-02  7.1245e-04  5.0648e-04
XLB   3.3622e-02  4.2727e-04  4.0007e-04
XLC   4.1753e-02  3.8898e-04  4.9198e-04
XLE   1.0913e-02  1.5991e-04  1.4337e-04
XLF   3.3955e-02  4.2797e-04  4.0384e-04
XLI   4.3202e-02  5.2749e-04  5.0837e-04
XLK   5.8745e-02  7.2098e-04  6.8405e-04
XLP   5.0971e-02  7.2716e-04  5.9618e-04
XLRE  2.8840e-02  4.0801e-04  3.4602e-04
XLU   4.1306e-02  7.4434e-04  4.8693e-04
XLV   5.4096e-02  7.0624e-04  6.3151e-04
XLY   5.8257e-02  7.0537e-04  6.7854e-04
AAPL  6.4505e-02  1.1265e-03  7.4916e-04
AMGN  4.4478e-02  8.3072e-04  5.2278e-04
AXP   3.4408e-02  5.2425e-04  4.0896e-04
BA    3.4502e-02  5.9107e-04  4.1002e-04
CAT   3.9291e-02  6.1063e-04  4.6416e-04
CRM   4.8216e-02  8.9939e-04  5.6504e-04
CSCO  2.7904e-02  4.6900e-04  3.3543e-04
CVX   2.2858e-02  3.6069e-04  2.7840e-04
DD    2.4954e-02  3.9113e-04  3.0209e-04
DIS   4.7213e-02  7.6317e-04  5.5370e-04
GE    8.8785e-03  1.6316e-04  1.2038e-04
GS    2.3111e-02  3.5029e-04  2.8126e-04
HD    6.7732e-02  1.0471e-03  7.8564e-04
HON   5.1039e-02  7.0354e-04  5.9695e-04
IBM   1.5850e-02  2.6304e-04  1.9918e-04
INTC  3.5540e-02  6.0223e-04  4.2175e-04
JNJ   4.5686e-02  8.0213e-04  5.3644e-04
JPM   3.7464e-02  5.4552e-04  4.4350e-04
KO    3.6863e-02  6.6186e-04  4.3671e-04
MCD   4.9408e-02  8.9181e-04  5.7851e-04
MMM   3.5530e-02  5.5412e-04  4.2164e-04
MRK   3.6081e-02  6.7680e-04  4.2787e-04
MSFT  5.8837e-02  9.0529e-04  6.8510e-04
NKE   5.6939e-02  1.0196e-03  6.6364e-04
PFE   3.8951e-02  7.0989e-04  4.6031e-04
PG    4.0481e-02  8.0002e-04  4.7761e-04
RTX   2.4118e-02  3.6670e-04  2.9264e-04
T     2.6830e-02  4.9518e-04  3.2330e-04
TRV   3.9612e-02  6.4187e-04  4.6779e-04
UNH   6.4659e-02  1.1285e-03  7.5090e-04
V     5.7990e-02  9.0868e-04  6.7552e-04
VZ    4.3518e-02  9.2542e-04  5.1194e-04
WBA   2.1510e-02  4.8881e-04  2.6317e-04
WMT   3.9298e-02  9.6338e-04  4.6423e-04
XOM   1.1442e-02  1.8642e-04  1.4935e-04
```

The top three investments among the three measures are the same.

```
          sharpe     treynor          m2
HD    6.7732e-02  1.0471e-03  7.8564e-04
UNH   6.4659e-02  1.1285e-03  7.5090e-04
AAPL  6.4505e-02  1.1265e-03  7.4916e-04
```

# 2

\inputminted{python}{q2/main.py}

## 2.a

\begin{tabular}{l|rrr|rrr}
  \toprule
  & \multicolumn{3}{c|}{Total Contribution} & \multicolumn{3}{|c}{Marginal Contribution} \\
  & 1 & 2 & 3 & 1 & 2 & 3 \\
  \midrule
  XLF & 1.6250e-05 & 7.3697e-06 & 2.4774e-05 & 2.9250e-04 & 2.9479e-04 & 3.0968e-04 \\
  XLB & 1.5178e-05 & 1.3980e-05 & 2.0130e-05 & 2.7321e-04 & 2.7960e-04 & 2.8757e-04 \\
  XLI & 1.4777e-05 & 1.3574e-05 & 1.8152e-05 & 2.6599e-04 & 2.7149e-04 & 2.7926e-04 \\
  XLY & 1.3069e-05 & 1.8367e-05 & 1.4751e-05 & 2.3524e-04 & 2.4490e-04 & 2.4584e-04 \\
  XLK & 1.3690e-05 & 2.6065e-05 & 1.4084e-05 & 2.4642e-04 & 2.6065e-04 & 2.5608e-04 \\
  XLE & 1.7704e-05 & 2.4845e-05 & 1.6654e-05 & 3.1866e-04 & 3.3127e-04 & 3.3308e-04 \\
  XLV & 1.1096e-05 & 1.0191e-05 & 9.2382e-06 & 1.9973e-04 & 2.0381e-04 & 2.0529e-04 \\
  XLP & 8.8399e-06 & 7.9666e-06 & 6.4427e-06 & 1.5912e-04 & 1.5933e-04 & 1.6107e-04 \\
  XLU & 9.3128e-06 & 4.0199e-06 & 5.7948e-06 & 1.6763e-04 & 1.6080e-04 & 1.6556e-04 \\
  \bottomrule
\end{tabular}

## 2.b

```
XLF   -0.177337
XLB   -0.004935
XLI   -0.055791
XLY    0.226720
XLK   -0.140291
XLE    0.002119
XLV    0.267664
XLP    0.774284
XLU    0.107566
```

# 3

Let the return of the growth assets of each year be an i.i.d.\ normal variable $R\sim\mathcal N(\mu,\sigma^2)$. Let the risk-free rate be $r_f$. Let the exposure to the grothwth assets in yaer $i$ be $w_i$ where $i\in\{1,\dots,18\}$. The accumulated return at age 18 would be

$$\frac{W_{18}}{W_0}=\prod_{i=1}^{18}[(1+r_f)(1-w_i)+(1+R_i)w_i]\,,$$

or

$$\frac{W_{18}}{W_0}=\prod_{i=1}^{18}[1+r_f+(R_i-r_f)w_i]\,.$$

Let the $\gamma_i=1+r_f+(R_i-r_f)w_i$, we have $\E\gamma_i=1+r_f+(\mu-r_f)w_i$, $\Var\gamma_i=w_i^2\sigma^2$, and $\frac{W_{18}}{W_0}=\prod_{i=1}^{18}\gamma_i$. The expectation and the variance of the accumulated return are

$$\E\frac{W_{18}}{W_0}=\prod\E\gamma_i\,,$$

$$\Var\frac{W_{18}}{W_0}=\prod\left(\Var\gamma_i+(\E\gamma_i)^2\right)-\prod(\E\gamma_i)^2\,.
$$

Calculating the risk-adjusted return (RAR) $\frac{\E\frac{W_{18}}{W_0}-1}{\sqrt{\Var\frac{W_{18}}{W_0}}}$, with the assumption that $r_f,\mu,\sigma^2$ vary around 0.01, 0.2149, and 0.3327, we get the following result. ($\mu$ and $\sigma^2$ are estimated from the historical data of ^RUA in the last 30 years.)

\includegraphics{q3/rf.pdf}

\includegraphics{q3/mu.pdf}

\includegraphics{q3/sigma2.pdf}

Therefore, the grandparents should choose plan B since it yields higher RAR as the risk-free rate, and the distribution of the return of the growth assets vary in a reasonable domain. Moreover, a more accurate estimation of $r_f$, $\mu$ and $\sigma^2$ from a macroeconomic study might assist the decision.

\inputminted{python}{q3/main.py}
