---
title: MATH 412, 2021 Summer, Chapter 15
...

# 15.1

> **Theorem 15.1.** Let $R$ be the ring of integers or the ring of polynomials over a field and let $N$ be the measure of size for $R$.
>
> 1. The unique element of $R$ of smallest size is 0.
> 1. The elements of $R$ of the second-smallest size are precisely the units of $R$.
> 1. The elements of $R$ of the third-smallest size are irreducible.
> 1. If $a$ and $b$ are nonzero elements of $R$, then $N(a)\le N(ab)$. Moreover, equality holds iff $b$ is a unit.

1. Suppose $R=\mathbb Z$.
    1. The unique element of $R$ of smallest size is integer 0.
    1. The elements of $R$ of the second-smallest size are $-1$ and 1, which are precisely the units of $R$.
    1. The elements of $R$ of the third-smallest size are $-2$ and 2, which are irreducible.
    1. If $a$ and $b$ are nonzero integers, then $N(ab)=|ab|=|a||b|=N(a)N(b)\ge N(a)$, while the equality holds iff $b$ is $-1$ or $1$.
1. Suppose $R=K[x]$ over field $K$.
    1. The unique element of $R$ of smallest size is polynomial $0$.
    1. The elements of $R$ of the second-smallest size are nonzero constants, which are precisely the units of $R$.
    1. The elements of $R$ of the third-smallest size are polynomials of degree one, which are irreducible.
    1. If $a$ and $b$ are nonzero constants, then $N(ab)=\deg (ab)=\deg a+\deg b=N(a)+N(b)\ge N(a)$, while the equality holds iff $b$ is a nonzero constant.

# 15.2

> **Theorem 15.2.** Let $R$ be the ring of integers or the ring of polynomials over a field. Suppose $r$ is an element of $R$ that is not zero or a unit.
>
> 1. If $r=ab$ is a nontrivial factorization of $r$, then $N(a)<N(r)$ and $N(b)<N(r)$.
> 1. Either $r$ is irreducible, or $r$ is a product of irreducible elements.

1. If $r=ab$ is a nontrivial factorization, then both $a$ and $b$ are not units, which by Theorem 15.1 implies $N(a)<N(r)$ and $N(b)<N(r)$.
1. Since $r$ is neither zero nor a unit, by Theorem 15.1, $N(r)$ is at least of the third smallest size. We will prove the second statement by induction.
    1. If $r$ is of the third smallest size, by Theorem 15.1, $r$ is irreducible.
    1. Assume the proposition holds for every element with a size less than $k$, i.e., $\rho$ is either irreducible or a product of irreducible elements for every $\rho\in R$ and $N(\rho)<k$. Let $N(r)=k$.
        1. If $r$ does not have a nontrivial factorization, then $r$ is irreducible.
        1. Assume $r$ has a nontrivial factorization $r=ab$. by the first statement proved above, we have $N(a)<k$ and $N(b)<k$. By assumption, both $a$ and $b$ are either irreducible or a product of irreducible elements. Therefore, $r$ is a product of irreducible elements.
    1. By the principle of induction, every nonzero nonunit element of $R$ is either irreducible or a product of irreducible elements.

# 15.3

> **Exercise 15.3.** Suppose $a$ and $b$ are complex numbers.
>
> 1. Verify that $N(ab)=N(a)N(b)$.
> 1. Check that if $a$ is in $\mathbb Z\left[\sqrt{-m}\right]$, then $N(a)$ is an integer.
> 1. Deduce that if $a$ and $b$ are both in $\mathbb Z\left[\sqrt{-m}\right]$, then $N(a)N(b)$ is a factorization of integer $N(ab)$ as a product of two integers.

1. Let $r,s,t,u$ be real numbers such that $a=r+si$ and $b=t+ui$. $N(ab)=N((r+si)(t+ui))=N((rt-su)+(ru+st)i)=(rt-su)^2+(ru+st)^2=(r^2+s^2)(t^2+u^2)=N(r+si)N(t+ui)=N(a)N(b)$.
1. Given $a\in\mathbb Z\left[\sqrt{-m}\right]$, let $m,r,s$ be integers such that $a=r+s\sqrt{-m}$. We have $N(a)=N\left(r+s\sqrt{-m}\right)=r^2+ms^2\in\mathbb Z$.
1. Given $a,b\in\mathbb Z\left[\sqrt{-m}\right]\subset\mathbb C$, by the first statement, we have $N(ab)=N(a)N(b)$. Given $a,b,ab\in\mathbb Z\left[\sqrt{-m}\right]$, by the second statement, $N(a)$, $N(b)$, and $N(a+b)$ are all integers. Therefore, $N(a)N(b)$ is a factorization of integer $N(ab)$ as a product of two integers.

# 15.4

Let $s+t\sqrt{-m}$ be an element of $\mathbb Z\left[\sqrt{-m}\right]$ with $s,t\in\mathbb Z$. We have $N(s+t\sqrt{-m})=s^2+mt^2$.

1. The smallest size is $N(0)=0$.
1. The elements of $R$ of the second-smallest size are precisely the units of $R$.
    1. If $m=1$, the second-smallest size is $N(1)=N(-1)=N(-i)=N(i)=1$.
    1. If $m>1$, the second-smallest size is $N(-1)=N(1)=1$.
1. The elements of $R$ of the third-smallest size are irreducible.
    1. If $m=1$, the third-smallest size is $N(\pm1\pm\sqrt{-1})=2$.
    1. If $m=2$ or $m=3$, the third-smallest size is $N(\pm\sqrt{-m})=m$.
    1. If $m=5$, the third-smallest size is $N(\pm2)=4$.
1. Let $a$ and $b$ be two nonzero elements of $R$. As proved in Exercise 15.3, we have $N(ab)=N(a)N(b)$. In particular, $N(ab)\ge N(a)$ while the equality holds iff $b$ is a unit.

# 15.5

1. If $r=ab$ is a nontrivial factorization, then both $a$ and $b$ are not units, which by Theorem 15.4 implies $N(a)<N(r)$ and $N(b)<N(r)$.
1. Since $r$ is neither zero nor a unit, by Theorem 15.4, $N(r)$ is at least the third smallest size. We will prove the second statement by induction.
    1. If $r$ is of the third smallest size, by Theorem 15.4, $r$ is either $\pm1\pm\sqrt{-m}$, $\pm\sqrt{-m}$, or $\pm2$, depending on $m$, which implies $r$ is either irreducible or a product of irreducible elements.
    1. Assume the proposition holds for every element with a size less than $k$, i.e., $\rho$ is either irreducible or a product of irreducible elements for every $\rho\in\mathbb Z\left[\sqrt{-m}\right]$ and $N(\rho)<k$. Let $N(r)=k$.
        1. If $r$ does not have a nontrivial factorization, then $r$ is irreducible.
        1. Assume $r$ has a nontrivial factorization $r=ab$. by the first statement proved above, we have $N(a)<k$ and $N(b)<k$. By assumption, both $a$ and $b$ are either irreducible or a product of irreducible elements. Therefore, $r$ is a product of irreducible elements.
    1. By the principle of induction, every nonzero nonunit element of $R$ is either irreducible or a product of irreducible elements.

# 15.6

1. Let $r$ and $s$ be integers. Given
    1. $N(r+s\sqrt{-5})=r^2+5s^2$, and
    1. equation $r^2+5s^2=k$ with $k\in\{2,3,7,8\}$ is not solvable in $\mathbb Z$ (we can prove this by enumerating $r$ and $s$),

    we have $\mathbb Z\left[\sqrt{-5}\right]$ has no elements of norm 2, 3, 7, or 8.
1.  1. All elements in $\mathbb Z\left[\sqrt{-5}\right]$ of norm 4 are $\pm2$.
    1. All elements in $\mathbb Z\left[\sqrt{-5}\right]$ of norm 5 are $\pm\sqrt{-5}$.
    1. All elements in $\mathbb Z\left[\sqrt{-5}\right]$ of norm 6 are $\pm1\pm\sqrt{-5}$.
    1. All elements in $\mathbb Z\left[\sqrt{-5}\right]$ of norm 9 are $\pm2\pm\sqrt{-5}$ and $\pm3$.
1.  Assume $a=bc$ is a nontrivial factorization in $\mathbb Z\left[\sqrt{-5}\right]$. As proved in Exercise 15.3, $N(b)$ and $N(c)$ are both integers greater than or equal to 2, and $N(a)=N(b)N(c)$. Therefore, $N(b)$ is a integer factor of $N(a)$ at least 2.
    1. Assume $N(a)=4$. Norm $N(b)$ is 2, contradicting the fact that $\mathbb Z\left[\sqrt{-5}\right]$ has no elements of norm 2. Therefore, elements in $\mathbb Z\left[\sqrt{-5}\right]$ of norm 4 are irreducible.
    1. Similarily, we can prove elements in $\mathbb Z\left[\sqrt{-5}\right]$ of norm 6 or 9 are irreducible.
1. Therefore, 2, 3, and $1\pm\sqrt{-5}$ are irreducible in $\mathbb Z\left[\sqrt{-5}\right]$.
1. Therefore, $2\cdot3$ and $(1-\sqrt{-5})(1+\sqrt{-5})$ are both factorizations of 6 in $\mathbb Z\left[\sqrt{-5}\right]$ as products of irreducible elements.
1. Therefore, elements of $\mathbb Z\left[\sqrt{-5}\right]$ may not have unique irreducible factorizations.

# 15.7

> **Theorem 15.9.** Let $R$ be the ring $\mathbb Z[i]$ of Gaussian integers and let $N$ be the norm function on $R$. For every two nonzero elements $a$ and $b$ of $R$, there exist elements $q$ and $r$ such that $b=aq+r$ and $N(r)<N(a)$.

1. Let $f+gi$ be the quotient $\frac ba$ with $f,g\in\mathbb Q$.
1. Let $q=m+ni$ be the unique Gaussian integer satisfying $m,n\in\mathbb Z$, $-\frac12<f-m\le\frac12$ and $-\frac12<g-n\le\frac12$.
1. Let $r$ be the unique Gaussian integer satisfying $b=aq+r$.
1. $N(r)=N(b-aq)=N(((f-m)+(g-n)i)a)=N(a)N((f-m)+(g-n)i)=N(a)\sqrt{(f-m)^2+(g-n)^2}\le N(a)\sqrt{(\frac12)^2+(\frac12)^2}<N(a)$.
1. Therefore, for every two nonzero elements $a$ and $b$ of $R$, there exist elements $q$ and $r$ satisfying $b=aq+r$ and $N(r)<N(a)$.

# 15.9

> **Theorem 15.12.** Suppose $R$ is a Euclidean ring.
>
> 1. The elements of $R$ of the second-smallest size are precisely the units of $R$.
> 1. The elements of $R$ of the third-smallest size are irreducible.
> 1. Every nonzero, nonunit element of $R$ is irreducible or a product of irreducible elements.

1. We will prove that element $u$ is a unit iff $N(u)=N(1)$.
    1. Let $u$ be an unit of $R$. By Property B, we have $N(1)=N\left(uu^{-1}\right)\ge N(u)$ and $N(u)=N(1u)\ge N(1)$, which implies $N(u)=N(1)$.
    1. Let $a$ be an element of $R$ satisfying $N(a)=N(1)$. By Property C, we have $1=aq+r$ and $N(r)<N(a)$ for some $q$ and $r$ in $R$. Given $N(a)=N(1)$ and $N(r)<N(a)$, we have $N(r)<N(1)$, which by Property A implies $r=0$. Therefore, $1=aq$, which implies $a$ is a unit.
1. We will prove the elements of $R$ of the third-smallest size are irreducible by contraposition.
    1. Assume element $p$ of $R$ is reducible. By assumption, we have $a=bc$ such that $b$ and $c$ are nonzero and nonunit.
    1. Given $a=bc$ and $b$ is nonzero and nonunit, we have $N(a)>N(c)$.
    1. Given $c$ is nonzero and nonunit, $N(c)$ is at least the third-smallest size.
    1. Given $N(a)>N(c)$ and $N(c)$ is at least the third-smallest size, $N(a)$ is greater than the third-smallest size.
    1. Therefore, the size of a reducible element of $R$ is greater than the third-smallest size. Contrapositively, the elements of $R$ of the third-smallest size are irreducible.
1. Let $a$ be a nonzero, nonunit element of $R$. As is proved, $a$ has at least the third-smallest size. We will prove $a$ is either irreducible or a product of irreducible elements by induction.
    1. If $a$ has the third-smallest size, as is proved, $a$ is irreducible.
    1. Assume $N(a)=k$, where $k$ is greater than the third-smallest size. Also assume every element of size less than $k$ is either irreducible or a product of irreducible elements.
        1. Assume $a$ is reducible, i.e., we have non-trivial $a=bc$ where $b$ and $c$ are not units. By Property B and Theorem 15.11, $N(a)>N(b)$ and $N(a)>N(c)$, which implies $k>N(b)$ and $k>N(c)$, which by assumption implies both $b$ and $c$ are either irreducible or a product of irreducible elements. Therefore, $a$ is a product of irreducible elements.

        Therefore, $a$ with size $k$ is either irreducible or a product of irreducible elements.
    1. By the principle of induction, $a$ is either irreducible or a product of irreducible elements.

# 15.11

Every theorem from Theorem 15.13 to Theorem 15.19 holds for $\mathbb Z[i]$ because $\mathbb Z[i]$ is a Euclidean ring thus satisfies Properties A, B, and C.
