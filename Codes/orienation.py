from cs1robots import *
create_world()

hubo=Robot(orientation="E", avenue=7, street =5 )
hubo.set_trace("blue")

hubo.turn_left()
hubo.turn_left()


while hubo.front_is_clear():
    hubo.move()
hubo.turn_left()
while hubo.front_is_clear():
    hubo.move()

hubo.turn_left()


