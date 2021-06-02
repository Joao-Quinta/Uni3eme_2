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
