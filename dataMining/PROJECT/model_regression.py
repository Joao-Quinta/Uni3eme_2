from __future__ import print_function, division
import numpy as np
from utils import smile_to_hot
import math


class LinearRegression_RidgeRegression():

    def __init__(self, X, y, largest, alphabet):
        self.X = X
        self.y_0 = y[:, 0].reshape(y.shape[0], 1)
        self.y_1 = y[:, 1].reshape(y.shape[0], 1)
        self.y_2 = y[:, 2].reshape(y.shape[0], 1)
        self.y_3 = y[:, 3].reshape(y.shape[0], 1)
        limit = 1 / np.sqrt(X.shape[0])
        self.w_0 = np.random.uniform(-limit, limit, (len(alphabet), 1)).reshape(len(alphabet), 1)
        self.w_1 = np.random.uniform(-limit, limit, (len(alphabet), 1)).reshape(len(alphabet), 1)
        self.w_2 = np.random.uniform(-limit, limit, (len(alphabet), 1)).reshape(len(alphabet), 1)
        self.w_3 = np.random.uniform(-limit, limit, (len(alphabet), 1)).reshape(len(alphabet), 1)
        self.alphabet = alphabet
        self.largest = largest
        """ Initialize weights randomly [-1/d, 1/d] """

    def build(self):
        self.X_hot = np.array([smile_to_hot(x, self.largest, self.alphabet)[1].sum(axis=0) for x in self.X])

    def fit_0(self, lr=0.001, iterations=100):
        self.lr = lr
        self.iterations = iterations

