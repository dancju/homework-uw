#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def sample_rejection_(gen_y, pdf_x, pdf_y, f_ratio):
    global i_iter
    i_iter += 1
    y = gen_y()
    if np.random.rand() * f_ratio * pdf_y(y) < pdf_x(y):
        return y
    else:
        return sample_rejection_(gen_y, pdf_x, pdf_y, f_ratio)


def sample_rejection(gen_y, pdf_x, pdf_y, f_ratio, i_size):
    return np.array(
        [sample_rejection_(gen_y, pdf_x, pdf_y, f_ratio) for i in range(i_size)]
    )


def gen_y():
    u = np.random.rand()
    return np.log(2 * u) if u < 1 / 2 else -np.log(2 - 2 * u)


def pdf_x(x):
    return np.exp(-(x ** 2) / 2) / np.sqrt(2 * np.pi)


def pdf_y(x):
    return np.exp(-np.abs(x)) / 2


f_ratio = (2 * np.e / np.pi) ** 0.5

ar_x = np.arange(-4, 4.1, 0.1)
plt.plot(ar_x, pdf_y(ar_x) * f_ratio, label="$g(x)a$")
plt.plot(ar_x, pdf_x(ar_x), label="$f(x)$")

i_size = 10000
i_iter = 0
ar_samples = sample_rejection(gen_y, pdf_x, pdf_y, f_ratio, i_size)
plt.hist(ar_samples, 32, density=True, label="samples")
print(ar_samples.mean())
print(ar_samples.var())
print(i_iter / i_size * 2)

plt.xlabel("$x$")
plt.ylabel("Density")
plt.legend()
plt.savefig("main.pdf")
