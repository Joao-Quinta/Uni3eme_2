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


mse = lib.metric.mean_squared_error(imageLena, noisyGrayLena)
print(mse)

# b
i=600
"""
mse_a = []
while i < 980:
    ideal_lowpass_filter = lib.lowPassFilter(noisyGrayLena, 980)
    mse_a.append(lib.metric.mean_squared_error(ideal_lowpass_filter, imageLena))
    i = i + 1
    print(i)

print(mse_a.index(min(mse_a)))
print(mse_a.index(min(mse_a)) + 600)
"""
ideal_lowpass_filter = lib.lowPassFilter(noisyGrayLena, 590)
mse = lib.metric.mean_squared_error(imageLena, ideal_lowpass_filter)
print(mse)
imagesToPlot = [imageLena, noisyGrayLena, image_padded_filtered, ideal_lowpass_filter]
label = ["image Lena", " noisy", "a", "b"]
lib.affichage_rows_cols_images(1, 4, imagesToPlot, label)
