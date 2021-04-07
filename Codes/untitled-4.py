from cs1graphics import *

paper = Canvas()

one = Circle(30)
one.setFillColor("red")
one.move(100,100)
paper.add(one)

two = Circle(30)
two.setFillColor("black")
two.move(100,100)
two.setDepth(0.5)
paper.add(two)