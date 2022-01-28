#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

f_sigma = 0.2
f_k = 1
x = np.linspace(0.5, 1.5, 1024, False)


def call_price(f_t: float, f_s: np.ndarray) -> np.ndarray:
    f0 = 1 / f_sigma / np.sqrt(f_t) * np.log(f_s / f_k)
    f1 = f_sigma * np.sqrt(f_t) / 2
    return f_s * scipy.stats.norm.cdf(f0 + f1) - f_k * scipy.stats.norm.cdf(f0 - f1)


plt.figure()
plt.plot(x, call_price(1, x), label="$t=0$")
plt.plot(x, call_price(0.5, x), label="$t=T/2$")
plt.plot(x, call_price(0.25, x), label="$t=3T/4$")
plt.plot(x, np.maximum(0, x - f_k), label="payoff")
plt.legend()
plt.xlabel("Stock Price")
plt.ylabel("Call Price")
plt.savefig("call.pdf")


def delta(f_t: float, f_s: np.ndarray) -> np.ndarray:
    f0 = 1 / f_sigma / np.sqrt(f_t) * np.log(f_s / f_k)
    f1 = f_sigma * np.sqrt(f_t) / 2
    return scipy.stats.norm.cdf(f0 + f1)


plt.figure()
plt.plot(x, delta(1, x), label="$t=0$")
plt.plot(x, delta(0.5, x), label="$t=T/2$")
plt.plot(x, delta(0.25, x), label="$t=3T/4$")
plt.legend()
plt.xlabel("Stock Price")
plt.ylabel("Delta")
plt.savefig("delta.pdf")


def gamma(f_t: float, f_s: np.ndarray) -> np.ndarray:
    f0 = 1 / f_sigma / np.sqrt(f_t) * np.log(f_s / f_k)
    f1 = f_sigma * np.sqrt(f_t) / 2
    return scipy.stats.norm.pdf(f0 + f1) / f_sigma / np.sqrt(f_t) / f_s


plt.figure()
plt.plot(x, gamma(1, x), label="$t=0$")
plt.plot(x, gamma(0.5, x), label="$t=T/2$")
plt.plot(x, gamma(0.25, x), label="$t=3T/4$")
plt.legend()
plt.xlabel("Stock Price")
plt.ylabel("Gamma")
plt.savefig("gamma.pdf")


def vega(f_t: float, f_s: np.ndarray) -> np.ndarray:
    f0 = 1 / f_sigma / np.sqrt(f_t) * np.log(f_s / f_k)
    f1 = f_sigma * np.sqrt(f_t) / 2
    return np.sqrt(f_t) * scipy.stats.norm.pdf(f0 + f1) * f_s


plt.figure()
plt.plot(x, vega(1, x), label="$t=0$")
plt.plot(x, vega(0.5, x), label="$t=T/2$")
plt.plot(x, vega(0.25, x), label="$t=3T/4$")
plt.legend()
plt.xlabel("Stock Price")
plt.ylabel("Vega")
plt.savefig("vega.pdf")
