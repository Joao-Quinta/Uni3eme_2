import numpy as np


def train_nb(X, y):
    """
    Train the Naive Bayes classifier. For NB this is just
    computing the necessary probabilities to perform classification
    1. The probability P(ci) for every class -> prior (the prior comes from the distribution of labels)
    2. The mean and std -> mean, std (The mean and variance are applied to each feature in the input data X)

    Inputs:
    - X: A numpy array of shape (num_train, D) containing the training data
    consisting of num_train samples each of dimension D.
    - y: A numpy array of shape (N,) containing the training labels, where
        y[i] is the label for X[i].

    Outputs:
    - prior : list with length equal to the number of classes
    - mean : A numpy array of shape (num_classes, num_features)
    - std  : A numpy array of shape (num_classes, num_features)

    **** train() should be run with X as training data
    """
    # use list comprehension

    # Separate training points by class
    unique_y = np.unique(y)  # returns a list of all different values in y -> all possible classes
    points_by_class = [[x for x, t in zip(X, y) if t == c] for c in unique_y]

    total = X.shape[0]  # total number of data points
    prior = [len(x) / total for x in points_by_class]
    #
    # mean = [X[y == c].mean(axis=0) for c in unique_y]
    # std = [X[y == c].var(axis=0) for c in unique_y]

    return prior, points_by_class  # , np.array(mean), np.array(std)


# def normal_distribution(x, mean, std):
#     """
#     Compute normal distribution
#     output size: (num_input_data, num_features)
#
#     """
#     #########################################################################
#     # TODO : Compute normal distribution                                    #
#     #########################################################################
#
#     # normal =
#
#     return normal


def predict(X, prior, mean, std):
    """
    Using the dustributions from before, predict labels for test data (or train data) using this classifier.
    We predict the class of the data maximizing the likelihood or you can
     maximize the log likelihood to make it numericaly more stable.
     (This is possible since f(x)=log(x) is a monotone function)

    You have to compute:
    - Compute the conditional probabilities  P(x|c) (or log P(x|c) )
    - The posterior (if you compute the log likelihood the product  becomes sum)
    - Make the prediction

    Inputs:
    - X: A numpy array of shape (num_test, D) containing test data consisting
        of num_test samples each of dimension D.
    - prior, mean, std: output of train() function

    Returns:
    - y_pred : A numpy array of shape (num_test,) containing predicted labels for the
    test data, where y[i] is the predicted label for the test point X[i].

    *** predict() should be run with X as test data, based on mean and variance and prior from the training data
        (to compute the training accuracy run with X as train data)

    """
    # use list comprehension

    #################################################################################
    #        # Compute the conditional probabilities  P(x|c)                        #
    #             # There are three loops in the code.                              #
    #             # 1. through each sample.                                         #
    #             # 2. through each class.                                          #
    #             # 3. through each attribute and apply the Normal/ logNormal distribution. #
    #        # Compute the posterior                                                #
    #                                                                               #
    #################################################################################

    #########################################################################
    #                           TODO
    #             compute the posterior and predict                         #
    # - hint for prediction: class having the biggest probability[argmax()] #
    #########################################################################
    y_pred = []
    # pre = la proba prior pour chaque classe
    for x in X:
        eachClass = []
        for c in range(0, len(prior)):
            eachClass.append(prior[c] * np.prod(
                [np.exp(-1 * np.square((x[attrN] - mean[c][attrN]) / (2 * std[c][attrN]))) for attrN in
                 range(0, len(x))]))
        y_pred.append(np.argmax(eachClass))

    return np.array(y_pred)
