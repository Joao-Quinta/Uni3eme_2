import matplotlib.pyplot as plt
import math
from skimage import io
import numpy as np
import copy
import skimage.metrics as metric
from scipy import signal


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


def createD(M, N):
    u = np.arange(M)
    u = u - M / 2
    v = np.arange(N)
    v = v - N / 2
    V, U = np.meshgrid(v, u)
    D = np.sqrt(np.multiply(U, U) + np.multiply(V, V))
    return D


def idealLowPassFilter(image, cutOff):
    dft_image = np.fft.fft2(image)
    D = createD(image.shape[0], image.shape[1])
    H = np.zeros((D.shape[0], D.shape[1]))

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            if D[i][j] <= cutOff:
                H[i][j] = 1

    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image


def butterLowPassFilter(image, cutOff, n):
    dft_image = np.fft.fft2(image)
    D = createD(image.shape[0], image.shape[1])
    H = np.zeros((D.shape[0], D.shape[1]))

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            H[i][j] = 1 / (1 + ((D[i][j] / cutOff) ** (2 * n)))

    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image


def gaussianLowPassFilter(image, cutOff):
    dft_image = np.fft.fft2(image)
    D = createD(image.shape[0], image.shape[1])
    H = np.zeros((D.shape[0], D.shape[1]))

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            H[i][j] = np.exp(((D[i][j] ** 2) / (2 * (cutOff ** 2))) * -1)

    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image


def idealHighPassFilter(image, cutOff):
    dft_image = np.fft.fft2(image)
    D = createD(image.shape[0], image.shape[1])
    H = np.zeros((D.shape[0], D.shape[1]))

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            if D[i][j] > cutOff:
                H[i][j] = 1

    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image


def butterHighPassFilter(image, cutOff, n):
    dft_image = np.fft.fft2(image)
    D = createD(image.shape[0], image.shape[1])
    H = np.zeros((D.shape[0], D.shape[1]))

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            H[i][j] = 1 - (1 / (1 + ((D[i][j] / cutOff) ** (2 * n))))

    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image


def gaussianHighPassFilter(image, cutOff):
    dft_image = np.fft.fft2(image)
    D = createD(image.shape[0], image.shape[1])
    H = np.zeros((D.shape[0], D.shape[1]))

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            H[i][j] = 1 - np.exp(((D[i][j] ** 2) / (2 * (cutOff ** 2))) * -1)

    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image


def bandRejectIdeal(image, cutOff, bandWidth):
    dft_image = np.fft.fft2(image)
    D = createD(image.shape[0], image.shape[1])  # no pad ?
    H = np.ones((D.shape[0], D.shape[1]))
    lBandWidth = cutOff - bandWidth / 2
    hBandWidth = cutOff + bandWidth / 2

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            if lBandWidth <= D[i][j] <= hBandWidth:
                H[i][j] = 0
    return H

    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image


def bandRejectButter(image, cutOff, bandWidth, n):
    dft_image = np.fft.fft2(image)
    D = createD(image.shape[0], image.shape[1])  # no pad ?
    H = np.zeros((D.shape[0], D.shape[1]))

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            H[i][j] = 1 / (1 + (((D[i][j] * bandWidth) / ((D[i][j] ** 2) - (cutOff ** 2))) ** (2 * n)))

    return H
    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image


def bandRejectGaussian(image, cutOff, bandWidth):
    dft_image = np.fft.fft2(image)
    D = createD(image.shape[0], image.shape[1])  # no pad ?
    H = np.zeros((D.shape[0], D.shape[1]))

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            H[i][j] = 1 - np.exp(-1 * ((((D[i][j] ** 2) - (cutOff ** 2)) / (D[i][j] * bandWidth)) ** 2))
    return H

    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image


def bandPassIdeal(image, cutOff, bandWidth):
    dft_image = np.fft.fft2(image)
    D = createD(image.shape[0], image.shape[1])  # no pad ?
    H = np.zeros((D.shape[0], D.shape[1]))
    lBandWidth = cutOff - bandWidth / 2
    hBandWidth = cutOff + bandWidth / 2

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            if lBandWidth <= D[i][j] <= hBandWidth:
                H[i][j] = 1
    return H

    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image


def bandPassButter(image, cutOff, bandWidth, n):
    dft_image = np.fft.fft2(image)
    D = createD(image.shape[0], image.shape[1])  # no pad ?
    H = np.zeros((D.shape[0], D.shape[1]))

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            H[i][j] = 1 - (1 / (1 + (((D[i][j] * bandWidth) / ((D[i][j] ** 2) - (cutOff ** 2))) ** (2 * n))))

    return H
    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image


def bandPassGaussian(image, cutOff, bandWidth):
    dft_image = np.fft.fft2(image)
    D = createD(image.shape[0], image.shape[1])  # no pad ?
    H = np.zeros((D.shape[0], D.shape[1]))

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            H[i][j] = 1 - (1 - np.exp(-1 * ((((D[i][j] ** 2) - (cutOff ** 2)) / (D[i][j] * bandWidth)) ** 2)))
    return H

    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image


def medianFiltering(image, N):
    imageRes = np.zeros((image.shape[0], image.shape[1]))
    boxValues = []
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for z in range(N):
                if i + z - N < 0 or i + z - N > image.shape[0] - 1:
                    for _ in range(N):
                        boxValues.append(0)
                else:
                    if j + z - N < 0 or j + N > image.shape[1] - 1:
                        boxValues.append(0)
                    else:
                        for k in range(N):
                            boxValues.append(image[i + z - N][j + k - N])
            boxValues.sort()
            imageRes[i][j] = boxValues[len(boxValues) // 2]
            boxValues = []
    return imageRes


def compute_D1_D2(u, v, M, N, val0, val1, type):
    if type == 1:
        return np.sqrt((u - M / 2 - val0) ** 2 + (v - N / 2 - val1) ** 2)
    else:
        return np.sqrt((u - M / 2 + val0) ** 2 + (v - N / 2 + val1) ** 2)


def notchIdealFilter(image, centers):
    dft_image = np.fft.fft2(image)
    M = image.shape[0]
    N = image.shape[1]
    H = np.ones((M, N))
    # D1 = np.sqrt((u - M/2 - centers[0][0])**2 + (v - N/2 - centers[0][1])**2))
    # D2 = np.sqrt((u - M/2 + centers[0][0])**2 + (v - N/2 + centers[0][1])**2))

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            res = 1
            for center in centers:
                if compute_D1_D2(i, j, M, N, center[0], center[1], 1) <= center[2] or compute_D1_D2(i, j, M, N,
                                                                                                 center[0],
                                                                                                 center[1],
                                                                                                 0) <= center[2]:
                    res = res * 0
            H[i][j] = res

    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image


def notchIdealFilter_(image, centers):
    dft_image = np.fft.fft2(image)
    M = image.shape[0]
    N = image.shape[1]
    H = np.ones((M, N))
    # D1 = np.sqrt((u - M/2 - centers[0][0])**2 + (v - N/2 - centers[0][1])**2))
    # D2 = np.sqrt((u - M/2 + centers[0][0])**2 + (v - N/2 + centers[0][1])**2))
    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            res = 1
            for center in centers:
                if compute_D1_D2(i, j, M, N, center[0], center[1], 1) <= center[2] or compute_D1_D2(i, j, M, N,
                                                                                                 center[0],
                                                                                                 center[1],
                                                                                                 0) <= center[2]:
                    res = res * 0
            H[i][j] = res
    return H


"""
def bandPassIdeal(image, cutOff, bandWidth):
    dft_image = np.fft.fft2(image)
    D = createD(image.shape[0], image.shape[1])  # no pad ?
    H = np.zeros((D.shape[0], D.shape[1]))
    lBandWidth = cutOff - bandWidth / 2
    hBandWidth = cutOff + bandWidth / 2

    for i in range(H.shape[0]):
        for j in range(H.shape[1]):
            if lBandWidth <= D[i][j] <= hBandWidth:
                H[i][j] = 1
    return H

    G = np.multiply(H, dft_image)
    filtered_image = np.fft.ifft2(G).real
    return filtered_image

"""
