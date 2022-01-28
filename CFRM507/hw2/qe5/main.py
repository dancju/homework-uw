#!/usr/bin/env python3
import matplotlib.pyplot as plt

plt.axis("equal")
plt.axhline(0)
plt.axvline(0)
plt.plot([0, 600], [100, 25], color="C0")
plt.plot([0, 600], [180, 0], color="C0")
plt.plot([0, 600], [5.75, 155.75], color="C0")
plt.fill(
    [0, 600, 457.143, 754 / 3, 0], [0, 0, 42.847, 823 / 12, 5.75], alpha=0.5, color="C1"
)
plt.gca().add_patch(plt.Circle((253.42, 34.0288), 34.0288, facecolor="C2"))
plt.plot([253.42], [34.0288], marker="x")
plt.savefig("main.pdf")
