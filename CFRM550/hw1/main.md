---
title: CFRM 550, 2021 Autumn, HW 1
...

# 1.1

> Let $\mathcal F$ be a $\sigma$-algebra of $\Omega$. Suppose $B\in\mathcal F$. Show that $\mathcal G=\{A\cap B:A\in\mathcal F\}$ is a $\sigma$-algebra of $B$.

1. We will prove $\mathcal G$ contains the empty set.
    1. Since $\mathcal F$ is a $\sigma$-algebra, we have $\emptyset\in\mathcal F$.
    1. Given $\emptyset\in\mathcal F$ and $\mathcal G=\{A\cap B:A\in\mathcal F\}$, we have $\emptyset\in\mathcal G$.
1. Let $Y$ be a set in $\mathcal G$. We will prove $\mathcal G$ is closed under complements in $B$ by showing $B\setminus Y\in\mathcal G$.
    1. Given $Y\in\mathcal G$ and $\mathcal G=\{A\cap B:A\in\mathcal F\}$, there exists a set $X$ in $\mathcal F$ such that $X\cap B=Y$.
    1. Given $X\in\mathcal F$ and $\mathcal F$ is a $\sigma$-algebra on $\Omega$, we have $\Omega\setminus X\in\mathcal F$.
    1. Given $\Omega\setminus X\in\mathcal F$ and $\mathcal G=\{A\cap B:A\in\mathcal F\}$, we have $(\Omega\setminus X)\cap B\in\mathcal G$, or $(\Omega\cap B)\setminus X\in\mathcal G$.
    1. Given $(\Omega\cap B)\setminus X\in\mathcal G$ and $B\subset\Omega$, we have $B\setminus X\in\mathcal G$, or $B\setminus(B\cap X)\in\mathcal G$, or $B\setminus Y\in\mathcal G$.
1. Let $Y_1,\dots,Y_n$ be $n$ sets in in $\mathcal G$. We will prove $\mathcal G$ is closed under countable unions by showing $\bigcup_{i=1}^nY_i\in\mathcal G$.
    1. Given $Y_1,\dots,Y_n\in\mathcal G$ and $\mathcal G=\{A\cap B:A\in\mathcal F\}$, there exist $X_1,\dots,X_n$ in $\mathcal F$ such that $\forall i:X_i\cap B=Y_i$.
    1. Given $X_1,\dots,X_n\in\mathcal F$ and $\mathcal F$ is a $\sigma$-algebra on $\Omega$, we have $\bigcup_{i=1}^n X_i\in\mathcal F$.
    1. Given $\bigcup_{i=1}^n X_i\in\mathcal F$ and $\mathcal G=\{A\cap B:A\in\mathcal F\}$, we have $\left(\bigcup_{i=1}^n X_i\right)\cap B\in\mathcal G$, or $\bigcup_{i=1}^n(X_i\cap B)\in\mathcal G$, or $\bigcup_{i=1}^nY_i\in\mathcal G$.
1. Given $\mathcal G$ contains $\emptyset$, is closed under complements, and is closed under countable unions, $\mathcal G$ is a $\sigma$-algebra of $B$.

# 1.2

> Let $\mathcal F$ and $\mathcal G$ be $\sigma$-algebras of $\Omega$.
>
> a. Show that $\mathcal F\cap\mathcal G$ is a $\sigma$-algebra of $\Omega$.
> a. Show that $\mathcal F\cup\mathcal G$ is not necessarily a $\sigma$-algebra of $\Omega$.

a.  1. We will prove $\mathcal F\cap\mathcal G$ contains the empty set.
        1. Given $\mathcal F$ and $\mathcal G$ are both $\sigma$-algebras, we have $\emptyset\in\mathcal F$ and $\emptyset\in\mathcal G$, which implies $\emptyset\in\mathcal F\cap\mathcal G$.
    1. Let $X$ be a set in $\mathcal F\cap\mathcal G$. We will prove $\mathcal F\cap\mathcal G$ is closed under complements by showing $\Omega\setminus X\in\mathcal F\cap\mathcal G$.
        1. Given $X\in\mathcal F\cap\mathcal G$, we have both $X\in\mathcal F$ and $X\in\mathcal G$.
        1. Given $\mathcal F$ is a $\sigma$-algebra on $\Omega$ and $X\in\mathcal F$, we have $\Omega\setminus X\in\mathcal F$. Similarily, we have $\Omega\setminus X\in\mathcal G$.
        1. Given $\Omega\setminus X\in\mathcal F$ and $\Omega\setminus X\in\mathcal G$, we have $\Omega\setminus X\in\mathcal F\cap\mathcal G$.
    1. Let $X_1,\dots,X_n$ be $n$ sets in in $\mathcal F\cap\mathcal G$. We will prove $\mathcal F\cap\mathcal G$ is closed under countable unions by showing $\bigcup_{i=1}^nX_i\in\mathcal F\cap\mathcal G$.
        1. Given $X_1,\dots,X_n\in\mathcal F\cap\mathcal G$, we have both $X_1,\dots,X_n\in\mathcal F$ and $X_1,\dots,X_n\in\mathcal G$.
        1. Given $\mathcal F$ is a $\sigma$-algebra and $X_1,\dots,X_n\in\mathcal F$, we have $\bigcup_{i=1}^n X_i\in\mathcal F$. Similarily, we have $\bigcup_{i=1}^n X_i\in\mathcal G$.
        1. Given $\bigcup_{i=1}^n X_i\in\mathcal F$ and $\bigcup_{i=1}^n X_i\in\mathcal G$, we have $\bigcup_{i=1}^nX_i\in\mathcal F\cap\mathcal G$.
    1. Given $\mathcal F\cap\mathcal G$ contains $\emptyset$, is closed under complements, and is closed under countable unions, $\mathcal F\cap\mathcal G$ is a $\sigma$-algebra of $\Omega$.
a. Let $\mathcal F=\{\emptyset,\Omega,F,F^c\}$ and $\mathcal G=\{\emptyset,\Omega,G,G^c\}$, where $F$ and $G$ are two non-empty disjoint events such that $F\cap G=\emptyset$. We have $\mathcal F\cup\mathcal G=\{\emptyset,\Omega,F,F^c,G,G^c\}$, which is not a $\sigma$-algebra since it does not contain $F\cup G$. Therefore, $\mathcal F\cup\mathcal G$ is not necessarily a $\sigma$-algebra.

# 1.4

> Suppose $X$ is a continuous random variable with CDF $F_X$, $g$ is a strictly increasing continuous function, and $Y=g(X)$.
>
> a. What is $F_Y$, the CDF of $Y$?
> a. What is $f_Y$, the PDF of $Y$?

1. Given $g$ is a strictly increasing continuous function, we have $F_Y(y)=\Pr(Y<y)=\Pr(g(X)<y)=\Pr\left(X<g^{-1}(y)\right)=F_X\left(g^{-1}(y)\right)$.
1. $f_Y(y)=\frac{\diff F_Y(y)}{\diff y}=\frac{\diff F_X\left(g^{-1}(y)\right)}{\diff y}=f_X\left(g^{-1}(y)\right)\frac{\diff g^{-1}(y)}{\diff y}$.

# 1.6

> Suppose $X$ is a continuous random variable defined on a probability space $(\Omega,\mathcal F,\Pr)$. Let $f$ be the PDF of $X$ under $\Pr$ and assume $f>0$. Let $g$ be the PDF of a random variable. Define $Z=g(X)/f(X)$.
>
> a. Show that $Z=\frac{\diff\widetilde{\Pr}}{\diff\!\Pr}$ defines a Radon-Nikodým derivative.
> a. What is the PDF of $X$ under $\widetilde{\Pr}$?

a. We will prove $Z$ is a Radon-Nikodým derivative by showing $Z\ge0$ and $\E(Z)=1$.
    1. Given $g$ is a PDF, we have $g\ge0$. Given $g\ge0$ and $f>0$, we have $Z=\frac{g(X)}{f(X)}\ge0$.
    1. $\E(Z)=\int_\Omega Zf(x)\diff x=\int_\Omega g(x)\diff x=1$.
a.  Given $Z=\frac{g(X)}{f(X)}$ and $Z=\frac{\diff\widetilde{\Pr}}{\diff\!\Pr}$, we have $\widetilde{\Pr}(\diff\omega)=\frac{\diff\widetilde{\Pr}}{\diff\!\Pr}(\omega)\Pr(\diff\omega)=\frac{g}{f}(\omega)\Pr(\diff\omega)$. Plugging in $\Pr(\diff\omega)=f(\omega)\diff\omega$ yields $\widetilde{\Pr}(\diff\omega)=g(\omega)\diff\omega$, implying that the PDF of $X$ under $\widetilde{\Pr}$ is $g$.

# 1.7

> Let $X$ be uniformly distributed on $[0,1]$. For what function $g$ is the random variable $g(X)$ exponentially distributed with parameter 1, i.e.\ $g(X)\sim\operatorname{Exp}(1)$?

1. Given $X\sim U(0,1)$, we have $$F_X(x)=\begin{cases}0&x\in(-\infty,0)\,,\\x&x\in[0,1)\,,\\1&x\in[1,+\infty)\,.\end{cases}$$
1. Given $g(X)\sim\operatorname{Exp}(1)$, we have $$F_{g(X)}(y)=\begin{cases}0&y\in(-\infty,0)\,,\\1-e^{-y}&y\in[0,+\infty)\,.\end{cases}$$
1. Assuming $g(x)$ is strictly increasing, we have $F_X(x)=\Pr(X<x)=\Pr(g(X)<g(x))=F_{g(X)}(g(x))$.
1. Plugging $F_X$ and $F_{g(X)}$ into $F_X(x)=F_{g(X)}(g(x))$, we get $$g(x)=-\ln(1-x)\,.$$
