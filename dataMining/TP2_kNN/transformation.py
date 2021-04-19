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
    ax.arrow(xmin, 0, xmax - xmin, 0., fc='k', ec='k', lw=0.5,
             head_width=0.08, head_length=0.08, overhang=0.1,
             length_includes_head=True, clip_on=False)
    ax.text(xmax + 0.1, 0, "x1", size=10, ha='center', va='center')

    ax.arrow(0, ymin, 0., ymax - ymin, fc='k', ec='k', lw=0.1,
             head_width=0.08, head_length=0.08, overhang=0.01,
             length_includes_head=True, clip_on=False)
    ax.text(0, ymax + 0.1, "x2", size=10, ha='center', va='center')

    return fig, ax


def draw(ax, X, n, color='green'):
    # simply plot the points
    ax.plot(X[0, :], X[1, :], color=color)


def unit_circle_points(n):
    X = np.zeros((2, 2 * n))
    # the x coordinates in the unit circle go from -1 to 1, and then come back from 1 to -1
    X[0, :] = np.concatenate((np.linspace(-1.0, 1.0, n), np.linspace(1.0, -1.0, n)), axis=0)
    # we use the formula to compute y, since we have x we can easily do it
    X[1, :] = np.sqrt(1 - X[0, :] ** 2)
    # to have the simitry in the x axis we multiply the second half of y coordinates by -1
    X[1, n:] = X[1, n:] * -1
    return X


def apply_transformation_AX(X, A):
    AX = A.dot(X)
    # just a dot multiplication
    return AX


def apply_transformation_Z(X, A):
    Z = np.linalg.inv(A).dot(X)
    # we get the inv of A, and apply dot multiplication to X
    return Z
