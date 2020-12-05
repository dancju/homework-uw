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

$$\left(\widetilde p(uS_0-100)^++(1-\widetilde p)(dS_0-100)^+\right)\left(\widetilde q\frac{1}{RB_0}+(1-\widetilde q)\frac{1}{rB_0}\right)=\frac{V_0}{B_0},$$

or

$$V_0=\widetilde p(uS_0-100)\left(\frac{\widetilde q}{R}+\frac{1-\widetilde q}{r}\right)\,.$$

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
    1. buy _one_ stock at price $S_0$,
    1. sell the call option at price $V_0$ of amount $\Gamma_0$, and
    1. sell bonds at price $B_0$ of amount $\frac{S_0-V_0\Gamma_0}{B_0}$.
1. At time $T$,
    1. sell the stock at price $S_T$,
    1. fulfill the option to its owner at $(S_T-100)^+$, and
    1. pay off the bonds at price $B_T$.

Since a variable $\Gamma_0$ is introduced, a value or range is required to make the arbitrage complete. Given the portfolio, we have

$$X_0=-S_0+V_0\Gamma_0+\frac{S_0-V_0\Gamma_0}{B_0}B_0=0\,,$$

and

\begin{align*}
  X_T &
  =S_T-(S_T-100)^+\Gamma_0-\frac{S_0-V_0\Gamma_0}{B_0}B_T \\&
  =\begin{cases}
    uS_0-(uS_0-100)^+\Gamma_0-(S_0-V_0\Gamma_0)R\,, &
    \text{if }S_T=uS_0\text{ and }B_T=RB_0, \\
    dS_0-(dS_0-100)^+\Gamma_0-(S_0-V_0\Gamma_0)r\,, &
    \text{if }S_T=dS_0\text{ and }B_T=rB_0,
  \end{cases} \\&
  =\begin{cases}
    \left(\frac{11}{10}V_0-20\right)\Gamma_0+10\,, \\
    V_0\Gamma_0-20\,.
  \end{cases} \\&
\end{align*}

According to the definition of arbitrage, we have $\forall V_0>12.5:X_T\ge0$, or

$$\forall V_0>12.5:\quad\begin{cases}
  \left(\frac{11}{10}V_0-20\right)\Gamma_0+10\ge0\,, \\
  V_0\Gamma_0-20\ge0\,.
\end{cases}$$

Solving for $\Gamma_0$ yields

\begin{equation}
\Gamma_0\in\begin{cases}
  \left[\frac{20}{V_0},\frac{100}{200-11V_0}\right] &
  \text{if }V_0\in\left(\frac{25}{2},\frac{200}{11}\right) \\
  \left[\frac{20}{V_0},\infty\right) &
  \text{if }V_0\in\left[\frac{200}{11},+\infty\right)
\end{cases}
\end{equation}

With this range for $\Gamma_0$ holds, we have $X_0=0$ and $X_T\ge0$. To make it a legit arbitrage, we have to assure $\Pr(X_T>0)>0$, or $\Pr(X_T=0)<1$. In this case,

\begin{align*}
\Pr(X_T=0) &
=\Pr\left[\left(\frac{11}{10}V_0-20\right)\Gamma_0+10=0 \text{ and }V_0\Gamma_0-20=0\right] \\&
=\Pr(V_0=12.5\text{ and }\Gamma_0=1.6)\,.
\end{align*}

Given the condition that $V_0>12.5$, the circumstance of $X_T=0$ is already excluded, i.e.\ $\Pr(X_T>0)=1$. Therefore, we can be sure that the portfolio described above with a $\Gamma_0$ in the range (3) is an arbitrage as long as $V_0>12.5$.
