#!/usr/bin/env python3
import matplotlib.pyplot as plt

plt.plot([0, 600], [1200, 0])
plt.plot([0, 1100], [1100, 0])
plt.plot([0, 1100], [400, 400])
plt.plot([700, 700], [0, 1200])
plt.fill([0, 600, 400, 0], [0, 0, 400, 400], alpha=0.5)
plt.savefig("main.pdf")
