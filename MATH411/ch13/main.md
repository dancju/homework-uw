---
title: MATH 412, 2021 Summer, Chapter 13
...

# 13.1

1. $(a+b)^2=a^2+2ab+b^2=a^2+0ab+b^2=a^2+b^2$ in $K$.
1. $(x+a)^2=x^2+2xa+a^2=x^2+0xa+a^2=x^2+a^2$ in $K[x]$.
1. Since $a^2+a^2=2a^2=0a^2=0$, $x=a$ is a solution to $x^2+a^2=0$. Suppose $x=b$ is also a solution to $x^2+a^2=0$, i.e., $b^2+a^2=0$, which implies $(a+b)^2=0$. Since $K$ is a field, $K$ does not have zero divisors. Therefore, $a+b=0$, which implies $a=b$. Therefore, $x=a$ is the only solution to $x^2+a^2=0$.
1. Suppose $d\in K$ has two square roots in $K$ such that $d=\gamma_0^2=\gamma_1^2$, which implies $\gamma_0=\gamma_1$. Therefore, $d$ only has one unique square root such that $d=\gamma^2$.
1. $x^2+d=x^2+\gamma^2=(x+\gamma)^2$.

# 13.2

1. $(x+a)^2=x^2+2ax+a^2$, $x^2+bx+\frac{b^2}4=\left(x+\frac b2\right)^2$.
1. Equation $x^2+bx+c=0$ is equivalent to $\left(x+\frac b2\right)^2=\frac{b^2-4c}4$.
1. If $b^2-4c=0$, then $x^2+bx+c=\left(x+\frac b2\right)^2$, and the only solution to $x^2+bx+c=0$ is $x=-\frac b2$.
1. If $b^2-4c$ has no square root in $K$, then there is no solution to $x^2+bx+c=0$ and $x^2+bx+c$ is irreducible in $K[x]$.
1. If $b^2-4c$ is nonzero and has a square root in $K$, then $x^2+bx+c=0$ has two solutions in $K$, i.e., $x=\frac{-b\pm\sqrt{b^2-4c}}2$.
1. In conclusion, the quadratic formula works for quadratic equations with coefficients in any field $K$ with $2\ne0$.

# 13.3

1. For every complex number $a+bi$ with $a,b\in\mathbb R$ and $b\ne0$, consider the square root of it such that $(r+si)^2=a+bi$.
    1. Given $(r+si)^2=a+bi$, we have \begin{align}r^2-s^2=a\label{eq:13.3.0}\\2rs=b\label{eq:13.3.1}\end{align}.
    1. Equation \ref{eq:13.3.1} and $b\ne0$ implies $s=\frac b{2r}$. Plugging into \ref{eq:13.3.0} gives $4r^4-4ar^2-b^2=0$, which is a quadratic equation for $r^2$. Applying the quadratic formula yields $r^2=\frac{a\pm\sqrt{a^2+b^2}}2$.
    1. Since $r^2\ge0$ and $\frac{a-\sqrt{a^2+b^2}}2<0$, we have $r^2=\frac{a+\sqrt{a^2+b^2}}2$, which implies $r=\pm\sqrt{\frac{\sqrt{a^2+b^2}+a}2}$.
    1. Plugging into Equation \ref{eq:13.3.1} yields $s=\pm\frac{b}{\sqrt2\sqrt{\sqrt{a^2+b^2}+a}}=\pm\sqrt{\frac{\sqrt{a^2+b^2}-a}{2}}$.
1. We have proved that every complex number with a nonzero imagnary part has a square root. Moreover, every real number $a$ has square roots $\pm\sqrt a$. Therefore, every complex number has a square root.
1. Therefore, by applying the quadratic formula, we can find two roots for every quadratic polynomial in $\mathbb C[x]$. Therefore, every quadratic polynomial in $\mathbb C[x]$ factors as the product of two polynomials in $\mathbb C[x]$ of degree one.

# 13.4

1. Given complex number $c=a+bi$, we have $c=r(\cos\theta+i\sin\theta)$, with $r=\sqrt{a^2+b^2}$, $\theta=\arctan\frac ba$.
1. Let $\nu(\cos\xi+i\sin\xi)$ be the square root of $c$, we have $r(\cos\theta+i\sin\theta)=[\nu(\cos\xi+i\sin\xi)]^2$, or $r(\cos\theta+i\sin\theta)=\nu^2(\cos^2\xi-\sin^2\xi+2i\cos\xi\sin\xi)$. Plugging in double-angle formulas yields $r(\cos\theta+i\sin\theta)=\nu^2(\cos2\xi+i\sin2\xi)$, which implies $r=\nu^2$ and $\theta=2\xi$. Therefore, the square root of $c$ is $\pm\sqrt r\left(\cos\frac\theta2+i\sin\frac\theta2\right)$.

# 13.5

For every positive integer $n$, consider the square root $\sqrt n$.

1. Suppose $\sqrt n$ is not an integer. Furthermore, suppose $\sqrt n$ is rational, i.e., $\sqrt n=\frac{a}{b}$ with $b\ne0$.
    1. Given $\sqrt n=\frac{a}{b}$, we have $b^2n=a^2$. Suppose the prime factorization of $a$, $b$, and $n$ are \begin{align*}a=p_1^{\alpha_1}p_2^{\alpha_2}\cdots\\b=p_1^{\beta_1}p_2^{\beta_2}\cdots\\n=p_1^{\eta_1}p_2^{\eta_2}\cdots\end{align*} For every $i$, we have $2\beta_i+\eta_i=2\alpha_i$, which implies $\eta_i$ is even. Let $\eta_i=2\theta_i$ for every $i$. We have $n=p_1^{2\theta_1}p_2^{2\theta_2}\cdots=\left(p_1^{\theta_1}p_2^{\theta_2}\cdots\right)^2$, contradicting the assumption that $\sqrt n$ is not an integer. Therefore, the assuption is false, i.e., $\sqrt n$ irrational.
1. Therefore, $\sqrt n$ is either an integer or irrational.
1. Therefore, polynomial $x^2+bx+c\in\mathbb Z[x]$ have roots in $\mathbb Q$ iff $\sqrt{b^2-4c}$ is an integer.

# 13.6

1. Given $0^2=0$, $1^2=1$, $2^2=4$, $3^2=4$, and $4^2=1$, 1 and 4 have square roots in $\mathbb F_5$ while 2 and 3 do not.
1. Using the quadratic formula, the solutions to $x^2+2x+2=0$ are $\frac{-2\pm\sqrt{1}}{2}=1,2$.
1. Using the quadratic formula, the solutions to $x^2+2x+3=0$ are $\frac{-2\pm\sqrt{2}}{2}$. Since 2 does not have square roots, $x^2+2x+3=0$ has no solutions in $\mathbb F_5$.
1. The solution to $x^2+3x+1=0$ is 1.
1. There is no solutions to $x^2+3x+3=0$.

# 13.7

> **Theorem 13.5.** For an odd prime number $p$, field $\mathbb F_p$ contains $\frac{p-1}2$ nonzero elements that are squares of elements of $\mathbb F_p$ and $\frac{p-1}2$ elements that are not.

1. The $p$ elements of $\mathbb F_p$ are $$0,1,\dots,\frac{p-1}2,\frac{p-1}2+1,\dots,p-1\,.$$
1. Given $i\equiv i-p\pmod p$, the $p$ elements of $\mathbb F_p$ are $$\left[-\frac{p-1}2\right],\dots,[-1],[0],[1],\dots,\left[\frac{p-1}2\right]\,.$$
1. Proposition 13.3 stated that if $b$ and $c$ are in a ring such that $b^2=c$, then $b$ and $-b$ are the only square roots of $c$. Therefore, the set of the squares of the elements of $\mathbb F_p$ is $$[0]^2,[1]^2,\dots,\left[\frac{p-1}2\right]^2\,,$$ which contains $\frac{p-1}2$ distinct nonzero elements.
1. Therefore, field $\mathbb F_p$ contains $\frac{p-1}2$ nonzero elements that are squares, and $\frac{p-1}2$ elements that are not.

# 13.8

1. The square in $\mathbb F_{3}$ is 1.
1. The squares in $\mathbb F_{5}$ are 1 and 4.
1. The squares in $\mathbb F_{7}$ are 1, 2, and 4.
1. The squares in $\mathbb F_{11}$ are 1, 3, 4, 5, and 9.
1. The squares in $\mathbb F_{13}$ are 1, 3, 4, 9, 10, and 12.
1. The squares in $\mathbb F_{17}$ are 1, 2, 4, 8, 9, 13, 15, and 16.
1. The squares in $\mathbb F_{19}$ are 1, 4, 5, 6, 7, 9, 11, 16, and 17.

# 13.9

> **Exercise 13.9.** Assume that $p$ is an odd prime number such that $[-1]$ is a square in $\mathbb F_p$. We wish to prove that $p\equiv1\pmod4$.

1. Given $[-1]$ is a square in $\mathbb F_p$, \begin{equation}\exists b:b^2\equiv-1\pmod p\,.\label{eq:13.9.0}\end{equation}
1. Given $p$ is odd, $\frac{p-1}2$ is an integer.
1. Given Equation \ref{eq:13.9.0} and $\frac{p-1}2$ is an integer, $\exists b:\left(b^2\right)^{\frac{p-1}2}\equiv(-1)^{\frac{p-1}2}\pmod p$, or \begin{equation}\exists b:b^{p-1}\equiv(-1)^{\frac{p-1}2}\pmod p\,.\label{eq:13.9.1}\end{equation}
1. Given $p$ is prime, by Fermat's theorem, \begin{equation}\forall a:p\nmid a\implies a^{p-1}\equiv1\pmod p\,.\label{eq:13.9.2}\end{equation}
1. Given Equation \ref{eq:13.9.1} and \ref{eq:13.9.2}, $(-1)^{\frac{p-1}2}=1$, which implies $\frac{p-1}2$ is even, which implies $p\equiv1\pmod4$.

# 13.10

1. By Proposition 13.3, polynomial $x^2=[1]$ has two roots in $\mathbb F_p$, namely $[-1]$ and $[1]$.
1. Therefore, $[-1]$ and $[1]$ are the only elements in $\mathbb F_p$ that equal their own multipicative inverse.
1. Therefore, set $\{[2],\dots,[p-2]\}$ consists of $\frac{p-3}2$ pairs of inverse in $\mathbb F_p$, which implies $[2]\times\cdots\times[p-2]=[1]$ in $\mathbb F_p$.
1. Therefore, $[1]\times\cdots\times[p-1]=[-1]$ in $\mathbb F_p$.
1. Equivalently, $1\times\cdots\times(p-1)\equiv-1\pmod p$.

# 13.11

> **Theorem 13.7.** Suppose $p$ is a prime number satisfying $p\equiv1\pmod 4$. Then $[-1]$ is a square in $\mathbb F_p$.

1. Given $p$ is odd and $i\equiv i+p\pmod p$, we have \begin{align*}1\times\cdots\times\frac{p-1}2\times\frac{p+1}2\times\cdots\times(p-1)\\\equiv\left(1\times\cdots\times\frac{p-1}2\right)\times\left(\left(-\frac{p-1}2\right)\times\cdots\times(-1)\right)\pmod p\,,\end{align*} which implies \begin{equation}1\times\cdots\times(p-1)\equiv(-1)^\frac{p-1}2\left(1\times\cdots\times\frac{p-1}2\right)^2\pmod p\,.\label{eq:13.11.0}\end{equation}
1. Given $p$ is prime, by Wilson's theorem, \begin{equation}1\times\cdots\times(p-1)\equiv-1\pmod p\,.\label{eq:13.11.1}\end{equation}
1. Given Equation \ref{eq:13.11.0} and \ref{eq:13.11.1}, \begin{equation}-1\equiv(-1)^\frac{p-1}2\left(1\times\cdots\times\frac{p-1}2\right)^2\pmod p\,.\label{eq:13.11.2}\end{equation}
1. Given $p\equiv1\pmod 4$, we have $(-1)^\frac{p-1}2=1$. Plugging into Equation \ref{eq:13.11.2} yields $$-1\equiv\left(1\times\cdots\times\frac{p-1}2\right)^2\pmod p\,,$$ which implies $[-1]$ is a square in $\mathbb F_p$.

# 13.12

\begin{tabular}{rrrrrr}
\toprule
& $\mathbb F_{3}$ & $\mathbb F_{5}$ & $\mathbb F_{7}$ & $\mathbb F_{11}$ & $\mathbb F_{13}$ \\
\midrule
 1 & 1 & 1 & 1 &  1 &  1 \\
 2 & 2 & 4 & 3 & 10 & 12 \\
 3 &   & 4 & 6 &  5 &  3 \\
 4 &   & 2 & 3 &  5 &  6 \\
 5 &   &   & 6 &  5 &  4 \\
 6 &   &   & 2 & 10 & 12 \\
 7 &   &   &   & 10 & 12 \\
 8 &   &   &   & 10 &  4 \\
 9 &   &   &   &  5 &  3 \\
10 &   &   &   &  2 &  6 \\
11 &   &   &   &    & 12 \\
12 &   &   &   &    &  2 \\
\midrule
\# of elements of order $p-1$ & 1 & 2 & 2 & 4 & 4 \\
\bottomrule
\end{tabular}

# 13.13

> **Theorem 13.6.** If $p\equiv1\pmod4$, then $[-1]$ is a square in $\mathbb F_p$, while if $p\equiv3\pmod4$, then $[-1]$ is not a square in $\mathbb F_p$.

Let $p$ be an odd prime number and $a$ be a primitive root of $\mathbb F_p$.

1. Suppose $m$ is an even integer between 2 and $p-1$.
    1. By assumption, $\exists \alpha\in\mathbb F_p:m=2\alpha$, which implies $\exists \alpha\in\mathbb F_p:a^m=\left(a^\alpha\right)^2$, which implies $a^m$ is a square in $\mathbb F_p$.
1. Suppose $m$ is an odd integer between 1 and $p-2$.
    1. Assume $a^m$ is a square in $\mathbb F_p$, i.e., \begin{equation}\exists \alpha\in\mathbb F_p:a^m\equiv\alpha^2\pmod p\,.\label{eq:13.13.0}\end{equation}
    1. Since $a$ is a primitive root of $\mathbb F_p$, \begin{equation}\forall\alpha\in\mathbb F_p:\exists i:\alpha\equiv a^i\pmod p\,.\label{eq:13.13.1}\end{equation}
    1. Given Equation \ref{eq:13.13.0} and Equation \ref{eq:13.13.1}, $$\exists i:a^m\equiv a^{2i}\pmod p\,,$$ which implies $\exists j:m=2i+(p-1)j$, which implies $m$ is even, contradicting the assumption. Therefore, $a^m$ is not a square in $\mathbb F_p$.
1. Therefore, among the $p-1$ nonzero elements of $\mathbb F_p$, half are squares and the other half are not.
1. We have proved that $m$ is even iff $a^m$ is a square in $\mathbb F_p$. Therefore,
    1. The product of two squares is a square;
    1. The product of two non-squares is a square; and
    1. The product of a square and a non-square is not a square.
1. Since $p$ is prime, by Fermat's little theorem, we have $\forall\alpha:\alpha^{p-1}\equiv1\pmod p$.
    1. Assume $p\equiv1\pmod4$.
        1. Given $a$ is a primitive root, we have $\forall i\in\{1,\dots,p-2\}:a^i\not\equiv1\pmod p$, which implies \begin{equation}a^\frac{p-1}2\not\equiv1\pmod p\label{eq:13.13.o}\end{equation}
        1. By Fermat's little theorem, we have $a^{p-1}\equiv1\pmod p$. Given the square roots of $-1$ in $\mathbb F_p$ are $1$ and $-1$, we have \begin{equation}a^\frac{p-1}2\equiv-1\pmod p\text{ or }a^\frac{p-1}2\equiv1\pmod p\label{eq:13.13.i}\end{equation}
        1. Given Equation \ref{eq:13.13.o} and Equation \ref{eq:13.13.i}, we have \begin{equation}a^\frac{p-1}2\equiv-1\pmod p\label{eq:13.13.ii}\end{equation}
        1. Since $p\equiv1\pmod4$, we have $p=4k+1$ for some integer $k$. Plugging into Equation \ref{eq:13.13.ii} yields $a^{2k}\equiv-1\pmod p$. Therefore, $-1$ is a square in $\mathbb F_p$.
    1. Assume $p\equiv3\pmod4$.
        1. By assumption, we have $p=4k+3$ for some integer $k$.
        1. Assume $-1$ is a square in $\mathbb F_p$. We have $b^2\equiv-1\pmod p$ for some $b$, which implies $b^{2(2k+1)}\equiv(-1)^{2k+1}\pmod p$, which implies $b^{p-1}\equiv-1\pmod p$, which contradicts the Fermat's little theorem. Therefore, $-1$ is not a square in $\mathbb F_p$.

# 13.14

1. Set $K$ is a ring since it is
    1. closed under addition and multiplication,
    1. associative for multiplication,
    1. distributive for multiplication over addition.
1. $(a+b\gamma)(a-b\gamma)=a^2-b^2\gamma^2=a^2-2b^2\in\mathbb Q$.
1. $a^2-2b^2=0\implies a=b=0$.
1. Assume $a$ and $b$ are not both zero. We have $a^2-2b^2\ne0$. Given $a^2-2b^2\ne0$ and $(a+b\gamma)(a-b\gamma)=a^2-2b^2\in\mathbb Q$, we have $\frac{(a+b\gamma)(a-b\gamma)}{a^2-2b^2}=1$, which implies the multiplicative inverse of $a+b\gamma$ is $\frac{a-b\gamma}{a^2-2b^2}$.

# 13.15

Let set $K$ be an extension of $\mathbb Q$ containing $\gamma=\sqrt m$. We have $K=\{a+b\gamma:a,b\in\mathbb Q\}$.

1. Set $K$ is closed under addition since $(a+b\gamma)+(c+d\gamma)=(a+c)+(b+d)\gamma\in K$.
1. Set $K$ is closed under multiplication since $(a+b\gamma)(c+d\gamma)=(ac+bdm)+(ad+bc)\gamma\in K$.
1. Every element $a+b\gamma$ has an multiplicative inverse in $K$ since $(a+b\gamma)(a-b\gamma)(a^2-b^2m)^{-1}=1$.
1. Therefore, $K$ is a field.

# 13.16

1. Set $K$ is a ring since it is
    1. closed under addition and multiplication,
    1. associative for multiplication,
    1. distributive for multiplication over addition.
1. .
\begin{footnotesize}\begin{tabular}{rrrrrrrrr}
\toprule
$\times$ & $\gamma$ & $2\gamma$ & 1 & $1+\gamma$ & $1+2\gamma$ & 2 & $2+\gamma$ & $2+2\gamma$ \\
\midrule
   $\gamma$ &           2 &           1 &    $\gamma$ &  $2+\gamma$ &  $1+\gamma$ &   $2\gamma$ & $2+2\gamma$ & $1+2\gamma$ \\
  $2\gamma$ &           1 &           2 &   $2\gamma$ & $1+2\gamma$ & $2+2\gamma$ &    $\gamma$ &  $1+\gamma$ &  $2+\gamma$ \\
          1 &    $\gamma$ &   $2\gamma$ &           1 &  $1+\gamma$ & $1+2\gamma$ &           2 &  $2+\gamma$ & $2+2\gamma$ \\
 $1+\gamma$ &  $2+\gamma$ & $1+2\gamma$ &  $1+\gamma$ &   $2\gamma$ &           2 & $2+2\gamma$ &           1 &    $\gamma$ \\
$1+2\gamma$ &  $1+\gamma$ & $2+2\gamma$ & $1+2\gamma$ &           2 &    $\gamma$ &  $2+\gamma$ &   $2\gamma$ &           1 \\
          2 &   $2\gamma$ &    $\gamma$ &           2 & $2+2\gamma$ &  $2+\gamma$ &           1 & $1+2\gamma$ &  $1+\gamma$ \\
 $2+\gamma$ & $2+2\gamma$ &  $1+\gamma$ &  $2+\gamma$ &           1 &   $2\gamma$ & $1+2\gamma$ &    $\gamma$ &           2 \\
$2+2\gamma$ & $1+2\gamma$ &  $2+\gamma$ & $2+2\gamma$ &    $\gamma$ &           1 &  $1+\gamma$ &           2 &   $2\gamma$ \\
\bottomrule
\end{tabular}\end{footnotesize}
1. .
\begin{tabular}{rrrrrrrrr}
\toprule
& $\gamma$ & $2\gamma$ & 1 & $1+\gamma$ & $1+2\gamma$ & 2 & $2+\gamma$ & $2+2\gamma$ \\
\midrule
inverse & $2\gamma$ & $\gamma$ & 1 & $2+\gamma$ & $2+2\gamma$ & 2 & $1+\gamma$& $1+2\gamma$ \\
\bottomrule
\end{tabular}
1. Since every nonzero element has an inverse, $K$ is a field.
1. $(a+b\gamma)(a-b\gamma)=a^2-2b^2=a^2+b^2\in\mathbb F_3$.
1. If $a^2+b^2=0$, then $(a+b\gamma)(a-b\gamma)=0$, which (given there is no zero divisor in $K$) implies $a+b\gamma=0\lor a-b\gamma=0$, which implies $a=b=0$. Therefore, $a^2+b^2=0\iff a=b=0$.
1. Suppose $a$ and $b$ are not both zero.
    1. By assumption, we have $a^2+b^2\ne0$.
    1. Given $a^2+b^2$ is nonzero, $a^2+b^2\in\mathbb F_3$, and $\mathbb F_3$ is a field, $a^2+b^2$ has a multiplicative inverse $\left(a^2+b^2\right)^{-1}$.
    1. Multiplying through $(a+b\gamma)(a-b\gamma)=a^2+b^2$ by $\left(a^2+b^2\right)^{-1}$ yields $(a+b\gamma)(a-b\gamma)\left(a^2+b^2\right)^{-1}=1$, which implies $a+b\gamma$ has an inverse.
    1. Therefore, every nonzero element in $K$ has an inverse. Therefore, set $K$ is a field.
1. Since $\gamma^2-2=(-\gamma)^2-2=0$, polynomial $x^2-2$ has root $-\gamma$ and $\gamma$. Therefore, equation $x^2-2$ factors as $(x-\gamma)(x+\gamma)$ in $K[x]$.
1.  1. $(1+\gamma)^1=1+\gamma$
    1. $(1+\gamma)^2=2\gamma$
    1. $(1+\gamma)^3=1+2\gamma$
    1. $(1+\gamma)^4=2$
    1. $(1+\gamma)^5=2+2\gamma$
    1. $(1+\gamma)^6=\gamma$
    1. $(1+\gamma)^7=2+\gamma$
    1. $(1+\gamma)^8=1$
    1. Therefore, $1+\gamma$ is a primitive root of $K$.

# 13.17

1. Set $K$ is a ring since it is
    1. associative for multiplication,
    1. distributive for multiplication over addition.
    1. closed under addition and multiplication,
1. Since every $a+b\gamma$ represents an unique element in $K$, there are 25 elements in $K$, i.e., $K=\{a+b\gamma:a,b=0,\dots,4\}$.
1. $(a+b\gamma)(a-b\gamma)=a^2-b^2\gamma^2=a^2-2b^2=a^2+3b^2\in\mathbb F_5$.
1. If $a^2+3b^2=0$, then $(a+b\gamma)(a-b\gamma)=0$, which (given there is no zero divisor in $K$) implies $a+b\gamma=0\lor a-b\gamma=0$, which implies $a=b=0$. Therefore, $a^2+3b^2=0\iff a=b=0$.
1. Suppose $a$ and $b$ are not both zero.
    1. By assumption, we have $a^2+3b^2\ne0$.
    1. Given $a^2+3b^2$ is nonzero, $a^2+3b^2\in\mathbb F_3$, and $\mathbb F_3$ is a field, $a^2+3b^2$ has a multiplicative inverse $\left(a^2+3b^2\right)^{-1}$.
    1. Multiplying through $(a+b\gamma)(a-b\gamma)=a^2+3b^2$ by $\left(a^2+3b^2\right)^{-1}$ yields $(a+b\gamma)(a-b\gamma)\left(a^2+3b^2\right)^{-1}=1$, which implies $a+b\gamma$ has an inverse.
    1. Therefore, every nonzero element in $K$ has an inverse. Therefore, set $K$ is a field.
1. $(2\gamma)^2=3$. Therefore, the square roots of $0,1,2,3,4$ are $0,1,\gamma,2\gamma,2$. Therefore, field $K$ is an extension of $\mathbb F_5$ containing the square roots for every element of $\mathbb F_5$.
1. Applying the quadratic formula to equation $x^2+2x+3=0$ in $K$ yields $x=4\pm3\gamma$. Therefore, polynomial $x^2+2x+3$ factors as $(x-4+3\gamma)(x-4-3\gamma)$ in $K[x]$.
1. .
\begin{tabular}{rr}
\toprule
$i$ & $(1+2\gamma)^i$ \\
\midrule
 1 & $1+2\gamma$ \\
 2 & $4+4\gamma$ \\
 3 &   $2\gamma$ \\
 4 & $3+2\gamma$ \\
 5 & $1+3\gamma$ \\
 6 &           3 \\
 7 &  $3+\gamma$ \\
 8 & $2+2\gamma$ \\
 9 &    $\gamma$ \\
10 &  $4+\gamma$ \\
11 & $3+4\gamma$ \\
12 &           4 \\
13 & $4+3\gamma$ \\
14 &  $1+\gamma$ \\
15 &   $3\gamma$ \\
16 & $2+3\gamma$ \\
17 & $4+2\gamma$ \\
18 &           2 \\
19 & $2+4\gamma$ \\
20 & $3+3\gamma$ \\
21 &   $4\gamma$ \\
22 & $1+4\gamma$ \\
23 &  $2+\gamma$ \\
24 &           1 \\
\bottomrule
\end{tabular}
Therefore, $1+2\gamma$ is a primitive root of $K$.

# 13.18

1. Set $K$ is a ring since it is
    1. closed under addition and multiplication,
    1. associative for multiplication,
    1. distributive for multiplication over addition.
1. $(a+b\gamma)(a-b\gamma)=a^2-b^2\gamma^2=a^2-mb^2\in F$
1. If $a^2-mb^2=0$, then $(a+b\gamma)(a-b\gamma)=0$, which (given there is no zero divisor in $K$) implies $a+b\gamma=0\lor a-b\gamma=0$, which implies $a=b=0$. Therefore, $a^2-mb^2=0\iff a=b=0$.
1. Suppose $a$ and $b$ are not both zero.
    1. By assumption, we have $a^2-mb^2=0$.
    1. Given $a^2-mb^2$ is nonzero, $a^2-mb^2\in F$, and $F$ is a field, $a^2-mb^2$ has a multiplicative inverse $\left(a^2-mb^2\right)^{-1}$.
    1. Multiplying through $(a+b\gamma)(a-b\gamma)=a^2-mb^2$ by $\left(a^2-mb^2\right)^{-1}$ yields $(a+b\gamma)(a-b\gamma)\left(a^2-mb^2\right)^{-1}=1$, which implies $a+b\gamma$ has an inverse $(a-b\gamma)\left(a^2-mb^2\right)^{-1}$.
    1. Therefore, every nonzero element in $K$ has an inverse. Therefore, set $K$ is a field.
1. Given $\gamma^2-m=(-\gamma)^2-m=0$, polynomial $x^2-m$ has two roots $-\gamma$ and $\gamma$ in $K$. Therefore, $x^2-m$ factors in $K$ as $(x-\gamma)(x+\gamma)$.
1. Assume $2\ne0$ in $F$, and $x^2+px+q$ is a quadratic polynomial in $K[x]$ whose discriminant $p^2-4q$ equals $m$. Applying the quadratic formula to $x^2+px+q$ yields $x=\frac{-p\pm\sqrt{p^2-4q}}{2q}=\frac{-p\pm\gamma}{2q}$. Therefore, the polynomial has no roots in $F$ but has two roots in $K$.

# 13.19

> **Exercise 13.19.** Let $p$ be a prime number congruent to 3 modulo 4 and write $-1$ for the additive inverse of 1 in $\mathbb F_p$. Recall from Theorem 13.6 that $-1$ is not a square in $\mathbb F_p$. Perform the construction of Exercise 13.18 on $\mathbb F_p$ and $-1$ to obtain a new ﬁeld $\mathbb F_p\left[\sqrt{-1}\right]$ containing $\mathbb F_p$ in which $-1$ has a square root. Show that $\mathbb F_p\left[\sqrt{-1}\right]$ has $p^2$ elements.

For every pair of elements $\left(a+b\sqrt{-1},c+d\sqrt{-1}\right)$ of $\mathbb F_p\left[\sqrt{-1}\right]$, we have $a+b\sqrt{-1}=c+d\sqrt{-1}$ iff $a=c$ and $b=d$. Therefore, $\mathbb F_p\left[\sqrt{-1}\right]=\left\{a+b\sqrt{-1}:a,b\in\mathbb F_p\right\}$, which has $p^2$ elements.

# 13.20

1. Since every $\alpha+\beta\sqrt a$ represents an unique element, there are $p^2$ elements in $\mathbb F_p\left[\sqrt a\right]$, i.e. $\left\{\alpha+\beta\sqrt a:\alpha,\beta=0,\dots,p-1\right\}$.
1. Since $a$ is a primitive root of $\mathbb F_p$, for every $\alpha\in\mathbb F_p$, we have $\alpha=a^i$ for some $i\in\{0,\dots,p-1\}$. If $i$ is even, then $\sqrt\alpha=a^\frac i2$; if $i$ is odd, then $\sqrt\alpha=a^\frac{i-1}2\sqrt a$. Either way, the square root of $\alpha$ lies in $\mathbb F_p\left[\sqrt a\right]$. Therefore, every element has a square root. For every polynomial $x^2+bx+c$ in $\mathbb F_p[x]$, by applying the quadratic formula, we get one or two roots in $\mathbb F_p\left[\sqrt a\right]$.
