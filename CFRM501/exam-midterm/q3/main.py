#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


def plot_function(x_lo, x_hi, fun, label):
    x = np.linspace(x_lo, x_hi, 1024)
    y = fun(x)
    plt.plot(x, y, label=label)


plot_function(1, 4.2, lambda x: (x ** 2 - 1) ** 0.5 + 2, "efficient frontier")
plot_function(0, 3.6, lambda x: 2 ** 0.5 * x + 1, "capital allocation line")
plot_function(0, 2.9, lambda x: 0.5 * x ** 2 + 2, "indifference curve")
plt.scatter(2 ** 0.5, 3, label="tangency portfolio")
plt.scatter(0, 1, label="risk-free portfolio")
plt.scatter(0, 2)
plt.text(0, 2, r"$\frac{r_f+\mu_T}{2}$")
plt.legend()
plt.ylim(top=6)
plt.gca().set_xticks([0, 1, 2, 3, 4])
plt.gca().set_xticklabels([0, None, None, None, None])
plt.gca().set_yticklabels([])
plt.xlabel("Standard Deviation")
plt.ylabel("Mean")
plt.savefig("main.pdf")
