import lib

########################## a ##########################

# in pdf file

t = lib.returnLinspace(-10, 10, 201)
y05 = lib.computeSha(t, 0.5)
y1 = lib.computeSha(t, 1)
y2 = lib.computeSha(t, 2)

lib.plotScatter([[t, y05, '#1f77b4']], "T = 0.5")
lib.plotScatter([[t, y1, '#1f77b4']], "T = 1")
lib.plotScatter([[t, y2, '#1f77b4']], "T = 2")

########################## b ##########################

# in pdf file

########################## c ##########################

tb = t.copy()
tb1 = []
tb2 = []
tb05 = []
for i in range(0, len(tb)):
    tb[i] = lib.math.sin(tb[i] + (lib.math.pi / 4))
    tb1.append(tb[i] * y1[i])
    tb05.append(tb[i] * y05[i])
    tb2.append(tb[i] * y2[i])

# lib.plotScatter1([t, tb, '#1f77b4'], [t, tb05, '#ff7f0e'], "T = 0.5")
# lib.plotScatter1([t, tb, '#1f77b4'], [t, tb1, '#ff7f0e'], "T = 1")
# lib.plotScatter1([t, tb, '#1f77b4'], [t, tb2, '#ff7f0e'], "T = 2")

########################## d ##########################

tbEven = lib.even(tb)
tbOdd = lib.odd(tb)

tbEven_tbOdd = []
for i in range(0,len(tbEven)):
    tbEven_tbOdd.append(tbEven[i]+tbOdd[i])

# lib.plotScatter1([t, tb, '#1f77b4'], [t, tbEven, '#ff7f0e'], "Even signal")
# lib.plotScatter1([t, tb, '#1f77b4'], [t, tbOdd, '#ff7f0e'], "Odd signal")
# lib.plotScatter1([t, tb, '#1f77b4'], [t, tbEven_tbOdd, '#ff7f0e'], "Even + Odd signal")

########################## e ##########################

# in pdf file
