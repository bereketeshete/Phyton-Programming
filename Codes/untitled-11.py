from cs1robots import *
load_world("C:\Python27\Lib\site-packages\PIL/worlds/harvest3.wld")
hubo=Robot()
def move_and_pick():
    hubo.move()
    if hubo.on_beeper():
            hubo.pick_beeper()    
  
    
        
for i in range(6):
    move_and_pick()
#
def left():
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    if hubo.on_beeper():
               hubo.pick_beeper()        
def turnright():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
        
def right():
    turnright()
    hubo.move()
    turnright()
    if hubo.on_beeper():
               hubo.pick_beeper()        
def move9():
    for i in range(6):
        move_and_pick()
        
def finish():
    left()
    move9()
    right()
    move9()
for i in range(4):
    finish()
    

 
