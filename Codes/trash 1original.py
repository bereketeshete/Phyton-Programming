from cs1robots import *
load_world("C:/Python27/Lib/site-packages/PIL/trash1.wld")
hubo=Robot()

def turnright():
    for i in range(3):
        hubo.turn_left()

def move_and_pick():
    while not hubo.on_beeper():
        if hubo.front_is_clear():
            hubo.move()
    while hubo.on_beeper():
        hubo.pick_beeper()
while hubo.front_is_clear():
    move_and_pick()
hubo.turn_left()
hubo.turn_left()
while hubo.front_is_clear():
    hubo.move()
turnright()
hubo.move()
while hubo.carries_beepers():
    hubo.drop_beeper()
turnright()
turnright()
hubo.move()
hubo.turn_left()