l = [1,2,3,4]
for i in range(0, len(l)):
    print(l[i], l[len(l[0:i+1]) * -1])