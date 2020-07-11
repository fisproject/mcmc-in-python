# coding: utf-8

import numpy as np
import matplotlib

matplotlib.use("TkAgg")  # for macOS
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D


def P(x1: float, x2: float, b: float) -> np.float64:
    """P(x) : Target distribution"""
    return np.exp(-1 / 2 * (x1 ** 2 - 2 * b * x1 * x2 + x2 ** 2))


def gibbs(N: int, thin: int, b: float) -> np.ndarray:
    x1 = 0.0
    x2 = 0.0
    s = []
    for _ in range(N):
        for _ in range(thin):
            x1 = np.random.normal(b * x2, 1)  # P(x1|x2)
            x2 = np.random.normal(b * x1, 1)  # P(x2|x1)
        s.append((x1, x2))
    return np.array(s)


def main():
    xs = []
    ys = []
    zs = []
    b = 0.5

    for i in np.arange(-3, 3, 0.1):
        for j in np.arange(-3, 3, 0.1):
            xs.append(i)
            ys.append(j)
            zs.append(P(i, j, b))

    ax = Axes3D(plt.figure())
    ax.scatter3D(xs, ys, zs, s=3, edgecolor="None")
    plt.show()

    # gibbs sampling
    N = 3000
    burn_in = 0.2

    sample = gibbs(N, thin=500, b=b)

    plt.scatter(
        sample[int(N * burn_in) :, 0],
        sample[int(N * burn_in) :, 1],
        s=3,
        edgecolor="None",
    )
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()

    print(
        f"x1: {np.mean(sample[int(N * burn_in):, 0])}, {np.var(sample[int(N * burn_in):, 0])}"
    )
    # => x1: 0.00741907569473 1.32326519155
    print(
        f"x2: {np.mean(sample[int(N * burn_in):, 1])}, {np.var(sample[int(N * burn_in):, 1])}"
    )
    # => x2: -0.00980409857562 1.33662629729


if __name__ == "__main__":
    main()
