import numpy as np
import matplotlib.pyplot as plt
import math


def returnLinspace(l, r, n):
    return np.linspace(l, r, n)


def computeSha(t, T):
    y = []
    for i in t:
        yi = 0
        if (i * T).is_integer():
            yi = 1
        y.append(yi)
    return y


def plotScatter(functions):
    for func in functions:
        plt.scatter(func[0], func[1], c=func[2])
    plt.show()


def even(s):
    return


def odd(s):
    return
