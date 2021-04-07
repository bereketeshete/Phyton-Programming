def is_zero(x):
    if x == 0:
        return True
def is_even(x):
    if x % 2 == 0:
        return True
def is_positive(x):
    if x > 0:
        return True
def print_properties(x):
    if type(x)!= int:
        print str(x) + " is not an integer number"
    elif is_zero(x):
        print str(x) + " is zero that is it."
    elif  is_positive(x) and is_even(x):
        print str(x) + " is a positive and even number."
    elif not is_positive(x) and is_even(x):
        print str(x) + " is negative and even number."
    elif is_positive(x) and not is_even(x):
        print str(x) + " is negative and odd number."
    elif not is_positive(x) and not is_even(x):
        print str(x) + " is negative and odd number."    
        
print_properties(-3)

         
        