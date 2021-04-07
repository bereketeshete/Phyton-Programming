from cs1robots import *
load_world("C:\Python27\Lib\site-packages\PIL/worlds/harvest3.wld")
hubo=Robot(beepers=36)
def move_and_drop():
    hubo.move()
    if not hubo.on_beeper():
            hubo.drop_beeper()    
  
    
        
for i in range(6):
    move_and_drop()
#
def left():
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    if not hubo.on_beeper():
               hubo.drop_beeper()        
def turnright():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()
        
def right():
    turnright()
    hubo.move()
    turnright()
    if not hubo.on_beeper():
               hubo.drop_beeper()        
def move9():
    for i in range(5):
        move_and_drop()
        
def finish():
    left()
    move9()
    right()
    move9()
for i in range(3):
    finish()
    

 
