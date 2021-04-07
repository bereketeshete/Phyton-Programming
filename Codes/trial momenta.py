from cs1graphics import *
from time import *
import random

canvas = Canvas(640,580)
canvas.setTitle("Memento")

path = "./images_6/"
names = ( "Dongyoung.jpg", "Jinyeong.jpg", "Sangjae.jpg", "Sungeun.jpg", "Suwon.jpg", "Yeongjae.jpg" )
cards = []
num_pads = []
tries = 1
correct_list = []

def initialize():    
    # initialize cards
    for i in range(6):
        for k in range(4):
            img = Image(path+names[i])
            temp_tuple = (img,names[i])
            cards.append(temp_tuple)
    
    for i in range(24):
        card = Layer()
        rect = Rectangle(90,120,Point(0,0))
        text = Text(str(i),18,Point(0,0))
        card.add(rect)
        card.add(text)
        num_pads.append(card)

    ################################################################
    
    # 2-2-1. shuffle the card list
    random.shuffle(cards)
    ################################################################


def print_cards():
    canvas.clear()
    w = 0
    h = 0
    i_w = 70
    i_h = 90
    for i in range( len(num_pads) ):
        ################################################################
        if i%2 == 0:    # 2-2-2. rewrite the condition for visualization.
        ################################################################
            cards[i][0].moveTo(i_w + w, i_h+h)
            canvas.add(cards[i][0])
        else:
            num_pads[i].moveTo(i_w + w, i_h+h)
            canvas.add(num_pads[i])
            
        w += 100
        if w % 600 == 0:
            w = 0
            h += 130
            
def is_valid(num1,num2):
    result=0
    for i in range(len(correct_list)):
        if correct_list[i] == num1 or correct_list[i] == num2:
            result = 1
    if result == 1:
        return False
    else:
        True
    
    if num1 == num2 or result == 1 or not( 0<=num1<=23 or 0<=num2<=23):
        return False
    else:
        return True
        
     
            
    
        ################################################################################################
    # 2-1-1. Check if any of two numbers exists in the current correct list,
    #        two numbers are the same, or both of the numbers are within a valid range.
    # Return Boolean value according to the result.

    ################################################################################################
    return False

def check(num1,num2):
    ################################################################################################
    for i in range( len(num_pads) ):
            ################################################################
            if True:    # 2-2-2. rewrite the condition for visualization.
            ################################################################
                cards[i][0].moveTo(i_w + w, i_h+h)
                canvas.add(cards[i][0])
            else:
                num_pads[i].moveTo(i_w + w, i_h+h)
                canvas.add(num_pads[i])    
    # 2-1-2. At first, visualize the screen including the two cards(num1-th card and num2-th card).
    #        If two pictures of the two cards are same, put two numbers into the correct list.
    #        If not, re-visualize the original screen.
    # Return Boolean value according to the result.
    
    ################################################################################################
    print_cards()
    return False
        
initialize()
print_cards()
print "### Welcome to the Python Memento game!!! ###"
################################################################################################
while True: # 2-2-3. Rewrite the condition for termination
################################################################################################
    
    ################################################################################################
    # 2-2-4. Print the number of tries and the corrected pairs    
    print str(tries) + "st try. You got " + str(len(correct_list)/2) + " pairs."
    ################################################################################################
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    if not is_valid(num1,num2):
        continue
    
    if check(num1,num2):
        print "Correct!"
    else:
        print "Wrong!"
    ################################################################################################
    # 2-2-5. Update number of tries (global variable, tries)
    ################################################################################################    