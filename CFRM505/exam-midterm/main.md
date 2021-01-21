---
title: CFRM 505, 2021 Winter, Midterm
...

# 1

## 1.a

Letting $1=\int_\mathbb Rf(x)\diff x$, or $1=\int_0^1(\alpha x+2\alpha x^3)\diff x$ yields

$$\alpha=1\,.$$

## 1.b

Since $F(x)=\frac{x^4}2+\frac{x^2}2$ when $x\in[0,1]$, we have the the following algorithm.

1. Generate independent uniform RVs $u_0, u_1\sim U(0,1)$.
1. If $u_0<1/2$, output $u_1^{1/2}$. Otherwise, output $u_1^{1/4}$.

### Script

\inputminted{python}{q1/b.py}

### Result

The simulated result is $\E(X)=0.734612$ and $\Var(X)=0.0446742$.

![](q1/b.pdf)

## 1.c

Let $g(x)=1,x\in[0,1]$, we have

$$a=\sup_{x\in[0,1]}\frac{f(x)}{g(x)}=3\,.$$

### Script

\inputminted{python}{q1/c.py}

### Result

The simulated result is $\E(X)=0.734073$ and $\Var(X)=0.0454563$.

![](q1/c.pdf)

# 2

## 2.a

$$
\Pr(X\le x|a\le X\le b)=\begin{cases}
0\,, &
x\in(-\infty,a)\,, \\
\frac{F(x)-F(a)}{F(b)-F(a)}\,, &
x\in[a,b)\,, \\
1\,, &
x\in[b,\infty)\,.
\end{cases}
$$

## 2.b

Letting $1=\int_a^bf(x)\diff x$ yields $C=\frac1{e^{-\lambda a}-e^{-\lambda b}}$.

Integrating the PDF $f_Y(x)$ yields the CDF $F_Y(x)=\frac{e^{-\lambda x}-e^{-\lambda a}}{e^{-\lambda b}-e^{-\lambda a}}$.

Inverting the CDF $F_Y(x)$ yields the quantile function $F_Y^{-1}(u)=-\frac1\lambda\ln[e^{-\lambda a}+(e^{-\lambda b}-e^{-\lambda a})u]$.

Plugging $a=1,b=3,\lambda=0.5$ yields $C=\frac1{e^{-1/2}-e^{-3/2}}$ and $F_Y^{-1}(u)=3-2\ln[e+(1-e)u]$.

The algorithm for simulating $Y$ is listed as follows.

1. Generate RV $u\sim\text{U}(0,1)$.
1. Output $Y:=3-2\ln[e+(1-e)u]$.

### Script

\inputminted{python}{q2/main.py}

### Result

The simulated result is $\E(Y)=1.83389$ and $\Var(Y)=0.317622$.

![](q2/main.pdf)

# 3

Plugging the parameters of $Y$ and $\widetilde Y$ into the quantile function $F_Y^{-1}(u)$ in **(2)** yields

$$F_Y^{-1}(u)=3-2\ln\left[e+\left(1-e\right)u\right]\,,$$

and

$$F_{\widetilde Y}^{-1}(u)=5-\ln\left[e^3+\left(1-e^3\right)u\right]\,.$$

### Script

\inputminted{python}{q3/main.py}

### Result

![](q3/main.pdf)

# 4

### Script

\inputminted{python}{q4/main.py}

### Result

$$\E(X_2)=15.0693\,,\quad\Var(X_2)=27.0870\,,$$
$$\E\left(\widetilde X_2\right)=10.0528\,,\quad\Var\left(\widetilde X_2\right)=2.9954\,.$$

![](q4/main.pdf)

# 5

Let the control variate be $Z=e^{V+W}$, we have

$$\E\left(e^V\right)=\int_{-0.5}^{1.5}\frac12e^v\diff v=\frac{e^{1.5}-e^{-0.5}}{2}$$

$$\E\left(e^W\right)=e^{0.8}$$

$$\E(Z)=\E\left(e^V\right)\E\left(e^W\right)=\frac{e^{2.3}-e^{0.3}}2\approx4.31216$$

### Script

\inputminted{python}{q5/main.py}

### Result

\begin{center}\begin{tabular}{lrrr}
\toprule
& Mean & Std. & 95\% Conf. Interval \\
\midrule
Crude MC        & 3.03133 & 10.62813 & (2.93818, 3.12449) \\
Control variate & 3.07359 &  0.73431 & (3.06716, 3.08003) \\
\bottomrule
\end{tabular}\end{center}

The variance is significantly reduced by 99.5226\%.
