import lib
import numpy as np

###################### 3 ######################
##### a #####

x = lib.np.linspace(-10, 10, 101)
alpha = [0.1, 1, 2, 10]
yaG = []
yaGChapeau = []

for a in alpha:
    yaG.append([lib.exo3G(t, a) for t in x])
    yaGChapeau.append([lib.exo3GChapeau(w, a) for w in x])

uBound = [6.2, 1.8, 1.4, 1.1]
# for y in range(len(yaG)):
#     lib.plt.plot(x, yaG[y], color='blue')
#     lib.plt.title("G(t): alpha = " + str(alpha[y]))
#     lib.plt.xlim([-10, 10])
#     lib.plt.ylim([0, uBound[y]])
#     lib.plt.show()
#
#     lib.plt.plot(x, yaGChapeau[y], color='red')
#     lib.plt.title("G^(w): alpha = " + str(alpha[y]))
#     lib.plt.xlim([-10, 10])
#     lib.plt.ylim([0, uBound[y]])
#     lib.plt.show()

##### b #####

##### c #####
# function : lib.represent_complex_signal(x, y, title) # I added the argument title

##### d #####
# function : lib.exo3HChapeau(w)
yGChapeau = np.array([lib.exo3GChapeau(t, a=1) for t in x])
yHChapeau = np.array([lib.exo3HChapeau(t) for t in x])

lib.represent_complex_signal(x, yGChapeau, "G^(w)")
lib.represent_complex_signal(x, yHChapeau, "H^(w)")

##### e #####
# function : lib.exo3HChapeau(w)
yIChapeau = np.array([lib.exo3IChapeau(t) for t in x])

lib.represent_complex_signal(x, yIChapeau, "I^(w)")