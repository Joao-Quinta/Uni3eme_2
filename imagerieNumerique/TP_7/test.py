import numpy as np

x = np.linspace(-2, 2, 6)
y = np.linspace(2, -2, 6)
xx, yy = np.meshgrid(x, y, sparse=True)
#
z = xx + yy * 1j
print(z)
z = (z**3)- 1
print()
print(z)
