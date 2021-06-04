import lib
import numpy as np
import skimage.util as util

path = "lena.png"
imageLena = lib.loadImag(path)
res = lib.bandPassButter(imageLena, 150, 30, 2)
lib.affichage_rows_cols_images(1, 1, [res], ["t"])

res = lib.notchIdealFilter(imageLena, 20, [[100,100]])
lib.affichage_rows_cols_images(1, 1, [res], ["t"])