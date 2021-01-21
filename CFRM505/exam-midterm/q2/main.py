#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

ar = 3 - 2 * np.log(np.e - (np.e - 1) * np.random.rand(100000))
print(ar.mean())
print(ar.var())
plt.xlabel("$Y$")
plt.ylabel("Density")
plt.hist(ar, 32, density=True)
plt.savefig("main.pdf")
