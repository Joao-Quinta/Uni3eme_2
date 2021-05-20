# matrice b ?  + c + d

import numpy as np

x = np.ones((3, 3))
y = np.pad(x, ((2, 0), (1, 0)))
print(y.shape)

print(y)
