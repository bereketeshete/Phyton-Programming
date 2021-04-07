from cs1graphics import *

#pin
paper = Canvas()
pin = Layer()
cir1 = Circle(10, Point(0,0))
cir1.setFillColor('red')
pin.add(cir1)
cir2 = Circle(5, Point(0, 0))
cir2.setFillColor('yellow')
pin.add(cir2)
petal1 = Ellipse(40,10)
petal1.setDepth(60)
petal1.rotate(45)
petal1.setFillColor('lightyellow')
pin.add(petal1)

petal2= petal1.clone()
petal2.rotate(90)
pin.add(petal2)
pin.moveTo(100,100)
paper.add(pin)