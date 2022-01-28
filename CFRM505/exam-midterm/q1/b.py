#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def generate():
    for u in np.random.rand(100000):
        if u < 0.5:
            yield np.random.rand() ** 0.5
        else:
            yield np.random.rand() ** 0.25


ar = np.array([i for i in generate()])
print(ar.mean())
print(ar.var())
plt.xlabel("$X$")
plt.ylabel("Density")
plt.hist(ar, 32, density=True)
plt.savefig("b.pdf")
