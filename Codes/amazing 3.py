from cs1robots import *
load_world("C:/Python27/Lib/site-packages/PIL/amazing3.wld")
hubo=Robot(beepers = 2)
hubo.set_trace("blue")

def turn_right():
    for i in range(3):
        hubo.turn_left()
hubo.drop_beeper()

while not hubo.front_is_clear():
     hubo.turn_left()
hubo.move()
while not hubo.on_beeper():
    if hubo.right_is_clear():
        turn_right()
        hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
