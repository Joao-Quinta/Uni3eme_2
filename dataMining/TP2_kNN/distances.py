import numpy as np
from scipy.spatial import distance


def compute_euclidean_dist_two_loops(x_train, x_test):
    num_test = x_test.shape[0]
    num_train = x_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in range(num_test):
        for j in range(num_train):
            dists[i][j] = distance.euclidean(x_test[i], x_train[j])
            # I use the module spicy.spatial to compute the euclidean distance
    return dists


def compute_euclidean_dist_one_loop(x_train, x_test):
    num_test = x_test.shape[0]
    num_train = x_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in range(num_test):
        dists[i, :] = np.apply_along_axis(distance.euclidean, 1, x_train, x_test[i])
        # I use the module spicy.spatial to compute the euclidean distance apply_along_axis apples a function to
        # every collum/line of x_train and other arguments if specified (here x_test[i)
    return dists


def compute_euclidean_dist_no_loops(x_train, x_test):
    # here we have to compute (a-b)^2 -> but this will result in a memory error, it was asking for 57 Gb of memory
    # we can developpe the equation and get -> a^2 -2ab + b^2, this is made of smaller matrices, and so easier on the
    # memory requirements

    # a^2
    x_testSumSquare = np.sum(np.square(x_test), axis=1)
    # b^2
    x_trainSumSquare = np.sum(np.square(x_train), axis=1)
    # ab
    mul = np.dot(x_test, x_train.T)

    # we have now computed all 3 parts separately

    # to have the good dimensaions we do [:, np.newaxis], and now we can add and substract
    dists = np.sqrt(x_testSumSquare[:, np.newaxis] + x_trainSumSquare - 2 * mul)
    return dists


def compute_mahalanobis_dist(x_train, x_test, sigma):
    num_test = x_test.shape[0]
    num_train = x_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in range(num_test):
        for j in range(num_train):
            dists[i][j] = distance.mahalanobis(x_test[i], x_train[j], np.linalg.inv(sigma))
            # I use the module spicy.spatial to compute the mahalanobis dist
    return dists


def compute_manhattan_dist(x_train, x_test):
    num_test = x_test.shape[0]
    num_train = x_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in range(num_test):
        for j in range(num_train):
            dists[i][j] = distance.cityblock(x_test[i], x_train[j])
            # I use the module spicy.spatial to compute the manhattan dist
    return dists


def define_covariance(X_train, method):
    d = X_train.shape[1]
    if method == 'diag_average_cov':
        # average var on all X_train together -> in all diag
        return np.diag(np.array([np.var(X_train) for i in range(d)]))
    elif method == 'diag_cov':
        # each value on the diag is the var for its corresponding feature
        return np.diag(np.array([np.var(X_train[i]) for i in range(d)]))
    elif method == 'full_cov':
        # each value on the diag is the covariance for its corresponding feature
        return np.diag(np.array([np.cov(X_train[i]) for i in range(d)]))
    else:
        raise ValueError("Unknown method identifier.")
