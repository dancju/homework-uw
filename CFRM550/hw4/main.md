---
title: CFRM 550, 2021 Autumn, HW 4
...

# 4.2

> Find an explicit expression for $Y_T$ where $\diff Y_t=r\diff t+\alpha Y_t\diff W_t$.

1. Supposing $$Z_t=e^{-\alpha W_t+\frac{\alpha^2t}2}\,,$$ by Itô's lemma, we have $$\diff Z_t=\alpha^2Z_t\diff t-\alpha Z_t\diff W_t\,.$$
1. Applying the product rule to $\diff(Y_tZ_t)$, plugging in $\diff Y_t$ and $\diff Z_t$, and applying rules $\diff W_t\diff W_t=\diff t$ and $\diff W_t\diff t=\diff t\diff t=0$ yields $$\diff(Y_tZ_t)=rZ_t\diff t\,.$$
1. Plugging $\diff(Y_tZ_t)$ and $Z_t$ into $Y_TZ_T-Y_0Z_0=\int_{t=0}^T\diff(Y_tZ_t)$, we have $$Y_TZ_T-Y_0Z_0=r\int_0^Te^{-\alpha W_t+\frac{\alpha^2t}2}\diff t\,,$$ which gives $$Y_T=\left(Y_0+r\int_0^Te^{-\alpha W_t+\frac{\alpha^2t}2}\diff t\right)e^{\alpha W_T-\frac{\alpha^2T}2}\,.$$

# 4.3

> Suppose $X,\Delta$, and $\Pi$ are given by $$\diff X_t=\sigma X_t\diff W_t\,,\quad\Delta_t=\frac{\partial f}{\partial x}(t,X_t)\,,\quad\Pi_t=X_t\Delta_t\,,$$ where $f$ is a smooth function. Show that if $f$ satisfies $$\left(\frac{\partial}{\partial t}+\frac{\sigma^2x^2}2\frac{\partial^2}{\partial x^2}\right)f(t,x)=0$$ for all $(t,x)$, then $\Pi$ is a martingale w.r.t.\ a filtration $(\mathcal F_t)_{0\le t\le T}$ for $W$.

1. Plugging $x=X_t$ into $\left(\frac{\partial}{\partial t}+\frac{\sigma^2x^2}2\frac{\partial^2}{\partial x^2}\right)f(t,x)=0$ and differentiating w.r.t.\ $X_t$ yields \begin{equation}\label{eq:4.3.1}\frac{\partial^2f(t,X_t)}{\partial t\partial X_t}+\sigma^2X_t\frac{\partial^2f(t,X_t)}{\partial X_t^2}+\frac{\sigma^2X_t^2}2\frac{\partial^3f(t,X_t)}{\partial X_t^3}=0\,.\end{equation}
1. Given $\diff X_t=\sigma X_t\diff W_t$, by Itô's lemma, we have $$\diff\Delta_t=\frac{\partial\Delta_t}{\partial t}\diff t+\frac{\sigma^2X_t^2}2\frac{\partial^2\Delta_t}{\partial X_t^2}\diff t+\sigma X_t\frac{\partial\Delta_t}{\partial X_t}\diff W_t\,.$$ Plugging in $\Delta_t=\frac{\partial f}{\partial x}(t,X_t)$ yeids \begin{equation}\label{eq:4.3.2}\diff\Delta_t=\frac{\partial^2f(t,X_t)}{\partial t\partial X_t}\diff t+\frac{\sigma^2X_t^2}2\frac{\partial^3f(t,X_t)}{\partial X_t^3}\diff t+\sigma X_t\frac{\partial^2f(t,X_t)}{\partial X_t^2}\diff W_t\,.\end{equation}
1. Merging Eq.\ (\ref{eq:4.3.1}) and Eq.\ (\ref{eq:4.3.2}) yields \begin{equation}\label{eq:4.3.3}\diff\Delta_t=-\sigma^2X_t\frac{\partial^2f(t,X_t)}{\partial X_t^2}\diff t+\sigma X_t\frac{\partial^2f(t,X_t)}{\partial X_t^2}\diff W_t\,.\end{equation}
1. Given $\Pi_t=X_t\Delta_t$, by the product rule, we have $$\diff\Pi_t=X_t\diff\Delta_t+\Delta_t\diff X_t+\diff X_t\diff\Delta_t\,.$$ Plugging in $\diff X_t=\sigma X_t\diff W_t$ and Eq.\ (\ref{eq:4.3.3}), and applying rules $\diff W_t\diff W_t=\diff t$ and $\diff W_t\diff t=\diff t\diff t=0$ yields $$\diff\Pi_t=\left(X_t\frac{\partial^2f(t,X_t)}{\partial X_t^2}+\frac{\partial f(t,X_t)}{\partial X_t}\right)\sigma X_t\diff W_t\,.$$ Since Itô integrals are martingales, it follows that $\Pi$ is a martingale w.r.t.\ filtration $\mathcal F$ for $W$.

# 4.4

> Suppose $X$ is given by $\diff X_t=\mu(t,X_t)\diff t+\sigma(t,X_t)\diff W_t$. For any smooth function $f$, define \begin{small}$$M_t^f=f(t,X_t)–f(0,X_0)–\int_0^t\left(\frac{\partial}{\partial s}+\mu(s,X_s)\frac{\partial}{\partial x}+\frac{\sigma^2(s,X_s)}2\frac{\partial^2}{\partial x^2}\right)f(s,X_s)\diff s\,.$$\end{small} Show that $M^f$ is a martingale w.r.t.\ a filtration ${\mathcal F_t}_{0\le t\le T}$ for $W$.

1. Given $\diff X_t=\mu(t,X_t)\diff t+\sigma(t,X_t)\diff W_t$, by Itô's lemma, we have \begin{footnotesize}$$\diff f(t,X_t)=\left(\frac{\partial}{\partial t}+\mu(t,X_t)\frac{\partial}{\partial X_t}+\frac{\sigma^2(t,X_t)}2\frac{\partial^2}{\partial X_t^2}\right)f(t,X_t)\diff t+\sigma(t,X_t)\frac{\partial f(t,X_t)}{\partial X_t}\diff W_t\,,$$\end{footnotesize} merging which with the definition of $M_t^f$ yields $$\diff M_t^f=\sigma(t,X_t)\frac{\partial f(t,X_t)}{\partial X_t}\diff W_t\,.$$ Since Itô integrals are martingales, it follows that $M^f$ is a martingale w.r.t.\ filtration $\mathcal F$ for $W$.

# 4.5

> Let $\mathbf X=(X_t)_{0\le t\le T}$ be an OU process on probability space $(\Omega,\mathcal F,\Pr)$ such that $$\diff X_t=K(\theta–X_t)\diff t+\sigma\diff W_t\,,$$ where $\mathbf W=(W_t)_{0\le t\le T}$ is a Brownian motion under probability measure $\Pr$. Then we can define a new probability measure $\widetilde{\Pr}$ such that process $\widetilde{\mathbf W}=(\widetilde W_t)_{0\le t\le T}$ is a Brownian motion under $\widetilde{\Pr}$. Then the OU process $\mathbf X$ on probability space $(\Omega,\mathcal F,\widetilde{\Pr})$ will be $$\diff X_t=K(\theta^*–X_t)\diff t+\sigma\diff\widetilde W_t\,.$$ Find the Radon-Nikodým derivative $\frac{\diff\widetilde{\Pr}}{\diff\!\Pr}$.

1. Given $\mathbf W$ is a Brownian motion under $\Pr$ and $\widetilde{\mathbf W}$ is a Brownian motion under $\widetilde{\Pr}$, by Girsanov theorem, there exists a process $(\Theta_t)_{0\le t\le T}$ being adapted to filtration $\mathcal F$ satisfying \begin{equation}\label{eq:4.5.1}\frac{\diff\widetilde{\Pr}}{\diff\!\Pr}=\exp\left(-\frac12\int_0^t\Theta_s^2\diff s-\int_0^t\Theta_s\diff W_s\right)\,,\end{equation} and \begin{equation}\label{eq:4.5.2}\diff\widetilde W_t=\Theta_t\diff t+\diff W_t\,.\end{equation}
1. Merging $\diff X_t=K(\theta–X_t)\diff t+\sigma\diff W_t$, $\diff X_t=K(\theta^*–X_t)\diff t+\sigma\diff\widetilde W_t$, and Eq.\ (\ref{eq:4.5.2}) yields $$\Theta_t=\frac{(\theta-\theta^*)K}\sigma\,.$$ Plugging into Eq.\ (\ref{eq:4.5.1}) yields $$\frac{\diff\widetilde{\Pr}}{\diff\!\Pr}=\exp\left(-\frac{(\theta-\theta^*)^2K^2t}{2\sigma^2}-\frac{(\theta-\theta^*)K}\sigma\int_0^t\diff W_s\right)\,.$$
<!-- TODO check answer-->

# 4.6

> Consider the Black-Sholes model described in Example 4.5.4. Suppose that, instead of taking the money market account $M$ as numéraire, we take the stock price as numéraire the stock price S.
>
> a. Find a change of measure $\frac{\diff\widehat{\Pr}}{\diff\!\Pr}$ under which $X/S$ is a $(\widehat{\Pr},\mathcal F)$ martingale for all self-financing
portfolios $X$.
> a. What are the dynamics of $M/S$ under $\widehat{\Pr}$? That is, find $\Theta_t$ and $\Delta_t$ such that $\diff\frac{M_t}{S_t}=\Theta_t\diff t+\Delta_t\diff\widehat W_t$ where $\widehat W$ is a $(\widehat{\Pr},\mathcal F)$ Brownian motion.

a.  1. Given $\diff S_t=\mu S_t\diff t+\sigma S_t\diff W_t$, by Itô's lemma, we have \begin{equation}\label{eq:4.6.1}\diff\frac1{S_t}=\frac{(-\mu+\sigma^2)\diff t-\sigma\diff W_t}{S_t}\,.\end{equation}
    1. Applying the product rule to $\diff\frac{X_t}{S_t}$ yields \begin{equation}\label{eq:4.6.2}\diff\frac{X_t}{S_t}=X_t\diff\frac1{S_t}+\frac1{S_t}\diff X_t+\diff X_t\diff\frac1{S_t}\,.\end{equation}
    1. Plugging Eq.\ (\ref{eq:4.6.1}) and $\diff X_t=\Delta_t S_t(\mu–r)\diff t+\Delta_t\sigma S_t\diff W_t+X_tr\diff t$ into Eq.\ (\ref{eq:4.6.2}) and applying rules $\diff W_t\diff W_t=\diff t$ and $\diff W_t\diff t=\diff t\diff t=0$ yields \begin{equation}\label{eq:4.6.3}\diff\frac{X_t}{S_t}=\left(-r+\mu-\sigma^2\right)\left(\Delta_t-\frac{X_t}{S_t}\right)\diff t+\sigma\left(\Delta_t-\frac{X_t}{S_t}\right)\diff W_t\,.\end{equation}
    1. Given $\widehat{\Pr}$ is equivalent to $\Pr$, by Girsanov theorem, there exists a process $(\Gamma_t)_{0\le t\le T}$ being adapted to filtration $\mathcal F$ satisfying \begin{equation}\label{eq:4.6.4}\frac{\diff\widehat{\Pr}}{\diff\!\Pr}=\exp\left(-\frac12\int_0^t\Gamma_s^2\diff s-\int_0^t\Gamma_s\diff W_s\right)\,,\end{equation} and \begin{equation}\label{eq:4.6.5}\diff\widehat W_t=\Gamma_t\diff t+\diff W_t\,.\end{equation}
    1. Plugging Eq.\ (\ref{eq:4.6.5}) into Eq.\ (\ref{eq:4.6.3}) yields \begin{equation}\label{eq:4.6.6}\diff\frac{X_t}{S_t}=\left(-r+\mu-\sigma^2-\sigma\Gamma_t\right)\left(\Delta_t-\frac{X_t}{S_t}\right)\diff t+\sigma\left(\Delta_t-\frac{X_t}{S_t}\right)\diff\widehat W_t\,.\end{equation}
    1. Given $X/S$ is a $(\widehat{\Pr},\mathcal F)$ martingale, the drift term of $\diff\frac{X_t}{S_t}$ is zero, i.e., \begin{equation}\label{eq:4.6.7}\Gamma_t=\frac{-r+\mu}\sigma-\sigma\,.\end{equation}
    1. Plugging Eq.\ (\ref{eq:4.6.7}) into Eq.\ (\ref{eq:4.6.4}) yields the Radon-Nikodým derivative $$\frac{\diff\widehat{\Pr}}{\diff\!\Pr}=\exp\left(-\frac12\left(\frac{-r+\mu}\sigma-\sigma\right)^2t-\left(\frac{-r+\mu}\sigma-\sigma\right)\int_0^t\diff W_s\right)\,.$$
a.  1. Applying the product rule to $\diff\frac{M_t}{S_t}$ yields \begin{equation}\label{eq:4.6.8}\diff\frac{M_t}{S_t}=M_t\diff\frac1{S_t}+\frac1{S_t}\diff M_t+\diff M_t\diff\frac1{S_t}\,.\end{equation}
    1. Plugging Eq.\ (\ref{eq:4.6.1}) and $\diff M_t=rM_t\diff t$ into Eq.\ (\ref{eq:4.6.8}), and applying rules $\diff W_t\diff W_t=\diff t$ and $\diff W_t\diff t=\diff t\diff t=0$ yields \begin{equation}\label{eq:4.6.9}\diff\frac{M_t}{S_t}=\frac{M_t}{S_t}\left(\left(r-\mu+\sigma^2\right)\diff t-\sigma\diff W_t\right)\,.\end{equation}
    1. Merging Eq.\ (\ref{eq:4.6.5}), (\ref{eq:4.6.7}), and (\ref{eq:4.6.9}) yields $$\diff\frac{M_t}{S_t}=-\frac{\sigma M_t}{S_t}\diff\widehat W_t\,.$$

# 4.7

> Consider a market with stochastic interest rates $R=(R_t)_{0\le t\le T}$. The Cox-Ingersoll-Ross (CIR) model for $R$ is $$\diff R_t=\kappa(\theta–R_t)\diff t+\delta\sqrt{R_t}\diff W_t\,,$$ where $W$ is a Brownian motion under the real-world probability measure $\Pr$. Note that, in this model, $R_t\ge0$ for all $t\in[0,T]$. Show that, under the following change of measure $$\frac{\diff\widetilde{\Pr}}{\diff\!\Pr}=\exp\left(-\frac{\lambda^2}2\int_0^TR_t\diff t-\lambda\int_0^T\sqrt{R_t}\diff W_t\right)\,,$$ the dynamics of $R$ have the form $$\diff R_t=\tilde\kappa\left(\tilde\theta–R_t\right)\diff t+\delta\sqrt{R_t}\diff\widetilde W_t\,,$$ and find $\tilde\kappa$ and $\tilde\theta$.

1. Given the Radon-Nikodým derivative $\frac{\diff\widetilde{\Pr}}{\diff\!\Pr}$, by Girsanov theorem, the dynamics of the equivalent Brownian motion under $\widetilde{\Pr}$ is \begin{equation}\label{eq:4.7.1}\diff\widetilde W_t=\lambda\sqrt{R_t}\diff t+\diff W_t\,.\end{equation}
1. Merging Eq.\ (\ref{eq:4.7.1}) and $\diff R_t=\kappa(\theta–R_t)\diff t+\delta\sqrt{R_t}\diff W_t$ yields \begin{equation}\label{eq:4.7.2}\diff R_t=(\kappa\theta-\kappa R_t-\delta\lambda R_t)\diff t+\delta\sqrt{R_t}\diff\widetilde W_t\,.\end{equation}
1. Merging Eq.\ (\ref{eq:4.7.2}) and $\diff R_t=\tilde\kappa\left(\tilde\theta–R_t\right)\diff t+\delta\sqrt{R_t}\diff\widetilde W_t$ yields $$\tilde\theta=\frac{\kappa\theta}{\kappa+\delta\lambda}\,,\quad\tilde\kappa=\kappa+\delta\lambda\,.$$
