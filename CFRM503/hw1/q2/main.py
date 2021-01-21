#!/usr/bin/env python3
import numpy as np
from numpy.linalg import LinAlgError, cholesky


def is_positive_definite(x):
    try:
        cholesky(x)
        return True
    except LinAlgError:
        return False


def func(x):
    cov = [
        [0.02890, 0.01530, 0.00816, 0.00765],
        [0.01530, 0.02250, x / 2, 0.00405],
        [0.00816, x / 2, 0.01440, 0.00756],
        [0.00765, 0.00405, 0.00756, 0.00810],
    ]
    return is_positive_definite(cov)


def get_root(func, lo, hi):
    mid = (lo + hi) / 2
    if abs(hi - lo) < np.finfo(float).eps:
        return mid
    res = [func(lo), func(mid), func(hi)]
    assert res[0] != res[2]
    if res[0] == res[1]:
        return get_root(func, mid, hi)
    elif res[1] == res[2]:
        return get_root(func, lo, mid)


print(get_root(func, -1, 0), get_root(func, 0, 1))
