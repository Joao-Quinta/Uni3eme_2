import lib
import numpy as np

#######     a     #######

# x axis
n = 400
x = np.linspace(-10, 10, n)

# y axis for all graphs
gaussianSignal_y = np.zeros(n)
gaussianTransform_y = np.zeros(n)
sincSignal_y = np.zeros(n)
productFTS_y = np.zeros(n)

# computation
for i in range(len(x)):
    gaussianSignal_y[i] = lib.gaussianSignal(x[i], 1)
    gaussianTransform_y[i] = lib.gaussianTransform(x[i], 1)
    sincSignal_y[i] = lib.getSinSignal(x[i])
    productFTS_y[i] = lib.getProductFTS(sincSignal_y[i], gaussianTransform_y[i])

# plot
lib.affichage_rows_cols(2, 2, [x, x, x, x],
                        [gaussianSignal_y, gaussianTransform_y, sincSignal_y, productFTS_y],
                        ["g(t,a) -> a = 1", "G(w, a)", "F(w)", "G(w) * F(w)"])

#######     b     #######

w0 = 10

# x axis
n = 400
x = np.linspace(-10, 10, n)

# y axis for all graphs
gaborSignal_y = np.zeros(n)
gaborTransform_y = np.zeros(n)
productFTS1_y = np.zeros(n)

# computation
for i in range(len(x)):
    gaborSignal_y[i] = lib.gaborSignal(x[i], 1, w0)
    gaborTransform_y[i] = lib.gaborTransform(x[i], 1, w0)
    productFTS1_y[i] = lib.getProductFTS(sincSignal_y[i], gaborTransform_y[i])

# plot
lib.affichage_rows_cols(2, 2, [x, x, x, x],
                        [gaborSignal_y, gaborTransform_y, sincSignal_y, productFTS1_y],
                        ["cos(w0 * x) * G(x, a) -> a = 1", "FT Gabor", "F(w)", "G(w) * F(w)"])

#######     c     #######

w0 = 10
gamma = 1.5

# x axis
n = 400
x = np.linspace(-5, 5, n)

# y axis for all graphs
unsharpenSignal_y = np.zeros(n)
unsharpenTransform_y = np.zeros(n)
productFTS2_y = np.zeros(n)

# computation
for i in range(len(x)):
    unsharpenSignal_y[i] = lib.unsharpenSignal(x[i], gaussianSignal_y[i], gamma, w0)
    unsharpenTransform_y[i] = lib.unsharpenTransform(gamma, 1, x[i])
    productFTS2_y[i] = lib.getProductFTS(sincSignal_y[i], unsharpenTransform_y[i])
print(np.sum(sincSignal_y))
print(np.sum(productFTS2_y))
# plot
lib.affichage_rows_cols(2, 2, [x, x, x, x],
                        [unsharpenSignal_y, unsharpenTransform_y, sincSignal_y, productFTS2_y],
                        ["unsharp mask", "unsharp transform -> G(w)", "F(w)", "G(w) * F(w)"])
