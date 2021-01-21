#!/usr/bin/env python3
import numpy as np

f_lambda = 1
print(np.mean(-np.log(np.random.rand(10000)) / 3 / f_lambda))
