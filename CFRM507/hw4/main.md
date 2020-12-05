---
title: CFRM 507, 2020 Autumn, HW 4
...

# 1

## AMPL model

\inputminted{ampl}{q1/main.mod}

## Results

\begin{center}\begin{tabular}{lrrr}
\toprule
& A & B & C \\
\midrule
$\alpha$ & -0.000043 & -0.000140 & -0.000104 \\
XLB      &         0 &  0.097305 &  0.036989 \\
XLC      &  0.177815 &         0 &         0 \\
XLY      &  0.159261 &  0.264768 &  0.184068 \\
XLP      &         0 &         0 &  0.164180 \\
XLE      &         0 &  0.180655 &  0.077833 \\
XLF      &         0 &  0.017686 &  0.257464 \\
XLV      &  0.181227 &  0.261015 &  0.155407 \\
XLI      &         0 &         0 &  0.092733 \\
XLRE     &         0 &  0.178572 &  0.031326 \\
XLK      &  0.481696 &         0 &         0 \\
XLU      &         0 &         0 &         0 \\
\bottomrule
\end{tabular}\end{center}

# extra 1

The objective function is

$$\max\quad f(C,T)=10C\ln C+90C+250T\ln T+80T\,.$$

It is a convex function for $C,T>0$ since its Hessian matrix

$$\begin{pmatrix}
    10/C & 0 \\
    0 & 250/T \\
\end{pmatrix}$$

is positive definite when $C$ and $T$ are both positive. However, since it is a maximization problem, this does not make it a convex optimization problem.

## AMPL model

\inputminted{ampl}{qe1/main.mod}

## Results

The optimal production schedule is given by

$$C=251.333\,,\quad T=68.5833\,.$$

# extra 2

Yes. Even through the feasible region is not convex, it is the union of four convex hulls. We can define four corresponding subproblems, and the best result among the four should be the result for the original problem.

# extra 3

**Proposition:** Given that $g$ is a non-increasing convex function and $f$ is is a concave function, then $g\circ f$ is convex.

**Proof**

Let $a$ be a real number in $[0,1]$. Since $f$ is concave, we have

$$af(x)+(1-a)f(y)\le f(ax+(1-a)y)\,.$$

Since $g$ is non-increasing, we have

\begin{equation}g(af(x)+(1-a)f(y))\ge g(f(ax+(1-a)y))\,.\end{equation}

Since $g$ is convex, we have

\begin{equation}g(af(x)+(1-a)f(y))\le ag(f(x))+(1-a)g(f(y))\,.\end{equation}

Connecting (2) and (3) yields

$$g(f(ax+(1-a)y))\le ag(f(x))+(1-a)g(f(y))\,.$$

That is, $g\circ f$ is convex.

# extra 4

**Proposition:** Given that $f_i(x)$ is a convex function for all $i\in\{1,\dots,n\}$, then $\sum_{i=1}^nf_i(x)$ is a convex function.

**Proof**

Given that $f_i(x)$ is a convex function for all $i\in\{1,\dots,n\}$, we have

$$\forall a\in[0,1],i\in\{1,\dots,n\}:f_i(ax+(1-a)y)\le af_i(x)+(1-a)f_i(y)\,.$$

Summing the $n$ inequalities yields

$$\forall a\in[0,1]:\sum_{i=1}^nf_i(ax+(1-a)y)\le\sum_{i=1}^naf_i(x)+(1-a)f_i(y)\,,$$

or

$$\forall a\in[0,1]:\sum_{i=1}^nf_i(ax+(1-a)y)\le a\left(\sum_{i=1}^nf_i(x)\right)+(1-a)\left(\sum_{i=1}^nf_i(y)\right)\,,$$

That is, $\sum_{i=1}^nf_i(x)$ is a convex function.

# extra 5

$$
\begin{pmatrix}
16 &  28 &  4 &  20 \\
28 & 130 & 52 &  80 \\
 4 &  52 & 30 &  46 \\
20 &  80 & 46 & 123 \\
\end{pmatrix}
=
\begin{pmatrix}
4 & 0 & 0 & 0 \\
7 & 9 & 0 & 0 \\
1 & 5 & 2 & 0 \\
5 & 5 & 8 & 3 \\
\end{pmatrix}
\begin{pmatrix}
4 & 7 & 1 & 5 \\
0 & 9 & 5 & 5 \\
0 & 0 & 2 & 8 \\
0 & 0 & 0 & 3 \\
\end{pmatrix}
$$
