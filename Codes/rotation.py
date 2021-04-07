from cs1graphics import *

width = 300

height = 300

paper = Canvas(width, height, 'white', "Rotating")
square1 = Square(100, Point(width/2, height/2))

square1.setFillColor('transparent')

square1.setBorderWidth(2)

paper.add(square1)

square2 = square1.clone()

square2.rotate(45)
square2.setDepth(40)

square2.setBorderWidth(1)

paper.add(square2)

square1.adjustReference(-50, 50)

square2 = square1.clone()

square2.rotate(45)