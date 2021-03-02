import numpy as np

x = np.arange(9.).reshape(3, 3)
print(x)
y = np.where( x > 5 )
y1 = y[0]
print(y)
print(y1)