import lib
import numpy as np

# (a)

path = "lena.png"
imageLena = lib.loadImag(path)
dft_imageLena = np.fft.fft2(imageLena)
angle_dft_imageLena = np.angle(dft_imageLena)
magnitude_dft_imageLena = np.abs(dft_imageLena)

imagesToPlot = [imageLena, angle_dft_imageLena, np.log(magnitude_dft_imageLena + 1)]
label = ["image Lena", "phase Lena", "magnitude Lena"]
lib.affichage_rows_cols_images(1, 3, imagesToPlot, label)

# (b)

lena_image_flip_h = lib.matrixflip(imageLena, 'h')
lena_image_flip_v = lib.matrixflip(imageLena, 'v')
lena_image_flip_h_v = lib.matrixflip(lena_image_flip_v, 'h')

# flip_h
dft_imageLena_flip_h = np.fft.fft2(lena_image_flip_h)
angle_dft_imageLena_flip_h = np.angle(dft_imageLena_flip_h)
magnitude_dft_imageLena_flip_h = np.abs(dft_imageLena_flip_h)

# flip_v
dft_imageLena_flip_v = np.fft.fft2(lena_image_flip_v)
angle_dft_imageLena_flip_v = np.angle(dft_imageLena_flip_v)
magnitude_dft_imageLena_flip_v = np.abs(dft_imageLena_flip_v)

# flip_h_v
dft_imageLena_flip_h_v = np.fft.fft2(lena_image_flip_h_v)
angle_dft_imageLena_flip_h_v = np.angle(dft_imageLena_flip_h_v)
magnitude_dft_imageLena_flip_h_v = np.abs(dft_imageLena_flip_h_v)

imagesToPlot = [lena_image_flip_h, angle_dft_imageLena_flip_h, np.log(magnitude_dft_imageLena_flip_h + 1),
                lena_image_flip_v, angle_dft_imageLena_flip_v, np.log(magnitude_dft_imageLena_flip_v + 1),
                lena_image_flip_h_v, angle_dft_imageLena_flip_h_v, np.log(magnitude_dft_imageLena_flip_h_v + 1)]

label = ["lena flip h", "lena flip h -> phase", "lena flip h -> magnitude",
         "lena flip v", "lena flip v -> phase", "lena flip v -> magnitude",
         "lena flip h_v", "lena flip h_v -> phase", "lena flip h_v -> magnitude"]

lib.affichage_rows_cols_images(3, 3, imagesToPlot, label)
