---
title: CFRM 501, 2020 Autumn, HW 6
...

# 1

## IBM

$$r=-0.0003+1.0039F+\epsilon\,.$$

\begin{center}\begin{tabular}{lrrrr}
\toprule
          &    Coef & Std err &    $t$ & $\Pr>|t|$ \\
\midrule
Intercept & -0.0003 &   0.000 & -1.115 &     0.265 \\
SPY       &  1.0039 &   0.025 & 39.564 &     0.000 \\
\bottomrule
\end{tabular}\end{center}

\includegraphics{q1/IBM.pdf}

## MCD

$$r=0.0003+0.7985F+\epsilon\,.$$

\begin{center}\begin{tabular}{lrrrr}
\toprule
          &   Coef & Std err &    $t$ & $\Pr>|t|$ \\
\midrule
Intercept & 0.0003 &   0.000 &  1.068 &     0.286 \\
SPY       & 0.7985 &   0.026 & 30.350 &     0.000 \\
\bottomrule
\end{tabular}\end{center}

\includegraphics{q1/MCD.pdf}

## MMM

$$r=-0.0002+0.9196F+\epsilon\,.$$

\begin{center}\begin{tabular}{lrrrr}
\toprule
          &    Coef & Std err &    $t$ & $\Pr>|t|$ \\
\midrule
Intercept & -0.0002 &   0.000 & -0.799 &     0.424 \\
SPY       &  0.9196 &   0.026 & 35.376 &     0.000 \\
\bottomrule
\end{tabular}\end{center}

\includegraphics{q1/MMM.pdf}

## WMT

$$r=0.0006+0.5485F+\epsilon\,.$$

\begin{center}\begin{tabular}{lrrrr}
\toprule
          &   Coef & Std err &    $t$ & $\Pr>|t|$ \\
\midrule
Intercept & 0.0006 &   0.000 &  1.761 &     0.079 \\
SPY       & 0.5485 &   0.030 & 18.297 &     0.000 \\
\bottomrule
\end{tabular}\end{center}

\includegraphics{q1/WMT.pdf}

## Residuals

\begin{table}[h]
    \scriptsize
    \begin{subtable}[h]{0.5\textwidth}
        \begin{tabular}{l|rrrr}
            \toprule
                &    IBM &    MCD &    MMM &    WMT \\
            \midrule
            IBM & 1.0000 & 0.4711 & 0.5900 & 0.3510 \\
            MCD & 0.4711 & 1.0000 & 0.4617 & 0.3008 \\
            MMM & 0.5900 & 0.4617 & 1.0000 & 0.3211 \\
            WMT & 0.3510 & 0.3008 & 0.3211 & 1.0000 \\
            \bottomrule
        \end{tabular}
       \caption{arithmetic returns}
    \end{subtable}
    \hfill
    \begin{subtable}[h]{0.5\textwidth}
        \begin{tabular}{l|rrrr}
            \toprule
                &       IBM &       MCD &       MMM &       WMT \\
            \midrule
            IBM &  $1.0000$ & $-0.0355$ &  $0.1270$ &  $0.0095$ \\
            MCD & $-0.0355$ &  $1.0000$ & $-0.0042$ & $-0.0018$ \\
            MMM &  $0.1270$ & $-0.0042$ &  $1.0000$ & $-0.0107$ \\
            WMT &  $0.0095$ & $-0.0018$ & $-0.0107$ &  $1.0000$ \\
            \bottomrule
        \end{tabular}
        \caption{residuals}
     \end{subtable}
     \caption{Correlation matrix of arithmetic returns and residuals}
\end{table}

\begin{figure}[H]
    \begin{subfigure}{0.5\textwidth}
        \includegraphics[width=0.9\linewidth]{q1/corr_return.pdf}
        \caption{arithmetic returns}
    \end{subfigure}
    \hfill
    \begin{subfigure}{0.5\textwidth}
        \includegraphics[width=0.9\linewidth]{q1/corr_resid.pdf}
        \caption{residuals}
    \end{subfigure}
    \caption{Correlation heatmaps of arithmetic returns and residuals}
\end{figure}

The arithmetic returns $\mathcal R$ are _correlated_; and the residuals $\hat{\mathcal E}$ are _uncorrelated_ or _serially independent_.

# 2

## 2.1

The mean of $L$ is $-1.00091\times10^{-9}$. The variance of $L$ is 42.1339.

\includegraphics{q2/1.pdf}

## 2.2

The eigenvector corresponding to the first principal component is

$$\begin{pmatrix}0.07340044 & -0.0747503 & -0.99438842 & 0.01471193\end{pmatrix}\tran\,.$$

## 2.3

The mean of $L$ is $-1.00091\times10^{-9}$. The variance of $L$ is 38.6906.

\includegraphics{q2/3.pdf}
