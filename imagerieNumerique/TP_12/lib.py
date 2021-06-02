import matplotlib.pyplot as plt
import math
from skimage import io
import numpy as np
import copy
import skimage.metrics as metric


def loadImag(path):
    return (io.imread(path, as_gray=True) * 255).astype("uint8")


def affichage_rows_cols_images(rows, cols, images, labels):
    rows = rows
    cols = cols
    axes = []
    fig = plt.figure()
    for i in range(rows * cols):
        axes.append(fig.add_subplot(rows, cols, i + 1))
        plt.imshow(images[i], cmap='gray')
        plt.title(labels[i])
    fig.tight_layout()
    plt.show()


def padding(images, filtre, mode):
    images_result = np.pad(images,
                           ((filtre.shape[0] - 1, filtre.shape[0] - 1), (filtre.shape[1] - 1, filtre.shape[1] - 1)),
                           mode)
    return images_result


def image_filtering(padded, filterr):
    image_copy = copy.deepcopy(padded)
    for index_row, row in enumerate(image_copy):
        if index_row + filterr.shape[0] >= len(image_copy):
            continue
        for index_pixel, pixel in enumerate(row):
            if index_pixel + filterr.shape[1] >= len(row):
                continue
            padded[index_row + (filterr.shape[0] // 2 - 1)][index_pixel + (filterr.shape[0] // 2 - 1)] = np.sum(
                np.multiply(filterr, image_copy[index_row:index_row + filterr.shape[0],
                                     index_pixel:index_pixel + filterr.shape[1]]))
    return padded


def get_cropped_image(image, offset):
    y_nonzero, x_nonzero = np.nonzero(image)
    return image[np.min(y_nonzero):np.max(y_nonzero) + offset, np.min(x_nonzero):np.max(x_nonzero) + offset]


def get_padded_image(imageLena):
    shape = imageLena.shape
    M = shape[0]
    N = shape[1]
    padded_size = np.pad(imageLena, ((0, M), (0, N)))
    return padded_size


def createD(P, Q):
    D = np.zeros((P, Q))
    for i in range(P):
        for j in range(Q):
            D[i][j] = ((i - P / 2) ** 2) + ((j - Q / 2) ** 2)
    return D


def lowPassFilter(image, cutOff):
    padded_image = get_padded_image(image)
    M = padded_image.shape[0]
    N = padded_image.shape[1]

    dft_padded_image = np.fft.fft2(padded_image)

    u = np.arange(M)
    u = u - M / 2
    v = np.arange(N)
    v = v - N / 2
    V, U = np.meshgrid(v, u)
    D = np.sqrt(np.multiply(U, U) + np.multiply(V, V))
    H = np.zeros((D.shape[0], D.shape[1]))
    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            if D[i][j] <= cutOff:
                H[i][j] = 1
    G = np.multiply(H, dft_padded_image)

    filtered_image = np.fft.ifft2(G).real
    crop_filtered_image = filtered_image[0:image.shape[0], 0:image.shape[1]]
    return crop_filtered_image


"""
    index_X = np.where(u > M)
    for val in index_X:
        u[val] = u[val] - M * 2

    index_Y = np.where(v > N)
    for val in index_Y:
        v[val] = v[val] - N * 2

    V, U = np.meshgrid(v, u)

    D = np.sqrt(np.multiply(U, U) + np.multiply(V, V))

    print(dft_padded_image.shape)
    print(D)
    imagesToPlot = [D]
    label = ["image Lena"]
    affichage_rows_cols_images(1, 1, imagesToPlot, label)
"""
