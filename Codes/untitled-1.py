##################################################################
# Homework #3 Skeleton Code
# Student ID : 
# Name : 
##################################################################

from cs1media import * #You cannot import anything else!

def show_img(img_fname): 
    #------------------------------------------------------
    # function show_img
    # input: image file name (string)
    # output: none
    # 
    # task: (1) open the image
    #       (2) display the image
    #------------------------------------------------------

    # task (1),(2) already implemented for you :)
    img = load_picture(img_fname)
    img.show()

def adj_contrast(img_fname, k):
    
    #------------------------------------------------------
    # function adj_constrast
    # input: image file name (string)
    # output: none
    # 
    # task: (1) open the image
    #       (2) calculates the constrast adjusted pixel value
    #       (3) saves file
    #------------------------------------------------------

    #-----------------------------------------
    # do task (1), (2) from here
    #-----------------------------------------
    img = load_picture(img_fname)
    if k < 0:
        c = (100 + k) / 100 
    if k > 0:
        c = 100/(100-k)
    if -99<=k<=99:
        w, h = img.size()
        for y in range(h):
            for x in range(w):
                r, g, b = img.get(x, y)
                r=128+ c*(r-128)
                g=128+ c*(g-128)
                b=128+ c*(b-128)
                img.set(x,y,(r,g,b))
        


    # task (3) already implemented for you :) DO NOT CHANGE THIS LINE!
    final.save_as('iu_adj.jpg')

def lomo(img_fname):
    #--------------------------------------------------------------------
    # function lomo
    # input: image file name (string)
    # output: none
    #
    # task: (1) load original image and vignette image(vignette1.jpg)
    #       (2) add vignette by factor 2
    #       (3) add vignette by factor 3
    #       (4) save file
    #
    #--------------------------------------------------------------------
 
    #-----------------------------------------
    # do task (1), (2), (3) from here
    #-----------------------------------------
    inputPic = load_picture(img_fname)
    vignettePic = load_picture("vignette1.jpg")
    w, h = inputPic.size()
    addVignette(inputPic, vignettePic, w, h, 2)
    addVignette(inputPic, vignettePic, w, h, 2) 
    # task (4) already implemented for you :) DO NOT CHANGE THIS LINE!
    final.save_as('final_iu.jpg')
    
def addVignette(inputPic, vignettePic, w, h, factor):
    #---------------------------------------------------------------------------------
    # function addVignette
    # input: original image (Picture), vignette image (Picture),
    #           width (int), height (int), intensity factor (int)
    # output: new image (Picture)
    #
    # task: (1) create an empty picture
    #       (2) read corresponding pixel pairs from the two pictures
    #       (3) get new pixel color by calling getNewColorValues functions
    #       (4) assign the new pixel to the empty picture
    #
    #---------------------------------------------------------------------------------

    #-----------------------------------------
    # do task (1), (2), (3), (4) from here
    #-----------------------------------------
    new_img = create_picture(w,h)
    for y in range(h):
        for x in range(w):
            inputpixel = inputPic.get(x, y)
            vintagepixel = vignettePic.get(x, y)
            new_img.set(x,y,getNewColorValues(inputPixel, vignettePixel, factor))
    
    
def getNewColorValues(inputPixel, vignettePixel, factor):
    #---------------------------------------------------------------------------------------
    # function addVignette
    # input: pixel from the original image (tuple), pixel from the vignette image (tuple)
    # output: pixel for the new image (tuple)
    #
    # task: (1) from the two tuples, decompose into R,G,B values for each
    #       (2) calculate the new color by applying the rule,
    #           new value = old value - ( 255 % vignette value ) / 2
    #       (3) return the newly constructed RGB value 
    #
    #---------------------------------------------------------------------------------------
    
    #-----------------------------------------
    # do task (1),(2),(3) from here
    #-----------------------------------------
    R,G,B= inputPixel
    r,g,b= vignettePixel
    R= R -  ( 255 % r ) / factor
    G= G -  ( 255 % g ) / factor
    B= B -  ( 255 % b ) / factor
    return (R,G,B)    

def main():
    #----------------------------------------------------------------------------------------------
    # function main
    # input: none
    # output: none
    # task:
    #
    #       (1) If a user's input is 'q', then quit this program.
    #       (2) If a user's input is 's', then ask the name of the file, call show_img() function
    #       (3) If a user's input is 'l', then ask the name of the file, call lomo() function
    #       (4) If a user's input is 'l', then ask the name of the file, call adj_contrast() function
    #       (5) If the command is unknown, notify the user and ask the user for another input
    #
    #----------------------------------------------------------------------------------------------

    #-----------------------------------------
    # do task (1),(2),(3),(4),(5) from here
    #-----------------------------------------
    while True:
        x=raw_input("Quit(q) or adjust_contrast(a) or show(s) or lomo(l):")
        if x=="q":
            break
        elif x=="s":
            img_fname=raw_input("please type the file name including file extension , i.e sh.jpg: ")
            show_img(img_fname)
        elif x=="l":
            img_fname=raw_input("please type the file name including file extension , i.e sh.jpg: ")
            lomo(img_fname)
        elif x=="a":
            img_fname=raw_input("please type the file name including file extension , i.e sh.jpg: ")
            k=int(raw_input("please input the value of k beteween 100 and 100: "))
            adj_contrast(img_fname, k)           
        else:
            print "wrong input please input another input"
        
        
main()

