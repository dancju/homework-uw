---
title: CFRM 505, 2021 Winter, HW 2
...

# 1

## 1.a

The CDF of $X$ on $[0,1]$ is

\begin{align*}
& F_X(x) \\
=& \Pr(X\le x) \\
=& \Pr(U_1\le x\lor U_2\le x) \\
=& 1-\Pr(U_1>x)\Pr(U_2>x) \\
=& 1-(1-x)(1-x) \\
=& -x^2+2x\,.
\end{align*}

The inverse transform yields

$$F_X^{-1}(u)=1-\sqrt{1-u}\,.$$

### Script

\inputminted{python}{q1/a.py}

### Result

<!-- The analytic result is 1/3. -->

The simulation result is $\E(X)=0.333680$.

## 1.b

The CDF of $X$ on $[0,1]$ is

\begin{align*}
& F_X(x) \\
=& \Pr(X\le x) \\
=& \Pr(U_1\le x\land U_2\le x) \\
=& \Pr(U_1\le x)\Pr(U_2\le x) \\
=& x^2
\end{align*}

The inverse transform yields

$$F_X^{-1}(u)=\sqrt{u}\,.$$

### Script

\inputminted{python}{q1/b.py}

### Result

<!-- The analytic result is 2/3. -->

The simulation result is $\E(X)=0.664150$.

## 1.c

The CDF of $X$ on $[0,\infty)$ is

\begin{align*}
& F_X(x) \\
=& \Pr(X\le x) \\
=& \Pr(Y_1\le x\lor Y_2\le x\lor Y_3\le x) \\
=& 1-\Pr(Y_1>x)\Pr(Y_2>x)\Pr(Y_3>x) \\
=& 1-e^{-3\lambda x}
\end{align*}

The inverse transform yields

$$F_X^{-1}(u)=-\frac{\ln(1-u)}{3\lambda}\,.$$

### Script

\inputminted{python}{q1/c.py}

### Result

<!-- The analytic result is 1/(3λ). -->

Assuming $\lambda=1$, the simulation result is $\E(X)=0.333062$.

# 2

### Script

\inputminted{python}{q2/main.py}

### Result

<!-- The analytic result is 1 and 1. -->

The simulation result is $\E(X)=1.0062$ and $\Var(X)=0.975762$.

# 3

The quantile function of $Y$ is

$$F_Y^{-1}(u)=-\ln(1-u)\,,\quad u\in[0,1]\,.$$

The CDF of $X$ with the condition $Y=y$ is

$$F_{X|Y}(x,y)=x^y\,,\quad x\in[0,1]\,,y\in[0,\infty)\,.$$

The quantile function of $X$ with the condition $Y=y$ is

$$\inf\left\{x:u\le F_{X|Y}(x,y),Y=y\right\}=u^{1/y}\,,\quad u\in[0,1]\,,y\in[0,\infty)\,.$$

### Script

\inputminted{python}{q3/main.py}

### Result

<!-- The analytic result is
    E(X) = 1 + e Ei(-1) ≈ 0.403653
    Var(X) = 2 e^2 Ei(-2) - e^2 Ei(-1)^2 - 2 e Ei(-1) ≈ 0.114407
-->

The simulation result is $\E(X)=0.403797$ and $\Var(X)=0.114054$.

# 4

Let $g(x)=1$ with domain $x\in[0,1]$ and $a=2$.

### Script

\inputminted{python}{q4/main.py}

### Result

<!-- The analytic result is 2. -->

The average number of iterations required for accepting each sample is 1.9975.

# 5

### Script

\inputminted{python}{q5/main.py}

### Result

<!-- The analytic result is
    0
    1
    2 * sqrt(2 * e / pi) ≈ 2.63098
-->

The simulation result is $\E(X)=0.00333$ and $\Var(X)=1.00144$. In the simulation, 2.62040 uniform RV are used on average to generate one normal RV. (Given that it takes 2 uniform RV for each iteration.)

\includegraphics{q5/main.pdf}
