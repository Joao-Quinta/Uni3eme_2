import numpy as np


def train_nb(X, y, cont):
    unique_y = np.unique(y)  # returns a list of all different values in y -> all possible classes
    total = X.shape[0]  # total number of data points
    if cont:
        points_by_class = [[x for x, t in zip(X, y) if t == c] for c in unique_y]
        prior = [len(x) / total for x in points_by_class]
        mean = [X[y == c].mean(axis=0) for c in unique_y]
        std = [X[y == c].var(axis=0) for c in unique_y]
        return prior, np.array(mean), np.array(std)
    else:
        prior = [[unique_y[i], np.count_nonzero(y[y == unique_y[i]]) / total] for i in range(len(unique_y))]
        proba = [[[] for i in range(X.shape[1])] for j in range(len(prior))]
        for i in range(len(prior)):
            for j in range(X.shape[1]):
                val_corr = X[y == prior[i][0]][:, j]
                col_unique = np.unique(val_corr)
                [proba[i][j].append([val, (np.count_nonzero(val_corr == val)) / len(X[y == prior[i][0]])]) for val in
                 col_unique]
        return prior, proba


def normal_distribution(x, mean, std):
    return np.exp(-1 * np.square((x - mean) / (2 * std)))


def predict(X, prior, mean, std, cont):
    y_pred = []
    if cont:
        for x in X:
            eachClass = []
            for c in range(0, len(prior)):
                eachClass.append(prior[c] * np.prod([normal_distribution(x[attrN], mean[c][attrN], std[c][attrN]) for attrN in range(0, len(x))]))
            y_pred.append(np.argmax(eachClass))
        return np.array(y_pred)
    else:
        for x in X:
            eachClass = [prior[i][1] for i in range(len(prior))]
            for j in range(len(prior)):
                for attrN in range(len(x)):
                    valeurs = mean[j][attrN]
                    z = 0
                    while z < len(valeurs):
                        if valeurs[z][0] == x[attrN]:
                            eachClass[j] = eachClass[j] * valeurs[z][1]
                            z = len(valeurs)
                        z = z + 1
            y_pred.append(prior[np.argmax(eachClass)][0])
        return y_pred
