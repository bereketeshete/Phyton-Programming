from cs1media import *
from math import cos ,sin,tan,pi
img = load_picture("C:/programming lab/images/kara.jpg")


w, h = img.size()
a=int(raw_input("enter angle"))
d=raw_input("enter direction")
r = create_picture(w, h+3)
w, h = img.size()
for x in range(w):
   for y in range(h):
      r.set(x, y, img.get(x, y))
r.show()       

   
if d=="h":
   if a>0:
      r = create_picture(w, h+int(w*tan(a*pi/180)))
   if a<0:
      r = create_picture(w, h)
if d=="v":
   if a>0:
      r = create_picture(w+int(h*tan(a*pi/180)), h)
   if a<0:
      r = create_picture(w+int(h*tan(a*pi/180)), h)

def skew(img,d,a):
   w, h = img.size()
   if -89<int(a)<89 and (d=="v" or d=="h"):
      if d=="v":
         for x in range(w):
            for y in range(h):
               r.set(x+int((h-y)*tan(s*pi/180)), y, img.get(x, y))
               
      elif d=="h":
         for x in range(w):
            for y in range(h):
               r.set(x, y, img.get(x, y))
              
   else:
      print "wrong input!!!"
   
   
skew(img,d,a)
r.show()
#((h-y)*tan(s*pi/180))