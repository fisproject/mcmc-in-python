#!/usr/bin/env python
# coding: utf-8

import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

def main():
    N = 100000

    x = np.random.uniform(-1.0, 1.0, N)
    y = np.random.uniform(-1.0, 1.0, N)
    z = np.random.uniform(-1.0, 1.0, N)

    l = []

    for i in xrange(N):
        if (x[i]**2 + y[i]**2 + z[i]**2) < 1.0:
            l.append(True)
        else:
            l.append(False)

    ax = Axes3D(plt.figure())
    ax.scatter3D(x, y, z, s=3, c=l, edgecolor='None')
    plt.xlim(-1.0, 1.0)
    plt.ylim(-1.0, 1.0)
    plt.show()

    print('Theoretical Value:', math.pi**(3.0/2.0) / math.gamma(3.0/2.0+1.0))
    # => Theoretical Value: 4.18879020479
    print('Monte Carlo:', 2.0**3 * float(l.count(True)) / float(N))
    # => Monte Carlo: 4.19312

if __name__ == '__main__':
    main()
