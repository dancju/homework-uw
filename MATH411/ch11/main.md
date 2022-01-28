---
title: MATH 412, 2021 Summer, Chapter 11
...

# 11.1

For $\alpha,\beta\in\mathbb Q$, since both $\alpha-\beta i$ and $\alpha+\beta i$ are roots of polynomial $x^2-2\alpha x+\alpha^2+\beta^2$, all numbers of the form $\alpha+\beta i$ are algebraic over $\mathbb Q$.

# 11.2

Polynomial $\left(1-\left(\left(\frac13-x\right)^2-2\right)^5\right)^3=7$ has $\frac13-\sqrt{2+\sqrt[5]{1-\sqrt[3]7}}$ as a root.

# 11.3

1. $x^4-2=(x^2-\sqrt2)(x^2+\sqrt2)$.
1. The four roots of $x^4-2$ are $-\sqrt[4]2$, $\sqrt[4]2$, $-\sqrt[4]2i$, and $\sqrt[4]2i$.
1. Since every root is irrational, $x^4-2$ has no linear rational factors. Therefore, either $x^4-2$ is irreducible in $\mathbb Q[x]$, or it factors as the product of two rational quadratic polynomial.
1. Suppose $x^4-2$ factors as a product of two rational quadratic polynomials $ax^2+bx+c$ and $dx^2+ex+f$ with $a,b,c,d,e,f\in\mathbb Q$. We get \begin{align} ad&=1 \label{eq:11.3.0} \\ ae+bd&=0 \label{eq:11.3.1} \\ af+be+cd&=0 \label{eq:11.3.2} \\ bf+ce&=0 \label{eq:11.3.3} \\ cf&=-2 \label{eq:11.3.4} \end{align}
1. Taking Equation \ref{eq:11.3.0} and \ref{eq:11.3.1} and eliminating $a$ yields \begin{equation}e+bd^2=0 \label{eq:11.3.5}\end{equation}.
1. Taking Equation \ref{eq:11.3.3} and \ref{eq:11.3.4} and eliminating $f$ yields \begin{equation}-2b+c^2e=0 \label{eq:11.3.6}\end{equation}.
1. Taking Equation \ref{eq:11.3.5} and \ref{eq:11.3.6} and eliminating $e$ yields $(c^2d^2+2)b=0$, implying $b=e=0$.
1. Plugging $b=e=0$ into Equation \ref{eq:11.3.2} yields \begin{equation}af+cd=0\,. \label{eq:11.3.7}\end{equation} Plugging Equation \ref{eq:11.3.0} and \ref{eq:11.3.4} into $ac\times$\ref{eq:11.3.7} yields $2a^2=c^2$.
1. The equation $2a^2=c^2$ contradicts the assumption $a,c\in\mathbb Q$. Therefore, the assumpiton must be wrong. Thus, $x^4-2$ is irreducible in $\mathbb Q[x]$.

# 11.4

> **Exercise 11.4.** Prove that the only units in $\mathbb Z[x]$ are 1 and $-1$.

1. Assume $a(x)\in\mathbb Z[x]$ is a unit. By the definition of unit, we have $a(x)a^{-1}(x)=1$, which implies $\deg a(x)+\deg a^{-1}(x)=0$.
1. If $\deg a(x)=-\infty$, there would be no $a^{-1}(x)\in\mathbb Z[x]$ satisfying $\deg a(x)+\deg a^{-1}(x)=0$. Therefore, $\deg a(x)\ne-\infty$. Similarily, $\deg a(x)^{-1}\ne-\infty$. Therefore, $\deg a(x)\ge0$ and $\deg a^{-1}(x)\ge0$.
1. Given $\deg a(x)\ge0$, $\deg a^{-1}(x)\ge0$, and $\deg a(x)+\deg a^{-1}(x)=0$, we have $\deg a(x)=\deg a^{-1}(x)=0$, which implies $a(x),a^{-1}(x)\in\mathbb Z$.
1. Therefore, every unit of $\mathbb Z[x]$ lies in $\mathbb Z$.
1. Since the only units in $\mathbb Z$ are 1 and $-1$. Therefore, the only units in $\mathbb Z[x]$ are 1 and $-1$.

# 11.5

1. 1. Assume $g(x)$ in $\mathbb Z[x]$ is primitive, i.e., the gcd of the coefficients of $g(x)$ is 1. Since all prime numbers are greater than 1, there does not exist a prime number being a divisor of every coefficient of $g(x)$.
    1. Assume $g(x)$ in $\mathbb Z[x]$ is not primitive, i.e., the gcd of the coefficients of $g(x)$ is $d>1$. Since every integer greater than 1 has a prime factor, let one of them be $p$. Given $d$ is the gcd of the coefficients of $g(x)$ and $p$ is a prime factor of $d$, $p$ divides every coefficients of $g(x)$.
    1. Polynomial $g(x)$ in $\mathbb Z[x]$ is primitive iff there is no prime number that divides every coefficients of $g(x)$.
1. $3x^7+12x^5-15x^2+21=(x^7+4x^5-5x^2+7)3$.

> **Proposition.** A primitive polynomial of positive degree that does not factor in $\mathbb Z[x]$ as a product of lower-degree polynomials is irreducible in $Z[x]$.

1. Suppose $f(x)$ is a primitive polynomial of positive degree that does not factor as a product of lower-degree polynomials in $\mathbb Z[x]$.
1. Since $f(x)$ does not factor as a product of lower-degree polynomials in $\mathbb Z[x]$, it only factors as a product of a constant and a polynomial of the same degree. Assume there exists a factorization $f(x)=ag(x)$.
1. Since $f(x)$ is primitive, i.e., the gcd of the coefficients of $f(x)$ is 1, and $a$ is a common divisor of the coefficients of $f(x)$, $a$ must be $-1$ or 1.
1. Since $a\in\{-1,1\}$, $f(x)=ag(x)$ is a trivial factorization. Therefore, $f(x)$ is irreducible in $\mathbb Z[x]$.

> **Theorem 11.2.** The irreducible elements of $Z[x]$ are
>
> 1. Prime numbers of $\mathbb Z$ and their negatives;
> 1. Polynomials of positive degree that are primitive and that do not factor as products of lower-degree polynomials.

1. Consider an element $f(x)$ in $\mathbb Z[x]$.
    1. If $f(x)\in\{-1,0,1\}$, it is by definition reducible.
    1. If $f(x)$ is a prime integer, by the definition of prime integers, it is irreducible.
    1. If $f(x)$ is a composite integer, by definition it has a nontrivial factorization in $\mathbb Z$ and therefore is reducible in $\mathbb Z[x]$.
    1. If $f(x)$ is a negative of a prime integer, with the only factorizations being trivial such that $f(x)=(-1)(-f(x))=(-f(x))(-1)$, it is irreducible.
    1. If $f(x)$ is a negative of a composite integer, e.g. $f(x)=-c$, since $c$ has a nontrivial factorization $c=ab$, $f(x)$ also has a nontrivial factorization $f(x)=(-a)b$. Therefore, $f(x)$ is reducible.
    1. If $f(x)$ is of positive degree and not primitive, it is reducible to $f(x)=mp(x)$ where $m$ is the gcd of its coefficients.
    1. If $f(x)$ factors as a product of lower-degree polynomials, it is by definition reducible.
    1. If $f(x)$ is a primitive polynomial of positive degree that do not factor as a product of lower-degree polynomials in $\mathbb Z[x]$, as is proved, it is irreducible.
1. Therefore, the irreducible elements of $\mathbb Z[x]$ are
    1. Prime numbers and their negatives, and
    1. Primitive polynomials of positive degree that do not factor as products of lower-degree polynomials.

# 11.6

> **Theorem 11.3.** The product of primitive polynomials is primitive. If $g(x)$ and $h(x)$ are two primitive polynomials in $Z[x]$, then their product $g(x)h(x)$ is also primitive.

1. Let $p$ be an arbitrary prime number and \begin{align*}g(x)=b_mx^m+\cdots+b_1x+b_0\\h(x)=c_nx^n+\cdots+c_1x+c_0\end{align*}
1. Since $g(x)$ is primitive, $g(x)$ has a coefficient that is not a multiple of $p$, otherwise $p$ would be a common divisor of $b_m,\dots,b_0$, contradicting the primitivity of $g(x)$.
1. Let $b_i$ be the first coefficient of $g(x)$ not being multiple of $p$ such that $i=\min\{i:p\nmid b_i\land i=0,\dots,m\}$.
1. Similarily, let $c_j$ be the first coefficient of $h(x)$ not being multiple of $p$ such that $j=\min\{i:p\nmid c_i\land i=0,\dots,n\}$.
1. The order-$(i+j)$ coefficient of $g(x)h(x)$ is \begin{equation}\sum_{k=0}^{i+j}b_kc_{i+j-k}=\left(\sum_{k=0}^{i-1}b_kc_{i+j-k}\right)+b_ic_j+\left(\sum_{k=i+1}^{i+j}b_kc_{i+j-k}\right).\label{eq:11.6.0}\end{equation}
1. Since $i=\min\{i:p\nmid b_i\land i=0,\dots,m\}$, we have $p$ divides $\sum_{k=0}^{i-1}b_kc_{i+j-k}$.
1. Similarily, $p$ also divides $\sum_{k=i+1}^{i+j}b_kc_{i+j-k}$.
1. Given $i=\min\{i:p\nmid b_i\land i=0,\dots,m\}$ and $j=\min\{i:p\nmid c_i\land i=0,\dots,n\}$, we have $p\nmid b_ic_j$.
1. Therefore, $p$ does not divide the order-$(i+j)$ coefficient of $g(x)h(x)$.
1. Therefore, for every prime number $p$, $g(x)h(x)$ has a coefficient not being multiple of $p$.
1. Therefore, $g(x)h(x)$ is primitive.

# 11.7

> **Exercise 11.7.** Let $n$ be an integer greater than 1. Prove that $x^n-2$ is irreducible in $\mathbb Q[x]$.

1. Assume $x^n-2$ is reducible such that $x^n-2=g(x)h(x)$ with $g(x)=\sum_{i=0}^kb_ix^i\in\mathbb Z[x]$ and $h(x)=\sum_{i=0}^lc_ix^i\in\mathbb Z[x]$. We will disprove it by contradition.
    1. By assumption, we have $x^n-2=\sum_{i=0}^n\left(\sum_{j=0}^ib_jc_{i-j}\right)x^i$ with $\forall i>k:b_i=0$ and $\forall i>l:c_i=0$. Consequently, we have \begin{align*}k+l&=n&b_0c_0&=-2&b_kc_l&=1\\\sum_{j=0}^1b_jc_{1-j}&=0&\dots&&\sum_{j=0}^{n-1}b_jc_{n-1-j}&=0\end{align*}
    1. Given $b_0c_0=-2$, 2 divides either $b_0$ or $c_0$ but not both. Assume $2|b_0$ and $2\nmid c_0$.
    1. We will prove $\forall i\in\{0,\dots,n-1\}:2|b_i$ by induction.
        1. We have proved $2|b_0$.
        1. Assume $\forall i\in\{0,\dots,m\}:2\mid b_i$ with $m\le n-2$. Considering $$b_{m+1}c_0=\left(\sum_{j=0}^{m+1}b_jc_{m+1-j}\right)-\left(\sum_{j=0}^mb_jc_{m+1-j}\right)\,,$$ plugging in $\sum_{j=0}^{m+1}b_jc_{m+1-j}=0$ and the assumption, we get $2|b_{m+1}c_0$. Given $2\nmid c_0$ and $2|b_{m+1}c_0$, we get $2|b_{m+1}$.
    1. Given $\forall i\in\{0,\dots,n-1\}:2|b_i$ and $k<n$, we have $2|b_k$, which contradicts $b_kc_l=1$. Therefore, the assumption is false, i.e., $x^n-2$ is irreducible in $\mathbb Z[x]$.
1. By Corollary 11.5, $x^n-2$ is also irreducible in $\mathbb Q[x]$.

# 11.8

1. The proof in Exercise 11.7 also holds for $x^n-2m$ with odd integer $m$ since we can deduce the contradiction by showing $2|b_k$.
1. Therefore, for every positive integer $n$ and odd integer $m$, polynomial $x^n-2m$ is irreducible in $\mathbb Q[x]$. Since there are infinitely many integer $m$, there exist infinitely many irreducible monic polynomials in $\mathbb Q[x]$ of given degree $n$.
1. In contrast, for polynomials in $\mathbb C[x]$, only ones of degree 0 or 1 are irreducible.

# 11.9

1. The proof in Exercise 11.7 also holds for $x^n-p$ with prime integer $p$ since we can deduce the contradiction by showing $p|b_k$.
1. Therefore, $x^n-p$ is irreducible in $\mathbb Q[x]$ for every positive integer $n$ and prime integer $p$.
1. The proof in Exercise 11.7 also holds for $x^n-pm$ with prime integer $p$ and integer $m$ coprime to $p$ since we can deduce the contradiction by showing $p|b_k$. Therefore, polynomial $x^n-pm$ with prime integer $p$ and integer $m$ coprime to $p$ is irreducible in $\mathbb Q[x]$.

# 11.10

1. Supposing
$$x^{14}-27x^{11}+15x^3+12=\left(\sum_{i=0}^kb_ix^i\right)\left(\sum_{i=0}^lc_ix^i\right)=\sum_{i=0}^{14}\left(\sum_{j=0}^ib_jc_{i-j}\right)x^i \,,$$
with every $b_i$ and $c_i$ being integers and out-of-bound elements being zeros such that
$$\forall i>k:b_i=0,\quad\forall i>l:c_i=0\,$$
we get
\begin{align*}
k+l &= 14 &
b_0c_0 &= 12 &
b_kc_l &= 1 \\
\sum_{j=0}^1b_jc_{1-j} &= 0 &
\sum_{j=0}^2b_jc_{2-j} &= 0 &
\sum_{j=0}^3b_jc_{3-j} &= 15 \\
\sum_{j=0}^4b_jc_{4-j} &= 0 &
\dots & &
\sum_{j=0}^{10}b_jc_{10-j} &= 0 \\
\sum_{j=0}^{11}b_jc_{11-j} &= -27 &
\sum_{j=0}^{12}b_jc_{12-j} &= 0 &
\sum_{j=0}^{13}b_jc_{13-j} &= 0
\end{align*}
which implies
\begin{align*} &
b_0c_0=12\,,\quad
b_kc_l=1\,, \\ &
\forall i\in\{1,\dots,13\}:\sum_{j=0}^{i}b_jc_{i-j}\equiv0\pmod3\,.
\end{align*}
1. Given $b_0c_0=12$, 3 divides either $b_0$ or $c_0$ but not both. Assume $0\equiv b_0\not\equiv c_0\pmod 3$.
1. 1. We have proved $0\equiv b_0\pmod 3$.
   1. Assume $\forall i\in\{0,\dots,m\}:b_i\equiv0\pmod 3$ with $m\le12$. Considering $$b_{m+1}c_0=\left(\sum_{j=0}^{m+1}b_jc_{m+1-j}\right)-\left(\sum_{j=0}^mb_jc_{m+1-j}\right) \,.$$, plugging in $\sum_{j=0}^{m+1}b_jc_{m+1-j}\equiv0\pmod3$ and the assumption, we get $b_{m+1}c_0\equiv0\pmod3$. Given $c_0\not\equiv0\pmod 3$ and $b_{m+1}c_0\equiv0\pmod3$, we have $b_{m+1}\equiv0\pmod 3$.
   1. By the principle of induction, we proved that $\forall i\in\{0,\dots,13\}:b_i\equiv0\pmod 3$.

<!-- 1. We have proved $\forall i\in\{0,\dots,14\}:3|b_i$, contradicting the assumption that $x^{14}-27x^{11}+15x^3+12=\left(\sum_{i=0}^kb_ix^i\right)\left(\sum_{i=0}^lc_ix^i\right)$. Thus, the assumption must be wrong, i.e., $x^{14}-27x^{11}+15x^3+12$ does not factor in $\mathbb Z[x]$. -->

# 11.11

> **Eisenstein's criterion.** Suppose $f(x)=a_nx^n+\cdots+a_1x+a_0\in\mathbb Z[x]$, $\deg f(x)>1$, and there is a prime number $p$ such that
>
> 1. the coeﬃcient $a_n$ is not divisible by $p$;
> 2. every coeﬃcient $ai$ with $i<n$ is divisible by $p$; and
> 3. the constant coeﬃcient $a_0$ is not divisible by $p^2$.

1. Suppose $f(x)$ satisfies Eisenstein's criterion and $f(x)=g(x)h(x)$ with $g(x)=\sum_{i=0}^kb_ix^i\in\mathbb Z[x]$ and $h(x)=\sum_{i=0}^lc_ix^i\in\mathbb Z[x]$. We have $f(x)=\sum_{i=0}^n\left(\sum_{j=0}^ib_jc_{i-j}\right)x^i$ with $$\forall i>k:b_i=0,\quad\forall i>l:c_i=0\,.$$ Since $f(x)$ satisfies Eisenstein's criterion, we have
\begin{align*}
k+l=n \\
p^2\nmid b_0c_0 \\
p|b_0c_0 \\
p|\sum_{j=0}^1b_jc_{1-j} \\
\dots \\
p|\sum_{j=0}^{n-1}b_jc_{n-1-j} \\
p\nmid \sum_{j=0}^nb_jc_{n-1-j} \\
\end{align*}
1. Given $p|b_0c_0$ and $p$ is prime, $p$ divides either $b_0$ or $c_0$ but not both. Assume $p|b_0$ and $p\nmid c_0$.
1.  1. We have shown $p|b_0$.
    1. Assume $\forall i\in\{0,1,\dots,k\}:p|b_i$ with $k\le n-2$. We have $$b_{k+1}c_0=\left(\sum_{j=0}^{k+1}b_jc_{k+1-j}\right)-\left(\sum_{j=0}^kb_jc_{k+1-j}\right)\,.$$ Plugging in $p|\sum_{j=0}^{k+1}b_jc_{k+1-j}$ and $\forall i\in\{0,1,\dots,k\}:p|b_i$, we have $p|b_{k+1}c_0$. Since $p\nmid c_0$, we have $p|b_{k+1}$. Thus, under the assumption of $\forall i\in\{0,1,\dots,k\}:p|b_i$ with $k\le n-2$, we have $p|b_{k+1}$.
    1. By the principle of induction, we have $\forall i\in\{0,1,\dots,n-1\}:p|b_i$.
1. Given $\forall i\in\{0,1,\dots,n-1\}:p|b_i$ and $k<n$, we have $p|b_k$, which implies $p|a_n$, contradicting the Eisenstein's criterion. Therefore, the assumption is false, i.e., a polynomial in $\mathbb Z[x]$ satisfying the Eisenstein's criterion does not factor in $\mathbb Z[x]$.

# 11.12

1. Using Eisenstein's criterion with $p=7$, polynomial $x^{22}+7x^3+7$ does not factor in $\mathbb Z[x]$ nor in $\mathbb Q[x]$.
1. Using Eisenstein's criterion with $p=5$, polynomial $x^{35}+35x^{15}-90$ does not factor in $\mathbb Z[x]$ nor in $\mathbb Q[x]$.
1. Using Eisenstein's criterion with $p=5$, polynomial $1662x^{384}-35x^{100}+625x^{44}+100x^{10}-75x+20$ does not factor in $\mathbb Z[x]$ nor in $\mathbb Q[x]$.
1. Using Eisenstein's criterion with $p=7$, polynomial $6x^{31}+35x^{21}+245x^{11}+175$ does not factor in $\mathbb Z[x]$ nor in $\mathbb Q[x]$.

# 11.13

1.
\begin{align*}
x^2 &= x^2 \\
x^2+1 &= (x+1)^2 \\
x^2+x &= x(x+1) \\
x^2+x+1 &\text{ is irreducible in }\mathbb F_2[x] \\
\end{align*}
1.
\begin{align*}
x^3 &= x^3 \\
x^3+1 &= (x+1)(x^2+x+1) \\
x^3+x &= x(x+1)^2 \\
x^3+x+1 &\text{ is irreducible in }\mathbb F_2[x] \\
x^3+x^2 &= x^2(x+1) \\
x^3+x^2+1 &\text{ is irreducible in }\mathbb F_2[x] \\
x^3+x^2+x &=x(x^2+x+1) \\
x^3+x^2+x+1 &=(x+1)^3  \\
\end{align*}
1.
\begin{align*}
x^2 &= x^2 \\
x^2+1 &\text{ is irreducible in }\mathbb F_3[x] \\
x^2+2 &= (x+1)(x+2) \\
x^2+x &= x(x+1) \\
x^2+x+1 &= (x+2)^2 \\
x^2+x+2 &\text{ is irreducible in }\mathbb F_3[x] \\
x^2+2x &= x(x+2) \\
x^2+2x+1 &= (x+1)^2 \\
x^2+2x+2 &\text{ is irreducible in }\mathbb F_3[x] \\
2x^2 &= 2x^2 \\
2x^2+1 &= 2(x+1)(x+2) \\
2x^2+2 &\text{ is irreducible in }\mathbb F_3[x] \\
2x^2+x &= 2x(x+2) \\
2x^2+x+1 &\text{ is irreducible in }\mathbb F_3[x] \\
2x^2+x+2 &= 2(x+1)^2 \\
2x^2+2x &= 2x(x+1) \\
2x^2+2x+1 &\text{ is irreducible in }\mathbb F_3[x] \\
2x^2+2x+2 &= 2(x+2)^2 \\
\end{align*}

# 11.14

> **Theorem 11.7.** For every prime integer $p$, the polynomial ring $\mathbb F_p[x]$ has irreducible polynomials of arbitrarily high degree. That is, there is no positive integer $n$ such that all the irreducible polynomials of $\mathbb F_p[x]$ have degree less than or equal to $n$.

1. By enumerating every coefficients, we find that the number of polynomials in $\mathbb F_p[x]$ of degree at most $n$ is $p^{n+1}$.
1. Assume there is a integer $n$ such that all the irreducible polynomials in $\mathbb F_p[x]$ have degree less than or equal to $n$.
    1. The number of all the irreducible polynomials in $\mathbb F_p[x]$ would be at most $p^{n+1}$, contradicting Theorem 9.4, which asserts that $\mathbb F_p[x]$ has infinitely many irreducible polynomials.
    1. Therefore, the assumption is false, i.e., there does not exist such integer $n$. Therefore, for every prime number $p$, ring $\mathbb F_p[x]$ has irreducible polynomials of arbitrarily high degree.

# 11.16

> **Theorem 11.9.** Suppose $f(x)$ is a polynomial of positive degree in $\mathbb Z[x]$ and $p$ is a prime number that does not divide the highest-degree coefficient of $f(x)$. If the reduction $[f](x)$ of $f(x)$ modulo $p$ is irreducible in $\mathbb F_p[x]$, then $f(x)$ does not factor in $\mathbb Z[x]$ as a product of lower-degree polynomials.

1. Assume $f(x)$ factors as a product of lower-degree polynomials in $\mathbb Z[x]$ such that $f(x)=g(x)h(x)$.
    1. By Theorem 11.8, we have $[f](x)=[g](x)[h](x)$ in $\mathbb F_p[x]$.
    1. Since $p$ does not divide the highest degree coefficient of $f(x)$, $\deg f(x)=\deg[f](x)$, which implies $[g](x)$ and $[h](x)$ have lower degree than that of $[f](x)$.
1. We have proved that if $f(x)$ factors as a product of lower-degree polynomials in $\mathbb Z[x]$, then $[f](x)$ is reducible in $\mathbb F_p[x]$. Contrapositively, if $[f](x)$ is irreducible in $\mathbb F_p[x]$, then $f(x)$ does not factor as a product of lower-degree polynomials in $\mathbb Z[x]$.

# 11.18

Given $f(x)=x^5+x^4+2x^3+2x+2$. We will find divisor of $f(x)$ in $\mathbb F_3[x]$.

1.  There are 3 irreducible monic polynomials in $\mathbb F_3[x]$ of degree 1, namely $x,x+1,x+2$, none of which is a divisor of $f(x)$ since
    1. $f(x)=(x)(x^4+x^3+2x^2+2)+2$
    1. $f(x)=(x+1)(x^4+2x^2+x+1)+1$
    1. $f(x)=(x+2)(x^4+2x^3+x^2+x)+2$
1.  There are 3 irreducible monic polynomials in $\mathbb F_3[x]$ of degree 2, namely $x^2+1,x^2+x+2,x^2+2x+2$, none of which is a divisor of $f(x)$ since
    1. $f(x)=(x^2+1)(x^3+x^2+x+2)+x$
    1. $f(x)=(x^2+x+2)(x^3)+2x+2$
    1. $f(x)=(x^2+2x+2)(x^3+2x^2+2x+1)+2x$
1. There are 6 reducible monic polynomials in $\mathbb F_3[x]$ of degree 2, none of which is a divisor of $f(x)$, otherwise there would be a divisor of $f(x)$ of degree 1.
1. We have proved there are no monic polynomials in $\mathbb F_3[x]$ of degree 1 or 2 being a divisor of $f(x)$. Given $\deg f(x)=5$, $f(x)$ is irreducible in $\mathbb F_3[x]$.
1. By Theorem 11.9, $f(x)$ is irreducible in $\mathbb Z[x]$.

# 11.19

1. Assume both $g(x)$ and $h(x)$ are primitive in $\mathbb Z[x]$.
    1. Equivalently, for every prime number $p$, both $[g]_p(x)$ and $[h]_p(x)$ are nonzero.
    1. For every prime number $p$, since there is no zero factor in $\mathbb F_p(x)$, $[g]_p(x)[h]_p(x)$ is nonzero.
    1. Equivalently, $g(x)h(x)$ is primitive.
1. If both $g(x)$ and $h(x)$ are primitive in $\mathbb Z[x]$, then $g(x)h(x)$ is also primitive.

# 11.20

> **Eisenstein's criterion.** Suppose $f(x)=a_nx^n+\cdots+a_1x+a_0\in\mathbb Z[x]$, $\deg f(x)>1$, and there is a prime number $p$ such that
>
> 1. the coeﬃcient $a_n$ is not divisible by $p$;
> 2. every coeﬃcient $ai$ with $i<n$ is divisible by $p$; and
> 3. the constant coeﬃcient $a_0$ is not divisible by $p^2$.

1. Suppose $f(x)$ satisfies Eisenstein's criterion, and $f(x)$ factors as the product of lower-degree polynomials in $\mathbb Z[x]$ such that $f(x)=g(x)h(x)$. We will disprove this by contradiction.
    1. Let $g(x)=b_kx^k+\cdots+b_1x+b_0$ and $h(x)=c_lx^l+\cdots+c_1x+c_0$ be two polynomials in $\mathbb Z[x]$ of degree $k$ and degree $l$ respectively.
    1. Given $f(x)=g(x)h(x)$, we have $\forall i\in\{0,\dots,n\}:a_i=\sum_{j=0}^ib_jc_{i-j}$ with $\forall i>k:b_i=0$ and $\forall i>l:c_i=0$.
    1. Given $f(x)$ satisfies Eisenstein's criterion, we have $[a_n]\ne0$ and $\forall i\in\{0,\dots,n-1\}:[a_i]=0$. Therefore, $[b_k][c_l]=1$ and $\forall i\in\{0,\dots,n-1\}:\sum_{j=0}^i[b_j][c_{i-j}]=0$.
    1. The fact $\forall i\in\{0,\dots,n-1\}:\sum_{j=0}^i[b_j][c_{i-j}]=0$ implies $[b_0][c_0]=0$.
    1. Assume both $[b_0]$ and $[c_0]$ are zero, then $p^2\mid a_0$, contraditing the Eisenstein's criterion. Either $[b_0]$ or $[c_0]$ is not zero.
    1. Given $[b_0][c_0]=0$ and either $[b_0]$ or $[c_0]$ is not zero, one of $[b_0]$ and $[c_0]$ is zero and the other is not. Assume $[b_0]=0$ and $[c_0]\ne0$.
    1. We will prove $\forall i\in\{0,\dots,n-1\}:[b_i]=0$ by induction.
        1. We have shown $[b_0]=0$.
        1. Assume $\forall i\in\{0,\dots,m\}:[b_i]=0$ with $m\le n-2$. Considering $$b_{m+1}c_0=a_{m+1}-\left(\sum_{j=0}^mb_jc_{m+1-j}\right)\,,$$ plugging in $[a_{m+1}]=0$ and the assumption, we get $[b_{m+1}c_0]=0$. Given $[b_{m+1}c_0]=0$ and $[c_0]\ne0$, we get $[b_{m+1}]=0$.
    1. Given $\forall i\in\{0,\dots,n-1\}:[b_i]=0$ and $k<n$, we get $[b_k]=0$. Given $[b_k]=0$ and $a_n=b_kc_l$, we get $[a_n]=0$, which contradicts the Eisenstein's criterion.
