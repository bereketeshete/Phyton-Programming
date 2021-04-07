from cs1media import *
import math
img = load_picture("C:/programming lab/images/yuna.jpg")
def luminance():
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            r = int(0.299*r)
            g = int(0.587*g) 
            b = int(0.114*b)
            p=(r+g+b)
            img.set(x, y, (p, p, p))
       

luminance()
img.show()