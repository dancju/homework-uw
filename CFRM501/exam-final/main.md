---
title: CFRM 501, 2020 Autumn, Final
...

I did not give or receive any unauthorized help during this test.

# 1

Buy 1 bond A and sell $a$ bound B, which replicates a zero-coupon bond. We have the net-coupon of the portfolio is zero

$$c_Ae^{-Ty_0(T_i)}-\alpha c_Be^{-Ty_0(T_i)}=0\,,$$

and

$$p_0^{(A)}-\alpha p_0^{(B)}=(F-\alpha F)e^{-Ty_0(T)}\,,$$

which yields

$$y_0(T)=-\frac1T\ln\frac{c_Bp_0^{(A)}-c_A p_0^{(B)}}{(c_B-c_A)F}\,.$$

# 2

Buying 3 shares of $r_1$, selling 4 shares of $r_2$, and buying 1 shares of $r_3$, the profit is

$$-3r_1+4r_2-1r_3=2\,.$$

# 3

## 3.a

$$F(x)=\int f(x)\diff x=1-e^{-\lambda x}$$

$$\textsf{VaR}_\alpha(L)=F^{-1}(\alpha)=-\frac{\ln(1-\alpha)}\lambda$$

## 3.b

**i**

$$r_p\sim\mathcal N(\bm w\tran\bm\mu,\bm w\tran\bm{\Sigma w})$$

**ii**

$$\textsf{VaR}_\alpha(-r_p)=-\bm w\tran\bm\mu+\sqrt{\bm w\tran\bm{\Sigma w}}\Phi^{-1}(\alpha)$$

**iii**

$$\textsf{VaR}_\alpha^{\textsf{mean}}(-r_p)=\sqrt{\bm w\tran\bm{\Sigma w}}\Phi^{-1}(\alpha)$$

The minimization of $\textsf{VaR}_\alpha^{\textsf{mean}}(-r_p)$ is equivalent to the Lagrangian function

$$\mathcal L(\bm w, L)=\bm w\tran\bm{\Sigma w}\Phi^{-1}(\alpha)+(\bm w\tran\bm 1-1)L\,.$$

Solving its first-order conditions $\nabla_{\bm w}\mathcal L=\bm0$ and $\nabla_{L}\mathcal L=\bm0$ for $\bm w$ yields

$$\bm w^*=\frac{\bm\Sigma^{-1}\bm1}{\bm1\tran\bm\Sigma^{-1}\bm1}\,.$$

# 4

## 4.a

The bootstrapping itself only yields discontinuous functions and relies on interpolation to get smooth results.

## 4.b

Multivariate normal distribution

## 4.c

Systematic factor risk
