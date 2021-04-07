from cs1robots import *

load_world(C:\Users\aspire\AppDataLocal/Temp/additional_worlds.zip/trash3.wld")

hubo = Robot ()

def turn_right():
    for i in range(3):
        hubo.turn_left()
        
hubo.turn_left()

def up():
    while hubo.front_is_clear():
        hubo.move()
    turn_right()
    
def down():
    while hubo.front_is_clear():
        hubo.move()
    hubo.turn_left()
    
while hubo.front_is_clear():
    up()
    if hubo.front_is_clear():
        hubo.move()
        turn_right()
    down()
    if hubo.front_is_clear():
        hubo.move()
        hubo.turn_left()
