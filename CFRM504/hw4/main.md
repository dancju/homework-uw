---
title: CFRM 504, 2020 Autumn, HW 4
...

# 4.1

## 4.1.a

The condition $\widetilde{\E}\left(\frac{S_T}{B_T}\right)=\frac{S_0}{B_0}$ is equivalent to

$$\widetilde{\E}(S_T)\widetilde{\E}\left(\frac{1}{B_T}\right)=\frac{S_0}{B_0}\,.$$

Expanding the $\widetilde{\E}$ yields

$$(\widetilde puS_0+(1-\widetilde p)dS_0)\left(\widetilde q\frac{1}{RB_0}+(1-\widetilde q)\frac{1}{rB_0}\right)=\frac{S_0}{B_0}\,,$$

or

$$\widetilde p=\frac{1}{u-d}\left(\frac{Rr}{\widetilde q(r-R)+R}-d\right)\,.$$

## 4.1.b

The market $(S,B)$ is incomplete since there is no unique $\widetilde{\mathrm P}$, but instead that $\widetilde p$ depends on $\widetilde q$.

## 4.1.c

According to the the no-arbitrage condition, we have

$$\widetilde{\E}\left(\frac{(S_T-100)^+}{B_T}\right)=\frac{V_0}{B_0}.$$

Since $S_T$ and $B_T$ are independent, we have

$$\widetilde{\E}\left((S_T-100)^+\right)\widetilde{\E}\left(\frac{1}{B_T}\right)=\frac{V_0}{B_0}.$$

Expanding the $\widetilde{\E}$ yields

$$\left(\widetilde p(uS_0-100)^++(1-\widetilde p)(dS_0-100)^+\right)\left(\widetilde q\frac{1}{RB_0}+(1-\widetilde q)\frac{1}{rB_0}\right)=\frac{V_0}{B_0}\,.$$

Plugging the $\widetilde p(\widetilde q)$ from 4.1.a, and the numerical values of $u, d, R, r$ yields

$$V_0=10+\frac{40}{11}\widetilde q\,.$$

Since $\widetilde q\in[0,1]$, we have $V_0\in[10,150/11]$. Therefore, the lower bound is $10$ and the upper bound is $150/11=13.636$.

## 4.1.d

Plugging $h(S_T)=(S_T-100)^+$ into $\widetilde{\E}\left(\frac{h(S_T)}{B_T}\right)=\frac{V_0}{B_0}$ yields

$$\widetilde{\E}\left(\frac{(S_T-100)^+}{B_T}\right)=\frac{V_0}{B_0}\,.$$

Since $S_T$ and $B_T$ are independent, the LHS of the equation above can be factorized such that

$$\widetilde{\E}\left((S_T-100)^+\right)\widetilde{\E}\left(\frac{1}{B_T}\right)=\frac{V_0}{B_0}\,.$$

Expanding the $\widetilde{\E}$ yields

\begin{equation}
\left(\widetilde p(uS_0-100)^++(1-\widetilde p)(dS_0-100)^+\right)\left(\widetilde q\frac{1}{RB_0}+(1-\widetilde q)\frac{1}{rB_0}\right)=\frac{V_0}{B_0}\,.
\end{equation}

Similarily, plugging $g(S_T)=(90-S_T)^+$ into $\widetilde{\E}\left(\frac{g(S_T)}{B_T}\right)=\frac{X_0}{B_0}$, factorizing, and expanding yields

\begin{equation}
\left(\widetilde p(90-uS_0)^++(1-\widetilde p)(90-dS_0)^+\right)\left(\widetilde q\frac{1}{RB_0}+(1-\widetilde q)\frac{1}{rB_0}\right)=\frac{X_0}{B_0}\,.
\end{equation}

Combining Eq.\ (1), Eq.\ (2), $\widetilde p(\widetilde q)$ from 4.1.a, and the numerical values of $u, d, R, r, V_0$ yields

$$\widetilde q=11/20=0.55\,,\quad X_0=7/2=3.5\,.$$

## 4.1.e

The portfolio at time zero is given by

$$X_0=\Delta_0S_0+\Gamma_0V_0+\frac{X_0-\Delta_0S_0-\Gamma_0V_0}{B_0}B_0,$$

and at time $T$ is given by

\begin{align*}
  X_T &
  =\Delta_0S_T+\Gamma_0(S_T-100)^++\frac{X_0-\Delta_0S_0-\Gamma_0V_0}{B_0}B_T \\&
  =\begin{cases}
    \Delta_0uS_0+\Gamma_0(uS_0-100)^++(X_0-\Delta_0S_0-\Gamma_0V_0)R \\
    \Delta_0uS_0+\Gamma_0(uS_0-100)^++(X_0-\Delta_0S_0-\Gamma_0V_0)r \\
    \Delta_0dS_0+\Gamma_0(dS_0-100)^++(X_0-\Delta_0S_0-\Gamma_0V_0)R \\
    \Delta_0dS_0+\Gamma_0(dS_0-100)^++(X_0-\Delta_0S_0-\Gamma_0V_0)r \\
  \end{cases} \\&
  =\begin{cases}
     10\Delta_0  +6.8\Gamma_0 +1.1X_0 ,& \text{if }S_T=uS_0\text{ and }B_T=RB_0\,, \\
     20\Delta_0    +8\Gamma_0    +X_0 ,& \text{if }S_T=uS_0\text{ and }B_T=rB_0\,, \\
    -30\Delta_0 -13.2\Gamma_0 +1.1X_0 ,& \text{if }S_T=dS_0\text{ and }B_T=RB_0\,, \\
    -20\Delta_0   -12\Gamma_0    +X_0 ,& \text{if }S_T=dS_0\text{ and }B_T=rB_0\,. \\
  \end{cases} \\&
\end{align*}

Meanwhile, the payoff of the put option is

\begin{align*}
  g(S_T)
  =(90-S_T)^+
  =\begin{cases}
      0 & \text{if }S_T=uS_0\,, \\
     10 & \text{if }S_T=dS_0\,.
  \end{cases}
\end{align*}

According to the replication $X_T=g(S_T)$, we have

$$
\begin{cases}
 0 &=  10\Delta_0  +6.8\Gamma_0 +1.1X_0\,, \\
 0 &=  20\Delta_0    +8\Gamma_0    +X_0\,, \\
10 &= -30\Delta_0 -13.2\Gamma_0 +1.1X_0\,, \\
10 &= -20\Delta_0   -12\Gamma_0    +X_0\,, \\
\end{cases}
$$

which yields

$$\Delta_0=0.125\,,\quad\Gamma_0=-0.75\,,\quad X_0=3.5\,.$$

# 4.2

## 4.2.a

The condition $\widetilde{\E}\left(\frac{S_T}{B_T}\right)=\frac{S_0}{B_0}$ is equivalent to

$$\frac{uS_0}{RB_0}\widetilde p+\frac{dS_0}{rB_0}\widetilde q=\frac{S_0}{B_0},$$

or

$$\frac{\widetilde pu}{R}+\frac{\widetilde qd}{r}=1.$$

Combining with $\widetilde p+\widetilde q=1$, we have

$$\widetilde p=\frac{Rr-dR}{ur-dR}\,,\quad\widetilde q=\frac{ur-Rr}{ur-dR}\,.$$

## 4.2.b

The market $(S,B)$ is complete since $\widetilde{\mathrm P}$ is unique.

## 4.2.c

According to the the no-arbitrage condition, we have

$$\widetilde{\E}\left(\frac{(S_T-100)^+}{B_T}\right)=\frac{V_0}{B_0}\,.$$

Expanding the $\widetilde{\E}$ yields

$$\frac{(uS_0-100)^+}{RB_0}\widetilde p+\frac{(dS_0-100)^+}{rB_0}\widetilde q=\frac{V_0}{B_0}\,.$$

Plugging the $\widetilde p$ from 4.2.a and the numerical values of $u, d, R, r, S_0$ yields

$$V_0=25/2=12.5\,.$$

Therefore, the lower bound and the upper bound are both $12.5$. They are the same because the market is complete.

## 4.2.d

An **arbitrage** is a portfolio $X$ satisfying the following conditions:

1. $X_0=0$ (starts from zero value);
1. $\Pr(X_t\ge0)=1$ (does not lose money); and
1. $\Pr(X_t>0)>0$ (might earn something).

In this case, if $V_0>12.5$, an arbitrage is constructed as follows.

1. At time zero,
    1. Underwrite _one_ call option at price $V_0$,
    1. buy stock at price $S_0$ of amount $\Delta_0$, and
    1. buy bonds at price $B_0$ of amount $\frac{V_0-\Delta_0S_0}{B_0}$.
1. At time $T$,
    1. fulfill the option to its owner at $(S_T-100)^+$,
    1. sell the stock at price $S_T$, and
    1. sell the bonds at price $B_T$.

Since a variable $\Delta_0$ is introduced, a value or range is required to complete the arbitrage. Given the portfolio, we have

$$X_0=-V_0+\Delta_0S_0+\frac{V_0-\Delta_0S_0}{B_0}B_0=0\,,$$

and

\begin{align*}
  X_T &
  =-(S_T-100)^++\Delta_0S_T+\frac{V_0-\Delta_0S_0}{B_0}B_T \\&
  =\begin{cases}
    -(uS_0-100)^++\Delta_0uS_0+(V_0-\Delta_0S_0)R\,, \\
    -(dS_0-100)^++\Delta_0dS_0+(V_0-\Delta_0S_0)r\,,
  \end{cases} \\&
  =\begin{cases}
    \frac{11}{10}V_0+10\Delta_0-20\,, &
    \text{if }S_T=uS_0\text{ and }B_T=RB_0, \\
    V_0-20\Delta_0\,, &
    \text{if }S_T=dS_0\text{ and }B_T=rB_0.
  \end{cases} \\&
\end{align*}

According to the definition of arbitrage, we have $V_0>12.5\implies X_T\ge0$, or

$$V_0>12.5\implies\begin{cases}
  \frac{11}{10}V_0+10\Delta_0-20\ge0\,, \\
  V_0-20\Delta_0\ge0\,.
\end{cases}$$

$$\Delta_0=0.625\,.$$

With this value for $\Delta_0$, we asure not losing money, or $\Pr(X_t\ge0)=1$. To make it a legit arbitrage, we also need assure we might earn something, or $\Pr(X_T>0)>0$. In our case, given $V_0>12.5$ and

\begin{align*}
  X_T &
  =\begin{cases}
    \frac{11}{10}V_0+10\Delta_0-20\,,\\
    V_0-20\Delta_0\,,
  \end{cases} \\&
  =\begin{cases}
    \frac{11}{10}V_0-13.75\,, &
    \text{if }S_T=uS_0\text{ and }B_T=RB_0, \\
    V_0-12.5\,, &
    \text{if }S_T=dS_0\text{ and }B_T=rB_0,
  \end{cases} \\&
\end{align*}

we get $X_T>0$, i.e., we always earn something.  Therefore, we can conclude that the portfolio described above with $\Delta_0=0.625$ is an arbitrage as long as $V_0>12.5$.
