#!/usr/bin/env python3
import numpy as np

ar = np.array(
    [
        1 if a * a < 1 / 2 else (3 / 2 - a * a) ** 0.5
        for a in np.random.uniform(-1, 1, 10000)
    ]
)
print(ar.mean())
