---
title: MATH 412, 2021 Summer, Chapter 12
...

# 12.1

1. Suppose $a(x)|b(x)$. We have $a(x)$ is a common divisors of $a(x)$ and $b(x)$. For every common divisor $d(x)$ of $a(x)$ and $b(x)$, we have $\deg d(x)\le\deg a(x)$ and $\deg d(x)\le b(x)$. Among every common divisors, $a(x)$ has the greatest degree. Therefore, $a(x)$ is the gcd of $a(x)$ and $b(x)$.
1.  1. Suppose $g(x)=\gcd[a(x),b(x)]$, i.e., $$\forall g'(x):g'(x)|a(x)\land g'(x)|b(x)\implies g'(x)|g(x)\land\deg g'(x)\le\deg g(x)\,.$$ Given $$g'(x)|a(x)\land g'(x)|[b(x)-a(x)q(x)]\implies g'(x)|b(x)\,,$$ we have $$\forall g'(x):g'(x)|a(x)\land g'(x)|[b(x)-a(x)q(x)]\implies g'(x)|g(x)\land\deg g'(x)\le\deg g(x)\,,$$ i.e., $g(x)=\gcd[a(x),b(x)-a(x)q(x)]$. Therefore, $$g(x)=\gcd[a(x),b(x)]\implies g(x)=\gcd[a(x),b(x)-a(x)q(x)]\,.$$
    1. Similarily, we can prove $$g(x)=\gcd[a(x),b(x)]\impliedby g(x)=\gcd[a(x),b(x)-a(x)q(x)]\,.$$
    1. Therefore, $$g(x)=\gcd[a(x),b(x)]\iff g(x)=\gcd[a(x),b(x)-a(x)q(x)]\,.$$
1. Supposing $g(x)=\gcd[a(x),b(x)]$ and $b(x)=a(x)q(x)+r(x)$, by the proposition we proved above, we have $g(x)=\gcd[r(x),a(x)]$.
1. Suppose $a(x)$ and $b(x)$ with $\deg a(x)\le\deg b(x)$. If $a(x)|b(x)$, we have proved that $\gcd[a(x),b(x)]=a(x)$. Otherwise, we can find the remainder $r(x)$ such that $b(x)=a(x)q(x)+r(x)$ and find the $\gcd[a(x),b(x)]$ by recursively finding $\gcd[r(x),a(x)]$.
1.  1. $3x^2+3=(x^4-1)-(x^3-2x^2+x-2)(x+2)$
    1. $0=(x^3-2x^2+x-2)-(3x^2+3)(\frac13x-\frac23)$
    1. Therefore, $\gcd\left(x^4-1,x^3-2x^2+x-2\right)=3x^2+3$ in $\mathbb Q[x]$.

# 12.2

1. If the Eclidean algorithm terminates for $a(x)$ and $b(x)$, the last nonzero remainder $a(x)$ is the gcd of $a(x)$ and $b(x)$.
1. If it takes 1 step until the Eclidean algorithm terminates for $a(x)$ and $b(x)$, we have \begin{align*}b(x)&=a(x)q_1(x)+r_1(x)\\a(x)&=r_1(x)q_2(x)+0\end{align*} Given $b(x)=a(x)q_1(x)+r_1(x)$, by a proposition we proved in Exercise 12.1, we have $\gcd[a(x),b(x)]=\gcd[r_1(x),a(x)]$. Given $a(x)=r_1(x)q_2(x)+0$, we have $\gcd[r_1(x),a(x)]=r_1(x)$. Therefore, $\gcd[a(x),b(x)]=r_1(x)$, i.e., the last nonzero remainder $r_1(x)$ is the gcd of $a(x)$ and $b(x)$.
1. Assume if it takes $k$ steps until the Eclidean algorithm terminates for $\alpha(x)$ and $\beta(x)$, then the last nonzero remainder is the gcd of $\alpha(x)$ and $\beta(x)$. Consider a pair of polynomials $a(x)$ and $b(x)$, for which it takes $k+1$ steps until the Eclidean algorithm terminates. We have \begin{align*}b(x)&=a(x)q_1(x)+r_1(x)\\a(x)&=r_1(x)q_2(x)+r_2(x)\\&\dots\\r_k(x)&=r_{k+1}(x)q_{k+2}(x)+0\end{align*} i.e., the Eclidean algorithm terminates for $r_1(x)$ and $a(x)$ after $k$ steps. By assumption, $\gcd[r_1(x),a(x)]=r_{k+1}(x)$. Given $b(x)=a(x)q_1(x)+r_1(x)$, by a proposition we proved in Exercise 12.1, we have $\gcd[a(x),b(x)]=\gcd[r_1(x),a(x)]$. Therefore, $\gcd[a(x),b(x)]=r_{k+1}(x)$.
1. By principle of induction, the last nonzero remainder obtained by the Euclidean algorithm applied to $a(x)$ and $b(x)$ is the gcd of $a(x)$ and $b(x)$.

# 12.3

1.  1. $x+1=(x^5+1)-(x^2+1)(x^3-x)$
    1. $2=(x^2+1)-(x+1)(x-1)$
    1. $0=(x+1)-2\left(\frac12x+\frac12\right)$
    1. $\gcd(x^2+1,x^5+1)=2$ in $\mathbb Q[x]$.
1.  1. $2x+2=(x^3+2x^2+2)-(x^2+2x+1)(x)$
    1. $0=(x^2+2x+1)-(2x+2)(2x+2)$
    1. $\gcd(x^2+2x+1,x^3+2x^2+2)=2x+2$ in $\mathbb F_3[x]$.

# 12.4

1. If the Euclidean algorithm applied to $a(x)$ and $b(x)$ terminates right away, we have $\gcd[$a(x)$,$b(x)]=a(x)=1+b(x)0$.
1. If the Euclidean algorithm applied to $a(x)$ and $b(x)$ terminates after 1 step, i.e., \begin{align*}b(x)&=a(x)q_1(x)+r_1(x)\\a(x)&=r_1(x)q_2(x)+0\end{align*}
we have $\gcd[$a(x)$,$b(x)]=r_1(x)=a(x)(-q_1(x))+b(x)1$.
1. Assume if the Euclidean algorithm applied to $\alpha(x)$ and $\beta(x)$ terminates after $k$ steps, then there exist polynomials $\gamma(x)$ and $\delta(x)$ in $K[x]$ such that $\gcd[\alpha(x),\beta(x)]=\alpha(x)\gamma(x)+\beta(x)\delta(x)$.
    1. Consider a pair of polynomials $a(x)$ and $b(x)$, for which it takes $k+1$ steps until the Eclidean algorithm terminates. We have $b(x)=a(x)q_1(x)+r_1(x)$ and the Eclidean algorithm applied to $r_1(x)$ and $a(x)$ terminates for after $k$ steps.
    1. By assumption, there exist polynomials $\gamma(x)$ and $\delta(x)$ in $K[x]$ such that $\gcd[r_1(x),a(x)]=r_1(x)\gamma(x)+a(x)\delta(x)$.
    1. Given $b(x)=a(x)q_1(x)+r_1(x)$, by a proposition we proved in Exercise 12.1, we have $\gcd[a(x),b(x)]=\gcd[r_1(x),a(x)]$.
    1. Given $b(x)=a(x)q_1(x)+r_1(x)$, $\gcd[r_1(x),a(x)]=r_1(x)\gamma(x)+a(x)\delta(x)$, and $\gcd[a(x),b(x)]=\gcd[r_1(x),a(x)]$, we have $$\gcd[a(x),b(x)]=a(x)[\delta(x)-q_1(x)\gamma(x)]+b(x)\gamma(x)\,.$$
1. By the principle of induction, for $a(x)$ and $b(x)$ in $K[x]$ over field $K$, there exist polynomials $r(x)$ and $s(x)$ in $K[x]$ such that $\gcd[a(x),b(x)]=a(x)r(x)+b(x)s(x)$.

# 12.5

1.
\begin{align*}
2 &= (x^2+1)-(x+1)(x-1) \\
&= (x^2+1)-[(x^5+1)-(x^2+1)(x^3-x)](x-1) \\
&= (x^5+1)(-x+1)+(x^2+1)(x^4-x^3-x^2+x+1)
\end{align*}
1.
\begin{align*}
2x+2 &= (x^3+2x^2+2)+(x^2+2x+1)(-x)
\end{align*}

# 12.6

1. Given $d(x)$ is the gcd of $a(x)$ and $b(x)$ in $K[x]$ produced by the Eculidean algorithm, by Bézout's Theorem, there exist $r(x)$ and $s(x)$ in $K[x]$ such that $d(x)=a(x)r(x)+b(x)s(x)$.
1. For every common divisor of $a(x)$ and $b(x)$, say $\delta(x)$, there exist $\alpha(x)$ and $\beta(x)$ such that $a(x)=\alpha(x)\delta(x)$ and $b(x)=\beta(x)\delta(x)$. Plugging into $d(x)=a(x)r(x)+b(x)s(x)$ yields $d(x)=[\alpha(x)r(x)+\beta(x)s(x)]\delta(x)$.

That is, every common divisor of $a(x)$ and $b(x)$ divides $d(x)$.

1. For every gcd of $a(x)$ and $b(x)$, say $\delta(x)$, we have $\deg\delta(x)=\deg d(x)$. By the proposition proved above, there exists $\rho(x)$ such that $d(x)=\rho(x)\delta(x)$.
1. Given $d(x)=\rho(x)\delta(x)$, we have $\deg d(x)=\deg\rho(x)+\deg\delta(x)$.
1. Given $\deg\delta(x)=\deg d(x)$ and $\deg d(x)=\deg\rho(x)+\deg\delta(x)$, we have $\deg\rho(x)=0$, implying $\rho(x)$ is a nonzero constant, say $\rho(x)=\sigma\in K$.
1. Given $d(x)=\sigma\delta(x)$ and $K$ is a field, we have $\sigma^{-1}d(x)=\delta(x)$.

That is, every gcd of $a(x)$ and $b(x)$ is a nonzero constant multiple of $d(x)$.

# 12.7

1. Given $a(x)$ and $b(x)$ are coprime polynomials in $K[x]$, by Bézout's theorem, there exist $r(x)$ and $s(x)$ in $K[x]$ such that $1=a(x)r(x)+b(x)s(x)$.
1. Given $a(x)$ divides $b(x)c(x)$ in $K[x]$, there exists $\gamma(x)$ such that $a(x)\gamma(x)=b(x)c(x)$.
1. Multiplying through $1=a(x)r(x)+b(x)s(x)$ with $c(x)$ and plugging in $a(x)\gamma(x)=b(x)c(x)$ yields $c(x)=a(x)[c(x)r(x)+\gamma(x)s(s)]$, which implies $a(x)$ divides $c(x)$ in $K[x]$.

# 12.8

> **Theorem 12.13.** Let $K$ be a field. Let $p(x)$ be an irreducible polynomial in $K[x]$, and $p(x)$ divides the product $b(x)c(x)$ in $K[x]$. Then $p(x)$ divides either $b(x)$ or $c(x)$.

1. By Bézout's theorem, there exist $s(x)$ and $t(x)$ in $K[x]$ such that $\gcd[b(x),p(x)]=b(x)s(x)+p(x)t(x)$.
1. Assume $p(x)$ does not divide $b(x)$.
    1. Assuming $\deg\gcd[b(x),p(x)]=\deg p(x)$, there exist constant $\alpha$ in $K$ and polynomial $\beta(x)$ in $K[x]$ such that $p(x)=\alpha\gcd[b(x),p(x)]$ and $b(x)=\beta(x)\gcd[c(x),p(x)]$. Since $K$ is a field, $\alpha^{-1}$ lies in $K$. Therefore, $b(x)=\beta(x)\alpha^{-1}p(x)$, contradicting the assumption that $p(x)$ does not divide $b(x)$. Therefore, $\deg\gcd[b(x),p(x)]<\deg p(x)$.
    1. Since $p(x)$ is irreducible in $K[x]$, every divisor of $p(x)$ in $K[x]$ is either a unit of $K[x]$ or of the same degree as $p(x)$. Given $\gcd[b(x),p(x)]|p(x)$ and $\deg\gcd[b(x),p(x)]<\deg p(x)$, $\gcd[b(x),p(x)]$ is a unit of $K[x]$. Let it be $u=\gcd[b(x),p(x)]$. We have $u=b(x)s(x)+p(x)t(x)$.
    1. Given $p(x)|b(x)c(x)$, there exists $q(x)$ such that $p(x)q(x)=b(x)c(x)$.
    1. Multiplying through $u=b(x)s(x)+p(x)t(x)$ with $c(x)$ and plugging in $p(x)q(x)=b(x)c(x)$ yields $c(x)=u^{-1}p(x)[q(x)s(x)+c(x)t(x)]$, which implies $p(x)$ divides $c(x)$.
1. Therefore, $p(x)$ divides either $b(x)$ or $c(x)$.

# 12.9

1. Given $a(x)$ has two factorizations such that $$p_1(x)\cdots p_m(x)=q_1(x)\cdots q_n(x),$$ which implies $p_m(x)|q_1(x)\cdots q_n(x)$, which by Corollary 12.14 implies $p_m(x)|q_j(x)$ for some $j$, i.e., $$q_j(x)=cp_m(x)$$ for some $c$.
1. Plugging $q_j(x)=cp_m(x)$ into $p_1(x)\cdots p_m(x)=q_1(x)\cdots q_n(x)$ yields $$p_1(x)\cdots p_{m-1}(x)=cq_1(x)\cdots q_{j-1}(x)q_{j+1}(x)\cdots q_n(x).$$
1. If we reorder the second factorization, particularily, swap $q_j(x)$ and $q_n(x)$, we would have $$p_1(x)\cdots p_{m-1}(x)=cq_1(x)\cdots q_{n-1}(x).$$

# 12.10

> **Theorem 12.3.** Let $K$ be a ﬁeld and let $a(x)$ be a polynomial in $K[x]$ of positive degree. Suppose $p_1(x)\cdots p_m(x)$ and $q_1(x)\cdots q_n(x)$ are two factorizations of $a(x)$ as a product of irreducible polynomials in $K[x]$. Then $m=n$, and the order of the factors in the second factorization can be changed so that for each index $i$ there is a nonzero constant $c_i$ such that $q_i(x)=c_ip_i(x)$.

1. If $m=1$, then $a(x)$ is irreducible, and $p_1(x)=q_1(x)$.
1. Assume the theorem is true when $m=k$.
    1. Considering the situation when $m=k+1$, we have $p_1(x)\cdots p_{k+1}(x)=q_1(x)\cdots q_n(x)$, which implies $p_1(x)$ divides $q_1(x)\cdots q_n(x)$, which by Corollary 12.14 implies $p_1(x)$ divides one of the factors $q_i(x)$.
    1. Properly reorder the factorization $q_1(x)\cdots q_n(x)$ so that $p_1(x)$ divides $q_1(x)$.
    1. Given both $p_1(x)$ and $q_1(x)$ are irreducible and $p_1(x)\mid q_1(x)$, there exists a unit $c_1$ of $K$ such that $c_1p_1(x)=q_1(x)$.
    1. Given $c_1p_1(x)=q_1(x)$ and $p_1(x)\cdots p_{k+1}(x)=q_1(x)\cdots q_n(x)$, we have $p_2(x)\cdots p_{k+1}(x)=c_1q_2(x)\cdots q_n(x)$.
    1. Let $q_2'(x)=c_1q_2(x)$, we have $p_2(x)\cdots p_{k+1}(x)=q_2'(x)q_3(x)\cdots q_n(x)$.
    1. By the assumption that the theorem is true when $m=k$, we have $m=n=k+1$ and $c_2p_2(x)=q_2'(x),c_3p_3(x)=q_3(x),\dots,c_{k+1}p_{k+1}(x)=q_{k+1}(x)$.
    1. Therefore, the theorem is also true when $m=k+1$.
1. By the principle of induction, the theorem is true for every positive integer $m$.
