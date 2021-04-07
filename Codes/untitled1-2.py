layer()
car = Circle(70, Point(100,100))
car.setDepth(1)
car.setFillColor("red")
paper.add(car)  
import time

timeDelay = 5
time.sleep(timeDelay)

car.move(-10, 0)
time.sleep(timeDelay)

car.move(-30, 0)
time.sleep(timeDelay)

car.move(-60, 0)
time.sleep(timeDelay)

car.move(-100, 0)
time.sleep(timeDelay)





