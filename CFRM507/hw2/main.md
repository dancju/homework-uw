---
title: CFRM 507, 2020 Autumn, HW 2
...

<!--
\usepackage{printlen}
\uselengthunit{in}
\printlength{\linewidth}
-->

# 1

**a. true.** Since the price of chairs is an item in the basic matrix $\bm B$, a tampering to it causes a different optimal solution $\bm B^{-1}\bm b$.

**b. false.** Eliminating non-binding constraints does not change the feasible region and consequently does not change the optimal solution.

**c. false.** All constraints are binding in the Furniture Maker Problem.

**d. true.** When the RHS value is decreased, the feasible region becomes smaller and the constraint becomes more restrictive.

**e. true.** A bounded feasible region bonds all variables, which transitively bond the objective function that is a linear combination of the variables.

# 2

## 2.a

Let $x_i$ be the amount of exchange-traded equity invested in year $i$ ($i\in\{1,\cdots,12\}$), $y_i$ be the amount of private equity in the secondary market invested in year $i$ ($i\in\{1,\cdots,10\}$), and $z_i$ be the amount of primary private equity invested in year $i$ ($i\in\{1,\cdots,8\}$).

The problem is formulated as follows.

\begin{align*}
  \text{max}\quad & w, \\
  \text{s.t.}\quad & \bm x,\bm y,\bm z\ge\bm0, \\
  & \begin{aligned}
    -x_{1}  &            &-y_{1}  &              &-z_{1} &             &= -10,000,000, \\
    -x_{2}  &+1.06x_{1}  &-y_{2}  &              &-z_{2} &             &= 0, \\
    -x_{3}  &+1.06x_{2}  &-y_{3}  &              &-z_{3} &             &= 0, \\
    -x_{4}  &+1.06x_{3}  &-y_{4}  &+1.12^3y_{1}  &-z_{4} &             &= 0, \\
    -x_{5}  &+1.06x_{4}  &-y_{5}  &+1.12^3y_{2}  &-z_{5} &             &= 0, \\
    -x_{6}  &+1.06x_{5}  &-y_{6}  &+1.12^3y_{3}  &-z_{6} &+1.16^5z_{1} &= 0, \\
    -x_{7}  &+1.06x_{6}  &-y_{7}  &+1.12^3y_{4}  &-z_{7} &+1.16^5z_{2} &= 0, \\
    -x_{8}  &+1.06x_{7}  &-y_{8}  &+1.12^3y_{5}  &-z_{8} &+1.16^5z_{3} &= 0, \\
    -x_{9}  &+1.06x_{8}  &-y_{9}  &+1.12^3y_{6}  &       &+1.16^5z_{4} &= 0, \\
    -x_{10} &+1.06x_{9}  &-y_{10} &+1.12^3y_{7}  &       &+1.16^5z_{5} &= 0, \\
    -x_{11} &+1.06x_{10} &        &+1.12^3y_{8}  &       &+1.16^5z_{6} &= 0, \\
    -x_{12} &+1.06x_{11} &        &+1.12^3y_{9}  &       &+1.16^5z_{7} &= 0, \\
            &+1.06x_{12} &        &+1.12^3y_{10} &       &+1.16^5z_{8} &= w,
  \end{aligned} \\
  & \begin{aligned}
    -x_{1}  &+y_{1}  &       &+3z_{1} &        &       &       &\le0, \\
    -x_{2}  &+y_{2}  &       &+3z_{2} &+2z_{1} &       &       &\le0, \\
    -x_{3}  &+y_{3}  &-y_{1} &+3z_{3} &+2z_{2} &+z_{1} &       &\le0, \\
    -x_{4}  &+y_{4}  &-y_{2} &+3z_{4} &+2z_{3} &+z_{2} &       &\le0, \\
    -x_{5}  &+y_{5}  &-y_{3} &+3z_{5} &+2z_{4} &+z_{3} &-z_{1} &\le0, \\
    -x_{6}  &+y_{6}  &-y_{4} &+3z_{6} &+2z_{5} &+z_{4} &-z_{2} &\le0, \\
    -x_{7}  &+y_{7}  &-y_{5} &+3z_{7} &+2z_{6} &+z_{5} &-z_{3} &\le0, \\
    -x_{8}  &+y_{8}  &-y_{6} &+3z_{8} &+2z_{7} &+z_{6} &-z_{4} &\le0, \\
    -x_{9}  &+y_{9}  &-y_{7} &        &+2z_{8} &+z_{7} &-z_{5} &\le0, \\
    -x_{10} &+y_{10} &-y_{8} &        &        &+z_{8} &-z_{6} &\le0.
  \end{aligned}
\end{align*}

## 2.b

The source code is listed as follows.

\begin{lstlisting}[language=Python,basicstyle=\tiny]
library('Rglpk')

m = Matrix(0, 24, 30, sparse = TRUE)

m[ 1, 1]=-1;                m[ 1,12+ 1]=-1;                     m[1,22+1]=-1;
m[ 2, 2]=-1; m[ 2, 1]=1.06; m[ 2,12+ 2]=-1;                     m[2,22+2]=-1;
m[ 3, 3]=-1; m[ 3, 2]=1.06; m[ 3,12+ 3]=-1;                     m[3,22+3]=-1;
m[ 4, 4]=-1; m[ 4, 3]=1.06; m[ 4,12+ 4]=-1; m[ 4,12+1]=1.12**3; m[4,22+4]=-1;
m[ 5, 5]=-1; m[ 5, 4]=1.06; m[ 5,12+ 5]=-1; m[ 5,12+2]=1.12**3; m[5,22+5]=-1;
m[ 6, 6]=-1; m[ 6, 5]=1.06; m[ 6,12+ 6]=-1; m[ 6,12+3]=1.12**3; m[6,22+6]=-1; m[ 6,22+1]=1.16**5;
m[ 7, 7]=-1; m[ 7, 6]=1.06; m[ 7,12+ 7]=-1; m[ 7,12+4]=1.12**3; m[7,22+7]=-1; m[ 7,22+2]=1.16**5;
m[ 8, 8]=-1; m[ 8, 7]=1.06; m[ 8,12+ 8]=-1; m[ 8,12+5]=1.12**3; m[8,22+8]=-1; m[ 8,22+3]=1.16**5;
m[ 9, 9]=-1; m[ 9, 8]=1.06; m[ 9,12+ 9]=-1; m[ 9,12+6]=1.12**3;               m[ 9,22+4]=1.16**5;
m[10,10]=-1; m[10, 9]=1.06; m[10,12+10]=-1; m[10,12+7]=1.12**3;               m[10,22+5]=1.16**5;
m[11,11]=-1; m[11,10]=1.06;                 m[11,12+8]=1.12**3;               m[11,22+6]=1.16**5;
m[12,12]=-1; m[12,11]=1.06;                 m[12,12+9]=1.12**3;               m[12,22+7]=1.16**5;

m[13, 1]=-1; m[13,12+ 1]=1;                 m[13,22+1]=3;
m[14, 2]=-1; m[14,12+ 2]=1;                 m[14,22+2]=3; m[14,22+1]=2;
m[15, 3]=-1; m[15,12+ 3]=1; m[15,12+ 1]=-1; m[15,22+3]=3; m[15,22+2]=2; m[15,22+1]=1;
m[16, 4]=-1; m[16,12+ 4]=1; m[16,12+ 2]=-1; m[16,22+4]=3; m[16,22+3]=2; m[16,22+2]=1;
m[17, 5]=-1; m[17,12+ 5]=1; m[17,12+ 3]=-1; m[17,22+5]=3; m[17,22+4]=2; m[17,22+3]=1; m[17,22+1]=-1;
m[18, 6]=-1; m[18,12+ 6]=1; m[18,12+ 4]=-1; m[18,22+6]=3; m[18,22+5]=2; m[18,22+4]=1; m[18,22+2]=-1;
m[19, 7]=-1; m[19,12+ 7]=1; m[19,12+ 5]=-1; m[19,22+7]=3; m[19,22+6]=2; m[19,22+5]=1; m[19,22+3]=-1;
m[20, 8]=-1; m[20,12+ 8]=1; m[20,12+ 6]=-1; m[20,22+8]=3; m[20,22+7]=2; m[20,22+6]=1; m[20,22+4]=-1;
m[21, 9]=-1; m[21,12+ 9]=1; m[21,12+ 7]=-1;               m[21,22+8]=2; m[21,22+7]=1; m[21,22+5]=-1;
m[22,10]=-1; m[22,12+10]=1; m[22,12+ 8]=-1;                             m[22,22+8]=1; m[22,22+6]=-1;

Rglpk_solve_LP(
  obj = c(
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.06,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 1.12**3,
    0, 0, 0, 0, 0, 0, 0, 1.16**5
  ),
  mat = m,
  dir = c(rep('==', 12), rep ('<=', 12)),
  rhs = c(-1e7, rep(0, 23)),
  bounds = list(
    lower = list(ind = 1:30, val = rep(0, 30)),
    upper = list(ind = 1:30, val = rep(Inf, 30))
  ),
  types = rep('C', 30),
  max = TRUE
)
\end{lstlisting}

### 2.b.i

The optimal solution is

$$
\bm x^*\approx\begin{pmatrix}5474057.726427\\3375308.321433\\0\\1632706.592237\\544407.8315461\\1269722.555562\\1226739.979944\\4485947.674220\\6481760.251664\\9161731.817926\\9711435.727001\\18388023.74684\end{pmatrix},
\bm y^*\approx\begin{pmatrix}4051884.547146\\2427192.868579\\3577826.820719\\4059899.460816\\4596292.378692\\5329622.016378\\5823032.358637\\0\\5761079.483235\\5889875.254393\end{pmatrix},
\bm z^*\approx\begin{pmatrix}474057.7264269\\0\\0\\0\\0\\0\\0\\3271856.563533\end{pmatrix}.
$$

The optimal objective value is $34638172.4711376$.

### 2.b.ii

The basic variables in the optimal solution are $x_1, x_2, x_4, x_5, x_6, x_7, x_8, x_9, x_{10}$, $x_{11}, x_{12}, y_1, y_2, y_3, y_4, y_5, y_6, y_7, y_9, y_{10}, z_1, z_8$.

### 2.b.iii

All constraints are active at the optimal solution.

### 2.b.iv

None constraints are active at the optimal solution.

### 2.b.v

None could the investment amount decrease before a different solution is optimal, because the concerning constraint is active. As a matter of fact, since the model is homogeneous, any change to the investment amount causes a proportional change to the optimal solution.

# 3

## 3.a

Let $\bm x$ be the proportions of funds spent on each strategies of Joe, and $\bm y$ be the proportions of funds spent on each strategies of Donald.

Joe's LP problem is

\begin{align*}
\text{max}\quad &
v, \\
\text{s.t.}\quad
& \bm x\ge\bm0, \\
& \bm e\tran\bm x=1, \\
& \bm A\bm x\ge v\bm e, \\
& v\text{ is unrestricted},
\end{align*}

and Donald's LP problem is

\begin{align*}
\text{min}\quad &
w, \\
\text{s.t.}\quad
& \bm y\ge\bm0, \\
& \bm y\tran\bm e=1, \\
& \bm y\tran\bm A\le w\bm e\tran, \\
& w\text{ is unrestricted},
\end{align*}

where

$$\bm A=\begin{pmatrix}2&-5&5\\3&-15&10\\-8&5&-6\end{pmatrix}.$$

## 3.b

Solving both LP problems yields

$$
\bm x^*=\begin{pmatrix}0&\frac{4}{9}&\frac{5}{9}\end{pmatrix}\tran, \quad
\bm y^*=\begin{pmatrix}0&\frac{11}{36}&\frac{25}{36}\end{pmatrix}\tran,
$$

$$\text{max}\,v=\text{min}\,w=-10/9.$$

The optimal strategy for Joe is spending $\frac{4}{9}$ of his funds on newspaper ads and spending $\frac{5}{9}$ of his funds on sending emails. The optimal strategy for Donald is spending $\frac{11}{36}$ of his funds on windshield flyers and spending $\frac{25}{36}$ of his funds on mayor's endorsement. The outcome is Donald gainning $10/9\approx1.11\%$. Since Donald trails by 6\%, Joe will win.

## 3.c

Joe's LP problem equivalent to

\begin{align*}
  \text{max}\quad &
  \begin{pmatrix}\bm0&1\end{pmatrix}\begin{pmatrix}\bm x\\v\end{pmatrix}, \\
  \text{s.t.}\quad
  & \begin{pmatrix}
    -\bm I&0\\-\bm e\tran&0\\\bm e\tran&0\\-\bm A&\bm e
  \end{pmatrix}
  \begin{pmatrix}\bm x\\v\end{pmatrix}
  \le
  \begin{pmatrix}\bm0\\-1\\1\\\bm0\end{pmatrix},
\end{align*}

whose (asymmetric) dual problem is

\begin{align*}
  \text{min}\quad &
  \begin{pmatrix}\bm0&-1&1&\bm0\end{pmatrix}
  \bm z, \\
  \text{s.t.}\quad
  & \begin{pmatrix}
    -\bm I&-\bm e&\bm e&-\bm A\tran\\
    0&0&0&\bm e\tran
  \end{pmatrix}
  \bm z
  =
  \begin{pmatrix}\bm0\\1\end{pmatrix}, \\
  & \bm z\ge\bm0.
\end{align*}

which is equivalent to

\begin{align*}
  \text{min}\quad &
  z_3-z_2, \\
  \text{s.t.}\quad
  & \bm z_4\tran\bm A\le(z_3-z_2)\bm e\tran \\
  & \bm z_4\tran\bm e=1 \\
  & \bm z_4\ge\bm0,
\end{align*}

where $\bm z=\begin{pmatrix}\bm z_1\tran&z_2&z_3&\bm z_4\tran\end{pmatrix}\tran$. Substituting $\bm z_4$ with $\bm y$ and $z_3-z_2$ with $w$, the LP problem becomes

\begin{align*}
  \text{min}\quad &
  w, \\
  \text{s.t.}\quad
  & \bm y\tran\bm A\le w\bm e\tran \\
  & \bm y\tran\bm e=1 \\
  & \bm y\ge\bm0.
\end{align*}

That proves the dual of Joe's LP problem is Donald's LP problem.

# extra 1

\includegraphics{qe1/main.pdf}

## e1.a

The optimal solution is

$$
\bm x^*\approx\begin{pmatrix}0\\50.98039215686\\0\\0\\0\end{pmatrix},
\bm y^*\approx\begin{pmatrix}150\\49.01960784314\\203.4343635760\end{pmatrix},
\bm z^*\approx\begin{pmatrix}0\\0\\351.9441674975\\0\\0\\92.49694915254\end{pmatrix}.
$$

## e1.b

The basic variables are $x_2, y_1, y_2, y_3$, and $z_3$.

## e1.c

All the equality constraints are active.

## e1.d

All the non-negativity constraints are inactive.

## e1.e

Decreasing of \$1 to the line of credit have no impact since the credit is not fully used in the optimal solution ($\|\bm x^*\|_\infty\approx50.98<100$).

# extra 2

# extra 3

The standard primal is

\begin{align*}
  \text{min}\quad &
  \bm c\tran\bm x, \\
  \text{s.t.}\quad &
    \bm A\bm x=\bm b, \\ &
    \bm x\ge\bm0,
\end{align*}

which is equivalent to the problem in von Neumann form

\begin{align*}
  \text{min}\quad &
  \bm c\tran\bm x, \\
  \text{s.t.}\quad &
    \begin{pmatrix}\bm A\\-\bm A\end{pmatrix}\bm x\ge\begin{pmatrix}\bm b\\-\bm b\end{pmatrix}, \\ &
    \bm x\ge\bm0,
\end{align*}

whose dual is

\begin{align*}
  \text{max}\quad &
  \begin{pmatrix}\bm b\tran&-\bm b\tran\end{pmatrix}\begin{pmatrix}\bm\alpha\\\bm\beta\end{pmatrix}
  , \\
  \text{s.t.}\quad &
    \begin{pmatrix}\bm A\tran&-\bm A\tran\end{pmatrix}\begin{pmatrix}\bm\alpha\\\bm\beta\end{pmatrix}\le\bm c, \\ &
    \bm\alpha,\bm\beta\ge\bm0.
\end{align*}

Let $\bm y=\bm\alpha-\bm\beta$. Plugging in the problem yields the standard dual

\begin{align*}
  \text{max}\quad &
  \bm b\tran\bm y, \\
  \text{s.t.}\quad
  & \bm A\tran\bm y\le\bm c, \\
  & \bm y\text{ is unrestricted}.
\end{align*}

# extra 4

It is possible for both the primal and the dual to be infeasible. Here is an example. Two LP problems listed below are both infeasible and dual to each other.

\begin{align*}
  \text{max}\quad &
  2x_1-x_2, \\
  \text{s.t.}\quad
  & x_1-x_2\le1, \\
  & -x_1+x_2\le-2, \\
  & x_1,x_2\ge0.
\end{align*}

\begin{align*}
  \text{min}\quad &
  y_1-2y_2, \\
  \text{s.t.}\quad
  & y_1-y_2\ge2, \\
  & -y_1+y_2\ge-1, \\
  & y_1,y_2\ge0.
\end{align*}

# extra 5

## e5.a

The problem is equivalent to finding the center of the largest inscribed hypersphere of the convex hull. Let $r$ be the radius of the inscribed hypersphere. We have the following problem.

\begin{align*}
  \text{max}\quad & r, \\
  \text{s.t.}\quad & \bm d(\bm x)\ge r\bm e,
\end{align*}

which is equivalent to

\begin{align*}
  \text{max}\quad &
    \begin{pmatrix}\bm0&1\end{pmatrix}
    \begin{pmatrix}\bm x\\r\end{pmatrix}, \\
  \text{s.t.}\quad &
    \begin{pmatrix}\bar{\bm A}&\bm e\\\end{pmatrix}
    \begin{pmatrix}\bm x\\r\end{pmatrix}
    \le
    \bar{\bm b},
\end{align*}

where $\bm A$ and $\bm b$ denote all constraints of the LP problem including non-negativity constraints.

## e5.b

The constraints of the Furniture Maker Problem is

$$
\begin{pmatrix}5&40\\3&10\\-1&4\\-1&0\\0&-1\end{pmatrix}
\bm x\le
\begin{pmatrix}4000\\1800\\23\\0\\0\end{pmatrix}.
$$

The corresponding LP problem finding the center is

\begin{align*}
  \text{max}\quad &
    \begin{pmatrix}\bm0&1\end{pmatrix}
    \begin{pmatrix}\bm x\\r\end{pmatrix}, \\
  \text{s.t.}\quad &
    \begin{pmatrix}
    \frac{1}{\sqrt{65}}&\frac{8}{\sqrt{65}}&1 \\
    \frac{3}{\sqrt{109}}&\frac{10}{\sqrt{109}}&1 \\
    -\frac{1}{\sqrt{17}}&\frac{4}{\sqrt{17}}&1 \\
    -1&0&1 \\
    0&-1&1 \\
    \end{pmatrix}
    \begin{pmatrix}\bm x\\r\end{pmatrix}\le
    \begin{pmatrix}
    \frac{800}{\sqrt{65}}\\
    \frac{1800}{\sqrt{109}}\\
    \frac{23}{\sqrt{17}}\\
    0\\
    0\\
    \end{pmatrix}.
\end{align*}

Solving the problem yields

$$
\bm x\approx\begin{pmatrix}253.42 \\ 34.0288\end{pmatrix},
\quad
r\approx34.0288.
$$

## e5.c

\includegraphics{qe5/main.pdf}
