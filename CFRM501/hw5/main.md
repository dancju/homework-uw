---
title: CFRM 501, 2020 Autumn, HW 5
...

# 1

\begin{align*}
\E(X_j) &
=\E(\alpha_j+\beta_jY+\epsilon_j) \\&
=\alpha_j+\beta_j\E(Y)+\E(\epsilon_j) \\&
=\alpha_j+\beta_j\mu_y
\end{align*}

\begin{align*}
\Var(X_j) &
=\Var(\alpha_j+\beta_jY+\epsilon_j) \\&
=\beta_j^2\Var(Y)+\Var(\epsilon_j)-2\beta_j\Cov(Y,\epsilon_j) \\&
=\beta_j^2\sigma_y^2+\sigma_\epsilon^2
\end{align*}

\begin{align*}
\Cov(X_j,Y) &
=\Cov(\alpha_j+\beta_jY+\epsilon_j,Y) \\&
=\beta_j\Var(Y)+\Cov(\epsilon_j,Y) \\&
=\beta_j\sigma_y^2
\end{align*}

\begin{align*}
\Cov(X_i,X_j) &
=\Cov(\alpha_i+\beta_iY+\epsilon_i, \alpha_j+\beta_jY+\epsilon_j) \\&
=\beta_i\beta_j\Var(Y)+\beta_i\Cov(Y,\epsilon_j)+\beta_j\Cov(Y,\epsilon_i)+\Cov(\epsilon_i,\epsilon_j) \\&
=\beta_i\beta_j\sigma_y^2+\rho_{i,j}\sigma_\epsilon^2
\end{align*}

\begin{align*}
\Var(r_p) &
=\Var\left(r_0+\bm w\tran\bm\beta r_{\text{m,e}}+\bm w\tran\bm\epsilon\right) \\&
=\Var(\bm w\tran\bm\beta r_{\text{m,e}})+\Var(\bm w\tran\bm\epsilon)+2\Cov(\bm w\tran\bm\beta r_{\text{m,e}}, \bm w\tran\bm\epsilon) \\&
=\left(\bm w\tran\bm\beta\right)^2\sigma_m^2+\sum_i\sum_jw_iw_j\sigma_\epsilon^2\rho_{i,j}+0 \\&
=\beta_p^2\sigma_m^2+\sigma_\epsilon^2\bm w\tran\bm{\rho w}
\end{align*}

# 2

Upon the given equation, multiplying both sides by $w_{m,j}$ and take a sum as $j$ goes from 1 to $n$ yields

$$\sum_j(r_j-r_0)w_{m,j}=\sum_j\left((r_m-r_0)\beta_j+\epsilon_j\right)w_{m,j}\,,$$

\begin{equation}r_{m,e}=\sum_j\left(r_{m,e}\beta_j+\epsilon_j\right)w_{m,j}\,.\end{equation}

Applying $\E(\cdot)$ on two sides of Equation (1) yields

\begin{equation}1=\bm\beta\tran\bm w_m\,.\end{equation}

Applying $\Var(\cdot)$ on two sides of Equation (1) yields

\begin{equation}\sigma_m^2=\bm\beta\tran\bm w_m\sigma_m^2+\sigma_\epsilon^2\bm w_m\tran\bm\rho\bm w_m\,.\end{equation}

Plugging Equation (2) into Equation (3) yields

$$\sigma_m^2=\sigma_m^2+\sigma_\epsilon^2\bm w_m\tran\bm\rho\bm w_m\,.$$

So far, we find an inconsistency since $\sigma_\epsilon^2\bm w_m\tran\bm\rho\bm w_m$ is obviously not zero. Next, we will prove that $\sigma_\epsilon^2\bm w_m\tran\bm\rho\bm w_m$ tends to zero under the condition that

1. all $\epsilon_j$-s are independent; and
1. $n$ becomes very large.

Since all $\epsilon_j$ are independent, we have $\bm w_m\tran\bm\rho\bm w_m=\|\bm w_m\|_2^2$.

Since the market portfolio weights sum to one, i.e.\ $\|\bm w_m\|_1=1$, we have $\lim_{n\to\infty}\|\bm w_m\|_2=0$, or

$$\lim_{n\to\infty}\sigma_\epsilon^2\|\bm w_m\|_2^2=0\,,$$

$$\lim_{n\to\infty}\sigma_\epsilon^2\bm w_m\tran\bm\rho\bm w_m=0\,.$$
