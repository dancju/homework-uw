---
title: CFRM 503, 2021 Spring, Project 1
...

In this project, we identify the portfolio weights for five decision points before the reconstitution as described in the instruction. Will will define an objective function with a portfolio weight vector variable $\bm w$, and combine it with constraints to form a quadratic programming problem, and finally find the solution.

# Objective function

We are finding the $\bm w$ minimizing the weighted sum of squared tracking errors

$$\alpha(\bm w-\bm w_{C})\tran\bm\Sigma(\bm w-\bm w_{C})+(1-\alpha)(\bm w-\bm w_{F})\tran\bm\Sigma(\bm w-\bm w_{F})\,,$$

where we have values for

1. $\bm\Sigma$ denoting the covariance matrix of the weekly logarithmic return,
1. $\bm w_C$ and $\bm w_F$ denoting the portfolio weights of the current benchmark and the future benchmark, and
1. $\alpha$ being a scalar that varies in the five decision points as described in Table \ref{tab:params}.

# Constraints

As required in the instruction, portfolio weights must be non-negative

$$\bm w\succeq\bm0\,,$$

and portfolio weights must add to 1

$$\bm1\tran\bm w=1\,.$$

Moreover, the expected excess return must be at least 2 basis points per week over a benchmark

$$\bm\mu\tran\bm w\succeq\bm\mu\tran\bm w_B+0.0002\,,$$

where $\bm\mu$ is the expected weekly return, and $\bm w_B$ is a vector that varies in five decision points as described in Table \ref{tab:params}.

\begin{table}[h]
  \centering
  \begin{tabular}{rrr}
    \toprule
    & $\alpha$ & $\bm w_B$ \\
    \midrule
    4 & 1.0 & $\bm w_C$ \\
    3 & 0.8 & $\bm w_C$ \\
    2 & 0.6 & $\bm w_C$ \\
    1 & 0.3 & $\bm w_C$ \\
    0 & 0.0 & $\bm w_F$ \\
    \bottomrule
  \end{tabular}
  \caption{Parameters}
  \label{tab:params}
\end{table}

# QP problem

Combining the objective function and the constraints, we have

\begin{align*}
  \min_{\bm w} \quad&
  \alpha(\bm w-\bm w_{C})\tran\bm\Sigma(\bm w-\bm w_{C})+(1-\alpha)(\bm w-\bm w_{F})\tran\bm\Sigma(\bm w-\bm w_{F}) \\
  \text{s.t.} \quad&
  \bm w\succeq\bm0 \\&
  \bm1\tran\bm w=1 \\&
  \bm\mu\tran\bm w\succeq\bm\mu\tran\bm w_B+0.0002
\end{align*}

or in the QP form

\begin{align*}
  \min_{\bm w} \quad&
  \bm w\tran\bm\Sigma\bm w-2[\alpha\bm w_C+(1-\alpha)\bm w_F]\tran\bm\Sigma\bm w+\text{const} \\
  \text{s.t.} \quad&
  \begin{pmatrix}\bm I\\\bm\mu\tran\end{pmatrix}\bm w\succeq\begin{pmatrix}\bm0\\\bm\mu\tran\bm w_B+0.0002\end{pmatrix} \\&
  \bm1\tran\bm w=1
\end{align*}

# Results

With the script shown in the Appendix, we get the results of the QP problems for the five decision points.

```
             4         3         2         1         0
DRH   0.009059  0.014594  0.014939  0.013875  0.002872
DLR   0.173146  0.128366  0.083909  0.014718  0.000990
DHC   0.001086  0.000186  0.000011  0.000020  0.000850
DEI   0.018229  0.011116  0.005332  0.003610  0.002363
DRE   0.067587  0.074987  0.086041  0.103757  0.008083
DX    0.000283  0.000175  0.000016  0.000024  0.000910
DEA   0.011939  0.011392  0.008421  0.002846  0.002126
EGP   0.018272  0.010752  0.006504  0.008944  0.002360
EFC   0.000744  0.000420  0.000035  0.000063  0.000843
EARN  0.000888  0.003230  0.006679  0.011947  0.003206
ESRT  0.003001  0.000551  0.000026  0.000054  0.000985
EPR   0.005772  0.000704  0.000025  0.000030  0.001065
EQIX  0.287816  0.247220  0.207935  0.149896  0.002968
EQC   0.007882  0.002443  0.000210  0.000167  0.000973
ELS   0.040711  0.021295  0.001679  0.000252  0.002204
EQR   0.095183  0.072336  0.053048  0.021058  0.001431
EPRT  0.016215  0.024414  0.032088  0.044018  0.006225
ESS   0.076069  0.064359  0.046321  0.010537  0.001206
EXR   0.069625  0.057692  0.045737  0.024678  0.002373
FPI   0.004772  0.012877  0.021501  0.033647  0.006624
FRT   0.026586  0.042973  0.058337  0.082092  0.100199
FR    0.031641  0.034104  0.031002  0.011600  0.073581
FCPT  0.011721  0.022006  0.032832  0.044757  0.035162
FSP   0.000761  0.000818  0.000151  0.000158  0.006710
GLPI  0.000242  0.022510  0.049754  0.088572  0.153550
GEO   0.000123  0.000125  0.000013  0.000020  0.012299
GTY   0.000463  0.000601  0.000070  0.000074  0.008995
GOOD  0.000401  0.000684  0.000113  0.000118  0.010389
GMRE  0.001596  0.009971  0.017525  0.027614  0.014231
GNL   0.000479  0.000506  0.000046  0.000060  0.019849
GPMT  0.000336  0.000710  0.000164  0.000150  0.007765
HASI  0.006369  0.032282  0.058613  0.099836  0.081615
HR    0.000480  0.001598  0.000319  0.000551  0.051863
HTA   0.000731  0.012241  0.021766  0.020948  0.088388
HT    0.000199  0.000140  0.000011  0.000019  0.002364
HIW   0.002715  0.018306  0.034869  0.055303  0.065997
HMG   0.000218  0.000213  0.000022  0.000042  0.000356
HST   0.000757  0.019247  0.040589  0.072830  0.157903
HPP   0.005903  0.021854  0.033350  0.051117  0.058126
```

The tracking errors relateive to the current benchmark and the future benchmark for the five decision points are shown in Table \ref{tab:tracking_error} and Figure \ref{fig:tracking_error}.

\begin{table}[H]
  \centering
  \begin{tabular}{lrrrrr}
    \toprule
    & 4 & 3 & 2 & 1 & 0 \\
    \midrule
    Current & 0.000447 & 0.006454 & 0.012874 & 0.022493 & 0.032366 \\
    Future  & 0.032483 & 0.026132 & 0.019822 & 0.010701 & 0.000483 \\
    \bottomrule
  \end{tabular}
  \caption{Tracking errors relative to the current and the future benchmark}
  \label{tab:tracking_error}
\end{table}

\begin{figure}[H]
  \centering
  \includegraphics{src/tracking_error.pdf}
  \caption{Tracking errors relative to the current and the future benchmark}
  \label{fig:tracking_error}
\end{figure}

The expected excess return relative to the current benchmark and the future benchmark for the five decision points are shown in Table \ref{tab:excess_return} and Figure \ref{fig:excess_return}.

\begin{table}[H]
  \centering
  \begin{tabular}{lrrrrr}
    \toprule
    & 4 & 3 & 2 & 1 & 0 \\
    \midrule
    Current & 0.000201 & 0.000201 & 0.000200 & 0.000200 & -0.001653 \\
    Future  & 0.002057 & 0.002057 & 0.002056 & 0.002056 & 0.000203 \\
    \bottomrule
  \end{tabular}
  \caption{Expected excess return relative to the current and the future benchmark}
  \label{tab:excess_return}
\end{table}

\begin{figure}[H]
  \centering
  \includegraphics{src/excess_return.pdf}
  \caption{Expected excess return relative to the current and the future benchmark}
  \label{fig:excess_return}
\end{figure}

# Discussion

1. The portfolio weights of each asset in different decision points do not vary significantly.
1. As shown in Figure \ref{fig:tracking_error}, when the relative importance of the current benchmark decreases, the tracking error relative to the current benchmark increases, and the tracking error relative to the future benchmark decreases.
1. As shown in Figure \ref{fig:excess_return}, when the relative importance of current versus future benchmark changes in the first four decision points, the expected excess return does not change.
1. As shown in Figure \ref{fig:excess_return}, when the benchmark for excess return calculation switches in the last decision point, the excess return constraint was relaxed, and the expected return decreases.
1. Two other approaches based on SLSQP and "Trust region methods" by Conn et al. were implemented, which yields highly similar results as listed above. Although not finishing in polynomial time, they apply to more general problems such as when the quadratic coefficient matrix is indefinite, or even when the objective function has a higher rank.

# Appendix

\inputminted{python}{src/main.py}
