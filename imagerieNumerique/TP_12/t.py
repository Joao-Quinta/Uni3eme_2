def t(x):
    print()
    if x == -1:
        print("x = -1",1)
        return 1
    elif x == 0:
        print("x = 0",0)
        return 0
    elif x == 1:
        print("x = 1",2)
        return 2
    else:
        temp = t(x - 3) / (x * x - 1)
        print("ici - x = ", x ," ",temp)
        return temp


l = t(5)

print(" l = ", l)
