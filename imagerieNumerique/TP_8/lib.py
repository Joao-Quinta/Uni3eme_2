import numpy as np
import matplotlib.pyplot as plt
import math


def fTildaExo1(T):
    y = np.zeros(T.shape)
    for i in range(0, len(T)):
        t = abs(T[i]) % 4
        r = -1
        if t <= 1 or t > 3:
            r = 1
        y[i] = r
    return y


def computeAk(k):
    r = 0
    if k % 2 != 0:
        r = ((-1) ** ((k - 1) / 2)) * (4 / (k * np.pi))
    return r


def fNemeApprox(N, t, w0):
    rep = 0.5 * computeAk(0)
    for i in range(1, N + 1):
        x = i * w0 * t
        rep = rep + (computeAk(i) * np.cos(x))
    return rep


def hExo2(t):
    y = np.zeros(t.shape)
    for i in range(0, len(t)):
        if abs(t[i]) <= 1:
            r = 1 - abs(t[i])
            y[i] = r
    return y


def periodicExtention(x, y, T):
    arr = []
    for val in T:
        arrVal = np.zeros(x.shape)
        mid = np.where(x == 0)[0][0]
        left = y[mid:np.where(x == val / 2)[0][0] + 1]
        right = y[np.where(x == -val / 2)[0][0]:mid]
        periodicExt = np.concatenate((left, right))
        arrVal[mid] = periodicExt[0]
        j = 1
        for i in range(1, len(x) - mid):
            arrVal[mid + i] = periodicExt[j % len(periodicExt)]
            arrVal[mid - i] = periodicExt[j % len(periodicExt)]
            j = j + 1
        arr.append(arrVal)
    return arr


def exo3G(t, a):
    return np.exp(-1 * a * (t ** 2))


def exo3GChapeau(w, a):
    return np.sqrt(np.pi / a) * np.exp((-1) * ((w ** 2) / 4 * a))


def exo3HChapeau(w):
    return exo3GChapeau(w, 1) * np.exp(1*w*1j)


# pour G alpha = 1: real = abs, imag = angle
def represent_complex_signal(x, y):
    plt.plot(x, np.real(y), label='real')
    plt.plot(x, np.imag(y), label='imag')
    plt.plot(x, np.abs(y), label='abs')
    plt.plot(x, np.angle(y), label='angle')
    plt.legend()
    plt.show()
