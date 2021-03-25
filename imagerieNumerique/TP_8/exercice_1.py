import lib
import numpy as np

###################### 1 ######################
##### a #####

# in pdf file

##### b #####

# in pdf file
# compute Fk by using the formula
# lets set k = 50

k = 50
ak = [lib.computeAk(i) for i in range(k)]
bk = [0 for i in range(k)]  # bk is 0 for every k
Fk = [(1 / 2 * (ak[i] - 1j*bk[i])) for i in range(k)]
print(Fk)

##### c #####

# function : lib.fTildaExo1(T)
# function : lib.computeAk(k)
# function : lib.fNemeApprox(s, t, w0)

x = lib.np.linspace(-5, 5, 101)
y = lib.fTildaExo1(x)

ak = lib.computeAk(101)

step = [0, 1, 3, 5, 10, 100]
stepT = "step = "
for s in step:
    y1 = np.array([lib.fNemeApprox(s, axeX, np.pi / 2) for axeX in x])
    lib.plt.plot(x, y)
    lib.plt.plot(x, y1)
    lib.plt.title(stepT + str(s))
    lib.plt.show()

##### d #####

# in pdf file
