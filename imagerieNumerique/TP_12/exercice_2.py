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
"""
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
"""

# b
x = range(25, 1000, 25)
y = []
for val in x:
    print(val)
    h_ideal = lib.gaussianHighPassFilter(image_padded_filtered_a, val)
    y.append(lib.metric.mean_squared_error(imageLena, h_ideal))

lib.plt.plot(x, y)
lib.plt.title("mse in function of cutoff - gauss high pass filter")
lib.plt.show()
