import math

sin = math.sin
pi  = math.pi

x = raw_input("Enter a float number> ")
x = int(x)
for i in range(int(x)):
	x = int(i) / (x-1) * 2 * pi
	print sin(x)
	

