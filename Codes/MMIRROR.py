from cs1media import *
img = load_picture("C:/Users/aspire/Pictures/Saved Pictures/google.jpg")


def mirror(img):
    w, h = img.size()
    for y in range(0,h):
        for x in range(w / 2):
            pl = img.get(x,y)
            pr = img.get(w -x -1, y)
            img.set(x, y, pr)
            img.set(w - x -1, y, pl)
mirror(img)          
img.show()