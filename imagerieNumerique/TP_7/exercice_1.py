import lib

# a

t = lib.returnLinspace(-10, 10, 201)
print(len(t))
y1 = lib.computeSha(t, 1)
y05 = lib.computeSha(t, 0.5)
y2 = lib.computeSha(t, 2)

# lib.plotScatter([[t, y1, '#1f77b4']])
# lib.plotScatter([[t, y05, '#1f77b4']])
# lib.plotScatter([[t, y2, '#1f77b4']])

# b

# lets assume T = 1, we want to sample the f(x) = y values such that x is not float
# since sha(1) is equal to 1 on all the x values we want, and 0 on floats, we simply multiply and get the same result

# c

tb = t.copy()
tb1 = t.copy()
tb2 = t.copy()
tb05 = t.copy()
for i in range(0, len(tb)):
    tb[i] = lib.math.sin(tb[i] + (lib.math.pi / 4))
    tb1[i] = tb[i] * y1[i]
    tb05[i] = tb[i] * y05[i]
    tb2[i] = tb[i] * y2[i]

# lib.plotScatter([[t, tb, '#1f77b4'], [t, tb05, '#ff7f0e']])
# lib.plotScatter([[t, tb, '#1f77b4'], [t, tb1, '#ff7f0e']])
# lib.plotScatter([[t, tb, '#1f77b4'], [t, tb2, '#ff7f0e']])

# d
