from cs1graphics import *

from time import sleep
paper = Canvas()

paper.setBackgroundColor("skyBlue")
paper.setWidth(400)
paper.setHeight(400)
paper.setTitle('animal')

animal = Layer()
animal.moveTo(200,200)
body = Ellipse(100, 20)
body.setFillColor('grey')
inside = Ellipse(50,10)
inside.setDepth(40)
inside.setFillColor('black')
animal.add(inside)

animal.add(body)
leg1 = Path(Point(10,10), Point(40, 40))
leg1.setBorderWidth(5)
animal.add(leg1)


leg2 = Path(Point(10,-10), Point(40, -40))
leg2.setBorderWidth(5)
animal.add(leg2)

body = Rectangle(70, 30, Point(0,-25))
body.setFillColor('blue')
body.setDepth(60)

paper.add(animal)
def animate():
    leg1.rotate(90)
    leg2.rotate(-90)
    sleep(0.25)
    leg1.rotate(-90)
    leg2.rotate(90)
    
    

for i in range(200):
    animal.move(1,0)
    animate()
    
    
    

