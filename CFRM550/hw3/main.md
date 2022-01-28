---
title: CFRM 550, 2021 Autumn, HW 3
...

# 3.1

> Let $W$ be a Brownian motion and let $\mathbf F=(\mathcal F_n)_{n\in\mathbb N_0}$ be a filtration for $W$. Show that $W_t^2–t$ is a martingale w.r.t.\ $\mathbf F$.

1. Plugging $W_t=W_s+(W_t-W_s)$ into $\E\left(W_t^2-t\middle|\mathcal F_s\right)$ and extracting $W_s$ from the expectation yields \begin{equation}\label{eq:3.1.1}\E\left(W_t^2-t\middle|\mathcal F_s\right)=W_s^2+2W_s\E(W_t-W_s|\mathcal F_s)+\E\left((W_t-W_s)^2\middle|\mathcal F_s\right)-t\,.\end{equation}
1. Given $W$ be a Brownian motion, we have $W_t-W_s\sim\mathcal N(0,t-s)$, i.e.\ \begin{equation}\label{eq:3.1.2}\E(W_t-W_s|\mathcal F_s)=0\end{equation} and \begin{equation}\label{eq:3.1.3}\E\left((W_t-W_s)^2\middle|\mathcal F_s\right)=\Var\left(W_t-W_s\middle|\mathcal F_s\right)+\E(W_t-W_s|\mathcal F_s)^2=t-s\,.\end{equation}
1. Plugging Eq.\ (\ref{eq:3.1.2}) and (\ref{eq:3.1.3}) into Eq.\ (\ref{eq:3.1.1}) yields $$\E\left(W_t^2-t\middle|\mathcal F_s\right)=W_s^2-s\,,$$ i.e., $W_t^2-t$ is a martingale w.r.t.\ $\mathbf F$.

# 3.2

> A Poisson process with intensity $\lambda$ is a continuous-time process $\mathbf N=(N_t)_{t\ge0}$ with the property that, for every $t\ge0$, we have $$\Pr(N_t=n)=\frac{(\lambda t)^ne^{–\lambda t}}{n!}\,,\quad n\in\{0,1,2,\dots\}\,.$$ In other words, $N_t$ is a Poisson random variable with parameter $\lambda t$. Compute the characteristic function of $W_{N_t}$ where $\mathbf N$ is a Poisson process with intensity $\lambda$ and Brownian motion $W$ is independent of the Poisson process $\mathbf N$.

1. By definition, the characteristic function of $W_{N_t}$ is $\phi(t)=\E\left(e^{itW_{N_t}}\right)$, which by iterated conditioning gives $\phi(t)=\E\left(\E\left(e^{itW_{N_t}}\middle|N_t\right)\right)$.
1. Given $W$ is a Brownian motion, we have $W_{N_t}\sim\mathcal N(0,N_t)$, i.e., $\E\left(e^{itW_{N_t}}\middle|N_t\right)=e^{-\frac{t^2N_t}2}$, $\phi(t)=\E\left(e^{-\frac{t^2N_t}2}\right)$.
1. Given $N_t$ is a Poisson random variable with parameter $\lambda t$, we have $$\E\left(e^{-\frac{t^2N_t}2}\right)=\sum_{n=0}^\infty\frac{(\lambda t)^ne^{–\lambda t}}{n!}e^{-\frac{t^2n}2}\,.$$ Applying formula $\sum_{n=0}^\infty\frac{a^n}{n!}=e^a$ yields $$\E\left(e^{-\frac{t^2N_t}2}\right)=\exp\left(\lambda te^{-\frac{t^2}2}-\lambda t\right)\,.$$
1. Therefore, the characteristic function of $W_{N_t}$ is $$\phi(t)=\exp\left(\lambda te^{-\frac{t^2}2}-\lambda t\right)\,.$$

# 3.3

> The $m^\text{th}$ variation of function $f$ over interval $[0,T]$ is defined as $$V_T(m,f)=\lim_{\|\Pi\|\to0}\sum_{j=0}^{n-1}\left|f(t_{j+1})–f(t_j)\right|^m,\quad\Pi=\{t_0=0,\dots,t_n=T\},\quad\|\Pi\|=\max_j(t_{j+1}–t_j)\,.$$ Show that $V_T(1,W)=\infty$ and $V_T(3,W)=0$, where $W$ is a Brownian motion.

a.  1. Evidently we have $$\sum_{j=0}^{n-1}(f(t_{j+1})–f(t_j))^2\le\left(\max_{j=0}^{n-1}|f(t_{j+1})–f(t_j)|\right)\left(\sum_{j=0}^{n-1}|f(t_{j+1})–f(t_j)|\right)\,.$$ Substituting $f$ with $W$ and applying $\lim_{\|\Pi\|\to0}$ to both sides of the inequality yields \begin{equation}\label{eq:3.3.1}V_T(2,W)\le\left(\lim_{\|\Pi\|\to0}\max_{j=0}^{n-1}\left|W_{t_{j+1}}–W_{t_j}\right|\right)V_T(1,W)\,.\end{equation}
    1. By Theorem 3.3.3, we have \begin{equation}\label{eq:3.3.2}V_T(2,W)=T\,.\end{equation}
    1. Given $W$ is uniformly continuous on $[0,T]$, we have \begin{equation}\label{eq:3.3.3}\lim_{\|\Pi\|\to0}\max_{j=0}^{n-1}\left|W_{t_{j+1}}–W_{t_j}\right|=0\,.\end{equation}
    1. Plugging Eq.\ (\ref{eq:3.3.2}) and (\ref{eq:3.3.3}) into Eq.\ (\ref{eq:3.3.1}) yields $T\le0V_T(1,W)$, which gives $V_T(1,W)=\infty$.
a.  1. Evidently we have $$\sum_{j=0}^{n-1}|f(t_{j+1})–f(t_j)|^3\le\left(\max_{j=0}^{n-1}|f(t_{j+1})–f(t_j)|\right)\left(\sum_{j=0}^{n-1}(f(t_{j+1})–f(t_j))^2\right)\,.$$ Substituting $f$ with $W$ and applying $\lim_{\|\Pi\|\to0}$ to both sides of the inequality yields \begin{equation}\label{eq:3.3.4}V_T(3,W)\le\left(\lim_{\|\Pi\|\to0}\max_{j=0}^{n-1}\left|W_{t_{j+1}}–W_{t_j}\right|\right)V_T(2,W)\,.\end{equation}
    1. Plugging Eq.\ (\ref{eq:3.3.2}) and (\ref{eq:3.3.3}) into Eq.\ (\ref{eq:3.3.4}) yields $V_T(3,W)\le0$. Evidently $V_T(3,W)$ is non-negative, which gives $V_T(3,W)=0$.

# 3.4

> Define $$X_t=\mu t+W_t\,,\quad\tau_m=\inf\{t\ge0:X_t=m\}\,,$$ where $\mathbf W=(W_t)_{t\ge0}$ is a Brownian motion. Let $\mathbf F=(\mathcal F_t)_{t\ge0}$ be a filtration for $W$. Show that $Z$ is a martingale w.r.t.\ $\mathbf F$ where $$Z_t=\exp\left(\sigma X_t-\left(\sigma\mu+\frac{\sigma^2}2\right)t\right)\,.$$ Assume $\mu>0$ and $m\ge0$. Assume further that $\tau_m<\infty$ with probability one and the stopped process $Z_{t\land\tau_m}$ is a martingale. Find the Laplace transform $\E\left(e^{-\alpha\tau_m}\right)$.

a.  1. By the definitions of $X$ and $Z$, we have $$\E(Z_t|\mathcal F_s)=\E\left(e^{\sigma W_t-\frac{\sigma^2t}2}\middle|\mathcal F_s\right)\,.$$ Plugging in $W_t=W_s+(W_t-W_s)$ and extracting $W_s$ from the expectation yields \begin{equation}\label{eq:3.4.1}\E(Z_t|\mathcal F_s)=e^{\sigma W_s-\frac{\sigma^2t}2}\E\left(e^{\sigma(W_t-W_s)}\middle|\mathcal F_s\right)\,.\end{equation}
    1. Given $W$ is a Brownian motion, we have $W_t-W_s\sim\mathcal N(0,t-s)$, which gives \begin{equation}\label{eq:3.4.2}\E\left(e^{\sigma(W_t-W_s)}\middle|\mathcal F_s\right)=e^{\frac{(t-s)\sigma^2}2}\,.\end{equation}
    1. Plugging Eq.\ (\ref{eq:3.4.2}) into Eq.\ (\ref{eq:3.4.1}) yields $\E(Z_t|\mathcal F_s)=e^{\sigma W_s-\frac{\sigma^2s}2}$, or $\E(Z_t|\mathcal F_s)=Z_s$, i.e., $Z$ is a martingale w.r.t.\ $\mathbf F$.
a.  1. From the proof of Theorem 3.5.2, we have $$1=\E\left(\lim_{t\to\infty}e^{-\frac{(t\land\tau_m)\sigma^2}2+\sigma W_{t\land\tau_m}}\right)\,.$$ Plugging in $W_t=X_t-\mu t$ and $\lim_{t\to\infty}X_{t\land\tau_m}=m$ yields \begin{equation}\label{eq:3.4.3}1=\E\left(e^{-\left(\frac{\sigma^2}2+\mu\sigma\right)\tau_m+\sigma m}\right)\,.\end{equation}
    1. Let \begin{equation}\label{eq:3.4.4}\alpha=\frac{\sigma^2}2+\mu\sigma\,.\end{equation} Applying the quadratic formula to Eq. (\ref{eq:3.4.4}) yields \begin{equation}\label{eq:3.4.5}\sigma=-\mu\pm\sqrt{\mu^2+2\alpha}\,.\end{equation}
    1. Plugging Eq.\ (\ref{eq:3.4.4}) and (\ref{eq:3.4.5}) into Eq.\ (\ref{eq:3.4.3}) yields $$1=\E\left(e^{-\alpha\tau_m-\mu m\pm m\sqrt{\mu^2+2\alpha}}\right)\,.$$ Given $\alpha>0$, $\mu>0$, $\tau_m>0$, and $m\ge0$, the $\pm$ could only be a +. Therefore, $$\E\left(e^{-\alpha\tau_m}\right)=e^{\mu m-m\sqrt{\mu^2+2\alpha}}\,.$$
