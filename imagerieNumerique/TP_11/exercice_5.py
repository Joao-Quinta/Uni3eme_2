import lib
import numpy as np

# (a)

path = "lena.png"
imageLena = lib.loadImag(path)

dft_imageLena = np.fft.fft2(imageLena)
angle_dft_imageLena = np.angle(dft_imageLena)
magnitude_dft_imageLena = np.abs(dft_imageLena)

imagesToPlot = [imageLena, angle_dft_imageLena, np.log(magnitude_dft_imageLena + 1)]
label = ["image Lena", "phase", "magnitude"]
lib.affichage_rows_cols_images(1, 3, imagesToPlot, label)

# (b)

index_0 = [x for x in range(imageLena.shape[0]) if x % 2 == 1]
index_1 = [y for y in range(imageLena.shape[1]) if y % 2 == 1]

imageLena_d = np.delete(imageLena, index_0, 0)
imageLena_d = np.delete(imageLena_d, index_1, 1)

dft_imageLena_d = np.fft.fft2(imageLena_d)
angle_dft_imageLena_d = np.angle(dft_imageLena_d)
magnitude_dft_imageLena_d = np.abs(dft_imageLena_d)

imagesToPlot = [imageLena_d, angle_dft_imageLena_d, np.log(magnitude_dft_imageLena_d + 1)]
label = ["image Lena downscale", "phase downscale", "magnitude downscale"]
lib.affichage_rows_cols_images(1, 3, imagesToPlot, label)

# (c)

lena_array_ones_zeroes = np.ones(imageLena.shape)
index_0 = [x for x in range(lena_array_ones_zeroes.shape[0]) if x % 2 == 1]
index_1 = [x for x in range(lena_array_ones_zeroes.shape[1]) if x % 2 == 1]

y0 = np.zeros(lena_array_ones_zeroes.shape[0])
y1 = np.zeros(lena_array_ones_zeroes.shape[1])

for val in index_0:
    lena_array_ones_zeroes[:, val] = y0
for val in index_1:
    lena_array_ones_zeroes[val, :] = y1

rebuild_lena = np.multiply(imageLena, lena_array_ones_zeroes)

dft_imageLena_rebuild = np.fft.fft2(rebuild_lena)
angle_dft_imageLena_rebuild = np.angle(dft_imageLena_rebuild)
magnitude_dft_imageLena_rebuild = np.abs(dft_imageLena_rebuild)

imagesToPlot = [rebuild_lena, angle_dft_imageLena_rebuild, np.log(magnitude_dft_imageLena_rebuild + 1)]
label = ["image Lena rebuild", "phase rebuild", "magnitude rebuild"]
lib.affichage_rows_cols_images(1, 3, imagesToPlot, label)