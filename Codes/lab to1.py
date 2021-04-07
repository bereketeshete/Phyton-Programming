from cs1robots import *
load_world("C:/Python27/Lib/site-packages/PIL/add34.wld")
hubo=Robot()

def turn_right():
    for i in range(3):
        hubo.turn_left()

def add():
    while hubo.on_beeper():
        hubo.pick_beeper()
    hubo.move()
    while hubo.carries_beepers():
        hubo.drop_beeper()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    if not hubo.on_beeper():
            hubo.turn_left()
            hubo.turn_left()
            hubo.move()
            turn_right()
    

    
     
        
    
hubo.turn_left()
hubo.move()
turn_right()
for i in range(9):
    hubo.move()
turn_right()
add()
for i in range(3):
    if hubo.on_beeper():
        hubo.pick_beeper()
        hubo.turn_left()
        hubo.turn_left()
        hubo.move()
        while hubo.carries_beepers():
            hubo.drop_beeper()
    
turn_right()
hubo.move()
