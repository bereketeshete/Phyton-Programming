from cs1robots import *
load_world("C:\Python27\Lib\site-packages/Maze5.wld")
hubo=Robot(orientation="E", avenue=1, street =2 , beepers =100 )
hubo.set_trace("blue")
ami=Robot("light_blue", orientation="E", avenue=7, street =2, beepers =1 )

hubo.drop_beeper()
hubo.move()
ami.drop_beeper()
def turn_right():
    for i in range(3):
        hubo.turn_left()
# def to turn ami to the right
def turn_righta():
    for i in range(3):
        ami.turn_left()    
        
def follow_right_wall():
    while hubo.right_is_clear():
        turn_right()
    while not hubo.on_beeper():
        if hubo.right_is_clear():
            turn_right()
            hubo.move()
        elif hubo.front_is_clear():
            hubo.move()
        else:
            hubo.turn_left()
follow_right_wall()
ami.pick_beeper()

def follow_left_wall():
    while hubo.left_is_clear():
        hubo.turn_left()
    while ami.left_is_clear():
        ami.turn_left()
    
    while not hubo.on_beeper():
        if hubo.left_is_clear():
            hubo.turn_left()
            hubo.move()
                
        elif ami.left_is_clear():
                ami.turn_left()
                ami.move()
        elif hubo.front_is_clear():
            hubo.move()
            ami.move()
       
        else :
            turn_right()
            while not hubo.front_is_clear():
                turn_right()
            turn_righta()
            while not ami.front_is_clear():
                turn_righta()
                
            
def followa_left_wall():
    while ami.left_is_clear():
        ami.turn_righta()
    while not ami.on_beeper():
        if ami.left_is_clear():
            ami.turn_left()
            ami.move()
        elif ami.front_is_clear():
            ami.move()
        else:
            turn_right()
            turn_right()
            turn_righta()


#    hubo.move()
    #ami.move()
#elif hubo.left_is_clear():
    #hubo.turn_left()
   # ami.turn_left()
#elif hubo.right_is_clear():
#    turn_left()
   # turn_righta()



#followa_left_wall()
follow_left_wall()
#while hubo.on_beeper():
    #if ami.front_is_clear():
        #ami.move()
    #if hubo.left_is_clear():
       # hubo.turn_left()
    #elif hubo.front_is_clear():
        #hubo.move()
    #else:
        #turn_right()
        
        
    
    
       
        
