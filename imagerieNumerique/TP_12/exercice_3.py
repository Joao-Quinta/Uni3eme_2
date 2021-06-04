import lib
import numpy as np
import skimage.util as util

# load images
path = "img_001.jpeg"
image_1 = lib.loadImag(path)

path = "img_002.png"
image_2 = lib.loadImag(path)

path = "img_003.jpg"
image_3 = lib.loadImag(path)

path = "img_004.png"
image_4 = lib.loadImag(path)

dft_image_1 = np.fft.fft2(image_1)
magnitude_dft_image_1 = np.abs(dft_image_1)
dft_image_2 = np.fft.fft2(image_2)
magnitude_dft_image_2 = np.abs(dft_image_2)
dft_image_3 = np.fft.fft2(image_3)
magnitude_dft_image_3 = np.abs(dft_image_3)
dft_image_4 = np.fft.fft2(image_4)
magnitude_dft_image_4 = np.abs(dft_image_4)

imagesToPlot = [image_1, image_2, image_3, image_4, np.log(magnitude_dft_image_1 + 1),
                np.log(magnitude_dft_image_2 + 1), np.log(magnitude_dft_image_3 + 1), np.log(magnitude_dft_image_4 + 1)]
label = ["image 1", "image 2", "image 3", "image 4", "magnitude image 1", "magnitude image 2", "magnitude image 3",
         "magnitude image 4"]
lib.affichage_rows_cols_images(2, 4, imagesToPlot, label)


# image 1 -> notch
centers = [[123, -105, 7], [135, 125, 5], [14, -105, 5], [-20, -105, 5], [50, -105, 5]]
filter = lib.notchIdealFilter_(dft_image_1, centers)

imagesToPlot = [np.log(magnitude_dft_image_1 + 1), filter]
label = ["magnitude image 1", "notch filter"]
lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)

result = lib.notchIdealFilter(image_1, centers)
result_mag = np.abs(np.fft.fft2(result))
imagesToPlot = [np.log(magnitude_dft_image_1 + 1), filter, np.log(result_mag + 1)]
label = ["magnitude image 1", "notch filter", "magnitude after filter"]
lib.affichage_rows_cols_images(1, 3, imagesToPlot, label)

imagesToPlot = [image_1, result]
label = ["image 1", "image 1 with notch filter"]
lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)

# image 3 -> notch

centers = [[80, 145, 20], [-80, 145, 20]]
filter = lib.notchIdealFilter_(dft_image_3, centers)

imagesToPlot = [np.log(magnitude_dft_image_3 + 1), filter]
label = ["magnitude image 3", "notch filter"]
lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)

result = lib.notchIdealFilter(image_3, centers)
result_mag = np.abs(np.fft.fft2(result))
imagesToPlot = [np.log(magnitude_dft_image_3 + 1), filter, np.log(result_mag + 1)]
label = ["magnitude image 3", "notch filter", "magnitude after filter"]
lib.affichage_rows_cols_images(1, 3, imagesToPlot, label)

imagesToPlot = [image_3, result]
label = ["image 3", "image 3 with notch filter"]
lib.affichage_rows_cols_images(1, 2, imagesToPlot, label)
