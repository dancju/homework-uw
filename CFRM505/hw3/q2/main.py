#!/usr/bin/env python3
import numpy as np


def nhpp(lambda_func, lambda_max, t_max):
    t = 0
    while True:
        t -= np.log(np.random.rand()) / lambda_max
        if t > t_max:
            break
        if np.random.rand() <= lambda_func(t) / lambda_max:
            yield t


ar = [nhpp(lambda x: (2 + x + x ** 2) / 100, 1.12, 10) for i in range(10000)]
ar = [np.random.choice([100, 400, 900], len(list(i))).sum() for i in ar]
print(np.mean(ar))
print(np.var(ar))
