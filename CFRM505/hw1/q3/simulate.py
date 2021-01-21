#!/usr/bin/env python3
import numpy as np

x = np.random.uniform(1, 2, 10000)
y = 1 - x

print(f"Cov(U, 1-U) = {(x * y).mean() - x.mean() * y.mean()}")
print(f"Var(1-U) = {y.var()}")
