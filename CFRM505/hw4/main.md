---
title: CFRM 505, 2021 Winter, HW 4
...

# 1

## 1.a

### Script

\inputminted{python}{q1/a.py}

### Result

The simulated result is 0.962445.

## 1.b

\begin{align*}
    & \Pr\left(U_a^2+U_b^2<\frac32\middle|U_a=u_a\right) \\
    =& \Pr\left(|U_b|<\sqrt{\frac32-u_a^2}\right) \\
    =& F_U\left(\sqrt{\frac32-u_a^2}\right)-F_U\left(-\sqrt{\frac32-u_a^2}\right)\,.
\end{align*}

Plugging in the CDF of $U_a$ such that

$$F_U(x)=\begin{cases}
    0 & x\in(-\infty,-1)\,, \\
    \frac{x+1}2 & x\in[-1,1)\,, \\
    1 & x\in[1,\infty)\,,
\end{cases}$$

yields

$$
    \Pr\left(U_a^2+U_b^2<\frac32\middle|U_a=u_a\right)
    = \begin{cases}
        1 &  u_a\in\left[-\frac{\sqrt2}2,\frac{\sqrt2}2\right]\,, \\
        \sqrt{\frac32-u_a^2} & \text{otherwise.}
    \end{cases}
$$

### Script

\inputminted{python}{q1/b.py}

### Result

The simulated result is 0.962045.

# 2

The probability for this question under condition $X=x$ is

$$\Pr(X+Y\ge4|X=x)=\Pr(Y\ge4-x)=1-F_Y(4-x)\,.$$

Plugging in the CDF of $Y$, which is $F_Y(x)=1-e^{-x/3}$, yields

$$\Pr(X+Y\ge4|X=x)=\begin{cases}
    e^{\frac{x-4}3} & x\in[0,4)\,, \\
    1 & x\in[4,\infty)\,.
\end{cases}$$

Similarily, we have the other conditional probability such that

$$\Pr(X+Y\ge4|Y=y)=\begin{cases}
    e^{\frac{y-4}2} & y\in[0,4)\,, \\
    1 & y\in[4,\infty)\,.
\end{cases}$$

<!--
\begin{align*}
    & \Var[\Pr(X+Y\ge4|X=x)] \\
    =& \frac12\int_0^4e^{\frac{(x-4)2}3}e^{-\frac x2}\diff x+\frac12\int_4^\infty e^{-\frac x2}\diff x \\
    & -\left(\frac12\int_0^4e^{\frac{x-4}3}e^{-\frac x2}\diff x+\frac12\int_4^\infty e^{-\frac x2}\diff x\right)^2 \\
    =& 4e^{-2}-12e^{-8/3}+12e^{-10/3}-4e^{-4} \\
    \approx& 0.06236508
\end{align*}

\begin{align*}
    & \Var[\Pr(X+Y\ge4|Y=y)] \\
    =& \frac13\int_0^4e^{\frac{(y-4)2}2}e^{-\frac y3}\diff y+\frac13\int_4^\infty e^{-\frac y3}\diff y \\
    & -\left(\frac13\int_0^4e^{\frac{y-4}2}e^{-\frac y3}\diff y+\frac13\int_4^\infty e^{-\frac y3}\diff y\right)^2 \\
    =& \frac{3}{2}e^{-4/3}-9e^{-8/3}+12e^{-10/3}-\frac{9}{2}e^{-4} \\
    \approx& 0.115712
\end{align*} -->

### Script

\inputminted{python}{q2/main.py}

### Result

Simulating $X$ is preferable since it leads to smaller variance such that

$$\Var[\Pr(X+Y\ge4|X=x)]\approx0.062365 < \Var[\Pr(X+Y\ge4|Y=y)]\approx0.115712\,.$$

The estimation of $\Pr(X+Y\ge4)$ is

$$\Pr(X+Y\ge4)=\E[\Pr(X+Y\ge4|X=x)]\approx0.520255\,.$$

# 3

<!-- \begin{align*}
    & \Pr(V>20) \\
    =& 1-F_{X_1}(20)F_{X_2}(20) \\
    =& 1-\left(1-e^{-20}\right)\left(1-e^{-40}\right) \\
    =& -e^{-60}+e^{-40}+e^{-20} \\
    =& 2.06115\times10^{-9}
\end{align*} -->

Given $X_i\sim\text{Exp}(i)$ for $i\in\{1,2\}$, we have the PDFs of $X_{1,2}$ such that

$$f_i(x)=ie^{-ix}\,,\quad x\in[0,\infty),i\in\{1,2\}\,.$$

Let $g_i(x)$ be the PDFs of $X_{1,2}$ under another measure such that

$$g_i(x)=\lambda_ie^{-\lambda_ix}\,,\quad x\in[0,\infty)\,,i\in\{1,2\}\,.$$

We have

$$
    \E_f\left(1_{X_i>20}\right)
    = \E_g\left(\frac{f_i(X_i)}{g_i(X_i)}1_{X_i>20}\right)
    = \frac{i}{\lambda_i}\E_g\left(e^{(-i+\lambda_i)X_i}1_{X_i>20}\right)\,,
$$

and

\begin{align*}
    & \Pr(V>20) \\
    =& 1-(1-\E_f(1_{X_1>20}))(1-\E_f(1_{X_2>20})) \\
    =& 1-\left(1-\frac{1}{\lambda_1}\E_g\left(e^{(-1+\lambda_1)X_1}1_{X_1>20}\right)\right)\left(1-\frac{2}{\lambda_2}\E_g\left(e^{(-2+\lambda_2)X_2}1_{X_2>20}\right)\right)\,,
\end{align*}

where the likelihood ratios for $X_1$ and $X_2$ are $e^{(-1+\lambda_1)X_1}$ and $e^{(-2+\lambda_2)X_2}$.

Through tuning, we get the optimal parameter values $\lambda_1\approx\lambda_2\approx0.05$.

### Script

\inputminted{python}{q3/main.py}

### Result

The estimated result is $2.06895\times10^{-9}$.

# 4

<!-- \begin{align*}
    & \Pr(V>5) \\
    =& [1-F_{X_1}(5)][1-F_{X_2}(5)] \\
    =& [1-\Phi(5)]\left[1-\Phi\left(\frac5{\sqrt2}\right)\right] \\
    =& \left[\frac12-\frac12\text{erf}\left(\frac5{\sqrt{2}}\right)\right]\left[\frac12-\frac12\text{erf}\left(\frac52\right)\right] \\
    =& 5.83267\times10^{-11}
\end{align*} -->

Given $X_i\sim\mathcal{N}(0,i)$ for $i\in\{1,2\}$, we have the PDFs of $X_{1,2}$ such that

$$f_i(x)=\frac{e^{-\frac{x^2}{2i}}}{\sqrt{2\pi i}}\quad i\in\{1,2\}\,.$$

Let $g_i(x)$ be the PDFs of $X_{1,2}$ under another measure such that

$$g_i(x)=\frac{e^{-\frac{(x-\mu_i)^2}{2\sigma_i^2}}}{\sigma_i\sqrt{2\pi}}\,,\quad i\in\{1,2\}\,.$$

We have

$$
    \E_f\left(1_{X_i>5}\right)
    = \E_g\left(\frac{f_i(X_i)}{g_i(X_i)}1_{X_i>5}\right)
    = \frac{\sigma_i}{\sqrt{i}}\E_g\left(e^{-\frac{X_i^2}{2i}+\frac{(X_i-\mu_i)^2}{2\sigma_i^2} }1_{X_i>5}\right)\,,
$$

and

\begin{align*}
    & \Pr(V>5) \\
    =& \E_f(1_{X_1>5})\E_f(1_{X_2>5}) \\
    =& \frac{\sigma_1\sigma_2}{\sqrt{2}}\E_g\left(e^{-\frac{X_1^2}{2}+\frac{(X_1-\mu_1)^2}{2\sigma_1^2}}1_{X_1>5}\right)\E_g\left(e^{-\frac{X_2^2}{4}+\frac{(X_2-\mu_2)^2}{2\sigma_2^2}}1_{X_2>5}\right)\,,
\end{align*}

where the likelihood ratios for $X_1$ and $X_2$ are $e^{-\frac{X_1^2}{2}+\frac{(X_1-\mu_1)^2}{2\sigma_1^2} }$ and $e^{-\frac{X_2^2}{4}+\frac{(X_2-\mu_2)^2}{2\sigma_2^2}}$.

Through tuning, we get the optimal parameter values $\mu_1\approx5.1, \sigma_1\approx0.3, \mu_2\approx5.2, \text{ and }\sigma_2\approx0.6$.

### Script

\inputminted{python}{q4/main.py}

### Result

The estimated result is $5.84583\times10^{-11}$.
