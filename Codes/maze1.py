from cs1robots import *
load_world("C:/Python27/Lib/site-packages/PIL/maze1.wld")
hubo=Robot()

def turn_right():
    for i in range(3):
        hubo.turn_left()
        
def follow_right_wall():
    while not hubo.on_beeper():
        if hubo.right_is_clear():
            turn_right()
            hubo.move()
        elif hubo.front_is_clear():
            hubo.move()
        else:
            hubo.turn_left()
follow_right_wall()