#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

def range_ex(start, end, step):
    while start + step < end:
        yield start
        start += step

# P(x) : Target distribution
def P(x1, x2, b):
    return np.exp(-1/2 * (x1**2 - 2*b*x1*x2 + x2**2))

xs = []
ys = []
zs = []
b = 0.5

for i in range_ex(-3, 3, 0.1):
    for j in range_ex(-3, 3, 0.1):
        xs.append(i)
        ys.append(j)
        zs.append(P(i, j, b))

ax = Axes3D(plt.figure())
ax.scatter3D(xs, ys, zs, s=3, edgecolor='None')
plt.show()

def gibbs(N, thin):
    s = []
    x1 = 0.0
    x2 = 0.0
    for i in range(N):
        for j in range(thin):
            x1 = np.random.normal(b * x2, 1) # P(x1|x2)
            x2 = np.random.normal(b * x1, 1) # P(x2|x1)
        s.append((x1,x2))
    return np.array(s)

def main():
    N = 3000
    thin = 500
    burn_in = 0.2

    sample = gibbs(N, thin)

    plt.scatter(
        sample[int(N * burn_in):,0],
        sample[int(N * burn_in):,1],
        s=3,
        edgecolor='None'
    )
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

    print('x1:', np.mean(sample[int(N * burn_in):,0]), np.var(sample[int(N * burn_in):,0]))
    # => x1: 0.00741907569473 1.32326519155
    print('x2:', np.mean(sample[int(N * burn_in):,1]), np.var(sample[int(N * burn_in):,1]))
    # => x2: -0.00980409857562 1.33662629729

if __name__ == '__main__':
    main()
