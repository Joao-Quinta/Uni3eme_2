import lib
import numpy as np
import skimage.util as util

# a

path = "lena.png"
imageLena = lib.loadImag(path)

var = (20 / 255) ** 2
noisyGrayLena = util.random_noise(imageLena, var=var)
msenoisy = lib.metric.mean_squared_error(imageLena, noisyGrayLena)


imagesToPlot = [imageLena, noisyGrayLena]
label = ["image Lena", " noisy lena -> mse = " + str(msenoisy)]
lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)

# actual exercice a

filter = 1 / 16 * lib.np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
image_padded = lib.padding(noisyGrayLena, filter, 'constant')
image_padded_filtered = lib.image_filtering(image_padded, filter)
image_padded_filtered = lib.get_cropped_image(image_padded_filtered, -1)
mseFilterA = lib.metric.mean_squared_error(imageLena, image_padded_filtered)

imagesToPlot = [imageLena, noisyGrayLena, image_padded_filtered]
label = ["image Lena", " noisy lena -> mse = " + str(msenoisy), "gaussion filter (a) -> " + str(mseFilterA)]
lib.affichage_rows_cols_images(1, 3, imagesToPlot, label)
print("MSE -> lena & lena gaussion filter (a) -> " + str(mseFilterA))

# b

ideal_lowpass_filter = lib.idealLowPassFilter(noisyGrayLena, 700)
mse_ideal = lib.metric.mean_squared_error(imageLena, ideal_lowpass_filter)


butter_lowpass_filter = lib.butterLowPassFilter(noisyGrayLena, 1000, 2)
mse_butter = lib.metric.mean_squared_error(imageLena, butter_lowpass_filter)


gaussian_lowpass_filter = lib.gaussianLowPassFilter(noisyGrayLena, 1000)
mse_gaussian = lib.metric.mean_squared_error(imageLena, gaussian_lowpass_filter)


imagesToPlot = [imageLena, noisyGrayLena, image_padded_filtered, ideal_lowpass_filter, butter_lowpass_filter, gaussian_lowpass_filter]
label = ["image lena", "noisy lena", "gaussian filter (a)", "ideal low pass (b)", "butter low pass (b)", "gaussian low pass (b)"]
lib.affichage_rows_cols_images(2, 3, imagesToPlot, label)

print("MSE -> lena & lena noisy -> " + str(msenoisy))
print("MSE -> lena & lena gaussian (a) -> " + str(mseFilterA))
print("MSE -> lena & ideal low pass (b) - cutoff = 700 -> " + str(mse_ideal))
print("MSE -> lena & butter low pass (b) - cutoff = 1000 - n = 2 -> " + str(mse_butter))
print("MSE -> lena & gaussian low pass (b) - cutoff = 1000 -> " + str(mse_gaussian))
