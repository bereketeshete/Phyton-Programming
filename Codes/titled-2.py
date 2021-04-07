from cs1robots import *

load_world("test.wld")

cnt = 0

hubo = Robot(street=1, beepers=100)

while not hubo.on_beeper():
 
 hubo.move()

while hubo.on_beeper():
 cnt += 1
 hubo.pick_beeper()

for i in range(cnt):

 hubo.drop_beeper()

while hubo.front_is_clear():

 hubo.move()

for i in range( (cnt/2)*10 ):

 hubo.drop_beeper()

hubo.turn_left()

hubo.turn_left()

for i in range( cnt ):

 hubo.move()

def a ( robot ):

 cnt = 0

 while robot.on_beeper():
  cnt = cnt + 1
  robot.pick_beeper()

 for i in range(cnt):
  robot.drop_beeper()

 return cnt