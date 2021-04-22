import numpy as np
import matplotlib.pyplot as plt
import math


def gaussianSignal(t, sigma):
    return np.exp(-(t ** 2) / (2 * sigma ** 2)) / np.sqrt(2 * np.pi * sigma ** 2)


def gaussianTransform(w, sigma):
    return gaussianSignal(w, 1) * (np.sqrt(2 * np.pi) / sigma)


def getSinSignal(x):
    return np.sinc(x) ** 2


def getProductFTS(a, b):
    return a * b


def gaborSignal(x, sigma, w0):
    return np.cos(w0 * x) * gaussianSignal(x, sigma)


def gaborTransform(x, sigma, w0):
    return np.sqrt(2 * np.pi)/(2*sigma) * (gaussianSignal(x + w0, sigma) + gaussianSignal(x - w0, sigma))


def get_sha_delta(t, T):
    if (t / T).is_integer():
        yi = 1
    else:
        yi = 0
    return yi


def unsharpenSignal(x, gauss, gamma, w0):
    # impulse = getsha ?
    return (1 + gamma) * get_sha_delta(x, w0) - gamma * gauss


def unsharpenTransform(gamma, sigma, x):
    return (1 + gamma) - (np.sqrt(2 * np.pi * gamma) / sigma) * gaussianSignal(x, sigma)


def computeDiracComb(t, T):
    y = []
    for i in t:
        yi = 0
        if (i / T).is_integer():
            yi = 1
        y.append(yi)
    return y


def computeHatFunction(t):
    res = 0
    if np.abs(t) <= 1:
        res = 1 - np.abs(t)
    return res


def computeHatFunctionPeriodique(t):
    x = abs(t)
    if -1 <= x <= 1:
        return 1 - x
    else:
        return computeHatFunctionPeriodique(x - 2)


def simplePlot(x, y):
    plt.plot(x, y)
    plt.show()


def sameGraphPlot(x, y):
    for i in range(len(x)):
        plt.plot(x[i], y[i])
    plt.show()


def affichage_rows_cols(rows, cols, x, y, labels):
    rows = rows
    cols = cols
    axes = []
    fig = plt.figure()
    for i in range(rows * cols):
        axes.append(fig.add_subplot(rows, cols, i + 1))
        plt.plot(x[i], y[i])
        plt.title(labels[i])
    fig.tight_layout()
    plt.show()
