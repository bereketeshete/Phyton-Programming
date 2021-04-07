def change_location(position,  x_move,  y_move, z_move):
  (x, y, z) =  position
  x  +=  x_move
  y  +=  y_move
  z  +=  z_move
  result =  x,  y,  z
  return result

location  =  (10, 20,  30)
location  =  change_location(location, -5,  10,  -15)
print location

