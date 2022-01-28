#!/usr/bin/env python3
import numpy as np

ar = np.array(
    [
        a * a + b * b < 3 / 2
        for a in np.random.uniform(-1, 1, 10000)
        for b in np.random.uniform(-1, 1, 10000)
    ]
)
print(ar.mean())
