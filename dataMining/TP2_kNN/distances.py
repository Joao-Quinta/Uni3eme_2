import numpy as np
from scipy.spatial import distance


def compute_euclidean_dist_two_loops(x_train, x_test):
    """
    Compute the distance between each test point in x_test and each training point
    in x_train using a nested loop over both the training data and the 
    test data.

    Inputs:
    - x_train: A numpy array of shape (num_train, D) containing test data.
    - x_test: A numpy array of shape (num_test, D) containing test data.

    Returns:
    - dists: A numpy array of shape (num_test, num_train) where dists[i, j]
      is the Euclidean distance between the ith test point and the jth training
      point.
    """
    num_test = x_test.shape[0]
    num_train = x_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in range(num_test):
        for j in range(num_train):
            #####################################################################
            # TODO:                                                             #
            # Compute the l2 distance between the ith test point and the jth    #
            # training point, and store the result in dists[i, j]. You should   #
            # not use a loop over dimension.                                    #
            #####################################################################
            # Your code

            '''
            sub = np.subtract(x_test[i], x_train[j])
            dotMul = np.dot(np.transpose(sub), sub)
            root = np.sqrt(dotMul)
            '''

            dists[i][j] = distance.euclidean(x_test[i], x_train[j])

        #####################################################################
        #                       END OF YOUR CODE                            #
        #####################################################################
    return dists


def compute_euclidean_dist_one_loop(x_train, x_test):
    """
    Compute the distance between each test point in x_test and each training point
    in x_train using a single loop over the test data.

    Input / Output: Same as compute_euclidean_dist_two_loops
    """
    num_test = x_test.shape[0]
    num_train = x_train.shape[0]
    dists = np.zeros((num_test, num_train))
    for i in range(num_test):
        #######################################################################
        # TODO:                                                               #
        # Compute the l2 distance between the ith test point and all training #
        # points, and store the result in dists[i, :].                        #
        #######################################################################
        # Your code
        pass

    #######################################################################
    #                         END OF YOUR CODE                            #
    #######################################################################
    return dists


def compute_euclidean_dist_no_loops(x_train, x_test):
    """
    Compute the distance between each test point in x_test and each training point
    in x_train using no explicit loops.

    Input / Output: Same as compute_euclidean_dist_two_loops
    """
    num_test = x_test.shape[0]
    num_train = x_train.shape[0]
    dists = np.zeros((num_test, num_train))
    #########################################################################
    # TODO:                                                                 #
    # Compute the l2 distance between all test points and all training      #
    # points without using any explicit loops, and store the result in      #
    # dists.                                                                #
    #                                                                       #
    # You should implement this function using only basic array operations; #
    # in particular you should not use functions from scipy.                #
    #                                                                       #
    # HINT: Try to formulate the l2 distance using matrix multiplication    #
    #       and two broadcast sums.                                         #
    #########################################################################
    # Your code

    #########################################################################
    #                         END OF YOUR CODE                              #
    #########################################################################
    return dists


def compute_mahalanobis_dist(x_train, x_test, sigma):
    """
    Compute the Mahalanobis distance between each test point in x_test and each training point
    in x_train (please feel free to choose the implementation).

    Inputs:
    - x_train: A numpy array of shape (num_train, D) containing test data.
    - x_test: A numpy array of shape (num_test, D) containing test data.
    - sigma: A numpy array of shape (D,D) containing a covariance matrix.

    Returns:
    - dists: A numpy array of shape (num_test, num_train) where dists[i, j]
      is the Mahalanobis distance between the ith test point and the jth training
      point.
    """
    num_test = x_test.shape[0]
    num_train = x_train.shape[0]
    dists = np.zeros((num_test, num_train))
    #########################################################################
    # TODO:                                                                 #
    # Compute the Mahalanobis distance between all test points and all      #
    # training points (please feel free to choose the implementation), and store the       #
    # result in dists.                                                      #
    #                                                                       #
    #########################################################################
    # Your code

    #########################################################################
    #                         END OF YOUR CODE                              #
    #########################################################################
    return dists


def compute_manhattan_dist(x_train, x_test):
    """
    Compute the Manhattan distance between each test point in x_test and each training point
    in x_train (please feel free to choose the implementation).

    Inputs:
    - x_train: A numpy array of shape (num_train, D) containing train data.
    - x_test: A numpy array of shape (num_test, D) containing test data.

    Returns:
    - dists: A numpy array of shape (num_test, num_train) where dists[i, j]
      is the Manhattan distance between the ith test point and the jth training
      point.
    """
    num_test = x_test.shape[0]
    num_train = x_train.shape[0]
    dists = np.zeros((num_test, num_train))
    #########################################################################
    # TODO:                                                                #
    # Compute the Manhattan distance between all test points and all      #
    # training points (please feel free to choose the implementation), and store the       #
    # result in dists.                                                      #
    #                                                                       #
    #########################################################################
    # Your code                    

    #########################################################################
    #                         END OF YOUR CODE                              #
    #########################################################################
    return dists


def define_covariance(X_train, method):
    """
    Define a covariance  matrix using 3 difference approaches: 
    """
    d = X_train.shape[1]

    #########################################################################
    # TODO:                                                                 #
    # Computre Σ as a diagonal matrix that has at its diagonal the average  #
    # variance of  the different features,       
    #  i.e. all diagonal entries Σ_ii will be the same                      #
    #                                                                       #
    #########################################################################
    # Your code
    if method == 'diag_average_cov':
        cov = np.zeros((d, d))
        return cov


    #########################################################################
    #                         END OF YOUR CODE                              #
    #########################################################################

    #########################################################################
    # TODO:                                                                 #
    # Computre  Σ as a diagonal matrix that has at its diagonal             #
    # he variance of eachfeature, i.e.σ_k     
    #                                                                       #
    #########################################################################
    # Your code
    elif method == 'diag_cov':
        cov = np.zeros((d, d))
        return cov



    #########################################################################
    #                         END OF YOUR CODE                              #
    #########################################################################

    #########################################################################
    # TODO:                                                                 #
    # Computre Σ as the full covariance matrix between all pairs of features#
    #                                                                       #
    #########################################################################

    # Your code
    elif method == 'full_cov':
        cov = np.zeros((d, d))

        return cov


    #########################################################################
    #                         END OF YOUR CODE                              #
    #########################################################################

    else:
        raise ValueError("Uknown method identifier.")
