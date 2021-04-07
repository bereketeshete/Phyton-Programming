from cs1robots import *
load_world("C:\Python27\Lib\site-packages/Maze4.wld")
hubo=Robot(orientation="E", avenue=1, street =2 , beepers =80 )
hubo.set_trace("blue")
ami=Robot("light_blue", orientation="E", avenue=7, street =2, beepers =1 )


hubo.move()
ami.drop_beeper()
def turn_right():
    for i in range(3):
        hubo.turn_left()
def follow_right_wall():
    if hubo.front_is_clear() and hubo.right_is_clear() and hubo.left_is_clear():
        turn_right()
        for i in range(3):
            hubo.drop_beeper()
        hubo.move()
    elif hubo.left_is_clear() and hubo.right_is_clear():
        hubo.drop_beeper()
        hubo.drop_beeper()
        turn_right()
        hubo.move()
       
        
    elif hubo.right_is_clear():
        turn_right()
        hubo.drop_beeper()
        hubo.move()
        while hubo.on_beeper():
            hubo.pick_beeper()
    elif hubo.front_is_clear():
        if hubo.left_is_clear():
            hubo.drop_beeper()
            hubo.drop_beeper()
            hubo.move()
        else:  
            hubo.move()
            hubo.drop_beeper()
    elif hubo.right_is_clear():
        turn_left()
        hubo.move()
        hubo.drop_beeper()
    elif hubo.left_is_clear():
        hubo.turn_left()
        hubo.move()
        hubo.drop_beeper()
        
            
    else:
        hubo.turn_left()
        hubo.turn_left()
        if hubo.right_is_clear():
            turn_right()
        else:
            if hubo.front_is_clear():
                if hubo.on_beeper():
                    hubo.pick_beeper()
                    hubo.move()
        if hubo.right_is_clear():
            turn_right()        
        while hubo.front_is_clear():
            if hubo.on_beeper():
                hubo.pick_beeper()
            if hubo.right_is_clear():
                turn_right()
            hubo.move()
            
        while hubo.on_beeper():
            hubo.pick_beeper()
        
        
   
while hubo.front_is_clear or hubo.right_is_clear() or hubo.left_is_clear():
    follow_right_wall()
    