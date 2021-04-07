from cs1robots import *
load_world("C:\Python27\Lib\site-packages\PIL/worlds/harvest4.wld")
hubo = Robot()

# to turn right

def turnright():
    for i in range(3):
        hubo.turn_left()
hubo.move()



if hubo.on_beeper():
    hubo.pick_beeper()
    hubo.move()
while not hubo.on_beeper():
    hubo.move()

while hubo.on_beeper():
    hubo.pick_beeper()
   
while hubo.on_beeper():
    hubo.pick_beeper()
    while hubo.on_beeper():
        hubo.pick_beeper()
    hubo.move()
        
while not hubo.on_beeper():
    hubo.move()
while hubo.on_beeper():
    hubo.pick_beeper()
   
while hubo.on_beeper():
    hubo.pick_beeper()
    while hubo.on_beeper():
        hubo.pick_beeper()
    hubo.move()    