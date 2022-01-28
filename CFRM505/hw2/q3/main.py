#!/usr/bin/env python3
import numpy as np

i_size = 10000
ar_y = -np.log(np.random.rand(i_size))
ar_x = np.random.rand(i_size) ** (1 / ar_y)
print(ar_x.mean())
print(ar_x.var())
