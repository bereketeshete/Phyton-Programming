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
        
def hubo_turn_around():
    for i in range(2):
        hubo.turn_left()
        
def Ami_turn_right():
    for i in range(3):
        Ami.turn_left()
        
def Ami_turn_around():
    for i in range(2):
        Ami.turn_left()

load_world("C:\Mazes/Maze3.wld")

hubo = Robot(avenue=1, street=2, color = "gray", beepers = 1000)
Ami = Robot(avenue=7, street=2, color = "purple", orientation = "S", beepers = 1)
# The positions of Hubo and Ami are fixed. 
# Modify the number of beepers if you need. 

hubo.set_trace("blue")
Ami.set_trace("purple")

hubo.drop_beeper()          # Indicate the exit of the maze
hubo.move()
Ami.drop_beeper()           # Indicate the position of Ami

# checks the three options
while not hubo.on_beeper() or hubo.front_is_clear() or hubo.right_is_clear() or hubo.left_is_clear():
    # checks if front, right and left is clear
    if hubo.front_is_clear() and hubo.right_is_clear() and hubo.left_is_clear():
            turn_right()
            if not hubo.on_beeper():
                for i in range(3):
                    hubo.drop_beeper()
            else:
                if hubo.on_beeper():
                    hubo.pick_beeper()
            hubo.move()
    # checks if both right and left is clear
    elif hubo.left_is_clear() and hubo.right_is_clear(): #
        if not hubo.on_beeper():
            hubo.drop_beeper()
            hubo.drop_beeper()
        else:
            if hubo.on_beeper():
                hubo.pick_beeper()
               
        turn_right()
        hubo.move()
    # checks if both front and right is clear
    elif hubo.front_is_clear() and hubo.right_is_clear():
        if not hubo.on_beeper():
            hubo.drop_beeper()
            hubo.drop_beeper()
        else:
            if hubo.on_beeper():
                hubo.pick_beeper()
        turn_right()
        hubo.move()    
    # checks if front and left is clear   
    elif hubo.front_is_clear() and hubo.left_is_clear():
        if not hubo.on_beeper():
            hubo.drop_beeper()
            hubo.drop_beeper()
        else:
            hubo.pick_beeper()
        hubo.move()  
    # checks if right is clear   
    elif hubo.right_is_clear():
        if not hubo.on_beeper():
            hubo.drop_beeper()
        else:
            hubo.pick_beeper()    
        turn_right()
        hubo.move()
    # checks if front is clear  
    elif hubo.front_is_clear():
        if hubo.on_beeper():
            hubo.pick_beeper()        
        else:
            hubo.drop_beeper()
        hubo.move()
   # checks if left is clear     
    elif hubo.left_is_clear():
        if not hubo.on_beeper():
            hubo.drop_beeper()
        else:
            hubo.pick_beeper()        
        hubo.turn_left()
        hubo.move()
    # if the above conditions are not satisfied then otherwise
    else :
        if hubo.on_beeper():
            hubo.pick_beeper()
        hubo_turn_around()
        if not hubo.on_beeper():
            hubo.drop_beeper()
        else:
            hubo.pick_beeper()           
             

    #####################################################
    ## Implement something here to find Ami            ##
    #####################################################    
                      # please remove this when you implement 
 
    
# Ami is here. Let's go back to the exit. 
while not hubo.front_is_clear():
    hubo.turn_left()
while not Ami.front_is_clear():
    Ami.turn_left()    

while hubo.on_beeper():
    if hubo.right_is_clear():
        turn_right()
        hubo.move()
        if not hubo.on_beeper():
            hubo_turn_around()
            hubo.move()
            hubo.pick_beeper()
            if hubo.right_is_clear():
                turn_right()
                hubo.move()
                if hubo.on_beeper():
                    Ami.pick_beeper()
                    Ami.move()
                
                
            elif Ami.right_is_clear():
                Ami.turn_left()
                
        else:
            Ami.pick_beeper()
            Ami_turn_right()
            Ami.move()
        if not hubo.on_beeper():
            hubo_turn_around()
            hubo.move()
            hubo.pick_beeper()
            turn_right()
            hubo.move()
            Ami.turn_left()
            Ami.pick_beeper()
            Ami.move()
    elif hubo.front_is_clear():
        hubo.move()
        if hubo.on_beeper():
            Ami.pick_beeper()
            Ami.move()                      
        if not hubo.on_beeper():
            hubo_turn_around()
            hubo.move()
            
            if hubo.right_is_clear():
                turn_right()
                hubo.pick_beeper()
                if hubo.front_is_clear():
                    hubo.move()
                    Ami.turn_left()
                    Ami.pick_beeper()
                    Ami.move()
            else:
                hubo.turn_left()
                hubo.move()
                Ami_turn_right()
                Ami.pick_beeper()
                Ami.move()
                          
    elif hubo.left_is_clear():
        hubo.turn_left()
        hubo.move()
        if not hubo.on_beeper():
            hubo_turn_around()
            hubo.move()
            turn_right()
        else:
            Ami.pick_beeper()
            Ami.turn_left()
            Ami.move()
    else:
        hubo.pick_beeper()
            
    #####################################################
    ## Implement something here to go back to the exit ##
    #####################################################    
                     # please remove this when you implement