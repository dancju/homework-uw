---
title: MATH 411, 2021 Summer, Chapter 6
...

# 6.1

1. Assume $\sqrt 2$ is rational, implying that there exists an integer $m$ and an positive integer $n$ such that $\sqrt 2=\frac mn$. If $m$ and $n$ are not coprime, integer $\frac m{\gcd(m,n)}$ and positive integer $\frac n{\gcd(m,n)}$ could replace $m$ and $n$. Hence, we can assume $m$ and $n$ are coprime.
1. Square both sides of $\sqrt 2=\frac m n$ yields $2n^2=m^2$. Since $2|m^2$ and 2 is prime, by Theorem 5.6, we have $2|m$. Assume $m=2a$ with integer $a$. Substituting $m=2a$ into $2n^2=m^2$ yields $n^2=2a^2$. Since $2|n^2$ and 2 is prime, by Theorem 5.6, we have $2|n$.
1. Given $2|m$ and $2|n$, $m$ and $m$ are not coprime, contradicting the assumption. Therefore, the assumption must be wrong, implying $\sqrt 2$ is not rational.

Similarily, we can prove $\sqrt 3$ is not rational.

# 6.2

Since both includes $\angle{A}$ and a right angle, we have $\triangle{ACB}\sim\triangle{ABD}$. Similarily, we have $\triangle{BCD}\sim\triangle{ABD}$. Therefore, $\triangle{ACB}\sim\triangle{BCD}$, implying $\frac r1=\frac 1s$, or $s$ is a multiplicative inverse of $r$.

# 6.3

Every negative real number $a$ has an additive inverses $-a$, which is a positive real number having a multiplicative inverse $-\frac 1a$, which has an additive inverses $\frac 1a$. Given $\frac 1a$ exists and $\frac 1a\cdot a=1$, every negative real number $a$ has a multiplicative inverse $\frac 1a$.

# 6.4

$(3+5i)(r+si)=(3r-5s)+(3s+5r)i$. Since it is a real number, we have $3s+5r=0$, which has a trivial solution $(r,s)=(3,-5)$, or $r+si=3-5i$.

# 6.5

1. $(a+bi)(a-bi)=a^2+b^2$.
1. $a+bi\ne0\iff a\ne0\lor b\ne0\iff a^2+b^2\in\mathbb R_+\iff(a+bi)(a-bi)\in\mathbb R_+$.
1. $a+bi\ne0\iff(a+bi)\left(\frac a{a^2+b^2}-\frac b{a^2+b^2}i\right)=1$.
1. Every nonzero complex number $a+bi$ has a multiplicative inverse $\frac a{a^2+b^2}-\frac b{a^2+b^2}i$.

# 6.6

1. $\left(a+b\sqrt 2\right)\left(a-b\sqrt 2\right)=a^2-2b^2$ is an integer, since $a$ and $b$ are assumably integers.
1. For every pair of number $a+b\sqrt 2$ and $c+d\sqrt 2$, the sum $\left(a+b\sqrt 2\right)+\left(c+d\sqrt 2\right)=(a+c)+(b+d)\sqrt 2$ and the product $\left(a+b\sqrt 2\right)\left(c+d\sqrt 2\right)=(ac+2bd)+(ad+bc)\sqrt 2$ are also in the set $\mathbb Z\left[\sqrt 2\right]$, since $a+c$, $b+d$, $ac+2bd$, and $ad+bc$ are integers. Therefore, $\mathbb Z\left[\sqrt 2\right]$ is closed under addition and multiplication.

# 6.7

1. Assume $a+b\sqrt 2$ is a unit in $\mathbb Z\left[\sqrt 2\right]$ with multiplicative inverse $c+d\sqrt 2$. By assumption, we have $\left(a+b\sqrt 2\right)\left(c+d\sqrt 2\right)=1$, implying $ac+2bd=1$ and $ad+bc=0$.
1. Given $ac+2bd=1$ and $ad+bc=0$, we have $\left(a-b\sqrt 2\right)\left(c-d\sqrt 2\right)=(ac+2bd)-(ad+bc)\sqrt 2=1$, implying that $a-b\sqrt 2$ is also a unit with the multiplicative inverse $c-d\sqrt 2$.
1. Given that the multiplicative inverses of $a+b\sqrt 2$ and $a-b\sqrt 2$ are $c+d\sqrt 2$ and $c-d\sqrt 2$ respectively, we have $$\left(a+b\sqrt 2\right)\left(a-b\sqrt 2\right)\left(c+d\sqrt 2\right)\left(c-d\sqrt 2\right)=1\,,$$ or $\left(a^2-2b^2\right)\left(c^2-2d^2\right)=1$. Since $a$, $b$, $c$, and $d$ are integers, we know $a^2-2b^2$ divides 1, implying $a^2-2b^2$ equals 1 or $-1$.
1. In summary, if $a+b\sqrt 2$ is a unit in $\mathbb Z\left[\sqrt 2\right]$, then $a^2-2b^2=\pm1$.
1. Conversely, assume $a^2-2b^2=\pm1$ with integers $a$ and $b$. By assumption, we have $\left(a+b\sqrt 2\right)\left(a-b\sqrt 2\right)=a^2-2b^2=\pm1$. Hence, $a+b\sqrt 2$ is a unit in $\mathbb Z\left[\sqrt 2\right]$ with multiplicative inverse $\pm(a-b\sqrt 2)$.
1. For every unit $a+b\sqrt 2$ in $\mathbb Z\left[\sqrt 2\right]$, the integers $a^2$ and $b^2$ satisfy the linear Diophantine equation $a^2-2b^2=1$ or $a^2-2b^2=-1$.
1. Observe that $(1,1)$ and $(3,2)$ are two solutions to either equation, indicating $1+\sqrt 2$ is a unit with inverse $-1+\sqrt 2$ while $3+2\sqrt 2$ is a unit with inverse $3-2\sqrt 2$.
1. Raising through $\left(1+\sqrt 2\right)\left(- 1+\sqrt 2\right)=1$ to the power of positive integer $n$ yields $\left(1+\sqrt 2\right)^n\left(- 1+\sqrt 2\right)^n=1$, implying the inverse of $\left(1+\sqrt 2\right)^n$ is $\left(-1+\sqrt 2\right)^n$. Since $\mathbb Z\left[\sqrt 2\right]$ is closed under multiplication, we know both $\left(1+\sqrt 2\right)^n$ and $\left(-1+\sqrt 2\right)^n$ are in $\mathbb Z\left[\sqrt 2\right]$. Therefore, $\left(1+\sqrt 2\right)^n$ is a unit in $\mathbb Z\left[\sqrt 2\right]$ for every positive integer $n$. By substituting every positive integer $n$, we get infinitely many units in $\mathbb Z\left[\sqrt 2\right]$.
1. Assume $a$ is an even integer $2k$ with integer $k$. We know that $a^2-2b^2=4k^2-2b^2$ is even and can not be 1 or $-1$, implying $a+b\sqrt 2$ can not be a unit in $\mathbb Z\left[\sqrt 2\right]$. Given there are infinitely many even numbers, there are infinitely many numbers in $\mathbb Z\left[\sqrt 2\right]$ that are not units.

# 6.8

1. There are $(2N+1)^2$ numbers $a+b\sqrt 2$ in $\mathbb Z\left[\sqrt 2\right]$ with $-N\le a,b\le N$.
1. Given $a^2-2b^2=\pm1$, we have $|b|=\sqrt{\frac{a^2\mp1}2}$. For a given $a$, there are two possible $|b|$-s. Let them be $|b|_1$ and $|b|_2$, we have
\begin{align*}
& |b|_1-|b|_2 \\
=& \sqrt{\frac{a^2+1}2}-\sqrt{\frac{a^2-1}2} \\
=& \frac1{\sqrt{\frac{a^2+1}2}+\sqrt{\frac{a^2-1}2}} \\
\le& \frac1{\sqrt{\frac{a^2+1}2+\frac{a^2-1}2}} \\
=& \frac1{|a|} \\
\le& 1\,,
\end{align*}
where the equality holds iff $|a|=1$. Therefore, for a $|a|>1$, the two possible $|b|$-s has a distance less than 1, and consequently can not be integers at the same time. Therefore, for a given $a$, there are at most two integer $b$-s. Therefore, there are at most $2(2N+1)$ numbers $a+b\sqrt 2$ with $-N\le a,b\le N$ being units.
1. The proportion of units among the numbers $a+b\sqrt 2$ with $-N\le a,b\le N$ in $\mathbb Z\left[\sqrt 2\right]$ is $\frac{2(2N+1)}{(2N+1)^2}=\frac 2{2N+1}$, which approximately equals to $\frac 1N$ for a sufficiently large $N$.

# 6.9

For every pair of numbers $a+bi$ and $c+di$ in $\mathbb Z[i]$, the sum $(a+bi)+(c+di)=(a+c)+(b+d)i$ and the product $(a+bi)(c+di)=(ac-bd)+(ad+bc)i$ are also in $\mathbb Z[i]$. Therefore, $\mathbb Z[i]$ is closed under addition and multiplication.

# 6.10

1. Assume $a+bi$ is a unit in $\mathbb Z[i]$ with multiplicative inverse $c+di$. By assumption, we have $(a+bi)(c+di)=1$, which implies $ac-bd=1$ and $ad+bc=0$. Therefore, we have $(a-bi)(c-di)=(ac-bd)-(ad+bc)i=1$, implying that $a-bi$ is also a unit with the multiplicative inverse $c-di$.
1. Given that the multiplicative inverse of $a+bi$ and $a-bi$ are $c+di$ and $c-di$ respectively, we have $(a+bi)(a-bi)(c+di)(c-di)=1\,,$ or $(a^2+b^2)(c^2+d^2)=1$. Since $a$, $b$, $c$, and $d$ are integers, we know $a^2+b^2$ divides 1, implying $a^2+b^2=1$.
1. Since $(0,\pm1)$ and $(\pm1,0)$ are the only integer solutions to $a^2+b^2=1$, we know that $\pm1$ and $\pm i$ are the only units in $\mathbb Z[i]$.

# 6.11

All integer solutions to $x^2+y^2=2$ are $(-1,\pm1)$ and $(1,\pm1)$.

1. If $r$ is an even integer $2k$, then $r^2=4k\equiv0\pmod4$. If $r$ is an odd integer $2k+1$, then $r^2=4k^2+4k+1\equiv1\pmod4$. Therefore, every integer is congruent to either 0 or 1 modulo 4.
1. For every pair of integers $a$ and $b$, $a^2+b^2$ is congruent to 0, 1, or 2 modulo 4.
1. Equation $x^2+y^2\equiv3\pmod4$ has no integer solutions.
1. Equation $x^2+y^2=n$ has no integer solutions for every integer $n$ such that $n\equiv3\pmod4$.
1. Equation $x^2+y^2=334 257 891 443 112 355$ has no integer solutions.

# 6.12

1. $(1,2)$ is a solution to $x^2+y^2=5$.
1. $(2,3)$ is a solution to $x^2+y^2=13$.
1. $(1,4)$ is a solution to $x^2+y^2=17$.
1. $(2,5)$ is a solution to $x^2+y^2=29$.
1. $(1,6)$ is a solution to $x^2+y^2=37$.
1. $(4,5)$ is a solution to $x^2+y^2=41$.
1. $(2,7)$ is a solution to $x^2+y^2=53$.
1. $(5,6)$ is a solution to $x^2+y^2=61$.
1. $(3,8)$ is a solution to $x^2+y^2=73$.
1. $(5,8)$ is a solution to $x^2+y^2=89$.

# 6.13

1. If $a^2+b^2=n$, then $n=(a+bi)(a-bi)$, i.e.\ $n$ factors as $(a+bi)(a-bi)$ in $\mathbb Z[i]$.
1. $2=(1+i)(1-i)$
1. The nontrivial factorization of every $p$ in $\mathbb Z[i]$ are listed below.
    1. $5=(1+2i)(1-2i)$.
    1. $13=(2+3i)(2-3i)$.
    1. $17=(1+4i)(1-4i)$.
    1. $29=(2+5i)(2-5i)$.
    1. $37=(1+6i)(1-6i)$.
    1. $41=(4+5i)(4-5i)$.
    1. $53=(2+7i)(2-7i)$.
    1. $61=(5+6i)(5-6i)$.
    1. $73=(3+8i)(3-8i)$.
    1. $89=(5+8i)(5-8i)$.
1. For every prime integer $p$ such that $p\equiv1\pmod4$, by Fermat's theorem, there exists an integer pair (a,b) such that $a^2+b^2=p$, or $p=(a+bi)(a-bi)$. Since $a+bi$ is not a unit in $\mathbb Z[i]$, $(a+bi)(a-bi)$ is a nontrivial factorization. Therefore, for every prime integer $p$ such that $p\equiv1\pmod4$, $p$ has a nontrivial factorization.

# 6.14

1. The orange, or $\mathit0$, is an additive identity, since every fruit added to $\mathit0$, the result is the fruit itself.
1. The banana, or $\mathit1$, is an multiplicative identity, since every fruit multiplied to $\mathit0$, the result is the fruit again.
1. The additive inverse of $\mathit0$, $\mathit1$, and $\mathit2$ are $\mathit0$, $\mathit2$, and $\mathit1$ respectively.

# 6.15

1. $(0+1)+2=0+(1+2)$, $(0+1)+1=0+(1+1)$, $(0+1)+2=0+(1+2)$, $(0\times1)\times2=0\times(1\times2)$, $(0\times1)\times1=0\times(1\times1)$, $(0\times1)\times2=0\times(1\times2)$.
1. $0+1=1+0$, $0+2=0+2$, $1+2=2+1$, $0\times1=1\times0$, $0\times2=0\times2$, $1\times2=2\times1$.
1. $(0+1)\times2=0\times2+1\times2$, $(1+2)\times2=1\times2+2\times2$.
1. Since $1\times1=1$ and $2\times2=1$, we know that 1 and 2 are units, whose multiplicative inverses are 1 and 2 respectively.

# 6.16

1. The additive identity is $\mathit0$.
1. The multiplicative identity is $\mathit1$.
1. Every fruit has an additive inverse, since $\mathit{0+0=0}$, $\mathit{1+3=0}$, and $\mathit{2+2=0}$.

# 6.17

1. The first two rings are fields since every non-zero fruit is a unit.
1. For the third fruit ring,
    a. $a^2=b$, $b^2=a$.
    a. $a^3=1$, $b^3=1$.
    a. $a$ is a unit with multiplicative inverse $b$.
    a. $b$ is a unit with multiplicative inverse $a$.
    a. The ring is a field since every non-zero fruit is a unit.

# 6.18

1.
    a. $2+5=0$,
    a. $3+1+4+2=3$,
    a. $4\times3=5$,
    a. $2\times2=4$,
    a. $3\times4\times6=2$.
1.
\begin{tabular}{r|*{7}r}
    $\times$ & 0 & 1 & 2 & 3 & 4 & 5 & 6 \\
    \midrule
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    1 & 0 & 1 & 2 & 3 & 4 & 5 & 6 \\
    2 & 0 & 2 & 4 & 6 & 1 & 3 & 5 \\
    3 & 0 & 3 & 6 & 2 & 5 & 1 & 4 \\
    4 & 0 & 4 & 1 & 5 & 2 & 6 & 3 \\
    5 & 0 & 5 & 3 & 1 & 6 & 4 & 2 \\
    6 & 0 & 6 & 5 & 4 & 3 & 2 & 1 \\
\end{tabular}
1. According to the table, integer 1 is a multiplicative identity in $\mathbb Z_7$.
1. Every non-zero integer is a unit. The multiplicative inverses of $1,\dots,6$ are 1, 4, 5, 2, 3, 6 respectively.

# 6.19

1.
    a.
\begin{tabular}{r|*{2}r}
    $\times$ & 0 & 1 \\
    \midrule
    0 & 0 & 0 \\
    1 & 0 & 1 \\
\end{tabular}
    a. Integer 1 is the multiplicative identity of $\mathbb Z_2$.
    a. Integer 1 in $\mathbb Z_2$ is unit. Its multiplicative inverse is 1. Ring $\mathbb Z_2$ is a field.
1.
    a.
\begin{tabular}{r|*{3}r}
    $\times$ & 0 & 1 & 2 \\
    \midrule
    0 & 0 & 0 & 0 \\
    1 & 0 & 1 & 2 \\
    2 & 0 & 2 & 1 \\
\end{tabular}
    a. Integer 1 is the multiplicative identity of $\mathbb Z_3$.
    a. Integers 1 and 2 are units. Their multiplicative inverses are 1 and 2. Ring $\mathbb Z_3$ is a field.
1.
    a.
\begin{tabular}{r|*{4}r}
    $\times$ & 0 & 1 & 2 & 3 \\
    \midrule
    0 & 0 & 0 & 0 & 0 \\
    1 & 0 & 1 & 2 & 3 \\
    2 & 0 & 2 & 0 & 2 \\
    3 & 0 & 3 & 2 & 1 \\
\end{tabular}
    a. Integer 1 is the multiplicative identity of $\mathbb Z_4$.
    a. Integer 1 and 3 are units. Their multiplicative inverses are 1 and 3. Ring $\mathbb Z_4$ is not a field.

# 6.20

a.
\begin{tabular}{r|*{12}r}
    $\times$ & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 \\
    \midrule
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
    1 & 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 \\
    2 & 0 & 2 & 4 & 6 & 8 & 10 & 0 & 2 & 4 & 6 & 8 & 10 \\
    3 & 0 & 3 & 6 & 9 & 0 & 3 & 6 & 9 & 0 & 3 & 6 & 9 \\
    4 & 0 & 4 & 8 & 0 & 4 & 8 & 0 & 4 & 8 & 0 & 4 & 8 \\
    5 & 0 & 5 & 10 & 3 & 8 & 1 & 6 & 11 & 4 & 9 & 2 & 7 \\
    6 & 0 & 6 & 0 & 6 & 0 & 6 & 0 & 6 & 0 & 6 & 0 & 6 \\
    7 & 0 & 7 & 2 & 9 & 4 & 11 & 6 & 1 & 8 & 3 & 10 & 5 \\
    8 & 0 & 8 & 4 & 0 & 8 & 4 & 0 & 8 & 4 & 0 & 8 & 4 \\
    9 & 0 & 9 & 6 & 3 & 0 & 9 & 6 & 3 & 0 & 9 & 6 & 3 \\
    10 & 0 & 10 & 8 & 6 & 4 & 2 & 0 & 10 & 8 & 6 & 4 & 2 \\
    11 & 0 & 11 & 10 & 9 & 8 & 7 & 6 & 5 & 4 & 3 & 2 & 1 \\
\end{tabular}
a. Integer 1 is the multiplicative identity of $\mathbb Z_{12}$.
a. Integer 1, 5, 7, and 11 are units. Their multiplicative inverses are 1, 5, 7, and 11 respectively. Ring $\mathbb Z_{12}$ is not a field.

# 6.21

1. By Theorem 4.6, for positive integers $a$ and $m$, equation $ax\equiv1\pmod m$ is solvable iff $\gcd(a,m)=1$.
1. By the difinition of modular rings, $[a]_m$ is a unit in $\mathbb Z_m$ iff equation $ax\equiv1\pmod m$ is solvable.
1. Therefore, $[a]_m$ is a unit in $\mathbb Z_m$ iff $\gcd(a,m)=1$.

# 6.22

1. Observe that the sum of an even integer and an odd integer is odd, the sum of an even integer and an even integer is even, and the sum of an odd integer and an odd integer is even.
1. In other words, the sum of an element from $\mathcal C(0)$ and an element from $\mathcal C(1)$ is in $\mathcal C(1)$, the sum of an element from $\mathcal C(0)$ and an element from $\mathcal C(0)$ is in $\mathcal C(0)$, and the sum of an element from $\mathcal C(1)$ and an element from $\mathcal C(1)$ is in $\mathcal C(0)$.
1. In other words, $\mathcal C(0)+\mathcal C(1)=\mathcal C(1)$, $\mathcal C(0)+\mathcal C(0)=\mathcal C(0)$, and $\mathcal C(1)+\mathcal C(1)=\mathcal C(0)$.
1. Similarily, $\mathcal C(0)\times\mathcal C(1)=\mathcal C(0)$, $\mathcal C(0)\times\mathcal C(0)=\mathcal C(0)$, and $\mathcal C(1)\times\mathcal C(1)=\mathcal C(1)$.
1. The set $\{\mathcal C(0),\mathcal(1)\}$ forms a ring since it is closed under addition and multiplication, associative for multiplication, and distributive for multiplication over addition.
1. This ring is equivalent to $\mathbb Z_2$, with the only difference on symbols, since they have identical addition table and multiplication table.

# 6.23

1. Given $a\in\mathcal C(i)$ and $b\in\mathcal C(j)$, we have $a\equiv i\pmod m$ and $b\equiv j\pmod m$, which implies $a+b\equiv i+j\pmod m$ and $ab\equiv ij\pmod m$, which implies $a+b\in\mathcal C(i+j)$ and $ab\in\mathcal C(ij)$.
1. We can define $\mathcal C(i)+\mathcal C(j)=\mathcal C(i+j)$ and $\mathcal C(i)\times\mathcal C(j)=\mathcal C(ij)$.
1. Since $\mathcal C(i)+\mathcal C(0)=\mathcal C(i)$ for every $i$, $\mathcal C(0)$ is an additive identity. Since $\mathcal C(i)+\mathcal C(1)=\mathcal C(i)$ for every $i$, $\mathcal C(1)$ is an multiplicative identity. Since $(\mathcal C(i)+\mathcal C(j))\times\mathcal C(k)=\mathcal C((i+j)k)=\mathcal C(ik+jk)$ and $\mathcal C(i)\times\mathcal C(k)+\mathcal C(j)\times\mathcal C(k)=\mathcal C(ik+jk)$, the ring is commutative for multiplication over addition.
1. Identify every element $[i]_m$ in $\mathbb Z_m$ with congruence class $\mathcal C(i)$. Given that
    1. $[i]_m+[j]_m=[(i+j)\bmod m]_m$,
    1. $[i]_m\times[j]_m=[(ij)\bmod m]_m$,
    1. $\mathcal C(i)+\mathcal C(j)=\mathcal C(i+j)=\mathcal C((i+j)\bmod m)$, and
    1. $\mathcal C(i)\times\mathcal C(j)=\mathcal C((ij)\bmod m)$,

> i.e.\ addition and multiplication rules correspond, we know that the ring of congruence classes modulo $m$ is equivalent to ring $\mathbb Z_m$, with the only difference on symbols.
