import math

sin = math.sin
pi = math.pi

a = int(raw_input("Enter an intger "))
for i in range( a + 1):
    x = float(i) / a * 2 * pi
    y = 40 + int (40 * sin(x))
    print " "* y + "#"

    