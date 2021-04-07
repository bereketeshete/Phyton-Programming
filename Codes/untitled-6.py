from cs1robots import *
load_world("C:/Python27/Lib/site-packages/PIL/hurdles4.wld")
hubo=Robot()
def move_or_jump():
        if hubo.front_is_clear():
                hubo.move()
        if hubo.on_beeper():
                pass
        elif not hubo.front_is_clear():
                hubo.turn_left()
                hubo.move()
                for i in range(3):
                        hubo.turn_left()
                hubo.move()
                for i in range(3):
                        hubo.turn_left()  
                hubo.move()
                hubo.turn_left()
        elif not hubo.front_is_clear():
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

move_or_jump()    
    
    