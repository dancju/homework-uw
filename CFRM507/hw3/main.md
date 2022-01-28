---
title: CFRM 507, 2020 Autumn, HW 3
...

# 1

\begin{align*}
  b_1,b_2,b_3,b_4\in\{0,1\} \\
  0\le x,y\le8 \\
  b_1+b_2+b_3+b_4\ge1 \\
  \left(x-y+2\right)b_1\le0 \\
  \left(x-y-2\right)b_2\ge0 \\
  \left(x+y-6\right)b_3\le0 \\
  \left(x+y-10\right)b_4\ge0 \\
\end{align*}

# 2

### Parameters

The logistic cost matrix is defined as

$$\bm a\tran=\begin{pmatrix}
  2 & 1 & 8 & 5 & 7 & 1 & 4 &  6 & 5 & 9 \\
  4 & 9 & 4 & 3 & 9 & 4 & 4 &  2 & 7 & 2 \\
  5 & 8 & 7 & 6 & 7 & 9 & 3 & 10 & 4 & 5 \\
  3 & 5 & 7 & 9 & 7 & 6 & 6 &  5 & 4 & 5 \\
  8 & 7 & 3 & 6 & 8 & 5 & 7 &  4 & 8 & 7 \\
\end{pmatrix}\,.$$

The construction cost vector is defined as

$$\bm b=\begin{pmatrix}10 & 12 & 7 & 8 & 6\end{pmatrix}\,.$$

### Variables

$x_{i,j}\in\{0,1\}$ indicates whether distribution center $i\in\{\text{A \dots J}\}$ supplies city $j\in\{1\dots5\}$.

$y_j\in\{0,1\}$ indicates whether distribution center $j\in\{1\dots5\}$ is built.

### Model

\begin{align*}
  \min\quad &
  \sum_{j\in\{1\dots5\}}b_jy_j+\sum_{i\in\{\text{A \dots J}\}}\sum_{j\in\{1\dots5\}}a_{i,j}x_{i,j}\,, \\
  \text{s.t.}\quad &
  \forall i\in\{\text{A \dots J}\},j\in\{1\dots5\}:x_{i,j}\in\{0,1\}\,, \\&
  \forall j\in\{1\dots5\}:y_j\in\{0,1\}\,, \\&
  \forall i\in\{\text{A \dots J}\},j\in\{1\dots5\}:x_{i,j}\le y_j\,, \\&
  \forall i\in\{\text{A \dots J}\}:\sum_{j\in\{1\dots5\}}x_{i,j}=1\,, \\&
\end{align*}

### Script

\inputminted{ampl}{q2/main.mod}

### Results

The optimal objective value is 53. The optimal variables are

$$\bm x_{\text{A\dots J},1\dots5}=\begin{pmatrix}
  1 & 0 & 0 & 0 & 0 \\
  1 & 0 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 & 0 \\
  1 & 0 & 0 & 0 & 0 \\
  1 & 0 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 & 0 \\
  1 & 0 & 0 & 0 & 0 \\
  0 & 1 & 0 & 0 & 0
\end{pmatrix}\,,$$

and

$$\bm y_{1\dots5}=\begin{pmatrix}1 & 1 & 0 & 0 & 0\end{pmatrix}\,.$$

# 3

### Definitions

The **utility** is defined as 25 if an exceptional candidate is employed, 5 if an acceptable candidate is employed, and 0 if not hiring anyone.

Let $f_{i,j,d}$ indicates the expected utility value under optimal decisions on stage $i\in\{1\dots20\}$, state $j\in\{\text{Exceptional, Acceptable, Unsuitable}\}$, and decision $d\in\{\text{Hire, Skip}\}$.

Let $f_{i, j}=\max_{d}f_{i,j,d}$.

Let $g_{i, j}$ be the optimal decision on stage $i\in\{1\dots20\}$ and state $j\in\{\text{Exceptional, Acceptable, Unsuitable}\}$.

### Boundry Values

$$
  f_{20, j}=\begin{cases}
    25 &
    \text{if }j=\text{E}\,, \\
    5 &
    \text{if }j=\text{A}\,, \\
    1 &
    \text{if }j=\text{U}\,,
  \end{cases}
  \quad
  g_{20, j}=\begin{cases}
    \text{H} &
    \text{if }j=\text{E}\,, \\
    \text{H} &
    \text{if }j=\text{A}\,, \\
    \text{S} &
    \text{if }j=\text{U}\,.
  \end{cases}
$$


### Recursive Equations

For all $i\in\{1\dots19\}$, we have

$$f_{i,\text{E}}=25\,,\quad g_{i,\text{E}}=\text{H}\,,$$

$$f_{i,\text{A},d}=\begin{cases}
  5 &
  \text{if }d=\text{H}\,, \\
  0.02f_{i+1, \text{E}} + 0.2f_{i+1,\text{A}}+0.78f_{i+1,\text{U}} &
  \text{if }d=\text{S}\,,
\end{cases}$$

$$g_{i, \text{A}}=\argmax_{d\in\{\text{H, S}\}}f_{i,\text{A},d}\,,$$

and

$$
  f_{i,\text{U}}=0.02f_{i+1, \text{E}} + 0.2f_{i+1,\text{A}}+0.78f_{i+1,\text{U}}\,,\quad
  g_{i,\text{U}}=\text{S}\,.
$$

### Script

\inputminted{cpp}{q3/main.cpp}

### Results

Executing the script above yields

$$\bm f_{1\dots20,\{\text{E, A, U}\}}=\begin{pmatrix}
  25 & 10.0314  & 10.0314  \\
  25 &  9.72596 &  9.72596 \\
  25 &  9.41425 &  9.41425 \\
  25 &  9.09617 &  9.09617 \\
  25 &  8.77160 &  8.77160 \\
  25 &  8.44041 &  8.44041 \\
  25 &  8.10246 &  8.10246 \\
  25 &  7.75761 &  7.75761 \\
  25 &  7.40573 &  7.40573 \\
  25 &  7.04666 &  7.04666 \\
  25 &  6.68027 &  6.68027 \\
  25 &  6.30639 &  6.30639 \\
  25 &  5.92489 &  5.92489 \\
  25 &  5.53560 &  5.53560 \\
  25 &  5.13837 &  5.13837 \\
  25 &  5       &  4.66458 \\
  25 &  5       &  4.05715 \\
  25 &  5       &  3.2784 \\
  25 &  5       &  2.28 \\
  25 &  5       &  1
\end{pmatrix}\,,$$

$$\bm g_{1\dots20,\{\text{E, A, U}\}}=\begin{pmatrix}
  H & S & S \\
  H & S & S \\
  H & S & S \\
  H & S & S \\
  H & S & S \\
  H & S & S \\
  H & S & S \\
  H & S & S \\
  H & S & S \\
  H & S & S \\
  H & S & S \\
  H & S & S \\
  H & S & S \\
  H & S & S \\
  H & S & S \\
  H & H & S \\
  H & H & S \\
  H & H & S \\
  H & H & S \\
  H & H & S
\end{pmatrix}\,.$$

That is, an exceptional candidate should always be hired; an acceptable candidate should be hired since the 16th day.

# 4

### Definitions

Let $f_{s,c,i}$, $g_{s,c,i,j}$, or $h_{s,c,i,j,d}$ be the exptected outcome in the situation that

1. stage $s\in\{0\dots36\}$,
1. comitted to $c\in\{0\dots s\}$ of the $s$ reviewed projects,
1. with an average anticipated return at $i\in[0.1,0.2]$ for the $c$ projects,
1. with an anticipated return at $j\in\{0.2,0.15,0.1,0\}$ for the project on month $s+1$,
1. decision $d\in\{\text{Commit, Decline}\}$.

### Boundry Values

$$
  f_{s,c,i}=\begin{cases}
    i-0.04\max(0,14-c) &
    \text{if }s=36\text{ and }c\le16\,, \\
    0 &
    \text{if }c\ge17\,. \\
  \end{cases}
$$

### Recursive Equations

$$
f_{s,c,i}
=0.1 g_{s,c,i,0.2}
+0.15g_{s,c,i,0.15}
+0.2 g_{s,c,i,0.1}
+0.55g_{s,c,i,0}
\quad
\text{if }s\le35\text{ and }j\le16
\,,
$$

$$g_{s,c,i,j}=\max_{d\in\{\text{C, D}\}}h_{s,c,i,j,d}\,,$$

$$
  h_{s,c,i,j,d}=\begin{cases}
    f_{s+1,c+1,\frac{ci+j}{c+1}} &
    \text{if }d=\text{C}\,, \\
    f_{s+1,c,i} &
    \text{if }d=\text{D}\,.
  \end{cases}
$$

### Script

\inputminted{cpp}{q4/main.cpp}

### Results

The project should be commited because

$$h_{32,12,0.14,0.1,\text{C}}\approx13.6035\%\,,$$

$$h_{32,12,0.14,0.1,\text{D}}\approx13.2591\%\,,$$

$$\argmax_{d\in\{\text{C, D}\}}h_{32,12,0.14,0.1,d}=\text{Commit}\,.$$

# Extra 1

## E1.a

An intuitive program for the problem is formulated as

\begin{align*}
\min\quad &
\max_{i=1}^n\left|f(x_i)-\sum_{j=1}^mt_jg_j(x_i)\right|\,,
\end{align*}

which is equivalent to the linear program

\begin{align*}
\min\quad &
r\,, \\
\text{s.t.}\quad &
\forall i\in\{1\dots n\}:-r\le f(x_i)-\sum_{j=1}^mt_jg_j(x_i)\le r\,.
\end{align*}

## E1.b

### Script

\inputminted{ampl}{qe1/a.mod}

### Results

#### In the case of $j\in\{0\dots3\}$,

the optimal objective value is 3.48190; and the optimal variable is

$$\bm t_{0\dots3}=\begin{pmatrix}
   2.92112 \\
  -7.90324 \\
   1.31283 \\
   0.963116 \\
\end{pmatrix}\,.$$

#### In the case of $j\in\{0\dots4\}$,

the optimal objective value is 1.00667; and the optimal variable is

$$\bm t_{0\dots4}=\begin{pmatrix}
   6.28373 \\
  -6.78384 \\
  -0.830378 \\
   0.709779 \\
   0.184192 \\
\end{pmatrix}\,.$$

## E1.c

An intuitive program for the problem is formulated as

\begin{align*}
\min\quad &
\sum_{i=1}^n\left|f(x_i)-\sum_{j=1}^mt_jg_j(x_i)\right|\,,
\end{align*}

which is equivalent to the linear program

\begin{align*}
\min\quad &
\sum_{i=1}^nr_i\,, \\
\text{s.t.}\quad &
\forall i\in\{1\dots n\}:-r_i\le f(x_i)-\sum_{j=1}^mt_jg_j(x_i)\le r_i\,.
\end{align*}

### Script

\inputminted{ampl}{qe1/b.mod}

### Results

#### In the case of $j\in\{0\dots3\}$,

the optimal objective value is 23.8012; and the optimal variable is

$$\bm t_{0\dots3}=\begin{pmatrix}
   2.4274  \\
  -9.88493 \\
   1.5066  \\
   1.10065 \\
\end{pmatrix}\,.$$

#### In the case of $j\in\{0\dots4\}$,

the optimal objective value is 4.69450; and the optimal variable is

$$\bm t_{0\dots4}=\begin{pmatrix}
   6.40302  \\
  -7.56582  \\
  -0.646862 \\
   0.769347 \\
   0.165651 \\
\end{pmatrix}\,.$$
