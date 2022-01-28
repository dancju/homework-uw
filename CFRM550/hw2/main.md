---
title: CFRM 550, 2021 Autumn, HW 2
...

# 2.1

> Let $\Omega=\{a,b,c,d\}$ and $\mathcal F=2^\Omega$. We define a probability measure $\Pr$ as follows $$\Pr(a)=1/6,\quad\Pr(b)=1/3,\quad\Pr(c)=1/4,\quad\Pr(d)=1/4,$$ Next, define three random variables $$X(a)=1,X(b)=1,X(c)=–1,X(d)=–1,$$ $$Y(a)=1,Y(b)=–1,Y(c)=1,Y(d)=–1,$$ and $Z=X+Y$.
>
> a. List the sets in $\sigma(X)$.
> a. What are the values of $\E[Y|X]$ for $\{a,b,c,d\}$?
> a. Verify the partial averaging property: $\E[\mathbf1_A\E[Y|X]]=\E[\mathbf1_AY]$ for all $A\in\sigma(X)$.
> a. What are the values of $\E[Z|X]$ for $\{a,b,c,d\}$?
> a. Verify the partial averaging property.

a. $\sigma(X)=\{\{\omega:X(\omega)\in A\}:A\in\mathcal B(\mathbb R)\}=\{\emptyset,\{a,b\},\{c,d\},\Omega\}$.
a.  - $\E(Y|X=X(a))=\E(Y|X=X(b))=\E(Y|X=1)=\frac{\Pr(a)Y(a)+\Pr(b)Y(b)}{\Pr(a)+\Pr(b)}=-1/3$.
    - $\E(Y|X=X(c))=\E(Y|X=X(d))=\E(Y|X=-1)=\frac{\Pr(c)Y(c)+\Pr(d)Y(d)}{\Pr(c)+\Pr(d)}=0$.
a. We will verify $\E[\mathbf1_A\E[Y|X]]=\E[\mathbf1_AY]$ for all $A\in\sigma(X)$.
    - In case $A=\emptyset$,
        - $\E[\mathbf1_A\E[Y|X]]=0$,
        - $\E[\mathbf1_AY]=0$.
    - In case $A=\{a,b\}$,
        - $\E[\mathbf1_A\E[Y|X]]=\Pr(a)\E(Y|X=X(a))+\Pr(b)\E(Y|X=X(b))=-1/6$,
        - $\E[\mathbf1_AY]=\Pr(a)Y(a)+\Pr(b)Y(b)=-1/6$.
    - In case $A=\{c,d\}$,
        - $\E[\mathbf1_A\E[Y|X]]=\Pr(c)\E(Y|X=X(c))+\Pr(d)\E(Y|X=X(d))=0$,
        - $\E[\mathbf1_AY]=\Pr(c)Y(c)+\Pr(d)Y(d)=0$.
    - In case $A=\Omega$,
        - $\E[\mathbf1_A\E[Y|X]]=\Pr(a)\E(Y|X=X(a))+\Pr(b)\E(Y|X=X(b))+\Pr(c)\E(Y|X=X(c))+\Pr(d)\E(Y|X=X(d))=-1/6$,
        - $\E[\mathbf1_AY]=\Pr(a)Y(a)+\Pr(b)Y(b)+\Pr(c)Y(c)+\Pr(d)Y(d)=-1/6$.
a.  - $\E(Z|X=X(a))=\E(Z|X=X(b))=\E(Z|X=1)=\frac{\Pr(a)Z(a)+\Pr(b)Z(b)}{\Pr(a)+\Pr(b)}=2/3$.
    - $\E(Z|X=X(c))=\E(Z|X=X(d))=\E(Z|X=-1)=\frac{\Pr(c)Z(c)+\Pr(d)Z(d)}{\Pr(c)+\Pr(d)}=-1$.
a. We will verify $\E[\mathbf1_A\E[Z|X]]=\E[\mathbf1_AZ]$ for all $A\in\sigma(X)$.
    - In case $A=\emptyset$,
        - $\E[\mathbf1_A\E[Z|X]]=0$,
        - $\E[\mathbf1_AY]=0$.
    - In case $A=\{a,b\}$,
        - $\E[\mathbf1_A\E[Z|X]]=\Pr(a)\E(Z|X=X(a))+\Pr(b)\E(Z|X=X(b))=1/3$,
        - $\E[\mathbf1_AY]=\Pr(a)Z(a)+\Pr(b)Z(b)=1/3$.
    - In case $A=\{c,d\}$,
        - $\E[\mathbf1_A\E[Z|X]]=\Pr(c)\E(Z|X=X(c))+\Pr(d)\E(Z|X=X(d))=-1/2$,
        - $\E[\mathbf1_AY]=\Pr(c)Z(c)+\Pr(d)Z(d)=-1/2$.
    - In case $A=\Omega$,
        - $\E[\mathbf1_A\E[Z|X]]=\Pr(a)\E(Z|X=X(a))+\Pr(b)\E(Z|X=X(b))+\Pr(c)\E(Z|X=X(c))+\Pr(d)\E(Z|X=X(d))=-1/6$,
        - $\E[\mathbf1_AY]=\Pr(a)Z(a)+\Pr(b)Z(b)+\Pr(c)Z(c)+\Pr(d)Z(d)=-1/6$.

# 2.2

> Fix a probability space $(\Omega,\mathcal F,\Pr)$. Let $Y$ be a square integrable random variable such that $\E\left(Y^2\right)<\infty$ and let $\mathcal G$ be a sub-$\sigma$-algebra of $\mathcal F$. Show that $$\forall X\in\mathcal G:\Var(Y-\E(Y|\mathcal G))\le\Var(Y-X)\,.$$

1. Applying the definition of variance to $\Var(Y-X)$ yields $$\Var(Y-X)=\E\left([Y-X+\E(Y-X)]^2\right)\,.$$
1. Adding and subtracting $\E(Y|\mathcal G)$ yields $$\Var(Y-X)=\E\left([Y-\E(Y|\mathcal G)+\E(Y|\mathcal G)-X+\E(Y-X)]^2\right)\,,$$ or \begin{align*}&\Var(Y-X)\\=&\E\left([Y-\E(Y|\mathcal G)]^2\right)\\&+\E\left([\E(Y|\mathcal G)-X+\E(Y-X)]^2\right)\\&+2\E\{[Y-\E(Y|\mathcal G)][\E(Y|\mathcal G)-X+\E(Y-X)]\}\,.\end{align*}
1. Letting $A$ be $\E(Y|\mathcal G)-X+\E(Y-X)$, we have \begin{equation}\label{eq:2.2.0}\Var(Y-X)=\E\left([Y-\E(Y|\mathcal G)]^2\right)+\E\left(A^2\right)+2\E\{[Y-\E(Y|\mathcal G)]A\}\,.\end{equation}
1. Given $\mathcal G\subseteq\mathcal F$, by the tower property, we have $\E(Y-\E(Y|\mathcal G))=0$, which yields \begin{equation}\label{eq:2.2.1}\Var[Y-\E(Y|\mathcal G)]=\E\left([Y-\E(Y|\mathcal G)]^2\right)\,.\end{equation}
1. Plugging Eq.\ (\ref{eq:2.2.1}) into Eq.\ (\ref{eq:2.2.0}) yields $$\Var(Y-X)=\Var[Y-\E(Y|\mathcal G)]+\E\left(A^2\right)+2\E\{[Y-\E(Y|\mathcal G)]A\}\,.$$ Cancelling $\E\{[Y-\E(Y|\mathcal G)]A\}$ yields $$\Var(Y-X)=\Var[Y-\E(Y|\mathcal G)]+\E\left(A^2\right)\,.$$
1. Since $\E\left(A^2\right)\ge0$, we have $\Var(Y-\E(Y|\mathcal G))\le\Var(Y-X)\,.$

# 2.3

> Give an example of a probability space $(\Omega,\mathcal F,\Pr)$, a random variable $X$ and a function $f$ such that $\sigma(f(X))$ is strictly smaller than $\sigma(X)$ but $\sigma(f(X))\ne\{\emptyset,\Omega\}$. Give a function $g$ such that $\sigma(g(X))=\{\emptyset,\Omega\}$.

1. Define $\Omega=\{a,b,c\}$, $\mathcal F=2^\Omega$, and $\Pr(a),\Pr(b),\Pr(c)>0$.
1. Defining $X(a)=-1,X(b)=0,X(c)=1$, We have $\sigma(X)=2^\Omega$.
1. Defining $f(x)=x^2$, we have $\sigma(f(X))=\{\emptyset,\{a,c\},\{b\},\Omega\}$.
1. Defining $g(x)=0$, we have $\sigma(g(X))=\{\emptyset,\Omega\}$.

# 2.4

> On probability space $(\Omega,\mathcal F,\Pr)$, define random variables $X$ and $Y_0,Y_1,Y_2,\dots$. Suppose $\E|X|<\infty$. Define $\mathcal F_n=\sigma(Y_0,Y_1,\dots,Y_n)$ and $X_n=\E[X|\mathcal F_n]$. Show that sequence $X_0,X_1,X_2,\dots$ is a martingale under $\Pr$ w.r.t.\ filtration $(\mathcal F_n)_{n\ge0}$.

Given $(\mathcal F_n)_n$ is a filtration, we have $\mathcal F_s\subseteq\mathcal F_t$ for all $0\le s\le t$, which implies $$\forall 0\le s\le t:\quad\E(X_t|\mathcal F_s)=\E(\E(X|\mathcal F_t)|\mathcal F_s)=\E(X|\mathcal F_s)=X_s\,,$$ e.g., sequence $X_0,X_1,X_2,\dots$ is a martingale under $\Pr$ w.r.t.\ filtration $(\mathcal F_n)_{n\ge0}$.

# 2.5

> Let $X_0,X_1,\dots$ be a sequence of i.i.d.\ Bernoulli random variable with parameter $p$, i.e., $\Pr(X_i=1)=p$. Define $S_n=\sum_{i=1}^nX_i$ where $S_0=0$. Let $(Z_n)_{n\ge0}$ be given by $Z_n=r^{2S_n-n}$ where $r>0$.
>
> a. Let $F=(\mathcal F_n)_{n\ge0}$ where $\mathcal F_n=\sigma(X_0,X_1,\dots,X_n)$. For what values of $r$ is $Z$ a $(\Pr,F)$ martingale, submartingale, and supermartingale?
> a. Let $G=(\mathcal G_n)_{n\ge0}$ where $\mathcal G_n=\sigma(S_0,S_1,\dots,S_n)$. Suppose $r$ is such that $Z$ is a $(\Pr,F)$ martingale. Is $Z$ also a $(\Pr,G)$ martingale?
> a. Suppose that $\widetilde{\Pr}(X_i=1)=\widetilde p\ne p$. Suppose $r$ is such that $Z$ is a $(\Pr,F)$ martingale. Is $Z$ also a $(\widetilde{\Pr},F)$ martingale?

a. Given $Z_n=r^{2S_n-n}$, we have $Z_{n+1}=Z_nr^{2(S_{n+1}-S_n)-1}$. Plugging in $S_n=\sum_{i=1}^nX_i$ yields $Z_{n+1}=Z_nr^{2X_{n+1}-1}$, which gives $\E(Z_{n+1}|\mathcal F_n)=Z_n\E\left(r^{2X_{n+1}-1}\middle|\mathcal F_n\right)$. Given $X_{n+1}$ is a Bernoulli random variable with parameter $p$, we have $\E(Z_{n+1}|\mathcal F_n)=Z_n\left(pr+(1-p)r^{-1}\right)$.
    - If $Z$ is a $(\Pr,F)$ martingale, we have $\E(Z_{n+1}|\mathcal F_n)=Z_n$, e.g., $pr+\frac{1-p}r=1$. Given $0<p<1$, we have $$r=1\quad\text{or}\quad r=\frac1p-1\,.$$
    - If $Z$ is a $(\Pr,F)$ sub-martingale, we have $\E(Z_{n+1}|\mathcal F_n)\ge Z_n$, e.g., $pr+\frac{1-p}r\ge1$. Given $0<p<1$ and $r>0$, we have $$r\in\begin{cases}(0,1]\cup\left[\frac1p-1,+\infty\right)&p\in(0,1/2)\,,\\\left(0,\frac1p-1\right]\cup[1,+\infty)&p\in[1/2,1)\,.\end{cases}$$
    - If $Z$ is a $(\Pr,F)$ super-martingale, we have $\E(Z_{n+1}|\mathcal F_n)\le Z_n$, e.g., $pr+\frac{1-p}r\le1$. Given $0<p<1$ and $r>0$, we have $$r\in\begin{cases}\left[1,\frac1p-1\right]&p\in(0,1/2)\,,\\\left[\frac1p-1,1\right]&p\in[1/2,1)\,.\end{cases}$$
a. Given $S_n=\sum_{i=1}^nX_i$, when we have sequence $X_0,\dots,X_n$, we can get sequence $S_0,\dots,S_n$, and vice versa. Therefore, $X_0,\dots,X_n$ and $S_0,\dots,S_n$ provide the exact same information, implying $\mathcal F_n=\mathcal G_n$. Therefore, $Z$ is also a $(\Pr,G)$ martingale.
a. If $r=1$, then $Z$ is also a $(\widetilde{\Pr},F)$ martingale, no matter what $\widetilde p$ is. If $r\ne1$ and $r=\frac1p-1$, then $Z$ is not a $(\widetilde{\Pr},F)$ martingale.
