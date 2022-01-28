---
title: CFRM 504, 2020 Autumn, HW 3
...

# 3.1

**In the case of $0<d<u<1+r<\infty$,** short $B_0$ shares of stock and long $S_0$ bonds at time zero. We have

$$X_0=S_0B_0-B_0S_0=0,$$

and

$$
X_1=\begin{cases}
  -S_0B_0u+B_0S_0(1+r)>0, & \omega=H,\\
  -S_0B_0d+B_0S_0(1+r)>0, & \omega=T.\\
\end{cases}
$$

**In the case of $0<1+r<d<u<\infty$,** long $B_0$ shares of stock and short $S_0$ bonds at time zero. We have

$$X_0=-S_0B_0+B_0S_0=0,$$

and

$$
X_1=\begin{cases}
  S_0B_0u-B_0S_0(1+r)>0, & \omega=H,\\
  S_0B_0d-B_0S_0(1+r)>0, & \omega=T.\\
\end{cases}
$$

# 3.2

## 3.2.a

The constructed portfolio contains $\Delta_0$ shares of stock and $\frac{X_0-\Delta_0S_0}{B_0}$ bonds. The value of the portfolio at time $T$ is

$$
X_T=\phi(S_T)=
\begin{cases}
\phi(uS_0)=\Delta_0S_0(u+a)+(X_0-\Delta_0S_0)(1+r), & \omega=H, \\
\phi(dS_0)=\Delta_0S_0(d+a)+(X_0-\Delta_0S_0)(1+r), & \omega=T.
\end{cases}
$$

Solving for $X_0$ and $\Delta_0$ yields

$$
\Delta_0=\frac{\phi(uS_0)-\phi(dS_0)}{(u-d)S_0},
$$

and

\begin{equation}
X_0=\frac{1}{1+r}\left(\frac{(1+r)-(d+a)}{u-d}\phi(uS_0)+\frac{u+a-(1+r)}{u-d}\phi(dS_0)\right).
\end{equation}

## 3.2.b

Given the measure $\widetilde{\mathrm P}$ such that $\widetilde{\E}(X_T/B_T)=X_0/B_0$, we have

$$\frac{\widetilde p\phi(uS_0)}{B_T}+\frac{\widetilde q\phi(dS_0)}{B_T}=\frac{X_0}{B_0},$$

\begin{equation}
X_0=\frac{\widetilde p\phi(uS_0)+\widetilde q\phi(dS_0)}{1+r}.
\end{equation}

Merging Eq.\ (1) and Eq.\ (2) yields

$$\widetilde p=\frac{(1+r)-(d+a)}{u-d},\quad\widetilde q=\frac{u+a-(1+r)}{u-d}.$$

## 3.2.c

$$B_0\widetilde{\E}\left(\frac{\phi(S_T)}{B_T}\right)=\frac{\widetilde p\phi(uS_0)+\widetilde q\phi(dS_0)}{1+r}=X_0.$$

## 3.2.d

\begin{align*}
\widetilde{\E}\left(\frac{S_T}{B_T}\right) &
=\frac{\widetilde puS_0+\widetilde qdS_0}{B_T} \\&
=\frac{S_0}{B_T}\left(\frac{(1+r)-(d+a)}{u-d}u+\frac{u+a-(1+r)}{u-d}d\right) \\&
=\left(1-\frac a{1+r}\right)\frac{S_0}{B_0} \\&
\ne\frac{S_0}{B_0}.
\end{align*}

# 3.3

## 3.3.a

Given the measure $\widetilde{\mathrm P}$ such that $\widetilde{\E}(S_T/B_T)=S_0/B_0$, we have

$$\frac{\widetilde puS_0}{B_T}+\frac{\widetilde qdS_0}{B_T}=\frac{S_0}{B_0},$$

$$\widetilde pu+\widetilde qd=1+r.$$

Using this equation and the fact that $\widetilde p+\widetilde q=1$, we have

$$\widetilde p=\frac{(1+r)-d}{u-d},\quad\widetilde q=\frac{u-(1+r)}{u-d}.$$

Therefore,

\begin{align*}
V_0 &
=B_0\widetilde{\E}(V_T/B_T) \\&
=\frac{B_0}{B_T}(\widetilde p\phi(uS_0)+\widetilde q\phi(dS_0)) \\&
=\frac{1}{1+r}\left(\frac{(1+r)-d}{u-d}\phi(uS_0)+\frac{u-(1+r)}{u-d}\phi(dS_0)\right).
\end{align*}

## 3.3.b

Given the measure $\widehat{\mathrm P}$ such that $\widehat{\E}(B_T/S_T)=B_0/S_0$, we have

$$\frac{\widehat pB_T}{uS_0}+\frac{\widehat qB_T}{dS_0}=\frac{B_0}{S_0},$$

$$\frac{\widehat p}{u}+\frac{\widehat q}{d}=\frac{1}{1+r}.$$

Using this equation and the fact that $\widetilde p+\widetilde q=1$, we have

$$\widehat p=\frac{ud}{u-d}\left(\frac{1}{d}-\frac{1}{1+r}\right),\quad\widehat q=\frac{ud}{u-d}\left(\frac{1}{1+r}-\frac{1}{u}\right).$$

Therefore,

\begin{align*}
V_0 &
=S_0\widehat{\E}(V_T/S_T) \\&
=S_0\left(\widehat p\frac{\phi(uS_0)}{uS_0}+\widehat q\frac{\phi(dS_0)}{dS_0}\right) \\&
=\frac{\widehat p\phi(uS_0)}{u}+\frac{\widehat q\phi(dS_0)}{d} \\&
=\frac{\phi(uS_0)}{u}\frac{ud}{u-d}\left(\frac{1}{d}-\frac{1}{1+r}\right)+\frac{\phi(dS_0)}{d}\frac{ud}{u-d}\left(\frac{1}{1+r}-\frac{1}{u}\right) \\&
=\frac{1}{1+r}\left(\frac{(1+r)-d}{u-d}\phi(uS_0)+\frac{u-(1+r)}{u-d}\phi(dS_0)\right).
\end{align*}
