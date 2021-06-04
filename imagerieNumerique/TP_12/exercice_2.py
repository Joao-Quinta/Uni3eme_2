import lib
import numpy as np
import skimage.util as util

# a

path = "lena.png"
imageLena = lib.loadImag(path)
filter = 1 / 9 * lib.np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
imageLena_pad = lib.padding(imageLena, filter, 'constant')
imageLena_pad_filtered_box_ = lib.image_filtering(imageLena_pad, filter)
imageLena_pad_filtered_box = lib.get_cropped_image(imageLena_pad_filtered_box_, -1)

mseFilter_box = lib.metric.mean_squared_error(imageLena, imageLena_pad_filtered_box)

imagesToPlot = [imageLena, imageLena_pad_filtered_box]
label = ["image Lena", " lena with box filter  " + str(mseFilter_box)]
lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)

# actual a

filter = 1 / 9 * lib.np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
imageLena_pad_filtered_box_pad_filtre_gauss_ = lib.image_filtering(imageLena_pad_filtered_box_, filter)
imageLena_pad_filtered_box_pad_filtre_gauss = lib.get_cropped_image(imageLena_pad_filtered_box_pad_filtre_gauss_, -1)

mseFilter_gauss = lib.metric.mean_squared_error(imageLena, imageLena_pad_filtered_box_pad_filtre_gauss)

imagesToPlot = [imageLena, imageLena_pad_filtered_box, imageLena_pad_filtered_box_pad_filtre_gauss]
label = ["image Lena", " lena with box filter  " + str(mseFilter_box),
         "lena with gaussian filter  " + str(mseFilter_gauss)]
lib.affichage_rows_cols_images(1, 3, imagesToPlot, label)

# b

ideal_lowpass_filter = lib.idealHighPassFilter(imageLena_pad_filtered_box, 200)
mse_ideal = lib.metric.mean_squared_error(imageLena, ideal_lowpass_filter)
imagesToPlot = [imageLena, imageLena_pad_filtered_box, imageLena_pad_filtered_box_pad_filtre_gauss, ideal_lowpass_filter]
label = ["image Lena", " lena with box filter  " + str(mseFilter_box),
         "lena with gaussian filter  " + str(mseFilter_gauss), "lena with ideal high pass filter : d0 = 200"]
lib.affichage_rows_cols_images(2, 2, imagesToPlot, label)

print("MSE -> lena & lena box filter -> " + str(mseFilter_box))
print("MSE -> lena & lena gaussian (a) -> " + str(mseFilter_gauss))
print("MSE -> lena & ideal high pass (b) - cutoff = 200 -> " + str(mse_ideal))

"""
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



x = range(200, 400, 1)
y = []
for val in x:
    print(val)
    res = lib.idealHighPassFilter(imageLena_pad_filtered_box, val)
    y.append(lib.metric.mean_squared_error(imageLena, res))
lib.plt.plot(x, y)
lib.plt.title("mse in function of cutoff -> high pass filter")
lib.plt.show()

print(200+ y.index(min(y)))
"""
