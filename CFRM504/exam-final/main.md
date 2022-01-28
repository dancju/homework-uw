---
title: CFRM 504, 2020 Autumn, Final
header-includes:
    \usepackage{frcursive}
...

I have worked alone on this exam and did not discuss it with others.

Chao (Daniel) Zhou

\begin{cursive}\Large~chao zhou\end{cursive}

17\textsuperscript{th} December 2020

# 1

## 1.a

The constructed portfolio $X$ consists of $x$ bonds $B$, $y$ shares of stock $S$, and $z$ options $V$. We have

$$\begin{cases}
    g(uS_0)=xB_0e^{RT}+yuS_0+h(uS_0)z \\
    g(mS_0)=xB_0e^{RT}+ymS_0+h(mS_0)z \\
    g(dS_0)=xB_0e^{RT}+ydS_0+h(dS_0)z
\end{cases}$$

We would solve for $x$, $y$, and $z$ to identify the portfolio $X$.

## 1.b

According to the no-arbitrage assumption, we have $\frac{S_0}{B_0}=\E\left(\frac{S_T}{B_T}\right)$, or $$e^{RT}=pu+qm+rd\,.$$

According to the no-arbitrage assumption, we have $\frac{V_0}{B_0}=\E\left(\frac{V_T}{B_T}\right)$, or $$V_0e^{RT}=h(uS_0)p+h(mS_0)q+h(dS_0)r\,.$$

Plugging $h(S_T)=\alpha S_T$ and $e^{RT}=pu+qm+rd$ yields $$V_0=\alpha S_0\,.$$

## 1.c

Plugging $h(S_T)=\alpha S_T$ to the system of equations of \textbf{1.a} yields

$$\begin{cases}
    g(uS_0)=xB_0e^{RT}+yuS_0+z\alpha uS_0 \,,\\
    g(mS_0)=xB_0e^{RT}+ymS_0+z\alpha mS_0 \,,\\
    g(dS_0)=xB_0e^{RT}+ydS_0+z\alpha dS_0 \,,\\
\end{cases}$$

which is not a full-ranked system of linear equations, because one equation is a linear combination of the two others. Therefore, there does not exist an unique solution.

# 2

## 2.a

Plugging $\diff S_t$ and $\diff B_t$ into $\diff X_t=\Delta_t\diff S_t+\frac{X_t-\Delta_tS_t}{B_t}\diff B_t$ yields $$\diff X_t=(\mu\Delta_tS_t+rX_t-r\Delta_tS_t)\diff t+\sigma\Delta_tS_t\diff W_t\,.$$

Given $\diff B_t=rB_t\diff t$, we have $$\diff\frac1{B_t}=-\frac{r\diff t}{B_t}\,.$$

According to the product rule, we have $$\diff\frac{X_t}{B_t}=\frac1{B_t}\diff X_t+X_t\diff\frac1{B_t}+\diff X_t\diff\frac1{B_t}\,.$$

Plugging $\diff\frac1{B_t}$, $\diff X_t$, and eliminating infinitesimals with higher orders than that of $\diff t$ yields $$\diff\frac{X_t}{B_t}=\frac{\Delta_tS_t}{B_t}((\mu-r)\diff t+\sigma\diff W_t)\,.$$

Since $X/B$ is a martingale under measure $\widetilde{\Pr}$, the drift term above should be zero, i.e. $$\widetilde\mu=r\,.$$

According to Itô's lemma, the dynamics of $\ln S_t$ is $$\diff\ln S_t=\left(\mu-\frac{\sigma^2}2\right)\diff t+\sigma\diff W_t\,,$$ which under measure $\widetilde{\Pr}$ is $$\diff\ln S_t=\left(r-\frac{\sigma^2}2\right)\diff t+\sigma\diff\widetilde W_t\,,$$

## 2.b

Since $\widetilde{\Pr}$ is a risk-neutral measure, we have $\frac{u_t}{B_t}=\widetilde{\E}\left(\frac{u_T}{B_T}\middle|\mathcal F_t^S\right)$, or $$u_t=e^{-(T-t)r}\widetilde{\E}\left(\left(\ln S_T\right)^2\middle|\mathcal F_t^S\right)\,.$$

Since $\ln S_T\sim\mathcal N\left(\ln S_t+(T-t)\left(r-\frac{\sigma^2}2\right),(T-t)\sigma^2\right)$ under $\widetilde{\mathcal F}_t^S$, according to lemma 1, we have $$u_t=e^{-(T-t)r}\left(\left(\ln S_t+(T-t)\left(r-\frac{\sigma^2}2\right)\right)^2+(T-t)\sigma^2\right)\,.$$

**Lemma 1:** Given $X\sim\mathcal N\left(\mu,\sigma^2\right)$, we have $\E\left(X^2\right)=\mu^2+\sigma^2$.

**Proof**

$$\E\left(X^2\right)=\int_{\mathbb R}\frac{e^{-\frac12\left(\frac{x-\mu}{\sigma}\right)^2}}{\sigma\sqrt{2\pi}}x^2\diff x=\mu^2+\sigma^2\,.$$

## 2.c

Since portfolio $X$ replicates the contract $u$, we have $X_0=u_0$, or $$X_0=e^{-rT}\left(\left(\ln S_0+T\left(r-\frac{\sigma^2}2\right)\right)^2+T\sigma^2\right)\,.$$

According to formula (6.1.6), we have $$\Delta_t=\frac{\partial u_t}{\partial S_t}=\frac{2e^{-(T-t)r}}{S_t}\left(\ln S_t+(T-t)\left(r-\frac{\sigma^2}2\right)\right)\,.$$

# 3

## 3.a

Applying Itô's lemma to $\ln S_t$ yields $$\diff\ln S_t=\left(\mu-\frac{\sigma^2}2\right)\diff t+\sigma\diff W_t\,.$$

Integrating from $t$ to $T$ yields $$S_T=S_t\exp\left((T-t)\left(\mu-\frac{\sigma^2}2\right)+(W_T-W_t)\sigma\right)\,,$$

which under neutral risk measure $\widetilde{\Pr}$ is equivalent to $$S_T=S_t\exp\left(-(T-t)\frac{\sigma^2}2+\left(\widetilde W_T-\widetilde W_t\right)\sigma\right)\,,$$

Since $\widetilde{\Pr}$ is a risk-neutral measure, we have $\frac{V_t(p)}{B_t}=\widetilde{\E}\left(\frac{V_T(p)}{B_T}\middle|\mathcal F_t^S\right)$, or $$V_t=\widetilde{\E}\left(S_T^p\middle|\mathcal F_t^S\right)\,.$$

Plugging $S_T$ yields $$V_t(p)=S_t^pe^{-\frac{(T-t)\sigma^2p}2}\widetilde{\E}\left(e^{(W_T-W_t)\sigma p}\middle|\mathcal F_t^S\right)\,.$$

Since $W_T-W_t\sim\mathcal N(0,T-t)$ under $\widetilde{\mathcal F}_t^S$, we have $$V_t(p)=S_t^p\exp\frac{(T-t)\left(p-1\right)\sigma^2p}2\,.$$

## 3.b

$$\Delta_t(p)=\frac{\partial V_t(p)}{\partial S_t}=pS_t^{p-1}\frac{(T-t)\left(p-1\right)\sigma^2p}2\,.$$

## 3.c

The portfolio having zero value and being Delta-neutral is equivalent to

$$\begin{cases}
    V_t(p)+\alpha V_t(q)+\beta V_t(r)=0 \,,\\
    \Delta_t(p)+\alpha\Delta_t(q)+\beta\Delta_t(r)=0 \,,\\
\end{cases}$$

or

$$
    \begin{pmatrix}
        V_t(q) & V_t(r) \\
        \Delta_t(q) & \Delta_t(r) \\
    \end{pmatrix}
    \begin{pmatrix} \alpha \\ \beta \end{pmatrix}
    =
    \begin{pmatrix} -V_t(p) \\ -\Delta_t(p) \end{pmatrix}
    \,.
$$
