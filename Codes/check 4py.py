def hello():
    if hubo.right_is_clear():
            turn_right()
            hubo.move()
    elif hubo.front_is_clear():
        while hubo.on_beeper():
            hubo.pick_beeper()        
        hubo.move()
    elif hubo.left_is_clear():
        while hubo.on_beeper():
            hubo.pick_beeper()        
        hubo.turn_left()
        hubo.move()
    else:
        hubo.turn_left()
        hubo.turn_left()
        hubo.turn_left()