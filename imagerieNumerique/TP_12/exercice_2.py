import lib
import numpy as np
import skimage.util as util

# a

path = "lena.png"
imageLena = lib.loadImag(path)

filter = 1 / 9 * lib.np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
image_padded = lib.padding(imageLena, filter, 'constant')
image_padded_filtered = lib.image_filtering(image_padded, filter)
image_padded_filtered_a = lib.get_cropped_image(image_padded_filtered, -1)

mseFilterA = lib.metric.mean_squared_error(imageLena, image_padded_filtered_a)

imagesToPlot = [imageLena, image_padded_filtered_a]
label = ["image Lena", " lena with box filter  " + str(mseFilterA)]
lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)

# actual a

filter = 1 / 9 * lib.np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
image_padded = lib.padding(imageLena, filter, 'constant')
image_padded_filtered = lib.image_filtering(image_padded, filter)
filter = 1 / 16 * lib.np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
image_padded_filtered = lib.image_filtering(image_padded_filtered, filter)
image_padded_filtered = lib.get_cropped_image(image_padded_filtered, -1)
mseFilterB = lib.metric.mean_squared_error(imageLena, image_padded_filtered)

imagesToPlot = [imageLena, image_padded_filtered_a, image_padded_filtered]
label = ["image Lena", " lena with box filter  " + str(mseFilterA), "lena with gaussian filter  " + str(mseFilterB)]
lib.affichage_rows_cols_images(1, 3, imagesToPlot, label)


# b

ideal_lowpass_filter = lib.idealHighPassFilter(image_padded_filtered_a, 200)
mse_ideal = lib.metric.mean_squared_error(imageLena, ideal_lowpass_filter)


butter_lowpass_filter = lib.butterHighPassFilter(image_padded_filtered_a, 200, 2)
mse_butter = lib.metric.mean_squared_error(imageLena, butter_lowpass_filter)


gaussian_lowpass_filter = lib.gaussianHighPassFilter(image_padded_filtered_a, 200)
mse_gaussian = lib.metric.mean_squared_error(imageLena, gaussian_lowpass_filter)


imagesToPlot = [imageLena, image_padded_filtered_a, image_padded_filtered, ideal_lowpass_filter, butter_lowpass_filter, gaussian_lowpass_filter]
label = ["image lena", "box blur lena", "gaussian filter lena (a)", "ideal high pass (b)", "butter high pass (b)", "gaussian high pass (b)"]
lib.affichage_rows_cols_images(2, 3, imagesToPlot, label)

print("MSE -> lena & lena noisy -> " + str(mseFilterA))
print("MSE -> lena & lena gaussian (a) -> " + str(mseFilterB))
print("MSE -> lena & ideal high pass (b) - cutoff = 200 -> " + str(mse_ideal))
print("MSE -> lena & butter high pass (b) - cutoff = 200 - n = 2 -> " + str(mse_butter))
print("MSE -> lena & gaussian high pass (b) - cutoff = 200 -> " + str(mse_gaussian))

