a1 = 0
a2 = 1

while b < 1000:
    b = a1+a2
    a1, a2 = a2, a1+a2
    print b