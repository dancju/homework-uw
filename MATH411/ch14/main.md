---
title: MATH 412, 2021 Summer, Chapter 14
...

# 14.1

1. Set $K$ is a ring since it is
    1. associative for multiplication,
    1. distributive for multiplication over addition,
    1. closed under addition $(a+b\gamma+c\gamma^2)+(d+e\gamma+f\gamma^2)=(a+d)+(b+e)\gamma+(c+f)\gamma^2$,
    1. closed under multiplication $(a+b\gamma+c\gamma^2)(d+e\gamma+f\gamma^2)=(ad+2bf+2cd)+(ae+bd+2cf)\gamma+(af+be+cd)\gamma^2$.
1. Ring $K$ is an extension of $\mathbb Q$ containing $\gamma=\sqrt[3]2$.
1. Assume $(a+b\gamma+c\gamma^2)(d+e\gamma+f\gamma^2)=1$.
    1. We have $$\begin{cases}ad+2bf+2ce=1\\ae+bd+2cf=0\\af+be+cd=0\end{cases}$$ Solving for $d,e,f$ yields $$\begin{cases}d=\frac{a^2-2bc}{a^3+2b^3+4c^3-6abc}\\e=-\frac{ab-2c^2}{a^3+2b^3+4c^3-6abc}\\f=-\frac{ac-b^2}{a^3+2b^3+4c^3-6abc}\end{cases}$$
    1. Therefore, every $a+b\gamma+c\gamma^2\ne0$ has a multipicative inverse in $K$.
    1. Therefore, ring $K$ is a field.
1. $(2+\gamma-\gamma^2)\left(\frac13+\frac16\gamma^2\right)=1$.

# 14.2

Let $K$ be an extension of $\mathbb Q$ containing $\gamma=\sqrt[n]2$ such that $K=\left\{\sum_{i=0}^{n-1}a_i\gamma^i:a_i\in\mathbb Q\right\}$.

1. For any integer $m$, let $q$ and $r$ be the quotient and remainder of $m$ modulo $n$. We have $m=nq+r$, which implies $\gamma^m=2^q\gamma^r$.
1. \begin{align*}&\left(\sum_{i=0}^{n-1}a_i\gamma^i\right)\left(\sum_{i=0}^{n-1}b_i\gamma^i\right)\\=&\left(\sum_{i=0}^{n-1}\sum_{j=0}^ia_jb_{i-j}\gamma^i\right)+\left(\sum_{i=n}^{2n-2}\sum_{j=i-n+1}^{n-1}a_jb_{i-j}\gamma^i\right)\\=&\left(\sum_{i=0}^{n-1}\sum_{j=0}^ia_jb_{i-j}\gamma^i\right)+2\left(\sum_{i=0}^{n-2}\sum_{j=i+1}^{n-1}a_jb_{i+n-j}\gamma^i\right)\end{align*}
1. Assuming $\left(\sum_{i=0}^{n-1}a_i\gamma^i\right)\left(\sum_{i=0}^{n-1}b_i\gamma^i\right)=1$ yields \begin{align*}\forall i\in\{1,\dots,n-2\}:\left(\sum_{j=0}^ia_jb_{i-j}\right)+2\left(\sum_{j=i+1}^{n-1}a_jb_{i+n-j}\right)=0 \,,\\\sum_{j=0}^{n-1}a_jb_{n-1-j}=0 \,,\\a_0b_0+2\sum_{j=0}^{n-1}a_jb_{n-j}=1\,,\end{align*} which, assuming $a_j$-s are variables and $b_j$-s are constants, is a system of $n$ linear equations with $n$ variables, which has an unique solution. Therefore, any nonzero element has an multiplicative inverse in $K$. Therefore, $K$ is a field.

# 14.5

1. $(x^5+7x^3-5x^2+2x+1)-(x^5-x^4+4x^3-10x^2-7x-5)=x^4+3x^3+5x^2+9x+6=(x^3+3x+2)(x+3)+(2x^2-2x)$. Therefore, the congruence $x^5+7x^3-5x^2+2x+1\equiv x^5-x^4+4x^3-10x^2-7x-5\pmod{x^3+3x+2}$ is not valid in $\mathbb Q[x]$.
1. $(x^4+3x^3+2x+1)-(3x^4+x^2+cx)=3x^4+3x^3+4x^2+(2-c)x+1=(x^2+x+2)(3x^2+3)+(4-c)x$. Therefore, $c=4$ makes $x^4+3x^3+2x+1\equiv 3x^4+x^2+cx\pmod{x^2+x+2}$ valid in $\mathbb F_5[x]$.
1. $(3x^4+x^2+cx)-(x^4+3x^3+2x+1)=2x^4-3x^3+x^2+(c-2)x-1=(x^2+x+2)(2x^2-5x+2)+((6+c)x-5)$. Therefore, there is no $c$ makes $x^4+3x^3+2x+1\equiv 3x^4+x^2+cx\pmod{x^2+x+2}$ valid in $\mathbb R[x]$.

# 14.6

> **Theorem 14.1.** Let $F$ be a field and $m(x)$ be a polynomial in $F[x]$ of positive degree $n$. Every polynomial $a(x)$ in $F[x]$ is congruent modulo $m(x)$ to exactly one polynomial of degree less than $n$.

Theorem 14.1 consists of two statements. First, it asserts that every $a(x)$ in $F[x]$ is congruent modulo $m(x)$ to at least one $r(x)$ with $\deg r(x)<\deg m(x)$. Second, it asserts that if $a(x)$ is congruent modulo $m(x)$ to both $r(x)$ and $s(x)$ in $F[x]$ with $\deg r(x)<\deg m(x)$ and $\deg s(x)<\deg m(x)$, then $s(x)=r(x)$.

1. Given $F$ is a field, $a(x),m(x)\in F[x]$, and $\deg m(x)>0$, by the division theorem, there exist $q(x)$ and $r(x)$ such that $a(x)=q(x)m(x)+r(x)$ and $\deg r(x)<\deg m(x)$. Therefore, $\forall a(x)\in F[x],\exists r(x)\in F[x]:a(x)\equiv r(x)\pmod{m(x)}\land\deg r(x)<\deg m(x)$.
1. Suppose both $r(x)$ and $s(x)$ with less degree than $m(x)$ are congruent modulo $m(x)$ to $a(x)$.
    1. We have $a(x)\equiv r(x)\pmod{m(x)}$, $a(x)\equiv s(x)\pmod{m(x)}$, $\deg r(x)<\deg m(x)$, and $\deg s(x)<\deg m(x)$.
    1. Given $a(x)\equiv r(x)\pmod{m(x)}$ and $a(x)\equiv s(x)\pmod{m(x)}$, we get $m(x)\mid(r(x)-s(x))$.
    1. Given $\deg r(x)<\deg m(x)$ and $\deg s(x)<\deg m(x)$, we get $\deg(r(x)-s(x))<\deg m(x)$.
    1. Given $m(x)\mid(r(x)-s(x))$ and $\deg(r(x)-s(x))<\deg m(x)$, we get $\deg(r(x)-s(x))=-\infty$ or $r(x)=s(x)$.

# 14.7

1. $x^2-4x+77$.
1. $498$.
1. $3x^2+3$.
1. $x+1$.

# 14.8

> **Proposition 14.2** Let $F$ be a field, $m(x)\in F[x]$, $\deg m(x)>0$.
>
> 1. Suppose $a(x),b(x),c(d)\in F[x]$ satisfy $a(x)\equiv b(x)\pmod{m(x)}$ and $b(x)\equiv c(x)\pmod{m(x)}$. Then $a(x)\equiv c(x)\pmod{m(x)}$.
> 1. Suppose $a(x),b(x),e(d),f(x)\in F[x]$ satisfy $a(x)\equiv e(x)\pmod{m(x)}$ and $b(x)\equiv f(x)\pmod{m(x)}$. Then $a(x)+b(x)\equiv e(x)+f(x)\pmod{m(x)}$ and $a(x)b(x)\equiv e(x)f(x)\pmod{m(x)}$.
> 1. Suppose $a(x),b(x),r(d)\in F[x]$ satisfy $a(x)\equiv b(x)\pmod{m(x)}$. Then $r(x)a(x)\equiv r(x)b(x)\pmod{m(x)}$.

1. Given $a(x)\equiv b(x)\pmod{m(x)}$, we have $m(x)\mid(a(x)-b(x))$. Similarily, we have $m(x)\mid(b(x)-c(x))$. Therefore, $m(x)\mid((a(x)-b(x))+(b(x)-c(x))$, which implies $a(x)\equiv c(x)\pmod{m(x)}$.
1.  1. Given $a(x)\equiv e(x)\pmod{m(x)}$, we have $m(x)\mid(a(x)-e(x))$. Similarily, we have $m(x)\mid(b(x)-f(x))$. Therefore, $m(x)\mid((a(x)-e(x))+(b(x)-f(x))$, which implies $m(x)\mid((a(x)+b(x))-(e(x)+f(x))$, which implies $a(x)+b(x)\equiv e(x)+f(x)\pmod{m(x)}$.
    1. Given $a(x)\equiv e(x)\pmod{m(x)}$, we have $\exists\alpha(x)\in F[x]:a(x)=e(x)+\alpha(x)m(x)$. Similarily, we have $\exists\beta(x)\in F[x]:b(x)=f(x)+\beta(x)m(x)$. Therefore, $\exists\alpha(x),\beta(x)\in F[x]:a(x)b(x)-e(x)f(x)=(e(x)+\alpha(x)m(x))(f(x)+\beta(x)m(x))-e(x)f(x)=(\alpha(x)f(x)+\beta(x)e(x))m(x)+\alpha(x)\beta(x)m^2(x)$, which is a multiple of $m(x)$. Therefore, $a(x)b(x)\equiv e(x)f(x)\pmod{m(x)}$.
1. Given $a(x)\equiv b(x)\pmod{m(x)}$, we have $m(x)\mid(a(x)-b(x))$, which implies $m(x)\mid(a(x)-b(x))r(x)$, which implies $r(x)a(x)\equiv r(x)b(x)\pmod{m(x)}$.

# 14.9

> **Theorem 14.3.** Let $F$ be a field, $r(x)$ and $m(x)$ are coprime polynomials in $F[x]$, and $\deg m(x)>0$. If $a(x)$ and $b(x)$ are polynomials for which $r(x)a(x)\equiv r(x)b(x)\pmod{m(x)}$, then $a(x)\equiv b(x)\pmod{m(x)}$.

1. Given $r(x)a(x)\equiv r(x)b(x)\pmod{m(x)}$, we have $m(x)\mid r(x)(a(x)-b(x))$.
1. Given $m(x)\mid r(x)(a(x)-b(x))$ and $m(x)$ is coprime to $r(x)$, by Theorem 12.12, we have $m(x)\mid(a(x)-b(x))$. Therefore, $a(x)\equiv b(x)\pmod{m(x)}$.

# 14.10

1. The set of polynomials in $\mathbb R[x]$ whose constant term is 3.
1. The set of polynomials in $\mathbb F_2[x]$ who has odd number of coeficients of [1], or has odd number of term not counting zero-coefficient terms.

# 14.11

> **Theorem 14.4.** Let $F$ be a field and $m(x)$ be a polynomial in $F[x]$ of positive degree $n$. Let $q(x)$ be a polynomial in $F[x]$. Then the congruence class of $q(x)$ modulo $m(x)$ consists of all polynomials of the form $p(x)m(x)+q(x)$ for $p(x)$ being an element of $F[x]$.

By the definition of congruence, the congruence class of $q(x)$ modulo $m(x)$ is $\{\alpha(x):\alpha(x)-q(x)=p(x)m(x),p(x)\in F[x]\}$, which equals $\{p(x)m(x)+q(x):p(x)\in F[x]\}$, which proves the theorem.

# 14.13

1.  Given $e(x)\in[a(x)]_{m(x)}$ and $f(x)\in[b(x)]_{m(x)}$, we have $e(x)\equiv a(x)\pmod{m(x)}$ and $f(x)\equiv b(x)\pmod{m(x)}$, which by Proposition 14.2 implies $a(x)+b(x)\equiv e(x)+f(x)\pmod{m(x)}$ and $a(x)b(x)\equiv e(x)f(x)\pmod{m(x)}$, which implies $[e(x)+f(x)]_{m(x)}=[a(x)+b(x)]_{m(x)}$ and $[e(x)f(x)]_{m(x)}=[a(x)b(x)]_{m(x)}$.
1. Define $[a(x)]_{m(x)}+[b(x)]_{m(x)}=[a(x)+b(x)]_{m(x)}$ and $[a(x)]_{m(x)}[b(x)]_{m(x)}=[a(x)b(x)]_{m(x)}$.
1. With such definitions, we have $[0]_{m(x)}+[a(x)]_{m(x)}=[a(x)]_{m(x)}$ and $[1]_{m(x)}[a(x)]_{m(x)}=[a(x)]_{m(x)}$. Therefore, $[0]_{m(x)}$ is an additive identity and $[1]_{m(x)}$ is a multiplicative identity. Furthermore, the set of congruence classes modulo $m(x)$ is a ring since it is
    1. associative for multiplication,
    1. distributive for multiplication over addition,
    1. closed under addition, and
    1. closed under multiplication.

# 14.14

1. Set $\mathbb F_2[x]_{x^2}$ is a ring since it is closed under multiplication and addition according to the following addition table and multiplication table. But it is not a field since $x$ does not have a multiplicative inverse.
\begin{tabular}{r|rrrr}
\toprule
$+$ & 0 & 1 & $x$ & $x+1$ \\
\midrule
0 & 0 & 1 & $x$ & $x+1$ \\
1 & 1 & 0 & $x+1$ & $x$ \\
$x$ & $x$ & $x+1$ & $0$ & $1$ \\
$x+1$ & $x+1$ & $x$ & $1$ & $0$ \\
\bottomrule
\end{tabular}
\begin{tabular}{r|rrrr}
\toprule
$\times$ & 0 & 1 & $x$ & $x+1$ \\
\midrule
0 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & $x$ & $x+1$ \\
$x$ & 0 & $x$ & $0$ & $x$ \\
$x+1$ & 0 & $x+1$ & $x$ & $1$ \\
\bottomrule
\end{tabular}
1. Ring $F[x]_x$ can be represented by the remainders of every polynomial in $F[x]$ modulo $x$, which is all constants in $F[x]$, which is $F$ itself. Therefore, ring $F[x]_x$ can be identified with $F$ itself.
1. For every degree-1 polynomial $m(x)\in F[x]$, $F$ and $m(x)\in F[x]$ are bijectively mapped such that
    1. every element $c$ in $F$ lies in an congruence class $[c]_{m(x)}$ in $F[x]_{m(x)}$;
    1. every congruence class $[a(x)]_{m(x)}$ in $F[x]_{m(x)}$ contains an element in $F$, which is the remainder of $a(x)$ modulo $m(x)$.

    Therefore, $F[x]_{m(x)}$ is isomorphic to $F$.

# 14.15

Let $K$ be the collection of congruence classes of constants.

1. Set $K$ is closed under addition and multiplication since
    1. $\forall a,b\in F:[a]_{m(x)}+[b]_{m(x)}=[a+b]_{m(x)}$;
    1. $\forall a,b\in F:[a]_{m(x)}[b]_{m(x)}=[ab]_{m(x)}$.

    Therefore, $K$ is a ring. Since
    1. $F[x]_{m(x)}=\{[a(x)]_{m(x)}:\deg a(x)<\deg m(x)\}$ and
    1. $K=\{[c]_{m(x)}:c\in F\}$,

    we have $K\subseteq F[x]_{m(x)}$.
1. Ring $F$ and $K$ are bijectively mapped such that
    1. $\forall a\in F:a\in[a]_{m(x)}\in K$.
    1. $\forall [a]_{m(x)}\in K:a\in[a]_{m(x)},a\in F$.

    Therefore, ring $K$ is isomorphic to $F$.
1. This generalizes part 3 of Exercise 14.14 since $m(x)$ could be of any positive degree.

# 14.17

1. $a(\gamma)=a\left([x]_{m(x)}\right)=[a(x)]_{m(x)}$
1. Since every $a(\gamma)$ in $K$ is identified with a unique $[a(x)]_{m(x)}$ in $F[x]_{m(x)}$ and vise versa, $K$ and $F[x]_{m(x)}$ are isomorphic.

# 14.18

> **Theorem 14.7.** Let $F$ be a field, let $a(x)$ and $b(x)$ be polynomials in $F[x]$ with gcd $d(x)$, and let $e(x)$ be a polynomial in $F[x]$. Then equation $a(x)U+b(x)V=e(x)$ has a polynomial solution if and only if $d(x)\mid e(x)$.

1. Assume equation $a(x)U+b(x)V=e(x)$ has a solution, say $U=r(x)$ and $V=s(s)$. Given $d(x)\mid a(x)$ and $d(x)\mid b(x)$, we have $d(x)\mid (a(x)r(x)+b(x)s(x))$, i.e. $d(x)\mid e(x)$.
1. Assume $d(x)\mid e(x)$, i.e., $e(x)=c(x)d(x)$ for some $c(x)$. By Bézout's theorem, we have $a(x)r(x)+b(x)s(x)=d(x)$ for some $r(x)$ and $s(x)$. Multiplying through with $c(x)$ yields $a(x)c(x)r(x)+b(x)c(x)s(x)=c(x)d(x)$, which gives a solution to $a(x)U+b(x)V=e(x)$, namely $U=c(x)r(x)$ and $V=c(x)s(x)$.

# 14.19

1. $(x^2+1)(-x^2+1)+(x^3)(x)=1$ in $\mathbb Q[x]$.
1. Assuming $x^2U+x^3V=x^4+5$, since $x\mid x^2$, $x\mid x^3$, we have $x\mid(x^4+5)$, which is false. Therefore, equation $x^2U+x^3V=x^4+5$ is unsolvable in $\mathbb F_7[x]$.
1. $(x^3+1)(x^2+x)+(x^3+x^2+x+1)(x^2+1)=x^2+1$ in $\mathbb F_2[x]$.

# 14.20

$(x^3+3x+1)(-\frac{31}{113}x^3+\frac8{113}x^2-\frac{13}{113}x+\frac7{113})\equiv1\pmod{x^4+1}$.

# 14.21

> **Theorem 14.8.** Let $F$ be a field. Let $a(x)$ and $m(x)$ be polynomials in $F[x]$ with $m(x)$ of positive degree. The congruence $a(x)U\equiv1\pmod{m(x)}$ is solvable if and only if $\gcd(a(x),m(x))=1$.

1. Assume equation $a(x)U\equiv1\pmod{m(x)}$ is solvable.
    1. By assumption, we have $a(x)\alpha(x)+m(x)\beta(x)=1$ for some polynomials $\alpha(x)$ and $\beta(x)$ in $F[x]$.
    1. Let $d(x)$ be a common divisor of $a(x)$ and $m(x)$ in $F[x]$. By assumption, we have $d(x)\mid(a(x)\alpha(x)+m(x)\beta(x))$, which implies $d(x)\mid1$, which $\deg d(x)=1$. Therefore, any common divisor of $a(x)$ and $m(x)$ in $F[x]$ is of degree 1.
    1. Therefore, $\gcd(a(x),m(x))=1$.
1. Assume $\gcd(a(x),m(x))=1$.
    1. By assumption and Bézout's theorem, we have $a(x)\alpha(x)+m(x)\beta(x)=1$ for some polynomials $\alpha(x)$ and $\beta(x)$ in $F[x]$, which implies $a(x)\alpha(x)\equiv1\pmod{m(x)}$, which implies equation $a(x)U\equiv1\pmod{m(x)}$ is solvable.

# 14.22

> **Theorem 14.10.** Let $F$ be a field. Let $a(x)$ and $m(x)$ be polynomials in $F[x]$ with $m(x)$ of positive degree. The congruence class $[a(x)]_{m(x)}$ is a unit in $F[x]_{m(x)}$ iff $\gcd(a(x),m(x))=1$.

1. By Theorem 14.8, $\gcd(a(x),m(x))=1$ iff $a(x)$ has an multiplicative inverse $a(x)^{-1}$ in $F[x]$.
1. $a(x)a(x)^{-1}=1\iff[a(x)]_{m(x)}[a(x)^{-1}]_{m(x)}=1$.
1. Congruence class $[a(x)]_{m(x)}$ has an multiplicative inverse iff $[a(x)]_{m(x)}$ is a unit in $F[x]_{m(x)}$.
1. Therefore, the congruence class $[a(x)]_{m(x)}$ is a unit in $F[x]_{m(x)}$ iff $\gcd(a(x),m(x))=1$.

# 14.23

Let $F$ be a field and $m(x)$ be a reducible polynomial of positive degree. Since $m(x)$ is reducible, we have nontrivial factorization $m(x)=a(x)b(x)$ in $F[x]$.

1.  1. Assume $[a(x)]_{m(x)}$ is a zero element $F[x]_{m(x)}$. We will disprove it by contradiction.
        1. Assume $a(x)$ is a zero element in $F[x]$, $m(x)=a(x)b(x)$ is zero, contradicting the fact that $m(x)$ is of positive degree. Therefore, $a(x)$ is not a zero element in $F[x]$.
        1. Given $a(x)$ is zero and $[a(x)]_{m(x)}$ is nonzero, we have $a(x)=m(x)\alpha(x)$ for some $\alpha(x)$ in $F[x]$. Given $a(x)=m(x)\alpha(x)$ and $m(x)=a(x)b(x)$, we have $m(x)=a(x)$, which implies $b(x)=1$, contradicting the fact that $m(x)=a(x)b(x)$ is a nontrivial factorization. Therefore, $[a(x)]_{m(x)}$ is not a zero element $F[x]_{m(x)}$.
    1. Similarily, $[b(x)]_{m(x)}$ is not a zero element $F[x]_{m(x)}$.
1. $[a(x)]_{m(x)}[b(x)]_{m(x)}=[a(x)b(x)]_{m(x)}=[m(x)]_{m(x)}=[0]$.
1. Therefore, ring $F[x]_{m(x)}$ has two zero-divisors and is not a field.

# 14.24

> **Exercise 14.24.** Let $F$ be a field and suppose $m(x)$ is an irreducible polynomial in $F[x]$. Show that $F[x]_{m(x)}$ is a field.

Given $m(x)$ is irreducible, by Bézout's theorem, for every $a(x)$ in $F[x]$, we have $1=a(x)\alpha(x)+m(x)\beta(x)$ for some $\alpha(x)$ and $\beta(x)$ in $F[x]$, which implies $1\equiv \alpha(x)a(x)\pmod{m(x)}$. Therefore, every polynomial has a multiplicative inverse in $F[x]_{m(x)}$. Therefore, $F[x]_{m(x)}$ is a field.

# 14.25

> **Theorem 14.12.** Suppose that $F$ is a field and that $m(x)$ is an irreducible polynomial in $F[x]$. The ring $F[x]_{m(x)}$ is a field extension of $F$ in which the element $[x]_{m(x)}$ is a root of $m(x)$.

Given $m(x)$ is a polynomial in $F[x]$, we have $m\left([x]_{m(x)}\right)=[m(x)]_{m(x)}=0$, i.e., $[x]_{m(x)}$ is a root of $m(x)$.
