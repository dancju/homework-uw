---
title: CFRM 503, 2021 Spring, HW 2
...

# 1

When one constructs portfolios

1. according to the modern portfolio theory,
1. under fixed expectations of returns $\bm\mu$, covariances of returns $\bm\Sigma$, and the risk-free return $r_f$, but
1. with different risk-aversion parameters $\gamma$,

all portfolios constructed should be on the capital market line, and the weights of risky assets of each portfolio should be proportional/parallel to the tangent portfolio weights

$$\bm w_c=\frac{\sigma_c}{\sigma_p}\bm w_p\propto\bm w_p\,.$$

We can reasonably assume that each company holds fixed market anticipation (fixed $\bm\mu, \bm\Sigma$, and $r$) when constructing different funds. If we look at the funds of each company, we can see that neither pair of funds have proportional weights of risky assets. Therefore, we can conclude that each company has no more than one fund that is constructed consistently with CAPM.

# 2

The expectation of $|X-\mu|$ is

$$\E(|X-\mu|)=\int_{-\infty}^\infty |x-\mu|f_X(x)\diff x\,.$$

Since both $|x-\mu|$ and $f_X(x)$ are symmetric w.r.t.\ the axis $x=\mu$, we have

$$\E(|X-\mu|)=2\int_{-\infty}^\mu(\mu-x)f_X(x)\diff x\,.$$

Since $f_X'(x)=\frac{\mu-x}{\sigma^2}f_X(x)$, we have

$$\E(|X-\mu|)=2\sigma^2\left.f_X(x)\right|_{-\infty}^\mu\,,$$

or

$$\E(|X-\mu|)=\sqrt\frac2\pi\sigma\,.$$

# 3

## Mean-variance frontier

Plugging the expected returns $\bm\mu$ and covariance matrix of returns $\bm\Sigma=\bm{\sigma\rho\sigma}$ into the formula

$$\frac{\sigma^2}{1/C}-\frac{(\mu-A/C)^2}{D/C^2}=1\,,$$

where

$$A=\bm1\tran\bm\Sigma^{-1}\bm\mu\,,B=\bm\mu\tran\bm\Sigma^{-1}\bm\mu\,,C=\bm1\tran\bm\Sigma^{-1}\bm1\,,D=BC-A^2\,,$$

yields the Markowitz efficient (Mean-variance) frontier.

## Mean-MAD frontier

The problem can be formulated as

\begin{align*}
  \min_{\bm w}\quad &
  -\bm\mu\tran\bm w+\lambda\E\left(\left|\bm r\tran\bm w-\bm\mu\tran\bm w\right|\right)\,, \\
  \text{s.t.}\quad &
  \bm1\tran\bm w=1\,,
\end{align*}

where $\bm r\in\mathbb R^3$ is a random vector drawn from the multivariate normal distribution $\mathcal N(\bm\mu,\bm\Sigma)$. Expanding the expectation and eliminating the absolute value function, we have

\begin{align*}
  \min_{\bm w,\bm y}\quad &
  -\bm\mu\tran\bm w+\frac\lambda n\bm1\tran\bm y\,, \\
  \text{s.t.}\quad &
  \bm1\tran\bm w=1\,, \\&
  \left(\begin{array}{c|ccc}
    (-\bm r_1+\bm\mu)\tran & 1 \\
    \vdots && \ddots \\
    (-\bm r_n+\bm\mu)\tran &&& 1 \\
    \hline
    (\bm r_1-\bm\mu)\tran & 1 \\
    \vdots && \ddots \\
    (\bm r_n-\bm\mu)\tran &&& 1 \\
  \end{array}\right)
  \begin{pmatrix}
    \bm w \\ \bm y
  \end{pmatrix}
  \succeq\bm 0\,.
\end{align*}


## Script

\inputminted{python}{q3/main_lp.py}

## Result

\includegraphics{q3/main_lp.pdf}

The optimal (vertex) portfolios of two frontiers are listed as follows.

\begin{tabular}{lrrrrr}
  \toprule
  & $w_1$ & $w_2$ & $w_3$ & Std Dev & Mean \\
  \midrule
  $\mu$-$\sigma$ frontier & -0.079722 & 0.275317 & 0.804405 & 0.111404 & 0.081520 \\
  $\mu$-MAD frontier & -0.089373 & 0.289497 & 0.799876 & 0.111425 & 0.081321 \\
  \bottomrule
\end{tabular}

## Discussion

Two frontiers almost overlap on the plot, which is unsurprising since it is easy to prove that two optimization problems are equivalent using the formula of Question 2.
