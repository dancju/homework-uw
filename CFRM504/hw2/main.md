---
title: CFRM 504, 2020 Autumn, HW 2
...

# 2.1

## a

- At time zero, lend $S_0$ from bank and buy asset S.
- At time $t_i$, receive dividend $D_i$ and save to bank for interests.
- At time $T$,
  - sell asset S for $F_0^T$,
  - pay off the debt with $e^{rT}S_0$, and
  - withdraw the deposit $\sum_{i}e^{r(T-t_i)}D_i$.

Since there is no arbitrage in the market, we have

$$F_0^T-e^{rT}S_0+\sum_{i}e^{r(T-t_i)}D_i=0,$$

$$F_0^T=e^{rT}S_0-\sum_ie^{r(T-t_i)}D_i.$$

Similarily, we have

$$F_t^T=e^{r(T-t)}S_t-\sum_{i:t_i>t}e^{r(T-t_i)}D_i.$$

## b

\begin{align*}
f_t^T &
=e^{-r(T-t)}\left(F_t^T-F_0^T\right) \\&
=S_t-e^{rt}S_0+\sum_{i:t_i<t}e^{r(t-t_i)}D_i.
\end{align*}

# 2.2

## a

The present value of cash flows $\text{CF}_1$ and $\text{CF}_2$ are

\begin{equation}V_1=e^{-rt_1}\text{CF}_1,\end{equation}

and

\begin{equation}V_2=e^{-rt_2}\text{CF}_2.\end{equation}

The trade is fair iff

\begin{equation}V_0+V_1-V_2=0.\end{equation}

Merging the three equations above yields

$$\text{CF}_2=e^{rt_2}V_0+e^{r(t_2-t_1)}\text{CF}_1.$$

## b

Merging (1), (2), and (3) yields

\begin{equation}V_0=-e^{-rt_1}\text{CF}_1+e^{-rt_2}\text{CF}_2.\end{equation}

$V_0>0$ is equivalent to

$$-e^{-rt_1}\text{CF}_1+e^{-rt_2}\text{CF}_2>0.$$

Since $\text{CF}_1$ and $\text{CF}_2$ are positive, we have

$$R<e^{r(t_1-t_2)}.$$

## c

$$R=\frac{\text{CF}_1}{\text{CF}_2}<0.$$

# 2.3

$$P_T=C_T(T,K_1)-C_T(T,K_2)$$

$$S_T-K_1B_T^T\le C_T(T,K_1)\le S_T$$

$$S_T-K_2B_T^T\le C_T(T,K_2)\le S_T$$

Merging the equation and inequalities above yields

$$-K_1B_T^T\le P_T\le K_2B_T^T.$$

Since a European contract is always positive, we have

$$0\le P_T\le K_2B_T^T,$$

$$0\le P_t\le K_2B_t^T.$$

The lower bound is $0$ and the upper bound is $K_2B_t^T$.

# 2.4

At time $t$, long one unit of asset $A$ and short one unit of asset $B$. At time $T$, short one unit of asset $A$ and long one unit of asset $B$. Let $X_t=0$. The overall profit of this strategy is

\begin{align*}
X_T &
= (X_t^B-X_t^A)e^{(T-t)r}+X_T^A-X_T^B \\&
> 0.
\end{align*}
