from cs1robots import *
load_world("C:\Python27\Lib\site-packages/Maze4.wld")
hubo=Robot(orientation="E", avenue=1, street =2 , beepers =100 )
hubo.set_trace("blue")
ami=Robot(orientation="E", avenue=7, street =2, beepers =1 )
hubo.drop_beeper()
hubo.move()

ami.drop_beeper()
def turn_right():
    for i in range(3):
        hubo.turn_left()
        
for i in range(5):
    hubo.move()
turn_right()
hubo.move()
def follow_right_wall_or_close():
    hubo.move()
    hubo.drop_beeper()
    hubo.turn_left()
    hubo.move()
    while not hubo.on_beeper():
       
        if hubo.left_is_clear():
            hubo.drop_beeper()
            hubo.move()
            if hubo.left_is_clear():
                hubo.turn_left()
                hubo.turn_left()
                hubo.move()
                hubo.turn_left()
                hubo.turn_left()
                hubo.turn_left()
                hubo.pick_beeper()
                hubo.move()
        elif hubo.front_is_clear():
            hubo.move()
        else: turn_right()
    hubo.pick_beeper()
    hubo.turn_left()
follow_right_wall_or_close()
            
