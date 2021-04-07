from cs1robots import *
load_world("C:/Python27/Lib/site-packages/PIL/trash1.wld")
hubo=Robot()


def pick():
    while hubo.on_beeper():
        hubo.pick_beeper()

def besmart():
    while not hubo.on_beeper():
        if hubo.front_is_clear():
            hubo.move()
def rotate():
    if not hubo.front_is_clear():
        for i in range(2):
            hubo.turn_left()
    
while not hubo.on_beeper():
    if hubo.front_is_clear():
        hubo.move()
while hubo.front_is_clear():
    pick()
    besmart()
    rotate()
    besmart()