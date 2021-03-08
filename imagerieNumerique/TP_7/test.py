import numpy as np

x = np.linspace(-2, 2, 6)
y = np.linspace(2, -2, 6)
xx, yy = np.meshgrid(x, y, sparse=True)
#
print(xx)
print(yy)
z = xx + yy*1j
print(z)
#
# for i in range(0,len(xx[0])):
#     print(xx[0][i], yy[i][0])
