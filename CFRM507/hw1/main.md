---
title: CFRM 507, 2020 Autumn, HW 1
...

# 1

## 1.a

The basic feasible solutions are $(7,0)$, $(9,6)$, $(5,5)$, and $(2,1)$. The basic infeasible solutions are $(203/19, -14/19)$, $(58/5, 69/5)$, $(131/16, 37/4)$, and $(-47/9, 22/9)$.

## 1.b

The constraint defined by $4x+y\le42$ is redundant.

## 1.c

The objective function $$\text{max}\quad4x+y$$ makes the LP having a finite optimal solution.

## 1.d

The objective function $$\text{max}\quad-x+4y$$ makes the LP having multiple (actually infinite number of) optimal solutions. The optimal objective value is $15$, while two associated optimal solutions are $(5, 5)$ and $(9, 6)$.

## 1.e

Such an objective function does not exist. Since the feasible region is bounded, the linear objective function is also bounded.

## 1.f

Such an objective function does not exist. Since the feasible region is not empty, the LP model is feasible.

# 2

## 2.a

Let the decision variables be $I$, and $A$, while the slack variables be $s_u, s_l, s_a$, and $s_c$. The decision variable vector is $\bm{x}=(I,A,s_u,s_l,s_a,s_c)\tran$. The LP model is

\begin{align*}
\text{max}\quad &
\begin{pmatrix}600&200&0&0&0&0\end{pmatrix}\bm{x}, \\
\text{s.t.}\quad &
\begin{pmatrix}4&2&1\\1&1&&1\\0&2&&&1\\2&0&&&&1\end{pmatrix}\bm{x}=\begin{pmatrix}2400\\1100\\800\\1400\end{pmatrix}, \\
& \bm{x}\ge\bm{0}.
\end{align*}

## 2.b

\includegraphics{q2/main.pdf}

## 2.c

The optimal solution is $(600,0,0,500,800,200)\tran$ while the optimal objective value is $3.6\times10^5$.

## 2.d

The given constraints are equivalent to

\begin{equation*}
\left\{\begin{aligned}
2\,\text{Insurance}-3\,\text{Annuity} \le0, \\
-3\,\text{Insurance}+2\,\text{Annuity} \le0.
\end{aligned}\right.
\end{equation*}

Letting the two additional slack variables be $s_{h0}$ and $s_{h1}$, combining the constraints with the LP model in \textbf{(a)} yields

\begin{align*}
\text{max}\quad &
\begin{pmatrix}600&200&0&0&0&0&0&0\end{pmatrix}\bm{x}, \\
\text{s.t.}\quad &
\begin{pmatrix}4&2&1\\1&1&&1\\0&2&&&1\\2&0&&&&1\\2&-3&&&&&1\\-3&2&&&&&&1\end{pmatrix}\bm{x}=\begin{pmatrix}2400\\1100\\800\\1400\\0\\0\end{pmatrix},\\
& \bm{x}\ge\bm{0}.
\end{align*}

## 2.e

The solution in \textbf{(c)} does \emph{not} apply to the model in \textbf{(d)}, because the solution is not in the feasible region of the model.

## 2.f

Such an objective function does not exist as the reason is specified in \textbf{(1.e)}.

## 2.g

Such an objective function does not exist as the reason is specified in \textbf{(1.f)}.

# 3

\includegraphics{q3/main.pdf}

## 3.a

The optimal solution is

$$
\begin{pmatrix}
I\\A\\s_u\\s_l\\s_a\\s_c\\s_{h0}\\s_{h1}
\end{pmatrix}^*
=
\begin{pmatrix}
450\\300\\0\\350\\200\\500\\0\\750
\end{pmatrix},
$$

and the optimal objective value is $3.3\times10^5$.

## 3.b

The basic variables are $i, a, s_l, s_a, s_c$, and $s_{h1}$.

## 3.c

The constraint of the Underwriting Department and the first constraint defined in \textbf{(2.d)} are active.

## 3.d

The constraints of the Legal, Administration, Claims departments, and the second constraint defined in \textbf{(2.d)} are inactive.

## 3.e

The partial derivative of the optimal objective value w.r.t.\ the RHS is

\begin{align*}
\frac{\partial \bm{c}_B\bm{B}^{-1}\bm{b}}{\partial\bm{b}}
&= \bm{c}_B\bm{B}^{-1} \\
&=
\begin{pmatrix}600&200&0&0&0&0\end{pmatrix}
\begin{pmatrix}
4&2 \\
1&1&1 \\
0&2&&1 \\
2&0&&&1 \\
2&-3 \\
-3&2&&&&1
\end{pmatrix}^{-1}
\\
&= \begin{pmatrix}137.5&0&0&0&25&0\end{pmatrix}.
\end{align*}

Therefore, the marginal value of an additional service hour from the Underwriting Department is $137.5$. The marginal values from the Legal, Administration, and Claims departements are 0.

## 3.f

The partial derivative of the optimal objective value w.r.t.\ the RHS is

\begin{equation*}
\frac{\partial \bm{c}_B\bm{B}^{-1}\bm{b}}{\partial\bm{b}}=\begin{pmatrix}137.5&0&0&0&25&0\end{pmatrix}.
\end{equation*}

Issuing one contract of Car Insurance would cost

\begin{equation*}
\begin{pmatrix}137.5&0&0&0\end{pmatrix}
\begin{pmatrix}1.5&2&2.5&4\end{pmatrix}\tran
=206.25
\end{equation*}

dollars. Therefore, a profit of at least $\$206.25$ is needed for this product to be attractive to the company.

# 4

<!--
Extracting the active constraints from the Furniture Maker Problem and assuming two hours of temporary labor hired yields

$$
\begin{pmatrix}5&40\\3&10\end{pmatrix}
\begin{pmatrix}C\\T\end{pmatrix}
=\begin{pmatrix}4000\\1801\end{pmatrix}.
$$

Solving this equation yields the new optimal solution $(C,T)\tran=(3208/7,299/7)\tran$ and the new optimal objective value $779850/7\approx 111407.14$, which is smaller than the original objective value $111428.57$. Therefore, it is not advisable to hire temporary labor.
-->

The partial derivative of the optimal objective value w.r.t.\ the RHS is

\begin{align*}
\frac{\partial \bm{c}_B\bm{B}^{-1}\bm{b}}{\partial\bm{b}}
&= \bm{c}_B\bm{B}^{-1} \\
&=
\begin{pmatrix}1000&150&0\end{pmatrix}
\begin{pmatrix}
40&5&0 \\
10&3&0 \\
4&-1&1
\end{pmatrix}^{-1}
\\
&= \begin{pmatrix}150/7&100/7&0\end{pmatrix}.
\end{align*}

Hence, hiring two additional hour of temporary labor change the profit by $\frac{150}{7}-50\approx -28.57$ dollars. Therefore, it is not advisable to hire temporary labor.

# 6

Define $\bm{x}$ as

\begin{equation*}
\begin{pmatrix}
\text{area of corn land in acres} \\
\text{area of oat land in arces}
\end{pmatrix},
\end{equation*}

and the LP model is

\begin{align*}
\text{max}\quad &
\begin{pmatrix}142&128\end{pmatrix}\bm{x}, \\
\text{s.t.}\quad &
\begin{pmatrix}1&1\\2&1.5\end{pmatrix}\bm{x}\le\begin{pmatrix}1250\\350\end{pmatrix}, \\
& \bm{x}\ge\bm{0}.
\end{align*}

# 7

There will be $\left\lceil\frac{1200}{350}\right\rceil=6$ payments received in the following days:

\begin{center}\begin{tabular}{lr}
\toprule
Date & \# of months \\
\midrule
Jun 1, year 0 & 5 \\
Dec 1, year 0 & 11 \\
Jun 1, year 1 & 17 \\
Dec 1, year 1 & 23 \\
Jun 1, year 2 & 29 \\
Dec 1, year 2 & 35 \\
\bottomrule
\end{tabular}\end{center}

Letting the monthly return rate be $\alpha$, we have

\begin{align*}
\frac{2000}{350}=&
\frac{1}{(1+\alpha)^5}
+\frac{1}{(1+\alpha)^{11}}
+\frac{1}{(1+\alpha)^{17}} \\&
+\frac{1}{(1+\alpha)^{23}}
+\frac{1}{(1+\alpha)^{29}}
+\frac{1}{(1+\alpha)^{35}}.
\end{align*}

Numerically solving this equation with the Newton–Raphson method, we get the monthly return rate being

$$\alpha\approx 0.002458349171524.$$

Consequently, the annual return rate is

$$(1+\alpha)^{12}-1\approx 0.0299023464685002\approx 2.99\%.$$

# 8

Being a NP problem, this Jigsaw Sudoku problem can be reduced to any NP-complete problem. I will reduce it to an Exact Cover Problem and resolve it with Dancing Links, which is empirically the most efficient way to solve Sudoku problems. The algorithm is described as follows.

1. Mark each row, column, and irregular group with number 1 to 5.
1. Define four sets $L_{i,j}$, $R_{i,j}$, $C_{i,j}$, and $G_{i,j}$, with $i,j\in\{1,\dots,5\}$, each of which contains 25 items.
1. Define _constraint_ as a tuple of 4 items each comes from $L$, $R$, $C$, $G$.
1. Create an empty set of constraints $P$.
1. For each cell in Sudoku with a given number, e.g.\ number $n$ located in row $r$, column $c$, and irregular group $g$, create a constraint $(L_{r,c},R_{r,n},C_{c,n},G_{g,n})$ and add it into $P$.
1. For each cell in Sudoku without a given number, e.g.\ no number given in row $r$, column $c$, and irregular group $g$, create five constraint $(L_{r,c},R_{r,n},C_{c,n},G_{g,n})$ with $n\in\{1,\dots,5\}$, and add them into $P$.
1. Run Dancing Links on $P$, the output $P'$ would be a subset of $P$ and an exact cover of the four sets.
1. For each item in $P'$, convert it to a number with a specific cell in Sudoku.

The source code solving the given Jigsaw Sudoku problem is listed as follows. The Dancing Links library invoked here (`exact_cover_solver.hpp`) is from \url{https://github.com/nerddan/dancing-links}.

```cpp
#include <exact_cover_solver.hpp>
#include <iostream>
using boost::coroutines::coroutine;
using dancing_links::exact_cover_solver;
using std::array;
using std::cout;
using std::endl;
using std::vector;

int main() {
  vector<array<int, 4>> puzzle;
  auto add_item_k = [&puzzle](int row, int col, int gro, int n) {
    n--;
    puzzle.push_back(array<int, 4>{
        row * 5 + col, 25 + row * 5 + n,
        50 + col * 5 + n, 75 + gro * 5 + n
    });
  };
  auto add_item_n = [&add_item_k](int row, int col, int gro) {
    for (int i = 1; i <= 5; i++)
      add_item_k(row, col, gro, i);
  };

  add_item_k(0, 0, 0, 3);
  add_item_n(0, 1, 1);
  add_item_n(0, 2, 1);
  add_item_n(0, 3, 1);
  add_item_n(0, 4, 1);

  add_item_n(1, 0, 0);
  add_item_n(1, 1, 0);
  add_item_n(1, 2, 2);
  add_item_k(1, 3, 2, 2);
  add_item_n(1, 4, 1);

  add_item_n(2, 0, 0);
  add_item_n(2, 1, 3);
  add_item_k(2, 2, 2, 5);
  add_item_n(2, 3, 2);
  add_item_n(2, 4, 4);

  add_item_n(3, 0, 0);
  add_item_k(3, 1, 3, 4);
  add_item_n(3, 2, 3);
  add_item_n(3, 3, 2);
  add_item_n(3, 4, 4);

  add_item_n(4, 0, 3);
  add_item_n(4, 1, 3);
  add_item_n(4, 2, 4);
  add_item_n(4, 3, 4);
  add_item_k(4, 4, 4, 1);

  exact_cover_solver ecs{100, puzzle.cbegin(), puzzle.cend()};
  coroutine<vector<vector<size_t>>>::pull_type solution_source{
      bind(&exact_cover_solver::solve, &ecs, std::placeholders::_1)
  };
  for (auto s : solution_source) {
    assert(s.size() == 25);
    array<int, 25> grid;
    for (auto i : s) {
      sort(i.begin(), i.end());
      assert(i[1] % 5 == i[2] % 5);
      grid[i[0]] = i[1] % 5 + 1;
    }
    for (int i = 0; i < 5; i++) {
      for (int j = 0; j < 5; j++)
        cout << grid[i * 5 + j];
      cout << endl;
    }
    cout << endl;
  }
  return 0;
}
```

The output of this program is listed as follows. Note that this is the only solution to the given problem.

\begin{centering}
31254 \\
15423 \\
43512 \\
24135 \\
52341 \\
\end{centering}

# extra 1

Letting $\bm{y}=\frac{|\bm{x}|+\bm{x}}{2}$ and $\bm{z}=\frac{|\bm{x}|-\bm{x}}{2}$, we have $\bm{x}=\bm{y}-\bm{z}$ and $|\bm{x}|=\bm{y}+\bm{z}$. Plugging into the original problem yields

\begin{align*}
\text{max}\quad &
-\bm{e}\tran(\bm{y}+\bm{z}), \\
\text{s.t.}\quad &
\bm{A}(\bm{y}-\bm{z})\ge\bm{b}, \\
& \bm{y}, \bm{z}\ge\bm{0},
\end{align*}

which is equivalent to the LP problem

\begin{align*}
\text{max}\quad &
-\bm{e}\tran\begin{pmatrix}\bm{y}\\\bm{z}\end{pmatrix}, \\
\text{s.t.}\quad &
\begin{pmatrix}\bm{A}&-\bm{A}\end{pmatrix}
\begin{pmatrix}\bm{y}\\\bm{z}\end{pmatrix}
\ge\bm{b}, \\
& \begin{pmatrix}\bm{y}\\\bm{z}\end{pmatrix}\ge\bm{0}.
\end{align*}

Once this LP problem is solved, we can work out the solution of the original problem by $$\bm{x^*}=\bm{y^*}-\bm{z^*}.$$

# extra 2

**Problem**

If $\bm{A}$ is skew-symmetric ($\bm{A}\tran=-\bm{A}$), what is the optimal objective function value for the following linear program (assuming that it is feasible)?

\begin{align*}
\text{min}\quad &
\bm{c}\tran\bm{x}, \\
\text{s.t.}\quad
& \bm{Ax}\ge-\bm{c}, \\
& \bm{x}\ge\bm{0}.
\end{align*}

**Solution**
