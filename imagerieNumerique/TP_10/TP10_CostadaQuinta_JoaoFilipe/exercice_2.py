import lib
import numpy as np

signalF = np.array([1, 2, 3, 4])
signalG = np.array([1, -1])

############ a ############
# by hand
############ b ############
# by hand
############ c ############
fgStrCon = np.convolve(signalF, signalG)
print(fgStrCon)
############ d ############
reps = 2
n = signalF.shape[0]
fgCirCon = np.convolve(np.tile(signalF, reps), signalG)[n:reps * n]
print(fgCirCon)
