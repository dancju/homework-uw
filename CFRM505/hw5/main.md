---
title: CFRM 505, 2021 Winter, HW 5
header-includes:
  \DeclareUnicodeCharacter{2206}{$\Delta$}
  \DeclareUnicodeCharacter{0393}{$\Gamma$}
...

# 1

We have

$$\Delta=-\Phi\left(-\frac1{\sigma\sqrt{T}}\ln\frac{S_0}K-\frac{r\sqrt{T}}{\sigma}-\frac{\sigma\sqrt{T}}2\right)$$

$$\Delta_\text{PW}=-e^{-rT}\E\left(\frac{1_{S_T<K}S_T}{S_0}\right)$$

$$\Delta_\text{LR}=\frac{e^{-rT}}{\sigma\sqrt{T}S_0}\E\left(\left(K-S_T\right)^+Z\right)$$

$$\Gamma=\frac{1}{\sigma\sqrt TS_0}\phi\left(\frac1{\sigma\sqrt{T}}\ln\frac{S_0}K+\frac{r\sqrt{T}}{\sigma}+\frac{\sigma\sqrt{T}}2\right)$$

$$\Gamma_\text{LR}=\frac{e^{-rT}}{\sigma\sqrt TS_0^2}\E\left(\left(K-S_T\right)^+\left(\frac{Z^2-1}{\sigma\sqrt T}-Z\right)\right)$$

$$\Gamma_\text{LR-PW}=-\frac{e^{-rT}K}{\sigma \sqrt{T}S_0^2}\text E(1_{S_T<K}Z)$$

$$\Gamma_\text{PW-LR}=-\frac{e^{-rT}}{S_0^2}\text E\left[\left(\frac{Z}{\sigma\sqrt{T}}-1\right)1_{S_T<K}S_T\right]$$

where $S_T=S_0e^{\left(r-\frac{\sigma^2}{2}\right)T+\sigma\sqrt{T}Z}$ and $Z\sim\mathcal N(0,1)$.

### Script

\inputminted{python}{q1/main.py}

### Result

\begin{scriptsize}\begin{center}\begin{tabular}{r*5l}
  \toprule
  $K$ & $\Delta$ & $\Delta_\text{PW}$ & $\Delta_\text{LR}$ & Var $\Delta_\text{PW}$ & Var $\Delta_\text{LR}$ \\
  \midrule
   90 & -0.220872 & -0.221614 & -0.221282 & 0.128977 & 0.386622 \\
  100 & -0.431231 & -0.431740 & -0.435484 & 0.188529 & 0.846086 \\
  110 & -0.642786 & -0.643915 & -0.650440 & 0.179919 & 1.566271 \\
  \bottomrule
\end{tabular}\end{center}\end{scriptsize}

\begin{scriptsize}\begin{center}\begin{tabular}{r*7l}
  \toprule
  $K$ & $\Gamma$ & $\Gamma_\text{LR}$ & $\Gamma_\text{LR-PW}$ & $\Gamma_\text{PW-LR}$ & Var $\Gamma_\text{LR}$ & Var $\Gamma_\text{LR-PW}$ & Var $\Gamma_\text{PW-LR}$ \\
  \midrule
   90 & 0.0167876 & 0.0170053 & 0.0168314 & 0.0168520 & 0.0060303 & 0.0009124 & 0.0008062 \\
  100 & 0.0222315 & 0.0220180 & 0.0221412 & 0.0222933 & 0.0110402 & 0.0010600 & 0.0007393 \\
  110 & 0.0211062 & 0.0213384 & 0.0211595 & 0.0211846 & 0.0191616 & 0.0015108 & 0.0008094 \\
  \bottomrule
\end{tabular}\end{center}\end{scriptsize}

# 2

## CDF of $Y$

### Script

\inputminted{python}{q2/cdf_y.py}

### Result

![](q2/cdf_y.pdf)

## PMF of $L$

### Script

\inputminted{python}{q2/pmf_l.py}

### Result

![](q2/pmf_l_10.pdf)

![](q2/pmf_l_25.pdf)

![](q2/pmf_l_50.pdf)

## Histogram of $L$

### Script

\inputminted{python}{q2/hist_l.py}

### Result

$$\Pr(L>10)=0.00714$$

![](q2/hist_l.pdf)
