import lib
import numpy as np

# a
"""
path = "img_003.png"
imageLena = lib.loadImag(path)
dft_imageLena = np.fft.fft2(imageLena)
angle_dft_imageLena = np.angle(dft_imageLena)
magnitude_dft_imageLena = np.abs(dft_imageLena)

imagesToPlot = [imageLena, angle_dft_imageLena, np.log(magnitude_dft_imageLena + 1)]
label = ["img 3", "phase img 3", "magnitude img 3"]
lib.affichage_rows_cols_images(1, 3, imagesToPlot, label)

"""
