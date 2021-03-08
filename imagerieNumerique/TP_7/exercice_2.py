import lib

########################## a ##########################

########################## b ##########################

z_matrix = lib.complexMatrix()

########################## c ##########################

w_matrix = lib.z_3_1(z_matrix)

########################## d ##########################

w_matrix_abs = lib.absNp(w_matrix)

c = lib.plt.imshow(w_matrix_abs, extent=[-2, 2, -2, 2])
lib.plt.colorbar(c)
lib.plt.show()
