from cs1graphics import *
paper = Canvas( )

head = Circle(75, Point(100,100))
head.setFillColor('yellow')
head.setDepth(60)

paper.add(head)

mouth = Circle(40, Point(100,110))

mouth.setFillColor('red')

mouth.setBorderWidth(0)

mouth.setDepth(52)
paper.add(mouth)
mouthCover = Circle(50, Point(100,95))

mouthCover.setFillColor('yellow')
mouthCover.setBorderWidth(0)
mouthCover.setDepth(51)
paper.add(mouthCover)


leftEye = Circle(10, Point(70,80))
leftEye.setFillColor('black')
rightEye = Circle(10, Point(130,80))
rightEye.setFillColor('black')
paper.add(leftEye)
paper.add(rightEye)



