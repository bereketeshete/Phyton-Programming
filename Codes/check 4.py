from cs1media import *

img = load_picture("C:Users/aspire/Pictures/Saved Pictures/google.jpg")

img.show()
w, h = img.size()

for y in range(h):
    for x in range(w):
        r, g, b = img.get(x, y)
        r, g, b = 255-r, 255-g, 255-b
        img.set(x, y,(r, g, b))
img.show()