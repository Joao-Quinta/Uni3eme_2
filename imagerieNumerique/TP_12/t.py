def tt(x, val):
    if x == -1:
        return 1
    elif x == 0:
        return 0
    elif x == 1:
        return 2
    else:
        if x == val:
            for i in range(-1, x):
                print(x, " a appele -> ", i, " res -> ", tt(i, val))
        res = tt(x - 3, val) / (x * x - 1)
        if x == val:
            print(x, " a appele -> ", val, " res -> ", res)
        return res


tt(5, 5)
