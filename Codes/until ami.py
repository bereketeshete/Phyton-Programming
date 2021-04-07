##########################################################################
# Title : 
# Author :
# The number of hours taken for finishing the homework :
##########################################################################
from cs1robots import *

# Define functions for turning right and around
def turn_right():
    for i in range(3):
        hubo.turn_left()
        
def Hubo_turn_around():
    for i in range(2):
        hubo.turn_left()
        
def Ami_turn_right():
    for i in range(3):
        Ami.turn_left()
        
def Ami_turn_around():
    for i in range(2):
        Ami.turn_left()

load_world("Mazes/Maze4.wld")

hubo = Robot(avenue=1, street=2, color = "gray", beepers = 1000)
Ami = Robot(avenue=7, street=2, color = "purple", orientation = "S", beepers = 1)
# The positions of Hubo and Ami are fixed. 
# Modify the number of beepers if you need. 

hubo.set_trace("blue")
Ami.set_trace("purple")

hubo.drop_beeper()          # Indicate the exit of the maze
hubo.move()
Ami.drop_beeper()           # Indicate the position of Ami

while not hubo.on_beeper() or hubo.front_is_clear() or hubo.right_is_clear() or hubo.left_is_clear():
    if hubo.front_is_clear() and hubo.right_is_clear() and hubo.left_is_clear():
            turn_right()
            if not hubo.on_beeper():
                for i in range(3):
                    hubo.drop_beeper()
            hubo.move()
    elif hubo.left_is_clear() and hubo.right_is_clear():
        if not hubo.on_beeper():
            hubo.drop_beeper()
            hubo.drop_beeper()
        else:
            if hubo.on_beeper():
                hubo.pick_beeper()
                
        turn_right()
        hubo.move()
    elif hubo.front_is_clear() and hubo.right_is_clear():
        if not hubo.on_beeper():
            hubo.drop_beeper()
            hubo.drop_beeper()
        turn_right()
        hubo.move()    
       
    elif hubo.front_is_clear() and hubo.left_is_clear():
        if not hubo.on_beeper():
            hubo.drop_beeper()
            hubo.drop_beeper()
        else:
            hubo.pick_beeper()
        hubo.move()            
    elif hubo.right_is_clear():
        if not hubo.on_beeper():
            hubo.drop_beeper()
        else:
            hubo.pick_beeper()    
        turn_right()
        hubo.move()
    elif hubo.front_is_clear():
        if not hubo.on_beeper():
            hubo.drop_beeper()
        else:
            hubo.pick_beeper()
        hubo.move()
        
    elif hubo.left_is_clear():
        if not hubo.on_beeper():
            hubo.drop_beeper()
        else:
            hubo.pick_beeper()        
        hubo.turn_left()
        hubo.move()
        
            
    else :
        if hubo.on_beeper():
            hubo.pick_beeper()
        Hubo_turn_around()
        if not hubo.on_beeper():
                    hubo.drop_beeper()
        else:
            hubo.pick_beeper()           
             

    #####################################################
    ## Implement something here to find Ami            ##
    #####################################################    
    pass                    # please remove this when you implement 
    
# Ami is here. Let's go back to the exit. 
while not Hubo.front_is_clear():
    Hubo.turn_left()
while not Ami.front_is_clear():
    Ami.turn_left()    

while hubo.on_beeper():     # please modify this condition to 'not Hubo.on_beeper()' when you do not use the the indicated route. 
    #####################################################
    ## Implement something here to go back to the exit ##
    #####################################################    
    pass                    # please remove this when you implement