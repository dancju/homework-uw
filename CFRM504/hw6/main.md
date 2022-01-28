---
title: CFRM 504, 2020 Autumn, HW 6
...

# 6.1

## 6.1.a

Given $\diff S_t=\mu S_t\diff t+\sigma S_t\diff W_t$, applying Itô's lemma on $\diff\ln S_t$ yields

$$\diff\ln S_t=\left(\mu-\frac{\sigma^2}2\right)\diff t+\sigma\diff W_t\,.$$

which indicates that the process $\ln S_t$ follows a generalised Wiener process with a drift $\mu-\frac{\sigma^2}2$ and a variance $\sigma^2$. Integrating from $t$ to $T$ yields

$$\ln S_T-\ln S_t=(T-t)\left(\mu-\frac{\sigma^2}2\right)+(W_T-W_t)\sigma\,,$$

or

$$S_T=S_t\exp\left((T-t)\left(\mu-\frac{\sigma^2}2\right)+(W_T-W_t)\sigma\right)\,.$$

Since $V_t/B_t$ is a martingale under risk-neutral measure $\widetilde{\Pr}$, we have $\frac{V_t}{B_t}=\widetilde{\E}\left(\frac{\phi(S_T)}{B_T}\middle|\mathcal F_t^S\right)$, or

$$V_t=e^{-(T-t)r}\widetilde{\E}\left(S_T^p\middle|\mathcal F_t^S\right)\,.$$

Plugging in $S_T$ yields

$$V_t=S_t^pe^{(T-t)\left(-r+\mu p-\frac{\sigma^2p}2\right)}\widetilde{\E}\left(e^{(W_T-W_t)\sigma p}\middle|\mathcal F_t^S\right)\,.$$

Applying Girsanov's theorem yields

$$V_t=S_t^pe^{(T-t)\left(-r+rp-\frac{\sigma^2p}2\right)}\widetilde{\E}\left(e^{\left(W_T-W_t\right)\sigma p}\middle|\mathcal F_t^S\right)\,.$$

Since $\frac{W_T-W_t}{\sqrt{T-t}}\sim\mathcal N(0,1)$, we can expand the expectation with the PDF of normal distribution such that

$$V_t=S_t^pe^{(T-t)\left(-r+rp-\frac{\sigma^2p}2\right)}\int_{\mathbb R}e^{x\sigma p\sqrt{T-t}}
\frac1{\sqrt{2\pi}}e^{-\frac{x^2}{2}}\diff x\,,$$

or

$$V_t=S_t^p\exp\frac{(p-1)(2r+\sigma^2p)(T-t)}2\,.$$

## 6.1.b

According to (6.1.6), we have $\Delta_t=\frac{\partial V_t}{\partial S_t}$. Plugging in $V_t$ yields

$$\Delta_t=pS_t^{p-1}\exp\frac{(p-1)(2r+\sigma^2p)(T-t)}2\,.$$

Since $X_0=V_0$, we have

$$X_0=S_0^p\exp\frac{(p-1)(2r+\sigma^2p)T}2\,.$$

## 6.1.c & 6.1.d

\includegraphics[width=\textwidth]{q1/c_d.pdf}

## 6.1.e

The paths of $V$ and $X$ are not exactly identical because that in every step in the Monte Carlo method, a tiny error was introduced for taking serial differences as differentials.

## 6.1.f

\includegraphics[width=\textwidth]{q1/f.pdf}

# 6.2

## 6.2.a

The dynamics of the portfolio $X$ is

$$\diff X_t=\Delta_t\diff S_t+\frac{X_t-\Delta_tS_t}{B_t}\diff B_t+q\Delta_tS_t\diff t\,,$$

or

$$\diff X_t=(\mu\Delta_tS_t-r\Delta_tS_t+q\Delta_tS_t+rX_t)\diff t+\sigma\Delta_tS_t\diff W_t\,.$$

## 6.2.b

Applying Itô's lemma on $\diff\frac1{B_t}$ yields

$$\diff\frac1{B_t}=-\frac{r}{B_t}\diff t\,.$$

Applying product rule on $\diff\frac{X_t}{B_t}$ yields

$$\diff\frac{X_t}{B_t}=\frac1{B_t}\diff X_t+X_t\diff\frac1{B_t}+\diff X_t\diff\frac1{B_t}\,.$$

Plugging in $\diff X_t$ and $\diff\frac1{B_t}$ yields

$$\diff\frac{X_t}{B_t}=\frac{(\mu-r+q)\Delta_tS_t}{B_t}\diff t+\frac{\sigma\Delta_tS_t}{B_t}\diff W_t\,.$$

Applying Itô's lemma on $V_t$ yields

$$\diff V_t=\left(\frac{\partial V_t}{\partial t}+\frac{\partial V_t}{\partial S_t}\mu S_t+\frac{\partial^2V_t}{\partial S_t^2}\frac{\sigma^2S_t^2}2\right)\diff t+\frac{\partial V_t}{\partial S_t}\sigma S_t\diff W_t\,.$$

Applying product rule on $\diff\frac{V_t}{B_t}$ yields

$$\diff\frac{V_t}{B_t}=\frac1{B_t}\diff V_t+V_t\diff\frac1{B_t}+\diff V_t\diff\frac1{B_t}\,.$$

Plugging in $\diff V_t$ and $\diff\frac1{B_t}$ yields

$$\diff\frac{V_t}{B_t}=\left(\frac{\partial V_t}{\partial t}+\frac{\partial V_t}{\partial S_t}\mu S_t+\frac{\partial^2V_t}{\partial S_t^2}\frac{\sigma^2S_t^2}2-rV_t\right)\frac1{B_t}\diff t+\frac{\partial V_t}{\partial S_t}\frac{\sigma S_t}{B_t}\diff W_t\,.$$

In order to replicate the option $V$ with the portfolio $X$, we have

$$\forall t:\diff\frac{X_t}{B_t}=\diff\frac{V_t}{B_t}\,,$$

i.e.\ the drift term and the variance term of $\diff\frac{X_t}{B_t}-\diff\frac{V_t}{B_t}$ are both zero, or

\begin{equation}
(\mu-r+q)\Delta_tS_t=\frac{\partial V_t}{\partial t}+\frac{\partial V_t}{\partial S_t}\mu S_t+\frac{\partial^2V_t}{\partial S_t^2}\frac{\sigma^2S_t^2}2-rV_t\,,
\end{equation}

and

\begin{equation}
\Delta_t=\frac{\partial V_t}{\partial S_t}\,.
\end{equation}

Plugging Equation (2) into Equation (1) yields

$$\frac{\partial V_t}{\partial t}+\frac{\partial V_t}{\partial S_t}rS_t+\frac{\partial^2V_t}{\partial S_t^2}\frac{\sigma^2S_t^2}2-rV_t-q\Delta_tS_t=0\,,$$

which gives the PDE for $V_t$. Besides, the terminal condition is

$$V_T=\phi(S_T)\,.$$

## 6.2.c

Since $X/B$ is a martingale under the measure $\widetilde{\Pr}$, the drift term of $\diff\frac{X_t}{B_t}$ under measure $\widetilde{\Pr}$ is zero, i.e.

$$\widetilde\mu=r-q\,.$$
