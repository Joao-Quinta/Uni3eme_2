import lib
import numpy as np

############ a ############

signalF = np.array([1, 2, 4, 8])
M = 4
# M = 4
# W_{M}^{1} = exp(-j * 2 * 1 * pi/ M) -> 2 par def, 1 -> formule -> U = ligne * col

W = np.zeros([M, M], dtype=complex)
print(W)

for i in range(M):
    for j in range(M):
        W[i][j] = lib.computeWMU(M, i * j)

F_me = lib.get_F_DFT(W, signalF)
F_numpy = np.fft.fft(signalF)
F_diff = F_me - F_numpy

############ b ############

# 1 - define a variable t
t = np.linspace(-2, 2, 101)

# 2 - define f
f = np.exp(-10 * (t ** 2))

# 3 - see 2 different plots
lib.simplePlotXY(t, f, "x = t, y = f")
lib.simplePlotY(f, "y = f")

# 4 - compute f_sym and plot
f_sym = np.roll(f, 51)
lib.simplePlotY(f_sym, "y = f_sym")

# 5 - compute F and do 4 plots
F = np.fft.fft(f_sym)
F_magnitude = lib.get_magnitude(F)
F_phase = lib.get_phase(F)
F_real = F.real
F_imag = F.imag
lib.affichage_rows_cols(2, 2, [None, None, None, None], [F_magnitude, F_phase, F_real, F_imag],
                        ["magnitude", "phase", "real", "imag"])

# 6 - compute F and plot
F = np.fft.fftshift(F)
lib.simplePlotY(F, "y = F shift")

############ c ############

# 1 - define a variable t
t = np.linspace(-2, 2, 101)

# 2 - define f
f = np.sin(t)

# 3 - see 2 different plots
lib.simplePlotXY(t, f, "x = t, y = sin(t)")
lib.simplePlotY(f, "y = sin(t)")

# 4 - compute f_sym and plot
f_sym = np.roll(f, 51)
lib.simplePlotY(f_sym, "y = f_sym")

# 5 - compute F and do 4 plots
F = np.fft.fft(f_sym)
F_magnitude = lib.get_magnitude(F)
F_phase = lib.get_phase(F)
F_real = F.real
F_imag = F.imag
lib.affichage_rows_cols(2, 2, [None, None, None, None], [F_magnitude, F_phase, F_real, F_imag],
                        ["magnitude", "phase", "real", "imag"])

# 6 - compute F and plot
F = np.fft.fftshift(F)
lib.simplePlotY(F, "y = F shift")
