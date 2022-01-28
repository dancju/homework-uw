#!/usr/bin/env python3
from sympy import solve, symbols
from sympy.matrices import Matrix, diag

std = diag(*[0.20, 0.18])
cor = Matrix([[1, -1], [-1, 1]])
cov = std @ cor @ std

w1, w2 = symbols("w1 w2")
w = Matrix(2, 1, [w1, w2])
res = solve([(w.T @ cov @ w)[0, 0], w1 + w2 - 1])

w = w.subs(res[0])
print(w)
print(Matrix(1, 2, [0.13, 0.10]) @ w)
