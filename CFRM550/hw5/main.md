---
title: CFRM 550, 2021 Autumn, HW 5
...

**Exercise 5.1.** Consider the Black-Scholes model described in Example 4.5.4. Assume for simplicity that the risk-free rate of interest is zero: $r=0$. Consider a power option, which pays $pS_T^q$ at time $T$. The value of this option at time $t\le T$ is given by $u(t,S_t)=\widetilde{\E}(pS_T^q|\mathcal F_t)$.

a) Find $u(t,S_t)$ by solving the SDE for $S_t$ and computing the expectation above directly.
a) Derive a PDE and BC for function $u(t,S_t)$. Show that the expression you obtained for $u$ in part (a) satisfies this PDE.

**Solution**

a)  1. According to Example 4.5.4, we have $$S_T=S_t\exp\left((T-t)\left(r-\frac{\sigma^2}2\right)+\left(\widetilde W_T-\widetilde W_t\right)\sigma\right)\,,$$ plugging which into $u(t,S_t)=\widetilde{\E}(pS_T^q|\mathcal F_t)$ yields \begin{equation}\label{eq:5.1.1}u(t,S_t)=pS_t^qe^{(T-t)\left(r-\frac{\sigma^2}2\right)q}\widetilde{\E}\left(e^{\left(\widetilde W_T-\widetilde W_t\right)\sigma q}\middle|\mathcal F_t\right)\,.\end{equation}
    1. Given $\widetilde W_T-\widetilde W_t\sim\mathcal N(0,T-t)$ under $\mathcal F_t$, we have \begin{equation}\label{eq:5.1.2}\widetilde{\E}\left(e^{\left(\widetilde W_T-\widetilde W_t\right)\sigma q}\middle|\mathcal F_t\right)=e^{\frac{(T-t)\sigma^2q^2}2}\end{equation}
    1. Plugging Eq.\ (\ref{eq:5.1.2}) and $r=0$ into Eq.\ (\ref{eq:5.1.1}) yields $$u(t,S_t)=pS_t^qe^{\frac{\left(q-1\right)(T-t)\sigma^2q}2}\,.$$
a)  1. According to Example 4.5.4, we have $$\diff S_t=rS_t\diff t+\sigma S_t\diff\widetilde W_t\,,$$ which by Kolmogorov backward equation gives a PDE $$\frac{\partial u(t,S_t)}{\partial t}+rS_t\frac{\partial u(t,S_t)}{\partial S_t}+\frac{\sigma^2S_t^2}{2}\frac{\partial^2u(t,S_t)}{\partial S_t^2}=0\,,$$ and a BC $$\forall s:\quad u(T,s)=ps^q\,.$$
    1. Partially derivativing the $u(t,S_t)$ from (a) and plugging into the PDE above yields a true statement. Therefore, the $u(t,S_t)$ from (a) satisfies this PDE.

**Exercise 5.2.** Consider the following SDE with linear coefficients \begin{equation}\label{eq:5.2.1}\diff X_t=[b(t)+\mu(t)X_t]\diff t+[a(t)+\sigma(t)X_t]\diff W_t\,,\quad X_0=x\,.\end{equation} Define two processes $(Z_t)_{t\ge0}$ and $(Y_t)_{t\ge0}$ by $$\diff Z_t=\mu(t)Z_t\diff t+\sigma(t)Z_t\diff W_t\,,\quad Z_0=1\,,$$ and $$\diff Y_t=\frac{b(t)–\sigma(t)a(t)}{Z_t}\diff t+\frac{a(t)}{Z_t}\diff W_t\,,\quad Y_0 = x\,.$$ Show that $X_t=Y_tZ_t$ solves Eq.\ (\ref{eq:5.2.1}).

**Proof**

1. Given $X_t=Y_tZ_t$, applying the product rule yields \begin{equation}\label{eq:5.2.2}\diff X_t=Y_t\diff Z_t+Z_t\diff Y_t+\diff Y_t\diff Z_t\,.\end{equation}
1. Plugging $\diff Y_t$ and $\diff Z_t$ into Eq.\ (\ref{eq:5.2.2}), substituting $Y_tZ_t$ with $X_t$ and applying rules $\diff W_t\diff W_t=\diff t$ and $\diff W_t\diff t=\diff t\diff t=0$ yields $$\diff X_t=[b(t)+\mu(t)X_t]\diff t+[a(t)+\sigma(t)X_t]\diff W_t\,.$$
1. Plugging $Z_0=1$ and $Y_0=x$ into $X_t=Y_tZ_t$ yields $$X_0=x\,.$$

**Exercise 5.3.** Let $W$ be a Brownian motion on a probability space $(\Omega,\mathcal F,\Pr)$ and let $(\mathcal F_t)_{0\le t\le T}$ be a filtration for $W$. Suppose $X$ be the solution of SDE $$\diff X_t=\kappa(\theta–X_t)\diff t+\delta\sqrt{X_t}\diff W_t\,.$$ Process $X$ is called a Cox-Ingersoll-Ross (CIR) process. Like the OU process, the CIR process is very often used in quantitative finance to model stochastic interest rates. Supposing that interest rates are given by $X$, the dynamics of a money market account are given by $$\diff M_t=X_tM_t\diff t\,.$$ Let $(B_t^T)_{0\le t\le T}$ be the price of a zero-coupon bond which pays one unit of currency at time  (i.e., $B_T^T=1$). If we interpret $\Pr$ as a the market's pricing measure with $M$ as numéraire, then using the fundamental theorem of asset pricing, the the value of a bond must satisfy \begin{small}$$\frac{B_t^T}{M_t}=\E\left(\frac{B_T^T}{M_T}\middle|\mathcal F_t\right)\implies B_t^T=M_t\E\left(\frac{B_T^T}{M_T}\middle|\mathcal F_t\right)=\E\left(\exp\left(-\int_t^TX_s\diff s\right)\middle|X_t\right)\,,$$\end{small} where we have used $B_T^T=1$ and $M_t=M_0\exp(\int_0^tX_s\diff s)$. Thus, given $X_t=x$, the price of a zero coupon bond is given by $$u(t,x)=\E\left(\exp\left(-\int_t^TX_s\diff s\right)\middle|X_t=x\right)\,.$$

a) Derive a PDE for function $u$.
a) Solve the PDE for $u$.

**Solution**

a) Given $u(t,x)=\E\left(\exp\left(-\int_t^TX_s\diff s\right)\middle|X_t=x\right)$ and $\diff X_t=\kappa(\theta–X_t)\diff t+\delta\sqrt{X_t}\diff W_t$, by Theorem 5.2.2, we have PDE $$\frac{\partial u(t,X_t)}{\partial t}+(\theta-X_t)\kappa\frac{\partial u(t,X_t)}{\partial X_t}+\frac{\delta^2X_t}2\frac{\partial^2u(t,X_t)}{\partial X_t^2}-X_tu(t,X_t)=0\,,$$ and BC $$\forall x:\quad u(T,x)=1\,.$$
a)  1. Let \begin{equation}\label{eq:5.3.1}u(t,x)=e^{-xa(t)-b(t)}\end{equation} where $a$ and $b$ are deterministic functions of $t$.
    1. Plugging Eq.\ (\ref{eq:5.3.1}) into the PDE yields $$\forall t,x:\quad\left(\frac{\delta^2a^2(t)}2+\kappa a(t)-a'(t)-1\right)x=\theta\kappa a(t)+b'(t)\,,$$ which gives $$\forall t:\quad\frac{\delta^2a^2(t)}2+\kappa a(t)-a'(t)-1=0\,,\quad\theta\kappa a(t)+b'(t)=0\,.$$
    1. Plugging Eq.\ (\ref{eq:5.3.1}) into the BC yields $$\forall x:\quad xa(T)+b(T)=0\,,$$ which gives $$a(T)=0\,,\quad b(T)=0\,.$$

**Exercise 5.4.**

**Solution**

a)  1. Given $\Pr$ is the market's pricing measure with the money market account as numéraire and the interest rates are zero, by the fundamental theorem of asset pricing, we have $$V_t=\E(S_T|\mathcal F_t)$$ which gives $$\varphi(x)=e^x$$
    1. Given $$\diff X_t=-\frac{Z_t}2\diff t+\sqrt{Z_t}\diff W_t$$ and $$\diff Z_t=\kappa(\theta-Z_t)\diff t+\sigma\sqrt{Z_t}\left(\rho\diff W_t+\sqrt{1-\rho^2}\diff B_t\right)$$ applying the two-dimensional Feynman–Kac formula yields
    $$\frac{\partial u}{\partial t}
    -\frac{Z_t}2\frac{\partial u}{\partial X_t}
    +\kappa(\theta-Z_t)\frac{\partial u}{\partial Z_t}
    +\frac{Z_t}2\frac{\partial^2u}{\partial X_t^2}
    +\rho\sigma Z_t\frac{\partial^2u}{\partial X_t\partial Z_t}
    +\frac{\sigma^2Z_t}2\frac{\partial^2u}{\partial Z_t^2}=0$$
    and the BC
    $$u(T,x,z)=\varphi(x,z)=e^x$$
a)  1. Define the Fourier transformation of $u$ by $$\hat u(t,\xi,z)=\int_{\mathbb R}\diff xe^{-i\xi x}u(t,x,z)$$
    1. Applying the Fourier transformation to the PDE yields $$-\frac{(i+\xi)\xi z}2\hat u+\frac{\partial\hat u}{\partial t}+[\kappa(\theta-z)+i\xi\rho\sigma z]\frac{\partial\hat u}{\partial z}+\frac{\sigma^2z}2\frac{\partial^2\hat u}{\partial z^2}=0$$
    1. Assume $\hat u$ is of the form $$\hat u(t,\xi,z)=\hat\varphi(\xi)e^{a(t,\xi)+zb(t,\xi)}$$
    1. Plugging the assumption to the PDE yields \begin{footnotesize}$$\forall z:\quad-\frac{(i+\xi)\xi z}2+\frac{\partial a(t,\xi)}{\partial t}+z\frac{\partial b(t,\xi)}{\partial t}+[\kappa(\theta-z)+i\xi\rho\sigma z]b(t,\xi)+\frac{\sigma^2z}2b^2(t,\xi)=0$$\end{footnotesize} which is equivalent to \begin{scriptsize}$$\forall z:\quad\left(\frac{\sigma^2}2b^2(t,\xi)+(i\xi\rho\sigma-\kappa) b(t,\xi)-\frac{i\xi+\xi^2}2+\frac{\partial b(t,\xi)}{\partial t}\right)z+\kappa\theta b(t,\xi)+\frac{\partial a(t,\xi)}{\partial t}=0$$\end{scriptsize} which gives two coupled OEDs \begin{footnotesize}$$\frac{\sigma^2}2b^2(t,\xi)+(i\xi\rho\sigma-\kappa) b(t,\xi)-\frac{i\xi+\xi^2}2+\frac{\partial b(t,\xi)}{\partial t}=0\,,\quad\kappa\theta b(t,\xi)+\frac{\partial a(t,\xi)}{\partial t}=0$$\end{footnotesize} where the BC are $$a(T,\xi)=b(T,\xi)=0$$
