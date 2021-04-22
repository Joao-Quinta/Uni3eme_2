import lib
import numpy as np


T = [1, 1.5, 2, 4]

n = 201
x = np.linspace(-5, 5, n)

y1 = np.zeros(n)
y15 = np.zeros(n)
y2 = np.zeros(n)
y4 = np.zeros(n)
y_sum = np.zeros(n)

y_all = [y1, y15, y2, y4]

periodique = True

# decalage pour T = 1
for pt in range(len(T)):
    for i in range(len(x)):
        if periodique:
            y_all[pt][i] = lib.computeHatFunctionPeriodique(x[i] - T[pt])
        else:
            y_all[pt][i] = lib.computeHatFunction(x[i] - T[pt])

# for i in range(len(x)):
#     y1[i] = lib.computeHatFunctionPeriodique(x[i] - 1)

lib.affichage_rows_cols(2, 2, [x, x, x, x], y_all, ["1", "1.5", "2", "4"])

lib.sameGraphPlot([x, x, x, x], y_all)

for i in range(len(x)):
    y_sum[i] = y_all[0][i] + y_all[1][i] + y_all[2][i] + y_all[3][i]

y_all.append(y_sum)

lib.sameGraphPlot([x, x, x, x, x], y_all)
