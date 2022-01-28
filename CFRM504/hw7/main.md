---
title: CFRM 504, 2020 Autumn, HW 7
...

# 7.1

## 7.1.a

\includegraphics[width=\textwidth]{q1/call.pdf}

## 7.1.b

$$\Delta^\textsf{BS}_t=\frac{\partial C_t^\textsf{BS}}{\partial S_t}=\Phi(d_+)\,.$$

\includegraphics[width=\textwidth]{q1/delta.pdf}

## 7.1.c

$$\Gamma^\textsf{BS}_t=\frac{\partial \Delta_t^\textsf{BS}}{\partial S_t}=\frac{\partial\Phi(d_+)}{\partial S_t}=\frac{\varphi(d_+)}{\sigma\sqrt{T-t}S_t}\,.$$

\includegraphics[width=\textwidth]{q1/gamma.pdf}

## 7.1.d

According to the definition of $\mathcal V$, we have

$$\mathcal V^\textsf{BS}_t=\frac{\partial C_t^\textsf{BS}}{\partial\sigma}=\frac{\partial d_+}{\partial\sigma}\varphi(d_+)S_t-\frac{\partial d_-}{\partial\sigma}\varphi(d_-)K\,.$$

Expnding the two $\varphi$-s yields

$$\mathcal V^\textsf{BS}_t=\frac{\partial d_+}{\partial\sigma}\frac{e^{-\frac{d_+^2}{2}}}{\sqrt{2\pi}}S_t-\frac{\partial d_-}{\partial\sigma}\frac{e^{-\frac{d_-^2}{2}}}{\sqrt{2\pi}}K\,.$$

Plugging in

$$
e^{-\frac{d_+^2}2}
=e^{-\frac{(d_-+\sigma\sqrt{T-t})^2}2}
=e^{-\frac{d_-^2}2}e^{-d_-\sigma\sqrt{T-t}-\frac{\sigma^2(T-t)}2}
=e^{-\frac{d_-^2}2}e^{-\ln\frac{S_t}K}
=\frac K{S_t}e^{-\frac{d_-^2}2}
$$

yields

$$\mathcal V^\textsf{BS}_t=\left(\frac{\partial d_+}{\partial\sigma}-\frac{\partial d_-}{\partial\sigma}\right)\frac{e^{-\frac{d_+^2}{2}}}{\sqrt{2\pi}}S_t\,.$$

Plugging in

$$\frac{\partial d_\pm}{\partial\sigma}=-\frac{1}{\sigma^2\sqrt{T-t}}\ln\frac{S_t}K\pm\frac{\sqrt{T-t}}{2}\,.$$

yields

$$\mathcal V^\textsf{BS}_t=\sqrt{T-t}\frac{e^{-\frac{d_+^2}{2}}}{\sqrt{2\pi}}S_t\,,$$

or

$$\mathcal V^\textsf{BS}_t=(T-t)\sigma S_t^2\Gamma^\textsf{BS}_t\,.$$

\includegraphics[width=\textwidth]{q1/vega.pdf}

# 7.2

## 7.2.a

According to the definition of $\Delta$, we have

$$\Delta_t=\frac{\partial C_t}{\partial S_t}\,.$$

According to the properties of the implied volatility, we have

$$\Delta_t=\frac{\partial C_t}{\partial S_t}=\frac{\partial C_t^\textsf{BS}}{\partial S_t}+\frac{\partial C_t^\textsf{BS}}{\partial\sigma}\frac{\partial\sigma}{\partial S_t}\,.$$

Plugging in $\Delta^\textsf{BS}_t=\frac{\partial C_t^\textsf{BS}}{\partial S_t}$, $\mathcal V^\textsf{BS}_t=\frac{\partial C_t^\textsf{BS}}{\partial\sigma}$, and

$$\frac{\partial\sigma}{\partial S_t}=-\frac1{S_t}\frac{\partial I}{\partial x}\left(T-t,\ln\frac K{S_t}\right)\,,$$

yields

$$\Delta_t=\Delta^\textsf{BS}_t-\frac{\mathcal V^\textsf{BS}_t}{S_t}\frac{\partial I}{\partial x}\left(T-t,\ln\frac K{S_t}\right)\,.$$

## 7.2.b

According to the definition of $\Theta$, we have

$$\Theta_t=\frac{\partial C_t}{\partial t}\,.$$

According to the properties of the implied volatility, we have

$$\Theta_t=\frac{\partial C_t}{\partial t}=\frac{\partial C_t^\textsf{BS}}{\partial t}+\frac{\partial C_t^\textsf{BS}}{\partial\sigma}\frac{\partial\sigma}{\partial t}\,.$$

Plugging in $\Theta^\textsf{BS}=\frac{\partial C_t^\textsf{BS}}{\partial t}$, $\mathcal V^\textsf{BS}_t=\frac{\partial C_t^\textsf{BS}}{\partial\sigma}$, and

$$\frac{\partial\sigma}{\partial t}=-\frac{\partial I}{\partial\tau}\left(T-t,\ln\frac K{S_t}\right)\,,$$

yields

$$\Theta_t=\Theta_t^\textsf{BS}-\mathcal V^\textsf{BS}_t\frac{\partial I}{\partial\tau}\left(T-t,\ln\frac K{S_t}\right)\,.$$

# 7.3

## 7.3.a

Given the portfolio $X_t=\alpha S_t+\beta C_t^\textsf{BS}+\gamma P_t^\textsf{BS}+\delta B_t$, we have

$$\Gamma_t=\frac{\partial^2X_t}{\partial S_t^2}=(\beta+\gamma)\Gamma_t^\textsf{BS}\,,$$

and

$$\mathcal V_t=\frac{\partial X_t}{\partial\sigma}=(\beta+\gamma)\mathcal V_t^\textsf{BS}=(\beta+\gamma)(T-t)\sigma S_t^2\Gamma_t^\textsf{BS}\,.$$

Assuming the portfolio $X$ is $\Gamma$-neutral but not $\mathcal V$-neutral, we have $\Gamma_t=0$ and $\mathcal V_t\ne0$, or

$$(\beta+\gamma)\Gamma_t^\textsf{BS}=0\,,\quad(\beta+\gamma)(T-t)\sigma S_t^2\Gamma_t^\textsf{BS}\ne0\,,$$

which is impossible. Therefore, the portfolio $X$ that is $\Gamma$-neutral but not $\mathcal V$-neutral does not exist.

## 7.3.b

Since the portfolio $X+Y$ is $\Delta$-neutral, $\Gamma$-neutral, $\Theta$-neutral, and $\mathcal V$-neutral, we have

$$
    \begin{pmatrix}
        1 & \Delta_t^\textsf{BS-C} & \Delta_t^\textsf{BS-P} \\
        & \Gamma_t^\textsf{BS-C} & \Gamma_t^\textsf{BS-P} \\
        & \Theta_t^\textsf{BS-C} & \Theta_t^\textsf{BS-P} & rB_0e^{rt} \\
        & \mathcal V_t^\textsf{BS-C} & \mathcal V_t^\textsf{BS-P}
    \end{pmatrix}
    \begin{pmatrix}\alpha \\ \beta \\ \gamma \\ \delta\end{pmatrix}
    =-
    \begin{pmatrix}
        \Delta_t^Y \\
        \Gamma_t^Y \\
        \Theta_t^Y \\
        \mathcal V_t^Y
    \end{pmatrix}\,,
$$

or

$$
    \begin{pmatrix}\alpha\\\beta\\\gamma\\\delta\end{pmatrix}
    =
    \frac1{\Gamma^PV^C-\Gamma^CV^P}
    \begin{pmatrix}
        (\Gamma^YV^P-\Gamma^PV^Y)\Delta^C-(\Gamma^YV^C-\Gamma^CV^Y)\Delta^P+(\Gamma^PV^C-\Gamma^CV^P)\Delta^Y \\
        -\Gamma^YV^P+\Gamma^PV^Y \\
        \Gamma^YV^C-\Gamma^CV^Y \\
        \frac{-(\Theta^YV^P-\Theta^PV^Y)\Gamma^C+(\Theta^YV^C-\Theta^CV^Y)\Gamma^P-(\Theta^PV^C-\Theta^CV^P)\Gamma^Y}{rB_0e^{rt}}
    \end{pmatrix}
    \,.
$$
