import lib
import numpy as np

# (a)

path = "lena.png"
imageLena = lib.loadImag(path)
path = "img_002.jpg"
imageAldo = lib.loadImag(path)

dft_imageLena = np.fft.fft2(imageLena)
angle_dft_imageLena = np.angle(dft_imageLena)
magnitude_dft_imageLena = np.abs(dft_imageLena)

dft_imageAldo = np.fft.fft2(imageAldo)
angle_dft_imageAldo = np.angle(dft_imageAldo)
magnitude_dft_imageAldo = np.abs(dft_imageAldo)

imagesToPlot = [imageLena, angle_dft_imageLena, np.log(magnitude_dft_imageLena + 1), imageAldo, angle_dft_imageAldo, np.log(magnitude_dft_imageAldo + 1)]
label = ["image Lena", "phase Lena", "magnitude Lena", "image Aldo", "phase Aldo", "magnitude Aldo"]
lib.affichage_rows_cols_images(2, 3, imagesToPlot, label)