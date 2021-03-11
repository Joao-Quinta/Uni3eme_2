import numpy as np
import matplotlib.pyplot as plt
import math


def returnLinspace(l, r, n):
    return np.linspace(l, r, n)


def computeSha(t, T):
    y = []
    for i in t:
        yi = 0
        if (i / T).is_integer():
            yi = 1
        y.append(yi)
    return y


def plotScatter(functions, titre):
    for func in functions:
        plt.scatter(func[0], func[1], c=func[2])
    plt.title(titre)
    plt.show()


def plotScatter1(plot, scatter, titre):
    plt.plot(plot[0], plot[1], c=plot[2])
    plt.scatter(scatter[0], scatter[1], c=scatter[2])
    plt.title(titre)
    plt.show()


def even(s):
    even = s.copy()
    for i in range(0, len(s)):
        even[i] = (s[i] + s[len(s[0:i + 1]) * -1]) / 2
    return even


def odd(s):
    odd = s.copy()
    for i in range(0, len(s)):
        odd[i] = (s[i] - s[len(s[0:i + 1]) * -1]) / 2
    return odd


def complexMatrix():
    x = np.linspace(-2, 2, 101)
    y = np.linspace(2, -2, 101)
    xx, yy = np.meshgrid(x, y, sparse=True)
    return xx + yy * 1j


def z_3_1(z):
    return (z ** 3) - 1


def absNp(m):
    return np.abs(m)


def logScale(m):
    return np.log(1 + m)


def npPhase(m):
    return np.angle(m)
