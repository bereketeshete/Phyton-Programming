a1 = 0
a2 = 1
b=0
print a1
print a2
while b < 1000:
    b = a1+a2
    a1, a2 = a2, a1+a2
    if b < 1000:
        print b,