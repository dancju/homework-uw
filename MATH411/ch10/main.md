---
title: MATH 412, 2021 Summer, Chapter 10
...

# 10.1

1. For real number $a$, we have $(x+a)^2=x^2+2ax+a^2$.
1. For real number $b$, we have $(x+\frac b2)^2=x^2+bx+\frac{b^2}4$.
1. Given $x^2+bx+c=(x+\frac b2)^2-\frac{b^2}4+c$, solving the equation $x^2+bx+c=0$ is equivalent to solving $(x+\frac b2)^2=\frac{b^2-4c}4$.
1. If $b^2-4c=0$, then $x^2+bx+c=(x+\frac b2)^2$, i.e., $x^2+bx+c$ factors as $(x+\frac b2)^2$, and the only solution to $x^2+bx+c=0$ is $x=-\frac b2$.
1. If $b^2-4c<0$, then there is no solution in $\mathbb R$ to $x^2+bx+c=0$, and $x^2+bx+c$ is irreducible in $\mathbb R[x]$.
1. If $b^2-4c>0$, then there are two solutions to $x^2+bx+c=0$, namely $-\frac b2\pm\frac{\sqrt{b^2-4c}}2$.

# 10.3

Given $x^2+bx+c=(x-r_1)(x-r_2)$, we have $b=-(r_1+r_2)$ and $c=r_1r_2$. Therefore, $(r_1-r_2)^2=(r_1+r_2)^4-4r_1r_2=b^2-4c$.

# 10.4

1. Given $x^2+bx+c=(x-r_1)(x-r_2)$, we have $b=-(r_1+r_2)$ and $c=r_1r_2$.
1. If $c=0$, then $\Delta=b^2-4c=b^2\ge0$, i.e., the roots are real.
1. If the roots have the same sign, then $c=r_1r_2>0$. If the roots have opposite signs, then $c=r_1r_2<0$.
1. There is an odd number of positive roots when $c<0$ and even number of roots when $c>0$.
1. Assume $c>0$, i.e. the roots have the same sign. If the roots are both positive, then $b=-(r_1+r_2)<0$. If $b=-(r_1+r_2)<0$, given the assumption that the roots have the same sign, we have the roots are both positive. Therefore, $b<0$ iff roots are both positive. Similarily, $b>0$ iff roots are both negative.
1. In conclusion, we can determine the signs of the roots when roots are real such that
    1. If $c=0$, then roots are 0 and $-b$.
    1. If $c<0$, then two roots have opposite signs.
    1. If $c>0$ and $b<0$, then both roots are positive.
    1. If $c>0$ and $b>0$, then both roots are negative.

# 10.6

Substituting $x=y+1$ into $x^3-3x^2-4x+12=0$ yields the reduced cubic equation $y^3-7y+6=0$.

# 10.8

Applying Cardano's formula to $y^3-3y+2=0$ yields $y=-2$. Polynomial $y^3-3y+2$ factors as $(y+2)(y-1)^2$.

# 10.9

1. $\sqrt[3]{-2+\frac{10}{9}\sqrt{3}}+\sqrt[3]{-2-\frac{10}{9}\sqrt{3}}=
\left(-1+\frac{\sqrt3}3\right)+\left(-1-\frac{\sqrt3}3\right)=-2$.
1. $y^3-2y+4=(y+2)(y^2-2y+2)=(y+2)(y-(1-i))(y-(1+i))$. The other two solutions are $1-i$ and $1+i$.

# 10.38

1. $a_0=b_0c_0$.
1. $a_1=b_0c_1+b_1c_0 \\ a_2=b_0c_2+b_1c_1+b_2c_0 \\ a_3=b_0c_3+b_1c_2+b_2c_1+b_3c_0$.
1. $a_k=\sum_{i=0}^kb_ic_{k-i}\,.$

# 10.40

1. Given $f(x)\in\mathbb R[x]$, we have $\bar f(x)=f(x)$, implying $f(\bar r)=\bar f(\bar r)=\overline{f(r)}=0$.
1. Since every coefficient of $(x-r)(x-\bar r)=x^2-(r+\bar r)x+r\bar r=x^2-2\Re(r)x+|r|^2$ are real, polynomial $(x-r)(x-\bar r)$ lies in $\mathbb R[x]$.
1.  1. Given $r\in\mathbb C$ and $(x-r)\mid f(x)$ in $\mathbb C[x]$, by Theorem 10.6, we have $(x-\bar r)\mid f(x)$ in $\mathbb C[x]$, which implies $(x-r)(x-\bar r)\mid f(x)$ in $\mathbb C[x]$.
    1. Given $f(x)\in\mathbb R[x]$, $(x-r)(x-\bar r)\in\mathbb R[x]$, and $(x-r)(x-\bar r)\mid f(x)$ in $\mathbb C[x]$, we get $(x-r)(x-\bar r)\mid f(x)$ in $\mathbb R[x]$.

# 10.41

1. By Theorem 10.8, the conjugate of $f(x)\bar f(x)$ is itself, i.e., $f(x)\bar f(x)$ is unchanged by conjugation. Therefore, $f(x)\bar f(x)\in\mathbb R[x]$.
1. Given $f(x)\bar f(x)\in\mathbb R[x]$ is non-constant, by Theorem 10.6, $f(x)\bar f(x)$ has at least one root in $\mathbb C$.
1. Letting a root of $f(x)\bar f(x)$ be $r\in\mathbb C$ such that $f(r)\bar f(r)=0$, we have $f(r)=0$ or $\bar f(r)=0$.
1. If $\bar f(r)=0$, by Theorem 10.8, we have $f(\bar r)=0$. Therefore, either $f(r)=0$ or $f(\bar r)=0$. Therefore, $f(x)$ has a root in $\mathbb C$.
