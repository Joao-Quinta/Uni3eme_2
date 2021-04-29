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
############ d ############
fgCirCon = np.convolve(np.tile(signalF, 2), np.tile(signalG, 2))
