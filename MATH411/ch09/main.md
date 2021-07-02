---
title: MATH 412, 2021 Summer, Chapter 9
...

# 9.4

> **Theorem 9.2.** A polynomial $f(x)$ of positive degree $n$ in $K[x]$ either is irreducible in $K[x]$ or factors as a product of irreducible polynomials in $K[x]$.

1. Since linear polynomials are irreducible, Theorem 9.2 holds for $n=1$.
1. Assume Theorem 9.2 hold for every polynomial of positive degree $k$. Let $f(x)$ be a polynomial in $K[x]$ of degree $k+1$. By the definition of reducibility, $f(x)$ either is irreducible or has a nontrivial factorization, say $f(x)=g(x)h(x)$ with non-constant polynomial $g(x)$ and $h(x)$ of degree less than $k+1$. By assumption, $g(x)$ and $h(x)$ either is irreducible or factors as a product of irreducible polynomials. Thus, $f(x)$ either is irreducible or factors as a product of irreducible polynomials.
1. By the principle of induction, the theorem is proved.

# 9.5

> **Theorem 9.3.** Let $K$ be a field and $n$ be a positive integer. Suppose $f(x)$ is a polynomial in $K[x]$ of degree $n$. Polynomial $f(x)$ is either irreducible or has a divisor of degree less than or equal to $n/2$.

1. Assume $f(x)$ is reducible such that $f(x)=g(x)h(x)$.
    1. By Theorem 9.1, $n=\deg g(x)+\deg h(x)$.
    1. Given $n=\deg g(x)+\deg h(x)$, $\deg g(x)>0$, $\deg h(x)>0$, we get either $\deg g(x)\le\frac n2$ or $\deg h(x)\le\frac n2$.
1. Therefore, polynomial $f(x)$ is either irreducible or has a divisor of degree less than or equal to $n/2$.

# 9.6

> **Theorem 9.4.** The ring of polynomials $K[x]$ with coefficients in a field $K$ contains infinitely many irreducible monic polynomials.

1. Ring $K[x]$ contains at least one irreducible monic polynomial, with $x$ being an example.
1. Assume ring $K[x]$ has and only has $k$ irreducible monic polynomial $p_1(x),\dots,p_k(x)$.
    1. None of $p_1(x),\dots,p_k(x)$ divides polynomial $\left(p_1(x)\cdots p_k(x)\right)+1$, otherwise some $p_i(x)$ would divide 1.
    1. By Theorem 9.2, polynomial $\left(p_1(x)\cdots p_k(x)\right)+1$ either is irreducible or factors as a product of irreducible polynomials in $K[x]$.
    1. Therefore, there is a monic irreducible polynomial in $K[x]$ distinct from $p_1(x),\dots,p_k(x)$.
1. Therefore, set $\{p_1(x),\dots,p_k(x)\}$ can not be the entire collection of irreducible monic polynomials in $K[x]$, contradicting the assumption. Therefore, there are infinitely many irreducible monic polynomials in $K[x]$.

# 9.7

$x^4-1=(x^3-2x^2+x-2)(x+2)+(3x^3+3)$. The quotient is $x+2$ and the remainder is $3x^3+3$.

# 9.8

> **Theorem 9.5.** Let $K$ be a field, and $a(x)$ and $b(x)$ be nonzero polynomials in $K[x]$. There exist unique polynomials $q(x)$ and $r(x)$, with $\deg r(x)<\deg a(x)$ and $b(x)=a(x)q(x)+r(x)$.

1. Assume $\deg b(x)<\deg a(x)$. We have $b(x)=0a(x)+b(x)$, satisfying the desired form.
1. Assume $\deg b(x)=\deg a(x)$.
    1. Let $b(x)=\beta_nx^n+\cdots+\beta_1x+\beta_0$ and $a(x)=\alpha_nx^n+\cdots+\alpha_1x+\alpha_0$.
    1. Given $\alpha_n\in K$ and $K$ is a field, $\alpha_n$ has an inverse $\alpha_n^{-1}$.
    1. Therefore, polynomial $b(x)-\alpha_n^{-1}\beta_na(x)$ lies in $K[x]$, whose order-$n$ term is zero, which implies $\deg\left(b(x)-\alpha_n^{-1}\beta_na(x)\right)<n$.
    1. Therefore, equation $b(x)=\alpha_n^{-1}\beta_na(x)+\left(b(x)-\alpha_n^{-1}\beta_na(x)\right)$ satisfies the desired form.
1. Assume $\deg b(x)>\deg a(x)$.
    1. Assume the theorem holds for every $b(x)$ with $\deg b(x)<n$.
    1. Letting $b(x)$ be a polynomial in $K[x]$ with degree $n$, we have $b(x)=xg(x)+c$ and $\deg g(x)=n-1$.
    1. Since $\deg g(x)=n-1$, by assumption, we have $\deg r_0(x)<\deg a(x)$ and $g(x)=a(x)q_0(x)+r_0(x)$ for some $q_0(x)$ and $r_0(x)$. Plugging $g(x)=a(x)q_0(x)+r_0(x)$ into $b(x)=xg(x)+c$ yields $b(x)=xa(x)q_0(x)+xr_0(x)+c$.
    1. If $\deg r_0(x)+1<\deg a(x)$, we have $\deg(xr_0(x)+c)<\deg a(x)$, implying equation $b(x)=xa(x)q_0(x)+xr_0(x)+c$ satisfies the desired form.
    1. If $\deg r_0(x)+1=\deg a(x)$, since $\deg a(x)<\deg b(x)$ and $\deg b(x)=n$, we have $\deg r_0(x)+1<n$, which implies $\deg(xr_0(x)+c)<n$, which by assumption implies $\deg r_1(x)<a(x)$ and $xr_0(x)+c=a(x)q_1(x)+r_1(x)$ for some $q_1(x)$ and $r_1(x)$. Plugging $xr_0(x)+c=a(x)q_1(x)+r_1(x)$ into $b(x)=xa(x)q_0(x)+xr_0(x)+c$ yields $b(x)=a(x)(xq_0(x)+q_1(x))+r_1(x)$, which satisfies the desired form.
    1. Therefore, there exist some $q(x)$ and $r(x)$ with $\deg r(x)<\deg a(x)$ and $b(x)=a(x)q(x)+r(x)$. Therefore, the theorem holds for every $b(x)$ with degree $n$.
    1. By the principle of induction, the division theorem holds for every $b(x)$ with $\deg b(x)>\deg a(x)$.

To prove the uniqueness of the division theorem, suppose there is another pair of polynomial $s(x)$ and $t(x)$ with $b(x)=a(x)s(x)+t(x)$ and $t(x)$ having a lower degree than that of $a(x)$.

1. By the division theorem, we have $\deg r(x)<\deg a(x)$ and $\deg t(x)<\deg a(x)$. We also have $\deg[r(x)-t(x)]\le\max(r(x),t(x))$. Therefore, \begin{equation}\label{eq:9.8.0}\deg[r(x)-t(x)]<\deg a(x)\,.\end{equation}
1. Given $b(x)=a(x)q(x)+r(x)$ and $b(x)=a(x)s(x)+t(x)$, we have $r(x)-t(x)=[s(x)-q(x)]a(x)$. By Theorem 9.1, we have \begin{equation}\label{eq:9.8.1}\deg[r(x)-t(x)]=\deg[s(x)-q(x)]+\deg a(x)\,.\end{equation}
1. Plugging Equation \ref{eq:9.8.1} into Equation \ref{eq:9.8.0} yields $\deg[s(x)-q(x)]<0$, which gives $\deg[s(x)-q(x)]=-\infty$, which gives $s(x)=q(x)$ and $r(x)=t(x)$.

# 9.9

1. Since $f(x)$ is a polynomial in $K[x]$ over field $K$, by Theorem 9.6, there is an unique polynomial $q(x)$ in $K[x]$ and an unique element $r$ of $K$ such that $f(x)=(x-\gamma)q(x)+r$.
1. Substituting $x=\gamma$ and $f(\gamma)=0$ into $f(x)=(x-\gamma)q(x)+r$ yields $r=0$.
1. Substituting $r=0$ into $f(x)=(x-\gamma)q(x)+r$ yields $f(x)=(x-\gamma)q(x)$. Therefore, $x-\gamma$ divides $f(x)$ in $K[x]$.

# 9.10

> **Theorem 9.8.** Let $K$ be a field, $\gamma$ be an element of $K$, and $f(x)$ and $g(x)$ be two polynomials in $K[x]$. If $x-\gamma$ divides the product $f(x)g(x)$, then $x-\gamma$ divides either $f(x)$ or $g(x)$.

1. Given $(x-\gamma)\mid f(x)g(x)$, we have $f(x)g(x)=(x-\gamma)h(x)$ for some $h(x)$, which implies $f(\gamma)g(\gamma)=0$.
1. Since $f(\gamma)g(\gamma)=0$ and $K$ is an integral domain, either $f(\gamma)=0$ or $g(\gamma)=0$.
1. Since $f(\gamma)=0$ or $g(\gamma)=0$, by Theorem 9.8, $x-\gamma$ divides either $f(x)$ or $g(x)$.

# 9.13

1. Assume polynomial $f(x)$ is in $K[x]$ of degree 2.
    1. Supposing $f(x)$ is reducible, by Theorem 9.3, $f(x)$ has a divisor of degree 1, assumably $x-\gamma$. Then $\gamma$ is a root of $f(x)$.
    1. Therefore, $f(x)$ either has a root in $K$ or is irreducible in $K[x]$.
1. Assume polynomial $f(x)$ is in $K[x]$ of degree 3.
    1. Supposing $f(x)$ is reducible, by Theorem 9.3, $f(x)$ has a divisor of degree less than or equal to $\frac32$. Thus, $f(x)$ has a divisor of degree 1, assumably $x-\gamma$. Then $\gamma$ is a root of $f(x)$.
    1. Therefore, $f(x)$ either has a root in $K$ or is irreducible in $K[x]$.
1. Polynomial $x^4+x^2+1=(x^2+1)^2$ in $\mathbb R[x]$ of degree 4 has no roots in $\mathbb R$.

# 9.14

> **Theorem 9.11.** Suppose $K\subseteq L$ is a field extension and $\gamma$ is an element of $L$ that is algebraic over $K$ of degree $n$. Let $f(x)$ be a degree-$n$ polynomial in $K[x]$ such that $f(\gamma)=0$ and let $g(x)$ be an arbitrary polynomial in $K[x]$ such that $g(\gamma)=0$. Then $f(x)$ divides $g(x)$.

1. By the division theorem, there exist polynomials $q(x)$ and $r(x)$ such that $g(x)=f(x)q(x)+r(x)$ with $r(x)$ having a degree less than $n$.
1. Plugging $f(\gamma)=0$ and $g(\gamma)=0$ into $g(x)=f(x)q(x)+r(x)$ yields $r(\gamma)=0$.
1. Since $\gamma$ is algebraic over $K$ of degree $n$, there does not exist a polynomial in $K[x]$ having a degree less than $n$ while having $\gamma$ as a root. Therefore $r(x)=0$.
1. Plugging $r(x)=0$ into $g(x)=f(x)q(x)+r(x)$ yields $g(x)=f(x)q(x)$, i.e., $f(x)$ divides $g(x)$.
