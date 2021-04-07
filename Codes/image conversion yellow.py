from cs1media import *

img = load_picture("C:/programming lab/images/yuna.jpg")

yellow=(255,255,255)
blue=(0,0,255)
green=(0,255,0)

w, h = img.size()
for y in range(h):
        for x in range(w):
                r, g, b = img.get(x, y)
                
                v = (r+g+b)//3
                if v > 200:
                        img.set(x, y, yellow)
                elif v < 100:
                        img.set(x, y, blue)
                else:
                        img.set(x, y, green)
                        


img.show()