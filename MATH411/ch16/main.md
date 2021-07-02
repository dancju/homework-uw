---
title: MATH 412, 2021 Summer, Chapter 16
header-includes:
    \usepackage{extarrows}
...

# 16.1

> **Theorem 16.1.** Let $p$ be a prime number. Suppose $r$ is a Gaussian integer satisfying $N(r)=p$. Then $r$ is irreducible in $\mathbb Z[i]$. In particular, if $a$ and $b$ are integers such that $a^2+b^2=p$, then the Gaussian integers $\pm a\pm bi$ and $\pm b\pm ai$ are irreducible.

Let $st$ be a factorization of $r$. Given $N(r)=p$, we have $p=N(s)N(t)$. Since both $N(s)$ and $N(t)$ are integers and $p$ is prime, $N(s)N(t)$ is a trivial factorization of $p$, i.e., either $N(s)$ or $N(t)$ equals 1. Therefore, either $s$ or $t$ is a unit, which implies $st$ is a trivial factorization of $r$. Therefore, $r$ is irreducible in $\mathbb Z[i]$.

# 16.2

> **Proposition 16.2** Let $r$ be a Gaussian integer that is neither zero nor a unit. Then $r$ is irreducible in $\mathbb Z[i]$ if and only if its complex conjugate $\bar r$ is irreducible in $\mathbb Z[i]$.

1. Suppose $r$ is irreducible in $\mathbb Z[i]$. We will prove $\bar r$ is also irreducible under such assumption.
    1. Let $xy$ be a nontrivial factorization of $r$. We have $\bar r=\bar x\bar y$.
    1. Since $xy$ is a nontrivial factorization in $\mathbb Z[i]$, neither $x$ nor $y$ is one of $-1,1,-i,i$. Therefore, neither $\bar x$ nor $\bar y$ is one of $-1,1,-i,i$.
    1. Given $\bar r=\bar x\bar y$ and neither $\bar x$ nor $\bar y$ is one of $-1,1,-i,i$, $\bar x\bar y$ is a nontrivial factorization.
1. Similarily, we can also prove that $\bar r$ being irreducible implies $r$ being irreducible. Therefore, $r$ is irreducible in $\mathbb Z[i]$ iff $\bar r$ is irreducible in $\mathbb Z[i]$.

# 16.3

> **Theorem 16.3.** Let $r$ be an irreducible Gaussian integer. Then one of the following holds:
>
> 1. There is a prime number $p$ such that $N(r)=p$. In this case, $r$ equals $a+bi$ for a pair of nonzero integers $a$ and $b$ satisfying $a^2+b^2=p$.
> 1. There is a prime number $p$ such that $N(r)=p^2$. In this case, $r$ equals one of the four numbers $p,-p,pi$, or $-pi$.

1. Given $N(r)=r\bar r$ and $r$ is irreducible in $\mathbb Z[i]$, $r\bar r$ is a irreducible factorization of $N(r)$ in $\mathbb Z[i]$. By Theorem 15.20, every irreducible factorization of $N(r)$ in $\mathbb Z[i]$ consists of two factors.
1. The prime factorization of $N(r)$ in $\mathbb Z$ consists of one or two factors. Otherwise, $N(r)$ would factors as a product of more than two elements in $\mathbb Z[i]$, contradicting the fact that every irreducible factorization of $N(r)$ in $\mathbb Z[i]$ consists of two factors.
1. Suppose the prime factorization of $N(r)$ in $\mathbb Z$ consists of one factor. $N(r)$ is a prime number itself, corresponding to the first case of the proposition.
1. Suppose the prime factorization of $N(r)$ in $\mathbb Z$ consists of two factors, such that $N(r)=p_1p_2$ where $p_1$ and $p_2$ are prime numbers. We have $N(r)=r\bar r=p_1p_2$. By Theorem 15.20, either $r$ or $\bar r$ equals $-p_1$, $p_1$, $-p_1i$, or $p_1i$. In either case, $N(r)=p_1^2$, corresponding to the second case of the proposition.

# 16.4

1. Let $p$ be a prime number. We will prove $p$ is either irreducible in $\mathbb Z[i]$ or factors as a product of two conjugate irreducible Gaussian integers in two steps.
    1. First, we will prove $p$ factors as a product of at most two Gaussian integers.
        1. Suppose $p$ factors as $\pi_1\cdots\pi_r$ in $\mathbb Z[i]$. We have $N(p)=N(\pi_1)\cdots N(\pi_r)=p^2$. By Theorem 16.3, which states every $N(\pi_i)$ is either a prime number or a square of prime number, we have $r$ equals either 1 or 2, i.e., $p$ factors as a product of at most two Gaussian integers, otherwise $N(p)$ would factor as more than 2 prime numbers in $\mathbb Z$.
    1. Second, we will prove that if $p$ factors as a product of two Gaussian integers, then they are conjugate.
        1. By assumption, we have $p=\pi_1\pi_2$ and $N(p)=N(\pi_1)N(\pi_2)=p^2$.
        1. Given $N(\pi_1)N(\pi_2)=p^2$, by Theorem 16.3, we have $N(\pi_1)=N(\pi_2)=p$.
        1. Assuming $\pi_1=a_1+b_1i$ and $\pi_2=a_2+b_2i$ with $a_1,b_1,a_2,b_2\in\mathbb Z$, we have \begin{align*}a_1^2+b_1^2=p\\a_2^2+b_2^2=p\\a_1a_2-b_1b_2=p\\a_1b_2+a_2b_1=0\end{align*} Solving for $a_2$ and $b_2$ yields $a_2=a_1$ and $b_2=-b_1$, which implies $\pi_1$ and $\pi_2$ are conjugate.
1. Therefore, $p$ is irreducible in $\mathbb Z[i]$ iff equation $x^2+y^2=p$ is not solvable in $\mathbb Z$.
1. Moreover, every integer solution to $x^2+y^2=p$ corresponds to a nontrivial factorization $(x+yi)(x-yi)$.
1. If $p=2$, since the only solutions to $x^2+y^2=2$ are $(\pm1,\pm1)$, the only irreducible Gaussian integers dividing 2 would be $\pm1\pm i$.
1. Assume $p$ is odd, we will prove there are 8 integer solutions to $a^2+b^2=p$ satisfying $|a|\ne|b|$.
    1. If $|a|=|b|$, there would be $p=2a^2=2b^2$, contradicting $p$ is odd. Therefore, $|a|\ne|b|$.
    1. Let $(a+bi)(a-bi)$ be a factorization of $p$, according to the Unique Factorization Theorem of Gaussian integers, all factorizations of $p$ are $(a+bi)(a-bi)$, $(-a-bi)(-a+bi)$, $(ai-b)(-ai-b)$, and $(-ai+b)(ai+b)$, which corresponds to all solutions to $a^2+b^2=p$, namely $(\pm a,\pm b)$, $(\pm b,\pm a)$.

# 16.6

1. $\mathbb Z_2[i]=\{a+bi:a,b\in\mathbb Z_2\}=\{0,1,i,1+i\}$.
1. .
\begin{tabular}{rrrrr}
\toprule
$+$ & 0 & 1 & $i$ & $1+i$ \\
\midrule
0 & 0 & 1 & $i$ & $1+i$ \\
1 & 1 & 0 & $1+i$ & $i$ \\
$i$ & $i$ & $1+i$ & 0 & 1 \\
$1+i$ & $1+i$ & $i$ & 1 & 0 \\
\bottomrule
\end{tabular}
\begin{tabular}{rrrrr}
\toprule
$\times$ & 0 & 1 & $i$ & $1+i$ \\
\midrule
0 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & $i$ & $1+i$ \\
$i$ & 0 & $i$ & $1$ & $1+i$ \\
$1+i$ & 0 & $1+i$ & $1+i$ & 0 \\
\bottomrule
\end{tabular}
1.  a. $1+i$ is a zero-divisor in $\mathbb Z_2[i]$.
    a. $1+i$ does not have a multiplicative inverse in $\mathbb Z_2[i]$.
    a. $\mathbb Z_2[i]$ is not a field.
1. .
\begin{tabular}{rrrrrrrrrr}
\toprule
$\times$ & 0 & $i$ & $2i$ & 1 & $1+i$ & $1+2i$ & 2 & $2+i$ & $2+2i$ \\
\midrule
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
$i$ & 0 & 2 & 1 & $i$ & $2+i$ & $1+i$ & $2i$ & $2+2i$ & $1+2i$ \\
$2i$ & 0 & 1 & 2 & $2i$ & $1+2i$ & $2+2i$ & $i$ & $1+i$ & $2+i$ \\
1 & 0 & $i$ & $2i$ & 1 & $1+i$ & $1+2i$ & 2 & $2+i$ & $2+2i$ \\
$1+i$ & 0 & $2+i$ & $1+2i$ & $1+i$ & $2i$ & 2 & $2+2i$ & 1 & $i$ \\
$1+2i$ & 0 & $1+i$ & $2+2i$ & $1+2i$ & 2 & $i$ & $2+i$ & $2i$ & 1 \\
2 & 0 & $2i$ & $i$ & 2 & $2+2i$ & $2+i$ & 1 & $1+2i$ & $1+i$ \\
$2+i$ & 0 & $2+2i$ & $1+i$ & $2+i$ & 1 & $2i$ & $1+2i$ & $i$ & 2 \\
$2+2i$ & 0 & $1+2i$ & $2+i$ & $2+2i$ & $i$ & 1 & $1+i$ & 2 & $2i$ \\
\bottomrule
\end{tabular}
    a. There are no zero-divisors in $\mathbb Z_3[i]$.
    a. Every nonzero element in $\mathbb Z_3[i]$ have a multiplicative inverse.
    a. $\mathbb Z_3[i]$ is a field.

# 16.7

> **Theorem 16.7.** Suppose $a$ is nonzero in $\mathbb Z[i]$, $p$ is a prime integer, $a$ and $p$ are relatively prime in $\mathbb Z[i]$. There exist Gaussian integers $r$ and $s$ such that $ar-ps=1$. In particular, if $p$ is irreducible in $\mathbb Z[i]$, and $p$ does not divide $a$, then there exist Gaussian integers $r$ and $s$ such that $ar-ps=1$.

Since $\mathbb Z[i]$ is a Euclidean ring, by Theorem 15.14, there exist Gaussian integers $r$ and $s$ such that $ar-ps=1$.

# 16.8

> **Theorem 16.8.** Given a prime number $p$, ring $\mathbb Z_p[i]$ is a field iff $p$ is irreducible in $\mathbb Z[i]$.

1. Assume $p$ is irreducible in $\mathbb Z[i]$. Let $c+di$ be a nonzero element in $\mathbb Z_p[i]$ with $c,d\in\mathbb Z_p$. We will prove $c+di$ has a multiplicative inverse in $\mathbb Z_p[i]$.
    1. Assume $c\ne0$ and $d=0$. Since $c\in\mathbb Z_p$, we have $c^{-1}c=1$ with $c^{-1}\in\mathbb Z_p$, which implies $c$ has a multiplicative inverse in $\mathbb Z_p[i]$.
    1. Assume $c=0$ and $d\ne0$. Since $d\in\mathbb Z_p$, we have $d^{-1}d=1$ with $d^{-1}\in\mathbb Z_p$, which implies $\left(-d^{-1}i\right)(di)=1$, which implies $di$ has a multiplicative inverse in $\mathbb Z_p[i]$.
    1. Assume $c\ne0$ and $d\ne0$.
        1. If $p\mid(c+di)$ in $\mathbb Z[i]$, there would be $\alpha,\beta\in\mathbb Z$ satisfying $c+di=(\alpha+\beta i)p$, which implies $c+di=0$ in $\mathbb Z_p[i]$, contradicting the assumption $c\ne0$ and $d\ne0$. Therefore, $p\nmid(c+di)$ in $\mathbb Z[i]$.
        1. Given $p\nmid(c+di)$ and $p$ is irreducible in $\mathbb Z[i]$, $p$ and $c+di$ are relatively prime in $\mathbb Z[i]$, which by Theorem 16.7 implies $(c+di)r-ps=1$ with $r,s\in\mathbb Z[i]$, which implies $([c]+[d]i)[e]=1$ in $\mathbb Z_p[i]$, which implies $c+di$ has a multiplicative inverse in $\mathbb Z_p[i]$.
    1. Therefore, $c+di$ has a multiplicative inverse in $\mathbb Z_p[i]$.
1. Assume ring $\mathbb Z_p[i]$ is a field. We will prove $p$ is irreducible in $\mathbb Z[i]$ by contradiction.
    1. Assume $p$ is reducible, i.e., $p=(a+bi)(c+di)$ with nonzero Gaussian integers $a+bi$ and $c+di$, which implies $0=([a]+[b]i)([c]+[d]i)$, which implies $\mathbb Z_p[i]$ has zero-divisors, contradicting the assumption $\mathbb Z_p[i]$ is a field. Therefore, the assumption is false, i.e., $p$ is irreducible in $\mathbb Z[i]$.

# 16.10

> **Theorem 16.11.** A prime number $p$ is irreducible in $\mathbb Z[i]$ iff polynomial $x^2+1$ is irreducible in $\mathbb F_p[x]$.

Given $p$ is prime, we have
\begin{align*}
& p\text{ is irreducible in }\mathbb Z[i] \\
\xLeftrightarrow{\text{Theorem 16.8}}& \text{ring }\mathbb F_p[i]\text{ is a field} \\
\xLeftrightarrow{\text{Theorem 16.10}}& \mathbb F_p[x]_{x^2+1}\text{ is a field} \\
\xLeftrightarrow{\text{Theorem 14.11}}& x^2+1\text{ is irreducible in }\mathbb F_p[i]
\end{align*}

# 16.11

> **Theorem 16.13.** For a prime number $p$, either
>
> 1. equation $x^2+y^2=p$ has no integer solutions;
> 1. $p$ is irreducible in $\mathbb Z[i]$;
> 1. $x^2+1$ is irreducible in $\mathbb F_p[x]$; and
> 1. $-1$ is not a square in $\mathbb F_p$;
>
> or
>
> 1. equation $x^2+y^2=p$ has integer solutions;
> 1. $p$ factors nontrivially in $\mathbb Z[i]$;
> 1. $x^2+1$ factors nontrivially in $\mathbb F_p[x]$; and
> 1. $-1$ is a square in $\mathbb F_p$.

1. $p$ is irreducible in $\mathbb Z[i]\xLeftrightarrow{\text{Theorem 16.6}}$ equation $x^2+y^2=p$ has no integer solutions.
1. $p$ is irreducible in $\mathbb Z[i]\xLeftrightarrow{\text{Theorem 16.11}}$ polynomial $x^2+1$ is irreducible in $\mathbb F_p[x]$.
1. $p$ is irreducible in $\mathbb Z[i]\xLeftrightarrow{\text{Theorem 16.12}}$ $-1$ is not a square in $\mathbb F_p$.

# 16.12

> **Theorem 16.15.** Suppose $p$ is a prime number satisfying $p\equiv1\pmod4$.
>
> 1. Equation $x^2+y^2=p$ has integer solutions, $p$ factors nontrivially in
$\mathbb Z[i]$, polynomial $x^2+1$ factors nontrivially in $\mathbb F_p[x]$, and $-1$ is a square in $\mathbb F_p$.
> 1. There are eight solutions to equation $x^2+y^2=p$. Each solution $(a,b)$ corresponds to a pair of irreducible Gaussian integers $a+bi$ and $a-bi$ such that $p=(a+bi)(a-bi)$.

1. Given $p$ is prime and $p\equiv1\pmod4$, by Theorem 6.1, equation $x^2+y^2=p$ has integer solutions, which by Theorem 16.13 implies $p$ factors nontrivially in $\mathbb Z[i]$, polynomial $x^2+1$ factors nontrivially in $\mathbb F_p[x]$, and $-1$ is a square in $\mathbb F_p$.
1. Let $(a+bi)(a-bi)$ be a factorization of $p$, according to the Unique Factorization Theorem of Gaussian integers, all factorizations of $p$ are $(a+bi)(a-bi)$, $(-a-bi)(-a+bi)$, $(ai-b)(-ai-b)$, and $(-ai+b)(ai+b)$, which corresponds to all solutions to $a^2+b^2=p$, namely $(\pm a,\pm b)$, $(\pm b,\pm a)$.

# 16.13

> **Theorem 16.16.** Suppose $p$ is a prime number satisfying $p\equiv3\pmod4$. Then equation $x^2+y^2=p$ has no integer solutions, $p$ is irreducible in $\mathbb Z[i]$, polynomial $x^2+1$ is irreducible in $\mathbb F_p[x]$, and $-1$ is not a square in $\mathbb F_p$.

Given $p$ is a prime number satisfying $p\equiv3\pmod4$, by Theorem 13.6, $[-1]$ is not a square in $\mathbb{F}_p$, which by Theorem 16.13 implies that equation $x^2+y^2=p$ has no integer solutions, $p$ is irreducible in $\mathbb Z[i]$, and polynomial $x^2+1$ is irreducible in $\mathbb F_p[x]$.
