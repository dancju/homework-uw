#!/usr/bin/env python3
import numpy as np

ar = np.array(
    [1 if i > 4 else np.exp((i - 4) / 3) for i in np.random.exponential(2, 100000)]
)
print(ar.mean(), ar.var())

ar = np.array(
    [1 if i > 4 else np.exp((i - 4) / 2) for i in np.random.exponential(3, 100000)]
)
print(ar.mean(), ar.var())
