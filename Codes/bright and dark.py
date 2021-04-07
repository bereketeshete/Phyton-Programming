from cs1media import *
img = load_picture("C:/Users/aspire/Pictures/Saved Pictures/google.jpg")

def make_lighter(img, factor):
    w, h = img.size()
    for y in range(h):
        for x in range(w):
            r, g, b = img.get(x, y)
            r = int(factor * r)
            g = int(factor * g)
            b = int(factor * b)
            if r > 255: r = 255
            if g > 255: g = 255
            if b > 255: b = 255
            img.set(x, y,(r, g, b))
make_lighter(img, 0.5)          
img.show()