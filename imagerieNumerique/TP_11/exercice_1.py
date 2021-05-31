import numpy as np
from skimage import transform
import lib

# (a)
intervalStart = 1
intervalEnd = 256
n = 256

one_axe = np.linspace(intervalStart, intervalEnd, n)
x_axis, y_axis = np.meshgrid(one_axe, one_axe)

image_1_a = np.sin(2 * np.pi * x_axis / (n / 10))
dft_image_1_a = np.fft.fftshift(image_1_a)
magnitude_dft_image_1_a = np.abs(dft_image_1_a)
print(image_1_a)
print()
print(magnitude_dft_image_1_a)
imagesToPlot = [image_1_a, np.log(magnitude_dft_image_1_a + 1)]
label = ["sinusoidal vertical", "magnitude"]

lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)

# (b)

image_1_b = np.sin(2 * np.pi * y_axis / (n / 5))
dft_image_1_b = np.fft.fftshift(image_1_b)
magnitude_dft_image_1_b = np.abs(dft_image_1_b)

imagesToPlot = [image_1_b, np.log(magnitude_dft_image_1_b + 1)]
label = ["sinusoidal horizontal", "magnitude"]

lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)

# (c)

image_1_c = image_1_a + image_1_b
dft_image_1_c = np.fft.fftshift(image_1_c)
magnitude_dft_image_1_c = np.abs(dft_image_1_c)

imagesToPlot = [image_1_c, np.log(magnitude_dft_image_1_c + 1)]
label = ["sinusoidal vertical + horizontal", "magnitude"]

lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)

# (d)

image_1_d = transform.rotate(image_1_c, 25)
wm, hm = lib.rotatedRectWithMaxArea(image_1_c.shape[0], image_1_c.shape[1], lib.math.radians(25))
image_1_d = lib.crop_around_center(image_1_d, wm, hm)
dft_image_1_d = np.fft.fftshift(image_1_d)
magnitude_dft_image_1_d = np.abs(dft_image_1_d)

imagesToPlot = [image_1_d, np.log(magnitude_dft_image_1_d + 1)]
label = ["sinusoidal vertical + horizontal - rotated and cropped", "magnitude"]

lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)

# (e)

image_1_e = image_1_a * image_1_b
dft_image_1_e = np.fft.fftshift(image_1_e)
magnitude_dft_image_1_e = np.abs(dft_image_1_e)

imagesToPlot = [image_1_e, np.log(magnitude_dft_image_1_e + 1)]
label = ["sinusoidal vertical * horizontal", "magnitude"]

lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)
