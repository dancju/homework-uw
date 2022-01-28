---
title: CFRM 504, 2020 Autumn, HW 1
...

## 1.1

Late submissions will receive an grade of zero automatically.

## 1.2

$$
\E(X) = 0\,\Pr(X=0)+1\,\Pr(X=1) = 1/2
$$

$$
\E\left(e^X\right) = e^0\,\Pr(X=0)+e^1\,\Pr(X=1) = \frac{1+e}{2}
$$

$$
\widetilde{\E}(X) = 0\,\widetilde{\Pr}(X=0)+1\,\widetilde{\Pr}(X=1) = 3/7
$$

$$
\widetilde{\E}\left(e^X\right) = e^0\,\widetilde{\Pr}(X=0)+e^1\,\widetilde{\Pr}(X=1) = \frac{4+3\,e}{7}
$$

## 1.3

$$
f_\omega(\text{HH})=p^2,\quad f_\omega(\text{HT})=f_\omega(\text{TH})=pq,\quad f_\omega(\text{TT})=q^2.
$$

\begin{equation*}\begin{aligned}
f_{S_1,S_2}(uS_0,u^2S_0)=p^2,\quad
f_{S_1,S_2}(uS_0,duS_0)=pq,\\
f_{S_1,S_2}(dS_0,duS_0)=pq,\quad
f_{S_1,S_2}(dS_0,d^2S_0)=q^2.
\end{aligned}\end{equation*}


\begin{equation*}\begin{aligned}
f_{S_1|S_2}(uS_0,u^2S_0)=1,\quad
f_{S_1|S_2}(uS_0,duS_0)=1/2,\\
f_{S_1|S_2}(dS_0,duS_0)=1/2,\quad
f_{S_1|S_2}(dS_0,d^2S_0)=1.
\end{aligned}\end{equation*}

\begin{equation*}\begin{aligned}
\E(S_2/S_1)
=& uf_{S_1,S_2}(uS_0,u^2S_0)+df_{S_1,S_2}(uS_0,duS_0) \\
& +uf_{S_1,S_2}(dS_0,duS_0)+df_{S_1,S_2}(dS_0,d^2S_0) \\
=& up^2 + dpq + upq + dq^2 \\
=& (p+q)(up+dq).
\end{aligned}\end{equation*}

$$
\E\left(\frac{S_2}{S_1}\middle|S_1=uS_0\right) = uf_{\left.\frac{S_2}{S_1}\right|S_1}(u,uS_0) + df_{\left.\frac{S_2}{S_1}\right|S_1}(d,uS_0) = up+dq,
$$

$$
\E\left(\frac{S_2}{S_1}\middle|S_1=dS_0\right) = uf_{\left.\frac{S_2}{S_1}\right|S_1}(u,dS_0) + df_{\left.\frac{S_2}{S_1}\right|S_1}(d,dS_0) = up+dq.
$$

## 1.6

**Proof of (1.4.2) in the discrete case**

\begin{equation*}\begin{aligned}
\text{RHS}
=& \E\left(\sum_xf_{X|Y}(x,Y)g(x,Y)\right) \\
=& \sum_yf_Y(y)\left(\sum_xf_{X|Y}(x,y)g(x,y)\right) \\
=& \sum_y\sum_xf_Y(y)f_{X|Y}(x,y)g(x,y) \\
=& \sum_y\sum_xf_{X,Y}(x,y)g(x,y)
= \text{LHS}.
\end{aligned}\end{equation*}

**Proof of (1.4.2) in the continuous case**

\begin{equation*}\begin{aligned}
\text{RHS}
=& \E\left(\int_x f_{X|Y}(x,Y)g(x,Y)\diff x\right) \\
=& \int_yf_Y(y)\left(\int_x f_{X|Y}(x,y)g(x,y)\diff x\right)\diff y \\
=& \int_y\int_xf_Y(y)f_{X|Y}(x,y)g(x,y)\diff x\diff y \\
=& \int_y\int_xf_{X,Y}(x,y)g(x,y)\diff x\diff y
= \text{LHS}.
\end{aligned}\end{equation*}

**Proof of (1.4.3) in the discrete case**

$$
\text{LHS} = \sum_xf_{X|Y}(x,Y)g(x)h(Y) = h(Y)\sum_xf_{X|Y}(x,Y)g(x) = \text{RHS}.
$$

**Proof of (1.4.3) in the continuous case**

$$
\text{LHS} = \int_xf_{X|Y}(x,Y)g(x)h(Y)\diff x = h(Y)\int_xf_{X|Y}(x,Y)g(x)\diff x = \text{RHS}.
$$

**Proof of (1.4.4) in the discrete case**

$$
\text{LHS} = \sum_xf_{X|Y}(x,Y)g(x) = \sum_xf_{X}(x)g(x) = \text{RHS}.
$$

**Proof of (1.4.4) in the continuous case**

$$
\text{LHS} = \int_xf_{X|Y}(x,Y)g(x)\diff x = \int_xf_{X}(x)g(x)\diff x = \text{RHS}.
$$

## 1.7

$$
\E(1/X)=\int_a^b\frac{1}{b-a}\frac{1}{x}\diff x=\frac{1}{b-a}\ln(x)|_a^b=\frac{\ln(b)-\ln(a)}{b-a}.
$$

$$
\E(1/Y)=\frac{\ln(d)-\ln(c)}{d-c}.
$$

\begin{equation*}\begin{aligned}
\E(X/Y)
=& \int_a^b\int_c^d\frac{1}{b-a}\frac{1}{d-c}\frac{x}{y}\diff x\diff y \\
=& \frac{1}{b-a}\frac{1}{d-c}\left(\int_a^bx\diff x\right)\left(\int_c^d\frac{1}{y}\diff y\right) \\
=& \frac{1}{b-a}\frac{1}{d-c}\frac{b^2-a^2}{2}(\ln(d)-\ln(c)) \\
=& \frac{(b+a)(\ln(d)-\ln(c))}{2(d-c)}
\end{aligned}\end{equation*}
