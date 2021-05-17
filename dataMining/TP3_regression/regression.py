from __future__ import print_function, division
import numpy as np
import math


class LinearRegression_RidgeRegression():
    """Linear Regression and Ridge Regression.
    Parameters:
    -----------
    X: data
    y: target values y
    iterations: int
         number of training iterations
    lr: float
        the learning rate
    l2_reg: float
        parameter for l2 regularizer
        l2_reg = 0 ->  Linear Regression
        l2_reg != 0 ->  Ridge Regression
    analytical_sol: boolean
        True or false depending if analytical solution will be used during the training.
    """

    def __init__(self, X, y, iterations=100, lr=0.001, l2_reg=0, analytical_sol=True):
        self.analytical_sol = analytical_sol
        self.iterations = iterations
        self.lr = lr
        self.l2_reg = l2_reg
        self.X = X
        self.y = y
        self.n_features = self.X.shape[1]
        """ Initialize weights randomly [-1/d, 1/d] """
        limit = 1 / np.sqrt(self.n_features)
        self.w = np.random.uniform(-limit, limit, (self.n_features,)).reshape(X.shape[1], 1)

    def fit(self):
        """Function that returns the weights of Linear Regression and
        Ridge Regression(Linear Regression with l2 regularizer)
        for both analytical solution and applying optimization method.
        If analytical_sol == 0 returns the weights computed using the analytical solution
        otherwise returns the weights computed using optimization.
        """
        # If analytical_sol => Least squares
        if self.analytical_sol:
            ######################################################################
            # To do:                                                             #
            # for both Linear and Ridge Regression (Linear with l2 regularizer)  #
            # Calculate weights by least squares (analytical solution)           #
            ######################################################################
            self.w = np.dot(np.dot(np.linalg.inv(np.add(np.dot(self.X.transpose(), self.X), np.identity(self.X.shape[1]) * self.l2_reg)), self.X.transpose()), self.y)
            return self.w
        else:
            ######################################################################
            # To do:                                                             #
            # for both Linear and Ridge Regression (Linear with l2 regularizer)  #
            # Calculate weights using gradient descent (GD)                      #
            ######################################################################
            if self.l2_reg == 0:
                for i in range(self.iterations):
                    self.w = np.subtract(self.w, (self.lr * (np.dot(-2*self.X.transpose(), np.subtract(self.y, np.dot(self.X, self.w))))))
            else:
                for i in range(self.iterations):
                    self.w = np.subtract(np.subtract(self.w, (self.lr * (np.dot(-2*self.X.transpose(), np.subtract(self.y, np.dot(self.X, self.w)))))), 2 * self.l2_reg * self.w)
            return self.w

    def predict(self, X):

        ######################################################################
        # To do:                                                             #
        # make prediction                                                    #
        ######################################################################
        return np.dot(X, self.w)
