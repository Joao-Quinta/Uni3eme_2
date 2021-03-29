import numpy as np


def train_nb(X, y, cont):
    unique_y = np.unique(y)  # returns a list of all different values in y -> all possible classes
    total = X.shape[0]  # total number of data points
    if cont:
        # continuous case
        points_by_class = [[x for x, t in zip(X, y) if t == c] for c in unique_y]
        prior = [len(x) / total for x in points_by_class]  # the prior probability, just |c|/|data|
        mean = [X[y == c].mean(axis=0) for c in unique_y]
        std = [X[y == c].var(axis=0) for c in unique_y]
        # both mean and variation are easily computed with the usage of np functions
        return prior, np.array(mean), np.array(std)
    else:
        # discrete case
        prior = [[unique_y[i], np.count_nonzero(y[y == unique_y[i]]) / total] for i in range(len(unique_y))]
        # [['mort', #prior of mort], ['surv', #prior of surv]] is what we get from this line
        proba = [[[] for i in range(X.shape[1])] for j in range(len(prior))]
        # proba will be : [ [[], [], []], [[], [], []]], it has |c| subarrays,
        # here 2, one for mort and one for surv, and in each sub array the prob for each attribute knowing the class
        # it is represented by another sub array, containing the prob for each possible case in this attribute
        # the array representing each attribute : [['enf', #p(enf|c)], ['adu', #p(adu|c)]] -> sum(#p(attr|c)) = 1
        for i in range(len(prior)):
            for j in range(X.shape[1]):
                val_corr = X[y == prior[i][0]][:, j]
                col_unique = np.unique(val_corr)
                [proba[i][j].append([val, (np.count_nonzero(val_corr == val)) / len(X[y == prior[i][0]])]) for val in
                 col_unique]
        return prior, proba


def normal_distribution(x, mean, std):
    # formula seen in class
    return np.exp(-1 * np.square((x - mean) / (2 * std)))


def predict(X, prior, mean, std, cont):
    y_pred = []
    if cont:
        # continuous case
        for x in X:  # for every point in X
            eachClass = []
            for c in range(0, len(prior)):  # for each possible class, we compute predict, and then pick max()
                # we simply apply the formula by calling normal_distribution function
                eachClass.append(prior[c] * np.prod(
                    [normal_distribution(x[attrN], mean[c][attrN], std[c][attrN]) for attrN in range(0, len(x))]))
                # and then eachClass stores the result for each possible class
            y_pred.append(np.argmax(eachClass))  # we then keep the one with max value from eachClass
        return np.array(y_pred)
    else:
        # discrete case
        for x in X:  # for every point in X
            eachClass = [prior[i][1] for i in range(len(prior))]
            for j in range(len(prior)):
                for attrN in range(len(x)):  # we compute p(x1|c)*....*p(xn|c) _ (x with n dimensions)
                    valeurs = mean[j][attrN]
                    z = 0
                    while z < len(valeurs):
                        if valeurs[z][0] == x[attrN]:  # this is to be sure  I have the right value
                            eachClass[j] = eachClass[j] * valeurs[z][1]
                            z = len(valeurs)
                        z = z + 1
            y_pred.append(prior[np.argmax(eachClass)][0])
        return y_pred
