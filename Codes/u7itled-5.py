from cs1graphics import *

width = 300

height = 300

paper = Canvas(width, height, 'white', 'Flipping(1)')


flag1 = Polygon(Point(width/2, height*3/4),
   Point(width/2, height/4), Point(width/4, height/4), 

   Point(width/4, height/4+20), Point(width/4+20, 
   height/4+20), Point(width/4+20, height*3/4))

paper.add(flag1)

flag2 = flag1.clone()

flag2.flip()

paper.add(flag2)

flag2.flip()