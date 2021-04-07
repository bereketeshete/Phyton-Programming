from cs1robots import *
load_world("C:/Python27/Lib/site-packages/PIL/hurdles4.wld")
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
def jump_two_hurdle():
        hubo.turn_left()
        hubo.move()
        hubo.move()
        for i in range(3):
            hubo.turn_left()
        hubo.move()
        for i in range(3):
            hubo.turn_left() 
        hubo.move()
        hubo.move()
        hubo.turn_left()   
def jump_three_hurdle():
        hubo.turn_left()
        hubo.move()
        hubo.move()
        hubo.move()
        for i in range(3):
            hubo.turn_left()
        hubo.move()
        for i in range(3):
            hubo.turn_left() 
        hubo.move()
        hubo.move()
        hubo.move()
        hubo.turn_left() 
def jump_three_hurdle():
    hubo.turn_left()
    hubo.move()
    hubo.move()
    hubo.move()
    hubo.move()
    
    for i in range(3):
        hubo.turn_left()
    hubo.move()
    for i in range(3):
        hubo.turn_left() 
    hubo.move()
    hubo.move()
    hubo.move()
    hubo.move()
    hubo.move()
    hubo.turn_left()     


def move_and_jump():
    if not hubo.on_beeper():
        if hubo.front_is_clear():
            hubo.move()
        if not hubo.front_is_clear():
            jump_one_hurdle()
        elif not hubo.front_is_clear():
                jump_two_hurdle()     
        elif not hubo.front_is_clear():
            jump_three_hurdle()
       
      
while not hubo.on_beeper():
    move_and_jump()


