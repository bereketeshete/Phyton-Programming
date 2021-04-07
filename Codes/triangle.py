
def is_triangle(x, y, z):
    if x+y>z and x+z>y and y+z>x:
        return True
    else:
        return False


x = float(raw_input("Enter x float value "))
y = float(raw_input("Enter x float value "))
z = float(raw_input("Enter x float value "))

if is_triangle(x, y, z):
    print 'YES'
else:
    print "No"



