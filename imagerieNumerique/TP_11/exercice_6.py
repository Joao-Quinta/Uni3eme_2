import numpy as np
import lib

# load images

path = "img_001.jpg"
path2 = "img_002.jpg"
image1 = lib.loadImag(path)
image2 = lib.loadImag(path2)

# (a)

dim1 = image1.shape
dim2 = image2.shape

dimRes = np.add(dim1, dim2)
dimRes[0] = dimRes[0] - 1
dimRes[1] = dimRes[1] - 1
image2_flip_v = lib.matrixflip(image2, 'v')
image2_flip_h_v = lib.matrixflip(image2_flip_v, 'h')
pad1 = np.pad(image1, ((0, dimRes[0] - dim1[0]), (0, dimRes[1] - dim1[1])))  # image 1 padded
pad2 = np.pad(image2_flip_h_v, ((0, dimRes[0] - dim2[0]), (0, dimRes[1] - dim2[1])))  # image 2 flipped and padded

fft1 = np.fft.fft2(pad1)
fft2 = np.fft.fft2(pad2)

res = np.fft.ifft2(np.multiply(fft1, fft2)).real

imagesToPlot = [res]
label = ["image Lena"]
lib.affichage_rows_cols_images(1, 1, imagesToPlot, label)
