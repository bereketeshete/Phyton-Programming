from cs1robots import *
load_world("C:/Python27/Lib/site-packages/PIL/amazing2.wld")
hubo=Robot(beepers=1)

def turn_right():
    for i in range(3):
        hubo.turn_left()
        
hubo.drop_beeper()
hubo.move()

while not hubo.on_beeper():
    hubo.move()
    if hubo.right_is_clear():
        turn_right()
    elif not hubo.front_is_clear():
        hubo.turn_left()

        
        