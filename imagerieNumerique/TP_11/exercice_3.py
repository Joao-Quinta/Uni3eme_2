import lib
import numpy as np

# get smaller image size
path = "lena.png"
imageLena = lib.loadImag(path)
path = "img_001.jpg"
imageAldo = lib.loadImag(path)
smallerSize = lib.get_smallest_shape_in_image([imageLena, imageAldo])

# set both images to the smaller one size
imageLena = imageLena[0:smallerSize, 0:smallerSize]
imageAldo = imageAldo[0:smallerSize, 0:smallerSize]

# (a)
dft_imageLena = np.fft.fft2(imageLena)
angle_dft_imageLena = np.angle(dft_imageLena)
magnitude_dft_imageLena = np.abs(dft_imageLena)

dft_imageAldo = np.fft.fft2(imageAldo)
angle_dft_imageAldo = np.angle(dft_imageAldo)
magnitude_dft_imageAldo = np.abs(dft_imageAldo)

imagesToPlot = [imageLena, angle_dft_imageLena, np.log(magnitude_dft_imageLena + 1), imageAldo, angle_dft_imageAldo, np.log(magnitude_dft_imageAldo + 1)]
label = ["image Lena", "phase Lena", "magnitude Lena", "image Aldo", "phase Aldo", "magnitude Aldo"]
lib.affichage_rows_cols_images(2, 3, imagesToPlot, label)

# (b)
reconstructed_mag_lena_phase_aldo = magnitude_dft_imageLena * np.exp(1j * angle_dft_imageAldo)
reconverted_reconstructed_mag_lena_phase_aldo = np.fft.ifft2(reconstructed_mag_lena_phase_aldo).real

reconstructed_mag_aldo_phase_lena = magnitude_dft_imageAldo * np.exp(1j * angle_dft_imageLena)
reconverted_reconstructed_mag_aldo_phase_lena = np.fft.ifft2(reconstructed_mag_aldo_phase_lena).real

imagesToPlot = [imageLena, imageAldo, reconverted_reconstructed_mag_lena_phase_aldo, reconverted_reconstructed_mag_aldo_phase_lena]
label = ["real lena", "real aldo", "mag -> lena & phase -> aldo", "mag -> aldo & phase -> lena"]
lib.affichage_rows_cols_images(2, 2, imagesToPlot, label)


