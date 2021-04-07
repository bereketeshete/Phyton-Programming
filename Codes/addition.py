from cs1robots import *
load_world("C:/Python27/Lib/site-packages/PIL/add2.wld")
hubo=Robot()

def turn_right():
    for i in range(3):
        hubo.turn_left()
hubo.turn_left()
hubo.move()
turn_right()
for i in range(6):
    hubo.move()
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0



while hubo.on_beeper():
    a=a+1
    hubo.pick_beeper()
hubo.move()
while hubo.on_beeper():
    b=b+1
    hubo.pick_beeper()
hubo.move()
while hubo.on_beeper():
    c=c+1
    hubo.pick_beeper()
hubo.move()
while hubo.on_beeper():
    d=d+1
    hubo.pick_beeper()

turn_right()
hubo.move()
turn_right()
while hubo.on_beeper():
    e=e+1
    hubo.pick_beeper()
    
if e+d < 10:
    for i in range(e+d):
        hubo.drop_beeper()
else:
    for i in range(e+d-10):
        hubo.drop_beeper()
hubo.move()
while hubo.on_beeper():
    f=f+1
    hubo.pick_beeper()
if e+d >= 10:
    for i in range(c+f+1):
        hubo.drop_beeper()
else:
    for i in range(c+f):
        hubo.drop_beeper()
hubo.move()

while hubo.on_beeper():
    g=g+1
    hubo.pick_beeper()
if b+g >= 10:
    for i in range(b+g-10):
        hubo.drop_beeper()
else:
    for i in range(b+g):
        hubo.drop_beeper()
hubo.move()
while hubo.on_beeper():
    h=h+1
    hubo.pick_beeper()
if a+h >= 10:
    for i in range(a+h-10):
        hubo.drop_beeper()
if a + h != 0 :
    for i in range(a+h+1):
        hubo.drop_beeper()
hubo.move()


