---
title: MATH 411, 2021 Summer, Chapter 4
...

# 4.1

$3\equiv123\pmod5$ since 3 and 123 have the same remainder 3 upon division by 5.

$42\not\equiv88\pmod{17}$ since 42 and 88 have different remainder upon division by 17.

An even integer can not be congruent to an odd integer modulo 2 since their remainder would be 0 and 1.

# 4.2

1. Firstly, we will show that if $m$ divides $a-b$, then $r_0$ equals $r_1$, where $r_0$ and $r_1$ are the remainders of $a$ and $b$ upon division by $m$.
    1. Given that $m$ divides $a-b$, there exists an integer $t$ such that $a-b=mt$.
    1. According to the division theorem, there exist integers $q_0$ and $q_1$ such that $$a=mq_0+r_0\,,\quad0\le r_0<m\,,\quad b=mq_1+r_1\,,\quad0\le r_1<m\,.$$
    1. Substituting $a=mq_0+r_0$ and $b=mq_1+r_1$ into $a-b=mt$ yields $r_0-r_1=(t-q_0+q_1)m$.
    1. Given $0\le r_0<m$ and $0\le r_1<m$, we have $-m<r_0-r_1<m$.
    1. Being a multiple of $m$ and strictly between $-m$ and $m$, $r_0-r_1$ could only be 0, indicating that $r_0=r_1$.
1. Secondly, we will show that if $r_0$ equals $r_1$, where $r_0$ and $r_1$ are the remainders of $a$ and $b$ upon division by $m$, then $m$ divides $a-b$.
    1. According to the division theorem, there exist integers $q_0$ and $q_1$ such that $$a=mq_0+r_0\,,\quad0\le r_0<m\,,\quad b=mq_1+r_1\,,\quad0\le r_1<m\,.$$
    1. Substituting $a=mq_0+r_0$ and $b=mq_1+r_1$ into $r_0=r_1$ yields $a-b=(q_0-q_1)m$, indicating that $m$ divides $a-b$.

# 4.3

> **Theorem 4.1.** Let $m$ be an integer greater than 1. Every integer $a$ is congruent modulo $m$ to exactly one of the integers $0,1,\dots,m-1$.

1. According to the Division Theorem, there exists a non-negative integer less than $m$ that is the remainder of $a$ upon division by $m$. Therefore, every integer $a$ is congruent modulo $m$ to at least one of the integers $0,1,\dots,m-1$.
1.  1. Suppose there are two integers $r$ and $s$ between 0 and $m-1$ that are congruent to $a$ modulo $m$.
    1. Since $r$ and $s$ are congruent to $a$, we have $r\equiv a\pmod m$ and $s\equiv a\pmod m$, implying that $m$ divides both $a-r$ and $a-s$, or $m$ divides $r-s$.
    1. Since $r$ and $s$ are both between 0 and $m-1$, $r-s$ is strictly between $-m$ and $m$.
    1. Being a multiple of $m$ and strictly between $-m$ and $m$, $r-s$ could only be 0. Therefore, any two integers between 0 and $m-1$ that are congruent to $a$ modulo $m$ are the same integer.

# 4.4

Given $a\equiv b\pmod m$, it is evident that $a^1\equiv b^1\pmod m$.

Assume $a^k\equiv b^k\pmod m$ for positive integer $k$, since $a\equiv b\pmod m$, by Proposition 4.3, we have $a^{k+1}\equiv b^{k+1}\pmod m$.

We have shown $a^1\equiv b^1\pmod m$. We have also shown under the assumption of $a^k\equiv b^k\pmod m$ for positive integer $k$, we have $a^{k+1}\equiv b^{k+1}\pmod m$. By the principle of induction, we can conclude that $a^n\equiv b^n\pmod m$ for every positive integer $n$.

# 4.5

1. $2^{82}\equiv2^{4\times20+2}\equiv1^{20}2^2\equiv4\pmod 5$
1. $3^{1502}\equiv3^{3\times500+2}\equiv1^{500}3^2\equiv9\pmod{13}$
1. $5^{1004}\equiv5^{6\times167+2}\equiv1^{167}5^2\equiv4\pmod 7$
1. $6^{13334451}\equiv6^{2n+1}\equiv1^n6^1\equiv6\pmod 7$

# 4.6

Given $ra\equiv rb\pmod m$, we have $m$ divides $(a-b)r$. Since $r$ and $m$ are relatively prime integers, by Theorem 3.4, we have $m$ divides $a-b$, implying $a\equiv b\pmod m$.

# 4.7

1. Solving $1x\equiv1\pmod5$ yields $x=5k+1$.
1. Solving $2x\equiv1\pmod5$ yields $x=5k+3$.
1. Solving $3x\equiv1\pmod5$ yields $x=5k+2$.
1. Solving $4x\equiv1\pmod5$ yields $x=5k+4$.
1. Solving $1x\equiv1\pmod6$ yields $x=6k+1$.
1. Solving $2x\equiv1\pmod6$ yields $x\in\emptyset$.
1. Solving $3x\equiv1\pmod6$ yields $x\in\emptyset$.
1. Solving $4x\equiv1\pmod6$ yields $x\in\emptyset$.
1. Solving $5x\equiv1\pmod6$ yields $x=6k+5$.
1. Solving $1x\equiv1\pmod7$ yields $x=7k+1$.
1. Solving $2x\equiv1\pmod7$ yields $x=7k+4$.
1. Solving $3x\equiv1\pmod7$ yields $x=7k+5$.
1. Solving $4x\equiv1\pmod7$ yields $x=7k+2$.
1. Solving $5x\equiv1\pmod7$ yields $x=7k+3$.
1. Solving $6x\equiv1\pmod7$ yields $x=7k+6$.

# 4.8

> **Theorem 4.6.** Let $a$ and $m$ be positive integers with $m>1$. The congruence $ax\equiv1\pmod m$ is solvable iff $(a, m)=1$.

1. Suppose the congruence equation $ax\equiv1\pmod m$ is solvable. Letting $d$ be a positive integer dividing both $a$ and $m$, there exist integers $u$ and $v$ such that $a=du$ and $m=dv$. Substituting into the equation, we know that $dux\equiv1\pmod{dv}$ is solvable. By the definition of congruence, there exist an integer $w$ such that $dux-1=dvw$, or $1=(ux-vw)d$, implying $d$ divides 1. Since $d$ is a positive integer, $d$ is 1. Therefore, the only positive integer dividing both $a$ and $m$ is 1. That is, $(a,m)=1$.
1. Suppose $(a,m)=1$. By Bézout's theorem, there exist integers $u$ and $v$ such that $1=au+mv$, which implies $au\equiv1\pmod m$. Hence, $ax\equiv1\pmod m$ is solvable.

# 4.9

> **Theorem 4.7.** Let $a,e$, and $m$ be positive integers with $m>1$. The congruence $ax\equiv e\pmod m$ is solvable iff $(a, m)|e$.

1. Suppose $ax\equiv e\pmod m$ is solvable. There exists an integer $s$ such that $ax-e=ms$, or $ax+ms=e$ is solvable. By Theorem 3.11, $(a,m)$ divides $e$.
1. Suppose $(a,m)$ divides $e$. By Theorem 3.11, there exist integers $s$ and $t$ such that $as+mt=e$ is solvable. Hence, $ax\equiv e\pmod m$ is solvable.

# 4.10

$8x\equiv1\pmod6$ is not solvable since $(8,6)=2$ does not divide 1.

$8x\equiv4\pmod6$ yields $x=3k+2$.

$15x\equiv1\pmod{21}$ is not solvable since $(15,21)=3$ does not divide 1.

$15x\equiv6\pmod{21}$ yields $x=7k+6$.

# 4.11

1. The contrapositive of Theorem 4.9 is true, that is, if $r$ and $s$ are integers that $r\not\equiv s\pmod m$ and $a$ and $m$ are relatively prime, then $ar\not\equiv as\pmod m$.
1. Suppose $s$ and $r$ are different non-negative integers that are less than $m$. Evidently, $r\not\equiv s\pmod m$. Since $a$ and $m$ are relatively prime, by the proposition proved above, we have $ar\not\equiv as\pmod m$. Therefore, for any different non-negative two integers $s$ and $r$ that are less than $m$, we have $ar\not\equiv as\pmod m$. Therefore, there do not exist two integers in the set $\{0,a,2a,\dots,(m-1)a\}$ are congruent modulo $m$.
1. There do not exist two integers in the set lie in the same congruence class.
1. Since there are $m$ congruence classes, and every two integers among the set lie in different congruence classes, we know that the set form a set of congruence class representatives modulo $m$.

# 4.12

1. Integer $ra$ is $(a,m)$-accessible for every positive integer $r$ since it is the sum of multiple $a$-s.
1. Integer $ra+sm$ is also $(a,m)$-accessible for every positive integer $s$ since it is the sum of $ra$ and multiple $m$-s.
1. For every integer $r$ between 0 and $m-1$, all integers greater than or equal to $ra$ in the congruence class $\mathcal C(ra)$ are $(a,m)$-accessible since they are sums of $ra$ and multiple $m$-s.
1. The largest integer that might fail to be $(a,m)$-accessible in the congruence class $\mathcal C(ra)$ is $ra-m$.
1. Since $r<m-1$, the largest integer that might fail to be $(a,m)$-accessible is $(m-1)a-m$, or $N=am-a-m$. That is, every integer greater than $N$ is $(a,m)$-accessible.
1. Assume $x$ is an integer $(a,m)$-accessible and in the congruence class $\mathcal C(ra)$. Since $x$ is $(a,m)$-accessible, there exist non-negative integers $s$ and $t$ such that $x=as+mt$. Since $x$ is in $\mathcal C(ra)$, we have $as+mt\equiv ra\pmod m$, or $as\equiv ra\pmod m$. Since $a$ and $m$ are relatively prime, by Theorem 4.9, we have $s\equiv r\pmod m$. Given $r\le m-1$ and $s\ge0$, we have $s\ge r$. Given $s\ge r$ and $t\ge0$, we have $x=as+mt\ge ar$. Therefore, any integer being $(a,m)$-accessible and in the congruence class $\mathcal C(ra)$ is greater than or equal to $ar$.
