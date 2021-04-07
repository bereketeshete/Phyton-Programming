from cs1media import *

pic = load_picture( "binary_img.bmp" )

for i in range(3) :

 count = 0

 for y in range( 6 - i*2 ) :
  for x in range( 10 - i*2 ) :
   if ( i%2 == 1 ) :
    if pic.get( x, y ) == ( 0, 0, 0 ) :
     count = count + 1
   else :
    if pic.get( x, y ) == ( 255, 255, 255 ) :
     count = count + 1
print count
