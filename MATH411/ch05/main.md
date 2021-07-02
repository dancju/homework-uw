---
title: MATH 411, 2021 Summer, Chapter 5
...

# 5.1

1. Integer 2 is prime.
1. Assume every integer from 2 to $k$ is either a prime number or a product of a finite number of prime numbers. If $k+1$ is not prime, then $k+1=rs$ for some integers $r$ and $s$ between 2 and $k$. By assumption, each of $r$ and $s$ is either a prime number or a product of a finite number of prime numbers, implying $k+1$ is a product of a finite number of prime numbers. Therefore, if each of the integers between 2 and $k$ is either a prime number or a product of a finite number of prime numbers, so is $k+1$.
1. By the principle of induction, every integer greater than or equal to 2 is prime number or a product of a finite number of prime numbers.

# 5.2

Suppose $n$ factors as $rs$. If $r\le\sqrt n$, then $n$ has a prime divisor (a prime divisor of $r$) that is less than or equal to $\sqrt n$; if $r>\sqrt n$, or $s<\sqrt n$, then $n$ has a prime divisor (a prime divisor of $s$) that is less than or equal to $\sqrt n$. Therefore, $n$ has a prime divisor that is less than or equal to $\sqrt n$.

# 5.3

1. Consider this lemma: if a positive integer $m$ divides integers $a$ and $a+1$, then $m$ equals 1. Since $m$ divides integers $a$ and $a+1$, $m$ also divides $(a+1)-a=1$. Since 1 is the only positive integer that divides 1, $m$ equals 1.
1. For integer $n=1$, there are at least $n$ distinct prime numbers, since there is 1 prime number, such as 2.
1. Assume there are at least $k$ distinct prime numbers, $p_1,\dots,p_k$. Let $\ell=(p_1\cdots p_k)+1$. Since each of $p_1,\dots,p_k$ is a divisor of $\ell-1$, by the lemma above, we have that none of $p_1,\dots,p_k$ is a divisor of $\ell$. Therefore, $\ell$ has a prime divisor distinct from $p_1,\dots,p_k$. Therefore, there are at least $k+1$ prime numbers.
1. By the principle of induction, for every positive integer $n$, there are at least $n$ distinct prime numbers. In other words, there are infinite number of prime numbers.

# 5.4

Consider the case that $p$ does not divide $b$. Given $p$ is prime, we know $p$ and $b$ are relatively prime. Given $p$ divides $bc$, by Theorem 3.4, $p$ divides $c$. Therefore, $p$ divides either $b$ or $c$.

# 5.5

1. When $n=2$, we know that $p$ divides $a_1\cdots a_n$ since it would be equivalent to Theorem 5.6.
1. Assume $p\mid a_1\cdots a_k$ implies $p$ divides some factor among $a_1,\dots a_k$. Let $a_{k+1}$ be an integer such that $p\mid a_1\cdots a_{k+1}$. By Theorem 5.6, $p$ divides either $a_1\cdots a_k$ or $a_{k+1}$. If $p\mid a_1\cdots a_k$, by assumption, $p$ divides some factor among $a_1,\dots a_k$. Otherwise, $p\mid a_{k+1}$. Either way, $p$ divides some factor among $a_1,\dots a_{k+1}$. Therefore, if $p\mid a_1\cdots a_k$ implies $p$ divides some factor among $a_1,\dots a_k$, $p\mid a_1\cdots a_{k+1}$ also implies $p$ divides some factor among $a_1,\dots a_{k+1}$.
1. By the principle of induction, for every integer $n\ge2$, if $p\mid a_1\cdots a_n$, then $p$ divides some factor $a_i$.

# 5.6

1. Since $p_1\cdots p_m=q_1\cdots q_n$, $p_m$ divides $q_1\cdots q_n$. By Theorem 5.7, there exists an index $j$ for which $p_m$ divides $q_j$. Since both $p_m$ and $q_j$ are prime, $p_m$ equals $q_j$.
1. Assume $p_1\le\cdots\le p_m$ and $q_1\le\cdots\le q_n$. Since $p_m=q_j$ and $q_j\le q_n$, we have $p_m\le q_n$. Similarily, we have $q_n\le p_m$. Therefore, $q_n=p_m$, indicating that $p_1\cdots p_{m-1}=q_1\cdots q_{n-1}$.

# 5.7

1. Consider the case that $m=1$. In this case, $a=p_1$, so that $a$ is a prime number. According to the definition, a prime number does not factor as a product of two prime numbers or more, which implies $n=1$ and $a=q_1$. Therefore, $m=n=1$ and $a=p_1=q_1$.
1. Assume the fundamental theorem of arithmetic is true for $m$, that is, for every positive integer that has a prime factorization of length $m$, the factorization is unique. Consider a positive integer having a prime factorization of length $m+1$ such that $a=p_1\cdots p_{m+1}$. Suppose it has another factorization of length $n+1$ such that $a=q_1\cdots q_{n+1}$. According to the proposition proved in Exercise 5.6, we have $p_{m+1}=q_{n+1}$ and $p_1\cdots p_m=q_1\cdots q_n$. By assumption, we have $m=n$ and $p_i=q_i$ for every index $i\in\{1,\dots,m\}$. Therefore, the fundamental theorem of arithmetic is true for $m+1$.
<!-- 1. By the principle of induction, the fundamental theorem of arithmetic is true for every integer having a prime factorization of positive integral length. -->
1. By the principle of induction, the fundamental theorem of arithmetic is true for every positive integer.

# 5.8

Assume there exists an integer $c=p_1^{k_1}\cdots p_r^{k_r}$ such that $c\mid a$, $c\mid b$, and $c>p_1^{\min(e_1,f_1)}\cdots p_r^{\min(e_r,f_r)}$. Since $c\mid a$ and $c\mid b$, by Proposition 5.8, $k_i\le e_i$ and $k_i\le f_i$ holds for every index $i$, implying $c\le p_1^{\min(e_1,f_1)}\cdots p_r^{\min(e_r,f_r)}$, contradicting the assumption. Therefore, the assumption must be wrong, implying there does not exist an integer $c$ being a common divisor of $a$ and $b$ while greater than $p_1^{\min(e_1,f_1)}\cdots p_r^{\min(e_r,f_r)}$. Therefore, the greatest common divisor of $a$ and $b$ is $p_1^{\min(e_1,f_1)}\cdots p_r^{\min(e_r,f_r)}$.

# 5.9

Assume there exists an integer $c=p_1^{k_1}\cdots p_r^{k_r}$ such that $a\mid c$, $b\mid c$, and $c<p_1^{\max(e_1,f_1)}\cdots p_r^{\max(e_r,f_r)}$. Since $a\mid c$ and $b\mid c$, by Proposition 5.8, $k_i\ge e_i$ and $k_i\ge f_i$ holds for every index $i$, implying $c\ge p_1^{\max(e_1,f_1)}\cdots p_r^{\max(e_r,f_r)}$, contradicting the assumption. Therefore, the assumption must be wrong, implying there does not exist an integer $c$ being a common multiple of $a$ and $b$ while less than $p_1^{\max(e_1,f_1)}\cdots p_r^{\max(e_r,f_r)}$. Therefore, the least common multiple of $a$ and $b$ is $p_1^{\max(e_1,f_1)}\cdots p_r^{\max(e_r,f_r)}$.

# 5.10

It is evident $x+y=\min(x,y)+\max(x,y)$ or $z^xz^y=z^{\min(x,y)}z^{\max(x,y)}$ for every real numbers $x$, $y$, and $z$. Multiplying $p_i^{e_i}p_i^{f_i}=p_i^{\min(e_i,f_i)}p_i^{\max(e_i,f_i)}$ from $i=1$ to $r$ yields $$p_1^{e_1}\cdots p_r^{e_r}\cdot p_1^{f_1}\cdots p_r^{f_r}=p_1^{\min(e_1,f_1)}\cdots p_r^{\min(e_r,f_r)}\cdot p_1^{\max(e_1,f_1)}\cdots p_r^{\max(e_r,f_r)}\,,$$ or $ab=(a,b)\times[a,b]$, or $[a,b]=\frac{ab}{(a,b)}$.

Since $[a,b]=\frac{ab}{(a,b)}$ holds, and $(a,b)$ can be found with the Euclidean algorithm, we can find the least common multiple $[a,b]$ of any positive integers $a$ and $b$ without prime factorizing.
