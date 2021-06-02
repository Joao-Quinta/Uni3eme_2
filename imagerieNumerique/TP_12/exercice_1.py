import lib
import numpy as np
import skimage.util as util

# a

path = "lena.png"
imageLena = lib.loadImag(path)

var = (20 / 255) ** 2
noisyGrayLena = util.random_noise(imageLena, var=var)
mse = lib.metric.mean_squared_error(imageLena, noisyGrayLena)
print("MSE -> lena & lena noisy -> " + str(mse))

filter = 1 / 16 * lib.np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
image_padded = lib.padding(noisyGrayLena, filter, 'constant')
image_padded_filtered = lib.image_filtering(image_padded, filter)
image_padded_filtered = lib.get_cropped_image(image_padded_filtered, -1)
mse = lib.metric.mean_squared_error(imageLena, image_padded_filtered)

imagesToPlot = [imageLena, noisyGrayLena, image_padded_filtered]
label = ["image Lena", " noisy", "gaussion filter (a) -> " + str(mse)]
lib.affichage_rows_cols_images(1, 3, imagesToPlot, label)
print("MSE -> lena & lena noisy with gaussian filter -> " + str(mse))

# b

ideal_lowpass_filter = lib.idealLowPassFilter(noisyGrayLena, 590)
mse = lib.metric.mean_squared_error(imageLena, ideal_lowpass_filter)
print(mse)
imagesToPlot = [imageLena, noisyGrayLena, image_padded_filtered, ideal_lowpass_filter]
label = ["image Lena", " noisy", "a", "b"]
lib.affichage_rows_cols_images(1, 4, imagesToPlot, label)
