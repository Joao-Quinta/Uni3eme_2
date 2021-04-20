import lib
import numpy as np

n = 400
x = np.linspace(-10, 10, n)

gaussianSignal_y = np.zeros(n)
gaussianTransform_y = np.zeros(n)

signalSinusSqr = np.sinc(x) ** 2

for i in range(len(x)):
    gaussianSignal_y[i] = lib.gaussianSignal(x[i], 1)
    gaussianTransform_y[i] = lib.gaussianTransform(gaussianSignal_y[i], 1)

lib.affichage_rows_cols(2, 2, [x, x, x, x], [gaussianSignal_y, gaussianTransform_y, gaussianSignal_y, gaussianSignal_y], ["g(t,a) -> a = 1", "G(w, a)", "F(w)", "G(w) * F(w)"])
