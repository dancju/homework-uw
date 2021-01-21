#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def sample_rejection_(gen_y, pdf_x, pdf_y, f_ratio):
    y = gen_y()
    if np.random.rand() * f_ratio * pdf_y(y) < pdf_x(y):
        return y
    else:
        return sample_rejection_(gen_y, pdf_x, pdf_y, f_ratio)


def sample_rejection(gen_y, pdf_x, pdf_y, f_ratio, i_size):
    return np.array(
        [sample_rejection_(gen_y, pdf_x, pdf_y, f_ratio) for i in range(i_size)]
    )


ar = sample_rejection(np.random.rand, lambda x: x + 2 * x ** 3, lambda x: 1, 3, 100000)
print(ar.mean())
print(ar.var())
plt.xlabel("$X$")
plt.ylabel("Density")
plt.hist(ar, 32, density=True)
plt.savefig("c.pdf")
