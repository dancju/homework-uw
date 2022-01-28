#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
y = [
    0.009952031007473255,
    0.009952031007473255,
    0.030011512284725324,
    0.030011512284725324,
    0.040004618622858840,
    0.040004618622858840,
    0.050000655190250876,
    0.050000655190250876,
    0.050000655190250876,
    0.050000655190250876,
    0.055007378975362500,
    0.055007378975362500,
    0.055007378975362500,
    0.055007378975362500,
    0.055007378975362500,
    0.055007378975362500,
    0.055007378975362500,
    0.055007378975362500,
    0.055007378975362500,
    0.055007378975362500,
]

cs = CubicSpline(x, y)
xs = np.arange(0.5, 10, 0.1)

plt.ylabel("Yield")
plt.xlabel("Maturity (years)")
plt.scatter(x, y, label="bootstrapped")
plt.plot(xs, cs(xs), label="cubic spline")
plt.legend()
plt.savefig("main.pdf")
