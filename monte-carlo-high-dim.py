# coding: utf-8

import math

import numpy as np
import matplotlib

matplotlib.use("TkAgg")  # for macOS
import matplotlib.pyplot as plt


def V(n: int) -> float:
    return math.pi ** (n / 2.0) / math.gamma(n / 2.0 + 1.0)


def count_point(N: int, n: int) -> int:
    x = []
    count = 0

    for _ in range(n):
        x.append(np.random.uniform(-1.0, 1.0, N))

    for i in range(N):
        r = 0.0
        for j in range(n):
            r += x[j][i] ** 2.0
        if r < 1.0:
            count += 1

    return count


def main():
    tv, mc = [], []
    N = 100000

    for n in range(1, 25):
        c = count_point(N, n)
        tv.append(V(n))
        mc.append(2.0 ** n * float(c) / float(N))

        print(f"{n} dim(s)")
        print(f"Theoretical Value: {tv[-1]}")
        print(f"Monte Carlo: {2.0**n * float(c) / float(N)}")

    x = np.arange(1, 25, 1)
    plt.plot(x, tv)
    plt.plot(x, mc)
    plt.xlabel("dim")
    plt.ylabel("V(r=1)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
