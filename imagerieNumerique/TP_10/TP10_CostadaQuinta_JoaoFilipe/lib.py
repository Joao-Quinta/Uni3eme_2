import numpy as np
import matplotlib.pyplot as plt
import math


def computeWMU(M, U):
    return np.exp((np.pi * 2 * U / M) * -1j)


def get_F_DFT(W, f):
    return np.dot(W, f)


def simplePlotY(y, label):
    plt.plot(y)
    plt.title(label)
    plt.show()


def simplePlotXY(x, y, label):
    plt.plot(x, y)
    plt.title(label)
    plt.show()


def affichage_rows_cols(rows, cols, x, y, labels):
    rows = rows
    cols = cols
    axes = []
    fig = plt.figure()
    for i in range(rows * cols):
        axes.append(fig.add_subplot(rows, cols, i + 1))
        if (x[i]) is None:
            plt.plot(y[i])
        else:
            plt.plot(x[i], y[i])
        plt.title(labels[i])
    fig.tight_layout()
    plt.show()


def get_magnitude(F):
    return np.abs(F)


def get_phase(F):
    return np.angle(F)
