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

# (b.a)

lenaReconstructionWithAngle = 1 * np.exp(1j * angle_dft_imageLena)
lenaReconstructionWithAngle = np.fft.ifft2(lenaReconstructionWithAngle).real

# (b.b)

lenaReconstructionWithMagnitude = magnitude_dft_imageLena * np.exp(1j * 0)
lenaReconstructionWithMagnitude = np.fft.ifft2(lenaReconstructionWithMagnitude).real

imagesToPlot = [angle_dft_imageLena, np.log(magnitude_dft_imageLena + 1), lenaReconstructionWithAngle, lenaReconstructionWithMagnitude]
label = ["lena phase", "lena magnitude", "reconstruction from phase", "reconstruction from magnitude"]
lib.affichage_rows_cols_images(2, 2, imagesToPlot, label)
