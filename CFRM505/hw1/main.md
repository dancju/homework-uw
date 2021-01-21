---
title: CFRM 505, 2021 Winter, HW 1
...

# 1

The integral of the PDF on its domain is one such that $\iint_{\mathbb R^2}f(x,y)\diff x\diff y=1$, or $c=1$.

## 1.a

$$\Pr(X+Y>1.5)=\int_{0.5}^1\left(\int_{1.5-x}^1\left(4x^2y+y^2\right)\diff y\right)\diff x=\frac{121}{320}\,.$$

## 1.b

$$\E(Y)=\iint_{[0,1]^2}\left(4x^2y+y^2\right)y\diff x\diff y=\frac{25}{36}\,.$$

## 1.c

$$\E(X)=\iint_{[0,1]^2}\left(4x^2y+y^2\right)x\diff x\diff y=\frac23\,.$$

$$\E(XY)=\iint_{[0,1]^2}\left(4x^2y+y^2\right)xy\diff x\diff y=\frac{11}{24}\,.$$

$$\Cov(X,Y)=\E(XY)-\E(X)\E(Y)=-\frac1{216}\,.$$

## 1.d

$$
    f_Y(y)=\int_\mathbb Rf_{X,Y}(x,y)\diff x=
    \begin{cases}
        y^2+\frac{4y}3\,, & y\in[0,1]\,, \\
        0\,, & \text{otherwise}.
    \end{cases}
$$

$$
    f_{X|Y}(x,y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}=
    \begin{cases}
        \frac{(4x^2+y)3}{3y+4}\,, & (x,y)\in[0,1]^2\,, \\
        0\,, & \text{otherwise}.
    \end{cases}
$$

## 1.e

$$\E\left(X\middle|Y=\frac13\right)=\int_0^1f_{X|Y}\left(x,\frac13\right)x\diff x=\frac7{10}\,.$$

## 1.f

$$\Pr\left(X-Y<0.1\middle|Y=0.5\right)=\int_0^{0.6}f_{X|Y}\left(x,0.5\right)\diff x=\frac{441}{1375}\,.$$

## 1.g

$$\Pr\left(X<0.5\middle|Y>0.5\right)=\frac{\int_0^{0.5}\left(\int_{0.5}^1\left(4x^2y+y^2\right)\diff y\right)\diff x}{\int_0^1\left(\int_{0.5}^1\left(4x^2y+y^2\right)\diff y\right)\diff x}=\frac5{19}\,.$$

# 2

### Script

\inputminted{python}{q2/simulate.py}

### Result

<!-- The analytic result is 1/4 -->

The simulation result is $0.252053$.

# 3

### Script

\inputminted{python}{q3/simulate.py}

### Result

<!-- The analytic result is -1/12 and 1/12 -->

The simulation result is $\Cov(U,1-U)=-0.0845503$ and $\Var(1-U)=0.0845503$.

# 4

In the case of $U_1<U_2$, the length of the three pieces are $U_1, U_2-U_1, 1-U_2$. According to the triangle inequality theorem, the three pieces make a triangle iff

$$\begin{cases}
U_1+(U_2-U_1)>1-U_2\,, \\
U_1+(1-U_2)>U_2-U_1\,, \\
(U_2-U_1)+(1-U_2)>U_1\,,
\end{cases}$$

or

$$\begin{cases}
U_2>1/2\,, \\
U_1-U_2>-1/2\,, \\
U_1<1/2\,.
\end{cases}$$

Similarily, in the case of $U_1>U_2$, the three pieces make a triangle iff

$$\begin{cases}
U_1>1/2\,, \\
U_2-U_1>-1/2\,, \\
U_2<1/2\,.
\end{cases}$$

Combining the two cases above, we get that the three pieces make a triangle iff

$$[(U_1<1/2)\oplus(U_2<1/2)]\land(U_1-U_2>-1/2)\land(U_2-U_1>-1/2)$$

whose phase diagram is shown blow.

\includegraphics{q4/main.pdf}

### Script

\inputminted{python}{q4/simulate.py}

### Result

The simulation result is $0.250228$.
