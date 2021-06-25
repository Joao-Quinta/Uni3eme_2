import numpy as np
from statistics import mode
from utils import smile_to_hot


class model_1(object):
    """ a kNN classifier with L2 distance """

    def __init__(self):
        pass

    def train(self, X1, y1, alphabet, longest):
        self.X_train = X1
        self.y_train = y1
        self.alphabet = alphabet
        self.longest = longest

    def predict(self):
        return self.predict_labels()

    def predict_labels(self, dists):
        num_test = dists.shape[0]
        y_pred = np.zeros(num_test)

        return y_pred
