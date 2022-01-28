---
title: MATH 411, 2021 Summer, Chapter 7
...

# 7.1

1. $x=6$.
1. $x=5$.
1. There is no solution since 6 does not have a multiplicative inverse in $\mathbb Z_{12}$.
1. $x=8$.

# 7.2

Given $a$ is a unit in $R$, its multiplicative inverse $a^{-1}$ exists. Multiplying $a^{-1}$ through $ab=ac$ yields $a^{-1}(ab)=a^{-1}(ac)$. Since $R$ is a ring, it is associative for multiplication, we have $(a^{-1}a)b=(a^{-1}a)c$ or $b=c$.

# 7.3

1. Given unit $u$ and elements $r$, $s$ of ring $R$, if $r\ne s$, then $ur\ne us$.
1. Suppose $r_1,\dots,r_t$ is a complete list of ring $R$, i.e., any pair $(r_i,r_j)$ does not equal. By the proposition above, any pair $(ur_i,ur_j)$ does not equal neither. In other words, list $ur_1,\dots,ur_t$ does not have duplicative elements. Since $R$ has $t$ elements, $ur_1,\dots,ur_t$ is a complete list of $R$.
1. If $a$ is not a unit of $R$, then $ar_1,\dots,ar_t$ may not be a complete list of the elements of $R$. For example, the elements of $\mathbb Z_4$ are $0,1,2,3$. Suppose $a=2$, then $ar_1,\dots,ar_t$ would be $0,2,0,2$ having duplicative elements.

# 7.4

1. Suppose $\gcd(a,m)=1$, which gives $[a]$ is a unit in $\mathbb Z_m$. Therefore, the multiplication by $a$ shuffles the elements of $\mathbb Z_m$.
1. Therefore, $[0],[a],\dots,[(m-1)a]$ is a complete list of the elements of $\mathbb Z_m$.
1. Every integer in the list $0,a,\dots,(m-1)a$ is congruent modulo $m$ to exactly one of the integers $0,1,\dots,m-1$.
1. Therefore, $0,a,\dots,(m-1)a$ is a complete list of congruence class representatives modulo $m$. Thus, if $\gcd(a,m)=1$, then the multiplication by $a$ shuffles the congruence classes modulo $m$.

# 7.5

Suppose $x$ is a real number and $n$ is a positive integer.

1. Assume $x>1$. Multiplying $n$ same inequalities $x>1$ yields $x^n>1$. Therefore, there is no positive integer $n$ for which $x^n=1$.
1. Assume $0<x<1$. Multiplying $n$ same inequalities $x<1$ yields yields $x^n<1$. Therefore, there is no positive integer $n$ for which $x^n=1$.
1. Therefore, the only positive integer $x$ satisfying $x^n=1$ is 1.
1. Assume $x<0$ and $x^n=1$. A negative real number raised to the power of a odd integer is negative. Given $x<0$ and $x^n=1$, $n$ is even. Let $n=2k$. We have $(x^2)^n=1$. Since $x^2>0$, by the proposition proved above, we have $x^2=1$, or $x=-1$.
1. Therefore, 1 and $-1$ are the only integer $n$ for which $x^n=1$.

Thus 1 and $-1$ are the only roots of unity in $\mathbb R$.

# 7.6

1. $\left(\cos0+i\sin0\right)^2=1^2=1. \\
    \left(\cos\pi+i\sin\pi\right)^2=(-1)^2=1.$
1. $\left(\cos0+i\sin0\right)^3=1^3=1. \\
    \left(\cos\frac{2\pi}3+i\sin\frac{2\pi}3\right)^3=\left(-\frac12+\frac{\sqrt3}2i\right)^3=1. \\
    \left(\cos\frac{4\pi}3+i\sin\frac{4\pi}3\right)^3=\left(-\frac12-\frac{\sqrt3}2i\right)^3=1.$
1. $\left(\cos0+i\sin0\right)^4=1^4=1. \\
    \left(\cos\frac{2\pi}4+i\sin\frac{2\pi}4\right)^4=i^4=1. \\
    \left(\cos\frac{4\pi}4+i\sin\frac{4\pi}4\right)^4=(-1)^4=1. \\
    \left(\cos\frac{6\pi}4+i\sin\frac{6\pi}4\right)^4=(-i)^4=1.$
1. $\left(\cos0+i\sin0\right)^6=1^6=1. \\
    \left(\cos\frac{2\pi}6+i\sin\frac{2\pi}6\right)^6=\left(\frac12+\frac{\sqrt3}2i\right)^6=1. \\
    \left(\cos\frac{4\pi}6+i\sin\frac{4\pi}6\right)^6=\left(-\frac12+\frac{\sqrt3}2i\right)^6=1. \\
    \left(\cos\frac{6\pi}6+i\sin\frac{6\pi}6\right)^6=(-1)^6=1. \\
    \left(\cos\frac{8\pi}6+i\sin\frac{8\pi}6\right)^6=\left(-\frac12-\frac{\sqrt3}2i\right)^6=1. \\
    \left(\cos\frac{10\pi}6+i\sin\frac{10\pi}6\right)^6=\left(\frac12-\frac{\sqrt3}2i\right)^6=1.$

# 7.7

1. Supposing $u$ a $v$ are units in $R$, their inverses $u^{-1}$ and $v^{-1}$ exist. By the associative of multiplication of $R$, we have $(v^{-1}u^{-1})(uv)=1$, or $uv$ is a unit.
1. Generally, if $u_1,\dots,u_t$ are units in $R$, then their inverses $u_1^{-1},\dots,u_t^{-1}$ exist. By the associative of multiplication of $R$, we have $$(u_{t}^{-1}\cdots u_1^{-1})(u_1\cdots u_t)=1,$$ or the product $u_1\cdots u_t$ is a unit.
1. In particular, if $u$ is a unit and $t$ is a positive integer, then $u^t$ is a unit.
1. Suppose $R$ has $t$ units and $u$ is one of them. By the proposition proved above, each of $1,u,\dots,u^t$ is a unit. Given $R$ has $t$ units and $1,u,\dots,u^t$ has $t+1$ elements, by the pigeonhole principle, at least two of them are equal. Let them be $u^i$ and $u^j$ with $0\le i<j\le t$, we have $u^i=u^j$ and $u^iu^{j-i}=u^j$, or $u^{j-i}=1$. Given $0\le i<j\le t$, we have $1\le j-i\le t$. Thus, for ring $R$ having $t$ units and $u$ being one of them, there exists some integer $n$ with $1\le n\le t$ satisfying $u^n=1$.

# 7.8

\begin{tabular}{lllr}
\toprule
$\mathbb Z_m$    & Units                      & Order                      & $e$ \\
\midrule
$\mathbb Z_2$    & 1                          & 1                           &  1 \\
$\mathbb Z_3$    & 1,2                        & 1,2                         &  2 \\
$\mathbb Z_4$    & 1,3                        & 1,2                         &  2 \\
$\mathbb Z_5$    & 1,2,3,4                    & 1,4,4                       &  4 \\
$\mathbb Z_6$    & 1,5                        & 1,2                         &  2 \\
$\mathbb Z_7$    & 1,2,3,4,5,6                & 1,3,6,3,6,2                 &  6 \\
$\mathbb Z_8$    & 1,3,5,7                    & 1,2,2,2                     &  4 \\
$\mathbb Z_9$    & 1,2,4,5,7,8                & 1,6,3,6,3,2                 &  6 \\
$\mathbb Z_{10}$ & 1,3,7,9                    & 1,4,4,2                     &  4 \\
$\mathbb Z_{11}$ & 1,2,3,4,5,6,7,8,9,10       & 1,10,5,5,5,10,10,10,5,2     & 10 \\
$\mathbb Z_{12}$ & 1,5,7,11                   & 1,2,2,2                     &  4 \\
$\mathbb Z_{13}$ & 1,2,3,4,5,6,7,8,9,10,11,12 & 1,12,3,6,4,12,12,4,3,6,12,2 & 12 \\
\bottomrule
\end{tabular}

Every unit $u$ in $\mathbb Z_m$ satisfies $u^{\phi_m}=1$. For prime integer $m$, every unit $u$ in $\mathbb Z_m$ satisfies $u^{m-1}=1$.

# 7.9

Since $\mathbb Z_p$ has $p-1$ units, by Theorem 7.8, every unit $u$ in $\mathbb Z_p$ satisfies $u^{p-1}=1$, which is equivalent to Fermat's theorem. Thus, Fermat's theorem is a special case of Theorem 7.8.

1. Suppose ring $R$ has $t$ units, $u_1,\dots,u_t$, and $u$ is one of them. By the theorem that multiplication by a unit shuffles a list of units, we have $uu_1,\dots,uu_t$ is also a complete list of the units of $R$.
1. Given $u_1,\dots,u_t$ and $uu_1,\dots,uu_t$ is the same list with different order, we have $u_1\cdots u_t=(uu_1)\cdots(uu_t)$. Since $\mathbb Z_p$ is associative and commutative for multiplication, we have $u^t=1$.

Thus, for a ring with $t$ units, every unit $u$ satisfies $u^t=1$.

# 7.10

1. Assume $m$ is a prime number and $a$ is a positive integer. Hence, $\mathbb Z_m$ is a ring with $m-1$ units and $a$ is one of them. By Theorem 7.8, we have $a^{m-1}\equiv1\pmod m$.
1. We have proved that $m$ is prime implies $a^{m-1}\equiv1\pmod m$. Hence, its contrapositive, which is Proposition 7.10, is also proved.

\begin{align*}
2^{1}\equiv2\pmod{511} \\
2^{2}\equiv4\pmod{511} \\
2^{4}\equiv16\pmod{511} \\
2^{8}\equiv256\pmod{511} \\
2^{16}\equiv128\pmod{511} \\
2^{32}\equiv32\pmod{511} \\
2^{64}\equiv2\pmod{511} \\
2^{128}\equiv4\pmod{511} \\
2^{256}\equiv16\pmod{511}
\end{align*}

$2^{510}\equiv2^{256+128+64+32+16+8+4+2}\equiv16\times4\times2\times32\times128\times256\times16\times4\equiv64\pmod{511}$

By Proposition 7.10, integer 511 is not prime.

# 7.11

1. Assume $p$ is prime and $e$ is a positive integer. Consider the set $A=\{1,2,\dots,p^e\}$. Split $A$ into two disjoint sets $B=\{p,2p,\dots,p^e\}$ and $C=A\setminus B$.
1. Every element in $A$ is not coprime to $p^e$ since they have mutual prime factor $p$. Every element in $B$ is coprime they do not have mutual prime factors.
1. Set $B$ has $p^{e-1}$ elements while set $C$ has $p^e-p^{e-1}$ elements.

Thus, for prime number $p$ and positive integer $e$, we have $\phi(p^e)=p^e-p^{e-1}$.

# 7.12

1. Since $p^e$ and $q^f$ are coprime, by Theorem 7.11, we have $\phi(p^eq^f)=\phi(p^e)\phi(q^f)=(p^e-p^{e-1})(q^f-q^{f-1})$.
1. $\phi(1728)=\phi(2^6\times3^3)=(2^6-2^5)(3^3-3^2)=576$.
1. $\phi(p_1^{e_1}\cdots p_r^{e_r})=(p_1^{e_1}-p_1^{e_1-1})\cdots(p_r^{e_r}-p_r^{e_r-1})$.
1. $\phi(60)=16,\phi(900)=240,\phi(7875)=3600$.
