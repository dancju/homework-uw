#!/usr/bin/env python3
import matplotlib.pyplot as plt

plt.axis("equal")
plt.xlabel("$U_1$")
plt.ylabel("$U_2$")
plt.fill([0, 1, 1, 0], [0, 0, 1, 1], alpha=0.5, label="event space")
plt.fill([0, 0.5, 0.5, 1], [0.5, 1, 0, 0.5], alpha=0.5, label="triangle")
plt.legend()
plt.savefig("main.pdf")
