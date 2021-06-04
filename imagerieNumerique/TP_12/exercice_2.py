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

