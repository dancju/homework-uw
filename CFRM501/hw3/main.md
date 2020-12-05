---
title: CFRM 501, 2020 Autumn, HW 3
...

# Q1

The expected terminal wealth in dollars is $$W_1=1 000\times(0.7\times1.2+0.3\times0.7)=1050.$$

The utility function of the investor is $$U(w)=\left.\frac{w^{1-\gamma}-1}{1-\gamma}\right|_{\gamma=2}=1-w^{-1}.$$

The certainty equivalent of the investment opportunity is

\begin{equation*}\begin{aligned}
W_C
=& U^{-1}(\E(U(W_1))) \\
=& U^{-1}(0.7U(1200)+0.3U(700)) \\
=& 16800/17 \\
\approx& 988.235,
\end{aligned}\end{equation*}

which is less than the initial value, indicating the the invester should NOT take the opportunity.

Meanwhile, if the initial wealth was $1,000,000, The certainty equivalent of the investment opportunity is

\begin{equation*}\begin{aligned}
W_C
=& U^{-1}(\E(U(W_1))) \\
=& U^{-1}(0.7U(1200000)+0.3U(700000)) \\
=& 16800000/17 \\
\approx& 988235.29,
\end{aligned}\end{equation*}

which is also less than the corresponding initial wealth, indicating the invester should NOT take the opportunity as well.

# Q2

The certainty equivalent, by definition, is

$$W_C=U^{-1}(\E(U(W_1))).$$

Plugging in the exponential utility $U(x)=-e^{-\gamma x},\gamma>0$ yields

\begin{equation*}\begin{aligned}
W_C
=& U^{-1}\left(\E\left(-e^{-\gamma(W_0+H)}\right)\right) \\
=& U^{-1}\left(-e^{-\gamma W_0}\E\left(e^{-\gamma H}\right)\right)
\end{aligned}\end{equation*}

Plugging in the inverse of $U(\cdot)$, i.e.\ $U^{-1}(x)=-\frac{\ln(-x)}{\gamma}$, yields

\begin{equation*}\begin{aligned}
W_C
=& -\frac{\ln\left(e^{-\gamma W_0}\E\left(e^{-\gamma H}\right)\right)}{\gamma} \\
=& W_0 -\frac{\ln\E\left(e^{-\gamma H}\right)}{\gamma}.
\end{aligned}\end{equation*}

Therefore, $W_C-W_0=-\frac{1}{\gamma}\ln\E\left(e^{-\gamma H}\right)$ does not depend on $W_0$.

# Q3

According to their definitions, we have \begin{equation}\forall W\in\mathbb{R}:W_C^{(1)}=U_1^{-1}(\E(U_1(W))),\end{equation} and \begin{equation}\forall W\in\mathbb{R}:W_C^{(2)}=U_2^{-1}(\E(U_2(W))).\end{equation}

Given $U_1\sim U_2$, we have \begin{equation}\exists a,b\in\mathbb{R},\forall W\in\mathbb{R}:U_2(W)=aU_1(W)+b,\end{equation}

which implies \begin{equation}\forall W\in\mathbb{R}:U_2^{-1}(aU_1(W)+b)=W.\end{equation}

Plugging (3) into (2) yields

\begin{equation*}\begin{aligned}
W_C^{(2)}
=& U_2^{-1}(\E(aU_1(W)+b)) \\
=& U_2^{-1}(a\E(U_1(W))+b) \\
=& U_2^{-1}(a U_1(U_1^{-1}( \E(U_1(W))))+b).
\end{aligned}\end{equation*}

Plugging (4) yields

\begin{equation*}\begin{aligned}
W_C^{(2)}
=& U_1^{-1}( \E(U_1(W))).
\end{aligned}\end{equation*}

Plugging (1) yields

$$W_C^{(2)}= W_C^{(1)}.$$
