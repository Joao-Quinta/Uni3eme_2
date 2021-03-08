import lib

########################## a ##########################

########################## b ##########################

z_matrix = lib.complexMatrix()

########################## c ##########################

w_matrix = lib.z_3_1(z_matrix)

########################## d ##########################

w_matrix_abs = lib.absNp(w_matrix)

# c = lib.plt.imshow(w_matrix_abs, cmap="hsv", extent=[-2, 2, -2, 2])
# lib.plt.colorbar(c)
# lib.plt.show()

########################## e ##########################

w_matrix_log_scale = lib.logScale(w_matrix_abs)

# c = lib.plt.imshow(w_matrix_log_scale, cmap="hsv", extent=[-2, 2, -2, 2])
# lib.plt.colorbar(c)
# lib.plt.show()

########################## f ##########################

x = lib.np.linspace(-2, 2, 101)

# lib.plt.plot(x, w_matrix.real)
# lib.plt.axis([-2, 2, -20, 20])
# lib.plt.show()
#
# lib.plt.plot(x, w_matrix.imag)
# lib.plt.axis([-2, 2, -20, 20])
# lib.plt.show()

########################## g ##########################

########################## h ##########################

w_matrix_abs = lib.npPhase(w_matrix)

c = lib.plt.imshow(w_matrix_abs, cmap="hsv", extent=[-2, 2, -2, 2])
lib.plt.colorbar(c)
lib.plt.show()