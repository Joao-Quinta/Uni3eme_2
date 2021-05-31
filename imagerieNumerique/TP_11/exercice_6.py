import numpy as np
import lib
import scipy.signal as sciSi
import time
# load images

path = "img_001.jpg"
path2 = "img_002.jpg"

image1 = lib.loadImag(path)
image2 = lib.loadImag(path2)

# (a)
start_a = time.time()

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

end_a = time.time()

imagesToPlot = [res]
label = ["exo 6 a"]
lib.affichage_rows_cols_images(1, 1, imagesToPlot, label)

# (b)

image1b = image1
image2b = image2

start_b = time.time()

image1b = image1b - image1b.mean()
image2b = image2b - image2b.mean()
res = sciSi.correlate2d(image1b, image2b)

imagesToPlot = [res]
label = ["image Lena"]
lib.affichage_rows_cols_images(1, 1, imagesToPlot, label)

end_b = time.time()

# (c)
print("A : ", end_a - start_a)
print("B : ", end_b - start_b)
