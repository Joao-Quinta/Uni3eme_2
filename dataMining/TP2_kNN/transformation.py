

import numpy as np
import matplotlib.pyplot as plt

def setup_plot(axes_size=2):
    """
    Setup the basis of the plot, i.e. put the axis in the middle with arrows.

    Inputs:
    - axes_size: The size of the axes.

    Returns:
    - fig (figure) and ax (axes) 
    """
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1, 1, 1)

    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # remove ticks
    ax.set_xticks([])
    ax.set_yticks([])
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    ax.set_aspect('equal', 'box')
    ax.axis([-axes_size, axes_size, -axes_size, axes_size])

    xmin, xmax = ax.get_xlim() 
    ymin, ymax = ax.get_ylim()

    # add arrow and axis names
    ax.arrow(xmin, 0, xmax-xmin, 0., fc='k', ec='k', lw = 0.5, 
            head_width=0.08, head_length=0.08, overhang = 0.1, 
            length_includes_head= True, clip_on = False) 
    ax.text(xmax+0.1, 0, "x1", size=10, ha='center', va='center')

    ax.arrow(0, ymin, 0., ymax-ymin, fc='k', ec='k', lw = 0.1, 
            head_width=0.08, head_length=0.08, overhang = 0.01, 
            length_includes_head= True, clip_on = False) 
    ax.text(0,  ymax+0.1, "x2", size=10, ha='center', va='center')

    return fig, ax


def draw(ax, X, n, color='green'):
    """
    Plot the set of points X, X should allow you to plot a circle.

    Inputs:
    - ax: The axes to plot.
    - X: A numpy array of shape (2, 2*n) containing the set of points (x1, x2).
    - n: The number of x1 points.
    - color: The color of the plot.

    Returns:
    - None
    """
    #########################################################################
    # TODO:                                                                 #
    # You should find a way to print a circle with the plot method of       #
    # matplotlib.                                                           #
    #                                                                       #
    # HINT: ax.plot(... , color=color)                                      #
    #                                                                       #
    #########################################################################
    # Your code



    
    #########################################################################
    #                         END OF YOUR CODE                              #
    #########################################################################


def unit_circle_points(n):
    """
    Compute the points for the unit circle, n gives you the number of elements 
    to take in the x1 axis..

    Inputs:
    - n: The number of points for x1 axis.

    Returns:
    - X: A numpy array of shape (2, 2*n) where X[0, :] is the set of points for
    the first coordinate x1 and X[1, :] is the set of points for the second 
    coordinate x2.
    """
    X = np.zeros((2, 2*n))
    #########################################################################
    # TODO:                                                                 #
    # Compute the points for the unit circle, n gives you the number of     #
    # elements to take in the x1 axis.                                      #
    #                                                                       #
    # Coding tip: you create the x variable, then y is defined from x.      #
    # This means that for each x, the corresponding y value is calculated   #
    # (and thus y has the same shape as x).  	                            #
    #
    # HINT: Think about the shape of a circle and the dimensions of X.      #
    # Why X is a 2 by 2*n array ? (don't answer this questions the goal is  #
    # to help you)                                                          #
    #########################################################################
    # Your code



    
    #########################################################################
    #                         END OF YOUR CODE                              #
    #########################################################################

    return X


def apply_transformation_AX(X, A):
    """
    Apply a linear transformation, given an orthogonal matrix A, on X.

    Inputs:
    - X: A numpy array of shape (2, 2*n) containing unit circle points.
    - A: A numpy array of shape (2, 2) containing the transformation matrix.

    Returns:
    - AX: A numpy array of shape (2, 2*n) containing the transformed set of 
    points where AX[0, :] is the set of points for the first coordinate x1 and
    AX[1, :] is the set of points for the second coordinate x2.
    """
    AX = np.zeros(X.shape)
    #########################################################################
    # TODO:                                                                 #
    # Apply a linear transformation which is given by a matrix A on X       #
    #########################################################################
    # Your code




    #########################################################################
    #                         END OF YOUR CODE                              #
    #########################################################################
    return AX


def apply_transformation_Z(X, A):
    """
    Apply a linear transformation on an unknown set of points Z such that the 
    result of the linear transformation with A gives you the unit circle.

    Inputs:
    - X: A numpy array of shape (2, 2*n) containing unit circle points.
    - A: A numpy array of shape (2, 2) containing the transformation matrix.

    Returns:
    - Z: A numpy array of shape (2, 2*n) containing the transformed set of 
    points where Z[0, :] is the set of points for the first coordinate x1 and
    Z[1, :] is the set of points for the second coordinate x2.
    """
    Z = np.zeros(X.shape)
    #########################################################################
    # TODO:                                                                 #
    # Apply a linear transformation on an unknown set of points Z such that #
    # the result of the linear transformation A with Z gives you the unit   #
    # circle.                                                               #
    # HINT:  Look up the function numpy.linalg.inv                          #
    #########################################################################
    # Your code





    #########################################################################
    #                         END OF YOUR CODE                              #
    #########################################################################
    return Z