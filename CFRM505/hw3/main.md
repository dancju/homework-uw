---
title: CFRM 505, 2021 Winter, HW 3
...

# 1

### Script

\inputminted{python}{q1/main.py}

### Result

The simulated result is $\E(P_1)=1.88907$.

A _sample process_ is shown in the following diagram.

![](q1/path.pdf)

The _frequency density histogram_ and the _probability density function_ are shown in the following diagram.

![](q1/hist.pdf)

# 2

### Script

\inputminted{python}{q2/main.py}

### Result

<!-- The analytic result is
    121 / 30 * 1400 / 3 ≈ 1882.22
    and
    ?
-->

The simulated result is

1. the mean amount of money spent is 1884.49;
1. the variance of the amount of money spent is 1292526.

# 3

### Script

\inputminted{python}{q3/main.py}

### Result

The _histogram_ is shown in the following diagram.

![](q3/hist.pdf)

The mean is 111532. The variance is 179138269.

The _cumulative histogram_ is shown in the following diagram.

![](q3/hist_cumulative.pdf)

\begin{center}\begin{tabular}{rr}
    \toprule
    $p$ & $\Pr(W_T\le pW_0)$ \\
    \midrule
    0.8 &  0.35\% \\
    0.9 &  4.17\% \\
    1.0 & 19.66\% \\
    1.1 & 47.82\% \\
    1.2 & 75.10\% \\
    1.3 & 90.98\% \\
    1.4 & 97.57\% \\
    1.5 & 99.40\% \\
    \bottomrule
\end{tabular}\end{center}

# 4

### Script

\inputminted{python}{q4/main.py}

### Result

The _histogram_ is shown in the following diagram.

![](q4/hist.pdf)

\begin{center}\begin{tabular}{rrr}
    \toprule
    $\rho$ & Mean & Variance \\
    \midrule
    $-0.5$ & 114467 &  78716775 \\
    0.0 & 114518 & 158065189 \\
    0.5 & 114386 & 240038679 \\
    \bottomrule
\end{tabular}\end{center}

The _cumulative histogram_ is shown in the following diagram.

![](q4/hist_cumulative.pdf)

\begin{center}\begin{tabular}{rrr}
    \toprule
    $\rho$ & p & $\Pr(W_T\le pW_0)$ \\
    \midrule
    & 0.9 & 0.11\% \\
    & 1.0 & 4.39\% \\
    $-0.5$ & 1.1 & 31.76\% \\
    & 1.2 & 74.34\% \\
    & 1.3 & 95.28\% \\
    \hline
    & 0.9 & 1.49\% \\
    & 1.0 & 12.04\% \\
    0.0 & 1.1 & 37.60\% \\
    & 1.2 & 68.41\% \\
    & 1.3 & 88.79\% \\
    \hline
    & 0.9 & 4.18\% \\
    & 1.0 & 17.83\% \\
    0.5 & 1.1 & 41.27\% \\
    & 1.2 & 66.34\% \\
    & 1.3 & 84.45\% \\
    \bottomrule
\end{tabular}\end{center}

# 5

### Script

\inputminted{python}{q5/main.py}

### Result

A _sample process_ and its corresponding _relative drawdown_ are shown in the following diagram.

![](q5/path.pdf)

The _expected maximum relative drawdown_ is shown in the following diagram.

![](q5/drawdown.pdf)
