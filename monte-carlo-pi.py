# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt


def main():
    N = 100000
    x = np.random.uniform(-1.0, 1.0, N)
    y = np.random.uniform(-1.0, 1.0, N)

    inside_sphere = []

    for i in range(N):
        if (x[i]**2 + y[i]**2) < 1.0:
            inside_sphere.append(True)
        else:
            inside_sphere.append(False)

    print(2.0**2 * float(inside_sphere.count(True)) / float(N))  # => 3.13632

    plt.scatter(
        x,
        y,
        c=inside_sphere,
        s=5,
        edgecolor='None'
    )
    plt.xlim(-1.0, 1.0)
    plt.ylim(-1.0, 1.0)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == '__main__':
    main()
