a1 = 0
a2 = 1
b=0
total= [a1,a2]

while b < 1000:
    b = a1+a2
    a1, a2 = a2, a1+a2
    if b < 1000:
        total += [b]
      
print total