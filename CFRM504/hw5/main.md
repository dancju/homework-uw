---
title: CFRM 504, 2020 Autumn, HW 5
...

# 5.1

Applying the product rule on $\diff X_t=\diff\frac{S_t}{M_t}$ yields

$$\diff X_t=\frac{M_t\diff S_t-S_t\diff M_t-\diff M_t\diff S_t}{M_t^2}\,.$$

Plugging $\diff S_t$ and $\diff M_t$ yields

$$\diff X_t=\frac{\left((\mu-r)\diff t+\sigma\diff W_t-\mu r(\diff t)^2-\sigma r\diff t\diff W_t\right)S_t}{M_t}\,.$$

Plugging $X_t=\frac{S_t}{M_t}$ yields

$$\diff X_t=\left((\mu-r)\diff t+\sigma\diff W_t-\mu r(\diff t)^2-\sigma r\diff t\diff W_t\right)X_t\,.$$

We can eliminate infinitesimals with higher orders than that of $\diff t$. Since $\diff W_t\in o(\diff t^{1/2})$, $(\diff t)^2\in o(\diff t^2)$, and $\diff t\diff W_t\in o(\diff t^{3/2})$, we have

$$\diff X_t\approx\left((\mu-r)\diff t+\sigma\diff W_t\right)X_t\,.$$

## 5.3

According to Itô's lemma, we have

$$\diff P_t=\beta\mu S_t^\beta\diff t+\frac{1}{2}\beta(\beta-1)\sigma^2S_t^\beta\diff t+\beta\sigma S_t^\beta\diff W_t\,.$$

Plugging $S_t^\beta=P_t$ yields

$$\diff P_t=\beta\mu P_t\diff t+\frac{1}{2}\beta(\beta-1)\sigma^2P_t\diff t+\beta\sigma P_t\diff W_t\,.$$

Since the process $P$ is a martingale,

$$\forall t:\beta\mu P_t+\frac{1}{2}\beta(\beta-1)\sigma^2P_t=0\,,$$

$$\beta=0\quad\text{or}\quad\beta=1-\frac{2\mu}{\sigma^2}\,.$$

# 5.5

According to Itô's lemma, we have

\begin{align*}
  \diff M_t &
  =\left(-\lambda\phi(X_t)+\mu(X_t)\phi'(X_t)+\frac{\sigma^2(X_t)\phi''(X_t)}{2}\right)e^{-\lambda t}\diff t \\&
  \quad+\sigma(X_t)\phi'(X_t)e^{-\lambda t}\diff W_t\,.
\end{align*}

Since the process $M$ is a martingale, we have

$$-\lambda\phi(X_t)+\mu(X_t)\phi'(X_t)+\frac{\sigma^2(X_t)\phi''(X_t)}{2}=0\,.$$

# 5.7

Apply $\log$ on two sides of $Z_t=\exp\left(-\frac12\int_0^t\Delta_s^2\diff s+\int_0^t\Delta_s\diff W_s\right)$ yields

$$\log Z_t=-\frac12\int_0^t\Delta_s^2\diff s+\int_0^t\Delta_s\diff W_s\,.$$

Applying derivation on two sides yields

$$\frac{\diff Z_t}{Z_t}=-\frac12\Delta_t^2\diff t+\Delta_t\diff W_t\,,$$

$$\diff Z_t=-\frac12\Delta_t^2Z_t\diff t+\Delta_tZ_t\diff W_t\,.$$

Let $f_t=Z_t^2$, according to Itô's lemma, we have

$$\diff Z_t^2=2\Delta_t Z_t^2\diff W_t\,,$$

$$\diff Z_t=\Delta_t Z_t\diff W_t\,.$$

That is, the process $Z$ is a martingale, which leads to $\E Z_t=Z_0$. Plugging $t=0$ to $Z_t=\exp\left(-\frac12\int_0^t\Delta_s^2\diff s+\int_0^t\Delta_s\diff W_s\right)$ yields $Z_0=1$. Therefore,

$$\E Z_t=1\,.$$
