from cs1robots import *
load_world("C:\Python27\Lib\site-packages/Maze5.wld")
hubo=Robot(orientation="E", avenue=1, street =2 , beepers =100 )
hubo.set_trace("blue")
ami=Robot(orientation="E", avenue=7, street =2, beepers =1 )
hubo.drop_beeper()
ami.drop_beeper()
hubo.move()


def turn_right():
    for i in range(3):
        hubo.turn_left()

    
        
def follow_right_wall():
    while not hubo.on_beeper():
            if hubo.right_is_clear():
                turn_right()
                hubo.drop_beeper()
                hubo.move()
            elif hubo.front_is_clear():
                hubo.drop_beeper()
                hubo.move()
            else:
                hubo.turn_left()
                while hubo.on_beeper():
                    hubo.pick_beeper()
    while hubo.on_beeper():
        if hubo.right_is_clear():
            turn_right()
            hubo.pick_beeper()
            hubo.move()
        elif hubo.front_is_clear():
            hubo.pick_beeper()
            hubo.move()
        else:
            hubo.turn_left()
            while hubo.on_beeper():
                hubo.pick_beeper()
                
    
while (hubo.front_is_clear() or hubo.right_is_clear() or hubo.left_is_clear() or \
       not hubo.on_beeper()):
    follow_right_wall()
    
       