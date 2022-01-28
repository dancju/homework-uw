---
title: CFRM 550, 2021 Autumn, HW 7
...

**Exercise 7.1.**

Consider a financial market defined on a probability space $(\Omega,\mathcal F,\Pr)$ consisting of two assets: stock $S$ and money market account $M$ with $$M_t=M_0e^{rt}\,,\quad S_t=S_0e^{X_t}\,,\quad X_t=\mu t+\sigma\widetilde W_t+\int_{\mathbb R} z\widetilde N(t,\diff z)\,,$$ where $\widetilde W$ is a Brownian motion under $\widetilde{\Pr}$ and $\widetilde N(\diff t,\diff z)=N(\diff t,\diff z)-\nu(\diff z)\diff t$ with $\widetilde{\E}N(\diff t,\diff z)=\nu(\diff z)\diff t$.

a) Suppose that $\widetilde{\Pr}$ is the market's pricing measure with money market account $M$ as numéraire. Then $S/M$ must be a martingale under $\widetilde{\Pr}$. Find $\mu$.
a) Let $V_t$ be the price of a derivative asset that pays $S_T^p$ at time $T$. Show that $V_t=v(t,S_t)$ and find function $v$.

**Solution**

a)  1. Given $S/M$ is a martingale, we have $$\forall 0\le s\le t:\quad\frac{S_s}{M_s}=\widetilde{\E}\left(\frac{S_t}{M_t}\middle|\mathcal F_s\right)\,.$$ Plugging in $M_t=M_0e^{rt}$ and $S_t=S_0e^{X_t}$ yields $$\forall 0\le s\le t:\quad e^{(t-s)r}=\widetilde{\E}\left(e^{X_t-X_s}\middle|\mathcal F_s\right)\,.$$ Substituting $s$ with 0 yields \begin{equation}\label{eq:7.1.1}\forall0\le t:\quad e^{rt}=\widetilde{\E}\left(e^{X_t}\right)\,.\end{equation}
    1. Given $X_t=\mu t+\sigma\widetilde W_t+\int_{\mathbb R} z\widetilde N(t,\diff z)$, by the Lévy-Khintchine formula, we have \begin{equation}\label{eq:7.1.2}\E\left(e^{i\langle u,X_t\rangle}\right)=e^{t\psi(u)}\,,\end{equation} where \begin{equation}\label{eq:7.1.3}\psi(u)=i\langle\mu,u\rangle-\frac12\left\langle u,\sigma^2 u\right\rangle+\int_{\mathbb R}\left(e^{i\langle u,z\rangle}-1-i\langle u,z\rangle\right)\nu(\diff z)\,.\end{equation} Substituting $u$ with $-i$ yields \begin{equation}\label{eq:7.1.4}\E\left(e^{X_t}\right)=e^{t\psi(-i)}\,,\end{equation} where \begin{equation}\label{eq:7.1.5}\psi(-i)=\mu+\frac{\sigma^2}2+\int_{\mathbb R}\left(e^z-1-z\right)\nu(\diff z)\,.\end{equation}
    1. Merging Eq.\ (\ref{eq:7.1.1}), (\ref{eq:7.1.4}), and (\ref{eq:7.1.5}) yields $$\mu=r-\frac{\sigma^2}2-\int_{\mathbb R}\left(e^z-1-z\right)\nu(\diff z)\,.$$
a)  1. According to the fundamental theorem of asset pricing, $V/M$ is a martingale, i.e. $$\frac{V_t}{M_t}=\E\left(\frac{V_T}{M_T}\middle|\mathcal F_t\right)\,.$$ Plugging in $M_t=M_0e^{rt}$, $S_t=S_0e^{X_t}$, and $V_T=S_T^p$ yields $$V_t=\frac{S_t^p\E\left(e^{(X_T-X_t)p}\middle|\mathcal F_t\right)}{e^{(T-t)r}}\,.$$ Given $X_t$ is a Lévy process, we have \begin{equation}\label{eq:7.1.6}V_t=\frac{S_t^p\E\left(e^{pX_{T-t}}\right)}{e^{(T-t)r}}\,.\end{equation}
    1. Substituting $u$ with $-pi$ in Eq.\ (\ref{eq:7.1.2}) and (\ref{eq:7.1.3}) yields
    \begin{equation}\label{eq:7.1.7}\E\left(e^{pX_t}\right)=e^{t\psi(-ip)}\,,\end{equation} where \begin{equation}\label{eq:7.1.8}\psi(-ip)=\mu p+\frac{\sigma^2p^2}2+\int_{\mathbb R}\left(e^{pz}-1-pz\right)\nu(\diff z)\,.\end{equation}
    2. Merging Eq.\ (\ref{eq:7.1.6}), (\ref{eq:7.1.7}), and (\ref{eq:7.1.8}) yields $$V_t=S_t^pe^{(T-t)\left(-r+\mu p+\frac{\sigma^2p^2}2+\int_{\mathbb R}\left(e^{pz}-1-pz\right)\nu(\diff z)\right)}\,.$$
