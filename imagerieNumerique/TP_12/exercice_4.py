import lib
import numpy as np
import skimage.util as util

path = "img_005.jpg"
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
