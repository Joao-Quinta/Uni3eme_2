import lib
import numpy as np
import skimage.util as util

# a

path = "lena.png"
imageLena = lib.loadImag(path)

var = (20 / 255) ** 2
noisyGrayLena = util.random_noise(imageLena, var=var)
filter = 1 / 16 * lib.np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
image_padded = lib.padding(imageLena, filter, 'constant')
image_padded_filtered = lib.image_filtering(image_padded, filter)
image_padded_filtered = lib.get_cropped_image(image_padded_filtered, -1)

imagesToPlot = [imageLena, noisyGrayLena, image_padded_filtered]
label = ["image Lena", "noisy lena - sigma = 20", "denoising - gaussian filter"]
lib.affichage_rows_cols_images(1, 3, imagesToPlot, label)

mse = lib.metric.mean_squared_error(noisyGrayLena, image_padded_filtered)

# b
