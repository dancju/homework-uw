---
title: CFRM 505, 2021 Winter, Final
...

# 1

## 1.a

The described acceptance-rejection method is available iff

\begin{align*}
  & \exists a\in\mathbb R\,,\forall x\in\mathbb R: f_Y(x)a\ge f_X(x) \\
  \Longleftrightarrow& \exists a\in\mathbb R\,,\forall x\in\mathbb R: a\ge\sigma e^{\frac{(1-\sigma^2)x^2-2x+1}{2\sigma^2}} \\
  \Longleftrightarrow& \sup_{x\in\mathbb R}\sigma e^{\frac{(1-\sigma^2)x^2-2x+1}{2\sigma^2}}\,\text{exists} \\
  \Longleftrightarrow& \sigma^2>1 \,.
\end{align*}

## 1.b

$$
  a
  =\sup_{x\in\mathbb R}\frac{f_X(x)}{f_Y(x)}
  =\sigma\sup_{x\in\mathbb R}e^{\frac{(1-\sigma^2)x^2-2x+1}{2\sigma^2}}
  =\begin{cases}
    \text{not existed} &
    \sigma\in(0,1]\,, \\
    \sigma e^{-\frac1{(1-\sigma^2)2}} &
    \sigma\in(1,\infty)\,.
  \end{cases}
$$

# 2

## 2.a

$$\text P_t(L=k)=\frac{e^{tk}}{e^{(e^t-1)\lambda}}\frac{\lambda^ke^{-\lambda}}{k!}=\frac{(\lambda e^t)^ke^{-\lambda e^t}}{k!}\,.$$

That is, $L\sim\text{Poi}(\lambda e^t)$ under measure P$_t$.

## 2.b

$$
\Var_{\text P_t}(L)>\Var_{\text P}(L)
\Longleftrightarrow \lambda e^{t}>\lambda
\Longleftrightarrow t>\ln 1
$$

# 3

1. Generate samples $Z_1,\dots,Z_4$ from $\mathcal N(0,\sigma^2)$;
1. Calculate the estimator $\left(\prod_{i=1}^4\frac{f(Z_i)}{g(Z_i)}\right)1_{\sum_{i=1}^4Z_i\ge20}$, where $f(\cdot)$ is the PDF of $\mathcal N(0,1)$ and $g(\cdot)$ is the PDF of $\mathcal N(0,\sigma^2)$;
1. Repeat the two steps above and report the mean of the estimators.

# 4

## 4.a

\inputminted{python}{q4/a.py}

$$\E(1_{S_T>K})\approx0.41591 \quad \Var(1_{S_T>K})\approx0.242929$$

![](q4/a.pdf)

## 4.b

We can't use $V$ as a control variate since $\Cov(S_T,V)=0$.

## 4.c

\begin{align*}
  & \Pr(S_T>K|V) \\
  =& \Pr\left\{Z > \left[\ln\frac{K}{S_0}-\left(\mu-\frac{V^2}2\right)T\right]\frac1{V\sqrt{T}}\middle|V\right\} \\
  =& 1-\Phi\left\{\left[\ln\frac{K}{S_0}-\left(\mu-\frac{V^2}2\right)T\right]\frac1{V\sqrt{T}}\right\}
\end{align*}

\inputminted{python}{q4/c.py}

$$\E(\Pr(S_T>K|V))\approx0.416306 \quad \Var(\Pr(S_T>K|V))\approx0.000159$$

![](q4/c.pdf)

# 5

## 5.a

\begin{align*}
  & \E(Y_i|Z) \\
  =& \Pr\left(\sqrt\rho Z+\sqrt{1-\rho}\epsilon_i>2\middle|Z\right) \\
  =& \Pr\left(\epsilon_i>\frac{2-\sqrt\rho Z}{\sqrt{1-\rho}}\middle|Z\right) \\
  =& \Phi\left(\frac{\sqrt\rho Z-2}{\sqrt{1-\rho}}\right)
\end{align*}

$$\E(Y_i^2|Z)=\E(Y_i|Z)$$

$$\Var(Y_i|Z)=\E(Y_i^2|Z)-\E(Y_i|Z)^2=\alpha-\alpha^2\,,\quad\text{where }\alpha=\Phi\left(\frac{\sqrt\rho Z-2}{\sqrt{1-\rho}}\right)\,.$$

## 5.b

\begin{align*}
& \Var(Y_1+Y_2) \\
=& \E[\Var(Y_1+Y_2|Z)]+\Var[\E(Y_1+Y_2|Z)] \\
=& \E[\Var(Y_1|Z)+\Var(Y_2|Z)]+\Var[\E(Y_1|Z)+\E(Y_2|Z)] \\
=& 2\E(\alpha-\alpha^2)+4\Var(\alpha)
\end{align*}

\inputminted{python}{q5/main.py}

$$\Var(Y_1+Y_2)=0.0516588\,.$$

# 6

## PW

\begin{align*}
& \rho_\text{PW} \\
=& \frac{\partial\E\left(e^{-rT}(K-S_T^p)^+\right)}{\partial r} \\
=& \E\frac{\partial e^{-rT}(K-S_T^p)^+}{\partial r} \\
=& \E\left(-e^{-rT}T(K-S_T^p)^++e^{-rT}p(-1_{K>S_T^p})S_T^{p-1}\frac{\partial S_T}{\partial r}\right)
\end{align*}

Plugging in

$$\frac{\partial S_T}{\partial r}=\frac{\partial S_0e^{\left(r-\frac{\sigma^2}2\right)T+\sigma Z}}{\partial r}=S_0e^{\left(r-\frac{\sigma^2}2\right)T+\sigma Z}T=TS_T$$

yields

$$\rho_\text{PW}=-e^{-rT}T\E\left((K-S_T^p)^++p1_{K>S_T^p}S_T^p\right)$$

## LR

Let $f(S_T;r)$ be the PDF of $S_T$. We have

\begin{align*}
& \rho_\text{LR} \\
=& \frac{\partial\E\left(e^{-rT}(K-S_T^p)^+\right)}{\partial r} \\
=& \frac{\partial}{\partial r}\int e^{-rT}(K-S_T^p)^+f(S_T;r)\diff S_T \\
=& \int (K-S_T^p)^+\left[e^{-rT}(-T)f(S_T;r)+e^{-rT}\frac{\partial f(S_T;r)}{\partial r}\right]\diff S_T \\
=& e^{-rT}\E\left[(K-S_T^p)^+\left(\frac{1}{f(S_T;r)}\frac{\partial f(S_T;r)}{\partial r}-T\right)\right]
\end{align*}

Since $S_T\sim\text{GBM}(r,\sigma)$, $S_T$ is a lognormal random variable such that

$$S_T=S_0e^{\left(r-\frac{\sigma^2}{2}\right)T+\sigma\sqrt{T}Z}\quad Z\sim\mathcal N(0,1)$$

whose CDF is

\begin{align*}
& F(x;r) \\
=& \Pr(S_T<x) \\
=& \Pr\left(\ln S_0+\left(r-\frac{\sigma^2}{2}\right)T+\sigma\sqrt{T}Z<\ln x\right) \\
=& \Phi\left(\frac{\ln x-\ln S_0-\left(r-\frac{\sigma^2}{2}\right)T}{\sigma\sqrt{T}}\right)
\end{align*}

Letting $\xi(x;r)=\frac{\ln x-\ln S_0-\left(r-\frac{\sigma^2}{2}\right)T}{\sigma\sqrt{T}}$, we have the CDF of $S_T$ such that $F(x;r)=\Phi(\xi(x;r))$, the PDF of $S_T$ such that $f(x;r)=\frac{\phi(\xi(x;r))}{\sigma\sqrt{T}x}$, and the derivative of the PDF w.r.t.\ $r$ such that

$$\frac{\partial f(x;r)}{\partial r}=\frac{\phi'(\xi(x;r))}{\sigma\sqrt{T}x}\frac{\partial\xi(x;r)}{\partial r}=\frac{-\phi(\xi(x;r))\xi(x;r)}{\sigma\sqrt Tx}\frac{-\sqrt T}{\sigma}=\frac{f(x;r)\xi(x;r)\sqrt T}{\sigma}$$

Plugging back into $\rho_\text{LR}$ yields

$$
\rho_\text{LR}=e^{-rT}\E\left[(K-S_T^p)^+\left(\frac{Z\sqrt T}\sigma-T\right)\right]
$$

## Script

\inputminted{python}{q6/main.py}

## Result

\begin{center}\begin{tabular}{lrr}
  \toprule
  & Mean of estimator & Variance of estimator \\
  \midrule
  PW & $-81.4011$ &  7327.02 \\
  LR & $-81.2926$ & 24882.37 \\
  \bottomrule
\end{tabular}\end{center}
