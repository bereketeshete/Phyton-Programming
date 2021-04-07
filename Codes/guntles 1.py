import math

sin = math.sin
pi  = math.pi

raw_f = raw_input("Enter a float number> ")
f = float(raw_f)
for i in range(int(f)):
	x = float(i) / (f-1) * 2 * pi
	print sin(x)
	



