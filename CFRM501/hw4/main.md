---
title: CFRM 501, 2020 Autumn, HW 4
...

# 1

$$\sigma_p^2=w^2\sigma_1^2+(1-w)^2\sigma_2^2+2w(1-w)\rho\sigma_1\sigma_2.$$

**In the case of $\rho=1$:**

Plugging in $\sigma_p=0$ and $\rho=1$ yields

$$w^2\sigma_1^2+(1-w)^2\sigma_2^2+2w(1-w)\sigma_1\sigma_2=0,$$

$$w=\frac{1}{1-\sigma_1/\sigma_2}.$$

Since $\sigma_1>0$, $\sigma_2>0$, and $\sigma_1\ne\sigma_2$, we have

$$\sigma_1/\sigma_2\in(0,1)\cup(1,+\infty),$$

$$w=\frac{1}{1-\sigma_1/\sigma_2}\in(-\infty,0)\cup(1,+\infty).$$

**In the case of $\rho=-1$:**

Plugging in $\sigma_p=0$ and $\rho=-1$ yields

$$w^2\sigma_1^2+(1-w)^2\sigma_2^2-2w(1-w)\sigma_1\sigma_2=0,$$

$$w=\frac{1}{1+\sigma_1/\sigma_2}.$$

Since $\sigma_1/\sigma_2\in(0,1)\cup(1,+\infty)$,

$$w=\frac{1}{1+\sigma_1/\sigma_2}\in(0,1/2)\cup(1/2,1).$$

# 2

\includegraphics{q2/main.pdf}

Of the global minimum variance portfolio, the mean of return is $-0.02702$, the standard deviation of return is $0.2089$, and the weights are listed below. Stock MMM has the largest weight in the global minimum variance portfolio, which is not surprising because MMM has the smallest variance among other equities.

|      |      weight |
| ---- | ----------: |
| AAPL | $-0.074227$ |
| BBBY | $-0.002477$ |
| EBAY |  $0.198968$ |
| GE   |  $0.151052$ |
| GOOG |  $0.261212$ |
| INTC |  $0.006851$ |
| MMM  |  $0.337932$ |
| MSFT | $-0.215032$ |
| ORCL |  $0.221250$ |
| TEVA |  $0.114472$ |

**In the case of changing all the pairwise correlations by $-0.1$,** the mean of return is $-0.005114$, the standard deviation of return is $0.1931$, and the weights are listed below.

|      |      weight |
| ---- | ----------: |
| AAPL | $-0.039048$ |
| BBBY |  $0.030270$ |
| EBAY |  $0.191923$ |
| GE   |  $0.157003$ |
| GOOG |  $0.182321$ |
| INTC |  $0.022861$ |
| MMM  |  $0.271801$ |
| MSFT | $-0.119212$ |
| ORCL |  $0.177270$ |
| TEVA |  $0.124812$ |

**In the case of changing all the pairwise correlations by $+0.1$,** the mean of return is $-0.06868$, the standard deviation of return is $0.2139$, and the weights are listed below.

|      |      weight |
| ---- | ----------: |
| AAPL | $-0.100293$ |
| BBBY | $-0.040371$ |
| EBAY |  $0.206050$ |
| GE   |  $0.131372$ |
| GOOG |  $0.456854$ |
| INTC |  $0.011791$ |
| MMM  |  $0.389785$ |
| MSFT | $-0.454488$ |
| ORCL |  $0.297310$ |
| TEVA |  $0.101990$ |

### Comment

According to the three efficient frontiers, the data with "correlation $-0.1$" is generally better than the real data, and the real data is generally better than the data with "correlation $+0.1$". "Better" in this context means greater mean and smaller standard deviation.

Intuitively, this fact indicates that with less correlations between stocks, we are able to make a better portfolio because variances of individual stocks can be hedged with other stocks. In extreme and infeasible cases that $\rho=-1$, arbitrage opportunities exist.
