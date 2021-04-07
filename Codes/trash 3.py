from cs1robots import *

load_world("C:/Python27/Lib/site-packages/trash4.wld")

hubo = Robot ()

def turn_right():
    for i in range(3):
        hubo.turn_left()
        
hubo.turn_left()

def up():
    while hubo.front_is_clear():
        while hubo.on_beeper():
            hubo.pick_beeper()        
        hubo.move()
    turn_right()
    
def down(): 
    while hubo.front_is_clear():
        while hubo.on_beeper():
            hubo.pick_beeper()        
        hubo.move()
    hubo.turn_left()
while hubo.on_beeper():
    hubo.pick_beeper()
    
while hubo.front_is_clear():
    up()
    while hubo.on_beeper():
        hubo.pick_beeper()    
    if hubo.front_is_clear():
        hubo.move()
        turn_right()
    down()
    if hubo.front_is_clear():
        hubo.move()
        hubo.turn_left()
hubo.turn_left()
hubo.turn_left()
while hubo.front_is_clear():
    hubo.move()