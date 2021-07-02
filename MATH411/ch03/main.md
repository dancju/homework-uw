---
title: MATH 411, 2021 Summer, Chapter 3
...

# 3.1

1.
\begin{align*}
\gcd(10,100)&=10\,,\\
\gcd(6,24)&=6\,,\\
\gcd(2, 234\,786\,991\,302)&=2\,.
\end{align*}
1. Suppose $a$ and $b$ are positive integers and $a\mid b$. We will prove $\gcd(a,b)=a$.
    1. We will prove the common divisors of $a$ and $b$ are precisely the divisors of $a$ in two steps.
        1. If an integer is a common divisor of $a$ and $b$, it is by definition a divisor of $a$.
        1. If an integer is a divisor of $a$, since $a$ divides $b$, by Theorem 2.6, it is also a divisor of $b$, and consequently a common divisor of $a$ and $b$.
    1. Since $a$ is the greatest divisor of itself, it is also the greatest common divisor of $a$ and $b$.
1.
\begin{align*}
\gcd(6, 9)&=3\,, \\
\gcd(25, 40)&=5\,, \\
\gcd(14, 85)&=1\,, \\
\gcd(30, 84)&=6\,, \\
\gcd(66, 561)&=33\,, \\
\gcd(70, 1\,869)&=7\,, \\
\gcd(227\,761,661\,643)&=541\,.
\end{align*}

# 3.2

To prove the set of common divisors of $a$ and $b$ equals the set of common divisors of $a$ and $b-a$, we need to show that every common divisor of $a$ and $b$ is a common divisor of $a$ and $b-a$, and vise versa.

If an integer is an common divisor of $a$ and $b$, since $a<b$, by Theorem 2.6, it is also a divisor of $b-a$, and consequently a common divisor of $a$ and $b-a$.

If an integer is an common divisor of $a$ and $b-a$, by Theorem 2.6, it is also a divisor of $b=(b-a)+a$, and consequently a common divisor of $a$ and $b$.

Therefore, the set of common divisors of $a$ and $b$ equals the set of common divisors of $a$ and $b-a$. Since two equal sets have the common greatest value, we can conclude $(a,b)=(a,b-a)$.

# 3.3

To prove the set of common divisors of $a$ and $b$ equals the set of common divisors of $a$ and $r$, we need to show that every common divisor of $a$ and $b$ is a common divisor of $a$ and $r$, and vise versa.

If an integer is a common divisor of $a$ and $b$, by Theorem 2.7, it is also an divisor of $r=-qa+b$, and consequently a common divisor of $a$ and $r$.

If an integer is a common divisor of $a$ and $r$, by Theorem 2.7, it is also an divisor of $b=qa+r$, and consequently a common divisor of $a$ and $b$.

Therefore, the set of common divisors of $a$ and $b$ equals the set of common divisors of $a$ and $r$.

# 3.4

\begin{align*}
(6,9)&=3\,, \\
(25,40)&=5\,, \\
(14,85)&=1\,, \\
(66,561)&=33\,, \\
(70,1869)&=7\,, \\
(568,4292)&=4\,, \\
(17017,18900)&=7\,, \\
(227761,661643)&=541\,.
\end{align*}

# 3.5

\begin{align*}
(6,9)&=3&=-1\times6+1\times9\,, \\
(25,40)&=5&=-3\times25+2\times40\,, \\
(14,85)&=1&=-6\times14+1\times85\,, \\
(66,561)&=33&=-8\times66+1\times561\,, \\
(70,1869)&=7&=-80\times70+3\times1869\,, \\
(568,4292)&=4&=-68\times568+9\times4292\,, \\
(17017,18900)&=7&=271\times17017-244\times18900\,, \\
(227761,661643)&=541&=581\times227761-200\times661643\,.
\end{align*}

# 3.6

> **Theorem 3.3 (Bézout).** Let $a$ and $b$ be integers with greatest common divisor $d$. Then there exist integers $r$ and $s$ such that $d=ar+bs$. Thus, the greatest common divisor of $a$ and $b$ is an integer linear combination of $a$ and $b$. Moreover, the data of the Euclidean algorithm can be used to determine an explicit pair of integers $r$ and $s$.

1. Suppose that $a$ and $b$ are positive integers for which the Euclidean algorithm terminates after one step such that
    \begin{align*}
    b=aq_1+r_1\,, \\
    a=r_1q_2+0\,.
    \end{align*}
    The gcd of $a$ and $b$ yielded by the algorithm is $r_1$. Therefore, $\gcd(a,b)=b-aq_1$. Therefore, Bézout's theorem is true for $a$ and $b$ if the Euclidean algorithm terminates after one step.
1. Assume Bézout's theorem is true for every pair of integers if the Euclidean algorithm terminates after $k$ steps. Suppose that $a$ and $b$ are positive integers for which the Euclidean algorithm terminates after $k+1$ steps such that
    \begin{align*}
    b=aq_1+r_1\,, \\
    a=r_1q_2+r_2\,. \\
    \end{align*}
The gcd of $a$ and $b$ yielded by the algorithm is the gcd of $a$ and $r_1$, which, by assumption, is a linear combination of $a$ and $r_1$. Since $r_1$ is a linear combination of $b$ and $a$ such that $r_1=b-aq_1$, the gcd of $a$ and $b$ is a linear combination of $b$ and $a$. Therefore, Bézout's theorem is true for every pair of integers if the Euclidean algorithm terminates after $k+1$ steps.
1. Since the Euclidean algorithm terminates after a finite number of steps, by the principle of induction, we can conclude that the output of the Euclidean algorithm is a linear combination of the input.

# 3.7

Since $d$ is the greatest common divisor of $a$ and $b$, by Bézout's theorem, there exist integers $r$ and $s$ such that $d=ar+bs$. Since $e$ is a common divisor of both $a$ and $b$, there exist integers $t$ and $u$ such that $a=et$ and $b=eu$. Therefore, $d=etr+eus=(tr+us)e$, which implies $e$ divides $d$.

# 3.8

Since $a$ and $b$ are two relatively prime integers, by Bézout's theorem, there exist integers $r$ and $s$ such that \begin{equation}1=ar+bs\,.\end{equation}

Since $a$ divides $bc$, there exist an integer $t$ such that \begin{equation}bc=ta\,.\end{equation}

Multiplying the both sides of (3) by $c$ and substituting by (4) yields $c=(cr+st)a$, which implies $a$ divides $c$.

The conclusion above may not hold if the relative primality of $a$ and $b$ is dropped, which is proven by the following example:

$$a=2\,,\quad b=4\,,\quad c=3\,.$$

# 3.9

> **Corollary 3.5.** Let $a$ and $b$ be relatively prime integers. Suppose that $c$ is an integer and $n$ is a positive integer such that $a\mid b^nc$. Then $a\mid c$.

1. Corollary 3.5 is valid for $n=1$ since it would be equivalent to Theorem 3.4.
1.  1. Let $a,b,c$ be integers and $k$ be a positive integer such that $a$ and $b$ are relatively prime and $a$ divides $b^{k+1}c$.
    1. Since $a$ and $b$ are relatively prime, by Bézout's theorem, there exist integers $r$ and $s$ such that \begin{equation}1=ar+bs\,.\end{equation}
    1. Since $a$ divides $b^{k+1}c$, there exist an integer $t$ such that \begin{equation}b^{k+1}c=ta\,.\end{equation}
    1. Multiplying both sides of (5) by $b^kc$ and substituting by (6) yields $b^kc=(b^kcr+st)a$, which implies $a$ divides $b^kc$.
    1. Since $a$ and $b$ are relatively prime and $a$ divides $b^kc$, assuming Corollary 3.5 is true for $n=k$, $a$ divides $c$. Therefore, Corollary 3.5 is true for $n=k+1$.
1. We have shown that Corollary 3.5 is true for $n=1$. We have also shown that Corollary 3.5 is true for $n=k+1$ under the assumption that Corollary 3.5 is true for $n=k$. By the principle of induction, we can conclude that Corollary 3.5 is true for every positive integer $n$.

# 3.10

Substituting $r/s$ into the given equation and multiplying by $s^n$ yields \begin{equation}a_nr^n+a_{n-1}r^{n-1}s+\cdots+a_1rs^{n-1}+a_0s^n=0\,.\end{equation}

Equation (7) is equivalent to $a_nr^n=-(a_{n-1}r^{n-1}+\cdots+a_1rs^{n-2}+a_0s^{n-1})s$, which implies $s$ divides $a_nr^n$. Given $s$ and $r$ are relatively prime, by Corollary 3.5, we have $s$ divides $a_n$.

Similarily, equation (7) is also equivalent to $a_0s^n=-(a_nr^{n-1}+a_{n-1}r^{n-2}s+\cdots+a_1s^{n-1})r$, which implies $r$ divides $a_0s^n$. Given $s$ and $r$ are relatively prime, by Corollary 3.5, we have $r$ divides $a_0$.

Therefore, Theorem 3.6 is proved. Since Theorem 3.7 is a special case of Theorem 3.6 for $a_n=1$, Theorem 3.7 is also proven.

# 3.11

Finding all divisors of the constant term and verifying by substituting yields all rational solutions of the equation.

1. $\emptyset$
1. $\{1\}$
1. $\{-1\}$
1. $\{-5\}$
1. $\{2\}$

# 3.12

By definition, $(a,b)$ divides $a$ and $b$. Since $e$ is a linear combination of $a$ and $b$, by Theorem 2.7, $(a,b)$ also divides $e$.

# 3.13

1. $\emptyset$
1. $x=11,\quad y=-11$
1. $x=-207,\quad y=138$
1. $x=-18,\quad y=3$
1. $\emptyset$
1. $x=-24,\quad y=3$
1. $x=-400,\quad y=15$
1. $\emptyset$
1. $x=2450,\quad y=-335$

# 3.14

1. $x=11+3k,\quad y=-11-2k$
1. $x=-207+8k,\quad y=138-5k$
1. $x=-18+85k,\quad y=3-14k$

# 3.15

1. $c=-2a+2b$. Start them at the same time. The time between the moment when the first hourglass runs out 2 periods and the moment when the second hourglass runs out 2 periods is 8 minutes.
1. $c=-2a+3b$. Start them at the same time. The time between the moment when the first hourglass runs out 2 periods and the moment when the second hourglass runs out 3 periods is 11 minuts.
1. $c=4a-b$. Start them at the same time. The time between the moment when the first hourglass runs out 4 periods and the moment when the second hourglass runs out 1 period is 13 minuts.
