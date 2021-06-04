import lib
import numpy as np
import skimage.util as util

# a

path = "img_006.jpg"
image5 = lib.loadImag(path)

res = lib.medianFiltering(image5, 2)

img = [image5]
lb = ["Original"]
for i in range(5, 13):
    res = lib.medianFiltering(image5, i)
    img.append(res)
    lb.append("N = " + str(i))
    print(i)

lib.affichage_rows_cols_images(3, 3, img, lb)

# b

dft_image_5 = np.fft.fft2(image5)
magnitude_dft_image_5 = np.abs(dft_image_5)
"""
imagesToPlot = [image5, np.log(magnitude_dft_image_5 + 1)]
label = ["image 6","magnitude image 6"]
lib.affichage_rows_cols_images(1,2, imagesToPlot, label)
"""
centers = [[77,-230, 10], [115,-240, 10]]
filter = lib.notchIdealFilter_(image5, centers)
"""
imagesToPlot = [np.log(magnitude_dft_image_5 + 1), filter]
label = ["magnitude image 6", "notch filter"]
lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)
"""
result = lib.notchIdealFilter(image5, centers)
result_mag = np.abs(np.fft.fft2(result))
imagesToPlot = [np.log(magnitude_dft_image_5 + 1), filter, np.log(result_mag + 1)]
label = ["magnitude image 6", "notch filter", "magnitude after filter"]
lib.affichage_rows_cols_images(1, 3, imagesToPlot, label)

imagesToPlot = [image5, result]
label = ["image 6", "image 6 with notch filter"]
lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)

# c

imagesToPlot = [image5, img[4], img[5], result]
label = ["image 6", "image6 median filter N = 8", "image6 median filter N = 9", "image 6 with notch filter"]
lib.affichage_rows_cols_images(2, 2, imagesToPlot, label)