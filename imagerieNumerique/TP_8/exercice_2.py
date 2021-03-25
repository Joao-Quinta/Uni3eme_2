import lib
import numpy as np

###################### 2 ######################
##### a #####

# in pdf file

##### b #####

# function : lib.hExo2(t)
# function : lib.periodicExtention(intB, intE, intBS, intES, val)

x = lib.np.linspace(-20 / 2, 20 / 2, 201)
y = lib.hExo2(x)

T = [2, 4, 8]
yA = lib.periodicExtention(x, y, T)
yA.insert(0, y)

Tl = ["h(t)", "h2(t)", "h4(t)", "h8(t)"]

for i in range(0, len(yA)):
    lib.plt.plot(x, yA[i])
    lib.plt.title(Tl[i])
    lib.plt.show()

##### c #####

##### d #####
# function : lib.hChapeauExo2(w)

T = [2, 4, 8, 50, 100]
w = lib.np.linspace(-20 / 2, 20 / 2, 201)


