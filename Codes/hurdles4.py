from cs1robots import *
load_world("C:/Python27/Lib/site-packages/PIL/hurdles4.wld")
hubo=Robot()

def turn_right():
    for i in range(3):
        hubo.turn_left()
        
while not hubo.on_beeper():
    if hubo.right_is_clear():
       turn_right()
       hubo.move()
       
    elif hubo.left_is_clear():
       hubo.turn_left()
    elif hubo.front_is_clear():
         hubo.move()
    elif not hubo.front_is_clear():
        hubo.turn_left()
        
    
    
