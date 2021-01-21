#!/usr/bin/env python3
import numpy as np

i_true = 0
i_false = 0
for f_x in np.random.rand(10000):
    for f_y in np.random.rand(10000):
        b = np.all([(f_x < 0.5) ^ (f_y < 0.5), f_x - f_y > -0.5, f_y - f_x > -0.5])
        if b:
            i_true += 1
        else:
            i_false += 1
print(i_true / (i_true + i_false))
