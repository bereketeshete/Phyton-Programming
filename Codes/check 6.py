from cs1robots import *
load_world("C:\Python27\Lib\site-packages/Maze3.wld")
hubo=Robot(orientation="E", avenue=1, street =2 , beepers =120 )
hubo.set_trace("blue")
ami=Robot("light_blue", orientation="E", avenue=7, street =2, beepers =1 )


hubo.move()
ami.drop_beeper()
def turn_right():
    for i in range(3):
        hubo.turn_left()
def follow_right_wall():
    if hubo.right_is_clear():
        turn_right()
        hubo.drop_beeper()
        hubo.move()
    elif hubo.front_is_clear():
        while not hubo.on_beeper():
            while hubo.front_is_clear():
                hubo.drop_beeper()
                hubo.move()
    elif hubo.left_is_clear():
        hubo.drop_beeper()
        hubo.turn_left()
        hubo.move()
    else:
        hubo.turn_left()
        hubo.turn_left()
        
   



while hubo.front_is_clear or hubo.right_is_clear() or hubo.left_is_clear():
    follow_right_wall()
