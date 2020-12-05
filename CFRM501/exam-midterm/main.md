---
title: CFRM 501, 2020 Autumn, Midterm
...

I did not give or receive any unauthorized help during this test.

# 1

Given

\begin{align*}
\bm w_a &=\bm w_p-\bm w_b \\
\bm w_b\tran\bm 1 &=1 \\
\bm w_p\tran\bm 1 &=1
\end{align*}

we have

$$\bm w_a\tran\bm 1=0.$$

Therefore, we can maximize the manager's utility function with the model

\begin{align*}
\text{max}\quad &
\bm w_a\tran\bm\mu-\frac{\gamma}{2}\bm w_a\tran\bm\Sigma\bm w_a \\
\text{s.t.}\quad &
\bm w_a\tran\bm 1=0
\end{align*}

which is equivalent to the Lagrange function

$$\mathcal L(\bm w_a,\lambda)=\bm w_a\tran\bm\mu-\frac{\gamma}{2}\bm w_a\tran\bm\Sigma\bm w_a+\lambda\bm w_a\tran\bm 1,$$

$$\nabla_{\bm w_a}\mathcal L(\bm w_a,\lambda)=\bm\mu-\gamma\bm\Sigma\bm w_a+\lambda\bm 1.$$

Letting $\nabla_{\bm w_a}\mathcal L(\bm w_a,\lambda)=0$ yields

$$\bm w_a^*=\frac{1}{\gamma}\bm\Sigma^{-1}(\bm\mu-\lambda\bm 1)$$

Plugging back into the constraint yields

$$\lambda=\frac{\bm 1\tran\bm\Sigma^{-1}\bm\mu}{\bm1\tran\bm\Sigma^{-1}\bm1}.$$

Plugging back into $\bm w_a^*$ yields

$$\bm w_a^*=\frac{1}{\gamma}\bm\Sigma^{-1}\left(\bm\mu-\frac{\bm 1\tran\bm\Sigma^{-1}\bm\mu}{\bm1\tran\bm\Sigma^{-1}\bm1}\bm 1\right)$$

$$\bm w_p^*=\bm w_b+\frac{1}{\gamma}\bm\Sigma^{-1}\left(\bm\mu-\frac{\bm 1\tran\bm\Sigma^{-1}\bm\mu}{\bm1\tran\bm\Sigma^{-1}\bm1}\bm 1\right)$$

# 2

$$W_1=W_0+\theta\Delta$$

$$U(W)=-e^{-\gamma W}$$

The expected exponential utility is

\begin{align*}
\E(U(W_1)) &
=\E\left(-e^{-\gamma(W_0+\theta\Delta)}\right) \\&
=-e^{-\gamma W_0-\gamma\theta\mu+\frac{\gamma^2\theta^2\sigma^2}{2}}
\end{align*}

The optimal parameter maximizing the expectation above is

\begin{align*}
\theta^* &
=\argmax_\theta\E(U(W_1)) \\&
=\argmin_\theta\frac{\gamma^2\theta^2\sigma^2}{2}-\gamma\theta\mu \\&
=\frac{\mu}{\gamma\sigma^2}
\end{align*}

# 3

## 3.a

Letting the percentages of wealth invested in the risk-free asset and the tangency portfolio be $w_f$ and $w_T$, we have

$$w_f+w_T=1,\quad\E(r)=w_fr_f+w_T\mu_T,\quad\Var(r)=w_T^2\sigma_T^2$$

The mean-variance criteria is

\begin{align*}
\quad\E(r)-\frac{\gamma}{2}\Var(r) &
=w_fr_f+w_T\mu_T-\frac{\gamma}{2}w_T^2\sigma_T^2 \\&
=r_f(1-w_T)+w_T\mu_T-\frac{\gamma}{2}w_T^2\sigma_T^2
\end{align*}

We have the optimal percentages of invested wealth

$$w_T^*=\frac{\mu_T-r_f}{\gamma\sigma_T^2},\quad w_f^*=1-w_T^*.$$

## 3.b

Given 100% of wealth invested in the tangency portfolio, we have

$$w_T^*=1$$

$$\gamma^*=\frac{\mu_T-r_f}{\sigma_T^2}$$

## 3.c

\includegraphics{q3/main.pdf}

# 4

## 4.a

diversification

## 4.b

$$
\E(e^X)=e^{\mu+\frac{\sigma^2}{2}}
$$

## 4.c

sovereign wealth funds
