---
title: MATH 411, 2021 Summer, Chapter 2
...

# 2.7

> **Proposition.** Suppose $n$, $a$, and $b$ are integers, and $n$ divides both $a$ and $b$. Then $n$ divides $a+b$ and $a-b$.

Since $n$ divides both $a$ and $b$, there exist integers $m$ and $l$ such that $a=mn$ and $b=ln$, which implies $a+b=(m+l)n$ and $a-b=(m-l)n$. Since $m$ and $l$ are integers, $m+l$ and $m-l$ are also integers. Therefore, $n$ divides $m+n$ and $m-n$.

> **Proposition.** Suppose $r$ divides $s$ and $s$ divides $t$. Then $r$ divides $t$.

Since $r$ divides $s$ and $s$ divides $t$, there exist integers $m$ and $l$ such that $s=mr$ and $t=ls$, which implies $t=(lm)r$. Therefore, $r$ divides $t$.

# 2.8

1. Since there are only two non-negative integers that are less than 2, the division theorem can be restated as given in the special case $a=2$.
1.  a. Integer 1 has one of the two given forms since $1=2\times0+1$.
    a. We will assume that some integer $k\ge1$ has the form $2q$ or $2q+1$ for some non-negative integer $q$, and show that $k+1$ also has one of the two forms under that assumption.
        i. In the case that $k=2q$, $k+1$ can be written as the second form since $k+1=2q+1$;
        i. in the case that $k=2q+1$, $k+1$ can be written as the first form since $k+1=2(q+1)$.
    a. We have shown that 1 has one of the two forms. We have also shown that if some integer $k\ge1$ has one of the two forms, $k+1$ also has one of the two forms. By the principle of induction, we can conclude that every positive integer has the form $2q$ or $2q+1$ for some non-negative integer $q$.

# 2.9

1. Integer 1 has one of the three forms since $1=3\times0+1$.
1. We will assume that some integer $k\ge1$ has the form $3q$, $3q+1$, or $3q+2$, for some non-negative integer $q$, and show that $k+1$ also has one of the three forms under that assumption.
    i. In the case that $k=3q$, $k+1$ can be written as the second form since $k+1=3q+1$;
    i. in the case that $k=3q+1$, $k+1$ can be written as the third form since $k+1=3q+2$;
    i. in the case that $k=3q+2$, $k+1$ can be written as the first form since $k+1=3(q+1)$.
1. We have shown that 1 has one of the three forms. We have also shown that if some integer $k\ge1$ has one of the three forms, $k+1$ also has one of the three forms. By the principle of induction, we can conclude that every positive integer has the form $3q$, $3q+1$, or $3q+2$, for some non-negative integer $q$.

# 2.10

Let Theorem$(b)$ be

> For a given positive integer $b$ and every positive integers $a$, there exist non-negative integers $q$ and $r$, with $r<a$ such that $b=aq+r$.

1. We will prove Theorem$(1)$ in two cases: $a=1$ and $a>1$.
    i. In the case that $a=1$, Theorem$(1)$ is obvious since $1=aq+r$ for $q=1$ and $r=0$;
    i. in the case that $a>1$, Theorem$(1)$ is obvious since $1=aq+r$ for $q=0$ and $r=1$.
1. We will prove Theorem$(k+1)$ under the assumption of Theorem$(k)$. Assuming Theorem$(k)$, there exist non-negative integers $q$ and $r$, with $r<a$, for every positive integer $a$ such that $k=aq+r$. We will prove Theorem$(k+1)$ in two cases.
    i. In the case that $r\in\{0,\dots,a-2\}$, Theorem$(k+1)$ is true since $k+1=aq+(r+1)$;
    i. in the case that $r=a-1$, Theorem$(k+1)$ is true since $k+1=a(q+1)+0$.
1. We have proven Theorem$(1)$. We have also proven Theorem$(k+1)$ under the assumption of Theorem$(k)$. By the principle of induction, we can conclude that Theorem$(b)$ is true for every positive integer $b$, which implies that the division theorem is true.

# 2.11

Given that $0\le r<a$ and $0\le t<a$, we have

\begin{equation}-a<r-t<a\,.\end{equation}

Given that $b=aq+r$ and $b=as+t$, we have

\begin{equation}r-t=(s-q)a\,.\end{equation}

Plugging (2) into (1) and dividing by $a$ yields

$$-1<s-q<1\,.$$

Thus $s-q$ is an integer strictly between 1 and $-1$, which could only be 0. Therefore, $q=s$, which implies $r=t$.
