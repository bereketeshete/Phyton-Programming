from cs1graphics import *
paper = Canvas( )

head = Circle(75, Point(100,100))
head.setFillColor('yellow')
head.setDepth(60)

paper.add(head)

mouth = Circle(40, Point(100,110))

mouth.setFillColor('black')

mouth.setBorderWidth(0)

mouth.setDepth(52)
paper.add(mouth)
mouthCover = Circle(40, Point(100,100))

mouthCover.setFillColor('yellow')
mouthCover.setBorderWidth(0)
mouthCover.setDepth(51)
paper.add(mouthCover)
nose = Polygon(Point(100,90), Point(92,110), Point(108,110))
nose.setFillColor('black')
paper.add(nose)

leftEye = Circle(10, Point(70,80))
leftEye.setFillColor('black')
rightEye = Circle(10, Point(130,80))
rightEye.setFillColor('black')
paper.add(leftEye)
paper.add(rightEye)
leftEyebrow = Path(Point(60,65), Point(70,60),Point(80,65))

leftEyebrow.setBorderWidth(3)

leftEyebrow.adjustReference(10,15)
# set to center of left eyeball
leftEyebrow.rotate(-15)

paper.add(leftEyebrow)
rightEyebrow = leftEyebrow.clone( )

rightEyebrow.flip()
# still relative to eyeball center
rightEyebrow.move(60,0)
# distance between eyeball centers
paper.add(rightEyebrow)


gg = Polygon(Point(100,0),Point(105,10),Point(120,10),Point(110,20),Point(120,30),Point(100,20),Point(80,30),Point(90,20),Point(80,10),Point(95,10))
paper.add(gg)

#gg.setFillColor('Yellow')
#star = Polygon(Point(x_pos-size, y_pos-(size/2)),Point(x_pos+size/4, y_pos-size/4),Point(x_pos+size/2, y_pos-size/4),Point(x_pos+size/4, y_pos)),Point(x_pos+size/2, #y_pos+size/2),Point(x_pos, y_pos+(size/4),Point(x_pos-(size/2), y_pos+(size/2)),Point(x_pos-size/4, y_pos),Point(x_pos-size/2, y_pos-(size/4)),
 #   Point(x_pos-size/4, y_pos-(size/4)))

#########################################

#star = Polygon(Point(x_pos-size, y_pos-(size/2)),Point(x_pos+(size/4), y_pos-size/4),Point(x_pos+size/2, y_pos-size/4),Point(x_pos+size/4, y_pos)),Point(x_pos+size/2, y_pos+size/2),Point(x_pos, y_pos+(size/4),Point(x_pos-(size/2), y_pos+(size/2)),Point(x_pos-size/4, y_pos))
    #star.setFillColor('Yellow')
    #canvas.add(star)
pu = Spline(Point(100,100),Point(110,110),Point(120,100))
pu.setBorderWidth(5)
paper.add(pu)

smile = Spline(Point(x_pos-(size/8), y_pos+(size/4)),Point(x_pos, y_pos+(size/3)),Point(x_pos+(size/8), y_pos+(size/4)),)