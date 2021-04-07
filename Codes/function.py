var1, var2, var3, var4  = 1, 2, 3, 5
def func1(var2, var4):
    var1  = 1
    var2  +=  0
    var3  = 1
    var4  +=  1
def func2(var1, var2):
    global var3, var4
    var1  +=  5
    var2  +=  5
    var3  /=  5
    var4  / 5
    return var1, var2
def func3(var):
    var = 15
    return var


def func4(a, b):
    var = 15
    return var

func1(var1, var3)
print var1, var2, var3, var4
var1, var2  = func2(var2, var4)
print var1, var2, var3, var4
var2  = func3(var1)
var3  = func4(func3(var3),  25)
var4  = func3(var4)
print var1, var2, var3, var4