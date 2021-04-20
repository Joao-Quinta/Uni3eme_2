import numpy as np
import matplotlib.pyplot as plt
import math


def gaussianSignal(t, sigma):
    return np.exp(-(t ** 2) / (2 * sigma ** 2)) / np.sqrt(2 * np.pi * sigma ** 2)


def gaussianTransform(gaussianS, sigma):
    return gaussianS * (np.sqrt(2 * np.pi) / sigma)


def simplePlot(x, y):
    plt.plot(x, y)
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
