---
title: CFRM 550, 2021 Autumn, HW 6
...

**Exercise 6.1.**

**Solution**

1. The cost function for the infinite-time stochastic control problem is $$J_u(x)=\E\left(\int_t^\infty e^{-\lambda(s-t)}F(X_u(s),u(s))\diff s\middle|X_u(t)=x\right)\,.$$ The corresponding value function is $$V(x)=\sup_{u\in\mathcal U}J_u(x)\,.$$ Plugging the cost function into the value function and split the conditional expectation into two intervals $[t,t+\delta]$ and $[t+\delta,\infty)$ gives \begin{footnotesize}\begin{equation}\label{eq:6.1.1}V(x)\ge\E\left(\int_t^{t+\delta} e^{-\lambda(s-t)}F(X_u(s),u(s))\diff s+e^{-\lambda\delta}V(X_u(x+\delta))\middle|X_u(t)=x\right)\,.\end{equation}\end{footnotesize}
1. By the fundamental theorem of calculus, we have $$V(X_u(t+\delta))=V(X_u(t))+\int_{s=t}^{t+\delta}\diff V(X_u(s))\,.$$ Applying Itô's lemma to $\diff V(X_u(s))$ and plugging in gives $$V(X_u(t+\delta))=V(X_u(t))+\int_t^{t+\delta}\mathcal A_u(s)V(X_u(s))\diff s+M(t)\,,$$ where $\mathcal A_u(s)$ is the infinitesimal generator of $X_u(s)$ and $M(t)$ is a martingale term. Taking an expectation with condition $X_u(t)=x$ and canceling an Itô integral gives \begin{footnotesize}\begin{equation}\label{eq:6.1.2}\E(V(X_u(t+\delta))|X_u(t)=x)=V(x)+\E\left(\int_t^{t+\delta}\mathcal A_u(s)V(X_u(s))\diff s\middle|X_u(t)=x\right)\,.\end{equation}\end{footnotesize}
1. Merging Eq.\ (\ref{eq:6.1.1}) and Eq.\ (\ref{eq:6.1.2}) gives \begin{scriptsize}$$\left(1-e^{-\lambda\delta}\right)V(x)\ge\E\left(\int_t^{t+\delta}\left(e^{-\lambda(s-t)}F(X_u(s),u(s))+e^{-\lambda\delta}\mathcal A_u(s)V(X_u(s))\right)\diff s\middle|X_u(t)=x\right)\,.$$\end{scriptsize} Dividing by $\delta$ and taking a limit as $\delta\to0$ gives $$\lambda V(x)\ge F(x,u(t))+\mathcal A_u(t)V(x)\,.$$ We obtain an equality if $u$ is optimal such that $$\lambda V(x)=\sup_{u\in\mathcal U}[F(x,u(t))+\mathcal A_u(t)V(x)]\,.$$

**Exercise 6.2.**

**Solution**

1. Given the cost function being $$J_u(t,x)=\frac1{1-\gamma}\E\left(X_u^{1-\gamma}(T)\middle|X_u(t)=x\right)\,,$$ and the value function being $$V(t,x)=\sup_{u\in\mathcal U}J_u(t,x)\,,$$ we have \begin{equation}\label{eq:6.2.1}V(t,x)\ge\E\left(V(t+\delta,X_u(t+\delta))\middle|X_u(t)=x\right)\,.\end{equation}
1. From Assumption 6.2.1, we get \begin{scriptsize}\begin{equation}\label{eq:6.2.2}\E(V(t+\delta,X_u(t+\delta))|X_u(t)=x)=V(t,x)+\E\left(\int_t^{t+\delta}(\partial_s+\mathcal A_u(s))V(s,X_u(s))\diff s\middle|X_u(t)=x\right)\,,\end{equation}\end{scriptsize} where $\mathcal A_u(s)$ is the infinitesimal generator of $X_u(s)$.
1. Merging Eq.\ (\ref{eq:6.2.1}) and Eq.\ (\ref{eq:6.2.2}) gives $$0\ge\E\left(\int_t^{t+\delta}(\partial_s+\mathcal A_u(s))V(s,X_u(s))\diff s\middle|X_u(t)=x\right)\,.$$ Dividing by $\delta$ and taking a limit as $\delta\to0$ gives $$0\ge(\partial_t+\mathcal A_u(t))V(t,x)\,.$$ We obtain an equality if $u$ is optimal such that \begin{equation}\label{eq:6.2.3}0=\partial_tV(t,x)+\sup_{u\in\mathcal U}\mathcal A_u(t)V(t,x)\,.\end{equation}
1. Given $\diff X_{u}(t)=\mu u(t)\diff t+\sigma u(t)\diff W_t$, we have $$\mathcal A_u=\mu u(t)\partial_x+\frac{\sigma^2u^2(t)}2\partial_x^2\,.$$ Plugging into Eq.\ (\ref{eq:6.2.3}) and finding the first-order condition w.r.t.\ $u$ yields $$u_*=-\frac{\mu\partial_xV(t,x)}{\sigma^2\partial_x^2V(t,x)}\,.$$ Plugging back into Eq.\ (\ref{eq:6.2.3}) yields \begin{equation}\label{eq:6.2.4}0=\partial_tV-\frac{\mu^2}{2\sigma^2}\frac{(\partial_xV)^2}{\partial_t^2V}\,.\end{equation}
1. Setting $t$ as $T$ in the value function yields \begin{equation}\label{eq:6.2.5}V(T,x)=\frac{x^{1-\gamma}}{1-\gamma}\,.\end{equation}
1. Now, we try to solve PDE (\ref{eq:6.2.4}) with BC (\ref{eq:6.2.5}). We guess that \begin{equation}\label{eq:6.2.6}V(t,x)=\frac{f(t)x^{1-\gamma}}{1-\gamma}\,.\end{equation} Plugging Eq.\ (\ref{eq:6.2.6}) into the PDE (\ref{eq:6.2.4}) and BC (\ref{eq:6.2.5}) yields $$f'(t)+\frac{\mu^2(1-\gamma)}{2\sigma^2\gamma}f(t)=0\,,\quad f(T)=1\,,$$ which gives $$f(t)=e^\frac{\mu^2(1-\gamma)(T-t)}{2\sigma^2\gamma}\,.$$ Plugging back into Eq.\ (\ref{eq:6.2.6}) yields $$V(t,x)=\frac{x^{1-\gamma}}{1-\gamma}e^\frac{\mu^2(1-\gamma)(T-t)}{2\sigma^2\gamma}\,.$$
