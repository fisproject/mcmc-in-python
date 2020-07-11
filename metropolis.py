# coding: utf-8

import copy
from typing import Tuple

import numpy as np
import matplotlib

matplotlib.use("TkAgg")  # for macOS
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


def P(x1: float, x2: float, b: float) -> np.float64:
    """P(x) : Target distribution"""
    return np.exp(-0.5 * (x1 ** 2 - 2 * b * x1 * x2 + x2 ** 2))


def Q(
    c: Tuple[float, float], mu1: float, mu2: float, sigma: float
) -> Tuple[float, float]:
    """Q(x) : Proposal distribution"""
    return (c[0] + np.random.normal(mu1, sigma), c[1] + np.random.normal(mu2, sigma))


def metropolis(N: int, mu1: float, mu2: float, sigma: float, b: float) -> np.ndarray:
    current = (10.0, 10.0)
    sample = []
    sample.append(current)
    accept_ratio = []

    for i in range(N):
        candidate = Q(current, mu1, mu2, sigma)

        T_prev = P(current[0], current[1], b)
        T_next = P(candidate[0], candidate[1], b)
        a = T_next / T_prev

        if a > 1 or a > np.random.uniform(0, 1):
            # Update state
            current = copy.copy(candidate)
            sample.append(current)
            accept_ratio.append(i)

    print(f"Accept ratio: {float(len(accept_ratio)) / N}")
    return np.array(sample)


def main():
    b = 0.5
    mu1 = 0
    mu2 = 0
    sigma = 1

    N = 30000
    burn_in = 0.2

    sample = metropolis(N, mu1, mu2, sigma, b)

    plt.scatter(
        sample[int(len(sample) * burn_in) :, 0],
        sample[int(len(sample) * burn_in) :, 1],
        alpha=0.3,
        s=5,
        edgecolor="None",
    )
    plt.title("MCMC (Metropolis)")
    plt.show()

    plt.figure(figsize=(15, 6))
    plt.hist(sample[int(N * burn_in) :, 0], bins=30)
    plt.xlabel("x")
    plt.hist(sample[int(N * burn_in) :, 1], bins=30)
    plt.ylabel("y")
    plt.show()

    print(
        f"x: {np.mean(sample[int(len(sample) * burn_in):, 0])}, {np.var(sample[int(len(sample) * burn_in):, 0])}"
    )
    # => x: -0.00252259614386 1.26378688755
    print(
        f"y: {np.mean(sample[int(len(sample) * burn_in):, 1])}, {np.var(sample[int(len(sample) * burn_in):, 1])}"
    )
    # => y: -0.0174372516771 1.24832585103


if __name__ == "__main__":
    main()
