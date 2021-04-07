from cs1robots import *
load_world("C:/Python27/Lib/site-packages/PIL/hurdles3.wld")
hubo=Robot()
def jump_one_hurdle():
    hubo.turn_left()
    hubo.move()
    for i in range(3):
        hubo.turn_left()
    hubo.move()
    for i in range(3):
           hubo.turn_left() 
    hubo.move()
    hubo.turn_left()
    
def move_and_jump():
    if not hubo.on_beeper():
        if hubo.front_is_clear():
            hubo.move()
        else:
            jump_one_hurdle()
for i in range(9):
    move_and_jump()
            




